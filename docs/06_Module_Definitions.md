# Module Definitions (v0.1)

This document defines the minimum set of IX-Vibe modules and how they are intended to be used in tests.

---

## Module A — Broadband Dissipation Patch Set (CLD / Passive)
**Purpose:** Convert vibration energy into heat across a broad frequency range.

**Implementation options:**
- CLD patches applied to panel regions with high strain energy
- Passive interface inserts at mounts/rings

**Placement rule (serious, not arbitrary):**
- place where modal strain energy concentrates (near stiffener transitions, panel edges, mount bosses)
- confirm with baseline FRF + (if possible) simple mode shape inference from multi-point accelerometers

**Pass/Fail evidence:**
- measurable reduction in overall response and/or reduced excitation into dominant modes (may be modest)
- no delamination or unsafe detachment under test

---

## Module B — Targeted Peak Suppression (Tuned Damping)
### B1 — Piezo + Shunt Network
**Purpose:** Increase damping at one or more dominant resonance peaks.

**Implementation concept:**
- Bond PZT patches to regions with strong modal strain for the targeted mode
- Attach a tuned shunt network to dissipate energy electrically

**Tuning rule:**
- tune based on measured baseline FRF peak frequency
- verify that tuning reduces the peak and does not create a new amplification elsewhere

**Pass/Fail evidence:**
- FRF peak reduction in dB at the targeted mode(s)
- repeatable across 3 runs

### B2 — Tuned Mass Damper (TMD) / Inertial Module
**Purpose:** Provide passive peak reduction at a specific mode via mass-spring-damper behavior.

**Implementation concept:**
- A secured mass block coupled with a compliant element and damping element
- Mounted at an interface or region that strongly participates in the targeted mode

**Pass/Fail evidence:**
- FRF peak reduction at targeted frequency
- no unsafe retention issues (mass must be positively retained)

---

## Module C — Truth Layer (Sensing + Verification)
**Purpose:** Make IX-Vibe measurable and auditable.

**Minimum sensor set:**
- 3 accelerometers (preferred tri-ax)
- optional strain/PVDF for high-strain correlation

**Pass/Fail evidence:**
- repeatable baseline measurements
- traceable plots and metadata
- multi-point confirmation (no single sensor cherry-picking)

---

## Module D — Sealed Fluidic Impedance Cartridge (Optional)
**Purpose:** Add a pressure-stable, serviceable passive damping element that can be tuned.

**Concept borrowed from pressure-compensated housings:**
- seal integrity + compliance element (small bladder/accumulator) stabilizes behavior across thermal expansion and pressure changes

**Use cases:**
- interface insert between fixture and test article
- edge-mounted cartridge on a panel boundary
- mount-adjacent cartridge near sensitive components

**Pass/Fail evidence:**
- measurable transmissibility reduction in a defined band
- stable behavior across repeated runs and temperature notes

---

## Integration posture (how to talk about it professionally)
Use bounded language:
- “This module set aims to reduce resonance peak amplification by increasing damping and reducing transmissibility.”
- “Validation is measured via FRF/SRS/acoustic response deltas under controlled conditions.”

Do not use absolute claims:
- “negates vibration entirely”
- “guarantees flight safety”

---
