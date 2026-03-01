---
id: influenza-pneumonia-severe
condition: Severe Influenza Pneumonia
aliases: [influenza pneumonia, flu pneumonia, influenza ARDS, viral influenza pneumonia, H1N1 pneumonia]
icd10: [J09.X1, J10.00, J10.01, J11.00, J11.08]
esi: 1
time_to_harm:
  irreversible_injury: "< 12 hours"
  death: "< 48 hours"
  optimal_intervention_window: "< 48 hours for antivirals"
category: respiratory
track: tier1
sources:
  - type: guideline
    ref: "2019 IDSA Clinical Practice Guidelines for the Diagnosis and Treatment of Seasonal Influenza in Adults and Children. Clin Infect Dis. 2019;68(6):e1-e47."
  - type: guideline
    ref: "2024 CDC Clinical Guidance for Influenza Treatment. CDC.gov."
  - type: review
    ref: "Kalil AC, Thomas PG. Influenza Virus-Related Critical Illness: Pathophysiology and Epidemiology. Crit Care. 2019;23(1):258."
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
# Severe Influenza Pneumonia

## Recognition

**Presentation:**
- Abrupt onset fever (often > 39°C), myalgia, headache, malaise
- Cough (initially dry, may become productive), dyspnea, pleuritic chest pain
- Tachypnea, hypoxemia (SpO2 < 94%), bilateral infiltrates
- Progression to ARDS (influenza is a leading viral cause of ARDS)
- GI symptoms (nausea, vomiting, diarrhea) in up to 25%

**Patterns of pneumonia:**
- Primary viral pneumonia: bilateral diffuse infiltrates, onset within 48 hours of flu symptoms
- Secondary bacterial pneumonia: improvement then deterioration ("double sickening") at 5-7 days; focal consolidation. S. pneumoniae, S. aureus (including MRSA), H. influenzae.
- Combined viral-bacterial pneumonia

**High-risk groups:**
- Age > 65 or < 2 years
- Pregnancy and 2 weeks postpartum
- Chronic lung disease (COPD, asthma), cardiovascular disease, diabetes, renal disease
- Immunosuppression (HIV, transplant, chemotherapy)
- Morbid obesity (BMI >= 40)
- Nursing home residents

## Critical Actions

| Action | Target |
|---|---|
| Influenza testing | < 30 minutes |
| Oseltamivir initiation | < 1 hour |
| Supplemental O2 | Immediate |
| Blood cultures (if bacterial superinfection suspected) | Before antibiotics |

1. **Oseltamivir 75 mg PO BID x 5 days** — start immediately upon clinical suspicion; do NOT wait for test results. Benefit greatest within 48 hours of symptom onset but still recommended after 48 hours in severe disease.
2. **Supplemental O2** — titrate to SpO2 92-96%; escalate to HFNC → NIV → intubation as needed
3. **Rapid influenza diagnostic test or PCR** — PCR preferred (sensitivity > 95% vs ~60% for rapid antigen)
4. **Add empiric antibiotics** if bacterial superinfection suspected: ceftriaxone 2 g IV q24h + azithromycin 500 mg IV q24h (or add vancomycin 15-20 mg/kg IV if MRSA risk factors)
5. **Respiratory isolation** — droplet precautions; airborne for aerosol-generating procedures
6. **IV fluids** cautiously — avoid volume overload in pneumonia/ARDS
7. **Corticosteroids:** NOT routinely recommended for influenza pneumonia (unlike COVID). Consider only if concurrent ARDS meeting Berlin criteria and after 24-48 hours of supportive care.

## Differential Diagnosis

- **COVID-19 pneumonia** — bilateral GGO, lymphopenia; PCR differentiates
- **Community-acquired pneumonia (bacterial)** — focal consolidation, productive sputum, elevated procalcitonin
- **RSV/parainfluenza pneumonia** — similar presentation; viral panel differentiates
- **PJP** — immunocompromised, bilateral GGO, elevated LDH
- **Acute eosinophilic pneumonia** — eosinophilia, rapid steroid response
- **Pulmonary embolism** — pleuritic pain, elevated D-dimer; CTA diagnostic

