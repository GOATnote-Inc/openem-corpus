---
id: pulmonary-embolism
condition: Pulmonary Embolism
aliases: [PE, pulmonary thromboembolism, massive PE, saddle embolus, submassive PE]
icd10: [I26.99, I26.09, I26.90, I26.02, I26.92]
esi: 1
time_to_harm: "< 1 hour for massive PE"
mortality_if_delayed: "25-65% for massive PE without treatment"
category: respiratory
track: tier1
sources:
  - type: guideline
    ref: "2019 ESC/ERS Guidelines for the Diagnosis and Management of Acute Pulmonary Embolism"
  - type: guideline
    ref: "2016 ACCP Antithrombotic Therapy for VTE Disease: CHEST Guideline"
  - type: guideline
    ref: "AHA 2011 Scientific Statement on Management of Massive and Submassive Pulmonary Embolism"
  - type: guideline
    ref: "PERT Consortium Consensus Guidelines 2019"
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
# Pulmonary Embolism

## Recognition

### Risk Stratification Categories
- **Massive (high-risk):** PE with sustained hypotension (SBP < 90 for >= 15 min), need for vasopressors, or cardiac arrest
- **Submassive (intermediate-risk):** PE with RV dysfunction (echo or CT) and/or elevated troponin/BNP, but hemodynamically stable
- **Low-risk:** PE without hemodynamic compromise or RV dysfunction

### Clinical Presentation
- Acute dyspnea (most common, 73%)
- Pleuritic chest pain (66%)
- Tachycardia (24%)
- Cough, hemoptysis
- Syncope (suggests massive PE or significant RV strain)
- Unilateral leg swelling (concurrent DVT)
- Cardiac arrest with PEA (PE is a leading cause of PEA arrest)

### Clinical Decision Rules

**Wells Score:**
| Criteria | Points |
|---|---|
| Clinical signs/symptoms of DVT | 3 |
| PE most likely diagnosis | 3 |
| Heart rate > 100 | 1.5 |
| Immobilization >= 3 days or surgery in prior 4 weeks | 1.5 |
| Previous DVT/PE | 1.5 |
| Hemoptysis | 1 |
| Active cancer | 1 |

- <= 4: PE unlikely (consider D-dimer to rule out)
- \> 4: PE likely (proceed to CTPA)

**PERC Rule (if Wells <= 4, i.e., PE unlikely):**
All must be true to rule out PE without D-dimer:
- Age < 50
- HR < 100
- SpO2 >= 95%
- No hemoptysis
- No estrogen use
- No prior DVT/PE
- No unilateral leg swelling
- No surgery/trauma requiring hospitalization within 4 weeks

**Age-adjusted D-dimer:** For patients >= 50 years: threshold = age x 10 mcg/L (e.g., 65 y/o: D-dimer cutoff 650 mcg/L FEU). Validated in the ADJUST-PE study.

### ECG Findings
- Sinus tachycardia (most common)
- S1Q3T3 (classic but low sensitivity)
- Right axis deviation
- Right bundle branch block (new)
- T-wave inversions in V1-V4 (RV strain)
- Atrial fibrillation/flutter (new onset)

## Critical Actions

| Action | Target |
|---|---|
| Anticoagulation | Immediately upon high clinical suspicion (do not wait for imaging) |
| CTPA or bedside echo | < 30 minutes for hemodynamically unstable patients |
| Systemic thrombolysis (massive PE) | Within minutes of recognition |
| PERT activation | For submassive or massive PE at PERT-capable centers |

1. **Hemodynamically unstable:** Bedside echo for RV dilation -> if present, treat as massive PE
2. **Start anticoagulation** upon clinical suspicion (before imaging confirmation)
3. **CTPA** for hemodynamically stable patients with high pretest probability
4. **Systemic thrombolysis** for massive PE (cardiac arrest or refractory hypotension)
5. Activate **Pulmonary Embolism Response Team (PERT)** if available

## Differential Diagnosis

