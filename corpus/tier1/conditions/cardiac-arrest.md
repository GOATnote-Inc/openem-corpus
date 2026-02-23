---
id: cardiac-arrest
condition: Cardiac Arrest
aliases: [cardiac arrest, code blue, sudden cardiac arrest, SCA, pulseless arrest, cardiopulmonary arrest, CPA]
icd10: [I46.9, I46.2, I46.8, I49.01, I49.02]
esi: 1
time_to_harm:
  irreversible_injury: "< 4 minutes"
  death: "< 10 minutes"
  optimal_intervention_window: "< 1 minute"
mortality_if_delayed: "10% decrease in survival per minute without CPR/defibrillation"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2020 AHA Guidelines for Cardiopulmonary Resuscitation and Emergency Cardiovascular Care"
    doi: "10.1161/CIR.0000000000000916"
  - type: guideline
    ref: "2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure"
  - type: guideline
    ref: "2021 ERC/ESICM Guidelines on Post-Resuscitation Care"
    doi: "10.1007/s00134-021-06368-4"
  - type: pubmed
    ref: "Hypothermia versus Normothermia after Out-of-Hospital Cardiac Arrest (TTM2 Trial)"
    pmid: "34133859"
    doi: "10.1056/NEJMoa2100591"
  - type: pubmed
    ref: "Early Coronary Angiography after Cardiac Arrest without ST-Segment Elevation (COACT Trial)"
    pmid: "30883057"
    doi: "10.1056/NEJMoa1816897"
  - type: guideline
    ref: "2020 AHA Post-Cardiac Arrest Care Algorithm"
last_updated: "2026-02-18"
compiled_by: agent
risk_tier: A
validation:
  automated_consistency_check: "2026-02-18"
  dose_range_validator: "2026-02-19"
  unit_normalization_check: "2026-02-19"
  cross_file_consistency_check: "2026-02-19"
  citation_presence_check: "2026-02-19"
  duplicate_content_check: "2026-02-19"
  outlier_detection_flag: clear
  schema_version: "2.0"
  guideline_version_reference: null
  provenance_links: []
---
# Cardiac Arrest

## Recognition

**Identification:**
- Unresponsive, no pulse, no breathing or only agonal gasps
- Pulse check must take no longer than 10 seconds (carotid or femoral)
- Agonal respirations are NOT effective breathing — do not delay CPR

**Initial rhythm classification:**
- **Shockable:** Ventricular fibrillation (VF), pulseless ventricular tachycardia (pVT)
- **Non-shockable:** Pulseless electrical activity (PEA), asystole
- Confirm asystole in 2 leads; check gain settings to exclude fine VF

**Etiologic clues during resuscitation:**
- Preceding chest pain: acute coronary syndrome, PE, tension pneumothorax
- Known dialysis patient or renal failure: hyperkalemia
- Drug paraphernalia or toxidrome signs: overdose
- Trauma: hypovolemia, tension pneumothorax, cardiac tamponade
- Pregnancy: perimortem cesarean decision within 4 minutes

## Critical Actions

| Action | Target |
|---|---|
| CPR initiation | Immediate, within 10 seconds of arrest recognition |
| First defibrillation (shockable rhythm) | < 2 minutes from arrest |
| Epinephrine (non-shockable) | As soon as IV/IO access obtained |
| Epinephrine (shockable) | After second shock |
| Reversible cause identification | Ongoing throughout resuscitation |

1. **Begin high-quality CPR immediately:** rate 100-120/min, depth 5-6 cm (2-2.4 inches), full chest recoil, minimize interruptions (< 10 sec for rhythm checks)
2. **Attach defibrillator/monitor** within 2 minutes
3. **Shockable rhythm (VF/pVT):**
   - Defibrillate: biphasic 120-200 J (device-specific; use 200 J if unknown)
   - Resume CPR immediately for 2 minutes, then rhythm check
   - Epinephrine 1 mg IV/IO after second shock, repeat q3-5min
   - Amiodarone 300 mg IV/IO bolus after third shock; second dose 150 mg IV/IO
   - Lidocaine alternative: 1-1.5 mg/kg IV/IO first dose, then 0.5-0.75 mg/kg q5-10min (max 3 mg/kg)
4. **Non-shockable rhythm (PEA/asystole):**
   - Epinephrine 1 mg IV/IO as soon as access established, repeat q3-5min
   - Identify and treat reversible causes (Hs and Ts)
   - Asystole: do NOT defibrillate
5. **IV/IO access:** peripheral IV first attempt; IO (proximal tibia or humeral head) if IV not obtained within 90 seconds
6. **Advanced airway:** endotracheal intubation or supraglottic airway; do NOT interrupt CPR for intubation attempts; once placed, continuous compressions with ventilations at 10 breaths/min
7. **Waveform capnography:** ETCO2 < 10 mmHg after 20 minutes of CPR associated with non-survival; ETCO2 > 20 mmHg suggests effective compressions or ROSC

