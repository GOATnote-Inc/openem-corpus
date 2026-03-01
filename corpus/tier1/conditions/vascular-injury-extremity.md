---
id: vascular-injury-extremity
condition: Vascular Injury of Extremity
aliases: [extremity vascular injury, arterial injury extremity, peripheral vascular trauma, traumatic arterial occlusion]
icd10: [S45.001A, S45.011A, S55.001A, S55.011A, S75.001A, S75.011A, S85.001A, S85.011A]
esi: 1
time_to_harm:
  irreversible_injury: "< 6 hours (warm ischemia)"
  death: "< 2 hours (exsanguination)"
  optimal_intervention_window: "< 6 hours (limb salvage)"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition, American College of Surgeons, 2018"
  - type: guideline
    ref: "EAST Practice Management Guideline: Evaluation and Management of Penetrating Lower Extremity Arterial Trauma. Fox N et al. J Trauma Acute Care Surg. 2012;73(5 Suppl 4):S315-S320"
  - type: guideline
    ref: "Western Trauma Association Algorithm: Evaluation and Management of Peripheral Vascular Injury. 2023"
  - type: review
    ref: "Feliciano DV. Peripheral Vascular Injury. In: Mattox KL, Moore EE, Feliciano DV, eds. Trauma. 9th ed. McGraw-Hill; 2021"
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
# Vascular Injury of Extremity

## Recognition

**Mechanism:** Penetrating (stab, GSW — most common cause), blunt (fracture-dislocation, crush), iatrogenic (catheterization). Popliteal artery most vulnerable to blunt mechanism (knee dislocation). Brachial artery vulnerable at supracondylar fractures.

