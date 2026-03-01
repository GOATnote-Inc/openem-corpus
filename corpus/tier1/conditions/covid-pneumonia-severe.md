---
id: covid-pneumonia-severe
condition: Severe COVID-19 Pneumonia
aliases: [COVID pneumonia, SARS-CoV-2 pneumonia, COVID ARDS, severe COVID-19, coronavirus pneumonia]
icd10: [J12.82, U07.1]
esi: 1
time_to_harm:
  irreversible_injury: "< 12 hours"
  death: "< 48 hours"
  optimal_intervention_window: "< 6 hours"
category: respiratory
track: tier1
sources:
  - type: guideline
    ref: "NIH COVID-19 Treatment Guidelines Panel. Therapeutic Management of Hospitalized Adults With COVID-19. Updated 2024."
  - type: guideline
    ref: "IDSA Guidelines on the Treatment and Management of Patients with COVID-19. Updated 2024."
  - type: review
    ref: "RECOVERY Collaborative Group. Dexamethasone in Hospitalized Patients with COVID-19. N Engl J Med. 2021;384(8):693-704."
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
# Severe COVID-19 Pneumonia

## Recognition

**Severity classification:**
- **Severe:** SpO2 < 94% on room air, RR > 30, PaO2/FiO2 < 300, or lung infiltrates > 50%
- **Critical:** Respiratory failure requiring mechanical ventilation, shock, or multiorgan dysfunction

**Presentation:**
- Dyspnea (typically onset day 5-10 of illness — post-viral inflammatory phase)
- Hypoxemia — often "silent hypoxia" (SpO2 in low 80s with minimal symptoms initially)
- Bilateral ground-glass opacities on CT (peripheral, lower lobe predominant)
- Fever, cough, fatigue, myalgia preceding respiratory decompensation
- Lymphopenia, elevated CRP, ferritin, D-dimer, LDH

**High-risk features for progression:**
- Age > 65, obesity (BMI > 30), diabetes, cardiovascular disease, chronic lung disease
- Immunosuppression (transplant, chemotherapy, HIV with CD4 < 200)
- Unvaccinated status
- Rapidly rising CRP, ferritin > 500, D-dimer > 2x ULN, lymphocyte count < 800

**Phenotypes:**
- Type L (early): low elastance, low V/Q mismatch, low lung weight — responds to supplemental O2 and prone
- Type H (late): high elastance, high shunt, high lung weight — classic ARDS pattern requiring mechanical ventilation

## Critical Actions

| Action | Target |
|---|---|
| SpO2 assessment | Immediate |
| Dexamethasone initiation | < 1 hour |
| Supplemental O2 or HFNC | Immediate |
| Prone positioning (awake or intubated) | Within 2 hours |

1. **Supplemental O2** to target SpO2 92-96%: nasal cannula → HFNC (40-60 L/min) → BiPAP → intubation as needed
2. **Dexamethasone 6 mg IV/PO daily x 10 days** — proven mortality benefit in patients requiring O2 (RECOVERY trial: NNT 25 for supplemental O2, NNT 8 for mechanical ventilation)
3. **Awake prone positioning** — for patients on HFNC/NIV; >= 8 hours/day if tolerated (improves oxygenation, may reduce intubation)
4. **Remdesivir 200 mg IV day 1, then 100 mg IV daily x 5 days** — started within 10 days of symptom onset; reduces time to recovery
5. **Anticoagulation:** Prophylactic enoxaparin 40 mg SC daily (standard); consider therapeutic enoxaparin 1 mg/kg SC q12h for non-critically-ill hospitalized patients with elevated D-dimer (per ACTIV-4a/ATTACC trials)
6. **Tocilizumab 8 mg/kg IV (max 800 mg) single dose** — within 24 hours of ICU admission for patients with rapidly progressive respiratory failure and elevated CRP (> 75 mg/L). Reduces mortality when added to dexamethasone.
7. **Baricitinib 4 mg PO daily x 14 days** — alternative to tocilizumab (JAK inhibitor); COV-BARRIER trial showed mortality benefit in severe COVID
8. **If intubated:** Lung-protective ventilation per ARDS protocol (TV 6 mL/kg IBW, Pplat < 30, prone >= 16 hrs/day for P/F < 150)

## Differential Diagnosis

- **Influenza pneumonia** — similar presentation; rapid flu antigen or PCR differentiates
- **Bacterial pneumonia** — focal consolidation, productive sputum, elevated procalcitonin > 0.5
- **PJP (Pneumocystis)** — HIV/immunocompromised, bilateral GGO, elevated LDH, beta-glucan positive
- **Acute eosinophilic pneumonia** — peripheral eosinophilia, steroid-responsive
- **Organizing pneumonia** — subacute, migratory infiltrates
- **Pulmonary embolism** — COVID increases VTE risk 3-5x; low threshold for CTA

