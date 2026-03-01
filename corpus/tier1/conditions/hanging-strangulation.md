---
id: hanging-strangulation
condition: Hanging and Strangulation
aliases: [near-hanging, asphyxia by hanging, ligature strangulation, manual strangulation, judicial hanging, incomplete hanging]
icd10: [T71.111A, T71.121A, T71.131A, T71.141A, T71.151A, T71.161A]
esi: 1
time_to_harm:
  irreversible_injury: "< 5 minutes (anoxic brain injury)"
  death: "< 10 minutes"
  optimal_intervention_window: "< 4 minutes"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition, American College of Surgeons, 2018"
  - type: review
    ref: "Coombs AE, Ashton-Cleary D. Hanging and near-hanging. BJA Educ. 2023;23(8):296-303"
  - type: pubmed
    ref: "Salim A et al. Approach considerations for the management of strangulation in the emergency department. West J Emerg Med. 2022;23(3):399-407"
  - type: guideline
    ref: "ENT UK: Guidelines for Clinical Management of Non-Fatal Strangulation. 2024"
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
# Hanging and Strangulation

## Recognition

**Types:**
- **Hanging:** Suspension by ligature around neck. Complete (feet off ground) vs. incomplete (partial body weight). Suicidal (most common), accidental, homicidal, judicial.
- **Ligature strangulation:** Constriction by cord, rope, wire, clothing without suspension
- **Manual strangulation:** Compression by hands, forearms, or choke holds

**Mechanisms of injury (may occur simultaneously):**
1. **Vascular occlusion:** Jugular veins (2 kg force) → cerebral venous congestion → carotid arteries (5 kg force) → cerebral ischemia → vertebral arteries (16 kg force). Vascular compromise is the primary cause of death in most cases.
2. **Airway obstruction:** Compression of hypopharynx, larynx, or trachea against cervical spine. Requires 15 kg force. Less common primary mechanism than vascular.
3. **Cervical spine injury:** Fracture-dislocation (C2 hangman fracture classic). Primarily in judicial hanging (drop with sudden deceleration). Rare in suicidal hanging or strangulation.
4. **Vagal reflex (cardiac arrest):** Direct pressure on carotid body → bradycardia → asystole. Can cause death with very brief compression.

**Presentation:**
- Altered mental status (ranging from confusion to coma)
- Ligature marks on neck (may be subtle or absent in manual strangulation)
- Petechiae: conjunctival, periorbital, facial (above ligature line — venous congestion)
- Hoarseness, dysphonia, aphonia
- Dysphagia, odynophagia
- Stridor (laryngeal edema or fracture)
- Subcutaneous emphysema (laryngeal or tracheal fracture)
- Focal neurological deficits (carotid dissection → stroke)
- Seizures, decerebrate posturing (anoxic brain injury)

**Injuries to assess:**
- Laryngeal/hyoid fracture
- Carotid/vertebral artery dissection or thrombosis
- Cervical spine fracture
- Tracheal injury
- Esophageal injury (rare)
- Pulmonary edema (neurogenic or post-obstructive)

## Critical Actions

| Action | Target |
|---|---|
| Secure airway with C-spine precautions | Immediate |
| C-spine immobilization | Immediate |
| CTA neck | < 1 hour |
| CT C-spine | < 1 hour |
| Psychiatric evaluation | After medical stabilization |

1. **Airway management** — highest priority. Anticipate difficult airway due to laryngeal edema, fracture, or blood.
   - If breathing spontaneously with stable airway: close monitoring, prepare for deterioration
   - If airway compromised: orotracheal intubation with C-spine precautions (video laryngoscopy preferred). If intubation fails (distorted anatomy from laryngeal fracture) → surgical airway (tracheostomy preferred over cricothyrotomy if laryngeal injury suspected)
   - Awake intubation or awake tracheostomy if anatomy is distorted but patient conscious
2. **Cervical spine immobilization** — maintain until cleared by CT. Cervical fractures rare in non-judicial hanging but cannot be excluded by mechanism alone.
3. **100% FiO2** — treat for anoxic injury
4. **CTA neck** — assess for carotid/vertebral dissection, thrombosis, pseudoaneurysm. Do NOT use carotid Doppler (insufficient for this assessment).
5. **CT cervical spine** — exclude fracture
6. **CT head** — if altered mental status (assess for anoxic injury, edema, infarction)

## Differential Diagnosis

- Anoxic brain injury from other cause (drowning, cardiac arrest, suffocation)
- Drug overdose (found unresponsive with ligature — was it hanging or overdose with incidental ligature?)
- Cervical spine fracture from other mechanism
- Carotid dissection (spontaneous or other traumatic mechanism)
- Laryngeal fracture from blunt neck trauma (non-hanging mechanism)
- Intimate partner violence with non-fatal strangulation (often underreported — screen specifically)

## Workup

