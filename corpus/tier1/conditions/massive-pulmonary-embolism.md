---
id: massive-pulmonary-embolism
condition: Massive Pulmonary Embolism
aliases: [massive PE, high-risk PE, saddle embolus, hemodynamically significant PE]
icd10: [I26.02, I26.09]
esi: 1
time_to_harm:
  irreversible_injury: "< 1 hour (right ventricular failure)"
  death: "< 2 hours (cardiovascular collapse)"
  optimal_intervention_window: "< 60 minutes (thrombolysis or embolectomy)"
category: hematologic
track: tier1
sources:
  - type: guideline
    ref: "2019 ESC/ERS Guidelines for the Diagnosis and Management of Acute Pulmonary Embolism"
  - type: guideline
    ref: "AHA Scientific Statement: Management of Massive and Submassive Pulmonary Embolism, 2011"
  - type: guideline
    ref: "ACC/AHA Pulmonary Embolism Guideline Comparison, 2024"
  - type: review
    ref: "High Risk Pulmonary Embolism Management. Emergency Medicine Cases, 2024"
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
# Massive Pulmonary Embolism

## Recognition

**Definition:** Acute PE with sustained hemodynamic instability:
- Systolic BP < 90 mmHg for >= 15 minutes
- Need for vasopressors
- Cardiac arrest or pulseless electrical activity (PEA)
- Signs of obstructive shock

**Presentation:**
- Sudden-onset dyspnea, pleuritic chest pain
- Syncope or near-syncope
- Tachycardia, hypotension
- Cyanosis, JVD
- Right heart failure signs: RV heave, loud P2, tricuspid regurgitation murmur
- Acute cor pulmonale
- Cardiac arrest (PEA is classic mechanism)

**Risk factors:**
- Recent surgery/immobilization, hospitalization
- Active malignancy
- Prior VTE, thrombophilia
- Oral contraceptives, HRT, pregnancy/postpartum
- Obesity, smoking
- Long-distance travel
- Central venous catheters

**Bedside clues to massive PE:**
- Acute RV dilation on bedside echo (RV:LV ratio > 1:1)
- McConnell sign (RV free wall hypokinesis with apical sparing)
- Interventricular septal bowing into LV
- Dilated IVC without respiratory variation
- ECG: S1Q3T3, right axis deviation, RBBB, anterior T-wave inversions (V1-V4)

## Critical Actions

1. **Systemic thrombolysis** for hemodynamically unstable PE — alteplase 100 mg IV over 2 hours (or 50 mg IV bolus if cardiac arrest/near-arrest)
2. **Bedside echocardiography** — RV dilation confirms diagnosis; do NOT delay treatment for CTPA if hemodynamically unstable
3. **IV heparin bolus** — UFH 80 units/kg bolus (max 10,000 units), then 18 units/kg/hr unless thrombolysis given (hold infusion during lysis, restart after)
4. **Volume challenge cautiously** — NS 250-500 mL bolus (excessive fluids worsen RV distension)
5. **Vasopressors:** Norepinephrine 0.05-0.5 mcg/kg/min (first-line for RV failure)
6. **If thrombolysis contraindicated:** Catheter-directed therapy or surgical embolectomy (PERT team activation)
7. **For cardiac arrest with suspected PE:** administer alteplase 50 mg IV push; continue CPR for at least 60-90 minutes after thrombolysis before declaring futility

## Differential Diagnosis

- Acute myocardial infarction — ECG changes, troponin; echo may distinguish
- Aortic dissection — tearing chest/back pain, blood pressure differential; CT angiography
- Cardiac tamponade — Beck triad, pericardial effusion on echo
- Tension pneumothorax — absent breath sounds, tracheal deviation, hyper-resonance
- Septic shock — fever, source of infection; distributive shock pattern
- Acute decompensated heart failure — bilateral pulmonary edema, history of HF
- ARDS — bilateral infiltrates, PaO2/FiO2 < 300

## Workup

- **Bedside echocardiography** — RV dilation, RV:LV > 1, McConnell sign, septal bowing, IVC dilation; can be done in < 5 minutes
- **CT Pulmonary Angiography (CTPA)** — gold standard for diagnosis; obtain ONLY if patient stable enough for transport
- **ECG:** Sinus tachycardia (most common), S1Q3T3, right axis deviation, RBBB, anterior T-wave inversions, P-pulmonale
- **Troponin** — elevated in submassive/massive PE (RV strain)
- **BNP/NT-proBNP** — elevated with RV dysfunction
- **ABG** — hypoxemia, respiratory alkalosis, increased A-a gradient
- **D-dimer** — NOT useful in hemodynamically unstable patients (pre-test probability is too high; do NOT use to rule out)
- **CBC, BMP, coagulation studies, type and screen**
- **Bilateral lower extremity duplex** — if time permits; DVT confirms VTE source
- **Point-of-care ultrasound:** Compress femoral and popliteal veins (non-compressible = DVT)

