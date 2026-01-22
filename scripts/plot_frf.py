"""
IX-Vibe FRF plotting utility (v0.1)

Inputs:
- One or more baseline CSVs
- One or more treated CSVs

Expected CSV columns (any of these are OK):
- frequency: freq_hz / frequency_hz / frequency / freq
- magnitude/value: mag / magnitude / value / resp / response

Output:
- A plot (PNG) with traceability text
- A peak table (CSV) with detected peaks for baseline and treated

Notes:
- We do NOT hardcode colors or styling.
- We prioritize traceability and repeatability over prettiness.
"""

from __future__ import annotations

import argparse
import os
from typing import List, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

from common_io import TraceInfo, ensure_dir, parse_csv_list, parse_run_ids, read_spectrum_csv, trace_line


def _aggregate_spectra(files: List[str]) -> Tuple[np.ndarray, np.ndarray]:
    """
    Load multiple spectra and aggregate by interpolating onto a common frequency grid.

    Assumptions:
- Each file is a (freq, value) curve.
- Frequency ranges overlap reasonably.

    Output:
- freq_common
- mean_value across files
    """
    spectra = []
    for f in files:
        freq, val, _ = read_spectrum_csv(f)
        spectra.append((freq.to_numpy(), val.to_numpy()))

    # Build common grid from intersection range, using baseline file #1 resolution as reference
    f0 = spectra[0][0]
    f_min = max(s[0].min() for s in spectra)
    f_max = min(s[0].max() for s in spectra)
    if f_max <= f_min:
        raise ValueError("Spectra frequency ranges do not overlap sufficiently for aggregation.")

    # Use median step of first spectrum as grid step (robust to small irregularities)
    step = np.median(np.diff(f0))
    if not np.isfinite(step) or step <= 0:
        step = (f_max - f_min) / 2000.0  # fallback grid

    freq_common = np.arange(f_min, f_max, step)
    vals_interp = []
    for fx, vx in spectra:
        vals_interp.append(np.interp(freq_common, fx, vx))
    mean_val = np.mean(np.vstack(vals_interp), axis=0)
    return freq_common, mean_val


def _detect_peaks(freq: np.ndarray, val: np.ndarray, prominence: float) -> pd.DataFrame:
    peaks, props = find_peaks(val, prominence=prominence)
    rows = []
    for idx in peaks:
        rows.append(
            {
                "peak_freq_hz": float(freq[idx]),
                "peak_value": float(val[idx]),
                "prominence": float(props["prominences"][list(peaks).index(idx)]),
            }
        )
    return pd.DataFrame(rows).sort_values("peak_value", ascending=False)


def main() -> None:
    ap = argparse.ArgumentParser(description="Plot FRF baseline vs treated with traceability.")
    ap.add_argument("--baseline", required=True, help="Comma-separated baseline CSV files")
    ap.add_argument("--treated", required=True, help="Comma-separated treated CSV files")
    ap.add_argument("--run_ids_baseline", default="", help="Comma-separated baseline run IDs")
    ap.add_argument("--run_ids_treated", default="", help="Comma-separated treated run IDs")
    ap.add_argument("--title", default="IX-Vibe FRF Baseline vs Treated", help="Plot title")
    ap.add_argument("--outdir", default="results/plots", help="Output directory for plots")
    ap.add_argument("--outfile", default="frf_baseline_vs_treated.png", help="Output plot filename")
    ap.add_argument("--peaks_outfile", default="results/output/frf_peaks.csv", help="Output peaks table CSV")
    ap.add_argument("--peak_prominence", type=float, default=0.0, help="Peak prominence threshold in data units")
    ap.add_argument("--log_y", action="store_true", help="Use log scale on Y axis if appropriate")
    args = ap.parse_args()

    baseline_files = list(parse_csv_list(args.baseline))
    treated_files = list(parse_csv_list(args.treated))

    freq_b, val_b = _aggregate_spectra(baseline_files)
    freq_t, val_t = _aggregate_spectra(treated_files)

    # Convert to dB if values look like linear magnitude; if user already provides dB, keep as-is.
    # Heuristic: if values are mostly positive and max/min ratio is large, dB is useful.
    def to_db(v: np.ndarray) -> np.ndarray:
        v_safe = np.maximum(np.abs(v), 1e-12)
        return 20.0 * np.log10(v_safe)

    use_db = True
    if np.nanmin(val_b) < 0 or np.nanmin(val_t) < 0:
        # negative values suggest already-in-dB or signed response; keep linear
        use_db = False

    yb = to_db(val_b) if use_db else val_b
    yt = to_db(val_t) if use_db else val_t
    y_label = "Magnitude (dB)" if use_db else "Magnitude (linear)"

    # Peaks
    peaks_b = _detect_peaks(freq_b, yb, prominence=args.peak_prominence)
    peaks_b["config"] = "baseline"
    peaks_t = _detect_peaks(freq_t, yt, prominence=args.peak_prominence)
    peaks_t["config"] = "treated"
    peaks = pd.concat([peaks_b, peaks_t], ignore_index=True)

    ensure_dir(args.outdir)
    ensure_dir(os.path.dirname(args.peaks_outfile))

    # Plot
    plt.figure()
    plt.plot(freq_b, yb, label="Baseline (mean)")
    plt.plot(freq_t, yt, label="Treated (mean)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel(y_label)
    plt.title(args.title)
    plt.legend()

    if args.log_y and not use_db:
        plt.yscale("log")

    # Traceability footer
    trace_b = TraceInfo(run_ids=parse_run_ids(args.run_ids_baseline), raw_files=baseline_files)
    trace_t = TraceInfo(run_ids=parse_run_ids(args.run_ids_treated), raw_files=treated_files)
    footer = f"BASELINE: {trace_line(trace_b)}\nTREATED: {trace_line(trace_t)}"
    plt.gcf().text(0.01, 0.01, footer, fontsize=8, va="bottom")

    outpath = os.path.join(args.outdir, args.outfile)
    plt.tight_layout()
    plt.savefig(outpath, dpi=200)
    plt.close()

    peaks.to_csv(args.peaks_outfile, index=False)

    print(f"[IX-Vibe] Wrote plot: {outpath}")
    print(f"[IX-Vibe] Wrote peaks: {args.peaks_outfile}")
    print(f"[IX-Vibe] Note: dB mode = {use_db}")


if __name__ == "__main__":
    main()
