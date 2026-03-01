---
id: thermal-burns
condition: Thermal Burns
aliases: [burn injury, scald burn, flame burn, contact burn, major burn, burn trauma]
icd10: [T30.0, T31.0, T31.10, T31.20, T31.30, T31.40, T31.50]
esi: 1
time_to_harm:
  irreversible_injury: "< 1 hour (airway burn)"
  death: "< 6 hours (unresuscitated major burn)"
  optimal_intervention_window: "< 1 hour (fluid resuscitation)"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition, American College of Surgeons, 2018"
  - type: guideline
    ref: "ABA Clinical Practice Guidelines: Burn Shock Resuscitation. 2024"
  - type: guideline
    ref: "ISBI Practice Guidelines for Burn Care. 2016; updated 2018"
  - type: review
    ref: "Jeschke MG et al. Burn injury. Nat Rev Dis Primers. 2020;6(1):11"
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
# Thermal Burns

## Recognition

**Mechanism:** Flame, scald (liquid/steam), contact (hot surface/object), flash (explosion). Assess for concurrent blast injury, inhalation injury, trauma.

**Burn depth classification:**
- **Superficial (1st degree):** Epidermis only. Erythema, pain, no blisters. Sunburn-type. NOT included in TBSA calculation.
- **Superficial partial thickness (2nd degree):** Epidermis + superficial dermis. Painful, moist, blistered, blanches with pressure. Heals in 2-3 weeks.
- **Deep partial thickness (2nd degree):** Epidermis + deep dermis. Less painful (nerve damage), pale/mottled, sluggish blanching. Often requires excision and grafting.
- **Full thickness (3rd degree):** Through entire dermis. Painless, leathery/waxy, no blanching. Requires excision and grafting.
- **4th degree:** Through dermis into subcutaneous fat, muscle, bone, tendon.

**TBSA estimation:**
- **Rule of Nines (adults):** Head 9%, each arm 9%, anterior trunk 18%, posterior trunk 18%, each leg 18%, perineum 1%
- **Lund-Browder chart:** More accurate, accounts for age-based body proportions (essential for pediatrics)
- **Palmar method:** Patient's palm (including fingers) = ~1% TBSA — useful for scattered burns
- **First degree burns are NOT counted** in TBSA for resuscitation calculations

**ABA burn center referral criteria:**
- > 10% TBSA partial thickness
- Burns involving face, hands, feet, genitalia, perineum, major joints
- Full thickness (3rd degree) burns of any size
- Electrical burns, chemical burns
- Inhalation injury
- Burns with significant comorbidities
- Burns with concomitant trauma (if burn is the greater risk)
- Children (if no qualified pediatric burn center available)
- Special considerations: abuse, social factors

## Critical Actions

| Action | Target |
|---|---|
| Stop the burning process | Immediate |
| Secure airway (if inhalation injury) | Immediate |
| IV fluid resuscitation (> 20% TBSA) | Within 30 minutes |
| Estimate TBSA | < 30 minutes |
| Burn center contact | < 1 hour |

1. **Stop the burning process** — remove clothing, jewelry, all circumferential items. Cool burns with room-temperature water briefly (< 20 min) — avoid hypothermia (especially children, large burns).
2. **ATLS primary survey** — burns may accompany trauma (explosion, jump from building).
3. **Secure airway early** if any inhalation concern — facial burns, singed nasal hairs, carbonaceous sputum, hoarse voice, stridor. Progressive airway edema peaks at 12-24 hours. Intubate early (will become impossible later).
4. **Calculate TBSA** using Rule of Nines or Lund-Browder. Exclude first-degree burns.
5. **Begin IV fluid resuscitation** for > 20% TBSA (> 10% in children):
   - **Modified Brooke formula (ABA recommended):** 2 mL x kg x %TBSA of LR
   - **Parkland formula:** 4 mL x kg x %TBSA of LR
   - Give half in first 8 hours (from time of burn, not arrival), remainder over next 16 hours
   - **Titrate to UOP:** 0.5-1 mL/kg/hr adults; 1-2 mL/kg/hr children
6. **Insert Foley catheter** for > 20% TBSA — hourly urine output monitoring is the primary resuscitation endpoint.

## Differential Diagnosis

- Chemical burn (exposure history, ongoing tissue destruction — requires decontamination, not just cooling)
- Electrical burn (entrance/exit wounds, rhabdomyolysis, arrhythmia — surface underestimates deep injury)
- Radiation burn (delayed presentation 1-3 weeks)
- Stevens-Johnson syndrome/TEN (drug exposure, mucosal involvement, Nikolsky sign)
- Staphylococcal scalded skin syndrome (children, generalized erythema/desquamation, no blister fluid)
- Toxic epidermal necrolysis (mucosal involvement, drug history)
- Non-accidental burn (child abuse: immersion burns with sharp demarcation, sock/glove distribution, bilateral symmetric)

## Workup

- **TBSA estimation:** Rule of Nines, Lund-Browder chart, or palmar method
- **Labs:** CBC, BMP (K+ monitoring), LFTs, coagulation studies, type and crossmatch, lactate, ABG/VBG (carboxyhemoglobin if enclosed fire), CK/myoglobin (deep burns, electrical)
- **Carboxyhemoglobin level:** Co-oximetry on ABG for all enclosed-space burns. SpO2 is unreliable (reads falsely normal in CO poisoning).
- **Chest X-ray:** Baseline, inhalation injury assessment
- **Bronchoscopy:** If inhalation injury suspected — definitive diagnosis (soot, mucosal edema, erythema, ulceration below cords)
- **ECG:** For electrical burns (arrhythmia screening)
- **Trauma imaging:** Per ATLS protocol if concurrent trauma mechanism

