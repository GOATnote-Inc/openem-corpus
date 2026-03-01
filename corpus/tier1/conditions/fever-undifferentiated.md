---
id: fever-undifferentiated
condition: "Fever — Undifferentiated Emergency Evaluation"
aliases: [fever, pyrexia, febrile, undifferentiated fever, fever of unknown source]
icd10: [R50.9, R50.81]
esi: 3
time_to_harm:
  irreversible_injury: "< 6 hours (meningitis, necrotizing fasciitis)"
  death: "< 24 hours (sepsis, meningitis, necrotizing fasciitis)"
  optimal_intervention_window: "< 60 minutes (antibiotics for sepsis and meningitis)"
category: presentations
condition_type: presentation
chief_complaint: "Fever"
differential_categories:
  - category: life-threatening
    conditions:
      - sepsis
      - bacterial-meningitis
      - necrotizing-fasciitis
      - fourniers-gangrene
      - neutropenic-fever
      - epiglottitis
      - malignant-hyperthermia
      - thyroid-storm
      - heat-stroke
      - toxic-shock-syndrome
  - category: emergent
    conditions:
      - pneumonia
      - ascending-cholangitis
      - pyelonephritis
      - acute-appendicitis
      - acute-cholecystitis
      - spinal-epidural-abscess
      - retropharyngeal-abscess
      - peritonsillar-abscess
      - infective-endocarditis
      - hepatic-abscess
      - empyema
      - mastoiditis
      - malignant-otitis-externa
      - hsv-encephalitis
      - covid-pneumonia-severe
      - complicated-uti
      - serotonin-syndrome
      - neuroleptic-malignant-syndrome
  - category: urgent
    conditions:
      - cellulitis-abscess
      - acute-diverticulitis
      - deep-vein-thrombosis
      - kawasaki-disease
      - drug-hypersensitivity-reaction
  - category: non-emergent
    conditions: []
red_flags:
  - "Hypotension (SBP < 90) or tachycardia (HR > 120) with fever"
  - "Altered mental status"
  - "Petechial or purpuric rash (meningococcemia, TTP, DIC)"
  - "Immunocompromised (neutropenic, HIV, transplant, chemotherapy)"
  - "Rigors (shaking chills) — suggest bacteremia"
  - "Indwelling hardware (prosthetic valve, joint, vascular graft, central line)"
  - "IVDU with fever"
  - "Recent surgery or invasive procedure"
  - "Extremes of age (neonates, elderly > 65)"
  - "Pain out of proportion to exam with overlying erythema (necrotizing fasciitis)"
  - "Rapid progression of skin changes"
decision_rules:
  - name: "qSOFA"
    citation: "Seymour CW et al. Assessment of Clinical Criteria for Sepsis: For the Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). JAMA. 2016;315(8):762-774."
    pmid: "26903335"
  - name: "SIRS Criteria"
    citation: "Bone RC et al. Definitions for sepsis and organ failure and guidelines for the use of innovative therapies in sepsis. Chest. 1992;101(6):1644-1655."
    pmid: "1303622"
track: tier1
sources:
  - type: guideline
    ref: "Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock. 2021."
    doi: "10.1007/s00134-021-06506-y"
  - type: guideline
    ref: "IDSA Practice Guidelines for the Diagnosis and Management of Community-Acquired Pneumonia in Adults. 2019."
    pmid: "31573350"
  - type: guideline
    ref: "IDSA Clinical Practice Guideline for Acute Bacterial Rhinosinusitis in Children and Adults. 2012."
    pmid: "22438350"
  - type: review
    ref: "Nakamura MM et al. Fever of unknown origin in the emergency department. Emerg Med Clin North Am. 2013;31(4):913-926."
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
# Fever — Undifferentiated Emergency Evaluation

## Recognition

Fever is defined as temperature >= 38.0°C (100.4°F). In the ED, the primary goal is identifying patients with life-threatening infections (sepsis, meningitis, necrotizing soft tissue infection) and those in high-risk categories requiring empiric treatment. Approximately 5% of febrile ED patients have bacteremia; the challenge is identifying them.

**Non-infectious causes of fever (must keep on differential):**
- Drug fever (antibiotics, anticonvulsants, common cause in hospitalized patients)
- Malignant hyperthermia (post-anesthetic exposure, volatile agents, succinylcholine)
- Neuroleptic malignant syndrome (antipsychotic exposure, rigidity, autonomic instability)
- Serotonin syndrome (serotonergic drug interaction, clonus, hyperreflexia)
- Thyroid storm (thyrotoxicosis, tachycardia, AMS)
- Heat stroke (environmental exposure, core temp > 40°C)
- Drug reaction (SJS/TEN, DRESS)
- Malignancy (lymphoma, leukemia, renal cell carcinoma)
- Adrenal crisis (may present with hypothermia but can be febrile)
- DVT/PE (low-grade fever in up to 14% of PE)
- Transfusion reaction

