---
id: ventilator-associated-pneumonia
condition: Ventilator-Associated Pneumonia
aliases: [VAP, ventilator pneumonia, nosocomial pneumonia ventilated, ICU-acquired pneumonia]
icd10: [J95.851]
esi: 2
time_to_harm: "< 24 hours (if untreated sepsis develops)"
category: respiratory
track: tier1
sources:
  - type: guideline
    ref: "2016 IDSA/ATS Clinical Practice Guidelines for Management of Adults With Hospital-Acquired and Ventilator-Associated Pneumonia. Clin Infect Dis. 2016;63(5):e61-e111."
  - type: guideline
    ref: "2017 ERS/ESICM/ESCMID/ALAT Guidelines for the Management of Hospital-Acquired and Ventilator-Associated Pneumonia. Eur Respir J. 2017;50(3):1700582."
  - type: review
    ref: "Kalil AC, et al. Management of Adults With Hospital-Acquired and Ventilator-Associated Pneumonia: 2016 Clinical Practice Guidelines by the IDSA and the ATS. Clin Infect Dis. 2016;63(5):e61-e111."
last_updated: "2026-03-01"
compiled_by: agent
risk_tier: B
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
# Ventilator-Associated Pneumonia

## Recognition

**Definition:**
- Pneumonia occurring >= 48 hours after endotracheal intubation
- New or progressive radiographic infiltrate PLUS clinical evidence of infection

**Clinical criteria (>= 2 of the following + new infiltrate):**
- Temperature > 38°C or < 36°C
- WBC > 12,000/mm3 or < 4,000/mm3
- Purulent tracheal secretions (new onset or change in character)
- Worsening oxygenation (P/F ratio decline, increased FiO2/PEEP requirement)

**Clinical Pulmonary Infection Score (CPIS):**
- Temperature, WBC, tracheal secretions, oxygenation, radiographic infiltrate, tracheal aspirate culture
- Score >= 6 suggests VAP (sensitivity ~65%, specificity ~65% — imperfect but useful adjunct)

**Microbiology:**
- **Early-onset (< 5 days of MV):** S. pneumoniae, H. influenzae, MSSA, Enterobacteriaceae (less resistant)
- **Late-onset (>= 5 days of MV):** Pseudomonas aeruginosa, MRSA, Acinetobacter, ESBL-producing Enterobacteriaceae, Stenotrophomonas
- Risk factors for MDR organisms: IV antibiotics within prior 90 days, septic shock at time of VAP, ARDS preceding VAP, >= 5 days hospitalization before VAP, acute RRT before VAP

**Pathogenesis:**
- Aspiration of contaminated oropharyngeal secretions around the ETT cuff
- Biofilm formation on endotracheal tube
- Impaired mucociliary clearance
- Altered host defenses from critical illness

## Critical Actions

| Action | Target |
|---|---|
| Obtain lower respiratory tract cultures | Before antibiotics |
| Empiric antibiotics | < 1 hour |
| De-escalation when cultures return | 48-72 hours |

1. **Obtain lower respiratory tract cultures BEFORE antibiotics** (if feasible without delaying treatment in unstable patients):
   - Quantitative endotracheal aspirate (ETA): >= 10^6 CFU/mL = positive
   - Bronchoalveolar lavage (BAL): >= 10^4 CFU/mL = positive
   - Protected specimen brush (PSB): >= 10^3 CFU/mL = positive
2. **Blood cultures x 2** before antibiotics
3. **Start empiric broad-spectrum antibiotics immediately** — delay in appropriate antibiotics increases mortality
4. **De-escalate** at 48-72 hours when culture data and sensitivities available
5. **Daily assessment of extubation readiness** — shortest duration of mechanical ventilation reduces VAP risk
6. **Procalcitonin-guided discontinuation** — consider stopping antibiotics when procalcitonin < 0.25 or > 80% decline from peak (adjunctive, not definitive)

## Differential Diagnosis

- **ARDS** — bilateral infiltrates, P/F < 300; can coexist with VAP. Distinguish by purulent secretions, fever pattern, culture data.
- **Atelectasis** — lobar collapse without infection; bronchoscopic suctioning may resolve
- **Pulmonary edema** — bilateral, responds to diuresis; elevated BNP
- **Pulmonary embolism** — new hypoxemia without new infiltrate; CTA diagnostic
- **Tracheobronchitis** — purulent secretions without new infiltrate; may not require antibiotics (controversial)
- **Drug fever** — temporal relationship with new medication; diagnosis of exclusion
- **Aspiration pneumonitis** — after witnessed aspiration event; may not need antibiotics initially

