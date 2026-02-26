---
id: pneumonia
condition: Pneumonia
aliases: [pneumonia, community-acquired pneumonia, CAP, hospital-acquired pneumonia, HAP, aspiration pneumonia, lower respiratory tract infection, LRTI]
icd10: [J18.9, J15.9, J13, J14, J69.0, J15.1]
esi: 2
time_to_harm: "< 4 hours"
mortality_if_delayed: "CAP mortality 1-5% outpatient, 5-25% inpatient, 30-50% ICU; increases with delayed antibiotics"
category: respiratory
track: tier1
sources:
  - type: guideline
    ref: "ATS/IDSA 2019 Diagnosis and Treatment of Adults with Community-acquired Pneumonia: An Official Clinical Practice Guideline"
    doi: "10.1164/rccm.201908-1581ST"
    pmid: "31573350"
  - type: guideline
    ref: "ATS/IDSA 2016 Clinical Practice Guidelines for Management of Adults with Hospital-acquired and Ventilator-associated Pneumonia"
    doi: "10.1093/cid/ciw353"
    pmid: "27418577"
  - type: guideline
    ref: "2023 Surviving Sepsis Campaign Guidelines (pneumonia-related sepsis management)"
  - type: review
    ref: "Mandell LA, Niederman MS. Aspiration Pneumonia. N Engl J Med. 2019;380(7):651-663"
    pmid: "30763196"
    doi: "10.1056/NEJMra1714562"
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
  provenance_links: []
---
# Pneumonia

## Recognition

### Classification

| Type | Definition |
|---|---|
| Community-acquired pneumonia (CAP) | Acquired outside hospital or < 48 hours after admission |
| Hospital-acquired pneumonia (HAP) | Onset >= 48 hours after admission, not incubating at admission |
| Ventilator-associated pneumonia (VAP) | Onset >= 48 hours after endotracheal intubation |
| Aspiration pneumonia | Pneumonia following witnessed or suspected aspiration event; commonly in right lower lobe |

### Clinical Presentation
- Cough (productive or dry), dyspnea, pleuritic chest pain
- Fever (may be absent in elderly or immunocompromised)
- Tachypnea, tachycardia, hypoxia
- Lung exam: crackles, bronchial breath sounds, egophony, dullness to percussion
- Elderly: altered mental status, falls, or functional decline may be the only presenting signs

### CURB-65 Severity Score (1 point each)
| Criterion | Definition |
|---|---|
| **C**onfusion | New altered mental status |
| **U**rea | BUN > 20 mg/dL (> 7 mmol/L) |
| **R**espiratory rate | >= 30/min |
| **B**lood pressure | SBP < 90 or DBP <= 60 mmHg |
| **65** | Age >= 65 years |

| Score | Mortality | Disposition |
|---|---|---|
| 0-1 | 1.5% | Outpatient |
| 2 | 9.2% | Admit (short inpatient stay or close outpatient follow-up) |
| 3-5 | 22% | Admit; score >= 4 evaluate for ICU |

### PSI/PORT Score
- Validated for identifying low-risk patients safe for outpatient treatment
- Class I-II: outpatient. Class III: short observation or admit. Class IV-V: inpatient, consider ICU.
- Incorporates age, comorbidities, vital signs, labs, imaging

### ATS/IDSA Criteria for Severe CAP (ICU admission)
**Major criteria (1 = ICU):**
- Septic shock requiring vasopressors
- Respiratory failure requiring mechanical ventilation

**Minor criteria (>= 3 = ICU):**
- RR >= 30/min
- PaO2/FiO2 <= 250
- Multilobar infiltrates
- Confusion
- BUN >= 20 mg/dL
- WBC < 4,000
- Platelets < 100,000
- Core temperature < 36C
- Hypotension requiring aggressive fluid resuscitation

