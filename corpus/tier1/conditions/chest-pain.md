---
id: chest-pain
condition: "Chest Pain — Emergency Evaluation"
aliases: [chest pain, thoracic pain, anterior chest pain, chest discomfort]
icd10: [R07.9, R07.1, R07.89]
esi: 2
time_to_harm:
  irreversible_injury: "< 90 minutes (STEMI)"
  death: "< 1 hour (aortic dissection, tension pneumothorax)"
  optimal_intervention_window: "< 90 minutes (door-to-balloon)"
category: presentations
condition_type: presentation
chief_complaint: "Chest Pain"
differential_categories:
  - category: life-threatening
    conditions:
      - stemi
      - acute-coronary-syndrome-nstemi
      - unstable-angina
      - aortic-dissection
      - pulmonary-embolism
      - tension-pneumothorax
      - cardiac-tamponade
      - boerhaave-syndrome
  - category: emergent
    conditions:
      - spontaneous-pneumothorax
      - pericarditis-myocarditis
      - acute-heart-failure
      - hypertensive-emergency
      - takotsubo-cardiomyopathy
      - spontaneous-coronary-artery-dissection
  - category: urgent
    conditions:
      - acute-cholecystitis
      - acute-pancreatitis
      - pleural-effusion-emergency
  - category: non-emergent
    conditions:
      - biliary-colic
      - acute-gout
red_flags:
  - "Sudden onset tearing or ripping pain radiating to back"
  - "Diaphoresis with substernal pressure"
  - "Hypotension or shock"
  - "Unilateral absent breath sounds"
  - "Pulse deficit between upper extremities > 20 mmHg"
  - "Muffled heart sounds with JVD (Beck triad)"
  - "New ST elevation or depression on ECG"
  - "Acute dyspnea with pleuritic chest pain and tachycardia"
  - "Subcutaneous emphysema"
  - "History of recent vomiting followed by severe chest/epigastric pain"
decision_rules:
  - name: "HEART Score"
    citation: "Six AJ et al. Chest pain in the emergency room: value of the HEART score. Neth Heart J. 2008;16(6):191-196."
    pmid: "18665203"
  - name: "HEART Pathway"
    citation: "Mahler SA et al. The HEART Pathway randomized trial. Circ Cardiovasc Qual Outcomes. 2015;8(2):195-203."
    pmid: "25737484"
  - name: "Wells Criteria for PE"
    citation: "Wells PS et al. Derivation of a simple clinical model to categorize patients probability of pulmonary embolism. Thromb Haemost. 2000;83(3):416-420."
    pmid: "10744147"
  - name: "PERC Rule"
    citation: "Kline JA et al. Clinical criteria to prevent unnecessary diagnostic testing in emergency department patients with suspected pulmonary embolism. J Thromb Haemost. 2004;2(8):1247-1255."
    pmid: "15304025"
  - name: "ADvISED Score (Aortic Dissection)"
    citation: "Defined by ACEP clinical policy on thoracic aortic dissection."
track: tier1
sources:
  - type: guideline
    ref: "2021 AHA/ACC/ASE/CHEST/SAEM/SCCT/SCMR Guideline for the Evaluation and Diagnosis of Chest Pain"
    doi: "10.1161/CIR.0000000000001029"
  - type: guideline
    ref: "2025 ACC/AHA/ACEP/NAEMSP/SCAI Guideline for the Management of Patients With Acute Coronary Syndromes"
  - type: guideline
    ref: "ACEP Clinical Policy: Critical Issues in the Evaluation and Management of Adult Patients Presenting to the Emergency Department With Acute Chest Pain. Ann Emerg Med. 2018;72(1):e65-e115."
    pmid: "29907420"
  - type: pubmed
    ref: "Six AJ et al. Chest pain in the emergency room: value of the HEART score. Neth Heart J. 2008;16(6):191-196."
    pmid: "18665203"
  - type: pubmed
    ref: "Backus BE et al. A prospective validation of the HEART score for chest pain patients at the emergency department. Int J Cardiol. 2013;168(3):2153-2158."
    pmid: "23465250"
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
# Chest Pain — Emergency Evaluation

## Recognition

Chest pain accounts for approximately 6-8 million ED visits annually in the US (5-8% of all ED visits). Fewer than 25% have an acute coronary syndrome; the challenge is identifying the minority with life-threatening causes.

**Key history elements:**
- Onset: sudden vs gradual; activity at onset
- Character: pressure/squeezing (ACS), tearing/ripping (dissection), sharp/pleuritic (PE, pneumothorax, pericarditis)
- Radiation: arm/jaw (ACS), back/interscapular (dissection), unilateral (pleuritic)
- Duration: seconds (usually benign), > 20 minutes (concerning for ACS)
- Associated symptoms: diaphoresis, dyspnea, syncope, nausea
- Positional: worse supine/improved leaning forward (pericarditis)
- Prior history: known CAD, PE, DVT, connective tissue disease, recent procedures/immobilization
- Cocaine or stimulant use within 72 hours