## Workup

- **CXR (portable):** New or progressive infiltrate, consolidation, air bronchograms. Serial comparison essential.
- **Lower respiratory tract culture:** Quantitative ETA (easiest) or BAL (most specific). Semi-quantitative cultures are acceptable.
- **Blood cultures x 2:** Before antibiotics. Positive in ~15% of VAP.
- **Labs:** CBC with differential (leukocytosis or leukopenia), procalcitonin (serial for antibiotic stewardship), BMP, lactate, ABG
- **CPIS score:** Aids in diagnosis when clinical picture unclear
- **CT chest:** If CXR non-diagnostic or complication suspected (abscess, empyema)
- **Bronchoscopy with BAL:** Preferred for quantitative cultures; also useful if concern for alternative diagnosis (DAH, eosinophilic pneumonia)

## Treatment

### Empiric Therapy — Early-Onset, No MDR Risk Factors
- Ceftriaxone 2 g IV q24h OR ampicillin-sulbactam 3 g IV q6h OR levofloxacin 750 mg IV q24h
- Duration: 7 days (short course non-inferior to longer courses per 2016 IDSA/ATS)

### Empiric Therapy — Late-Onset OR MDR Risk Factors
Two drugs for gram-negative coverage PLUS MRSA coverage:
- **Gram-negative (choose 1):**
  - Piperacillin-tazobactam 4.5 g IV q6h (extended infusion 4 hours)
  - Cefepime 2 g IV q8h
  - Meropenem 1 g IV q8h (for ESBL or high resistance concern)
  - PLUS one anti-pseudomonal from a different class: ciprofloxacin 400 mg IV q8h OR tobramycin 5-7 mg/kg IV daily OR colistin (for XDR organisms)
- **MRSA coverage:**
  - Vancomycin 15-20 mg/kg IV q8-12h (target trough 15-20 mcg/mL) OR
  - Linezolid 600 mg IV q12h (better lung penetration for MRSA pneumonia; ZEVTERA trial: non-inferior to vancomycin)
- Duration: 7 days (may extend for non-fermenting gram-negatives like Pseudomonas based on clinical response)

### De-Escalation Strategy
- Narrow spectrum at 48-72 hours based on culture and sensitivity data
- Discontinue MRSA coverage if cultures negative for MRSA
- Discontinue double gram-negative coverage if susceptible organism identified
- Procalcitonin < 0.25 or > 80% decline from peak supports antibiotic discontinuation

### VAP Prevention Bundle
- HOB elevation 30-45 degrees
- Daily sedation interruption and spontaneous breathing trial
- Oral hygiene with chlorhexidine 0.12% (q12h)
- Subglottic secretion drainage (silver-coated or subglottic suction ETT)
- Minimize duration of mechanical ventilation — daily extubation readiness assessment
- DVT and peptic ulcer prophylaxis
- Avoid unnecessary reintubation

## Disposition

- **ICU (already):** All VAP patients are in the ICU by definition. Continue ICU-level care.
- **Step-down:** After clinical improvement (afebrile, WBC normalizing, FiO2 weaning, extubated)
- **ID consultation:** MDR organisms, treatment failure, unusual pathogens
- **Outcomes:** VAP mortality 13-50% (attributable mortality ~10-15%); prolonged ICU stay by 4-8 days

## Pitfalls

1. **Delaying antibiotics while awaiting culture results.** In VAP, each hour of delay in appropriate antibiotics is associated with increased mortality. Obtain cultures, then start broad empiric therapy immediately. De-escalate when results return.

2. **Not de-escalating antibiotics when culture data is available.** Prolonged broad-spectrum therapy promotes MDR organisms, C. difficile, and fungal infections. When the causative organism is identified, narrow therapy to the most targeted effective agent.

3. **Treating tracheal colonization as VAP.** Positive tracheal cultures alone (without clinical signs of pneumonia) represent colonization, not infection. Quantitative cultures and clinical context (fever, WBC, infiltrate, oxygenation change) are needed to diagnose VAP.

4. **Using CXR alone to diagnose or exclude VAP.** Portable CXR in ICU has poor sensitivity and specificity for VAP. New infiltrates can represent atelectasis, ARDS, or edema. Clinical correlation with fever, secretions, WBC, and cultures is essential.

5. **Prescribing antibiotics for > 7 days without specific indication.** The 2016 IDSA/ATS guidelines recommend 7-day courses for most VAP. Longer courses (10-14 days) are reserved for non-lactose-fermenting gram-negatives (Pseudomonas, Acinetobacter) or patients with delayed clinical response. Unnecessary prolongation increases resistance.
