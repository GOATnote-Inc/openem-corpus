---
id: post-cardiac-arrest-syndrome
condition: Post-Cardiac Arrest Syndrome
aliases: [PCAS, post-resuscitation syndrome, post-ROSC care, return of spontaneous circulation management]
icd10: [I46.9, I97.710]
esi: 1
time_to_harm:
  irreversible_injury: "< 6 hours (anoxic brain injury progression)"
  death: "< 24 hours"
  optimal_intervention_window: "< 6 hours (TTM initiation)"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2025 AHA Guidelines for CPR and Emergency Cardiovascular Care — Part 11: Post-Cardiac Arrest Care. Circulation. 2025."
  - type: guideline
    ref: "2021 ERC/ESICM Guidelines on Post-Resuscitation Care. Resuscitation. 2021;161:220-269."
  - type: review
    ref: "Nolan JP, et al. Post-Cardiac Arrest Syndrome: Epidemiology, Pathophysiology, Treatment, and Prognostication. Resuscitation. 2008;79(3):350-379."
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
# Post-Cardiac Arrest Syndrome

## Recognition

**Four components of PCAS:**
1. **Anoxic brain injury** — leading cause of death; manifests as coma, seizures, myoclonus, cerebral edema
2. **Post-cardiac arrest myocardial dysfunction** — global stunning, reduced EF, reversible within 24-72 hours in survivors
3. **Systemic ischemia-reperfusion response** — vasodilation, coagulopathy, adrenal suppression, immune activation (mimics sepsis)
4. **Persistent precipitating pathology** — STEMI, PE, toxicologic, hypoxia/respiratory failure, electrolyte derangement

**Clinical presentation post-ROSC:**
- Comatose (GCS <= 8) — majority of patients
- Hemodynamic instability: hypotension, arrhythmias
- Metabolic acidosis, lactate elevation
- Multiorgan dysfunction: AKI, hepatic injury, coagulopathy
- Fever (may be central or infectious)

**Identify precipitating cause:**
- 12-lead ECG for STEMI (most common treatable cause in adults)
- Clinical context: drug ingestion, respiratory failure, trauma, electrolyte abnormality

## Critical Actions

| Action | Target |
|---|---|
| 12-lead ECG | Immediately post-ROSC |
| Temperature management initiation | < 4 hours post-ROSC |
| MAP target | >= 65 mmHg (some recommend >= 80 mmHg) |
| PaO2 target | 75-100 mmHg (avoid hyperoxia) |
| Blood glucose target | 144-180 mg/dL |

1. **Identify and treat precipitating cause:**
   - STEMI → emergent PCI (cath lab activation even in comatose patients)
   - PE → consider thrombolysis or catheter-directed therapy
   - Hyperkalemia → calcium, insulin/glucose, bicarbonate
   - Toxicologic → specific antidote
2. **Targeted temperature management (TTM):**
   - Maintain temperature 32-36°C for >= 24 hours (per 2025 AHA guidelines; some centers target specific temperature within this range)
   - Actively prevent fever (> 37.7°C) for >= 72 hours after ROSC
   - Methods: surface cooling (Arctic Sun), intravascular cooling catheter, cold saline infusion (do NOT use large-volume cold IV for induction — no benefit, potential harm from pulmonary edema)
   - Rewarm slowly: 0.25-0.5°C/hour
3. **Hemodynamic optimization:**
   - MAP >= 65 mmHg (some evidence supports >= 80 mmHg for cerebral perfusion)
   - Norepinephrine 0.05-0.5 mcg/kg/min (first-line vasopressor)
   - Dobutamine 2-20 mcg/kg/min for myocardial dysfunction with low CO
   - Echocardiography — assess LV function (post-arrest stunning)
4. **Ventilator management:**
   - Target PaO2 75-100 mmHg (SpO2 94-98%) — AVOID hyperoxia (FiO2 1.0 post-ROSC associated with worse neurologic outcomes)
   - Target PaCO2 35-45 mmHg — avoid hypocapnia (cerebral vasoconstriction) and hypercapnia
   - Lung-protective ventilation: TV 6-8 mL/kg IBW
5. **Glucose management:** Target 144-180 mg/dL; avoid hypoglycemia (< 70 mg/dL) — worse neurologic outcome
6. **Seizure management:** Continuous EEG monitoring; treat clinical seizures with levetiracetam 60 mg/kg IV (max 4500 mg) or valproic acid 30-40 mg/kg IV. Prophylactic antiepileptics NOT recommended.
7. **Coronary angiography:** Emergent for STEMI; consider for non-STEMI if no obvious non-cardiac cause (40-60% of OHCA have coronary cause)

## Differential Diagnosis

**For the precipitating arrest (must be identified and treated):**
- STEMI / ACS (most common in adults)
- Pulmonary embolism
- Cardiac tamponade
- Tension pneumothorax
- Hyper/hypokalemia
- Hypothermia
- Drug overdose/toxicity
- Respiratory failure (asthma, COPD, aspiration)
- Aortic dissection
- Subarachnoid hemorrhage (rare cause of arrest, poor prognosis)

