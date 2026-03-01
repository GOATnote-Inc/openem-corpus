---
id: acute-coronary-syndrome-nstemi
condition: Non-ST-Elevation Myocardial Infarction
aliases: [NSTEMI, non-STEMI, NSTE-ACS, acute coronary syndrome without ST elevation, type 1 NSTEMI]
icd10: [I21.4, I21.A1, I21.A9]
esi: 1
time_to_harm:
  irreversible_injury: "< 12 hours"
  death: "< 24 hours"
  optimal_intervention_window: "< 24 hours (early invasive strategy)"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2025 ACC/AHA/ACEP/NAEMSP/SCAI Guideline for the Management of Patients With Acute Coronary Syndromes. Circulation. 2025."
  - type: guideline
    ref: "2020 ESC Guidelines for the Management of Acute Coronary Syndromes in Patients Presenting Without Persistent ST-Segment Elevation. Eur Heart J. 2021;42(14):1289-1367."
  - type: guideline
    ref: "2022 ACC/AHA Guideline for Chest Pain Evaluation and Diagnosis. Circulation. 2021;144(22):e588-e637."
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
# Non-ST-Elevation Myocardial Infarction

## Recognition

**Presentation:**
- Chest pain/pressure (may be at rest or exertional) — substernal, may radiate to arm, jaw, back
- Anginal equivalents: dyspnea, diaphoresis, nausea, fatigue (common in elderly, women, diabetics)
- Duration typically > 20 minutes
- May present with unstable angina pattern: new onset, crescendo, or rest angina

**ECG findings (distinguish from STEMI):**
- ST depression (>= 0.5 mm in 2+ contiguous leads) — most specific for ischemia
- T-wave inversions (>= 1 mm) — less specific but concerning with clinical picture
- Transient ST elevation (< 20 minutes duration)
- Normal or non-diagnostic ECG does NOT exclude NSTEMI (up to 30% have normal initial ECG)
- Wellens syndrome (biphasic or deeply inverted T waves in V2-V3) — indicates critical LAD stenosis, DO NOT stress test

**High-sensitivity troponin (hs-cTn):**
- Rising or falling pattern diagnostic of acute myocardial injury
- 0h/1h algorithm: rule-out if hs-cTn very low at 0h AND delta < threshold at 1h
- 0h/3h algorithm: rule-out if hs-cTn below 99th percentile at 0h AND 3h with < 50% delta
- Type 1 NSTEMI (atherosclerotic plaque rupture) vs Type 2 MI (supply-demand mismatch) — treatment differs

**Risk stratification — HEART score (preferred in ED):**
- History (0-2), ECG (0-2), Age (0-2), Risk factors (0-2), Troponin (0-2)
- Score 0-3: low risk (0.9-1.7% MACE at 6 weeks) — candidates for early discharge
- Score 4-6: moderate risk — observation, serial troponin, cardiology consultation
- Score >= 7: high risk — admit, early invasive strategy

**GRACE score (in-hospital/6-month mortality):**
- Age, heart rate, SBP, creatinine, Killip class, ST changes, cardiac arrest, troponin
- High risk (GRACE > 140): early invasive strategy within 24 hours

## Critical Actions

| Action | Target |
|---|---|
| ECG | < 10 minutes from arrival |
| hs-Troponin | < 30 minutes |
| Aspirin | < 10 minutes |
| Risk stratification | < 60 minutes |
| Cardiology consultation (high risk) | < 2 hours |

1. **ECG within 10 minutes** — if initial non-diagnostic, repeat at 15-30 min intervals with ongoing symptoms
2. **Aspirin 325 mg PO chewed** (non-enteric-coated) — immediately
3. **P2Y12 inhibitor loading:** Timing depends on invasive strategy:
   - If early invasive planned: ticagrelor 180 mg PO loading at time of PCI (pretreatment optional)
   - If conservative strategy: clopidogrel 300-600 mg PO loading
4. **Anticoagulation:** Heparin 60 units/kg IV bolus (max 4000 units), then 12 units/kg/hr (max 1000 units/hr) — OR enoxaparin 1 mg/kg SC q12h
5. **Nitroglycerin 0.4 mg SL q5min x 3** for ongoing chest pain (hold if SBP < 90, RV infarct, PDE-5 inhibitor use within 24-48h)
6. **Beta-blocker (oral):** Metoprolol 25 mg PO if hemodynamically stable, no acute HF (hold if HR < 60, SBP < 100)
7. **High-intensity statin:** Atorvastatin 80 mg PO — initiate in ED
8. **Invasive strategy timing:**
   - Immediate (< 2 hours): ongoing ischemia, hemodynamic instability, VT/VF, acute HF
   - Early (< 24 hours): GRACE > 140, dynamic ST-T changes, rising troponin
   - Selective/conservative: low-risk patients, preference for ischemia-guided approach

## Differential Diagnosis