- **CT cervical spine:** Exclude fracture (C2 hangman fracture, other cervical injuries)
- **CTA neck (carotid and vertebral arteries):** Identify dissection, thrombosis, pseudoaneurysm. Sensitivity > 95%. Must include from aortic arch to circle of Willis.
- **CT head:** Anoxic brain injury — diffuse edema, loss of grey-white differentiation, basal ganglia changes. MRI more sensitive (obtain at 24-72 hours for prognostication).
- **CT soft tissues of neck:** Laryngeal fracture, prevertebral soft tissue swelling, subcutaneous emphysema
- **Flexible laryngoscopy (ENT):** Assess vocal cord mobility, mucosal injury, laryngeal framework integrity
- **CXR:** Aspiration pneumonia, post-obstructive pulmonary edema
- **Labs:** CBC, BMP, LFTs, coagulation studies, lactate, ABG, CK (rhabdomyolysis from prolonged suspension), troponin (cardiac injury from arrest/hypoxia)
- **Toxicology screen:** Co-ingestants common in suicidal hanging
- **ECG:** Arrhythmia from hypoxia or vagal injury

## Treatment

**Airway management:**
- Serial airway assessments q1-2h for 24 hours — delayed airway edema can develop
- Dexamethasone 10 mg IV x 1, then 4 mg IV q6h x 48h (reduce airway edema — limited evidence but commonly used)
- Nebulized racemic epinephrine 0.5 mL of 2.25% in 3 mL NS q2-4h for stridor
- Heliox (70:30 helium:oxygen) for stridor if adequate oxygenation maintained
- Definitive airway if progressive symptoms (see Critical Actions)

**Vascular injury management:**
- Carotid/vertebral dissection: anticoagulation vs. antiplatelet therapy per neurology/neurosurgery
  - Heparin drip (goal PTT 60-80) if acute thrombus/stroke without hemorrhage
  - Aspirin 325 mg PO if dissection without stroke
  - Endovascular stenting for pseudoaneurysm or flow-limiting dissection
- Serial neurological exams for delayed stroke (can occur 24-72 hours after dissection)

**Anoxic brain injury management:**
- Targeted temperature management: 32-36°C for 24 hours if comatose after ROSC (per post-cardiac arrest guidelines)
- Seizure management: levetiracetam 1000 mg IV load, then 500 mg IV q12h. Lorazepam 4 mg IV for active seizure.
- Avoid hypotension (MAP > 65), hypoxia (SpO2 > 94%), hyperglycemia (target glucose 140-180)
- ICP monitoring if GCS ≤ 8 with cerebral edema on CT
- MRI brain at 48-72 hours for prognostication (diffusion restriction pattern, cortical injury extent)

**Post-obstructive pulmonary edema:**
- Develops rapidly after relief of airway obstruction — "flash" pulmonary edema
- Treatment: positive pressure ventilation (CPAP/BiPAP or intubation), diuresis if fluid overloaded (furosemide 40 mg IV), supportive
- Usually resolves within 24-48 hours

**Cervical spine fracture:** Manage per cervical-spine-fracture protocol if identified.

## Disposition

- **ICU:** Altered mental status, intubated, post-cardiac arrest, anoxic brain injury, vascular dissection
- **Admit (minimum 24 hours):** All near-hanging/strangulation victims — delayed airway compromise, pulmonary edema, and vascular complications can develop over 24-48 hours
- **ENT consult:** Hoarseness, stridor, suspected laryngeal fracture
- **Neurology/neurosurgery consult:** Carotid/vertebral dissection, anoxic brain injury, stroke
- **Psychiatry consult:** Mandatory for all suicidal hanging — 1:1 observation, safety evaluation
- **Social work/domestic violence advocacy:** All strangulation cases — assess for intimate partner violence (strangulation is a risk factor for future homicide)
- **Law enforcement notification:** Per local requirements for assault/DV cases

## Pitfalls

1. **Underestimating the severity of strangulation injuries.** Victims may appear well initially despite carotid dissection, laryngeal fracture, or evolving anoxic injury. All strangulation/hanging victims need 24-hour observation minimum.

2. **Using carotid Doppler instead of CTA.** Doppler cannot adequately assess for dissection, intimal tears, or pseudoaneurysm. CTA from arch to vertex is the required study.

3. **Not immobilizing the cervical spine.** While C-spine fractures are rare in non-judicial hanging, they cannot be excluded without CT. Maintain immobilization during airway management.

4. **Discharging a patient who "looks fine" after strangulation.** Delayed stroke from carotid dissection (24-72 hours), delayed airway edema (12-24 hours), and post-obstructive pulmonary edema can all present after initial improvement.

5. **Not screening for intimate partner violence in strangulation cases.** Non-fatal strangulation is one of the strongest predictors of future lethal domestic violence. Every strangulation case — regardless of stated mechanism — warrants DV screening and safety planning.

6. **Failing to obtain psychiatric evaluation for suicidal hanging survivors.** Hanging has the highest case fatality rate of any suicide method after firearms. Survivors require immediate psychiatric evaluation, 1:1 safety monitoring, and inpatient psychiatric admission when medically cleared.

7. **Not anticipating difficult airway.** Laryngeal edema, fracture, and blood can make standard laryngoscopy impossible. Have surgical airway equipment and ENT backup immediately available for any hanging/strangulation patient with voice changes.