**High-risk populations for atypical presentations:**
- Women: more likely to present with dyspnea, nausea, fatigue, back/jaw pain
- Elderly (> 75): painless MI in up to 60%
- Diabetics: autonomic neuropathy masks angina
- Post-surgical/immobilized: PE risk

**Epidemiology of serious causes:**
- ACS: 10-15% of ED chest pain presentations
- PE: 2-5%
- Aortic dissection: < 1% but > 25% mortality if missed
- Pneumothorax: 1-2%

## Critical Actions

| Action | Target |
|---|---|
| ECG acquisition | < 10 minutes from arrival |
| Troponin drawn | < 30 minutes from arrival |
| Chest X-ray | < 60 minutes (do not delay if ACS suspected) |
| Repeat ECG if initial non-diagnostic | Every 15-30 minutes with ongoing symptoms |

**Immediate evaluation algorithm:**

1. **Assess hemodynamic stability.** Unstable patients (hypotension, acute respiratory distress, altered consciousness) → resuscitation bay, large-bore IV access, continuous monitoring.

2. **Obtain 12-lead ECG within 10 minutes.** STEMI → immediate cath lab activation (see `stemi`). New LBBB → apply Sgarbossa criteria.

3. **Targeted physical exam in parallel with ECG:**
   - Bilateral arm blood pressures (> 20 mmHg differential → aortic dissection)
   - Lung auscultation (unilateral absent breath sounds → pneumothorax)
   - Heart sounds (muffled → tamponade; friction rub → pericarditis)
   - JVD assessment
   - Lower extremity edema/asymmetry (DVT → PE)
   - Subcutaneous emphysema (esophageal rupture, pneumomediastinum)

4. **Risk stratify based on initial ECG and exam:**
   - ST elevation → `stemi` pathway
   - Hemodynamically unstable → immediate bedside ultrasound (tamponade, RV strain, pneumothorax, aortic root dilation)
   - Pleuritic + tachycardia → evaluate for PE (Wells → D-dimer or CTA)
   - Tearing pain + BP differential → CTA aorta for dissection
   - Non-diagnostic ECG, stable → apply HEART Score

5. **Serial troponin.** High-sensitivity troponin at 0 and 1-3 hours (institution-dependent protocol). Do NOT wait for troponin to activate cath lab for STEMI.

6. **HEART Score stratification (for stable patients without clear diagnosis):**
   - 0-3: Low risk (MACE < 2%). Consider discharge with outpatient follow-up.
   - 4-6: Moderate risk. Observation, serial troponin, stress testing or CTA.
   - 7-10: High risk (MACE > 50%). Admit, cardiology consultation, early invasive strategy.

## Differential Diagnosis

### Life-Threatening (must rule out immediately)
- **STEMI / ACS** (`stemi`, `acute-coronary-syndrome-nstemi`, `unstable-angina`): substernal pressure, diaphoresis, ECG changes, troponin elevation
- **Aortic dissection** (`aortic-dissection`): sudden tearing pain radiating to back, BP differential, widened mediastinum, aortic regurgitation murmur
- **Pulmonary embolism** (`pulmonary-embolism`): pleuritic pain, dyspnea, tachycardia, risk factors for VTE, right heart strain on ECG
- **Tension pneumothorax** (`tension-pneumothorax`): unilateral absent breath sounds, tracheal deviation, hypotension, distended neck veins
- **Cardiac tamponade** (`cardiac-tamponade`): Beck triad (hypotension, JVD, muffled heart sounds), pulsus paradoxus, electrical alternans
- **Esophageal rupture** (`boerhaave-syndrome`): post-emetic severe chest/epigastric pain, subcutaneous emphysema, pneumomediastinum

### Emergent
- **Spontaneous pneumothorax** (`spontaneous-pneumothorax`): sudden pleuritic pain, decreased breath sounds, tall thin habitus or COPD
- **Pericarditis/myocarditis** (`pericarditis-myocarditis`): sharp pleuritic pain worse supine and improved leaning forward, diffuse ST elevation with PR depression, friction rub
- **Acute heart failure** (`acute-heart-failure`): dyspnea, orthopnea, bilateral crackles, peripheral edema, BNP elevation
- **Hypertensive emergency** (`hypertensive-emergency`): SBP > 180 with end-organ damage
- **Takotsubo cardiomyopathy** (`takotsubo-cardiomyopathy`): post-emotional/physical stress, mimics ACS, apical ballooning on echo
- **Spontaneous coronary artery dissection** (`spontaneous-coronary-artery-dissection`): young women, peripartum, connective tissue disease, mimics ACS

### Urgent
- **Biliary disease** (`acute-cholecystitis`, `biliary-colic`): RUQ/epigastric pain, post-prandial, Murphy sign
- **Acute pancreatitis** (`acute-pancreatitis`): epigastric pain radiating to back, nausea/vomiting, lipase elevation
- **Pleural effusion** (`pleural-effusion-emergency`): dyspnea, decreased breath sounds at bases, dullness to percussion

