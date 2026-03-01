---
id: burn-wound-management
condition: Burn Wound Management
aliases: [thermal burn, burn injury, burn care, flame burn, scald burn]
icd10: [T20.00XA, T30.0, T31.0, T31.10, T31.20, T31.30]
esi: 2
time_to_harm:
  irreversible_injury: "< 2 hours (airway edema in inhalation injury)"
  death: "< 6 hours (hypovolemic shock in major burns)"
  optimal_intervention_window: "< 1 hour (fluid resuscitation, airway management)"
category: dermatologic
track: tier1
sources:
  - type: guideline
    ref: "ABA Clinical Practice Guidelines on Burn Shock Resuscitation, 2023"
  - type: guideline
    ref: "ISBI Practice Guidelines for Burn Care, 2018"
  - type: guideline
    ref: "ACS Advanced Trauma Life Support (ATLS): Burns Chapter"
  - type: review
    ref: "Parkland Formula. StatPearls, NCBI Bookshelf, 2024"
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
# Burn Wound Management

## Recognition

**Burn depth classification:**
- **Superficial (1st degree):** Erythema only, painful, dry, no blisters; heals in 3-5 days (e.g., sunburn)
- **Superficial partial-thickness (2nd degree):** Blisters, weeping, painful to touch, brisk capillary refill; heals in 7-21 days
- **Deep partial-thickness (2nd degree):** Pale, mottled, decreased sensation, sluggish capillary refill; may require grafting
- **Full-thickness (3rd degree):** Waxy white, leathery, charred, insensate, no capillary refill; requires excision and grafting
- **4th degree:** Extends into fascia, muscle, tendon, bone

**BSA estimation:**
- **Rule of Nines (adults):** Head 9%, each arm 9%, each leg 18%, anterior trunk 18%, posterior trunk 18%, perineum 1%
- **Palmar method:** Patient's palm (including fingers) = ~1% BSA — useful for scattered/irregular burns
- **Lund-Browder chart:** Most accurate, especially for pediatrics (adjusts for age-related body proportions)
- NOTE: Do NOT include superficial (1st degree) burns in BSA calculation for fluid resuscitation

**Inhalation injury indicators:**
- Singed facial hair, eyebrows, nasal vibrissae
- Soot in oropharynx or nares
- Hoarseness, stridor, wheezing
- Carbonaceous sputum
- Facial burns, especially circumferential neck
- Enclosed space fire exposure
- Carbon monoxide or cyanide poisoning

**ABA Burn Center referral criteria (any one):**
- Partial-thickness burns > 10% BSA
- Burns involving face, hands, feet, genitalia, perineum, or major joints
- Full-thickness (3rd degree) burns of any size
- Electrical or chemical burns
- Inhalation injury
- Burns with significant comorbidity
- Children at hospitals without qualified pediatric care
- Circumferential burns

## Critical Actions

1. **Stop the burning process** — remove clothing, jewelry; irrigate chemical burns copiously
2. **Primary survey (ATLS)** — airway is the priority; intubate early if ANY signs of inhalation injury (edema progresses rapidly; delay may make intubation impossible)
3. **Estimate BSA of 2nd and 3rd degree burns** — guides fluid resuscitation
4. **Start fluid resuscitation** for burns >= 20% BSA (adults) or >= 10% BSA (children):
   - **Modified Parkland formula:** 2-4 mL/kg/% TBSA burned of Lactated Ringer's over first 24 hours
   - Give HALF in first 8 hours (from time of burn, NOT from ED arrival), remainder over next 16 hours
5. **IV analgesia** — morphine 0.1 mg/kg IV q2-4h PRN or fentanyl 1-2 mcg/kg IV; burns are excruciatingly painful
6. **Escharotomy** for circumferential full-thickness burns causing compartment syndrome or respiratory compromise
7. **Tetanus prophylaxis** — update if > 5 years since last dose

## Differential Diagnosis

- Chemical burn — exposure history, ongoing tissue destruction (irrigate, do NOT neutralize)
- Electrical burn — entry/exit wounds, cardiac arrhythmia, rhabdomyolysis (damage worse than visible)
- Radiation burn — exposure history, delayed erythema
- Toxic epidermal necrolysis — drug-triggered, Nikolsky sign, mucosal involvement (mimics burn)
- Scalded skin syndrome (Staphylococcal) — infants/children, diffuse erythema, Nikolsky sign
- Child abuse — immersion pattern (stocking-glove distribution), cigarette burns, pattern injuries
- Frostbite — cold exposure, rewarming creates similar-appearing blisters
- Stevens-Johnson syndrome — drug history, target lesions, mucosal erosions

## Workup

- **BSA estimation** — Lund-Browder chart (most accurate) or Rule of Nines
- **Carboxyhemoglobin (COHb)** — if enclosed space exposure; co-oximetry (standard pulse ox is unreliable)
- **Cyanide level** if structural fire with altered mental status (or treat empirically with hydroxocobalamin)
- **Lactate** — tissue perfusion marker
- **CBC, BMP, coagulation studies** — baseline
- **Type and screen** — major burns may require transfusion
- **ABG/VBG** — assess oxygenation, ventilation, metabolic status
- **CXR** — baseline, monitor for ARDS
- **Urinalysis + urine myoglobin** — dark urine suggests rhabdomyolysis (especially electrical burns)
- **CK** — if electrical burn or crush component
- **ECG** — electrical burns mandate cardiac monitoring (risk of arrhythmia)
- **Fiberoptic laryngoscopy/bronchoscopy** — definitive assessment of inhalation injury if suspected

