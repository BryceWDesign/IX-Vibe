# IX-Vibe Project Charter

**Owner/Author:** Bryce Lovell  
**Repo:** IX-Vibe  
**Document status:** Controlled (engineering-facing)  
**Purpose:** Define scope, intent, and evaluation posture for vibro-acoustic mitigation work.

---

## 1. Problem statement
Launch vehicles experience combined environments of:
- **Random vibration** from propulsion and aero coupling
- **Acoustic forcing** (liftoff, plume/acoustics, bay/fairing acoustics)
- **Shock/impulse events** (staging/separation events, pyroshock pathways, hard landings, relights)

These loads can excite structural resonance and amplify response in local hardware:
- mounts/fasteners and joint interfaces (micro-slip, loosening, fretting)
- avionics/PCBs and connectors (intermittent faults, solder fatigue)
- panel edges/frames (crack initiation / growth)
- harnesses and sensor suites (chafing, dropout, drift)

IX-Vibe exists to reduce that failure pathway by stacking:
1) broadband passive dissipation,
2) targeted mode suppression,
3) distributed sensing and verification.

---

## 2. Mission objective
Deliver an evaluation kit that enables a third-party engineering team to:
- reproduce baseline vibro-acoustic response (FRF/SRS/acoustic response)
- apply IX-Vibe mitigation modules to a representative structure
- measure before/after deltas with standard instrumentation
- decide quickly whether the concept merits deeper integration

---

## 3. Deliverable definition (v0.1 Evaluation Kit)
v0.1 is considered complete when the repo includes:
- clear scope/non-scope and non-claims
- explicit requirements and success metrics (dB, Δζ, mass/complexity bounds)
- a reference architecture tying together passive + targeted damping + sensing
- a complete, buildable BOM for a minimum prototype
- a test plan (FRF + SRS + acoustic panel response) with fixture guidance
- scripts/templates to produce consistent plots and summary tables

v0.1 does not require flight qualification or program-level integration work.
It is engineered to be falsified quickly.

---

## 4. Scope
### In scope
- vibration transmissibility reduction at targeted modes and bands
- peak response reduction under shock pathways (SRS)
- acoustic response reduction at representative panels/bays
- sensor-driven verification (measurement, not marketing)
- constrained integration assumptions consistent with aerospace practice:
  - mass management
  - thermal considerations
  - maintainability
  - fail-safe behavior (no single-point unsafe failure)

### Out of scope (explicitly)
- thermal protection system design
- propulsion reliability, combustion instability, engine-out logic
- vehicle-level flight control and GNC
- orbital radiation shielding solutions (beyond general notes)
- program management, certification, and flight qualification

---

## 5. Positioning (how this should be read)
This is not written as hype. It is written as:
- hypothesis + measurable tests + bounded claims

If you cannot measure a delta in standard tests, IX-Vibe is not validated.

---

## 6. Engineering ethics and integrity
- No “zero vibration everywhere” claims.
- No hidden assumptions.
- Failure modes are treated as first-class deliverables.

---
