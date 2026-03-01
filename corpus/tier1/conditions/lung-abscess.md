---
id: lung-abscess
condition: Lung Abscess
aliases: [pulmonary abscess, necrotizing pneumonia, lung abscess primary, lung abscess secondary]
icd10: [J85.1, J85.2]
esi: 3
time_to_harm: "< 48 hours (if ruptured or septic)"
category: respiratory
track: tier1
sources:
  - type: review
    ref: "Kuhajda I, et al. Lung Abscess — Etiology, Diagnostic and Treatment Options. Ann Transl Med. 2015;3(13):183."
  - type: review
    ref: "Bartlett JG. Lung Abscess and Necrotizing Pneumonia. In: Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases. 2019."
  - type: guideline
    ref: "2019 ATS/IDSA Guidelines for Community-Acquired Pneumonia in Adults. Am J Respir Crit Care Med. 2019;200(7):e45-e67."
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
# Lung Abscess

## Recognition

**Presentation:**
- Subacute onset (1-2 weeks): fever, productive cough, foul-smelling (putrid) sputum
- Night sweats, weight loss, malaise
- Pleuritic chest pain
- Hemoptysis (25-50%)
- Tachypnea, decreased breath sounds over affected area
- Clubbing (chronic abscess)

**Risk factors for aspiration (most common cause):**
- Alcoholism, altered consciousness, seizures
- Dysphagia, esophageal disorders, GERD
- Poor dentition/periodontal disease
- Immunosuppression
- Recent general anesthesia

**Microbiology:**
- Primary abscess: anaerobes (Peptostreptococcus, Fusobacterium, Prevotella, Bacteroides) — often polymicrobial
- Secondary abscess: S. aureus (MRSA in particular), Klebsiella, Pseudomonas, Nocardia, fungi
- Consider TB in endemic areas or immunocompromised patients

**Imaging findings:**
- CXR: Cavitary lesion with air-fluid level, usually in dependent lung segments (right lower lobe, posterior segments)
- CT chest: Thick-walled cavity with air-fluid level, surrounding consolidation, enhancing wall

## Critical Actions

| Action | Target |
|---|---|
| IV antibiotics | < 2 hours |
| CT chest | < 12 hours |
| Sputum cultures | Before antibiotics |
| Assess for empyema | At presentation |

1. **IV antibiotics** — empiric coverage for anaerobes and common aerobes
2. **Respiratory isolation** if TB on differential (AFB x 3)
3. **CT chest with contrast** — confirm diagnosis, assess size, identify complications (empyema, bronchopleural fistula)
4. **Postural drainage** — position patient with abscess side dependent to promote drainage via airways
5. **Pulmonology and/or surgery consultation** if abscess > 6 cm or not improving at 7-10 days
6. **Rule out underlying malignancy** in patients > 50 years or non-responders — bronchoscopy or biopsy

## Differential Diagnosis

- **Cavitary lung cancer** — irregularly thick-walled cavity, no air-fluid level, older/smoker; biopsy required
- **Tuberculosis** — upper lobe cavitary disease, positive AFB/PPD, risk factors (immigration, HIV, incarceration)
- **Pulmonary embolism with infarction** — Hampton hump, wedge-shaped consolidation, can cavitate
- **Empyema** — purulent pleural collection; CT differentiates intraparenchymal vs pleural
- **Granulomatosis with polyangiitis** — cavitary lesions, ANCA positive, renal involvement
- **Fungal infection** — histoplasmosis, aspergillosis, coccidioidomycosis; endemic exposure

## Workup

- **CT chest with IV contrast:** Size, wall characteristics, air-fluid level, surrounding structures, empyema
- **Sputum culture (including anaerobic):** Often unreliable for anaerobes; aerobic cultures more helpful
- **Blood cultures x 2:** Before antibiotics
- **Labs:** CBC (leukocytosis), CRP/ESR (elevated), BMP, LFTs, prealbumin (nutritional status)
- **AFB smear and culture:** If TB on differential
- **Bronchoscopy:** If concern for obstruction (foreign body, malignancy), non-resolving abscess, or need for culture from lower airways
- **CXR:** Initial screening; follow serial CXRs for resolution (6-8 weeks typical)
- **Pleural fluid analysis:** If associated effusion — rule out empyema

## Treatment

### Empiric Antibiotics
- **First-line:** Ampicillin-sulbactam 3 g IV q6h (covers anaerobes + common aerobes)
- **Alternative:** Clindamycin 600 mg IV q8h + ceftriaxone 2 g IV q24h
- **MRSA coverage (if risk factors):** Add vancomycin 15-20 mg/kg IV q8-12h or linezolid 600 mg IV q12h
- **Pseudomonas coverage (if nosocomial):** Piperacillin-tazobactam 4.5 g IV q6h or meropenem 1 g IV q8h
- **Duration:** IV until clinical improvement (typically 5-7 days), then oral transition:
  - Amoxicillin-clavulanate 875/125 mg PO BID
  - Total course: 4-6 weeks minimum; continue until CXR shows resolution or small stable residual cavity

### Drainage Procedures (if medical therapy fails)
- **Percutaneous CT-guided drainage:** For large abscess (> 6 cm) or failure to improve at 7-10 days. Pigtail catheter placement. Success rate ~90%.
- **Bronchoscopic drainage:** Consider for central lesions accessible via airways
- **Surgical resection (lobectomy/segmentectomy):** Reserved for massive hemoptysis, bronchopleural fistula, suspected malignancy, failure of all other measures (< 10% of cases)

### Supportive Care
- Postural drainage and chest physiotherapy
- Nutritional support (these patients are often malnourished)
- Dental evaluation for periodontal disease

## Disposition

- **Inpatient admission:** All new lung abscesses for IV antibiotics, monitoring for complications
- **ICU admission:** Sepsis, massive hemoptysis, respiratory failure, ruptured abscess with empyema
- **Outpatient transition:** After clinical improvement (afebrile 48-72 hours, WBC normalizing, oral intake), switch to oral antibiotics
- **Follow-up imaging:** CXR at 2, 4, and 6-8 weeks. CT at 6-8 weeks if cavity persists (exclude malignancy).
- **Pulmonology referral:** Non-resolving abscess (no improvement at 7-10 days), recurrent abscess, suspected malignancy

## Pitfalls

1. **Not covering anaerobes empirically.** Primary lung abscesses are predominantly caused by anaerobic bacteria from aspiration. Standard CAP antibiotics (azithromycin + ceftriaxone) do not adequately cover anaerobes. Use ampicillin-sulbactam or clindamycin-based regimens.

2. **Stopping antibiotics too early.** Lung abscesses require prolonged therapy (4-6 weeks minimum). Premature discontinuation leads to relapse and complications. Imaging resolution lags behind clinical improvement — do not stop based on the patient feeling better alone.

3. **Missing cavitary lung cancer disguised as abscess.** Patients > 50 years, smokers, or those who fail to respond to appropriate antibiotics should undergo bronchoscopy or CT-guided biopsy. Squamous cell carcinoma commonly presents as a cavitary lesion.

4. **Failing to position the patient for postural drainage.** Positioning the patient with the abscess on the dependent side promotes gravitational drainage through the airways. This is an important adjunct to antibiotic therapy and is often overlooked.

5. **Inadequate evaluation for empyema.** Lung abscess frequently coexists with empyema or can rupture into the pleural space. CT chest should assess for concurrent pleural infection. Empyema requires tube thoracostomy in addition to antibiotics.