## Treatment

### Fluid Resuscitation (Burns >= 20% BSA Adults, >= 10% BSA Children)
- **Modified Parkland/Baxter:** 2-4 mL LR x kg x %TBSA burned over 24 hours
  - ABA 2023 recommendation: Start at 2 mL/kg/%TBSA to avoid fluid overload ("fluid creep")
  - First half over hours 0-8 (from time of burn); second half over hours 8-24
- **Titrate to urine output:** Adults 0.5-1.0 mL/kg/hr; children < 30 kg: 1.0 mL/kg/hr
- **Foley catheter** mandatory for monitoring in major burns
- **Colloid (5% albumin)** may be added after 24 hours or earlier if fluid requirements exceed 150% of Parkland estimate

### Airway Management
- **Intubate early** if: stridor, hoarseness, progressive edema, significant facial burns, altered consciousness
- Use uncut ETT (facial edema will swell; tape will fail on burned skin — use cloth ties)
- Avoid succinylcholine if burn > 24 hours old (hyperkalemia risk from upregulated acetylcholine receptors)

### Carbon Monoxide Poisoning
- **High-flow O2 via NRB 15 L/min** — half-life of COHb drops from 4-5h on room air to 60-90 min on 100% O2
- **Hyperbaric oxygen** for: COHb > 25%, loss of consciousness, neurologic symptoms, cardiac ischemia, pregnancy

### Cyanide Poisoning
- **Hydroxocobalamin 5 g IV over 15 minutes** (70 mg/kg in children) — treat empirically if altered mental status + lactic acidosis in structure fire

### Wound Care
- **Cool running water** over burn for 20 minutes (within 3 hours of injury) — reduces depth
- Do NOT use ice (causes vasoconstriction, worsens injury)
- **Superficial partial-thickness:** Clean gently, apply topical antimicrobial (silver sulfadiazine 1% or bacitracin), non-adherent dressing
- **Deep partial/full-thickness:** Clean, apply non-adherent dressing; definitive care (excision, grafting) at burn center
- **Blisters:** Intact blisters > 2 cm: aspirate or debride. Small intact blisters: may leave intact (controversial). Ruptured blisters: debride roof and dress.
- **Facial burns:** Bacitracin or antibiotic ointment; no occlusive dressings

### Escharotomy
- **Indication:** Circumferential full-thickness burn with vascular compromise (diminished pulses, cyanosis) or respiratory compromise (circumferential chest burn restricting ventilation)
- **Technique:** Full-thickness incision through eschar to subcutaneous fat along mid-lateral lines of extremities; bilateral anterior axillary lines for chest
- No anesthesia needed (full-thickness burns are insensate)
- Must be done emergently — do NOT delay for transfer

### Pain Management
- Morphine 0.1 mg/kg IV q2-4h PRN (or fentanyl 1-2 mcg/kg IV for rapid onset)
- Ketamine 0.1-0.3 mg/kg IV (sub-dissociative) for procedural pain and dressing changes
- Acetaminophen 1000 mg PO/IV q6h (adjunctive)
- Anxiety: Midazolam 0.5-1 mg IV or lorazepam 0.5-1 mg IV PRN

## Disposition

- **Burn center transfer** for all ABA referral criteria (see Recognition section)
- **Admit:** >= 10% BSA partial-thickness; any full-thickness; inhalation injury; electrical/chemical; circumferential; significant comorbidity
- **Discharge:** Superficial burns, small partial-thickness burns (< 10% BSA) not meeting referral criteria
- **Outpatient follow-up:** Wound check at 48 hours, then as needed
- **Return precautions:** Signs of infection (increased pain, redness, purulent drainage, fever), inability to manage wound care
- **Child abuse screening:** Immersion patterns, delay in seeking care, inconsistent history — involve social work and child protective services
- **Isolation:** Standard precautions; burn patients are immunosuppressed and require protective measures
- **Reportable:** Suspected child abuse is mandatorily reportable; fire-related injuries may require reporting to fire marshal in some jurisdictions

## Pitfalls

1. **Delayed intubation in inhalation injury.** Airway edema progresses over hours. By the time stridor is audible, the airway may be critically narrowed. Intubate early if ANY inhalation injury signs are present.

2. **Overestimating burn BSA (and over-resuscitating).** Fluid creep from excessive resuscitation causes abdominal compartment syndrome, extremity compartment syndrome, and pulmonary edema. Start at 2 mL/kg/%TBSA and titrate to urine output.

3. **Including superficial (1st degree) burns in BSA calculation.** Only 2nd degree and deeper burns are included when calculating fluid resuscitation requirements.

4. **Trusting pulse oximetry in CO poisoning.** Standard pulse ox cannot distinguish carboxyhemoglobin from oxyhemoglobin. SpO2 reads falsely normal. Use co-oximetry.

5. **Not performing escharotomy for circumferential burns.** Circumferential full-thickness burns form a rigid eschar that cannot expand with swelling. Compartment syndrome and respiratory failure develop rapidly. Escharotomy is emergent and should not be delayed for transfer.

6. **Failing to calculate fluids from time of burn.** The Parkland formula starts from the time of burn, NOT from time of ED arrival. If the burn occurred 3 hours ago, calculate accordingly and account for prehospital fluids.
