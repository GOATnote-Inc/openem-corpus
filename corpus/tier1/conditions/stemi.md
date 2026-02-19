---
id: stemi
condition: ST-Elevation Myocardial Infarction
aliases: [STEMI, ST-elevation MI, acute MI with ST elevation]
icd10: [I21.0, I21.1, I21.2, I21.3]
esi: 1
time_to_harm: "< 90 minutes"
mortality_if_delayed: "7.5% per 30-minute delay to reperfusion"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2013 ACCF/AHA Guideline for the Management of ST-Elevation Myocardial Infarction"
  - type: guideline
    ref: "2022 ACC/AHA Guideline for Chest Pain Evaluation and Diagnosis"
  - type: guideline
    ref: "2023 ESC Guidelines for the Management of Acute Coronary Syndromes"
last_updated: "2026-02-18"
compiled_by: agent
reviewed_by: null
verification:
  pmids_verified: "2026-02-18"
  audit_completed: "2026-02-18"
  dosing_crosscheck: "2026-02-19"
---

# ST-Elevation Myocardial Infarction (STEMI)

## Recognition

**Classic presentation:**
- Substernal chest pressure/tightness radiating to left arm, jaw, or back
- Diaphoresis, nausea, dyspnea
- Duration > 20 minutes, not relieved by rest or nitroglycerin

**Atypical presentations (elderly, women, diabetics):**
- Isolated dyspnea, syncope, epigastric pain, acute delirium
- New-onset heart failure without chest pain

**ECG criteria (must be obtained within 10 minutes of arrival):**
- New ST elevation at J-point in 2 or more contiguous leads:
  - >= 2 mm (0.2 mV) in leads V1-V3 (men >= 40 years)
  - >= 2.5 mm (0.25 mV) in leads V1-V3 (men < 40 years)
  - >= 1.5 mm (0.15 mV) in leads V1-V3 (women)
  - >= 1 mm (0.1 mV) in all other leads
- New LBBB with clinical suspicion (apply Sgarbossa criteria)
- Posterior MI: ST depression V1-V3 with tall R waves; obtain posterior leads V7-V9 (>= 0.5 mm elevation diagnostic)
- Right ventricular MI: ST elevation V1, obtain right-sided leads (V4R >= 1 mm)

**Sgarbossa criteria (in LBBB or ventricular paced rhythm):**
- Concordant ST elevation >= 1 mm in any lead (5 points)
- Concordant ST depression >= 1 mm in V1-V3 (3 points)
- Discordant ST elevation >= 5 mm (2 points; modified: ratio >= 0.25 of preceding S-wave)
- Score >= 3 highly specific for STEMI

## Critical Actions

| Action | Target |
|---|---|
| ECG acquisition | < 10 minutes from arrival |
| Cath lab activation | < 20 minutes from first medical contact |
| Door-to-balloon time | < 90 minutes |
| Door-to-needle (if no PCI available) | < 30 minutes |

1. **Activate cath lab immediately** upon STEMI recognition
2. Aspirin 325 mg PO chewed (non-enteric-coated)
3. P2Y12 inhibitor loading: ticagrelor 180 mg PO (preferred) OR clopidogrel 600 mg PO
4. Heparin: unfractionated heparin 60 units/kg IV bolus (max 4000 units), then 12 units/kg/hr (max 1000 units/hr)
5. Nitroglycerin 0.4 mg SL q5min x 3 (hold if SBP < 90, RV infarct, or PDE-5 inhibitor use within 24-48h)
6. Morphine 2-4 mg IV q5-15min PRN (use judiciously; associated with worse outcomes in some data)
7. Oxygen only if SpO2 < 90% (routine O2 not beneficial per DETO2X-AMI trial)
8. Beta-blocker: metoprolol 5 mg IV q5min x 3, then 25-50 mg PO q6h (hold if HR < 60, SBP < 100, acute HF, AV block, active bronchospasm)

**If no PCI capability within 120 minutes of first medical contact:**
- Fibrinolysis with tenecteplase (weight-based, single IV bolus):
  - < 60 kg: 30 mg
  - 60-69 kg: 35 mg
  - 70-79 kg: 40 mg
  - 80-89 kg: 45 mg
  - >= 90 kg: 50 mg
- Half-dose tenecteplase for age >= 75 years
- Transfer for angiography within 3-24 hours post-fibrinolysis

