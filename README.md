# IX-Vibe — Vibro-Acoustic Load Mitigation Stack (Evaluation Kit)

**Author:** Bryce Lovell  
**Status:** Evaluation / Proof-of-Concept Kit (v0.1 target)  
**License:** Evaluation-Only (internal test/build allowed; no commercial use without permission) — see `LICENSE`

---

## What problem this targets (plain English)
Launch and entry environments impose **vibration, acoustic forcing, and shock** that can excite structural resonances. Those resonances amplify local motion and transmitted loads into mounts, avionics, wiring, and panels—driving fatigue, loosening, fretting, intermittent faults, and sometimes outright structural damage.

IX-Vibe is built as a **stacked mitigation approach**:
- **Broadband attenuation** (reduce how hard the structure gets “kicked” in the first place)
- **Mode-targeted damping** (reduce the peaks that actually break things)
- **Distributed sensing + verification** (measure what changed, don’t guess)

This repo is written to be **auditable**: explicit assumptions, explicit non-claims, explicit tests, and hard success metrics.

---

## What IX-Vibe is (and is not)
### It IS:
- A **test-driven architecture** combining:
  1) passive energy dissipation (PressureX-style constrained/shear-thickening or viscoelastic inserts),
  2) targeted resonance suppression (e.g., tuned electro-mechanical damping modules),
  3) distributed sensing + go/no-go assessment (AHIS-style health monitoring).
- A **buildable evaluation kit** with a full BOM, build guidance, and measurement scripts.
- A framework meant to demonstrate **measurable reductions** in:
  - transmissibility at resonance peaks (dB),
  - shock response (SRS),
  - and/or panel acoustic response.

### It is NOT:
- A promise of “zero vibration everywhere.” Physics doesn’t work that way.
- A substitute for TPS, structural margins, propulsion reliability, or vehicle-level aero/thermal redesign.
- A “trust me” concept. If IX-Vibe can’t show deltas in standard tests, it fails.

---

## Design intent (how this reduces the pain point)
**Broadband layer intent (passive):**
- Reduce peak transmitted acceleration/strain during mixed vibration and shock environments.
- Expected impact: **material** reduction in overall response (often modest), and reduced excitation energy into dominant modes.

**Mode-targeted layer intent (resonance peaks):**
- Suppress the **worst resonance peaks** (the ones correlated with damage/faults), by increasing damping ratio and/or shifting/flattening the FRF peak.
- Expected impact: **large** reduction at targeted modes when tuned correctly (this is where “stacking” delivers most of the win).

**Truth layer intent (sensing/verification):**
- Quantify **before vs after** in FRF/SRS/acoustic tests.
- Detect onset of damage or abnormal growth in modal energy.
- Convert a violent event from “unknown condition” to **measured state**.

---

## Success metrics (what “works” means here)
IX-Vibe is considered successful if it demonstrates, with standard test methods:
- **FRF peak reduction at targeted mode(s):** measurable reduction in peak magnitude (dB) and/or increased damping ratio (Δζ)
- **SRS reduction:** measurable reduction at critical frequencies for shock events
- **Acoustic response reduction:** measurable reduction in panel/bay response under acoustic excitation
- **Mass/complexity bounds:** stays within explicitly stated mass and integration constraints

See `docs/01_Requirements_and_Metrics.md` once added.

---

## Quick start (what engineers can do with this repo)
1) Read the project charter: `docs/00_Project_Charter.md`
2) Review the architecture and limits: `docs/02_Architecture_Overview.md` and `docs/03_Failure_Modes_and_Limits.md`
3) Build the minimum prototype modules per `docs/07_Prototype_Build.md`
4) Run the measurement plan: `docs/04_Test_Plan_FRF_SRS_Acoustic.md`
5) Use the scripts in `/scripts` to generate before/after plots and summary deltas

---

## Why this repo exists (professional intent)
This is not a pitch deck. It’s an **evaluation package** designed to be falsified quickly.
If the measured deltas are meaningful under realistic constraints, IX-Vibe becomes a candidate for deeper integration work and consulting support.

**Commercial/production use requires a separate license.** Evaluation use is permitted under the terms in `LICENSE`.

---
