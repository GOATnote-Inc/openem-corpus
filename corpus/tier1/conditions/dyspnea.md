---
id: dyspnea
condition: "Dyspnea — Emergency Evaluation"
aliases: [shortness of breath, SOB, difficulty breathing, breathlessness, air hunger, respiratory distress]
icd10: [R06.00, R06.02, R06.09]
esi: 2
time_to_harm:
  irreversible_injury: "< 30 minutes (airway obstruction)"
  death: "< 10 minutes (complete airway obstruction, tension pneumothorax)"
  optimal_intervention_window: "< 60 minutes (most reversible causes)"
category: presentations
condition_type: presentation
chief_complaint: "Dyspnea"
differential_categories:
  - category: life-threatening
    conditions:
      - tension-pneumothorax
      - pulmonary-embolism
      - cardiac-tamponade
      - anaphylaxis
      - airway-obstruction-upper
      - acute-respiratory-failure
      - stemi
      - acute-heart-failure
      - ards
  - category: emergent
    conditions:
      - acute-asthma-exacerbation
      - copd-exacerbation
      - spontaneous-pneumothorax
      - pneumonia
      - pleural-effusion-emergency
      - angioedema
      - epiglottitis
      - pulmonary-hypertension-crisis
  - category: urgent
    conditions:
      - covid-pneumonia-severe
      - aspiration-pneumonia
      - pericarditis-myocarditis
  - category: non-emergent
    conditions:
      - panic-attack
red_flags:
  - "Stridor or inability to speak in full sentences"
  - "SpO2 < 90% on room air"
  - "Accessory muscle use, tripod positioning"
  - "Altered mental status with respiratory distress"
  - "Sudden onset at rest"
  - "Unilateral absent breath sounds"
  - "Facial or tongue swelling"
  - "Diffuse wheezing with hypotension (anaphylaxis)"
  - "Acute onset after immobilization, surgery, or long travel"
  - "Diaphoresis with chest pressure"
decision_rules:
  - name: "Wells Criteria for PE"
    citation: "Wells PS et al. Derivation of a simple clinical model to categorize patients probability of pulmonary embolism. Thromb Haemost. 2000;83(3):416-420."
    pmid: "10744147"
  - name: "PERC Rule"
    citation: "Kline JA et al. Clinical criteria to prevent unnecessary diagnostic testing in emergency department patients with suspected pulmonary embolism. J Thromb Haemost. 2004;2(8):1247-1255."
    pmid: "15304025"
  - name: "BNP/NT-proBNP for Heart Failure"
    citation: "Maisel AS et al. Rapid measurement of B-type natriuretic peptide in the emergency diagnosis of heart failure. N Engl J Med. 2002;347(3):161-167."
    pmid: "12124404"
track: tier1
sources:
  - type: guideline
    ref: "ACEP Clinical Policy: Critical Issues in the Evaluation and Management of Adult Patients Presenting to the Emergency Department With Acute Dyspnea. Ann Emerg Med. 2014;63(5):e15-e68."
  - type: guideline
    ref: "2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure"
    doi: "10.1161/CIR.0000000000001063"
  - type: guideline
    ref: "2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism"
    doi: "10.1093/eurheartj/ehz405"
  - type: guideline
    ref: "2023 GINA Global Strategy for Asthma Management and Prevention"
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
# Dyspnea — Emergency Evaluation

## Recognition

Dyspnea is the second most common chief complaint in US EDs (~3.5 million visits/year). The differential is broad, spanning pulmonary, cardiac, upper airway, metabolic, and psychiatric etiologies. The goal is rapid identification of immediately life-threatening causes.

**Key history elements:**
- Onset: acute (seconds-minutes: PE, pneumothorax, anaphylaxis) vs subacute (hours-days: pneumonia, HF exacerbation, asthma)
- Positional: orthopnea/PND (heart failure), platypnea (hepatopulmonary syndrome, ASD)
- Associated symptoms: chest pain (ACS, PE, pneumothorax), wheezing (asthma, COPD, anaphylaxis), stridor (upper airway obstruction), fever (pneumonia, epiglottitis), leg swelling (DVT/PE, HF)
- Triggers: allergen exposure (anaphylaxis), exertion, emotional stress
- Medical history: HF, COPD, asthma, malignancy, recent surgery/immobilization, intubation history
- Medications: ACE inhibitors (angioedema), beta-blockers (bronchospasm), anticoagulation status

**Rapid visual assessment:**
- Work of breathing: accessory muscle use, nasal flaring, intercostal retractions
- Position: tripod (COPD/asthma), upright with legs dangling (HF)
- Ability to speak: full sentences vs phrases vs words vs unable (correlates with severity)
- Skin: cyanosis, urticaria (anaphylaxis), mottling (shock)
- Stridor: inspiratory (supraglottic), biphasic (glottic/subglottic), expiratory (lower trachea)

## Critical Actions

| Action | Target |
|---|---|
| SpO2 measurement | Immediate on arrival |
| Supplemental O2 if SpO2 < 94% | < 2 minutes |
| Airway assessment | < 2 minutes |
| Identify life threat | < 10 minutes |
| CXR or bedside ultrasound | < 30 minutes |