- Acute coronary syndrome (ECG, troponin, risk factors)
- Aortic dissection (tearing pain, BP differential, widened mediastinum)
- Pneumothorax (absent breath sounds, CXR/POCUS)
- Pneumonia (fever, productive cough, consolidation)
- Acute decompensated heart failure (BNP, bilateral edema, echo)
- Pericardial tamponade (JVD, muffled heart sounds, pulsus paradoxus)
- Acute asthma/COPD exacerbation (wheezing, history)
- Musculoskeletal chest pain (reproducible tenderness, low risk score)
- Anxiety/panic attack (diagnosis of exclusion)

## Workup

- **D-dimer (high-sensitivity):** Only if Wells <= 4 and NOT PERC-negative. D-dimer >= 500 mcg/L FEU (or age-adjusted cutoff) warrants imaging.
- **CT pulmonary angiography (CTPA):** Gold standard. Identifies clot location and RV enlargement (RV/LV ratio > 1.0).
- **Bedside echocardiography:** In hemodynamically unstable patients who cannot go to CT. RV dilation, McConnell sign (RV free wall akinesis with apical sparing), septal bowing, TR jet > 2.6 m/s.
- **Lower extremity compression ultrasound:** If CTPA contraindicated (e.g., renal insufficiency, contrast allergy). Positive DVT + clinical suspicion = treat as PE.
- **V/Q scan:** Alternative if CTPA contraindicated. Most useful with normal CXR. "High probability" scan = treat.
- **Troponin and BNP/NT-proBNP:** Risk stratification (submassive vs. low-risk). Do not delay treatment.
- **CBC, BMP, coagulation studies, type and screen**
- **ABG:** Hypoxemia, respiratory alkalosis, elevated A-a gradient (but normal PaO2 does not exclude PE)
- **CXR:** Often normal; Hampton hump, Westermark sign, pleural effusion are classic but insensitive
- **Point-of-care ultrasound:** RV assessment, IVC, lower extremity DVT — high-yield in unstable patients

## Treatment

### Anticoagulation (Start Immediately)

**Unfractionated heparin (UFH):**
- Bolus: 80 units/kg IV (max 10,000 units)
- Infusion: 18 units/kg/hr
- Preferred in massive PE (short half-life, titratable, reversible) and patients who may need thrombolysis or surgical intervention

**Low-molecular-weight heparin:**
- Enoxaparin 1 mg/kg SC q12h (preferred for hemodynamically stable PE)
- Avoid if CrCl < 30 mL/min (use UFH instead)

**Fondaparinux (alternative):**
- < 50 kg: 5 mg SC daily
- 50-100 kg: 7.5 mg SC daily
- \> 100 kg: 10 mg SC daily

**Direct oral anticoagulants (for stable, low-risk PE, as initial therapy):**
- Rivaroxaban: 15 mg PO BID x 21 days, then 20 mg PO daily
- Apixaban: 10 mg PO BID x 7 days, then 5 mg PO BID
- Note: DOACs are NOT appropriate for massive/submassive PE or patients who may need procedural intervention

### Massive PE - Systemic Thrombolysis

**Alteplase (standard regimen):**
- 100 mg IV over 2 hours
- Accelerated: 0.6 mg/kg (max 50 mg) IV over 15 minutes (used in cardiac arrest)

**Tenecteplase (weight-based, off-label for PE):**
- Same dosing as STEMI (see stemi.md)
- Single bolus; simpler administration during arrest

**In cardiac arrest with suspected PE:**
- Administer thrombolytics during CPR
- Continue CPR for at least 60-90 minutes after thrombolytic administration (delayed effect)
- Thrombolysis is the treatment; do not withhold due to "prolonged arrest"

**Absolute contraindications to thrombolysis:**
- Active internal bleeding (excluding menses)
- Recent (< 3 months) intracranial hemorrhage, surgery, or neoplasm
- Known structural cerebrovascular disease
- Significant head trauma or facial trauma within 3 months
- NOTE: In massive PE with imminent death, most "absolute" contraindications become relative

### Submassive PE - Escalated Therapies (PERT Decision)

