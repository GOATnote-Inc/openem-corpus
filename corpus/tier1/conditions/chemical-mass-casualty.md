---
id: chemical-mass-casualty
condition: Chemical Mass Casualty Event
aliases: [chemical attack, chemical terrorism, nerve agent exposure, chemical incident, CBRN chemical, hazmat mass casualty]
icd10: [T59.91XA, T59.4X1A, T65.0X1A, T57.3X1A, T59.891A, T07.XXXA, Y38.6X0A]
esi: 1
time_to_harm:
  irreversible_injury: "< 5 minutes for nerve agents (respiratory failure); < 30 minutes for cyanide (cellular asphyxia)"
  death: "< 10 minutes for high-dose nerve agent without antidote; < 60 minutes for cyanide without treatment"
  optimal_intervention_window: "Atropine/pralidoxime within 1 minute of nerve agent symptom onset; hydroxocobalamin within 15 minutes of cyanide exposure"
category: disaster-mci
track: tier1
sources:
  - type: consensus-statement
    ref: "Ciottone GR et al. Ciottone's Disaster Medicine, 2nd Edition. Elsevier, 2016. Chapters 126-135: Chemical Terrorism."
  - type: guideline
    ref: "CDC Strategic National Stockpile CHEMPACK Program: Nerve Agent Antidote Guidelines (2019)"
    url: "https://www.cdc.gov/phpr/stockpile/"
  - type: pubmed
    ref: "Eddleston M et al. Management of acute organophosphorus pesticide poisoning. Lancet. 2008;371(9612):597-607."
    pmid: "17706760"
  - type: pubmed
    ref: "Borron SW et al. Prospective study of hydroxocobalamin for acute cyanide poisoning in smoke inhalation. Ann Emerg Med. 2007;49(6):794-801."
    pmid: "17481777"
  - type: consensus-statement
    ref: "Rotenberg JS, Newmark J. Nerve agent attacks on children: diagnosis and management. Pediatrics. 2003;112(3 Pt 1):648-658."
    pmid: "12949297"
last_updated: "2026-02-26"
compiled_by: agent
risk_tier: A
validation:
  schema_version: "2.0"
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  guideline_version_reference: null
  provenance_links: []
---
# Chemical Mass Casualty Event

## Recognition

**Definition:** A chemical mass casualty event involves release of toxic chemical agents — intentionally (terrorism, warfare) or accidentally (industrial spill, transportation incident) — causing illness or death across multiple patients simultaneously. The critical recognition step is identifying the chemical class, which dictates decontamination urgency, antidote selection, and PPE requirements.

**Scene Assessment — Chemical Indicators:**
- Multiple patients with simultaneous symptom onset
- Unusual odors (bitter almond = cyanide; garlic = organophosphate; freshly mown hay = phosgene; bleach = chlorine)
- Dead animals, birds, or insects in the area
- Unexplained liquid or vapor clouds
- Patients collapsing in a pattern radiating from a point source
- First responder symptoms (headache, eye irritation, dyspnea) = contamination breach

**Chemical Agent Classes:**

| Agent Class | Examples | Onset | Key Findings | Lethal Mechanism |
|-------------|----------|-------|-------------- |------------------|
| **Nerve agents** | Sarin (GB), VX, soman (GD), tabun (GA), novichok | Seconds-minutes (vapor), minutes-hours (liquid) | SLUDGE/DUMBELS, miosis, fasciculations, seizures, apnea | Respiratory muscle paralysis, bronchospasm, bronchorrhea |
| **Vesicants (blistering)** | Mustard (HD), lewisite, phosgene oxime | 2–24 hours (mustard), immediate (lewisite) | Skin erythema → blisters, eye pain, respiratory distress | Airway necrosis, bone marrow suppression (delayed) |
| **Choking (pulmonary)** | Chlorine, phosgene, ammonia | Minutes (chlorine), 2–24h (phosgene) | Cough, dyspnea, pulmonary edema, stridor | Noncardiogenic pulmonary edema, ARDS |
| **Blood/metabolic** | Hydrogen cyanide, cyanogen chloride | Seconds-minutes | Altered mental status, seizure, cherry-red skin (unreliable), lactic acidosis | Inhibition of cytochrome oxidase → cellular asphyxia |
| **Incapacitating** | BZ (3-quinuclidinyl benzilate), fentanyl analogs | Minutes-hours | Anticholinergic (BZ): mydriasis, tachycardia, delirium. Opioid: miosis, bradypnea, coma | Delirium (BZ), respiratory arrest (opioids) |