**Evaluation algorithm:**

1. **Assess airway patency and breathing effort.** Stridor, drooling, inability to phonate → prepare for immediate airway management. Do NOT lay the patient supine if epiglottitis suspected.

2. **Correct hypoxemia.** Nasal cannula 2-6 L/min → simple face mask 6-10 L/min → non-rebreather 15 L/min → BIPAP/CPAP → intubation. Target SpO2 92-96% (88-92% in COPD with known CO2 retention).

3. **Bedside assessment (POCUS within 5 minutes for unstable patients):**
   - Lung: B-lines (pulmonary edema), absent lung sliding (pneumothorax), consolidation (pneumonia), pleural effusion
   - Heart: pericardial effusion (tamponade), RV dilation (PE), global LV dysfunction (HF)
   - IVC: plethoric (RV failure, tamponade) vs flat (volume depletion, sepsis)

4. **Pattern recognition for immediate intervention:**
   - Unilateral absent breath sounds + hypotension → needle decompression for tension pneumothorax
   - Urticaria + wheezing + hypotension → epinephrine 0.3-0.5 mg IM for anaphylaxis
   - Stridor + drooling → prepare surgical airway, do NOT attempt blind intubation
   - Bilateral crackles + JVD + peripheral edema → IV nitroglycerin + BIPAP for acute HF
   - Wheezing + air trapping + prolonged expiration → bronchodilators for asthma/COPD

5. **Risk stratify for PE.** Apply Wells criteria to all acute dyspnea without clear alternative diagnosis. Low pretest probability → PERC rule → D-dimer → CTA as needed.

6. **Differentiate cardiac vs pulmonary.** BNP/NT-proBNP: BNP > 400 pg/mL or NT-proBNP > 900 pg/mL (age < 50), > 1800 (age > 50) supports HF. BNP < 100 essentially excludes HF as cause.

## Differential Diagnosis

### Life-Threatening
- **Tension pneumothorax** (`tension-pneumothorax`): unilateral absent breath sounds, tracheal deviation, hypotension, JVD. Clinical diagnosis — do NOT delay for imaging.
- **Pulmonary embolism** (`pulmonary-embolism`): acute dyspnea with tachycardia, pleuritic chest pain, risk factors for VTE, hypoxia out of proportion to exam findings
- **Cardiac tamponade** (`cardiac-tamponade`): JVD, hypotension, muffled heart sounds, pulsus paradoxus
- **Anaphylaxis** (`anaphylaxis`): urticaria, angioedema, wheezing, hypotension, exposure history
- **Upper airway obstruction** (`airway-obstruction-upper`): stridor, drooling, voice changes, foreign body history
- **Acute respiratory failure** (`acute-respiratory-failure`): SpO2 < 90%, altered mental status, severe accessory muscle use, impending respiratory arrest
- **ACS with heart failure** (`stemi`, `acute-heart-failure`): flash pulmonary edema from acute MI, dyspnea as anginal equivalent
- **ARDS** (`ards`): bilateral infiltrates, severe hypoxemia (P/F ratio < 300), no cardiogenic cause

### Emergent
- **Acute asthma exacerbation** (`acute-asthma-exacerbation`): wheezing, prolonged expiratory phase, peak flow < 50% predicted. Silent chest = critical (no air movement).
- **COPD exacerbation** (`copd-exacerbation`): increased sputum, worsening dyspnea, wheezing/rhonchi, CO2 retention on VBG
- **Spontaneous pneumothorax** (`spontaneous-pneumothorax`): sudden pleuritic pain, decreased breath sounds, tall thin habitus, history of blebs
- **Pneumonia** (`pneumonia`): fever, productive cough, focal crackles/consolidation, leukocytosis
- **Pleural effusion** (`pleural-effusion-emergency`): dyspnea, dullness to percussion, decreased breath sounds at base
- **Angioedema** (`angioedema`): lip/tongue/uvula swelling, ACE-inhibitor use, may lack urticaria (bradykinin-mediated)
- **Epiglottitis** (`epiglottitis`): sore throat, muffled voice, drooling, fever, dysphagia (adults)
- **Pulmonary hypertension crisis** (`pulmonary-hypertension-crisis`): known PAH with acute decompensation, syncope, RV failure

### Urgent
- **COVID/viral pneumonia** (`covid-pneumonia-severe`): hypoxemia out of proportion to subjective dyspnea ("happy hypoxia"), bilateral ground glass opacities
- **Aspiration pneumonia** (`aspiration-pneumonia`): altered mental status, swallowing dysfunction, fever, infiltrate in dependent segments
- **Pericarditis/myocarditis** (`pericarditis-myocarditis`): pleuritic chest pain, friction rub, diffuse ST elevation

### Non-Emergent (diagnosis of exclusion)
- **Panic attack** (`panic-attack`): hyperventilation, paresthesias, sense of doom. Diagnosis of exclusion ONLY after objective evaluation complete. Normal SpO2, ECG, CXR.
- Metabolic acidosis (DKA, toxic ingestion): Kussmaul breathing — deep, rapid respirations. Check glucose, VBG/ABG, anion gap.
- Anemia: gradual onset, exertional, check hemoglobin

