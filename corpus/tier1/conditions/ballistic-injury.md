---
id: ballistic-injury
condition: Ballistic Injury (Gunshot Wound)
aliases: [gunshot wound, GSW, penetrating ballistic trauma, bullet wound, firearm injury]
icd10: [T14.8XXA, W34.00XA, W33.00XA, X95.9XXA]
esi: 1
time_to_harm:
  irreversible_injury: "minutes"
  death: "< 30 minutes (torso/head)"
  optimal_intervention_window: "< 15 minutes (hemorrhage control)"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition, American College of Surgeons, 2018"
  - type: guideline
    ref: "Western Trauma Association Critical Decisions in Trauma. 2023"
  - type: review
    ref: "Stefanopoulos PK et al. Gunshot Wounds: Ballistics, Pathology, and Treatment Recommendations. Orthop Rev. 2022;14(3):38135"
  - type: guideline
    ref: "Hartford Consensus: THREAT response for active shooter events. 2015"
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
# Ballistic Injury (Gunshot Wound)

## Recognition

**Mechanism:** Firearm discharge — handgun, rifle, shotgun. Injury severity depends on kinetic energy (KE = 1/2 mv^2), projectile design, and tissue density.

**Ballistic wound characteristics:**
- **Low-velocity (< 600 m/s):** Handguns — permanent cavity only, limited tissue destruction beyond direct path. Most civilian GSWs.
- **High-velocity (> 600 m/s):** Military rifles — permanent + temporary cavitation, extensive tissue destruction 10-20x bullet diameter. Associated with greater energy transfer, cavitation, and fragment dispersal.
- **Shotgun:** Severity depends on range. Close-range (< 3 meters) = devastating; distant = superficial pellet wounds.

**Wound assessment:**
- Count all wounds — every wound is either entrance or exit until proven otherwise
- Entrance wounds: round/oval, marginal abrasion ring, may have soot/stippling (close range)
- Exit wounds: typically larger, irregular, stellate — no abrasion ring
- Do NOT assume bullet trajectory from entrance/exit locations (bullets ricochet off bone, change direction)
- Assume all body cavities in the path are penetrated

**Anatomic zones of concern:**
- **Head:** GCS on arrival is the strongest prognostic indicator. GCS 3-5 with bilateral fixed dilated pupils = near-universal mortality.
- **Neck:** Zone I (clavicle to cricoid), Zone II (cricoid to angle of mandible), Zone III (angle of mandible to skull base)
- **Torso:** Precordial box (nipple to nipple, clavicles to xiphoid) — cardiac injury. Thoracoabdominal (nipple/scapular tip to costal margin) — diaphragm/abdominal violation.
- **Extremity:** Vascular injury, compartment syndrome, fractures

## Critical Actions

| Action | Target |
|---|---|
| Hemorrhage control | Immediate |
| ATLS primary survey | Immediate |
| Decision: OR vs. imaging | < 15 minutes |
| OR for unstable torso GSW | < 15 minutes |

1. **Hemorrhage control:** Direct pressure, tourniquet (extremity), wound packing with hemostatic gauze (junctional wounds)
2. **ATLS primary survey** — most GSW deaths are from hemorrhage. Address life-threatening bleeding in the primary survey.
3. **Two large-bore IVs** — massive transfusion protocol if hemorrhagic shock. 1:1:1 PRBC:FFP:platelets.
4. **Decision: OR vs. workup:**
   - **Hemodynamically unstable + torso GSW → immediate OR** (no imaging)
   - **Hemodynamically stable → imaging** (CXR, FAST, CT as indicated by trajectory)
5. **Broad-spectrum antibiotics:** cefazolin 2 g IV q8h for all GSWs. Add metronidazole 500 mg IV q8h for abdominal penetration.
6. **Tetanus prophylaxis:** Tdap 0.5 mL IM
7. **TXA** 1 g IV over 10 min within 3 hours of injury for hemorrhagic shock
8. **Document and photograph all wounds** — forensic evidence. Do not alter entrance/exit wounds.

## Differential Diagnosis

- Stab wound (lower energy, different wound characteristics)
- Blast fragment injury (irregular fragments, multiple wounds)
- Industrial projectile injury (nail gun, rivet gun)
- Self-inflicted vs. assault vs. accidental (forensic context but does not change acute management)

## Workup

**Imaging by anatomic region:**

- **Head GSW:** CT head without contrast — identify trajectory, fragments, hemorrhage, edema, herniation
- **Neck GSW:** CTA neck (all zones) — identify vascular injury, esophageal proximity, airway integrity
- **Chest GSW:** CXR → CT chest with IV contrast if stable. FAST exam. Identify hemothorax, pneumothorax, cardiac injury, great vessel injury.
- **Abdominal GSW:** FAST → CT abdomen/pelvis with IV contrast (triple phase for liver/kidney). If unstable → OR without imaging.
- **Extremity GSW:** X-ray (fracture, fragment location) → CTA if hard/soft signs of vascular injury. ABI < 0.9 → CTA.
- **Tangential/unclear trajectory:** CT with trajectory reconstruction