## Treatment

**Fluid resuscitation (> 20% TBSA):**
- Lactated Ringer's solution via large-bore IV (two peripheral or central access)
- Modified Brooke: 2 mL/kg/%TBSA first 24 hours
- Parkland: 4 mL/kg/%TBSA first 24 hours
- Half in first 8 hours (from burn time), half over next 16 hours
- **Titrate to urine output** — the formula is a starting point only
- Adult UOP target: 0.5-1 mL/kg/hr
- Pediatric UOP target: 1-2 mL/kg/hr
- Avoid "fluid creep" (over-resuscitation) — causes compartment syndrome, pulmonary edema, abdominal compartment syndrome
- If inadequate response to crystalloid: consider 5% albumin 0.3-0.5 mL/kg/%TBSA over 24 hours (starting at hour 8-12)

**Airway management:**
- Early intubation for: stridor, hoarseness, facial edema, carbonaceous sputum, large TBSA (> 40%)
- Use largest possible ETT (anticipate airway edema making reintubation difficult)
- Do NOT use succinylcholine > 48 hours post-burn (hyperkalemic cardiac arrest from upregulated receptors)

**Wound care (ED):**
- Clean with mild soap and water or saline
- Debride ruptured blisters; leave intact blisters with clear fluid < 2 cm
- Apply topical antimicrobial: silver sulfadiazine 1% cream (avoid on face — silver staining) or bacitracin or mafenide acetate (for ear cartilage — penetrates eschar)
- Non-adherent dressing (petrolatum gauze, Adaptic, or Mepilex Ag)
- Elevate burned extremities above heart level

**Escharotomy (emergent):**
- Circumferential full-thickness burns cause compartment syndrome as eschar contracts
- **Chest:** If restrictive eschar impairs ventilation — bilateral anterior axillary line incisions connected across chest
- **Extremity:** Medial and lateral longitudinal incisions through eschar (not into subcutaneous fat)
- Performed in ED or at bedside — no general anesthesia needed (full-thickness burns are insensate)

**Pain management:**
- IV opioids: morphine 0.1 mg/kg IV q2-4h PRN or fentanyl 1-2 mcg/kg IV q30-60min
- Ketamine 0.1-0.3 mg/kg IV for procedural analgesia
- Acetaminophen 1 g IV q6h
- Avoid NSAIDs acutely (renal perfusion concerns in major burns)
- Anxiolytics: midazolam 1-2 mg IV PRN for procedure anxiety

**Tetanus prophylaxis:** Tdap 0.5 mL IM if not current.

**Carbon monoxide poisoning (enclosed fire):**
- 100% FiO2 via NRB or ventilator until COHb < 5%
- Half-life of CO: 4-6 hours on room air, 60-90 minutes on 100% O2
- Consider hyperbaric O2 for: COHb > 25%, loss of consciousness, cardiac ischemia, pregnancy

## Disposition

- **Burn center transfer:** Per ABA criteria (see Recognition section)
- **ICU:** > 20% TBSA, inhalation injury, concurrent trauma, hemodynamic instability
- **Admit (non-ICU):** 10-20% TBSA without complications, burns requiring IV pain management
- **Outpatient (selected cases):** < 10% TBSA partial thickness, no involvement of critical areas (face, hands, feet, genitalia, joints), no inhalation injury, reliable follow-up. Return in 24-48 hours for wound check.
- **Child protective services referral:** If burn pattern suggests non-accidental injury (immersion burns, bilateral/symmetric, delay in seeking care)

## Pitfalls

1. **Overestimating TBSA by including first-degree (superficial) burns.** Only partial and full thickness burns count for TBSA and resuscitation calculations. Erythema without blistering is first degree.

2. **Delaying intubation in inhalation injury.** Airway edema peaks at 12-24 hours. A patient who is hoarse but stable at presentation may have complete airway obstruction hours later. Intubate early based on clinical signs, not degree of distress.

3. **Using SpO2 to rule out carbon monoxide poisoning.** Pulse oximetry reads carboxyhemoglobin as oxyhemoglobin. SpO2 will be falsely normal. Use co-oximetry on ABG.

4. **Fluid creep — over-resuscitation.** Blindly following Parkland formula without titrating to urine output leads to massive edema, abdominal compartment syndrome, extremity compartment syndrome, and pulmonary edema. Titrate to 0.5-1 mL/kg/hr UOP.

5. **Using succinylcholine > 48 hours post-burn.** Burns cause massive upregulation of extrajunctional acetylcholine receptors. Succinylcholine produces lethal hyperkalemia. Use rocuronium instead.

6. **Not performing escharotomy for circumferential full-thickness burns.** Eschar cannot expand. Circumferential chest burns restrict ventilation; circumferential limb burns cause compartment syndrome. These are time-sensitive procedures.

7. **Missing non-accidental burn patterns in children.** Immersion burns with sharp lines of demarcation (stocking/glove pattern), bilateral symmetric burns, and spared skin folds (child held in fetal position) are red flags for abuse.