### Microbiology by Setting
| Setting | Common Pathogens |
|---|---|
| CAP (outpatient) | S. pneumoniae, M. pneumoniae, C. pneumoniae, respiratory viruses |
| CAP (inpatient) | S. pneumoniae, H. influenzae, Legionella, S. aureus, respiratory viruses |
| CAP (ICU) | S. pneumoniae, S. aureus (including MRSA), Legionella, gram-negatives, Pseudomonas (if risk factors) |
| HAP/VAP | Pseudomonas, MRSA, Klebsiella, Acinetobacter, Enterobacter |
| Aspiration | Mixed anaerobes, gram-negatives, S. pneumoniae |

## Critical Actions

| Action | Target |
|---|---|
| Chest X-ray | Confirm infiltrate |
| Severity scoring | CURB-65 or PSI within 30 minutes |
| Antibiotics | Within 4 hours (within 1 hour if sepsis) |
| Sepsis screening | qSOFA, lactate if any concern |
| Oxygenation | SpO2 >= 94% (>= 88% if COPD) |
| Blood cultures | Before antibiotics if inpatient/ICU (do NOT delay antibiotics) |

1. Obtain chest X-ray (or CT if high suspicion and CXR equivocal)
2. Calculate CURB-65 or PSI score
3. Screen for sepsis: qSOFA, lactate, vital signs
4. Obtain blood cultures x 2 if admitting (before antibiotics, but do NOT delay antibiotics)
5. Administer empiric antibiotics based on severity and risk factors
6. Supplemental oxygen to maintain SpO2 >= 94%
7. Determine disposition based on severity scoring and clinical judgment

## Differential Diagnosis

- Acute heart failure / pulmonary edema (bilateral infiltrates, BNP elevated, response to diuresis)
- Pulmonary embolism (pleuritic pain, hypoxia out of proportion to infiltrate, elevated D-dimer, CT angiography)
- Lung malignancy (mass on CXR, hemoptysis, weight loss, smoking history)
- COPD exacerbation (wheezing, hyperinflation, known COPD, minimal infiltrate)
- Asthma exacerbation (wheezing, known asthma, clear CXR)
- Tuberculosis (chronic cough, hemoptysis, upper lobe cavitation, risk factors, isolation required)
- Pleural effusion (dullness, decreased breath sounds, layer on CXR)
- Empyema (loculated effusion, fever despite antibiotics)
- COVID-19 / influenza (bilateral GGOs, epidemiologic context, rapid testing)

## Workup

- **Chest X-ray (PA and lateral):** Infiltrate confirms clinical diagnosis. CXR may lag behind clinical presentation by 12-24 hours in dehydrated or neutropenic patients. CT chest if CXR equivocal with high clinical suspicion.
- **CBC with differential:** Leukocytosis (bacterial), leukopenia (severe sepsis, viral), lymphopenia (viral)
- **BMP:** BUN for CURB-65 scoring, creatinine for drug dosing, electrolytes
- **Lactate:** STAT if sepsis suspected
- **Blood cultures x 2:** Before antibiotics for all admitted patients; yield 5-14% in CAP, higher in severe disease
- **Sputum culture and Gram stain:** If productive cough; obtain before antibiotics when feasible. Most useful for inpatient/ICU patients.
- **Procalcitonin:** > 0.25 mcg/L supports bacterial etiology; useful for antibiotic stewardship and de-escalation. Do NOT withhold antibiotics based on low procalcitonin in clinically apparent pneumonia.
- **Urinary antigens:** Legionella (inpatient/ICU), pneumococcal (ICU) — order for severe CAP
- **Respiratory viral panel:** Influenza and COVID-19 testing when seasonally appropriate; guides antiviral therapy and isolation
- **ABG/VBG:** If respiratory distress, SpO2 < 92%, or COPD (assess for hypercapnia)
- **CT chest:** Parapneumonic effusion, empyema, lung abscess, necrotizing pneumonia, or diagnostic uncertainty
- **Point-of-care ultrasound:** Lung consolidation (tissue-like sign, air bronchograms), pleural effusion, B-lines

## Treatment

