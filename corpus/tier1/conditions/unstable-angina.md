---
id: unstable-angina
condition: Unstable Angina
aliases: [UA, NSTE-ACS, crescendo angina, preinfarction angina]
icd10: [I20.0, I20.1, I20.8, I20.9]
esi: 2
time_to_harm: "< 2 hours (progression to NSTEMI or STEMI)"
mortality_if_delayed: "5-10% 30-day mortality without treatment; risk of progression to MI"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2014 AHA/ACC Guideline for the Management of Patients with Non-ST-Elevation Acute Coronary Syndromes"
    pmid: "25249585"
  - type: guideline
    ref: "2021 AHA/ACC/ASE/CHEST/SAEM/SCCT/SCMR Guideline for the Evaluation and Diagnosis of Chest Pain"
    pmid: "34756653"
  - type: guideline
    ref: "2023 ESC Guidelines for the Management of Acute Coronary Syndromes"
  - type: review
    ref: "Amsterdam EA et al. Testing of Low-Risk Patients Presenting to the ED with Chest Pain. Circulation 2010;122(17):1756-1776"
    pmid: "20660809"
last_updated: "2026-02-18"
compiled_by: agent
reviewed_by: null
verification:
  pmids_verified: "2026-02-18"
  audit_completed: "2026-02-18"
---

# Unstable Angina

## Recognition

**Definition:** Acute coronary syndrome (ACS) characterized by myocardial ischemia at rest or with minimal exertion, without biomarker evidence of myocardial necrosis (troponin-negative). Differentiated from NSTEMI solely by negative troponin. Part of the NSTE-ACS spectrum.

**Braunwald Classification:**
- Class I: new-onset severe or accelerated angina (< 2 months, ≥ 3 episodes/day, or at significantly lower threshold)
- Class II: subacute rest angina (rest pain within prior month but not within 48 hours)
- Class III: acute rest angina (rest pain within 48 hours)

**Pathophysiology:**
- Atherosclerotic plaque rupture or erosion with non-occlusive thrombus formation
- Transient reduction in coronary blood flow
- Dynamic obstruction (coronary vasospasm, Prinzmetal)
- Progressive mechanical obstruction
- Increased myocardial oxygen demand with fixed stenosis

**Risk Factors:**
- Age (men > 45, women > 55)
- Hypertension, diabetes, hyperlipidemia
- Smoking (active or recent)
- Family history of premature CAD (male first-degree relative < 55, female < 65)
- Known coronary artery disease, prior MI, prior PCI/CABG
- Cocaine/amphetamine use
- Peripheral arterial disease

**Presentation:**
- Chest pain/pressure at rest or with minimal exertion, lasting > 20 minutes
- Crescendo pattern: previously stable angina now occurring with less exertion, more frequently, lasting longer, or at rest
- New-onset angina with exertion that is severe, frequent, or prolonged
- Radiation to left arm, jaw, neck, back, or epigastrium
- Associated dyspnea, diaphoresis, nausea, lightheadedness

**Atypical Presentations (common in women, elderly, diabetics):**
- Dyspnea without chest pain
- Epigastric pain, nausea, vomiting (mimics GI)
- Isolated jaw or arm pain
- Syncope or presyncope
- Acute fatigue or weakness
- Diabetic patients may present with "silent ischemia"

## Critical Actions

1. **12-lead ECG within 10 minutes of arrival** — look for ST depression, T-wave inversions, or dynamic changes. A normal ECG does not exclude ACS. Serial ECGs q15-30 min if ongoing pain.
2. **Aspirin 325 mg PO (chewed, non-enteric-coated)** — immediately unless true aspirin allergy.
3. **Troponin at presentation and serial (3-6 hours)** — high-sensitivity troponin (hsTnI or hsTnT) preferred. UA is defined by negative troponin; serial troponins are mandatory to differentiate from NSTEMI.
4. **Nitroglycerin 0.4 mg SL q5 min x 3 doses** for ongoing chest pain. Do NOT administer if: SBP < 90 mmHg, RV infarction suspected, PDE-5 inhibitor use within 24-48 hours (sildenafil/vardenafil 24h, tadalafil 48h).
5. **Anticoagulation** — heparin (unfractionated heparin 60 units/kg IV bolus [max 4000 units], then 12 units/kg/hr [max 1000 units/hr]) or enoxaparin 1 mg/kg SQ q12h.
6. **Risk stratification** — use HEART score, TIMI score, or institutional protocol to guide disposition and invasive strategy.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| NSTEMI | Troponin-positive; otherwise identical presentation. Differentiated by serial troponin testing. |
| STEMI | ST elevation ≥ 1 mm in ≥ 2 contiguous leads, or new LBBB with ischemic symptoms. Requires emergent cath lab. |
| Aortic dissection | Tearing/ripping pain radiating to back, pulse deficit, widened mediastinum, blood pressure differential between arms |
| Pulmonary embolism | Pleuritic chest pain, dyspnea, tachycardia, hypoxia, risk factors (DVT, immobility, malignancy), elevated D-dimer, CT angiography |
| Pericarditis | Sharp, pleuritic, positional (worse supine, better leaning forward), diffuse ST elevation with PR depression, friction rub |
| Esophageal spasm | Can mimic angina exactly; may respond to nitroglycerin; endoscopy/manometry for definitive diagnosis |
| Musculoskeletal chest pain | Reproducible with palpation, positional, no ECG changes, negative troponin, low risk scores |
| Costochondritis | Point tenderness over costochondral junction, reproducible with palpation |
| Biliary colic | RUQ pain, post-prandial, Murphy sign, RUQ ultrasound shows gallstones |

