# Prototype Build (v0.1 Reference)

**Goal:** Provide a reference build that a lab team can reproduce quickly to validate IX-Vibe modules.

This build is intentionally simple and does not assume specialized aerospace tooling.

---

## 1) Reference test article (Panel)
**Recommended baseline panel:**
- Material: Aluminum 6061-T6 (or equivalent)
- Size: ~500 mm x 500 mm (adjustable)
- Thickness: 3–6 mm
- Optional: 2 stiffeners to create multi-mode behavior (document geometry)

**Why this works:**
- big enough to show meaningful modes in an accessible band
- small enough for bench testing and repeatable fixturing

---

## 2) Fixture concept (repeatability matters)
- Use a rigid frame to clamp one edge or two edges (pick one and document it).
- Record torque values and contact condition.
- Use consistent clamp pads/material to avoid drift.

Repeatability is not optional. If the fixture changes, the FRF changes.

---

## 3) Minimum instrumentation setup
- Accelerometer 1: near excitation input boundary
- Accelerometer 2: near “sensitive” region (where mitigation is intended)
- Accelerometer 3: far-field control point (detect unintended amplification)

Cable strain relief must be applied. Loose cables create false peaks.

---

## 4) Build steps (baseline → stack)
### Step A — Baseline build
1) Build panel and fixture
2) Install sensors
3) Capture baseline FRF (3 runs minimum)

### Step B — Add Module A (broadband)
1) Apply CLD patches to two regions near strain hotspots (start conservative)
2) Re-run FRF (3 runs)
3) Record mass added and exact placement

### Step C — Add Module B (targeted mode suppression)
1) Identify the dominant resonance peak from baseline FRF
2) Place piezo patches in a region that participates strongly in that mode
3) Tune shunt network to the measured peak frequency
4) Re-run FRF (3 runs)
5) Confirm peak reduction and check for new amplified peaks

### Step D — Add Module B2 (optional TMD)
1) If a dominant peak remains problematic, mount a secured TMD near a high-participation region
2) Re-run FRF (3 runs)
3) Confirm retention safety and repeatability

### Step E — Add Module D (optional sealed fluidic cartridge)
1) Install cartridge at a mount/interface location (not blanket coating)
2) Re-run FRF and (if relevant) a shock test for SRS deltas

---

## 5) What to publish as “proof” (engineer standard)
To avoid eye-rolls, publish:
- Baseline vs treated FRF plots with run IDs
- Peak table with dB deltas and any frequency shifts
- A short bounded summary using `templates/analysis_summary.md`
- Mass added and placement photos/diagrams (as allowed)

Avoid:
- claims without plots
- single-run “wins”
- hand-wavy language

---

## 6) Next-step escalation (subassembly)
Once the panel shows measurable deltas, move to:
- a ring/adapter segment mock
- a mount frame mock
- a bay panel mock

Use the same test structure and traceability rules.

---