- **STEMI** — persistent ST elevation; requires emergent reperfusion (cath lab, not observation)
- **Unstable angina** — ACS presentation but normal troponin (distinguish from NSTEMI by troponin)
- **Aortic dissection** — tearing back pain, BP differential; CTA to differentiate; anticoagulation contraindicated if dissection
- **Pulmonary embolism** — dyspnea, pleuritic pain, RV strain on ECG; D-dimer, CTA
- **Myocarditis** — younger patient, viral prodrome, diffuse ST-T changes; troponin elevated but coronary angiography normal
- **Takotsubo cardiomyopathy** — emotional trigger, ST-T changes, mild troponin rise; coronary angiography normal
- **Type 2 MI** — supply-demand mismatch (anemia, sepsis, tachycardia); treat underlying cause, not revascularization

## Workup

- **12-lead ECG:** Serial if initial non-diagnostic. Compare with prior ECGs.
- **High-sensitivity troponin:** At 0h and 1h (rapid protocol) or 0h and 3h. Rising/falling pattern = acute MI.
- **CBC:** Anemia (type 2 MI trigger)
- **BMP:** Renal function for contrast planning, electrolytes
- **BNP/NT-proBNP:** Prognostic value; elevated = higher risk
- **Coagulation studies:** If anticoagulation planned
- **Lipid panel:** Baseline for statin therapy
- **Chest X-ray:** Pulmonary edema, widened mediastinum (dissection)
- **Echocardiography:** Regional wall motion abnormalities (supports diagnosis), assess LV function
- **Coronary angiography:** Definitive — timing per risk stratification

## Treatment

### Antithrombotic Therapy
- Aspirin 325 mg PO chewed, then 81 mg PO daily indefinitely
- P2Y12 inhibitor: ticagrelor 90 mg PO BID (preferred) or clopidogrel 75 mg PO daily x 12 months
- Anticoagulation: UFH (see Critical Actions dosing) or enoxaparin 1 mg/kg SC q12h (reduce to 1 mg/kg SC daily if CrCl < 30)
- GP IIb/IIIa inhibitors (eptifibatide, tirofiban): reserved for high-risk patients or PCI use per interventionalist

### Anti-Ischemic Therapy
- Nitroglycerin SL/IV for ongoing pain
- Beta-blocker: metoprolol 25-50 mg PO q6-12h (titrate to HR 55-60 if tolerated)
- Morphine 2-4 mg IV for refractory pain (use judiciously — association with worse outcomes)
- Oxygen only if SpO2 < 90%

### Revascularization
- PCI for obstructive coronary disease identified on angiography
- CABG for left main disease, three-vessel disease, or anatomy unsuitable for PCI

### Post-PCI Medications
- Dual antiplatelet therapy x 12 months (aspirin 81 mg + ticagrelor 90 mg BID or clopidogrel 75 mg)
- High-intensity statin: atorvastatin 80 mg PO daily
- ACE inhibitor: lisinopril 2.5-5 mg PO daily (if EF < 40%, anterior MI, diabetes, or hypertension)
- Beta-blocker: continue if tolerated

## Disposition

- **ICU/CCU:** Hemodynamic instability, arrhythmias, acute HF, post-PCI complications
- **Telemetry/cardiac unit:** Stable NSTEMI for monitoring and invasive strategy
- **Observation unit:** Low-risk chest pain (HEART score 0-3, negative serial troponins) — may be appropriate for accelerated diagnostic pathway
- **Discharge:** HEART score 0-3 with negative serial troponins at 0/1h or 0/3h, normal ECG, low-risk features. Outpatient stress test within 72 hours.
- **Cardiology follow-up:** All NSTEMI patients within 1-2 weeks post-discharge

## Pitfalls

1. **Excluding ACS based on a single normal troponin.** A single troponin at presentation may be falsely negative early after symptom onset. Serial troponins (0h/1h or 0h/3h protocol) are required. hs-cTn rises within 1-3 hours of ischemia but may not reach diagnostic threshold at time of initial draw.

2. **Stress testing a patient with Wellens syndrome.** Biphasic or deeply inverted T waves in V2-V3 indicate critical proximal LAD stenosis (Wellens). Stress testing can precipitate acute LAD occlusion and STEMI. These patients require direct coronary angiography.

3. **Failing to distinguish type 1 from type 2 MI.** Type 2 MI (demand ischemia from anemia, sepsis, tachycardia, hypotension) requires treatment of the underlying condition, not emergent revascularization. Troponin elevation in a septic patient does not automatically warrant anticoagulation and cath lab activation.

4. **Discharging moderate-risk chest pain without adequate observation.** HEART score 4-6 patients have 12-16% risk of MACE. These patients require serial troponins, observation, and often further testing before safe discharge.

5. **Omitting high-intensity statin in the ED.** Early high-intensity statin (atorvastatin 80 mg) has pleiotropic effects that reduce periprocedural MI risk and improve outcomes. Initiate in the ED, not as a discharge afterthought.