## Treatment

### Systemic Thrombolysis (First-Line for Massive PE)
**Alteplase (tPA):**
- **Standard dose:** 100 mg IV over 2 hours (10 mg bolus, then 90 mg over 2 hours)
- **Accelerated/half-dose:** 50 mg IV over 2 hours (or bolus for arrest) — emerging evidence supports similar efficacy with lower bleeding risk
- **Cardiac arrest dose:** 50 mg IV push, with continued CPR for 60-90 minutes post-administration

**Tenecteplase (alternative):**
- Weight-based single IV bolus (same dosing as for STEMI)
- < 60 kg: 30 mg; 60-69 kg: 35 mg; 70-79 kg: 40 mg; 80-89 kg: 45 mg; >= 90 kg: 50 mg
- Half-dose (0.25 mg/kg, max 25 mg) used in some protocols

### Anticoagulation
- **UFH:** 80 units/kg IV bolus (max 10,000 units), then 18 units/kg/hr infusion
- Hold heparin infusion during thrombolysis; restart 1-2 hours after completion (when aPTT < 80 seconds)
- Target aPTT 60-80 seconds (1.5-2.5x control)

### Hemodynamic Support
- **Norepinephrine 0.05-0.5 mcg/kg/min** — first-line vasopressor for RV failure
- **Dobutamine 2.5-10 mcg/kg/min** — if additional inotropy needed (caution: may cause hypotension)
- **IV fluids:** Cautious 250-500 mL NS challenge ONLY; excessive fluids worsen RV distension by increasing RV wall tension
- **Avoid intubation if possible** — positive pressure ventilation reduces RV preload and can precipitate cardiovascular collapse. If required: ketamine for induction, low PEEP, avoid hypoxia/hypercarbia

### Catheter-Directed Therapy
- **Indications:** Thrombolysis contraindicated, thrombolysis failed, or submassive PE with RV dysfunction
- Catheter-directed thrombolysis: alteplase 0.5-1.0 mg/hr per catheter x 12-24 hours
- Mechanical thrombectomy (FlowTriever, Penumbra)
- **PERT (Pulmonary Embolism Response Team)** activation recommended

### Surgical Embolectomy
- Massive PE with failed thrombolysis or absolute contraindication to thrombolysis
- Requires cardiopulmonary bypass
- Mortality 20-50% but may be life-saving

### Absolute Contraindications to Systemic Thrombolysis
- Active internal bleeding (excluding menses)
- Recent (< 3 months) hemorrhagic stroke
- Intracranial neoplasm, AVM, or aneurysm
- Known structural cerebrovascular lesion
- Recent (< 3 weeks) major surgery or significant trauma

**Note:** In cardiac arrest from massive PE, there are NO absolute contraindications to thrombolysis — the alternative is death.

## Disposition

- **All massive PE patients:** ICU with continuous hemodynamic monitoring
- **Post-thrombolysis:** Monitor for bleeding complications (intracranial hemorrhage 1-3%)
- **Anticoagulation:** Transition to LMWH or DOAC when hemodynamically stable
- **IVC filter:** Consider only if anticoagulation absolutely contraindicated
- **Transfer:** If facility lacks thrombolysis capability, catheter-directed therapy, or surgical embolectomy — transfer to a higher-level center
- **Isolation:** Standard precautions
- **Reportable:** Not a reportable disease

## Pitfalls

1. **Withholding thrombolysis due to bleeding risk in massive PE.** The mortality of untreated massive PE exceeds the risk of thrombolytic-related hemorrhage. In cardiac arrest from PE, there are NO absolute contraindications.

2. **Delaying treatment for CTPA in the hemodynamically unstable patient.** Bedside echo showing RV dilation in the right clinical context is sufficient to justify thrombolysis. Do not send an unstable patient to CT.

3. **Aggressive IV fluid resuscitation.** The failing RV in massive PE is volume-overloaded, not volume-depleted. Excessive fluids increase RV wall tension, worsen septal bowing, and reduce LV filling. Small boluses (250-500 mL) with reassessment.

4. **Intubating without preparation for hemodynamic collapse.** Positive pressure ventilation reduces venous return and can cause cardiac arrest in massive PE. If intubation is necessary, use hemodynamically neutral agents (ketamine), have vasopressors drawn and ready, and use the lowest effective PEEP.

5. **Using D-dimer to risk-stratify hemodynamically unstable patients.** D-dimer is a rule-out test for low-probability patients. In massive PE, pre-test probability is high and D-dimer adds no value.

6. **Stopping CPR too early after thrombolysis.** After thrombolytic administration during cardiac arrest, CPR should continue for at least 60-90 minutes to allow drug effect. Early termination may prevent successful resuscitation.
