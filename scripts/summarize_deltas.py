"""
IX-Vibe delta summarizer (v0.1)

Purpose:
- Load baseline and treated FRF curves
- Identify dominant peaks (treated vs baseline)
- Report peak deltas in dB (or linear if dB cannot be inferred safely)

This script is conservative. It does not claim causality, only measured deltas.

Usage example:
python scripts/summarize_deltas.py \
  --baseline data/examples/frf_baseline.csv \
  --treated data/examples/frf_treated.csv \
  --out results/output/frf_delta_summary.csv
"""

from __future__ import annotations

import argparse
import os
from typing import Tuple

import numpy as np
import pandas as pd
from scipy.signal import find_peaks

from common_io import ensure_dir, read_spectrum_csv


def _to_db(val: np.ndarray) -> Tuple[np.ndarray, bool]:
    # If values include negatives, assume user may already be in dB or signed; do not transform.
    if np.nanmin(val) < 0:
        return val, False
    v_safe = np.maximum(np.abs(val), 1e-12)
    return 20.0 * np.log10(v_safe), True


def _dominant_peaks(freq: np.ndarray, val: np.ndarray, n: int, prominence: float) -> pd.DataFrame:
    peaks, props = find_peaks(val, prominence=prominence)
    rows = []
    for i, idx in enumerate(peaks):
        rows.append(
            {
                "rank": i + 1,
                "peak_freq_hz": float(freq[idx]),
                "peak_value": float(val[idx]),
                "prominence": float(props["prominences"][i]),
            }
        )
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    return df.sort_values("peak_value", ascending=False).head(n).reset_index(drop=True)


def main() -> None:
    ap = argparse.ArgumentParser(description="Summarize peak deltas between baseline and treated curves.")
    ap.add_argument("--baseline", required=True, help="Baseline CSV")
    ap.add_argument("--treated", required=True, help="Treated CSV")
    ap.add_argument("--out", default="results/output/frf_delta_summary.csv", help="Output CSV summary")
    ap.add_argument("--top_n", type=int, default=5, help="Number of dominant peaks to summarize")
    ap.add_argument("--prominence", type=float, default=0.0, help="Peak prominence threshold (data units)")
    args = ap.parse_args()

    fb, vb, _ = read_spectrum_csv(args.baseline)
    ft, vt, _ = read_spectrum_csv(args.treated)

    # Interpolate to common grid (baseline grid)
    f = fb.to_numpy()
    vbv = vb.to_numpy()
    vtv = np.interp(f, ft.to_numpy(), vt.to_numpy())

    vb_db, base_db_mode = _to_db(vbv)
    vt_db, treat_db_mode = _to_db(vtv)

    # If one is dB-mode and the other isn't, keep linear to avoid mismatched units
    if base_db_mode != treat_db_mode:
        vb_u = vbv
        vt_u = vtv
        units = "linear"
    else:
        vb_u = vb_db if base_db_mode else vbv
        vt_u = vt_db if treat_db_mode else vtv
        units = "dB" if base_db_mode else "linear"

    peaks_b = _dominant_peaks(f, vb_u, args.top_n, args.prominence)
    peaks_t = _dominant_peaks(f, vt_u, args.top_n, args.prominence)

    # Match treated response at baseline peak frequencies (closest point)
    summary_rows = []
    for _, row in peaks_b.iterrows():
        f0 = float(row["peak_freq_hz"])
        idx = int(np.argmin(np.abs(f - f0)))
        b_val = float(vb_u[idx])
        t_val = float(vt_u[idx])
        delta = t_val - b_val
        delta_pct = (t_val / b_val - 1.0) * 100.0 if b_val != 0 else np.nan
        summary_rows.append(
            {
                "peak_freq_hz": f0,
                "baseline_value": b_val,
                "treated_value": t_val,
                "delta_treated_minus_baseline": delta,
                "delta_percent": delta_pct,
                "units": units,
            }
        )

    out_df = pd.DataFrame(summary_rows).sort_values("peak_freq_hz")
    ensure_dir(os.path.dirname(args.out))
    out_df.to_csv(args.out, index=False)

    print(f"[IX-Vibe] Wrote delta summary: {args.out}")
    print(f"[IX-Vibe] Units: {units}")


if __name__ == "__main__":
    main()
