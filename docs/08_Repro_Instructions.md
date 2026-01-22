# Repro Instructions (v0.1)

**Owner/Author:** Bryce Lovell  
**Purpose:** Make the evaluation workflow executable by a third-party engineering team with minimal back-and-forth.

This document does not claim flight qualification. It exists to make the **measurement and deltas** reproducible.

---

## 1) What you should be able to do with v0.1
A test team should be able to:
1) establish a baseline FRF (and optionally SRS/acoustic response)
2) apply one or more IX-Vibe modules (Module A/B/D, with Module C instrumentation)
3) re-measure using identical settings
4) generate plots and delta tables
5) report results using bounded language and traceability

---

## 2) Environment setup (analysis scripts)
### Option A — Python venv (recommended)
1) Create and activate a virtual environment:
- macOS/Linux:
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`
- Windows:
  - `python -m venv .venv`
  - `.venv\Scripts\activate`

2) Install dependencies:
- `pip install -r requirements.txt`

---

## 3) Data expectations (no “special format” lock-in)
The scripts accept generic CSV curves with:
- a frequency column (Hz)
- a magnitude/response column

Common column names are auto-detected (see `scripts/common_io.py`):
- frequency: `freq_hz`, `frequency_hz`, `frequency`, `freq`
- value: `mag`, `magnitude`, `value`, `resp`, `response`, `srs`, `srs_g`, `g`

If your tools output different names, the scripts attempt a numeric-column fallback.

---

## 4) Run metadata discipline (non-negotiable)
For each run ID:
- create `tests/runs/<RUN_ID>/metadata.yml` from `templates/test_run_metadata.yml`
- create `tests/runs/<RUN_ID>/test_log.md` from `templates/test_log.md`

This is what prevents “looks good” plots from turning into “unreviewable” plots.

---

## 5) Generate FRF baseline vs treated plots
Example command (replace file paths and run IDs):

```bash
python scripts/plot_frf.py \
  --baseline "path/to/20260122_PANEL_BASELINE_01_FRF.csv,path/to/20260122_PANEL_BASELINE_02_FRF.csv,path/to/20260122_PANEL_BASELINE_03_FRF.csv" \
  --treated  "path/to/20260122_PANEL_TREATED_A_01_FRF.csv,path/to/20260122_PANEL_TREATED_A_02_FRF.csv,path/to/20260122_PANEL_TREATED_A_03_FRF.csv" \
  --run_ids_baseline "20260122_PANEL_BASELINE_01,20260122_PANEL_BASELINE_02,20260122_PANEL_BASELINE_03" \
  --run_ids_treated  "20260122_PANEL_TREATED_A_01,20260122_PANEL_TREATED_A_02,20260122_PANEL_TREATED_A_03" \
  --title "IX-Vibe FRF: Panel Baseline vs Treated_A" \
  --outdir "results/plots" \
  --outfile "frf_panel_baseline_vs_treatedA.png" \
  --peaks_outfile "results/output/frf_panel_peaks.csv"