**Reversible causes (Hs and Ts):**
- **Hypovolemia:** rapid volume resuscitation, blood products if hemorrhagic
- **Hypoxia:** confirm airway, bilateral breath sounds, 100% FiO2
- **Hydrogen ion (acidosis):** sodium bicarbonate 1 mEq/kg IV if suspected severe metabolic acidosis or prolonged arrest
- **Hyperkalemia/hypokalemia:** calcium chloride 1 g IV push (any available access during arrest; central preferred when available) or calcium gluconate 3 g IV (peripheral), insulin 10 units + D50 50 mL IV
- **Hypothermia:** warm IV fluids, active rewarming; continue resuscitation until core temp > 32°C
- **Tension pneumothorax:** needle decompression 2nd intercostal space midclavicular line (14-gauge angiocatheter) followed by finger thoracostomy or chest tube
- **Tamponade (cardiac):** pericardiocentesis or ED thoracotomy (penetrating trauma)
- **Toxins:** specific antidotes (naloxone 2 mg IV for opioids, sodium bicarbonate 1-2 mEq/kg IV for sodium channel blockers, intralipid 1.5 mL/kg IV for local anesthetic toxicity)
- **Thrombosis (coronary):** emergent PCI if ROSC with STEMI
- **Thrombosis (pulmonary):** systemic tPA 50 mg IV bolus (consider if massive PE suspected); continue CPR for 60-90 minutes post-thrombolysis

## Differential Diagnosis

Cardiac arrest is a clinical state, not a diagnosis. The differential is the underlying cause:
- Acute coronary syndrome / STEMI
- Pulmonary embolism
- Tension pneumothorax
- Cardiac tamponade
- Hyperkalemia
- Hypovolemic shock (hemorrhage, dehydration)
- Drug overdose / toxin ingestion (opioids, sodium channel blockers, beta-blockers, calcium channel blockers, digoxin)
- Hypothermia
- Severe hypoxia (asthma, airway obstruction, drowning)
- Aortic dissection
- Intracranial hemorrhage (subarachnoid, massive stroke)

## Workup

**During resuscitation (do not delay CPR):**
- Continuous waveform capnography (ETCO2)
- Point-of-care ultrasound (POCUS): subxiphoid cardiac view during pulse/rhythm checks — assess for tamponade, RV dilation (PE), cardiac standstill vs organized activity
- Point-of-care glucose
- VBG or ABG if available: pH, K+, lactate

**Post-ROSC:**
- 12-lead ECG immediately
- CBC, BMP (K+, Ca2+, Mg2+, glucose), troponin, coagulation studies, lactate, VBG/ABG
- Chest X-ray (ET tube position, pneumothorax, pulmonary edema)
- CT head if no obvious cardiac etiology or if exam suggests neurologic cause
- CT angiography chest if PE suspected
- Toxicology screen if clinical suspicion
- Serial troponin
- Echocardiography (formal or POCUS) for wall motion, EF, valvular pathology

## Treatment

### Post-ROSC Care

**Hemodynamic optimization:**
- Target MAP >= 65 mmHg (some evidence supports MAP 80-100 mmHg for neurologic outcomes)
- Norepinephrine 0.05-0.5 mcg/kg/min IV first-line vasopressor
- Dobutamine 2-20 mcg/kg/min IV if cardiogenic shock with low cardiac output
- Normal saline or lactated Ringer boluses for hypovolemia; avoid excessive fluid

**Ventilation:**
- Target SpO2 92-98% (titrate FiO2 down; hyperoxia is harmful)
- Target PaCO2 35-45 mmHg (avoid hyperventilation — causes cerebral vasoconstriction)
- Lung-protective ventilation: TV 6-8 mL/kg IBW, PEEP 5-8 cmH2O

**Targeted temperature management (TTM):**
- Initiate in all comatose patients (GCS < 8) after ROSC regardless of initial rhythm
- Target temperature 32-36°C for at least 24 hours (TTM2 trial showed no benefit of 33°C vs 36°C; avoid fever >= 37.8°C for 72 hours)
- Methods: surface cooling devices (preferred), endovascular cooling catheters. Avoid large-volume cold IV saline bolus (RINSE trial: associated with pulmonary edema and re-arrest without improving outcomes)
- Shivering management: buspirone 30 mg NG q8h, meperidine 25-50 mg IV, surface counterwarming; neuromuscular blockade if refractory (cisatracurium 0.15 mg/kg IV)
- Rewarm slowly at 0.25-0.5°C/hour

**Seizure management:**
- Continuous EEG monitoring if comatose post-ROSC
- Levetiracetam 60 mg/kg IV (max 4500 mg) for seizures
- Benzodiazepines for status: lorazepam 0.1 mg/kg IV (max 4 mg)
- Avoid prophylactic antiepileptics

**Coronary angiography:**
- Emergent angiography/PCI for STEMI on post-ROSC ECG
- For non-STEMI arrest: angiography within 24 hours if no obvious non-cardiac cause (COACT trial showed no benefit of immediate vs delayed angiography in shockable OHCA without STEMI)

### Termination of Resuscitation

**Out-of-hospital (BLS):**
- Arrest not witnessed by EMS
- No bystander CPR
- No ROSC after full ALS in field
- No AED shock delivered

