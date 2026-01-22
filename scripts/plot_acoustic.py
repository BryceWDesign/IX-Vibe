"""
IX-Vibe acoustic response plotting utility (v0.1)

Inputs:
- One or more baseline acoustic-response CSVs (accel/strain spectrum or PSD-derived)
- One or more treated acoustic-response CSVs

Expected CSV columns:
- frequency: freq_hz / frequency_hz / frequency / freq
- response: resp / response / value / magnitude / mag

Outputs:
- PNG plot with traceability footer

This is intentionally generic: acoustic test rigs vary widely. The key is traceability.
"""

from __future__ import annotations

import argparse
import os
from typing import List, Tuple

import numpy as np
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
        raise ValueError("Acoustic spectra frequency ranges do not overlap sufficiently for aggregation.")

    f0 = spectra[0][0]
    step = np.median(np.diff(f0))
    if not np.isfinite(step) or step <= 0:
        step = (f_max - f_min) / 2000.0

    f_common = np.arange(f_min, f_max, step)
    vals = [np.interp(f_common, fx, vx) for fx, vx in spectra]
    mean_val = np.mean(np.vstack(vals), axis=0)
    return f_common, mean_val


def main() -> None:
    ap = argparse.ArgumentParser(description="Plot acoustic response baseline vs treated with traceability.")
    ap.add_argument("--baseline", required=True, help="Comma-separated baseline CSV files")
    ap.add_argument("--treated", required=True, help="Comma-separated treated CSV files")
    ap.add_argument("--run_ids_baseline", default="", help="Comma-separated baseline run IDs")
    ap.add_argument("--run_ids_treated", default="", help="Comma-separated treated run IDs")
    ap.add_argument("--title", default="IX-Vibe Acoustic Response Baseline vs Treated", help="Plot title")
    ap.add_argument("--outdir", default="results/plots", help="Output directory")
    ap.add_argument("--outfile", default="acoustic_baseline_vs_treated.png", help="Output plot filename")
    ap.add_argument("--log_y", action="store_true", help="Use log scale on Y axis")
    args = ap.parse_args()

    baseline_files = list(parse_csv_list(args.baseline))
    treated_files = list(parse_csv_list(args.treated))

    fb, vb = _aggregate(baseline_files)
    ft, vt = _aggregate(treated_files)

    f_min = max(fb.min(), ft.min())
    f_max = min(fb.max(), ft.max())
    mask_b = (fb >= f_min) & (fb <= f_max)
    mask_t = (ft >= f_min) & (ft <= f_max)

    f_common = fb[mask_b]
    vb2 = vb[mask_b]
    vt2 = np.interp(f_common, ft[mask_t], vt[mask_t])

    ensure_dir(args.outdir)

    plt.figure()
    plt.plot(f_common, vb2, label="Baseline (mean)")
    plt.plot(f_common, vt2, label="Treated (mean)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Response (units as provided)")
    plt.title(args.title)
    plt.legend()

    if args.log_y:
        plt.yscale("log")

    trace_b = TraceInfo(run_ids=parse_run_ids(args.run_ids_baseline), raw_files=baseline_files)
    trace_t = TraceInfo(run_ids=parse_run_ids(args.run_ids_treated), raw_files=treated_files)
    footer = f"BASELINE: {trace_line(trace_b)}\nTREATED: {trace_line(trace_t)}"
    plt.gcf().text(0.01, 0.01, footer, fontsize=8, va="bottom")

    outpath = os.path.join(args.outdir, args.outfile)
    plt.tight_layout()
    plt.savefig(outpath, dpi=200)
    plt.close()

    print(f"[IX-Vibe] Wrote plot: {outpath}")


if __name__ == "__main__":
    main()