## Workup

- **Influenza PCR (nasopharyngeal):** Gold standard. Rapid antigen has ~60% sensitivity (false negatives common).
- **Respiratory viral panel:** Rule out other viral etiologies
- **CXR:** Bilateral interstitial/alveolar infiltrates (primary viral) or focal consolidation (bacterial superinfection)
- **CT chest:** If CXR non-diagnostic — bilateral GGO, consolidation
- **Labs:** CBC (lymphopenia, leukocytosis if bacterial), BMP, LDH (elevated in severe), CRP, procalcitonin (> 0.5 suggests bacterial co-infection), lactate
- **ABG:** P/F ratio for ARDS assessment
- **Blood cultures:** If bacterial superinfection suspected
- **Sputum culture:** Gram stain + culture (S. aureus, S. pneumoniae)

## Treatment

### Antiviral Therapy
- Oseltamivir 75 mg PO BID x 5 days (standard); extend to 10 days in severe/immunocompromised
- Double-dose oseltamivir (150 mg PO BID) considered in ICU patients (limited evidence)
- Peramivir 600 mg IV single dose — alternative if unable to take PO
- Baloxavir 40-80 mg PO single dose (weight-based) — alternative for uncomplicated; limited data in severe disease

### Bacterial Superinfection
- Ceftriaxone 2 g IV q24h + azithromycin 500 mg IV q24h (standard CAP coverage)
- Add vancomycin 15-20 mg/kg IV q8-12h if MRSA suspected (cavitary lesion, post-influenza S. aureus, severe disease)
- De-escalate when cultures result

### Respiratory Support
- Escalation: NC → HFNC → NIV → Intubation with lung-protective ventilation
- ARDS management per standard protocol (TV 6 mL/kg IBW, PEEP per table, prone >= 16 hrs if P/F < 150)
- VV-ECMO for refractory cases

### Supportive
- Antipyretics: acetaminophen 1000 mg PO/IV q6h (avoid aspirin in children/adolescents — Reye syndrome)
- IV fluid resuscitation cautiously
- DVT prophylaxis: enoxaparin 40 mg SC daily

## Disposition

- **ICU admission:** SpO2 < 90% despite supplemental O2, requiring HFNC/NIV/intubation, hemodynamic instability, multiorgan dysfunction
- **Inpatient admission:** Hypoxemia requiring supplemental O2, bilateral infiltrates, high-risk comorbidities, inability to tolerate PO
- **Discharge:** Low-risk patients with improving symptoms, SpO2 > 94% on room air, able to take oral oseltamivir, reliable follow-up
- **Respiratory isolation:** Until afebrile x 24 hours or per institutional policy

## Pitfalls

1. **Withholding oseltamivir because > 48 hours from symptom onset.** While oseltamivir is most effective within 48 hours, it still reduces mortality and duration of ICU stay when given later in severe/hospitalized influenza. All hospitalized patients should receive oseltamivir regardless of symptom duration.

2. **Relying on rapid antigen test to exclude influenza.** Rapid influenza diagnostic tests have sensitivity of only ~60%. A negative rapid test in a patient with classic influenza presentation should prompt PCR testing. Do not withhold empiric oseltamivir pending PCR results.

3. **Missing bacterial superinfection during influenza.** The "double sickening" pattern (initial improvement at days 3-5 followed by worsening with new fever, productive sputum, and focal consolidation) indicates bacterial superinfection. S. aureus (including MRSA) superinfection carries high mortality. Add antibiotics promptly if suspected.

4. **Routine corticosteroid use for influenza pneumonia.** Unlike COVID-19, corticosteroids have NOT been shown to improve outcomes in influenza pneumonia and may increase bacterial superinfection risk and prolong viral shedding. Use only if meeting ARDS criteria with refractory hypoxemia.

5. **Forgetting to administer oseltamivir to the correct population.** All hospitalized influenza patients, high-risk outpatients, and household contacts of immunocompromised patients should receive antivirals. This is frequently missed in elderly patients with atypical presentations.
