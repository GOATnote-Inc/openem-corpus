---
id: inhalation-injury
condition: Inhalation Injury
aliases: [smoke inhalation, inhalation burn, airway burn, smoke inhalation injury]
icd10: [T27.0XXA, T27.1XXA, T27.2XXA, T27.3XXA, T59.811A]
esi: 1
time_to_harm:
  irreversible_injury: "< 2 hours (airway obstruction)"
  death: "< 6 hours"
  optimal_intervention_window: "< 1 hour (airway control)"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition, American College of Surgeons, 2018"
  - type: guideline
    ref: "Surgical Critical Care Guidelines: Burn Inhalation Injury. 2025"
  - type: review
    ref: "Walker PF et al. Diagnosis and management of inhalation injury: an updated review. Crit Care. 2015;19:351"
  - type: pubmed
    ref: "Dries DJ, Endorf FW. Inhalation injury: epidemiology, pathology, treatment strategies. Scand J Trauma Resusc Emerg Med. 2013;21:31"
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
# Inhalation Injury

## Recognition

**Mechanism:** Enclosed-space fire, explosion, steam exposure, chemical fume exposure. Three distinct injury patterns:

1. **Supraglottic thermal injury:** Direct heat damage to upper airway (mouth, pharynx, larynx). Air is a poor conductor — heat rarely reaches below the cords except with steam (which carries 4000x more thermal energy than dry air).
2. **Infraglottic chemical injury:** Toxic combustion products (acrolein, HCl, phosgene, ammonia) damage tracheobronchial mucosa and alveoli. Causes chemical tracheobronchitis, mucosal sloughing, cast formation.
3. **Systemic toxicity:** Carbon monoxide (CO) and hydrogen cyanide (HCN) poisoning from incomplete combustion.

**Clinical signs suggesting inhalation injury:**
- Facial burns, singed nasal hairs, singed eyebrows
- Carbonaceous sputum (soot in mouth, nose, or sputum)
- Hoarseness, stridor, dysphonia
- Cough, wheezing, dyspnea
- Altered mental status (CO/cyanide poisoning)
- Cherry-red skin (CO — classic but uncommon)
- Oropharyngeal edema, erythema, blistering on direct inspection

**Key point:** Airway edema peaks at 12-24 hours. May be accelerated by fluid resuscitation for concurrent burns. A stable-appearing airway at presentation can rapidly deteriorate.

## Critical Actions

| Action | Target |
|---|---|
| 100% FiO2 via NRB | Immediate |
| Airway assessment and early intubation | < 30 minutes if any concern |
| CO-oximetry (ABG) | < 15 minutes |
| Hydroxocobalamin for cyanide | Immediate if suspected |
| Bronchoscopy | Within 4 hours (diagnosis) |

1. **100% FiO2 via non-rebreather mask** — treats CO poisoning and supports oxygenation. Do NOT rely on SpO2 (falsely normal with CO).
2. **Early intubation** — indicated for: stridor, hoarseness, progressive dyspnea, facial edema, carbonaceous sputum with oropharyngeal burns, altered mental status, large TBSA burns (> 40%). Use largest possible ETT (≥ 8.0 in adults) to facilitate bronchoscopy and suction of casts. Leave ETT uncut to accommodate swelling.
3. **CO-oximetry on ABG** — measure carboxyhemoglobin (COHb). Normal < 3% (non-smokers), < 10% (smokers). > 15% = significant exposure. > 25% = severe.
4. **Hydroxocobalamin 5 g IV over 15 minutes** — empiric for cyanide poisoning if: enclosed fire, altered mental status, severe lactic acidosis (lactate > 8 mmol/L), hemodynamic instability disproportionate to burns. Safe, does not worsen CO poisoning.
5. **Bronchoscopy** within 4 hours of admission — definitive diagnosis. Findings: soot below cords, mucosal edema/erythema, ulceration, cast formation. Grades injury severity.

## Differential Diagnosis

- Thermal upper airway burn without infraglottic injury
- CO poisoning without structural airway injury
- Cyanide poisoning without smoke exposure (industrial)
- Anaphylaxis (urticaria, angioedema, no fire exposure)
- Toxic gas exposure without fire (chlorine, ammonia, phosgene)
- Aspiration pneumonitis
- Pulmonary contusion (blunt mechanism)
- ARDS from non-inhalation cause

## Workup

- **ABG with co-oximetry:** COHb level, PaO2, pH, lactate (lactate > 8 suggests concurrent cyanide poisoning)
- **Serum lactate:** Elevated disproportionately in cyanide poisoning
- **CBC, BMP, LFTs, coagulation studies**
- **CXR:** Often initially normal; may show perihilar infiltrates, ARDS pattern at 24-48 hours
- **Bronchoscopy:** Gold standard for diagnosis and grading. Perform within 4 hours.
  - Grade 0: No injury
  - Grade 1: Mild edema, erythema, soot deposits
  - Grade 2: Moderate edema, friability, bronchorrhea
  - Grade 3: Severe edema, ulceration, necrosis, cast formation
  - Grade 4: Mucosal destruction, obliteration of airways
