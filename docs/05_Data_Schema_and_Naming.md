# Data Schema and Naming (v0.1)

**Goal:** Ensure plots and claims are traceable to raw data and test configurations.

---

## 1) Folder structure (repo-ready)
Recommended structure when you start collecting data:

- `data/`
  - `raw/`               (untracked by default; local or private storage)
  - `processed/`         (optional; derived files)
  - `examples/`          (tracked; small example datasets or synthetic placeholders)
- `results/`
  - `output/`            (tables, summaries)
  - `plots/`             (figures)
- `tests/`
  - `runs/`              (tracked metadata logs; no large binaries)

---

## 2) Run ID convention
Use a run ID that is unique and human readable:

`YYYYMMDD_<stage>_<config>_<run#>`

Where:
- `<stage>` = COUPON | PANEL | SUBASSY
- `<config>` = BASELINE | TREATED_A | TREATED_B (etc.)
- `<run#>` = 01, 02, 03

Example:
- `20260122_PANEL_BASELINE_01`
- `20260122_PANEL_TREATED_A_02`

---

## 3) File naming for raw captures
Raw files should include:
- run ID
- sensor set
- acquisition type

Examples:
- `20260122_PANEL_BASELINE_01_FRF_accelsetA.csv`
- `20260122_PANEL_TREATED_A_01_SRS_accelsetA.csv`
- `20260122_PANEL_BASELINE_02_ACOUSTIC_accelsetA.csv`

---

## 4) Metadata files (required, tracked)
Each run must have:
- `tests/runs/<run_id>/metadata.yml` (from template)
- `tests/runs/<run_id>/test_log.md`  (from template)

Optional:
- photos stored separately with references in metadata (do not commit proprietary images unless intended)

---

## 5) Plot traceability rule
Every plot must specify:
- run IDs used
- raw file names used
- processing parameters used

No plot should exist without a trace line.

---

## 6) Claim traceability rule
Every quantitative claim must link to:
- the plot(s)
- the run IDs
- the raw file(s)
- the processing method used

Example acceptable claim pattern:
“Measured FRF peak reduction of 8.2 dB at 142 Hz (run IDs: 20260122_PANEL_BASELINE_01-03 vs 20260122_PANEL_TREATED_A_01-03).”

---