## Differential Diagnosis

- Aortic dissection (check bilateral arm BPs; do NOT give anticoagulation if suspected)
- Pericarditis (diffuse ST elevation, PR depression, pleuritic pain)
- Myocarditis (troponin elevation, ECG changes, recent viral illness)
- Takotsubo cardiomyopathy (apical ballooning, emotional/physical trigger)
- Benign early repolarization (concave-up ST elevation, prominent in young men)
- Left ventricular aneurysm (persistent ST elevation post-MI)
- Hyperkalemia (peaked T waves, widened QRS)
- Pulmonary embolism (right heart strain, S1Q3T3)

## Workup

- **ECG:** Serial every 15-30 minutes if initial non-diagnostic and clinical suspicion persists
- **Troponin:** High-sensitivity troponin at presentation (do NOT delay reperfusion for results)
- **CBC, BMP, coagulation studies, type and screen**
- **Lipid panel, HbA1c** (can be drawn but not actionable acutely)
- **Chest X-ray:** Portable; do not delay cath lab for imaging
- **Point-of-care echocardiography:** Regional wall motion abnormalities support diagnosis; assess for mechanical complications
- **Bilateral arm blood pressures** if aortic dissection on differential

## Treatment

### Cardiogenic Shock (Killip Class IV)
- Norepinephrine 0.05-0.5 mcg/kg/min IV first-line vasopressor
- Dobutamine 2-20 mcg/kg/min IV for inotropy
- Mechanical circulatory support (IABP, Impella) per institutional protocol
- Emergent PCI remains the priority

### Reperfusion Arrhythmias
- Accelerated idioventricular rhythm: typically benign, observe
- Ventricular fibrillation: defibrillation per ACLS
- Complete heart block (inferior MI): temporary transvenous pacing if hemodynamically significant

### Anticoagulation (PCI pathway)
- UFH 60 units/kg bolus (max 4000 units) with ACT-guided dosing in cath lab
- Bivalirudin 0.75 mg/kg bolus then 1.75 mg/kg/hr infusion (alternative, especially with high bleeding risk)

### Post-PCI Medications
- Dual antiplatelet therapy: aspirin 81 mg daily indefinitely + P2Y12 inhibitor x 12 months
- High-intensity statin: atorvastatin 80 mg PO daily
- ACE inhibitor within 24h if anterior STEMI or EF < 40%: lisinopril 2.5-5 mg PO daily, titrate
- Beta-blocker: continue if tolerated

## Disposition

- **All STEMI patients:** CCU/ICU admission post-PCI
- **Cardiogenic shock or mechanical complications:** ICU with hemodynamic monitoring
- **Successful reperfusion, uncomplicated:** Step-down unit at 24-48h if stable
- **Transfer criteria:** Any STEMI at a non-PCI-capable facility requires immediate transfer; do not delay for fibrinolysis decision > 30 minutes

## Pitfalls

1. **Posterior STEMI missed on standard 12-lead.** ST depression in V1-V3 is not "reciprocal change" of anterior ischemia alone. Obtain posterior leads V7-V9 when suspected.

2. **Right ventricular infarct treated with nitroglycerin or diuretics.** RV infarcts are preload-dependent. Aggressive volume resuscitation (NS 1-2 L bolus) is required; nitrates and diuretics cause catastrophic hypotension.

3. **Waiting for troponin results before activating the cath lab.** STEMI is an ECG diagnosis. Troponin may be negative early. Delay kills myocardium.

4. **LBBB dismissed as "old" without applying Sgarbossa criteria.** New or presumably new LBBB with ischemic symptoms warrants emergent reperfusion evaluation. Use modified Sgarbossa (Smith criteria) for improved sensitivity.

5. **Aortic dissection misdiagnosed as STEMI.** Dissection flap involving the coronary ostia can cause ST elevation (usually inferior). Anticoagulation and thrombolysis are lethal in dissection. Check bilateral arm pressures. Widened mediastinum on CXR is a red flag.

6. **Beta-blocker given in acute heart failure or cardiogenic shock.** Contraindicated acutely. Initiate only after hemodynamic stabilization.

7. **Failure to recognize STEMI equivalents:** de Winter T-waves (upsloping ST depression V1-V6 with tall symmetric T-waves), Wellens syndrome (biphasic or deeply inverted T-waves V2-V3 indicating critical LAD stenosis).
