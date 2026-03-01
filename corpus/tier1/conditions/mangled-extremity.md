---
id: mangled-extremity
condition: Mangled Extremity
aliases: [mangled limb, crush injury extremity, limb-threatening injury, MESS score injury]
icd10: [T14.8XXA, S88.011A, S78.011A, T07.XXXA]
esi: 1
time_to_harm:
  irreversible_injury: "< 6 hours (warm ischemia)"
  death: "< 2 hours (hemorrhagic shock, hyperkalemia)"
  optimal_intervention_window: "< 6 hours"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition, American College of Surgeons, 2018"
  - type: review
    ref: "Johansen K et al. Objective criteria accurately predict amputation following lower extremity trauma. J Trauma. 1990;30(5):568-572"
  - type: review
    ref: "Bosse MJ et al. An analysis of outcomes of reconstruction or amputation after leg-threatening injuries (LEAP study). N Engl J Med. 2002;347(24):1924-1931"
  - type: guideline
    ref: "EAST Landmark Papers: Mangled Extremity. 2023"
last_updated: "2026-03-01"
compiled_by: agent
risk_tier: A
validation:
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  schema_version: "2.0"
  provenance_links: []
---
# Mangled Extremity

## Recognition

**Definition:** Severe extremity injury with combined skeletal, soft tissue, vascular, and/or nerve damage that threatens limb viability and may require amputation.

**Mechanism:** High-energy blunt trauma (MVC, motorcycle, industrial crush, fall from height), blast injury, GSW with cavitation, farming/machinery entrapment.

**Mangled Extremity Severity Score (MESS):**

| Component | Criteria | Points |
|---|---|---|
| Skeletal/soft tissue | Low energy (stab, simple fracture) | 1 |
| | Medium energy (open/multiple fracture, dislocation) | 2 |
| | High energy (close-range GSW, crush) | 3 |
| | Very high energy (above + gross contamination) | 4 |
| Limb ischemia | Pulse reduced/absent, perfusion normal | 1 |
| | Pulseless, paresthesias, diminished cap refill | 2 |
| | Cool, paralyzed, insensate, numb | 3 |
| | (Double score if ischemia > 6 hours) | |
| Shock | SBP always > 90 | 0 |
| | Transient hypotension | 1 |
| | Persistent hypotension | 2 |
| Age | < 30 | 0 |
| | 30-50 | 1 |
| | > 50 | 2 |

**MESS ≥ 7:** Historically predicted amputation with high specificity. However, MESS should NOT be used as sole basis for amputation decision — LEAP study showed MESS poorly predicts functional outcomes.

**Presentation:**
- Severe deformity, open fracture with bone exposed
- Massive soft tissue destruction
- Absent distal pulses
- Insensate, paralyzed distal extremity
- Hemorrhagic shock
- Gross contamination (soil, debris)

## Critical Actions

| Action | Target |
|---|---|
| Hemorrhage control (tourniquet) | Immediate |
| ATLS primary survey | Immediate |
| Vascular assessment | < 15 minutes |
| Orthopedic + vascular surgery consult | < 30 minutes |
| Operative management | < 6 hours (ischemia clock) |

1. **Tourniquet** for active hemorrhage — apply proximal to injury, document time
2. **ATLS primary survey** — life over limb. Address airway, breathing, circulation first.
3. **Assess limb viability:** pulses (Doppler), sensation, motor function, capillary refill, compartment tension
4. **Large-bore IV access** and initiate massive transfusion if hemorrhagic shock
5. **Tetanus prophylaxis:** Tdap 0.5 mL IM if not current
6. **Antibiotics for open fracture:**
   - Gustilo Type I-II: cefazolin 2 g IV q8h
   - Gustilo Type III: cefazolin 2 g IV q8h + gentamicin 5 mg/kg IV q24h
   - Gross contamination (farm, water): add penicillin G 4 million units IV q4h (clostridial coverage)
7. **Do NOT irrigate wounds extensively in ED** — gross debris removal only. Formal irrigation and debridement in OR.

## Differential Diagnosis

- Isolated open fracture without vascular compromise (salvageable with less aggressive intervention)
- Vascular injury without skeletal injury (simpler repair)
- Compartment syndrome (limb viable but at risk — fasciotomy can save)
- Crush syndrome (systemic effects of rhabdomyolysis without limb mangling)
- Degloving injury (soft tissue avulsion without skeletal/vascular damage)

## Workup