**Hypothermia as "sepsis equivalent":**
Temperature < 36°C (96.8°F) with infection is an ominous sign indicating overwhelming sepsis with hemodynamic failure. Elderly and immunosuppressed patients frequently present hypothermic rather than febrile.

**Key history elements:**
- Duration and pattern of fever
- Associated localizing symptoms: cough (pneumonia), dysuria (UTI), headache/neck stiffness (meningitis), abdominal pain (intra-abdominal infection), skin changes (cellulitis, NSTI)
- Immune status: HIV, transplant, chemotherapy, steroids, biologics, splenectomy, diabetes
- Recent travel (malaria, dengue, typhoid)
- Recent procedures, hospitalizations, antibiotics (C. diff, resistant organisms)
- Indwelling devices: central lines, prosthetic valves/joints, vascular grafts
- IVDU: endocarditis, epidural abscess, septic arthritis, osteomyelitis
- Medications: antipsychotics (NMS), serotonergic drugs, new medications (drug fever)
- Animal/insect exposures: tick-borne illness, animal bites

## Critical Actions

| Action | Target |
|---|---|
| Identify hemodynamic instability | < 5 minutes |
| Blood cultures (before antibiotics) | < 15 minutes |
| Lactate level | < 15 minutes |
| Empiric antibiotics if sepsis suspected | < 60 minutes (Surviving Sepsis Campaign) |
| 30 mL/kg crystalloid if sepsis-induced hypotension | < 3 hours |

**Evaluation algorithm:**

1. **Assess for sepsis.** Apply qSOFA (GCS < 15, RR >= 22, SBP <= 100) or SIRS criteria (temp > 38 or < 36, HR > 90, RR > 20, WBC > 12k or < 4k). qSOFA >= 2 → high mortality risk. Any suspicion for sepsis → initiate sepsis bundle.

2. **Sepsis bundle (Hour-1):**
   - Measure lactate (> 2 mmol/L = tissue hypoperfusion; > 4 mmol/L = septic shock physiology)
   - Blood cultures x 2 (from different sites) before antibiotics
   - Broad-spectrum antibiotics within 1 hour
   - 30 mL/kg crystalloid for hypotension or lactate >= 4 mmol/L
   - Reassess perfusion, re-measure lactate if initial > 2 mmol/L

3. **Source identification.** Systematic evaluation:
   - **Head/neck:** meningeal signs, oropharyngeal exam (peritonsillar abscess, Ludwig angina), sinuses, ears (mastoiditis)
   - **Lungs:** auscultation, CXR
   - **Heart:** new murmur (endocarditis)
   - **Abdomen:** tenderness, peritoneal signs (intra-abdominal abscess, cholangitis, appendicitis)
   - **Genitourinary:** CVA tenderness (pyelonephritis), suprapubic (UTI), perineal (Fournier gangrene)
   - **Skin:** cellulitis, wounds, surgical sites, indwelling catheter sites, ecchymoses/petechiae, crepitus (gas gangrene), disproportionate pain (NSTI)
   - **Joints:** warm, swollen, painful joint (septic arthritis — arthrocentesis if suspected)
   - **Lines/devices:** inspect all intravascular catheters, prosthetic sites

4. **High-risk populations requiring empiric treatment:**
   - **Neutropenic fever (ANC < 500):** Cefepime 2 g IV or piperacillin-tazobactam 4.5 g IV immediately. This is an emergency — delay is associated with mortality (see `neutropenic-fever`).
   - **Splenectomy/functional asplenia:** Encapsulated organism risk (Strep pneumoniae, N. meningitidis, H. influenzae). Ceftriaxone 2 g IV empirically.
   - **IVDU:** Blood cultures x 3 (if possible), echocardiography for endocarditis, MRI spine if back pain
   - **Prosthetic hardware:** Low threshold for imaging + aspiration of joint/collection

## Differential Diagnosis