- **CT chest:** Consider for delayed assessment; identifies parenchymal changes, bronchial wall thickening
- **Cyanide levels:** If available (rarely results in time to guide acute treatment — treat empirically)
- **ECG:** CO and cyanide both cause myocardial injury

## Treatment

**Airway management:**
- Endotracheal intubation: use ≥ 8.0 ETT, leave uncut, secure firmly (facial edema loosens tape)
- Avoid nasal intubation (facial burns, edema make nasal route high risk)
- Keep cuff pressure minimal (30 cmH2O) — tracheal mucosa is injured
- Plan for difficult extubation (cuff leak test before extubation attempt)

**Carbon monoxide treatment:**
- 100% FiO2 — reduces CO half-life from 4-6 hours to 60-90 minutes
- Continue until COHb < 5% and symptoms resolve
- Hyperbaric oxygen (HBO): consider for COHb > 25%, loss of consciousness, cardiac ischemia/arrhythmia, pregnancy, persistent neurological symptoms. Reduces delayed neuropsychiatric sequelae. Treat within 24 hours.

**Cyanide treatment:**
- **Hydroxocobalamin (Cyanokit) 5 g IV over 15 minutes** — first-line, safe in fire victims. Repeat 5 g if persistent hemodynamic instability.
- Alternative: sodium thiosulfate 12.5 g IV over 10 minutes (slower onset, less effective as sole agent)
- Avoid amyl nitrite/sodium nitrite in fire victims (induces methemoglobin which further reduces O2 carrying capacity when already CO-poisoned)

**Pulmonary care:**
- Nebulized unfractionated heparin 5000 units + albuterol 2.5 mg via ETT q4h (reduces cast formation, improves survival per burn center data)
- Nebulized 20% N-acetylcysteine (NAC) 3 mL q4h alternating with heparin (mucolytic, antioxidant)
- Aggressive pulmonary toilet: frequent suctioning, therapeutic bronchoscopy for cast removal
- Lung-protective ventilation: TV 6 mL/kg IBW, PEEP 5-10 cmH2O, plateau pressure < 30
- Avoid excessive PEEP in setting of pneumothorax (barotrauma risk increased with damaged airways)

**Fluid resuscitation (if concurrent burns):**
- Add 20-40% to calculated resuscitation volumes for patients with inhalation injury
- Monitor for pulmonary edema — balance fluid needs against respiratory status
- UOP target: 0.5-1 mL/kg/hr adults

## Disposition

- **ICU:** All patients with confirmed inhalation injury requiring intubation, CO/CN poisoning, or > 20% TBSA burns
- **Burn center transfer:** All patients with inhalation injury (ABA criterion)
- **Observation (24 hours minimum):** Patients with smoke exposure but without immediate intubation criteria — delayed presentation possible
- **HBO referral:** If meeting criteria (see CO treatment), transfer to facility with hyperbaric chamber
- **Discharge (rare):** Minimal exposure, normal COHb, normal bronchoscopy, no symptoms at 6 hours. Return precautions for any respiratory symptoms.

## Pitfalls

1. **Trusting SpO2 in smoke inhalation.** Pulse oximetry reads COHb as oxyhemoglobin. A patient with 40% COHb will show SpO2 of 98-100%. Always obtain co-oximetry on ABG.

2. **Delaying intubation because the patient "looks fine."** Upper airway edema peaks at 12-24 hours and accelerates with IV fluid resuscitation. By the time stridor develops, intubation may be impossible due to massive edema. Intubate early, extubate later.

3. **Giving sodium nitrite to a fire victim with CO poisoning.** Nitrites induce methemoglobinemia. Combined COHb + MetHb can be lethal. Use hydroxocobalamin instead — it chelates cyanide without affecting hemoglobin oxygen carrying capacity.

4. **Using small ETT.** A 7.0 ETT will clog with casts and cannot accommodate a bronchoscope for therapeutic lavage. Use ≥ 8.0 in adults.

5. **Normal CXR excludes inhalation injury.** CXR is typically normal for the first 24-48 hours after inhalation injury. Bronchoscopy within 4 hours is the diagnostic standard.

6. **Not considering cyanide poisoning in enclosed-space fire victims.** CO and cyanide coexist in 35-50% of enclosed-space fire victims. Severe lactic acidosis (> 8 mmol/L) disproportionate to burn size or hemodynamic status should trigger empiric hydroxocobalamin.