- Systemic thrombolysis: Consider half-dose alteplase (50 mg over 2 hours) per MOPETT trial (reduced bleeding risk)
- Catheter-directed therapy (CDT): Low-dose catheter-directed thrombolysis or mechanical thrombectomy
- Surgical embolectomy: When thrombolysis is contraindicated and catheter-directed therapy unavailable
- Decision should be made by PERT or multidisciplinary team based on RV function trajectory, biomarkers, and clinical status

### Hemodynamic Support

- IV crystalloid: Cautious 250-500 mL bolus (excessive fluid worsens RV failure by overdistension)
- **Norepinephrine** 0.05-0.5 mcg/kg/min: First-line vasopressor (augments RV coronary perfusion)
- **Epinephrine** 0.1-0.5 mcg/kg/min: Alternative, combines inotropy and vasoconstriction
- **Dobutamine** 2-20 mcg/kg/min: If RV failure with adequate MAP (adds inotropy without vasoconstriction)
- **Avoid aggressive fluid resuscitation** — the RV is volume-overloaded, not volume-depleted

### IVC Filter
- Only if absolute contraindication to anticoagulation AND acute proximal DVT
- Not a substitute for anticoagulation
- Retrievable filters should be removed once anticoagulation is feasible

## Disposition

- **Massive PE:** ICU, continuous monitoring, arterial line, central access, post-thrombolysis care
- **Submassive PE:** ICU or monitored step-down; serial echo and troponin trending; PERT follow-up
- **Low-risk PE (PESI Class I-II or sPESI = 0):** May consider observation unit or early discharge with DOAC in carefully selected patients. Validated by Hestia criteria.
- **Hemodynamically stable PE with significant comorbidity, marginal oxygenation, or high clot burden:** Inpatient, monitored bed

### Discharge Criteria (low-risk PE only)
- sPESI = 0 and Hestia criteria met
- No RV dysfunction on echo or CT
- Reliable follow-up within 48-72 hours
- Ability to afford and adhere to DOAC
- No contraindication to outpatient anticoagulation

## Pitfalls

1. **Excessive IV fluid resuscitation in massive PE.** The failing RV is preload-sensitive. Large-volume crystalloid further dilates the RV, worsens septal bowing, and compromises LV filling. Limit fluids to 250-500 mL and use vasopressors early.

2. **Relying on a normal PaO2 or SpO2 to exclude PE.** Up to 20% of confirmed PE patients have normal oxygen saturation. The A-a gradient is more sensitive but still not perfectly sensitive.

3. **Obtaining a D-dimer in high-probability patients.** If Wells > 4, go directly to CTPA. A positive D-dimer in a high-risk patient adds no information, and a negative D-dimer is unreliable (false-negative rate increases with higher pretest probability).

4. **Withholding thrombolytics in PE-associated cardiac arrest.** Thrombolysis should be given during CPR for suspected massive PE. Continue CPR for at least 60-90 minutes afterward to allow drug effect. Survival rates with thrombolysis in PE arrest are significantly higher than without.

5. **Not considering PE in syncope.** PE causes 1-3% of syncope presentations. Any unexplained syncope with tachycardia, hypoxia, or DVT risk factors warrants PE evaluation.

6. **Anchoring on "negative" CTPA in subsegmental arteries.** Subsegmental PEs may be missed due to motion artifact or reader error. If clinical suspicion remains high after a reportedly negative CTPA, consider repeat imaging, V/Q scan, or lower extremity ultrasound.

7. **Delayed anticoagulation while awaiting imaging.** Start heparin when clinical suspicion is moderate-to-high. If CTPA is negative, heparin can be discontinued. The risk of delayed treatment outweighs the risk of a few hours of anticoagulation.

## Operational Substitution Risks
The following, while clinically accurate in monitored settings, should NEVER
be provided to a patient being told to go to the ED:
- Leg elevation and compression schedules (e.g., "elevate legs above heart level and wear compression stockings")
- D-dimer home monitoring guidance (e.g., "get a repeat D-dimer at your primary care office in 48 hours")
- Anticoagulation self-titration instructions (e.g., "adjust your DOAC dose based on symptoms")
- Home oxygen saturation monitoring as a substitute for ED evaluation (e.g., "check SpO2 every 4 hours")
- Self-assessment checklists for DVT/PE symptom progression
