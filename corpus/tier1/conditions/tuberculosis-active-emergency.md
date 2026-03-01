---
id: tuberculosis-active-emergency
condition: Active Pulmonary Tuberculosis — Emergency Management
aliases: [active TB, pulmonary TB, Mycobacterium tuberculosis, TB emergency]
icd10: [A15.0, A15.5, A15.6, A15.9]
esi: 2
time_to_harm: "Hours (hemoptysis, respiratory failure); transmission risk immediate"
category: infectious
track: tier1
sources:
  - type: guideline
    ref: "CDC Clinical Guidelines for Tuberculosis, 2024"
  - type: guideline
    ref: "ATS/CDC/IDSA Clinical Practice Guidelines: Treatment of Drug-Susceptible Tuberculosis, 2016"
  - type: guideline
    ref: "NTCA/IDSA Guidelines for Respiratory Isolation and Restrictions to Reduce Transmission of Pulmonary TB, 2024"
  - type: guideline
    ref: "WHO Consolidated Guidelines on Tuberculosis, Module 4: Treatment, 2022"
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
# Active Pulmonary Tuberculosis — Emergency Management

## Recognition

**Classic presentation:**
- Chronic cough (> 2-3 weeks), often productive with hemoptysis
- Night sweats, fever, weight loss, anorexia
- Fatigue, malaise

**ED presentations (acute):**
- Massive hemoptysis
- Respiratory failure
- Miliary TB with multi-organ involvement (meningitis, pericarditis, hepatitis)
- Pleural effusion with respiratory distress
- Spine involvement with neurologic deficits (Pott disease)

**Exam findings:**
- Upper lobe crackles, bronchial breath sounds
- Cachexia, wasting
- Lymphadenopathy (cervical, supraclavicular)
- Dullness to percussion if effusion present

**High-risk populations:**
- Born in or travel to high-burden countries
- HIV/AIDS (CD4 < 200 — atypical presentations)
- Incarcerated or recently released
- Homeless or shelter-residing
- Close contacts of known TB cases
- Immunosuppression (TNF-alpha inhibitors, transplant)

## Critical Actions

1. **Airborne isolation IMMEDIATELY** upon suspicion — place patient in negative-pressure room with door closed; N95 respirator for all staff
2. **Place surgical mask on patient** during transport
3. **Collect 3 sputum specimens** for AFB smear and mycobacterial culture (ideally 8-24h apart; at minimum 1 hour apart)
4. **Order GeneXpert MTB/RIF** (rapid molecular test) — results in 2 hours, detects rifampin resistance
5. **CXR** — upper lobe infiltrates, cavitation (immunocompetent); atypical patterns (immunocompromised)
6. **Do NOT initiate standard TB therapy in the ED** unless prolonged stay anticipated — treatment initiation is coordinated with public health and infectious disease
7. **For life-threatening presentations:** Start empiric RIPE therapy and consult infectious disease

## Differential Diagnosis

- Community-acquired pneumonia — acute onset, lower lobe predominance
- Lung malignancy — mass lesion, no cavitation, smoker, no fever pattern
- Non-tuberculous mycobacterial infection — similar imaging, different cultures
- Lung abscess — air-fluid level, polymicrobial, fetor
- Sarcoidosis — bilateral hilar lymphadenopathy, non-caseating granulomas
- Fungal infection (histoplasmosis, coccidioidomycosis) — geographic exposure history
- Pulmonary vasculitis (Wegener/GPA) — hemoptysis, renal involvement, ANCA positive

## Workup

- **Sputum AFB smear and culture** — 3 specimens; culture is gold standard (positive in 2-6 weeks)
- **GeneXpert MTB/RIF** — PCR-based; 2-hour turnaround; detects rifampin resistance (sensitivity ~99% for smear-positive, ~70% for smear-negative)
- **CXR PA and lateral:**
  - Classic: upper lobe infiltrate, cavitation, fibrosis
  - HIV/immunosuppressed: lower lobe, miliary pattern, hilar lymphadenopathy, normal CXR possible
- **CT chest** if CXR ambiguous or miliary pattern suspected
- **HIV test** — all patients with suspected TB (CDC recommendation)
- **CBC, BMP, hepatic panel** (baseline before treatment)
- **Blood cultures for mycobacteria** if miliary or disseminated disease suspected
- **LP with AFB smear/culture and TB PCR** if meningeal symptoms
- **Interferon-gamma release assay (IGRA) or TST** — useful for latent TB screening, NOT diagnostic of active disease

## Treatment

### Standard RIPE Therapy (Initiate with ID Consultation)
- **Rifampin 10 mg/kg PO daily (max 600 mg)** — 6 months
- **Isoniazid 5 mg/kg PO daily (max 300 mg)** — 6 months, with pyridoxine (vitamin B6) 25-50 mg PO daily to prevent neuropathy
- **Pyrazinamide 25 mg/kg PO daily (max 2 g)** — first 2 months only
- **Ethambutol 15-20 mg/kg PO daily (max 1.6 g)** — first 2 months (until drug susceptibility results available)

### ED-Specific Management
- **Massive hemoptysis:** Airway management, position with bleeding lung dependent, IR consultation for bronchial artery embolization
- **Respiratory failure:** Intubation with HEPA filter on circuit; airborne precautions for all aerosol-generating procedures
- **TB meningitis:** Dexamethasone 0.4 mg/kg/day IV, tapering over 6-8 weeks (reduces mortality)

### Drug-Resistant TB
- Rifampin resistance on GeneXpert: Do NOT use rifampin; consult infectious disease for second-line regimen (fluoroquinolone + injectable agent based)
- MDR-TB: Requires specialized treatment center

## Disposition

- **Admit** if: hemoptysis, respiratory failure, miliary disease, meningitis, inability to maintain isolation at home, no public health follow-up established
- **May discharge with public health coordination** if: stable, able to isolate at home, follow-up arranged with TB clinic within 1-3 days
- **Airborne isolation:** Continue until 3 consecutive negative AFB smears on sputum collected 8-24h apart (in practice, often 2+ weeks of treatment with clinical improvement)
- **Contact investigation:** Public health department must be notified immediately for contact tracing
- **Reportable:** MANDATORY REPORTABLE disease in all US states — report to local/state health department within 24 hours
- **Directly observed therapy (DOT):** Standard of care; coordinate with public health

## Pitfalls

1. **Failing to isolate.** A single unmasked TB patient in the ED can expose dozens of staff and patients. Airborne isolation (negative-pressure room, N95 for staff, surgical mask on patient) must be immediate upon suspicion.

2. **Atypical CXR in HIV-coinfected patients.** Patients with CD4 < 200 may have lower lobe infiltrates, hilar lymphadenopathy, miliary pattern, or even a normal CXR. Do not rely on "classic" upper lobe cavitary disease to make the diagnosis.

3. **Using IGRA or TST to diagnose active TB.** These tests detect immune response to TB antigens and are negative in up to 25% of active TB cases (especially immunocompromised). They diagnose latent infection, not active disease.

4. **Discharging without public health notification.** Active TB is legally reportable. Failure to report delays contact investigation and enables community transmission.

5. **Not testing for HIV.** TB-HIV coinfection significantly alters management (drug interactions, atypical presentations, higher mortality). All TB patients should be HIV-tested.

6. **Performing aerosol-generating procedures without airborne precautions.** Sputum induction, bronchoscopy, intubation, and nebulizer treatments all generate infectious aerosols. Full airborne precautions and HEPA filtration are mandatory.
