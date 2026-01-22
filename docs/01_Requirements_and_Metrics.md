# Requirements and Success Metrics (v0.1)

**Goal:** Define what “success” means in testable terms.

---

## 1. Primary performance requirements (measured)
### R1 — FRF peak reduction at targeted mode(s)
- **Metric:** FRF magnitude reduction at resonance peak(s) in dB  
- **Test:** Modal/FRF measurement on representative structure (coupon → panel → subassembly)
- **Success criteria (v0.1 target):**
  - At least **6 dB** reduction at one targeted dominant peak
  - And/or measurable increase in damping ratio (**Δζ**) at that mode

> Note: 6 dB corresponds roughly to halving response amplitude at the peak.

### R2 — Shock response reduction (SRS)
- **Metric:** reduction in Shock Response Spectrum magnitude at critical frequencies  
- **Test:** Controlled impulse/shock input and measured SRS at sensitive locations
- **Success criteria (v0.1 target):**
  - Demonstrate a **measurable SRS reduction** at one or more critical bands without unacceptable mass/complexity penalty

### R3 — Acoustic response reduction (panel/bay)
- **Metric:** reduction in panel acceleration/strain response under acoustic excitation  
- **Test:** Acoustic excitation (speaker array / reverberant-like setup where available) with accelerometer/strain capture
- **Success criteria (v0.1 target):**
  - Demonstrate **measurable response reduction** in at least one representative configuration

---

## 2. Secondary requirements (integration realism)
### R4 — Mass and packaging discipline
- **Metric:** added mass per treated area or per treated interface
- **v0.1 expectation:** document mass accounting and placement rationale; no “blanket coating” assumptions

### R5 — Maintainability and inspectability
- **Metric:** time and steps to remove/replace modules or sensors
- **v0.1 expectation:** include service procedure notes and failure-safe behaviors

### R6 — Environmental bounds (declared, not assumed)
- **Metric:** documented operating limits (temperature, humidity, aging assumptions)
- **v0.1 expectation:** define what is tested vs what is assumed; do not imply qualification

---

## 3. Measurement integrity requirements
### R7 — Repeatability
- **Metric:** repeated runs showing consistent deltas
- **v0.1 expectation:** minimum of 3 repeated measurements for baseline and treated configurations

### R8 — Data traceability
- **Metric:** each plot links to raw data file(s), test configuration, and calibration info
- **v0.1 expectation:** enforce a consistent naming and metadata scheme

---

## 4. “Works” language (how to communicate results)
Acceptable statements:
- “Measured FRF peak reduction of X dB at Y Hz on configuration Z.”
- “Measured Δζ increase from A to B at the dominant mode.”
- “Observed SRS reduction of X% in band [f1, f2] under test condition Z.”

Unacceptable statements:
- “Negates all vibration.”
- “Guaranteed flight protection.”
- “Solves resonance universally.”

---

## 5. Acceptance gate for v0.1 release
v0.1 is acceptable if it provides:
- complete requirements + metrics
- architecture + failure modes
- minimum BOM + build notes
- complete test plan + scripts/templates

Data can be added later, but the system must be test-ready.

---