**Nerve Agent Recognition — SLUDGE/DUMBELS:**
- **S**alivation, **L**acrimation, **U**rination, **D**efecation, **G**I cramping, **E**mesis
- **D**iarrhea, **U**rination, **M**iosis, **B**ronchospasm/**B**ronchorrhea, **E**mesis, **L**acrimation, **S**alivation/**S**eizures
- Miosis is the single most reliable sign of vapor exposure
- Fasciculations → flaccid paralysis → respiratory arrest (nicotinic effects)
- Seizures occur early with severe exposure — status epilepticus is common

## Critical Actions

1. **Establish Hot Zone and initiate decontamination before patient contact.** No medical provider enters the Hot Zone without Level A (SCBA + encapsulating suit) or Level B PPE. Patients exiting the Hot Zone undergo gross decontamination (clothing removal eliminates 80–90% of contamination) followed by thorough water decontamination (high-volume, low-pressure water, tepid if available, 3–5 min rinse per patient).

2. **Identify the agent class within the first 5 minutes.** Clinical syndrome recognition drives antidote selection. Do not wait for laboratory identification or HazMat team chemical detection. Miosis + secretions + fasciculations = nerve agent. Skin blisters + eye pain = vesicant. Cough + pulmonary edema = choking agent. Seizure + metabolic acidosis + rapid collapse = cyanide.

3. **Nerve agent: atropine first, atropine fast, atropine aggressively.**
   - Mild (miosis, rhinorrhea, mild dyspnea): atropine 2 mg IM, repeat q5–10min until secretions dry
   - Moderate (SLUDGE, wheezing, moderate dyspnea): atropine 4 mg IM (or 2 mg IV), repeat q5min as needed
   - Severe (seizures, apnea, flaccid paralysis): atropine 2 mg IV q2–3min × 3 rapid doses, then repeat 2 mg IV q5min. No maximum cumulative dose — titrate to dried secretions and adequate oxygenation. Patients may require 20–40 mg in the first hour.
   - **Endpoint:** dried pulmonary secretions, adequate oxygenation. NOT pupil size (miosis persists after adequate atropinization).
   - Pralidoxime (2-PAM): 1–2 g IV over 15–30 min (adults), 25–50 mg/kg IV (pediatric, max 1 g). Follow with infusion 500 mg/h. Effective if given before "aging" of AChE-agent complex (sarin: 5h, soman: 2 min, VX: 48h, tabun: 13h). Give empirically — do not wait to determine specific agent.

4. **Nerve agent seizures: benzodiazepines immediately.**
   - Diazepam 10 mg IM (autoinjector — CANA kit) or 5 mg IV
   - Midazolam 10 mg IM if IV not available (faster IM absorption)
   - Refractory: midazolam 10 mg IM q5min × 3 doses, then phenobarbital 20 mg/kg IV at 100 mg/min
   - Do NOT use succinylcholine for intubation in nerve agent exposure (prolonged paralysis from inhibited AChE)

5. **Cyanide: hydroxocobalamin is first-line antidote.**
   - Hydroxocobalamin (Cyanokit): 5 g IV over 15 min (adults), 70 mg/kg IV (pediatric, max 5 g). Repeat once if symptomatic. Turns skin and urine red — warn lab that it interferes with colorimetric assays (co-oximetry, lactate).
   - Alternative if hydroxocobalamin unavailable: sodium thiosulfate 12.5 g IV over 10–20 min (adults), 400 mg/kg IV (pediatric, max 12.5 g). Slower onset than hydroxocobalamin.
   - Amyl nitrite 0.3 mL crushed pearls inhaled for 30 sec/min as bridge while establishing IV access (only if hydroxocobalamin unavailable).
   - Sodium nitrite 300 mg (10 mL of 3% solution) IV over 5 min — use only if hydroxocobalamin unavailable; induces methemoglobinemia (contraindicated in smoke inhalation with concurrent CO poisoning).

6. **Decontaminate before hospital entry.** Establish outdoor decontamination corridor with shower facilities. All patients undergo decontamination before entering the ED — contaminated patients in the ED disable the entire facility. Staff decontamination line: Level C PPE (powered air-purifying respirator + Tyvek suit). Remove all clothing, jewelry; bag and label for HazMat disposal. Irrigate eyes with NS for 15 minutes for any ocular exposure.

7. **Activate CHEMPACK if nerve agent confirmed or suspected.** CHEMPACK is a pre-positioned cache of nerve agent antidotes (atropine autoinjectors, pralidoxime autoinjectors, diazepam autoinjectors) deployed through the CDC Strategic National Stockpile. Access through local emergency management. Typical hospital pharmacy stocks are exhausted within 5–10 nerve agent patients.

## Differential Diagnosis

| Presentation | Chemical Agent | Non-Chemical Differential |
|-------------|---------------|--------------------------|
| Miosis + secretions + fasciculations | Nerve agent (sarin, VX) | Organophosphate/carbamate pesticide exposure, myasthenic crisis |
| Rapid collapse + seizure + lactic acidosis | Cyanide | Carbon monoxide poisoning, hydrogen sulfide, status epilepticus, cardiac arrest |
| Skin blisters (delayed onset) + eye pain | Mustard agent | Thermal burns, Stevens-Johnson syndrome, phytophotodermatitis |
| Cough + stridor + pulmonary edema | Chlorine, phosgene | Smoke inhalation, acute asthma, flash pulmonary edema, anaphylaxis |
| Mydriasis + tachycardia + delirium | BZ (anticholinergic agent) | Anticholinergic medication overdose, sympathomimetic toxidrome |
| Miosis + bradypnea + coma | Opioid aerosolization (carfentanil) | Opioid overdose, sedative overdose |

**Key Distinction:** Multiple patients with identical symptom onset within minutes in a geographic cluster = chemical event until proven otherwise. Isolated single-patient presentation = consider non-chemical etiology.

## Workup

**Field (Decontamination Zone):**
- Clinical syndrome recognition — no laboratory testing in the field
- Pupil size, respiratory rate, secretion status, mental status, skin findings
- Chemical detection equipment (M8/M9 paper, ChemPro, MultiRAE) operated by HazMat team

**Hospital (Post-Decontamination):**
- **Nerve agent:** RBC/plasma cholinesterase levels (confirms exposure but does not guide acute treatment — treat clinically), ABG (acidosis, oxygenation), CXR (pulmonary edema, aspiration), ECG (QTc prolongation, bradycardia or tachycardia), glucose (hypoglycemia from cholinergic excess)
- **Cyanide:** Lactate (>8 mmol/L strongly suggests cyanide in fire/industrial exposure), ABG (metabolic acidosis with normal PaO2 — "the patient is hypoxic at the cellular level but the blood is oxygenated"), venous blood gas (arteriovenous O2 difference narrowed — cells cannot extract oxygen), whole blood cyanide level (send but do not wait for results to treat), co-oximetry (carboxyhemoglobin if concurrent CO exposure)
- **Choking agents:** CXR (serial q4h — phosgene pulmonary edema is delayed), SpO2, ABG, CBC (chlorine causes leukocytosis)
- **Vesicants:** CBC with differential q6h for 14 days (mustard causes bone marrow suppression with nadir at days 7–14), skin biopsy if diagnosis unclear, bronchoscopy for airway involvement

## Treatment

**Nerve Agents — Treatment Protocol:**
- Atropine: dose as above. Continue until secretions dry. Maintain infusion 0.5–1 mg/h if recurring secretions.
- Pralidoxime: 1–2 g IV over 15–30 min, then 500 mg/h infusion for 24h minimum. Continue until clinical improvement and cholinesterase levels recovering.
- Seizure control: diazepam 5–10 mg IV q5min or midazolam 10 mg IM q5min. Load phenobarbital 20 mg/kg IV if refractory. Continuous EEG monitoring — subclinical status epilepticus occurs after paralysis.
- Intubation (RSI): rocuronium 1.2 mg/kg IV (avoid succinylcholine — prolonged paralysis). Ketamine 1–2 mg/kg IV for induction.
- Ventilation: copious suctioning (bronchorrhea is massive), low tidal volume 6 mL/kg IBW, PEEP 5–10 cmH2O.

**Cyanide — Treatment Protocol:**
- Hydroxocobalamin 5 g IV over 15 min (first-line). Repeat × 1 if persistent symptoms.
- 100% FiO2 via NRB or intubation
- Sodium bicarbonate 1–2 mEq/kg IV for pH <7.1
- Treat concurrent CO poisoning if fire/smoke exposure (hyperbaric oxygen for CO levels >25% or neurological symptoms)

**Chlorine/Choking Agents:**
- Remove from exposure, 100% FiO2
- Nebulized sodium bicarbonate 3.75% (3 mL q15min) for chlorine inhalation — neutralizes HCl formed on mucous membranes
- Nebulized albuterol 2.5 mg q20min for bronchospasm
- Phosgene: NO fluid resuscitation for pulmonary edema (it is noncardiogenic — fluids worsen it). CPAP/BiPAP for mild-moderate. Intubation and mechanical ventilation with low PEEP for severe. Steroids not proven beneficial.
- Observation minimum 24h for phosgene exposure regardless of initial symptoms (delayed pulmonary edema is the hallmark)

**Vesicants (Mustard):**
- Decontamination within 1–2 minutes of exposure to prevent skin absorption (usually too late for presenting patients)
- Blisters: unroof large blisters, irrigate with sterile saline, apply silver sulfadiazine cream to denuded areas
- Eyes: copious NS irrigation for 15 min, ophthalmology consultation, cycloplegic drops (homatropine 5% q6h), erythromycin ophthalmic ointment
- Airway: early intubation for stridor, hoarseness, or laryngeal edema
- Bone marrow suppression: G-CSF (filgrastim) 5 mcg/kg/day SC starting at ANC <1000

## Disposition

**Nerve Agent:**
- Severe exposure (required intubation, seizures, pralidoxime): ICU admission minimum 48h
- Moderate exposure (required multiple atropine doses): ED observation 24h, then ward if improving
- Mild exposure (miosis only, minimal secretions, responded to single atropine dose): observation 6–8h, discharge if asymptomatic at reassessment
- All patients: return precautions for delayed cholinergic symptoms (intermediate syndrome at 24–96h: proximal muscle weakness, respiratory failure)

**Cyanide:**
- Any patient requiring hydroxocobalamin: ICU admission minimum 24h
- Cardiac arrest survivors: ICU with targeted temperature management
- Mild exposure (headache, mild confusion, resolved with antidote): observe 4–6h, discharge if lactate normalized

**Chlorine/Phosgene:**
- Phosgene: mandatory 24h observation regardless of symptoms (delayed pulmonary edema)
- Chlorine with respiratory symptoms: observation 6–12h minimum; admit if persistent hypoxia or infiltrates
- Asymptomatic chlorine exposure: observe 4–6h, discharge with return precautions for delayed respiratory distress

**Vesicants:**
- Burns >10% BSA or airway involvement: burn center transfer
- Eye involvement: ophthalmology admission
- Bone marrow suppression (after mustard): hematology co-management, reverse isolation if neutropenic

**MCI Decontamination Flow:**
- All patients decontaminate before hospital entry — no exceptions
- Contaminated patients in the ED create secondary contamination affecting staff and other patients, effectively closing the ED
- Decontamination throughput: ~6 patients per shower per hour with a 2-lane setup
- If patient volume exceeds decontamination capacity: gross decontamination (clothing removal + dry wipe) at minimum before entry

## Pitfalls

1. **Treating nerve agent patients without decontamination.** Medical staff who contact nerve agent-contaminated patients without PPE become casualties themselves. Off-gassing from liquid VX on clothing produces vapor exposure. The 2017 Kuala Lumpur VX assassination (Kim Jong-nam) caused secondary contamination in first responders. Decontaminate first. Always.

2. **Under-dosing atropine in severe nerve agent exposure.** Standard ACLS dosing (1 mg) is inadequate. Severe nerve agent exposure requires 6 mg IV initially, repeated q5min, with total doses of 20–40 mg in the first hour. The endpoint is drying of pulmonary secretions, NOT pupil dilation. Sub-therapeutic atropine = persistent bronchorrhea = asphyxiation from secretions.

3. **Using succinylcholine for intubation.** Nerve agents inhibit acetylcholinesterase. Succinylcholine is metabolized by plasma cholinesterase (butyrylcholinesterase). Inhibited enzyme → prolonged paralysis (hours instead of minutes). Rocuronium 1.2 mg/kg IV is the correct agent for RSI in nerve agent/organophosphate exposure.

4. **Dismissing phosgene exposure because the patient looks well initially.** Phosgene has a latent period of 2–24 hours before pulmonary edema develops. The patient who walks in after a "chlorine-like" exposure feeling "fine" may develop fatal noncardiogenic pulmonary edema 12 hours later. Mandatory 24h observation for all suspected phosgene exposure.

5. **Giving sodium nitrite for cyanide poisoning in fire victims.** Sodium nitrite induces methemoglobinemia. Fire victims have concurrent carbon monoxide poisoning (carboxyhemoglobin). Adding methemoglobin to carboxyhemoglobin critically reduces oxygen-carrying capacity. Hydroxocobalamin is the correct antidote for cyanide in fire/smoke exposure — it does not induce methemoglobinemia.

6. **Failure to access CHEMPACK.** Hospitals stock limited nerve agent antidotes. A typical ED pharmacy has enough atropine for 5–10 patients. CHEMPACK caches, pre-positioned by CDC, contain thousands of doses. Accessing CHEMPACK requires notification through local emergency management or the health department — this process must be practiced before the event. If the first call to activate CHEMPACK is during the actual event, it is too late.

### System Overwhelm

Chemical MCI events generate a unique resource crisis because decontamination is the bottleneck — not treatment capacity:

- **Decontamination throughput:** A 2-lane decontamination setup processes ~12 patients per hour. 100 contaminated patients = 8+ hours of decontamination, during which the ED cannot accept non-decontaminated patients. Gross decontamination (clothing removal) eliminates 80–90% of agent and may be the only feasible option at scale.
- **PPE endurance:** Level C PPE (minimum for decontamination operations) causes heat stress. Providers last 30–45 minutes in PPE before requiring rotation. A 4-provider decontamination team requires 12 providers for continuous 2-hour operations.
- **Antidote depletion:** Atropine, pralidoxime, hydroxocobalamin — all deplete rapidly. 20 severe nerve agent patients × 40 mg atropine each = 800 mg (800 vials of 1 mg atropine). Standard ED stock: 50–100 vials. CHEMPACK activation and regional pharmacy mutual aid are mandatory.
- **Ventilator demand:** Nerve agents produce mass respiratory failure. 30% of moderate-severe nerve agent casualties require mechanical ventilation. A 20-patient event generates 6+ simultaneous intubations. Prepare all available ventilators including anesthesia machines and transport ventilators.
- **Self-presenting contaminated patients:** 70–80% of chemical MCI patients self-transport and arrive without decontamination. They contaminate the ED waiting room, triage area, and staff on contact. Hospital decontamination activation must be immediate — post a sentinel at the entrance who can recognize chemical exposure (odor, symptom cluster, multiple simultaneous presentations) before contaminated patients enter the building.