### Non-Emergent (diagnoses of exclusion)
- Musculoskeletal chest wall pain: reproducible with palpation, positional, no red flags
- GERD/esophageal spasm: burning, post-prandial, relief with antacids (but do NOT anchor on this without ruling out ACS)
- Anxiety/panic: diagnosis of exclusion ONLY after cardiac evaluation complete (see `panic-attack`)

## Workup

**All patients:**
- 12-lead ECG (repeat serially if symptoms persist and initial is non-diagnostic)
- High-sensitivity troponin (0h and 1-3h)
- CBC, BMP, coagulation studies
- Portable CXR

**Based on clinical suspicion:**
- **ACS pathway:** Serial troponin, HEART Score, cardiology consultation for moderate-high risk
- **PE pathway:** Wells score → PERC rule (if low pretest) → D-dimer (if PERC not met) → CTA chest (if D-dimer positive or high clinical suspicion)
- **Aortic dissection:** CTA chest/abdomen/pelvis with IV contrast (definitive); TEE if unstable and cannot go to CT
- **Pneumothorax:** CXR (upright, expiratory); bedside ultrasound (M-mode: absent lung sliding)
- **Tamponade:** Bedside echo (pericardial effusion, RV diastolic collapse, IVC plethora)
- **Boerhaave syndrome:** CT chest with oral contrast, CXR (left pleural effusion, pneumomediastinum)

**Bedside point-of-care ultrasound (POCUS):**
Indicated in unstable chest pain. Rapid assessment for pericardial effusion, RV dilation, pneumothorax, aortic root dilation, and global LV function. Integrates with RUSH protocol.

## Treatment

Treatment is cause-specific. Stabilization measures while working up:

- **IV access:** Two large-bore (18G or larger) peripheral IVs
- **Continuous monitoring:** Cardiac telemetry, pulse oximetry, BP cycling
- **Aspirin 325 mg PO** if ACS suspected and no contraindication (do NOT give if aortic dissection is on differential until excluded)
- **Nitroglycerin 0.4 mg SL** for ischemic-type pain (contraindicated if SBP < 90, RV infarct, PDE-5 inhibitor use within 24-48h, or aortic stenosis)
- **Analgesia:** Avoid morphine in ACS if possible (associated with worse outcomes); consider fentanyl 25-50 mcg IV for severe pain
- **Oxygen:** Only if SpO2 < 94% (routine supplemental O2 not beneficial)
- **Needle decompression** for tension pneumothorax (see `needle-decompression`)
- **Pericardiocentesis** for tamponade with hemodynamic compromise (see `emergency-pericardiocentesis`)
- **Esmolol or labetalol** if aortic dissection suspected: target HR < 60 and SBP 100-120

Defer to specific condition entries for definitive management.

## Disposition

- **Immediate cath lab:** STEMI, high-risk NSTEMI
- **ICU/CCU:** Aortic dissection, massive PE, tamponade, Boerhaave, hemodynamic instability
- **Telemetry admission:** Moderate-risk ACS (HEART 4-6 with positive troponin), new arrhythmia
- **Observation unit:** HEART 4-6 with negative serial troponin for stress test or CTA coronary
- **Discharge with follow-up (< 72 hours):** HEART 0-3, two negative troponins, no ECG changes, no hemodynamic instability, reliable follow-up available
- **Transfer:** Any STEMI at non-PCI center, aortic dissection at non-surgical center

## Pitfalls

1. **Anchoring on "GERD" or "musculoskeletal" without completing ACS workup.** Reproducible chest wall tenderness is present in 5-15% of patients with ACS. A response to antacids does not rule out ACS. Always obtain ECG and troponin regardless of initial impression.

2. **Failure to consider aortic dissection in the patient treated for ACS.** Giving anticoagulation and thrombolytics to a patient with aortic dissection is lethal. Check bilateral arm pressures on every chest pain patient. Dissection can cause ST elevation by occluding coronary ostia.

3. **Dismissing PE because chest pain is not pleuritic.** Up to 50% of PE patients have non-pleuritic chest pain. Dyspnea with tachycardia should trigger PE evaluation regardless of pain character.

4. **Over-reliance on negative initial troponin.** High-sensitivity troponin can be negative in the first 1-3 hours of symptom onset. Serial testing is mandatory for moderate-risk patients. A single negative troponin does not rule out ACS.

5. **Premature closure on musculoskeletal diagnosis in young patients.** Spontaneous coronary artery dissection affects young women. Type A aortic dissection occurs in Marfan syndrome in the 20s-30s. Myocarditis affects young adults.

6. **Missing posterior STEMI.** Standard 12-lead ECG misses posterior MI. ST depression in V1-V3 should prompt posterior leads (V7-V9). This is the most commonly missed STEMI territory.

7. **Cocaine-associated chest pain mismanagement.** Do NOT give beta-blockers (unopposed alpha stimulation → coronary vasospasm and hypertension). Use benzodiazepines, nitroglycerin, and calcium channel blockers. Phentolamine for refractory hypertension.

8. **Attributing chest pain to anxiety in women and young patients.** Women are more likely to be diagnosed with anxiety when presenting with ACS. Complete objective workup before considering psychiatric diagnosis.
