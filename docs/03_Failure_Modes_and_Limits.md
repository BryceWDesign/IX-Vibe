# Failure Modes and Limits (Read This First)

IX-Vibe is designed for measurable mitigation, not magic. This document lists how it can fail.

---

## 1. Core limits
### L1 — No universal “vibration negation”
You cannot eliminate all vibration in all directions across all frequencies and mission phases.
You can only:
- dissipate energy
- detune/shunt specific modes
- reduce transmissibility at sensitive interfaces

### L2 — Shifting a mode can create a new problem
Increasing stiffness or adding mass can shift resonances:
- away from one sensitive band
- into another band that matters
This must be measured and controlled.

### L3 — Local improvement does not imply global improvement
Treating one interface may reduce response locally but increase it elsewhere.
Acceptance requires measurements at multiple points.

---

## 2. Passive material failure modes (CLD / STF / viscoelastic)
- temperature dependence (softening/stiffening changes damping)
- aging, outgassing, moisture ingress (depending on material choice)
- delamination at bondline under cycling
- creep/relaxation leading to drift in performance
- contamination or manufacturing defects affecting shear behavior

Mitigation:
- document operating temperature band
- design for serviceability/replacement
- perform repeatability tests and environmental sweeps where feasible

---

## 3. Mode-targeted damping failure modes (piezo shunt / TMD / fluidic cartridges)
- detuning due to temperature or tolerance drift
- insufficient coupling to the mode (wrong placement)
- added mass at wrong location increasing response
- electrical failure in shunt networks (for piezo-based damping)
- leakage or seal failure in fluidic cartridges

Mitigation:
- tune using measured FRF, not assumed models
- place modules where modal strain energy is highest
- design fail-safe: module failure should degrade gracefully, not amplify loads

---

## 4. Sensing/verification failure modes (AHIS lane)
- sensor drift and calibration issues
- mounting artifacts (adhesive, cable strain, mass loading)
- aliasing or poor sampling leading to misleading spectra
- “false confidence” from sparse measurement points

Mitigation:
- calibrate, document sampling, repeat measurements
- include a minimum sensor placement strategy
- use consistent fixturing and cable management

---

## 5. Safety and “do no harm”
IX-Vibe must not introduce:
- single-point unsafe failures
- unexpected structural weak points
- trapped moisture/contamination paths
- maintenance barriers that hide damage

---

## 6. Bottom line
If IX-Vibe can’t demonstrate measured improvements in FRF/SRS/acoustic response
under declared constraints, it is not validated.

---