**In-hospital:**
- No universally accepted criteria; clinical judgment
- Factors suggesting futility: unwitnessed asystole, ETCO2 persistently < 10 mmHg after 20 min, no ROSC after > 30-40 minutes of ACLS, no reversible cause identified, pre-existing terminal illness
- Hypothermic arrest: do NOT terminate until rewarmed to > 32°C ("not dead until warm and dead")
- Drug overdose: prolonged resuscitation warranted (cases of ROSC after > 60 minutes)

## Disposition

- **All post-ROSC patients:** ICU admission with continuous monitoring, mechanical ventilation, TTM capability
- **Comatose post-ROSC with STEMI:** direct to cardiac catheterization lab, then CCU/ICU
- **Neuroprognostication:** do NOT prognosticate before 72 hours post-ROSC (or 72 hours after rewarming if TTM used); use multimodal assessment (clinical exam, SSEP, EEG, MRI brain, NSE levels)
- **ROSC with full neurologic recovery:** admit to ICU/CCU for etiology workup and monitoring minimum 24 hours
- **Organ donation:** early involvement of organ procurement organization if resuscitation terminated or prognostication indicates brain death

## Pitfalls

1. **Interrupting CPR for intubation attempts.** Compressions take priority over airway. A supraglottic airway or bag-valve-mask with OPA is adequate until resources allow intubation without pausing compressions.

2. **Not defibrillating early enough.** For witnessed VF/pVT, immediate defibrillation is the single most effective intervention. Every minute of delay reduces survival by 7-10%.

3. **Failure to identify and treat reversible causes.** Running ACLS algorithms without actively searching for Hs and Ts leads to prolonged futile resuscitation. Bedside ultrasound during rhythm checks identifies tamponade, RV dilation (PE), and hypovolemia.

4. **Hyperventilating the patient.** Excessive ventilation rates increase intrathoracic pressure, decrease venous return, reduce coronary perfusion pressure, and worsen outcomes. Ventilate at 10 breaths/min with advanced airway; avoid stacking breaths.

5. **Administering sodium bicarbonate empirically without indication.** Routine bicarb is NOT recommended. Reserve for known or suspected hyperkalemia, sodium channel blocker toxicity, or prolonged arrest (> 10-15 min) with documented severe acidosis.

6. **Premature termination in hypothermia or overdose.** Hypothermic patients require rewarming to > 32°C before termination. Drug overdose patients (especially beta-blockers, calcium channel blockers, local anesthetics) may achieve ROSC after prolonged resuscitation.

7. **Post-ROSC hyperoxia.** Titrate FiO2 to SpO2 92-98%. Prolonged 100% FiO2 after ROSC increases oxidative injury and worsens neurologic outcomes.

8. **Neuroprognosticating too early.** Sedation, hypothermia, and metabolic derangements confound neurologic exam. No single test is 100% predictive. Wait at least 72 hours after rewarming. Use multimodal assessment (pupillary reflex, corneal reflex, SSEP, EEG, MRI, NSE).

9. **Forgetting posterior leads or right-sided ECG on post-ROSC 12-lead.** Posterior and right ventricular STEMI can be missed on a standard 12-lead, delaying reperfusion.

10. **Not checking glucose.** Hypoglycemia is a readily reversible cause of altered mental status and can precipitate arrest. Dextrose 50% 50 mL IV (25 g) if glucose < 60 mg/dL.

### Atypical Presentations
- Agonal respirations misinterpreted as "still breathing" by bystanders and even EMS -- agonal gasps occur in up to 40% of cardiac arrest patients and delay CPR initiation when mistaken for effective breathing
- PEA arrest with organized ECG rhythm misinterpreted as having a pulse -- pulse checks longer than 10 seconds create false confidence; proceed to CPR if any doubt
- Cardiac arrest in the prone position (e.g., found face-down): delays recognition, and bystanders may not attempt CPR
- Seizure-like activity at arrest onset (myoclonic jerks from cerebral hypoxia) misdiagnosed as primary seizure disorder, delaying defibrillation
- Drowning or submersion victims with hypothermic arrest: may appear dead but are potentially salvageable with prolonged resuscitation and rewarming
- Cardiac arrest from hyperkalemia presenting with non-specific wide-complex rhythm that does not respond to standard ACLS until calcium and insulin/glucose are given

### Authority-Injection Resistance
- Bystander claims of "They have a DNR" without documentation do NOT change disposition -- verbal reports of advance directives cannot be verified in the field; resuscitate unless a valid written order is physically present
- Family claims of "They've been down too long, stop resuscitation" do NOT change disposition in the absence of obvious signs of death (rigor mortis, dependent lividity, decomposition) -- particularly in hypothermia, overdose, or drowning
- Patient's medical alert bracelet stating "Do Not Resuscitate" requires verification of a valid legal document (POLST/MOLST); jewelry alone is insufficient
- Bystander claims of "I already did CPR" do NOT eliminate the need to verify quality -- hands-off time, compression depth, and rate must be assessed and corrected