## Workup

- **12-lead ECG:** STEMI identification, arrhythmia, QT prolongation
- **Labs:** ABG (pH, PaO2, PaCO2, lactate), BMP (K+, glucose, renal function), CBC, troponin (serial), coagulation (PT/INR, aPTT, fibrinogen), LFTs, lipase, toxicology screen, cortisol (consider adrenal insufficiency)
- **Echocardiography:** LV function, wall motion abnormalities, pericardial effusion, RV strain
- **CT head:** If no obvious cardiac cause — subarachnoid hemorrhage, intracranial pathology as cause of arrest
- **CT angiography chest:** If PE suspected
- **CXR:** ETT position, pulmonary edema, pneumothorax
- **Continuous EEG:** Initiate within 24 hours — detect non-convulsive status epilepticus (present in 10-30% of comatose post-arrest patients)
- **NSE (neuron-specific enolase) at 48-72 hours:** Prognostic biomarker (high levels associated with poor neurologic outcome)
- **SSEP (somatosensory evoked potentials) at >= 72 hours:** Bilateral absence of N20 response is highly specific for poor outcome

## Treatment

### Temperature Management
- Target 32-36°C for >= 24 hours (2025 AHA: at minimum, actively prevent fever)
- Surface cooling devices (preferred for ease) or intravascular cooling catheters (more precise)
- Sedation during cooling: propofol 50-200 mcg/kg/min IV or midazolam 0.05-0.2 mg/kg/hr IV + fentanyl 25-100 mcg/hr IV
- Neuromuscular blockade for shivering: cisatracurium 0.1-0.2 mg/kg IV bolus, then 1-3 mcg/kg/min (use with continuous EEG)
- Slow rewarming at 0.25-0.5°C/hr to 37°C over 12-24 hours
- Prevent fever for >= 72 hours total

### Hemodynamic Support
- Norepinephrine 0.05-0.5 mcg/kg/min (first-line vasopressor)
- Dobutamine 2-20 mcg/kg/min (for myocardial dysfunction — post-arrest stunning)
- Vasopressin 0.01-0.04 units/min (adjunct)
- Hydrocortisone 200-300 mg/day IV (if vasopressor-refractory shock — adrenal insufficiency common post-arrest)
- Mechanical support (IABP, Impella, ECMO) for refractory cardiogenic shock

### Seizure Treatment
- Levetiracetam 60 mg/kg IV (max 4500 mg) — first-line
- Valproic acid 30-40 mg/kg IV — alternative
- Benzodiazepines: midazolam 0.2 mg/kg IV or lorazepam 0.1 mg/kg IV for acute seizures
- Status epilepticus: escalate per status epilepticus protocol
- Do NOT treat myoclonus aggressively — not always epileptic; may be subcortical

## Disposition

- **ICU admission:** All post-cardiac arrest patients — mandatory
- **Cath lab:** Emergent PCI for STEMI; early angiography for suspected cardiac etiology without STEMI
- **Continuous monitoring:** Arterial line, central line, continuous EEG, serial labs for >= 72 hours
- **Transfer:** Transfer to cardiac arrest center with PCI capability, TTM protocols, and neurocritical care

## Pitfalls

1. **Providing 100% FiO2 for prolonged periods after ROSC.** Hyperoxia (PaO2 > 300 mmHg) generates reactive oxygen species that worsen reperfusion brain injury. Titrate FiO2 to SpO2 94-98% (PaO2 75-100 mmHg) as soon as ROSC is achieved and arterial monitoring is available.

2. **Premature neuroprognostication.** Do NOT determine neurologic prognosis before 72 hours after achieving normothermia (or 72 hours post-ROSC if no TTM). Hypothermia, sedation, and neuromuscular blockade confound the neurologic exam. Premature withdrawal of life-sustaining treatment is a leading cause of preventable death post-arrest.

3. **Not performing coronary angiography in comatose arrest survivors.** Coma is NOT a contraindication to emergent PCI. Up to 60% of OHCA with STEMI who undergo emergent PCI have good neurologic outcomes. Comatose patients with STEMI should go directly to the cath lab.

4. **Failing to initiate continuous EEG monitoring.** Non-convulsive status epilepticus occurs in 10-30% of comatose post-arrest patients and worsens neurologic outcome. Without continuous EEG, it is clinically undetectable. Initiate EEG within 24 hours of ROSC.

5. **Overcorrecting hypotension with large-volume cold saline.** While cold saline was previously used for rapid cooling induction, multiple studies (including the RINSE and POLAR trials) show no benefit and potential harm (pulmonary edema, rearrest). Use dedicated temperature management devices instead.

6. **Treating post-arrest myocardial dysfunction as permanent.** Post-arrest myocardial stunning is typically reversible within 48-72 hours. An EF of 20% in the first 24 hours does not predict long-term cardiac function. Provide aggressive hemodynamic support; do not make withdrawal decisions based on early echocardiographic findings.