### Life-Threatening
- **Sepsis/septic shock** (`sepsis`): suspected infection + organ dysfunction. Hypotension, tachycardia, AMS, lactate elevation. Source may not be immediately apparent.
- **Bacterial meningitis** (`bacterial-meningitis`): fever, headache, nuchal rigidity, AMS. Classic triad < 50%. LP diagnostic. Do NOT delay antibiotics.
- **Necrotizing fasciitis** (`necrotizing-fasciitis`): fever + pain out of proportion to exam + skin changes (edema, erythema, crepitus, bullae, necrosis). Surgical emergency. CT may show gas in soft tissue. LRINEC score may assist but sensitivity is limited.
- **Fournier gangrene** (`fourniers-gangrene`): perineal NSTI, often in diabetics, rapidly progressive
- **Neutropenic fever** (`neutropenic-fever`): ANC < 500 + temp >= 38.3°C (single) or >= 38.0°C sustained > 1 hour. Empiric antibiotics within 60 minutes mandatory.
- **Epiglottitis** (`epiglottitis`): fever, muffled voice, drooling, dysphagia, stridor. Do NOT examine with tongue depressor if suspected in children. Adults: flexible nasopharyngoscopy.
- **Malignant hyperthermia** (`malignant-hyperthermia`): post-anesthetic, masseter spasm, rapidly rising temperature > 40°C, rhabdomyolysis, hypercarbia. Dantrolene 2.5 mg/kg IV immediately.
- **Thyroid storm** (`thyroid-storm`): fever, tachycardia out of proportion, AMS, known hyperthyroidism. Burch-Wartofsky score >= 45.
- **Heat stroke** (`heat-stroke`): core temp > 40°C, CNS dysfunction, exertional or classic
- **Toxic shock syndrome** (`toxic-shock-syndrome`): fever, diffuse macular rash, hypotension, multiorgan involvement, recent wound or tampon use

### Emergent
- **Pneumonia** (`pneumonia`): cough, dyspnea, crackles, infiltrate on CXR. CURB-65 or PSI for risk stratification.
- **Ascending cholangitis** (`ascending-cholangitis`): Charcot triad (fever, RUQ pain, jaundice). ERCP emergently.
- **Pyelonephritis** (`pyelonephritis`): fever, flank pain, CVA tenderness, pyuria/bacteriuria
- **Appendicitis** (`acute-appendicitis`): fever, RLQ pain, anorexia, leukocytosis
- **Cholecystitis** (`acute-cholecystitis`): fever, RUQ pain, Murphy sign
- **Epidural abscess** (`spinal-epidural-abscess`): fever, back pain, neurological deficit (late). IVDU, immunocompromised.
- **Deep neck space infections** (`retropharyngeal-abscess`, `peritonsillar-abscess`): fever, odynophagia, trismus, neck swelling, drooling
- **Infective endocarditis** (`infective-endocarditis`): fever + new murmur + risk factors (IVDU, prosthetic valve, dental procedure). Modified Duke criteria.
- **Hepatic abscess** (`hepatic-abscess`): fever, RUQ pain, diabetes, recent biliary procedure
- **Empyema** (`empyema`): fever persisting despite pneumonia treatment, pleural effusion
- **HSV encephalitis** (`hsv-encephalitis`): fever, AMS, temporal lobe seizures
- **Serotonin syndrome** (`serotonin-syndrome`): fever, clonus, hyperreflexia, agitation, serotonergic drug exposure
- **NMS** (`neuroleptic-malignant-syndrome`): fever, rigidity, AMS, autonomic instability, antipsychotic exposure

### Urgent
- **Cellulitis/abscess** (`cellulitis-abscess`): localized erythema, warmth, swelling, fluctuance (abscess). I&D for abscess.
- **Diverticulitis** (`acute-diverticulitis`): LLQ pain, fever, leukocytosis
- **DVT** (`deep-vein-thrombosis`): low-grade fever in up to 30% of DVT
- **Kawasaki disease** (`kawasaki-disease`): pediatric, fever >= 5 days, conjunctivitis, rash, mucous membrane changes, extremity changes, lymphadenopathy
- **Drug hypersensitivity reaction** (`drug-hypersensitivity-reaction`): fever, rash, eosinophilia, recent new medication

## Workup

**All febrile patients with concerning features:**
- CBC with differential (leukocytosis, bandemia, neutropenia, thrombocytopenia)
- BMP (renal function, electrolytes)
- Lactate (sepsis marker — > 2 mmol/L concerning, > 4 mmol/L requires aggressive resuscitation)
- Blood cultures x 2 (different sites, before antibiotics)
- Urinalysis + urine culture

**Source-directed workup:**
- **Pulmonary:** CXR (PA and lateral if ambulatory), procalcitonin (useful for distinguishing bacterial from viral)
- **Meningitis:** LP (CSF cell count, protein, glucose, gram stain, culture, HSV PCR). Meningococcal PCR if available.
- **Abdominal:** CT abdomen/pelvis with IV contrast, hepatic panel, lipase
- **Skin/soft tissue:** CT with contrast (gas gangrene, deep abscess), surgical exploration for NSTI
- **Endocarditis:** Blood cultures x 3, echocardiography (TTE then TEE if TTE negative with ongoing suspicion)
- **Joint:** Arthrocentesis (cell count > 50,000 WBC/mm3 with > 75% PMNs → septic arthritis until proven otherwise)