**Hard signs (mandate immediate surgery — no imaging needed):**
- Pulsatile external hemorrhage (active arterial bleeding)
- Expanding or pulsatile hematoma
- Absent distal pulses (with no other explanation)
- Signs of distal ischemia (6 P's): Pain, Pallor, Pulselessness, Poikilothermia (cold), Paresthesias, Paralysis
- Bruit or thrill over wound

**Soft signs (require further evaluation/imaging):**
- Non-expanding hematoma near a vessel
- History of hemorrhage (controlled by EMS/bystander)
- Proximity of wound to major vessel
- Diminished (not absent) pulse compared to contralateral
- Peripheral nerve deficit (adjacent nerve injury suggests vessel injury)
- Ankle-Brachial Index (ABI) < 0.9

**ABI measurement:** ABI < 0.9 in trauma = abnormal, warrants CTA. ABI ≥ 0.9 has > 95% NPV for significant arterial injury.

## Critical Actions

| Action | Target |
|---|---|
| Direct pressure / tourniquet | Immediate (hemorrhage control) |
| Vascular surgery consult | < 30 minutes |
| CTA (if soft signs only) | < 60 minutes |
| Operative repair | < 6 hours from injury (ischemia clock) |

1. **Control hemorrhage immediately:**
   - Direct pressure (first-line)
   - Tourniquet if pressure fails (apply proximal to injury, note time of application). Safe for up to 2 hours; can extend to 6 hours in extremis.
   - Foley catheter balloon tamponade for junctional/groin wounds
   - Do NOT clamp blindly — risks adjacent nerve injury
2. **Assess pulses and ABI** — compare to contralateral extremity
3. **Hard signs → immediate OR** (no imaging delay)
4. **Soft signs → CTA** (sensitivity/specificity > 95% for clinically significant injury)
5. **Splint fractures in anatomic alignment** — reduces continued vascular injury from bone fragments
6. **Heparin** for confirmed arterial occlusion without active hemorrhage: heparin 80 units/kg IV bolus (consider risks in polytrauma)

## Differential Diagnosis

- Compartment syndrome (pain with passive stretch, tense compartment — may coexist)
- Arterial spasm (temporary, resolves; difficult to distinguish from intimal injury)
- Venous injury alone (hemorrhage without ischemia)
- Pre-existing peripheral arterial disease (chronic absent pulses — obtain history)
- Nerve injury without vascular injury (motor/sensory deficit but normal pulses)
- Arteriovenous fistula (traumatic — bruit, thrill, late presentation)

## Workup

- **ABI:** Rapid bedside assessment. ABI < 0.9 = abnormal. Must be measured bilaterally.
- **CTA extremity:** Gold standard for non-emergent assessment (soft signs, ABI 0.5-0.9). Identifies: occlusion, intimal flap, pseudoaneurysm, AV fistula, active extravasation.
- **Doppler ultrasound:** Alternative if CTA not immediately available; operator-dependent.
- **Conventional angiography:** Rarely needed emergently; reserved for therapeutic embolization or unclear CTA.
- **Labs:** CBC, BMP (watch potassium — reperfusion), coagulation studies, type and crossmatch, lactate, CK (baseline and serial for rhabdomyolysis after reperfusion)
- **X-rays:** Identify fractures associated with vascular injury (knee dislocation → popliteal; supracondylar humerus → brachial)

## Treatment

**Hemorrhage control:**
- Direct pressure → tourniquet if failing
- Wound packing with hemostatic gauze (combat gauze/QuikClot) for junctional wounds
- Tourniquet time > 6 hours: anticipate reperfusion syndrome — pre-treat with calcium gluconate 2 g IV, sodium bicarbonate 50 mEq IV, and prepare for hyperkalemia

**Temporary shunting:**
- Javid or Argyle shunt for damage control when definitive repair will be delayed
- Restores flow while addressing other life-threatening injuries
- Shunts can maintain patency for 24-48 hours

**Definitive repair (within 6 hours of warm ischemia):**
- **Primary repair:** Lateral arteriorrhaphy for small lacerations (< 50% circumference)
- **Patch angioplasty:** Saphenous vein patch for larger defects
- **Interposition graft:** Reversed saphenous vein graft (gold standard for conduit) for segmental defects. PTFE graft if no autologous vein available.
- **End-to-end anastomosis:** If < 2 cm gap after debridement and mobilization
- **Venous repair:** Lateral venorrhaphy for accessible major veins (femoral, popliteal). Ligation acceptable for most veins except popliteal (ligation increases amputation risk).

**Fasciotomy:**
- Prophylactic fasciotomy strongly recommended for: ischemia > 4-6 hours, combined arterial + venous injury, massive soft tissue injury, compartment pressures > 30 mmHg
- Four-compartment fasciotomy of the leg (anterior, lateral, superficial posterior, deep posterior)
- Volar and dorsal compartment release for forearm

**Post-reperfusion management:**
- Monitor for reperfusion syndrome: hyperkalemia (treat with calcium gluconate 1-2 g IV, insulin 10 units + D50 1 amp IV, kayexalate), metabolic acidosis, myoglobinuria
- Aggressive IV hydration: LR or NS at 200-300 mL/hr to maintain UOP > 1 mL/kg/hr
- Serial CK levels: > 5000 indicates significant rhabdomyolysis risk
- Anticoagulation post-repair: heparin drip or enoxaparin 30 mg SQ q12h (balance with bleeding risk from other injuries)

## Disposition

- **ICU:** All major arterial repairs, bilateral injuries, reperfusion syndrome, fasciotomy
- **OR emergent:** Hard signs of vascular injury
- **Vascular surgery consult:** All confirmed or suspected vascular injuries
- **Orthopedic surgery co-management:** Concurrent fractures (sequence: vascular repair → fracture fixation, or temporary shunt → fixation → definitive repair)
- **Serial pulse checks:** q1-2h for 24 hours post-repair (Doppler if palpation difficult)
- **Transfer:** Level I/II trauma center with vascular surgery if not available — do NOT delay transfer to obtain imaging if hard signs present

## Pitfalls

1. **Delaying surgery for imaging with hard signs.** Hard signs of vascular injury (active hemorrhage, absent pulses, expanding hematoma) require immediate operative exploration. CTA delays reperfusion.

2. **Failing to check ABI.** A normal-feeling pulse can mask a partial arterial injury. ABI < 0.9 is abnormal and warrants CTA. Takes 2 minutes to perform.

3. **Ignoring the 6-hour warm ischemia clock.** Skeletal muscle tolerates 4-6 hours of warm ischemia before irreversible injury. After 6 hours, amputation risk rises dramatically. Fasciotomy is mandatory after prolonged ischemia.

4. **Not performing prophylactic fasciotomy after prolonged ischemia.** Reperfusion of ischemic muscle causes edema and compartment syndrome. Prophylactic fasciotomy is needed for ischemia > 4-6 hours, combined arterial and venous injury, or massive swelling.

5. **Missing popliteal artery injury with knee dislocation.** Even if the knee spontaneously reduces before arrival, popliteal artery injury occurs in 20-40% of knee dislocations. CTA is mandatory for all knee dislocations regardless of pulse status.

6. **Tourniquet time mismanagement.** Leaving a tourniquet on > 2 hours without reassessment or converting to definitive control increases limb loss. Document tourniquet application time and reassess at 2 hours.

7. **Ligating the popliteal vein.** Unlike most veins, popliteal vein ligation significantly increases amputation rate. Repair the popliteal vein when possible.