- **X-rays of extremity:** Define fracture pattern, joint involvement, foreign bodies
- **CTA extremity:** If vascular status uncertain and patient stable enough for imaging
- **Doppler assessment:** Bedside pulse evaluation — compare to contralateral
- **Labs:** CBC, BMP (potassium — hyperkalemia from crush/ischemia), CK (baseline for rhabdomyolysis), lactate, type and crossmatch (6+ units), coagulation studies, ABG, myoglobin
- **Compartment pressure measurement:** If compartment syndrome suspected (Stryker needle or arterial line transducer)

## Treatment

**Hemorrhage control:**
- Tourniquet (first-line for extremity hemorrhage)
- Direct pressure, wound packing with hemostatic gauze
- Massive transfusion protocol: 1:1:1 PRBC:FFP:platelets
- TXA 1 g IV over 10 min within 3 hours of injury

**Limb salvage pathway:**
- **Vascular shunting:** Temporary intraluminal shunt restores perfusion while other injuries managed
- **External fixation:** Skeletal stabilization (external fixator) before or concurrent with vascular repair
- **Vascular repair:** Interposition vein graft or bypass (reversed saphenous vein preferred)
- **Fasciotomy:** Prophylactic four-compartment fasciotomy mandatory if ischemia > 4-6 hours
- **Soft tissue coverage:** Staged — vacuum-assisted closure initially, flap coverage later
- **Serial debridement:** Return to OR q48-72h for re-debridement until wound clean

**Amputation decision:**
- Life-threatening hemorrhage not controllable with salvage
- Complete nerve transection (posterior tibial nerve — LEAP study showed functional equivalence between salvage and amputation)
- Warm ischemia > 6-8 hours with insensate limb
- Massive contamination with multi-system injury where reconstruction poses systemic risk (sepsis, ARDS, renal failure)
- MESS ≥ 7 is a guide but NOT absolute indication — involve experienced trauma/ortho surgeon

**Damage control orthopedics:**
- Temporary external fixation
- Wound VAC
- ICU resuscitation (correct lethal triad: hypothermia, acidosis, coagulopathy)
- Return to OR in 48-72h for definitive fixation

**Crush/reperfusion syndrome management:**
- Aggressive IV crystalloid: NS or LR 1-1.5 L/hr targeting UOP > 200-300 mL/hr
- Sodium bicarbonate 150 mEq/L in D5W at 200 mL/hr (alkalinize urine pH > 6.5 to prevent myoglobin precipitation)
- Calcium gluconate 2 g IV for hyperkalemia (cardiac membrane stabilization)
- Insulin 10 units regular IV + D50 50 mL IV for hyperkalemia
- Continuous cardiac monitoring (hyperkalemia risk)
- Mannitol 1-2 g/kg IV for osmotic diuresis (if adequate UOP)

## Disposition

- **ICU:** All mangled extremity injuries
- **OR emergent:** Hemorrhage control, vascular repair, fasciotomy
- **Multidisciplinary team:** Trauma surgery, orthopedic surgery, vascular surgery, plastic surgery
- **Transfer:** Level I trauma center with microsurgical capability if limb salvage considered
- **Rehabilitation planning:** Early consultation even in acute phase (OT/PT, prosthetics if amputation)
- **Serial OR trips:** Planned re-debridement at 48-72 hour intervals

## Pitfalls

1. **Using MESS score as sole basis for amputation.** The LEAP study showed MESS poorly predicts functional outcomes. Scoring systems should guide, not dictate, the salvage vs. amputation decision. An experienced reconstructive surgeon should be involved.

2. **Spending excessive time on limb salvage in a dying patient.** Life over limb. If the patient has hemorrhagic shock, severe TBI, or other life-threatening injuries, damage control amputation may be the faster, safer option.

3. **Not performing prophylactic fasciotomy after prolonged ischemia.** Reperfusion of a mangled, ischemic extremity without fasciotomy causes compartment syndrome. Fasciotomy is mandatory after > 4-6 hours of ischemia or combined arterial + venous injury.

4. **Inadequate antibiotic coverage for contaminated open fractures.** Gustilo Type III fractures require broader coverage (cefazolin + gentamicin; add penicillin for soil/farm contamination). Delay in antibiotics increases infection and amputation rates.

5. **Failing to monitor for systemic reperfusion effects.** Release of a tourniquet or reperfusion of a mangled limb can cause lethal hyperkalemia, metabolic acidosis, and myoglobinuric renal failure. Preemptive treatment (IV fluids, bicarbonate, calcium) is essential.

6. **Delaying the amputation decision indefinitely.** Multiple failed salvage attempts increase sepsis, organ failure, and mortality. If salvage criteria are clearly not met, early amputation with good functional rehabilitation provides better outcomes than a painful, non-functional limb after years of reconstruction.