**Not routinely helpful:**
- CRP and procalcitonin alone do not diagnose or exclude serious bacterial infection — use as adjuncts only
- Viral panels in adults rarely change management in the ED
- Routine blood cultures in low-risk febrile patients without SIRS criteria: low yield (< 2%)

## Treatment

Stabilization and empiric therapy while identifying source:

- **IV crystalloid:** NS or LR 30 mL/kg for sepsis-induced hypotension or lactate >= 4 mmol/L
- **Vasopressors:** Norepinephrine 0.05-0.5 mcg/kg/min first-line if MAP < 65 despite fluid resuscitation
- **Antipyretics:** Acetaminophen 1 g IV/PO for patient comfort. Evidence does NOT support routine antipyresis improving outcomes in sepsis, but it reduces metabolic demand.
- **Empiric antibiotics (source-dependent):**
  - Unknown source: vancomycin 25-30 mg/kg IV + piperacillin-tazobactam 4.5 g IV OR cefepime 2 g IV
  - Pneumonia: ceftriaxone 1 g IV + azithromycin 500 mg IV (or respiratory fluoroquinolone monotherapy)
  - UTI/pyelonephritis: ceftriaxone 1 g IV (uncomplicated), piperacillin-tazobactam 4.5 g IV (complicated/septic)
  - Meningitis: vancomycin 25-30 mg/kg IV + ceftriaxone 2 g IV + dexamethasone 0.15 mg/kg IV
  - Neutropenic fever: cefepime 2 g IV (monotherapy) OR piperacillin-tazobactam 4.5 g IV
  - NSTI: vancomycin 25-30 mg/kg IV + piperacillin-tazobactam 4.5 g IV + clindamycin 900 mg IV (toxin inhibition)
- **Source control:** I&D for abscess, surgical debridement for NSTI, ERCP for cholangitis, line removal for CLABSI

## Disposition

- **ICU:** Septic shock (persistent hypotension despite fluids), intubated for airway protection, NSTI post-debridement, meningitis with hemodynamic instability
- **Step-down/telemetry:** Sepsis responding to initial resuscitation, endocarditis on IV antibiotics, complicated pneumonia
- **Floor admission:** Pyelonephritis requiring IV antibiotics, cellulitis requiring IV antibiotics, neutropenic fever on empiric therapy
- **Observation:** Fever of unclear source in elderly or immunocompromised (pending cultures and monitoring)
- **Discharge:** Low-risk febrile patient with identified viral source, uncomplicated UTI, simple cellulitis/abscess (post-I&D) with reliable follow-up. Ensure blood cultures are followed up.
- **Important:** Do NOT discharge neutropenic patients with fever. Do NOT discharge patients with undrained abscesses (unless superficial and completely drained in ED).

## Pitfalls

1. **Normal or low temperature in elderly and immunosuppressed sepsis.** Up to 30% of elderly patients with bacteremia are afebrile. Hypothermia (< 36°C) with suspected infection is an ominous sign. Use clinical suspicion and lactate rather than relying on fever.

2. **Anchoring on UTI as fever source in elderly.** Asymptomatic bacteriuria prevalence is 20-50% in institutionalized elderly. A positive UA does NOT confirm the fever source. Look for other causes (pneumonia, intra-abdominal, skin/soft tissue) even when UA is positive.

3. **Delaying antibiotics waiting for culture results or imaging.** In sepsis, each hour of antibiotic delay increases mortality by 7-8%. Blood cultures before antibiotics is ideal but should take < 15 minutes. Do NOT wait for CT, LP, or any other test to give antibiotics when sepsis is suspected.

4. **Missing necrotizing fasciitis.** NSTI can present with minimal skin findings early. Pain out of proportion to visible skin changes is the cardinal feature. Crepitus and bullae are late findings. A normal-appearing skin surface does not exclude deep NSTI. CT or surgical exploration if suspected.

5. **Failing to consider non-infectious hyperthermia.** NMS, serotonin syndrome, malignant hyperthermia, and thyroid storm all cause high fever and are not treated with antibiotics. Review medication list in every febrile patient. Rigidity + hyperthermia + AMS → consider NMS or serotonin syndrome before anchoring on sepsis.

6. **Discharging the febrile IVDU patient without endocarditis evaluation.** IVDU + fever requires blood cultures and at minimum TTE (ideally TEE). Fever in IVDU can represent endocarditis, epidural abscess, septic arthritis, or osteomyelitis. These diagnoses are catastrophic if missed.

7. **Ignoring rigors.** Shaking chills (rigors, not simple shivering) are 40-60% predictive of bacteremia. A febrile patient with rigors is significantly more likely to have bacteremia than one with simple fever and should be treated accordingly.