### Outpatient CAP (CURB-65 0-1, no comorbidities)
- **Amoxicillin 1 g PO TID x 5 days** (preferred)
- OR **Doxycycline 100 mg PO BID x 5 days**
- OR **Azithromycin 500 mg PO day 1, then 250 mg PO daily x 4 days** (only if local pneumococcal macrolide resistance < 25%)

### Outpatient CAP (with comorbidities: COPD, diabetes, chronic heart/liver/renal disease, alcoholism, malignancy, asplenia)
- **Amoxicillin-clavulanate 875/125 mg PO BID** OR **cefpodoxime 200 mg PO BID** PLUS **azithromycin 500 mg PO day 1, then 250 mg daily** OR **doxycycline 100 mg PO BID**
- OR monotherapy with **respiratory fluoroquinolone: levofloxacin 750 mg PO daily x 5 days** OR **moxifloxacin 400 mg PO daily x 5 days**

### Inpatient CAP (non-ICU)
- **Ceftriaxone 1-2 g IV daily PLUS azithromycin 500 mg IV daily**
- OR monotherapy with **respiratory fluoroquinolone: levofloxacin 750 mg IV daily** OR **moxifloxacin 400 mg IV daily**
- If beta-lactam allergy: respiratory fluoroquinolone monotherapy

### Inpatient CAP (ICU, no Pseudomonas/MRSA risk)
- **Ceftriaxone 2 g IV daily PLUS azithromycin 500 mg IV daily**
- OR **ceftriaxone 2 g IV daily PLUS levofloxacin 750 mg IV daily**
- If beta-lactam allergy: **levofloxacin 750 mg IV daily PLUS aztreonam 2 g IV q8h**

### Inpatient CAP (ICU, with MRSA risk factors)
Add: **vancomycin 25-30 mg/kg IV loading dose, then 15-20 mg/kg IV q8-12h** OR **linezolid 600 mg IV q12h**
- MRSA risk factors: prior MRSA infection/colonization, recent hospitalization with parenteral antibiotics, cavitary/necrotizing infiltrate

### Inpatient CAP (ICU, with Pseudomonas risk factors)
Replace ceftriaxone with: **piperacillin-tazobactam 4.5 g IV q6h** OR **cefepime 2 g IV q8h** OR **meropenem 1 g IV q8h**
- Pseudomonas risk factors: structural lung disease (bronchiectasis, CF), prior Pseudomonas isolation, recent hospitalization with parenteral antibiotics

### Hospital-Acquired Pneumonia (HAP)
- **Piperacillin-tazobactam 4.5 g IV q6h** OR **cefepime 2 g IV q8h** OR **meropenem 1 g IV q8h**
- ADD **vancomycin 25-30 mg/kg IV loading, then 15-20 mg/kg q8-12h** OR **linezolid 600 mg IV q12h** if MRSA risk or local MRSA prevalence > 20%
- Narrow based on culture and sensitivity data

### Aspiration Pneumonia
- **Ampicillin-sulbactam 3 g IV q6h** (covers anaerobes)
- OR **ceftriaxone 2 g IV daily PLUS metronidazole 500 mg IV q8h**
- OR **piperacillin-tazobactam 4.5 g IV q6h** if HAP risk factors
- Do NOT treat aspiration pneumonitis (chemical inflammation without infection) with antibiotics — observe and reassess at 48 hours

### Adjunctive Treatment
- **Supplemental oxygen:** Titrate to SpO2 >= 94% (>= 88-92% in COPD to avoid CO2 retention)
- **IV fluids:** If dehydrated or septic; balanced crystalloid preferred
- **Non-invasive ventilation (BiPAP):** For hypoxemic respiratory failure with intact airway and mental status; reduces intubation rates in immunocompromised patients
- **Intubation:** Refractory hypoxia (SpO2 < 88% on high-flow), respiratory fatigue (rising pCO2), inability to protect airway, hemodynamic instability
- **Corticosteroids:** Dexamethasone 6 mg IV daily x 4 days for severe CAP requiring ICU has mortality benefit (CAPE COD trial). Use for COVID-19 pneumonia requiring supplemental oxygen.
- **Oseltamivir 75 mg PO BID x 5 days:** If influenza confirmed or suspected (start within 48 hours of symptom onset, but benefit even if started later in hospitalized patients)

