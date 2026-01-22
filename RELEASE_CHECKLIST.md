# IX-Vibe Release Checklist (v0.1)

**Owner/Author:** Bryce Lovell  
**Purpose:** Ensure v0.1 is a clean evaluation kit that aerospace engineers can review without friction.

---

## A) Repo clarity (no hype / no ambiguity)
- [ ] README states scope, non-scope, and non-claims clearly
- [ ] Requirements define success in measurable terms (FRF/SRS/acoustic)
- [ ] Failure modes + limits documented
- [ ] Glossary included for consistent language

Files:
- `README.md`
- `docs/00_Project_Charter.md`
- `docs/01_Requirements_and_Metrics.md`
- `docs/03_Failure_Modes_and_Limits.md`
- `docs/99_Glossary.md`

---

## B) Testability (engineers can run it)
- [ ] FRF test plan exists and is executable
- [ ] SRS and acoustic plans are included as optional paths
- [ ] Repeatability requirements included (>= 3 runs baseline and treated)
- [ ] Metadata and test log templates included

Files:
- `docs/04_Test_Plan_FRF_SRS_Acoustic.md`
- `docs/05_Data_Schema_and_Naming.md`
- `templates/test_run_metadata.yml`
- `templates/test_log.md`
- `templates/analysis_summary.md`

---

## C) Buildability (minimum prototype path)
- [ ] Minimum BOM included (spec-based)
- [ ] Module definitions define what “A/B/C/D” means
- [ ] Prototype build path explains baseline → stack → re-test
- [ ] Explicitly avoids “blanket coating” assumptions

Files:
- `BOM/IX_Vibe_Minimum_BOM.csv`
- `BOM/IX_Vibe_Minimum_BOM.md`
- `docs/06_Module_Definitions.md`
- `docs/07_Prototype_Build.md`

---

## D) Analysis reproducibility (plots + deltas)
- [ ] Scripts exist for FRF plot + peak table
- [ ] Scripts exist for SRS plot + band deltas
- [ ] Scripts exist for acoustic plot
- [ ] Scripts embed traceability (run IDs + raw files)
- [ ] `requirements.txt` exists

Files:
- `requirements.txt`
- `scripts/common_io.py`
- `scripts/plot_frf.py`
- `scripts/plot_srs.py`
- `scripts/plot_acoustic.py`
- `scripts/summarize_deltas.py`
- `docs/08_Repro_Instructions.md`

---

## E) Licensing posture (evaluation-only)
- [ ] Evaluation-only license included and consistent with README
- [ ] Contributing rules prevent hype / unverifiable claims
- [ ] SECURITY.md included (basic hygiene)

Files:
- `LICENSE`
- `CONTRIBUTING.md`
- `SECURITY.md`

---

## F) Final v0.1 release notes (when tagging)
When you tag `v0.1`:
- State this is an **evaluation kit**.
- State what tests are supported (FRF/SRS/acoustic).
- State what “success” means (e.g., >=6 dB at a targeted peak, repeatable).
- State what data is included (if any) and what is expected from evaluators.
- Invite contact for deeper integration/licensing.

---

## G) Stop conditions (credibility protection)
If any are true, do not overstate results:
- only one run
- inconsistent fixture conditions
- sensor mounting changed between runs
- cable strain artifacts
- treatment detuned between runs
- any unsafe retention condition

---
