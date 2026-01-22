"""
IX-Vibe SRS plotting utility (v0.1)

Inputs:
- One or more baseline SRS CSVs
- One or more treated SRS CSVs

Expected CSV columns:
- frequency: freq_hz / frequency_hz / frequency / freq
- SRS value: srs / srs_g / value / magnitude / resp / response

Outputs:
- PNG plot with traceability footer
- CSV summary of band deltas (optional coarse bands)

This script is intentionally conservative: it plots, and computes simple deltas.
"""

from __future__ import annotations

import argparse
import os
from typing import List, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from common_io import TraceInfo, ensure_dir, parse_csv_list, parse_run_ids, read_spectrum_csv, trace_line


def _aggregate(files: List[str]) -> Tuple[np.ndarray, np.ndarray]:
    spectra = []
    for f in files:
        freq, val, _ = read_spectrum_csv(f)
        spectra.append((freq.to_numpy(), val.to_numpy()))

    f_min = max(s[0].min() for s in spectra)
    f_max = min(s[0].max() for s in spectra)
    if f_max <= f_min:
        raise ValueError("SRS frequency ranges do not overlap sufficiently for aggregation.")

    f0 = spectra[0][0]
    step = np.median(np.diff(f0))
    if not np.isfinite(step) or step <= 0:
        step = (f_max - f_min) / 2000.0

    f_common = np.arange(f_min, f_max, step)
    vals = [np.interp(f_common, fx, vx) for fx, vx in spectra]
    mean_val = np.mean(np.vstack(vals), axis=0)
    return f_common, mean_val


def _band_table(freq: np.ndarray, base: np.ndarray, treat: np.ndarray, bands: List[Tuple[float, float]]) -> pd.DataFrame:
    rows = []
    for f1, f2 in bands:
        mask = (freq >= f1) & (freq < f2)
        if not np.any(mask):
            continue
        b = float(np.max(base[mask]))
        t = float(np.max(treat[mask]))
        delta = t - b
        delta_pct = (t / b - 1.0) * 100.0 if b != 0 else np.nan
        rows.append(
            {
                "band_hz": f"{f1:g}-{f2:g}",
                "baseline_peak": b,
                "treated_peak": t,
                "delta": delta,
                "delta_percent": delta_pct,
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    ap = argparse.ArgumentParser(description="Plot SRS baseline vs treated with traceability.")
    ap.add_argument("--baseline", required=True, help="Comma-separated baseline SRS CSV files")
    ap.add_argument("--treated", required=True, help="Comma-separated treated SRS CSV files")
    ap.add_argument("--run_ids_baseline", default="", help="Comma-separated baseline run IDs")
    ap.add_argument("--run_ids_treated", default="", help="Comma-separated treated run IDs")
    ap.add_argument("--title", default="IX-Vibe SRS Baseline vs Treated", help="Plot title")
    ap.add_argument("--outdir", default="results/plots", help="Output directory")
    ap.add_argument("--outfile", default="srs_baseline_vs_treated.png", help="Output plot filename")
    ap.add_argument("--bands_outfile", default="results/output/srs_band_deltas.csv", help="Output band deltas CSV")
    ap.add_argument("--bands", default="20-100,100-500,500-2000,2000-5000", help="Comma bands f1-f2")
    args = ap.parse_args()

    baseline_files = list(parse_csv_list(args.baseline))
    treated_files = list(parse_csv_list(args.treated))

    fb, vb = _aggregate(baseline_files)
    ft, vt = _aggregate(treated_files)

    # Match frequency grid if slight differences
    f_min = max(fb.min(), ft.min())
    f_max = min(fb.max(), ft.max())
    mask_b = (fb >= f_min) & (fb <= f_max)
    mask_t = (ft >= f_min) & (ft <= f_max)
    f_common = fb[mask_b]
    vb2 = vb[mask_b]
    vt2 = np.interp(f_common, ft[mask_t], vt[mask_t])

    ensure_dir(args.outdir)
    ensure_dir(os.path.dirname(args.bands_outfile))

    plt.figure()
    plt.plot(f_common, vb2, label="Baseline (mean)")
    plt.plot(f_common, vt2, label="Treated (mean)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("SRS (units as provided)")
    plt.title(args.title)
    plt.legend()
    plt.yscale("log")  # SRS commonly spans orders of magnitude

    trace_b = TraceInfo(run_ids=parse_run_ids(args.run_ids_baseline), raw_files=baseline_files)
    trace_t = TraceInfo(run_ids=parse_run_ids(args.run_ids_treated), raw_files=treated_files)
    footer = f"BASELINE: {trace_line(trace_b)}\nTREATED: {trace_line(trace_t)}"
    plt.gcf().text(0.01, 0.01, footer, fontsize=8, va="bottom")

    outpath = os.path.join(args.outdir, args.outfile)
    plt.tight_layout()
    plt.savefig(outpath, dpi=200)
    plt.close()

    # Band deltas
    bands = []
    for seg in args.bands.split(","):
        seg = seg.strip()
        if not seg:
            continue
        f1s, f2s = seg.split("-")
        bands.append((float(f1s), float(f2s)))

    table = _band_table(f_common, vb2, vt2, bands)
    table.to_csv(args.bands_outfile, index=False)

    print(f"[IX-Vibe] Wrote plot: {outpath}")
    print(f"[IX-Vibe] Wrote band deltas: {args.bands_outfile}")


if __name__ == "__main__":
    main()