## Workup

**ECG:**
- 12-lead ECG within 10 minutes; repeat q15-30 min if ongoing or recurrent symptoms
- Findings: ST depression (≥ 0.5 mm), T-wave inversions (≥ 1 mm), or transient ST elevation (< 20 min)
- Normal ECG does NOT exclude UA/ACS (present in 50% of ACS patients at initial ECG)
- Compare to prior ECGs when available
- Right-sided leads (V4R) and posterior leads (V7-V9) if inferior ischemia suspected

**Biomarkers:**
- High-sensitivity troponin (hsTnI or hsTnT) at presentation and at 3 hours (some protocols use 1-hour rule-in/rule-out with hs-cTn)
- UA = troponin-negative ACS. If troponin rises, reclassify as NSTEMI.
- CK-MB: no longer first-line but useful for detecting reinfarction

**Risk Stratification:**
- **HEART Score (preferred in ED):** History (0-2), ECG (0-2), Age (0-2), Risk factors (0-2), Troponin (0-2). Score 0-3: low risk (< 2% MACE). Score 4-6: moderate. Score 7-10: high risk.
- **TIMI Score for UA/NSTEMI:** Age ≥ 65, ≥ 3 CAD risk factors, known CAD ≥ 50% stenosis, ST deviation, ≥ 2 anginal events in 24h, ASA use in past 7 days, elevated troponin. Score 0-1: 5% MACE. Score 6-7: 41% MACE.

**Labs:**
- CBC (anemia worsening ischemia, leukocytosis)
- BMP (renal function for contrast, electrolytes)
- Coagulation studies (baseline before anticoagulation)
- BNP/NT-proBNP (prognostic — elevated levels in ACS predict worse outcomes)
- Lipid panel
- Glucose, HbA1c

**Imaging:**
- Chest X-ray (cardiomegaly, pulmonary edema, aortic dissection screening, alternative diagnoses)
- Echocardiography: wall motion abnormalities (regional = ischemia), EF assessment. Useful if diagnosis uncertain.
- CT coronary angiography: intermediate-risk patients in ED with negative troponin and non-diagnostic ECG. High negative predictive value.

## Treatment

**Acute Medical Therapy ("MONA-B-H" framework):**
- **Aspirin 325 mg PO** (chewed, non-enteric coated) — immediate, unless true allergy
- **Nitroglycerin 0.4 mg SL q5 min x 3** for chest pain; transition to nitroglycerin 10-200 mcg/min IV drip for refractory pain. Avoid if SBP < 90, RV infarction, PDE-5 inhibitor use.
- **Morphine 2-4 mg IV q5-15 min** — for pain refractory to nitroglycerin. Use cautiously (associated with worse outcomes in some studies; avoid in NSTEMI if possible). Fentanyl 25-50 mcg IV is an alternative.
- **Supplemental O2** only if SpO2 < 94%. Routine oxygen in normoxic ACS patients provides no benefit and may cause harm.
- **Beta-blocker:** metoprolol 5 mg IV q5 min x 3 (if no contraindication), then metoprolol 25-50 mg PO q6h. Contraindicated in: HR < 60, SBP < 100, acute heart failure, cocaine use, second/third-degree heart block, severe reactive airway disease.
- **Anticoagulation (choose one):**
  - Unfractionated heparin 60 units/kg IV bolus (max 4000 units), then 12 units/kg/hr IV (max 1000 units/hr), aPTT target 1.5-2.5x control
  - Enoxaparin 1 mg/kg SQ q12h (reduce to 1 mg/kg SQ daily if CrCl < 30 mL/min)
