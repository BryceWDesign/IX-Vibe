# Scripts (v0.1)

This folder will contain small, auditable utilities to:
- parse FRF / SRS / acoustic datasets
- generate standardized plots (baseline vs treated)
- output peak tables and delta summaries
- enforce traceability (run IDs → raw files → plots)

v0.1 requirement:
- scripts must be reproducible, minimal-dependency, and clearly documented
- every plot must embed run IDs and raw file references

Planned scripts (to be added):
- `plot_frf.py`
- `plot_srs.py`
- `plot_acoustic.py`
- `summarize_deltas.py`

No scripts are included in this commit yet—this is the interface contract.

---
