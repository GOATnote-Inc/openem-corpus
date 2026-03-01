---
id: acute-respiratory-failure
condition: Acute Respiratory Failure
aliases: [ARF, type 1 respiratory failure, type 2 respiratory failure, hypoxemic respiratory failure, hypercapnic respiratory failure]
icd10: [J96.00, J96.01, J96.02, J96.20, J96.21, J96.22]
esi: 1
time_to_harm:
  irreversible_injury: "< 10 minutes (complete failure)"
  death: "< 30 minutes"
  optimal_intervention_window: "< 5 minutes"
category: respiratory
track: tier1
sources:
  - type: guideline
    ref: "2024 ATS Clinical Practice Guideline: An Update on Management of Adult Patients With Acute Respiratory Distress Syndrome. Am J Respir Crit Care Med. 2024;209(1):24-36."
  - type: review
    ref: "Stefan MS, et al. Diagnosis and Management of Acute Respiratory Failure. Crit Care Clin. 2024;40(2):235-250."
  - type: guideline
    ref: "2017 ERS/ATS Guidelines for the Use of NIV in Acute Respiratory Failure. Eur Respir J. 2017;50(2):1602426."
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
# Acute Respiratory Failure

## Recognition

**Type 1 — Hypoxemic respiratory failure:**
- PaO2 < 60 mmHg on room air (or P/F ratio < 300 on supplemental O2)
- PaCO2 normal or low (hyperventilation compensation)
- Etiologies: pneumonia, ARDS, pulmonary edema, PE, pneumothorax, atelectasis, interstitial lung disease

**Type 2 — Hypercapnic respiratory failure:**
- PaCO2 > 50 mmHg with pH < 7.35 (acute)
- PaO2 often also low
- Etiologies: COPD exacerbation, asthma, neuromuscular disease (Guillain-Barre, myasthenia gravis), drug overdose (opioids, benzodiazepines), obesity hypoventilation, flail chest

**Type 3 — Perioperative (atelectatic):**
- Post-surgical hypoventilation, atelectasis, diaphragm dysfunction

**Type 4 — Shock-related:**
- Hypoperfusion causing respiratory muscle fatigue, lactic acidosis driving compensatory tachypnea

**Clinical signs of impending respiratory failure:**
- Tachypnea > 30 breaths/min, accessory muscle use, nasal flaring
- Paradoxical abdominal breathing (diaphragm fatigue)
- Inability to speak in full sentences
- Altered mental status (hypercapnia → somnolence; hypoxemia → agitation)
- SpO2 < 88% despite supplemental O2
- Silent chest in asthma (too little airflow for wheeze)

## Critical Actions

| Action | Target |
|---|---|
| Supplemental O2 | Immediate — SpO2 > 92% |
| ABG | < 15 minutes |
| Identify cause | < 30 minutes |
| Intubation if indicated | < 15 minutes of recognition |

1. **Supplemental oxygen** — titrate to SpO2 92-96% (88-92% in COPD with chronic CO2 retention)
2. **Assess airway patency** — suction, positioning, jaw thrust
3. **ABG** — classify type 1 vs 2, assess A-a gradient, pH
4. **Noninvasive support escalation:**
   - High-flow nasal cannula (HFNC): 40-60 L/min, FiO2 titrated — first-line for type 1 (non-COPD, non-CHF)
   - BiPAP: IPAP 10-20 cmH2O, EPAP 5-10 cmH2O — first-line for type 2 (COPD, obesity hypoventilation)
   - CPAP: 5-10 cmH2O — first-line for cardiogenic pulmonary edema
5. **Intubation indications:**
   - Failure to protect airway (GCS <= 8)
   - Failure of noninvasive support (worsening gas exchange, respiratory fatigue)
   - Hemodynamic instability
   - Anticipated clinical deterioration
6. **Post-intubation ventilator settings:**
   - TV 6-8 mL/kg ideal body weight
   - RR 14-20 breaths/min
   - PEEP 5-10 cmH2O (higher in ARDS)
   - Plateau pressure < 30 cmH2O
7. **Treat underlying cause** — antibiotics for pneumonia, diuretics for CHF, bronchodilators for COPD/asthma, reversal agents for overdose

## Differential Diagnosis

- **Cardiogenic pulmonary edema** — bilateral crackles, elevated BNP, S3, orthopnea; responds to diuretics and CPAP
- **Pneumonia** — fever, productive cough, focal consolidation on CXR
- **COPD/asthma exacerbation** — wheezing, prolonged expiration, hyperinflation on CXR
- **Pulmonary embolism** — pleuritic pain, tachycardia, DVT risk factors; CTA diagnostic
- **Pneumothorax** — absent breath sounds, pleuritic pain; CXR or US diagnostic
- **ARDS** — bilateral opacities, P/F < 300, no cardiogenic cause
- **Neuromuscular weakness** — paradoxical breathing, weak cough, NIF < -20 cmH2O
- **Upper airway obstruction** — stridor, drooling, positional distress

