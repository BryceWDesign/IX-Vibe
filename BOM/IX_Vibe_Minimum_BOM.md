# IX-Vibe Minimum BOM (v0.1 Evaluation Kit)

**Author:** Bryce Lovell  
**Intent:** This BOM is written as a **spec-based minimum** so a test team can source equivalent parts without being locked to specific vendors.

If you substitute components, that is acceptable — but the substitution must meet or exceed the stated specs and be documented in test metadata.

---

## 1) What this minimum BOM enables
With the minimum BOM, an engineering team can:
- build a representative coupon/panel test article,
- measure baseline FRF,
- apply IX-Vibe treatment modules,
- re-measure FRF and quantify deltas,
- optionally run SRS and acoustic response checks if equipment is available.

This is the fastest credible pathway to validating whether IX-Vibe materially reduces resonance peaks and transmitted response.

---

## 2) BOM philosophy (why spec-based)
Aerospace teams and labs differ in:
- available DAQ systems,
- preferred sensors,
- fixture standards,
- internal approved materials lists.

Therefore, IX-Vibe uses spec-based requirements to preserve:
- test repeatability,
- traceability,
- and integration realism.

---

## 3) How to use this BOM
1) Start with a **panel** test article (Stage B) unless you need a rapid Stage A coupon falsification first.
2) Instrument at minimum 3 accelerometer locations:
   - input-adjacent
   - sensitive interface location
   - far-field control point
3) Implement the stack in layers:
   - Layer A: CLD patches and/or STF/fluidic cartridge modules
   - Layer B: piezo shunt (targeted mode) and/or TMD module
   - Layer C: optional strain/PVDF truth sensors
4) Run the test plan in `docs/04_Test_Plan_FRF_SRS_Acoustic.md`
5) Record every run using templates in `/templates`

---

## 4) Notes on the “stacking effect”
The credible “stacking” approach is:
- Broadband measures reduce the energy injected into resonant modes
- Targeted measures reduce the peak amplification at the critical modes

That combination is what converts “some improvement” into “meaningful mitigation” in the only way aerospace teams will accept:
- measured FRF peak reduction (dB)
- repeatability across runs
- documented trade-offs (mass, mode shifts)

---

## 5) What this BOM does NOT imply
- It does not imply qualification for flight environments.
- It does not imply universal vibration cancellation.
- It does imply a disciplined path to measure and quantify whether IX-Vibe meaningfully reduces the resonance-driven risk pathway.

---
