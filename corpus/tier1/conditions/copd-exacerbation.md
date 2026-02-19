---
id: copd-exacerbation
condition: Acute Exacerbation of Chronic Obstructive Pulmonary Disease
aliases: [AECOPD, COPD flare, COPD exacerbation, acute on chronic COPD, chronic bronchitis exacerbation]
icd10: [J44.1, J44.0]
esi: 2
time_to_harm: "< 2 hours"
mortality_if_delayed: "In-hospital mortality 2-11%; rises with delayed NIV in hypercapnic respiratory failure"
category: respiratory
track: tier1
sources:
  - type: guideline
    ref: "2024 GOLD Report: Global Strategy for the Diagnosis, Management, and Prevention of COPD"
    url: https://goldcopd.org/2024-gold-report/
  - type: guideline
    ref: "ATS/ERS 2017: Management of COPD Exacerbations — An American Thoracic Society/European Respiratory Society Clinical Practice Guideline"
    doi: "10.1164/rccm.201510-2076ST"
  - type: pubmed
    ref: "Wedzicha JA, Miravitlles M, Hurst JR, et al. Management of COPD exacerbations: a European Respiratory Society/American Thoracic Society guideline. Eur Respir J. 2017;49(3):1600791"
    pmid: "28298398"
last_updated: "2026-02-18"
compiled_by: agent
risk_tier: B
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
# Acute Exacerbation of COPD

## Recognition

**Definition:** Acute sustained worsening of dyspnea, cough, and/or sputum (volume or purulence) beyond normal day-to-day variation, requiring a change in therapy.

### Severity Classification
- **Mild:** Treated with short-acting bronchodilators alone
- **Moderate:** Requires short-acting bronchodilators plus antibiotics and/or oral corticosteroids
- **Severe:** Requires ED visit or hospitalization; may include respiratory failure

### Key Findings
- Increased dyspnea, wheeze, chest tightness
- Increased sputum volume and/or purulence
- Accessory muscle use, tripod positioning
- Prolonged expiratory phase, diffuse expiratory wheezing
- Diminished breath sounds ("silent chest" = impending respiratory failure)
- Tachypnea, tachycardia, diaphoresis
- Altered mental status (hypercapnia)
- Cyanosis, paradoxical abdominal wall motion

### ABG Patterns
- Acute hypercapnic respiratory failure: pH < 7.35, PaCO2 > 45 mmHg
- Chronic compensated: normal pH, elevated PaCO2, elevated HCO3
- Acute on chronic: pH < 7.35, PaCO2 above baseline, elevated HCO3 (partial compensation)

## Critical Actions

| Action | Target |
|---|---|
| Supplemental O2 | SpO2 88-92% (avoid hyperoxia) |
| Nebulized SABA | Within 15 minutes of arrival |
| Systemic corticosteroids | Within 1 hour |
| NIV (BiPAP) | Immediately if pH < 7.35 with PaCO2 > 45 |
| ABG/VBG | Within 30 minutes for moderate-severe presentations |
| Antibiotics | If purulent sputum or requiring mechanical ventilation |

1. Target SpO2 88-92% with controlled supplemental oxygen (nasal cannula or Venturi mask)
2. Administer albuterol 2.5 mg nebulized every 20 minutes x 3, then every 1-4 hours
3. Add ipratropium 0.5 mg nebulized with first 3 albuterol treatments
4. Prednisone 40 mg PO or methylprednisolone 125 mg IV if unable to take PO
5. Initiate BiPAP (IPAP 10-15 cmH2O, EPAP 5 cmH2O) for pH < 7.35 with hypercapnia
6. Obtain ABG or VBG to quantify acid-base status

## Differential Diagnosis

- Acute decompensated heart failure (orthopnea, JVD, B-lines on POCUS, BNP elevated)
- Pneumonia (focal consolidation, fever, productive cough)
- Pulmonary embolism (pleuritic pain, DVT risk factors, unilateral leg swelling)
- Pneumothorax (absent breath sounds unilaterally, pleuritic pain, hypotension if tension)
- Acute coronary syndrome (chest pressure, diaphoresis, ECG changes, troponin elevation)
- Asthma exacerbation (younger patient, reversible obstruction, no smoking history)
- Anxiety/hyperventilation (diagnosis of exclusion; confirm normal O2, CO2, imaging)
- Upper airway obstruction (stridor, foreign body, angioedema)

## Workup

- **ABG or VBG:** pH, PaCO2, PaO2, HCO3 — drives NIV decision and intubation threshold
- **Chest X-ray:** Rule out pneumonia, pneumothorax, pleural effusion, pulmonary edema
- **ECG:** Evaluate for arrhythmia (multifocal atrial tachycardia common), right heart strain, ACS
- **CBC:** Leukocytosis (infection), eosinophilia (asthma overlap), polycythemia (chronic hypoxia)
- **BMP:** Electrolytes, renal function, HCO3 (chronic compensation baseline)
- **BNP/NT-proBNP:** If CHF in the differential
- **Troponin:** If ACS suspected or significant tachycardia
- **Procalcitonin:** Supports bacterial etiology; aids antibiotic decision
- **Sputum culture:** Only if not responding to empiric antibiotics or MDR risk
- **Point-of-care ultrasound:** Lung sliding (pneumothorax), B-lines (pulmonary edema), cardiac function, IVC