## Workup

- **SARS-CoV-2 PCR (nasopharyngeal):** Confirm diagnosis
- **CT chest:** Bilateral peripheral GGO, consolidation, crazy-paving pattern. Typical COVID CT pattern is highly characteristic.
- **Labs:** CBC (lymphopenia), CRP, ferritin, D-dimer, LDH, BMP, LFTs, troponin, procalcitonin (to evaluate for bacterial co-infection)
- **ABG:** Assess oxygenation, calculate P/F ratio
- **Blood cultures:** If concern for bacterial co-infection (procalcitonin > 0.5)
- **IL-6:** If considering tocilizumab (elevated supports use)
- **Echocardiography:** If hemodynamically unstable — assess for RV strain (PE), myocarditis
- **Point-of-care US:** B-lines (bilateral diffuse), subpleural consolidations, pleural irregularity

## Treatment

### Oxygenation Strategy (Escalation Ladder)
1. Nasal cannula 1-6 L/min → target SpO2 92-96%
2. HFNC 30-60 L/min, FiO2 titrated + awake prone positioning
3. NIV (BiPAP IPAP 10-16, EPAP 6-10) — with caution (may delay intubation in some patients)
4. Intubation for worsening despite NIV (P/F < 150, encephalopathy, hemodynamic instability)
5. Lung-protective MV: TV 6 mL/kg IBW, Pplat < 30, PEEP per ARDSNet table
6. Prone ventilation >= 16 hrs/day for P/F < 150
7. VV-ECMO for refractory hypoxemia (P/F < 80 despite optimal ventilation + proning)

### Pharmacologic
- Dexamethasone 6 mg IV/PO daily x 10 days (all patients requiring supplemental O2)
- Remdesivir 200 mg IV day 1, then 100 mg IV daily x 4 days (within 10 days symptom onset)
- Tocilizumab 8 mg/kg IV x 1 (with dexamethasone, for rapidly progressive disease + CRP > 75)
- Baricitinib 4 mg PO daily x 14 days (alternative to tocilizumab)
- Prophylactic anticoagulation: enoxaparin 40 mg SC daily (all hospitalized patients)

### Avoid
- Hydroxychloroquine (no benefit, potential harm)
- Ivermectin (no proven benefit for COVID)
- Routine broad-spectrum antibiotics (bacterial co-infection only ~8% of COVID admissions; use procalcitonin to guide)

## Disposition

- **ICU admission:** Requiring HFNC > 50 L/min, BiPAP/CPAP, intubation, vasopressors, organ failure
- **Stepdown/telemetry:** Supplemental O2 2-6 L/min, stable, receiving dexamethasone and remdesivir
- **Transfer criteria:** Facilities without ICU ventilator capability or ECMO for deteriorating patients
- **Discharge criteria:** Off supplemental O2 for >= 24 hours, able to ambulate, temperature < 38°C for 24 hours, reliable follow-up

## Pitfalls

1. **Missing "silent hypoxia" — patients with SpO2 in the 70s-80s who appear comfortable.** COVID causes a V/Q mismatch phenotype where patients can have profound hypoxemia without proportional dyspnea. Always check SpO2 — do not rely on clinical appearance alone.

2. **Withholding dexamethasone from patients requiring supplemental O2.** Dexamethasone reduces 28-day mortality in patients requiring O2 (NNT 25) and mechanical ventilation (NNT 8). Conversely, do NOT give dexamethasone to patients NOT requiring O2 — it showed a trend toward harm in this subgroup.

3. **Delayed intubation while exhausting noninvasive strategies.** Prolonged high-effort breathing on HFNC/NIV can cause patient self-inflicted lung injury (P-SILI). If a patient on HFNC has P/F < 150, RR > 30, and ROX index < 4.88 at 12 hours, intubation should not be delayed further.

4. **Not anticoagulating hospitalized COVID patients.** COVID is a prothrombotic state. VTE occurs in up to 20-30% of ICU COVID patients. At minimum, prophylactic anticoagulation should be started on admission unless contraindicated.

5. **Prescribing broad-spectrum antibiotics reflexively.** Bacterial co-infection is uncommon (~8%) at presentation. Procalcitonin < 0.25 makes bacterial co-infection unlikely. Reserve antibiotics for patients with clinical features of superimposed bacterial pneumonia (productive sputum, focal consolidation, elevated procalcitonin).