## Workup

- **ABG:** PaO2, PaCO2, pH, A-a gradient (normal < 15 mmHg; elevated = V/Q mismatch or shunt)
- **Chest X-ray:** Infiltrates, effusion, pneumothorax, cardiomegaly, hyperinflation
- **Labs:** CBC, BMP, BNP/NT-proBNP (cardiogenic vs non-cardiogenic), lactate, troponin, procalcitonin
- **CT chest:** If CXR non-diagnostic — PE protocol if indicated
- **Point-of-care ultrasound:** B-lines (pulmonary edema), A-lines (COPD/PE), lung sliding (pneumothorax), pleural effusion, cardiac function
- **Bedside spirometry/NIF:** If neuromuscular cause suspected (NIF < -20 cmH2O or FVC < 20 mL/kg = impending failure in GBS/MG)
- **Toxicology screen:** If overdose suspected

## Treatment

### Type 1 — Hypoxemic
- HFNC 40-60 L/min (preferred over conventional O2 in acute hypoxemic failure, per FLORALI trial)
- If HFNC fails: BiPAP with high EPAP (8-12 cmH2O) for recruitment
- Intubation with lung-protective ventilation if noninvasive support fails
- Treat cause: antibiotics, diuretics, chest tube, anticoagulation

### Type 2 — Hypercapnic
- BiPAP: IPAP 10-20, EPAP 5-10 cmH2O — NNT=5 for COPD exacerbation to avoid intubation
- Assess within 1-2 hours: if pH improving and RR decreasing, continue; if worsening, intubate
- COPD: nebulized albuterol 2.5 mg + ipratropium 0.5 mg q20min x 3, then q4h; methylprednisolone 125 mg IV
- Overdose: naloxone 0.4-2 mg IV for opioids; flumazenil 0.2 mg IV for benzodiazepines (use cautiously — seizure risk)

### Cardiogenic Pulmonary Edema
- CPAP 5-10 cmH2O or BiPAP (IPAP 10-15, EPAP 5-10)
- Furosemide 40-80 mg IV
- Nitroglycerin 10-200 mcg/min IV for afterload reduction (if SBP > 100)
- Morphine 2-4 mg IV cautiously (may worsen respiratory depression)

### Post-Intubation Management
- Lung-protective ventilation: TV 6-8 mL/kg IBW, Pplat < 30 cmH2O
- PEEP titration per FiO2-PEEP table (ARDSNet)
- Driving pressure < 15 cmH2O (Pplat - PEEP)
- Prone positioning if P/F < 150 (severe ARDS) for >= 16 hours/day

## Disposition

- **ICU admission:** All intubated patients, severe ARDS, hemodynamic instability, BiPAP/HFNC failure, neuromuscular respiratory failure
- **Monitored/step-down:** Stable patients on HFNC or BiPAP with improving gas exchange
- **ED observation:** Mild exacerbation responding to treatment (e.g., COPD with pH normalizing on BiPAP)
- **Transfer:** Facilities without ICU ventilator capability or ECMO for refractory ARDS

## Pitfalls

1. **Delaying intubation in a deteriorating patient.** Noninvasive support should be reassessed within 1-2 hours. Worsening tachypnea, encephalopathy, or hemodynamic instability on NIV indicates failure. Crash intubation in an exhausted, hypoxic patient is far more dangerous than timely elective intubation.

2. **Giving high-flow oxygen to a chronic CO2 retainer without monitoring.** COPD patients who chronically retain CO2 rely on hypoxic drive. High-flow O2 can suppress respiratory drive, worsen hypercapnia, and cause CO2 narcosis. Target SpO2 88-92% and follow serial ABGs.

3. **Failing to measure NIF/FVC in suspected neuromuscular respiratory failure.** Patients with GBS or myasthenia gravis can maintain SpO2 until precipitous decompensation. Serial NIF and FVC measurements detect declining respiratory muscle strength before overt failure. Intubate when NIF < -20 cmH2O or FVC < 20 mL/kg (the 20/20 rule).

4. **Attributing hypoxemia to COPD exacerbation without considering PE.** COPD patients have increased VTE risk. Acute hypoxemia out of proportion to bronchospasm should raise suspicion for PE. Check D-dimer or obtain CTA if pretest probability is not low.

5. **Using excessive tidal volumes after intubation.** High tidal volumes (> 8 mL/kg IBW) cause ventilator-induced lung injury (VILI) and worsen ARDS. Use 6-8 mL/kg predicted body weight and monitor plateau pressures. This applies to ALL mechanically ventilated patients, not just those with ARDS.