### Sepsis Management
- If sepsis criteria met: follow sepsis protocol — antibiotics within 1 hour, lactate, blood cultures, 30 mL/kg crystalloid for hypotension or lactate >= 4 mmol/L, vasopressors if MAP < 65 after fluids

## Disposition

| Severity | Disposition |
|---|---|
| CURB-65 0-1, PSI I-II, stable | Outpatient with 48-hour follow-up |
| CURB-65 2, PSI III | Short observation or admit; clinical judgment |
| CURB-65 3-5, PSI IV-V | Inpatient admission |
| Any ATS/IDSA major criterion | ICU |
| >= 3 ATS/IDSA minor criteria | ICU |
| Hypoxia requiring > 4 L/min O2 | Inpatient, evaluate for step-down or ICU |
| Failed outpatient therapy | Admit for IV antibiotics and workup |

### Discharge Criteria for Outpatient Management
- Able to tolerate oral medications
- Stable vital signs (HR < 100, RR < 24, SBP > 90, temp < 38C, SpO2 > 90% on room air)
- Baseline mental status
- Reliable follow-up in 48-72 hours
- No significant comorbidities requiring monitoring

### Inpatient Switch to Oral
- Transition IV to oral antibiotics when: temperature < 38C x 24 hours, HR < 100, RR < 24, SpO2 > 90% on RA, tolerating PO, normal mental status

## Pitfalls

1. **Discharging elderly patients with pneumonia based solely on CURB-65 = 1.** Elderly patients with baseline comorbidities may deteriorate rapidly. Integrate clinical judgment, functional status, and social support into disposition decisions.

2. **Missing sepsis in pneumonia patients.** Screen every pneumonia patient for sepsis. Tachycardia, hypotension, altered mental status, or lactate >= 2 mmol/L requires aggressive resuscitation and antibiotics within 1 hour.

3. **Relying on a normal CXR to exclude pneumonia.** Chest X-ray sensitivity for pneumonia is 60-75%. Early disease, dehydration, and neutropenia reduce sensitivity. If clinical suspicion is high and CXR is negative, obtain CT chest or treat empirically and repeat imaging in 24-48 hours.

4. **Treating aspiration pneumonitis with antibiotics.** Witnessed aspiration with chemical pneumonitis (fever, infiltrate within hours) does not require antibiotics unless the patient fails to improve at 48 hours or develops new fever/infiltrate suggesting superinfection.

5. **Using azithromycin monotherapy for inpatient CAP.** Macrolide monotherapy is inadequate for inpatient pneumonia. Always pair with a beta-lactam (ceftriaxone) or use a respiratory fluoroquinolone for inpatient treatment.

6. **Not covering for MRSA in severe necrotizing or cavitary pneumonia.** Cavitary infiltrates, rapidly progressive disease, or concurrent influenza should prompt addition of vancomycin or linezolid for MRSA coverage.

7. **Forgetting to test for influenza and COVID-19 during respiratory illness season.** Specific antiviral therapy (oseltamivir, nirmatrelvir-ritonavir) changes management. Isolation prevents nosocomial transmission.

8. **Not obtaining Legionella urinary antigen in severe CAP.** Legionella causes 2-15% of CAP requiring ICU admission. Urinary antigen detects serogroup 1 (70-80% of disease). Directs targeted therapy with fluoroquinolone or azithromycin.

9. **Delaying intubation in a tiring patient with pneumonia.** Rising respiratory rate, accessory muscle use, inability to speak full sentences, and rising pCO2 indicate impending respiratory arrest. Early intubation is safer than crash intubation.

10. **Prescribing fluoroquinolones as first-line for healthy outpatients.** ATS/IDSA guidelines reserve respiratory fluoroquinolones for patients with comorbidities or prior antibiotic use. Amoxicillin or doxycycline is first-line for healthy adults to minimize resistance selection and adverse effects (tendinopathy, C. difficile, aortic dissection risk).