**Labs:** CBC, BMP, type and crossmatch (6+ units for torso GSW), coagulation studies, lactate, ABG, troponin (precordial GSW), urinalysis (hematuria for renal/bladder trajectory)

**Forensic documentation:** Location, size, characteristics of each wound. Clothing preserved for law enforcement. Bullet fragments saved.

## Treatment

**Damage control resuscitation (hemorrhagic shock):**
- Permissive hypotension: target SBP 80-90 mmHg until surgical hemorrhage control (except with TBI — MAP > 80)
- Massive transfusion protocol: 1:1:1 PRBC:FFP:platelets
- TXA 1 g IV over 10 min, then 1 g over 8 hours
- Calcium gluconate 1-2 g IV per 4 units PRBC (counteract citrate)
- Limit crystalloid (dilutes clotting factors, worsens acidosis)
- Target: pH > 7.2, temp > 35°C, fibrinogen > 150, platelets > 50K

**Head GSW:**
- GCS ≤ 8: intubate, ICP monitoring, neurosurgery consult
- Elevate HOB 30 degrees, maintain CPP > 60 mmHg
- Mannitol 1 g/kg IV or hypertonic saline 3% 250 mL for herniation
- Surgical decompression for accessible lesions with viable brain
- Comfort care discussions for GCS 3 with bilateral fixed pupils

**Neck GSW:**
- Secure airway (oral intubation or surgical airway if disrupted)
- Control hemorrhage (direct pressure, Foley balloon tamponade for Zone I/III)
- CTA to delineate injuries → OR for confirmed vascular, esophageal, or airway injury
- All Zone II injuries with hard signs → OR exploration

**Torso GSW:**
- **Precordial:** Emergent thoracotomy or sternotomy if unstable. Pericardiocentesis for tamponade (temporizing only).
- **Thoracic:** Chest tube 36-40 Fr. Thoracotomy criteria: > 1500 mL initial or > 200 mL/hr ongoing.
- **Abdominal:** Exploratory laparotomy for unstable patients or peritonitis. Stable patients with trajectory analysis may undergo selective non-operative management (right upper quadrant, flank, tangential).
- **Damage control laparotomy:** Control hemorrhage (packing, ligation), control contamination (staple bowel, tie off), temporary abdominal closure, ICU resuscitation, return to OR 24-48h.

**Extremity GSW:**
- Low-velocity, no fracture or vascular injury: wound care, antibiotics, outpatient follow-up
- Fractures: splint, orthopedic consult, irrigation and debridement
- Vascular injury: per vascular injury extremity protocol (hard signs → OR)
- Fasciotomy for compartment syndrome

**Antibiotics:**
- All GSWs: cefazolin 2 g IV q8h x 24 hours (wound prophylaxis)
- Abdominal penetration: add metronidazole 500 mg IV q8h
- Duration: 24 hours if source controlled; 4-7 days for contamination

**Do NOT attempt bullet removal** unless it is causing specific clinical harm (embolization, joint damage, lead toxicity). Most retained bullets are benign.

## Disposition

- **OR emergent:** Hemodynamic instability, peritonitis, cardiac injury, major vascular injury, airway compromise
- **ICU:** Post-operative, head GSW, ongoing resuscitation, multiple body region involvement
- **Admit:** All torso GSWs (even if initially managed non-operatively — observation for 24-48h)
- **Outpatient (selected):** Isolated extremity GSW without fracture, vascular injury, or compartment syndrome. Wound care, antibiotics, 48-72h follow-up.
- **Social work/trauma counseling:** All GSW patients
- **Law enforcement notification:** Per state law (GSWs are reportable events in all US jurisdictions)

## Pitfalls

1. **Assuming bullet trajectory from entrance and exit wounds.** Bullets tumble, fragment, and ricochet off bone. A thigh entrance wound can harbor an abdominal injury. CT trajectory analysis or surgical exploration is required.

2. **Sending an unstable torso GSW patient to CT.** Hemodynamic instability with penetrating torso trauma = immediate OR. CT delays hemorrhage control.

3. **Not counting all wounds.** Every wound must be accounted for as entrance or exit. An odd number means a retained projectile. Missing an entrance wound means missing an injured body cavity.

4. **Selective non-operative management without appropriate observation.** Right upper quadrant or tangential GSWs can be managed non-operatively in select stable patients, but require 24-48 hours of serial exams, serial labs, and repeat imaging.

5. **Not performing EDT when indicated.** Penetrating thoracic trauma with loss of vital signs in the ED (or within 15 minutes of arrival) has documented survivors with emergent department thoracotomy. Do not withhold if trained and time criteria are met.

6. **Giving excessive crystalloid instead of blood products.** Damage control resuscitation prioritizes 1:1:1 blood products over crystalloid. Crystalloid dilutes clotting factors, worsens hypothermia, and contributes to the lethal triad (hypothermia, acidosis, coagulopathy).