## Treatment

### Bronchodilators
- **Albuterol:** 2.5 mg nebulized every 20 minutes x 3, then every 1-4 hours as needed
- **Ipratropium:** 0.5 mg nebulized every 20 minutes x 3 (with initial albuterol treatments)
- Continuous nebulization (albuterol 10-15 mg/hour) for severe exacerbations not responding to intermittent dosing
- MDIs with spacer are equivalent to nebulizers in patients able to coordinate

### Corticosteroids
- **Prednisone 40 mg PO daily x 5 days** (REDUCE trial: 5-day course non-inferior to 14-day)
- **Methylprednisolone 125 mg IV** if unable to take PO, then transition to PO
- Do NOT taper if course is 5 days or less

### Antibiotics (indicated if purulent sputum, requiring ventilatory support, or severe exacerbation)
- **Azithromycin 500 mg PO day 1, then 250 mg PO daily x 4 days**
- **OR doxycycline 100 mg PO BID x 5-7 days**
- **OR amoxicillin-clavulanate 875/125 mg PO BID x 5-7 days** (if recent antibiotic use)
- **Levofloxacin 750 mg PO/IV daily x 5 days** reserved for patients with risk factors for Pseudomonas or treatment failure

### Non-Invasive Ventilation
- **BiPAP:** Start IPAP 10-15 cmH2O, EPAP 5 cmH2O; titrate IPAP by 2 cmH2O every 5-10 minutes targeting tidal volume 6-8 mL/kg and improved pH
- Indications: pH < 7.35 with PaCO2 > 45, severe dyspnea with accessory muscle use or paradoxical breathing
- Contraindications: cardiac/respiratory arrest, hemodynamic instability, inability to protect airway, facial trauma/burns, copious secretions
- NNT = 4 to prevent intubation; NNT = 10 to prevent death (Cochrane data)

### Intubation
- Required when NIV fails (worsening pH, mental status, or hemodynamics after 1-2 hours of NIV)
- Use lower respiratory rates (10-12/min) and longer expiratory times to prevent auto-PEEP
- Target plateau pressure < 30 cmH2O
- Initial settings: tidal volume 6-8 mL/kg IBW, rate 10-12, PEEP 5 cmH2O, FiO2 to target SpO2 88-92%

### Adjuncts
- **Magnesium sulfate 2 g IV over 20 minutes** — limited evidence, may benefit severe bronchospasm not responding to standard therapy
- **IV aminophylline** — NOT recommended; marginal benefit with significant toxicity

## Disposition

- **ICU:** Respiratory failure requiring intubation, hemodynamic instability, altered mental status not improving with NIV, severe acidosis (pH < 7.25)
- **Step-down/monitored bed:** Responding to NIV, pH 7.25-7.35, requiring frequent respiratory assessments
- **General medical floor:** Moderate exacerbation responding to bronchodilators and steroids, stable oxygenation, no NIV requirement
- **Discharge from ED:** Mild exacerbation with rapid improvement, SpO2 > 88% on home O2, adequate follow-up within 48-72 hours, prescription for prednisone 40 mg PO daily x 5 days and rescue inhaler
- **Discharge requirements:** Able to ambulate, eat, sleep, and manage secretions; O2 requirement at or near baseline; reliable follow-up arranged

## Pitfalls

1. **Targeting SpO2 > 94% with high-flow oxygen.** Hyperoxia suppresses hypoxic respiratory drive and worsens hypercapnia. Target SpO2 88-92%. Use Venturi mask for precise FiO2 delivery.

2. **Delaying NIV in hypercapnic respiratory failure.** BiPAP reduces intubation rates and mortality. Start immediately when pH < 7.35 with elevated PaCO2. Waiting for ABG confirmation when clinical picture is clear wastes critical time.

3. **Relying on VBG alone without understanding its limitations.** VBG PaCO2 is approximately 3-8 mmHg higher than arterial. Venous pH correlates well with arterial pH. Acceptable for trending but obtain ABG if clinical picture and VBG discordant.

4. **Attributing all wheezing to COPD without chest imaging.** Pneumothorax, pulmonary embolism, and acute heart failure all cause dyspnea and wheezing in COPD patients. Chest X-ray is mandatory.

5. **Using excessive tidal volumes and rates during mechanical ventilation.** Auto-PEEP (breath stacking) causes hemodynamic collapse. Use lower rates (10-12/min), longer expiratory times (I:E ratio 1:3 to 1:5), and monitor plateau pressures.

6. **Discharging without a 5-day steroid course.** Oral prednisone 40 mg daily x 5 days reduces treatment failure. Ensure patients leave with a prescription and understand completion of course.

7. **Not addressing the trigger.** Identify why the patient decompensated — medication non-adherence, pneumonia, PE, environmental exposure, or new arrhythmia. Treat the underlying cause alongside the exacerbation.

8. **Missing concurrent PE in COPD exacerbation.** PE prevalence is 3-25% in patients hospitalized for AECOPD. Maintain a low threshold for CTPA in patients not responding to standard treatment or with risk factors for VTE.

9. **Failing to reassess after initial interventions.** Serial ABG/VBG measurements, respiratory rate, work of breathing, and mental status should drive escalation decisions. A single set of vitals at triage is insufficient.