- **P2Y12 inhibitor (dual antiplatelet therapy):** Timing depends on invasive vs. conservative strategy.
  - If early invasive strategy planned: ticagrelor 180 mg PO loading dose, or prasugrel 60 mg PO loading dose (at time of PCI; not before angiography due to CABG bleeding risk). Clopidogrel 600 mg PO loading dose if ticagrelor/prasugrel contraindicated.
  - If conservative strategy: clopidogrel 300-600 mg PO loading dose

**Statin:**
- Atorvastatin 80 mg PO — initiate in ED regardless of lipid levels

**Refractory Ischemia:**
- Nitroglycerin IV drip escalation
- Intra-aortic balloon pump (cardiogenic shock, refractory ischemia)
- Emergent cardiac catheterization

## Disposition

**Cardiac Catheterization / Invasive Strategy:**
- High-risk features (any of): recurrent angina at rest despite treatment, dynamic ST changes, hemodynamic instability, new/worsening mitral regurgitation, sustained VT, TIMI ≥ 5, HEART ≥ 7
- Early invasive strategy (cath within 24 hours) recommended for most UA/NSTEMI patients with elevated risk

**Admission to Telemetry/CCU:**
- All patients diagnosed with or strongly suspected of UA
- Ongoing or recurrent ischemic symptoms
- Dynamic ECG changes
- Elevated HEART score (≥ 4) or TIMI score (≥ 3)
- Hemodynamic instability, heart failure, arrhythmia

**Observation Unit (6-12 hours):**
- Low-to-intermediate risk (HEART score 4-6)
- Serial troponins q3h
- Repeat ECG
- Provocative testing or CT coronary angiography if available within observation period

**Discharge (low-risk chest pain, NOT UA):**
- HEART score 0-3, two negative troponins (0 and 3h), non-ischemic ECG, symptom-free
- Outpatient stress testing within 72 hours or cardiology follow-up
- Aspirin 81 mg PO daily, statin
- Nitroglycerin 0.4 mg SL PRN, prescribed with instructions
- Return immediately if: chest pain recurrence, dyspnea, syncope, diaphoresis

**Do NOT discharge patients with:**
- Active chest pain
- Dynamic ECG changes
- Positive or rising troponin (this is NSTEMI, not UA)
- High-risk features on risk stratification

## Pitfalls

1. **Single negative troponin ruling out ACS.** Serial troponins are mandatory. High-sensitivity troponin may be negative at initial presentation and peak at 3-6 hours. Discharging after a single negative troponin misses early NSTEMI and high-risk UA.

2. **Normal ECG excluding ACS.** Up to 50% of ACS patients have a non-diagnostic initial ECG. Serial ECGs during ongoing symptoms and comparison to prior tracings are essential. Posterior MI is invisible on standard 12-lead — obtain V7-V9 leads if inferior changes present.

3. **Attributing chest pain to GERD or musculoskeletal causes without risk stratification.** ACS presents atypically, especially in women, elderly, and diabetic patients. Chest wall tenderness is present in 10% of MI patients. Apply a validated risk score (HEART) before attributing chest pain to a non-cardiac cause.

4. **Administering nitroglycerin with recent PDE-5 inhibitor use.** Sildenafil/vardenafil within 24 hours or tadalafil within 48 hours + nitroglycerin = profound refractory hypotension. Ask directly about erectile dysfunction medications before administering nitrates.

5. **Giving beta-blockers to a cocaine user.** Beta-blockers in cocaine-associated chest pain cause unopposed alpha-stimulation, worsening coronary vasospasm and hypertension. Use benzodiazepines (diazepam 5-10 mg IV) and nitroglycerin as first-line for cocaine-associated ACS.

6. **Failing to start dual antiplatelet therapy and anticoagulation.** Aspirin alone is insufficient for ACS. Heparin (UFH or enoxaparin) and a P2Y12 inhibitor are standard of care. Delays in initiating anticoagulation increase thrombus propagation and progression to MI.

7. **Discharging moderate-risk patients without objective testing.** HEART score 4-6 patients have a 12-17% rate of MACE at 6 weeks. These patients require either inpatient workup, observation with serial troponins and provocative testing, or CCTA before safe discharge.

8. **Using morphine as first-line analgesia.** Morphine is associated with delayed antiplatelet absorption (slowed GI motility), higher rates of adverse events, and possibly increased mortality in NSTEMI. Use nitroglycerin as first-line for ischemic pain. Reserve morphine for pain refractory to nitrates.

9. **Missing ACS in women.** Women with ACS present more frequently with dyspnea, nausea, jaw/back pain, and fatigue rather than classic substernal chest pressure. ACS is underdiagnosed and undertreated in women, leading to higher mortality. Apply the same risk stratification tools regardless of sex.