## Workup

**All patients:**
- Continuous pulse oximetry
- 12-lead ECG
- Portable CXR (or bedside lung ultrasound)
- CBC, BMP, troponin

**Based on clinical suspicion:**
- **Heart failure:** BNP or NT-proBNP, echocardiography
- **PE:** Wells score → D-dimer → CTA chest
- **Pneumonia:** Blood cultures (if septic), procalcitonin, sputum culture if intubated
- **Asthma/COPD:** Peak flow, VBG for CO2 (not ABG unless critically ill — VBG pH correlates well)
- **Airway obstruction:** Lateral soft tissue neck radiograph, CT neck, direct laryngoscopy (with anesthesia/ENT backup for epiglottitis)
- **Metabolic:** ABG/VBG, lactate, toxicology screen, serum ketones, osmolality

**Bedside POCUS protocol (BLUE protocol for lung ultrasound):**
- A-profile with lung sliding: COPD/asthma
- B-profile (bilateral B-lines): pulmonary edema
- A-profile without lung sliding + lung point: pneumothorax
- PLAPS (posterolateral alveolar/pleural syndrome): pneumonia/effusion
- Deep vein assessment: DVT → supports PE diagnosis

## Treatment

Stabilization while working up — definitive treatment per specific condition entries.

- **Supplemental O2:** Titrate to SpO2 92-96% (88-92% in known CO2-retaining COPD)
- **BIPAP/CPAP:** 10/5 cmH2O for acute cardiogenic pulmonary edema or COPD exacerbation. Reduces intubation rates.
- **Bronchodilators:** Albuterol 2.5 mg nebulized q20min x 3 + ipratropium 0.5 mg nebulized for bronchospasm
- **Epinephrine 0.3-0.5 mg IM** (1:1000) for anaphylaxis — do NOT delay, do NOT substitute IV for first dose
- **Nitroglycerin 0.4 mg SL or IV infusion** (start 10-20 mcg/min, titrate) for acute HF with hypertension
- **Needle decompression** (14G needle, 2nd intercostal space midclavicular or 5th ICS anterior axillary line) for tension pneumothorax (see `needle-decompression`)
- **Corticosteroids:** Methylprednisolone 125 mg IV or prednisone 60 mg PO for acute asthma/COPD
- **Intubation:** Prepare for RSI if impending respiratory failure (see `rapid-sequence-intubation`). Ketamine 1-2 mg/kg IV preferred induction agent for bronchospasm; etomidate 0.3 mg/kg IV for cardiac compromise.

## Disposition

- **Intubation/ICU:** Respiratory failure requiring mechanical ventilation, massive PE with hemodynamic instability, impending airway loss
- **ICU/step-down:** Severe asthma (peak flow < 25% predicted after treatment), acute HF requiring IV vasodilators, submassive PE on anticoagulation
- **Telemetry/floor:** Pneumonia requiring IV antibiotics, moderate HF exacerbation responding to treatment, stable PE on anticoagulation
- **Observation:** Asthma with partial response (peak flow 50-75% predicted after treatment), chest pain with negative serial troponin
- **Discharge:** Asthma with full response (peak flow > 75%, sustained > 60 min off nebulizer), simple pneumothorax (< 2 cm) in reliable patient with follow-up, anxiety/hyperventilation after complete negative workup

## Pitfalls

1. **Attributing dyspnea to "anxiety" without objective evaluation.** PE, ACS, and metabolic acidosis all cause subjective air hunger. A normal SpO2 does not exclude PE. Complete workup before labeling as anxiety.

2. **Failure to recognize the "silent chest" in severe asthma.** Absence of wheezing in a patient with asthma and respiratory distress indicates critical air trapping with minimal airflow. This patient is pre-arrest. Prepare for intubation.

3. **COPD patient with "normal" SpO2 of 98%.** A COPD patient who is normally 88-92% and is now 98% on room air may have been hyperventilating from PE, metabolic acidosis, or other acute process. Do not dismiss this as reassuring.

4. **Missed PE because CXR shows pneumonia.** PE and pneumonia coexist. Hampton hump on CXR is often misread as consolidation. Maintain suspicion for PE even when pneumonia is identified, especially with disproportionate tachycardia or hypoxia.

5. **Over-oxygenating COPD patients.** High-flow O2 in CO2 retainers causes V/Q mismatch worsening and suppresses hypoxic respiratory drive. Target 88-92%. Use VBG to monitor CO2.

6. **Flash pulmonary edema misdiagnosed as asthma ("cardiac asthma").** Bilateral wheezing from pulmonary edema mimics asthma. Check BNP, assess JVD, and perform bedside echo. Treating with bronchodilators alone while missing HF is dangerous.

7. **Failure to prepare for difficult airway in angioedema.** Tongue/oropharyngeal swelling progresses rapidly. Have surgical airway equipment at bedside before any intubation attempt. Video laryngoscopy is first-line but may fail. ENT backup if available.
