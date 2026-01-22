# Test Plan — FRF / SRS / Acoustic Response (v0.1)

**Objective:** Produce defensible before/after evidence of vibro-acoustic mitigation using standard measurements.

This plan is written to be executable on a small lab setup first (coupon/panel), then scaled to a subassembly.

---

## 0) Safety and control posture
- All testing must follow your lab safety procedures.
- Treat all impulse/shock tests as hazards (flying fixtures, loose masses, cable whip).
- If any mitigation module can detach, it is unsafe by definition—fix that before testing.

---

## 1) Test progression (minimum path)
### Stage A — Coupon (fast falsification)
Purpose: validate material/module coupling and repeatability quickly.

Configuration:
- small beam or plate coupon with a known boundary condition
- mount repeatably to a fixture (document torque and contact condition)

Measurements:
- baseline FRF
- treated FRF
- repeat 3x each configuration

### Stage B — Panel / Frame segment (realistic response)
Purpose: capture panel/bay-like behavior and multi-mode response.

Configuration:
- representative plate with stiffeners or frame segment
- controlled boundary conditions (document exactly)

Measurements:
- baseline FRF and optional acoustic response
- treated FRF and optional acoustic response
- repeat 3x

### Stage C — Subassembly (integration realism)
Purpose: validate at an interface of interest (ring/mount/bay segment).

Configuration:
- representative subassembly with at least one sensitive mounting location

Measurements:
- baseline FRF / SRS (if shock relevant) / acoustic response (if feasible)
- treated FRF / SRS / acoustic response
- repeat 3x

---

## 2) Instrumentation (minimum viable)
### Sensors
- **Accelerometers:** at least 3 locations; tri-ax where possible
- **Optional strain:** strain gauges or PVDF film on high-strain regions

### Acquisition
- sample rate: >= 10x highest frequency of interest (with anti-aliasing)
- record sensor calibration/serials
- document mounting method (wax, stud, adhesive) and cable strain relief

### Excitation sources
- **FRF:** instrumented impact hammer or shaker (preferred)
- **SRS:** controlled impulse (hammer, drop, or prescribed shock source)
- **Acoustic response:** speaker excitation or equivalent; document SPL and geometry

---

## 3) Sensor placement (practical guidance)
Minimum measurement set:
- Point 1: near the primary excitation input boundary
- Point 2: at a “sensitive” mount/interface location (where mitigation is intended)
- Point 3: a far-field location to detect unintended amplification elsewhere

If the structure has known modal hotspots, place sensors near:
- stiffener transitions
- panel edges
- mount bosses
- connector/harness supports (if represented)

---

## 4) FRF procedure (baseline then treated)
### Step-by-step
1) Photograph and document configuration, boundary conditions, and torque values.
2) Verify sensor mounting and cable management.
3) Acquire baseline FRF:
   - perform N hits or sweeps (document N, averaging method)
   - compute FRF magnitude/phase
4) Apply IX-Vibe module(s) as prescribed:
   - document exact placement (photos + dimensions)
   - document added mass and attachment method
5) Acquire treated FRF with identical settings.
6) Repeat baseline and treated runs at least **3 times** each.

### Deliverables
- FRF plots (magnitude vs frequency) baseline vs treated
- peak table: frequency, magnitude (dB), estimated damping ratio (ζ) if computed
- delta summary (dB at peak, Δζ, any shifted resonances)

---

## 5) Shock procedure (SRS)
### Step-by-step
1) Establish baseline:
   - apply shock input with controlled setup
   - capture response at sensitive location(s)
   - compute SRS (document method and damping assumption)
2) Apply treatment.
3) Repeat shock and compute SRS.
4) Minimum 3 runs each configuration.

### Deliverables
- SRS plots baseline vs treated
- band deltas at critical frequencies
- note any increased response elsewhere

---

## 6) Acoustic response procedure (panel/bay)
### Step-by-step (minimum viable)
1) Define geometry:
   - distance and placement of speakers
   - SPL measurement position and value
2) Baseline response:
   - capture acceleration/strain under acoustic excitation
3) Apply treatment.
4) Treated response:
   - identical SPL and geometry
5) Minimum 3 runs each configuration.

### Deliverables
- response PSD/spectrum plots baseline vs treated
- summary deltas in relevant bands

---

## 7) Acceptance checks (what counts as “works”)
IX-Vibe “works” in v0.1 terms if you can show:
- at least one dominant FRF peak reduced by **>= 6 dB** OR a clear Δζ increase,
- and results are repeatable (3 runs) without unsafe side effects,
- and any trade-offs (mass, shifted modes) are explicitly documented.

---

## 8) Required metadata (no exceptions)
Every test run must include:
- date/time, operator, environment (temp)
- fixture/boundary conditions + torque values
- sensor types/serials + mounting method
- acquisition settings (sample rate, filtering)
- excitation method and parameters
- treatment configuration and placement details

Use the templates in `/templates`.

---
