---
id: radiation-mass-casualty
condition: Radiation Mass Casualty Event
aliases: [radiation emergency, nuclear incident, radiological dispersal device, dirty bomb, acute radiation syndrome, ARS]
icd10: [T66.XXXA, W88.0XXA, W88.1XXA, W88.8XXA, Y38.5X0A, T07.XXXA]
esi: 1
time_to_harm:
  irreversible_injury: "< 24 hours for bone marrow syndrome (>2 Gy); immediate for >10 Gy (GI/cerebrovascular syndrome)"
  death: "48 hours to 60 days depending on dose (LD50/60 ≈ 3.5-4.5 Gy without treatment, ~7 Gy with supportive care)"
  optimal_intervention_window: "Cytokine therapy within 24 hours of exposure; KI within 4 hours of radioiodine exposure"
category: disaster-mci
track: tier1
sources:
  - type: guideline
    ref: "Radiation Emergency Medical Management (REMM), U.S. Department of Health and Human Services. https://remm.hhs.gov/"
    url: "https://remm.hhs.gov/"
  - type: consensus-statement
    ref: "National Council on Radiation Protection and Measurements (NCRP). Report No. 161: Management of Persons Contaminated with Radionuclides. Bethesda, MD: NCRP, 2008."
  - type: pubmed
    ref: "Waselenko JK et al. Medical management of the acute radiation syndrome: recommendations of the Strategic National Stockpile Radiation Working Group. Ann Intern Med. 2004;140(12):1037-1051."
    pmid: "15197022"
  - type: pubmed
    ref: "Dainiak N et al. Literature review and global consensus on management of acute radiation syndrome affecting nonhuman primates. Disaster Med Public Health Prep. 2011;5(Suppl 1):S183-S195."
    pmid: "21402813"
  - type: pubmed
    ref: "Gusev IA, Guskova AK, Mettler FA. Medical Management of Radiation Accidents, 2nd Edition. CRC Press, 2001."
last_updated: "2026-02-26"
compiled_by: agent
risk_tier: A
validation:
  schema_version: "2.0"
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  guideline_version_reference: null
  provenance_links: []
---
# Radiation Mass Casualty Event

## Recognition

**Definition:** A radiation mass casualty event involves exposure of multiple persons to ionizing radiation from a nuclear detonation, radiological dispersal device (RDD/"dirty bomb"), nuclear facility incident, or industrial/medical source accident. Radiation injury is invisible, painless at onset (except at very high doses), and produces a delayed clinical syndrome that evolves over days to weeks.

**Exposure Scenarios:**

| Scenario | Source | Radiation Type | Contamination Risk |
|----------|--------|---------------|-------------------|
| **Nuclear detonation** | Fission/fusion weapon | Gamma, neutron, beta, fallout | Massive: fallout particles, induced radioactivity |
| **Radiological dispersal device (dirty bomb)** | Conventional explosive + radioactive material (Cs-137, Co-60, Ir-192) | Gamma, beta | Moderate: aerosolized particles, blast debris |
| **Nuclear facility accident** | Reactor meltdown (Chernobyl, Fukushima) | Gamma, beta, radioiodine (I-131) | Massive: airborne plume, groundwater contamination |
| **Industrial source** | Orphaned source (Goiânia incident), radiography device | Gamma (Co-60, Cs-137, Ir-192) | Variable: contact contamination |
| **Medical source** | Teletherapy device, brachytherapy source | Gamma, beta | Usually low unless source shielding breached |

**Types of Radiation Exposure:**
- **Irradiation (external exposure):** Patient exposed to radiation source but NOT contaminated. Not radioactive — no decontamination needed. Treat without PPE.
- **Contamination (external):** Radioactive material on skin, clothing, wounds. Patient IS radioactive. Requires decontamination. PPE for providers (standard precautions + N95 + double gloves sufficient for beta/gamma — NOT alpha).
- **Incorporation (internal):** Radioactive material inhaled, ingested, or absorbed through wounds. Requires internal decontamination (chelation, Prussian blue, KI).
- **Combined injury:** Radiation + trauma (blast, burns, penetrating). Mortality significantly higher than either alone. Combined injury patients are highest priority for treatment.

**Acute Radiation Syndrome (ARS) — Dose-Dependent Phases:**

| Dose (Gy) | Syndrome | Prodrome Onset | Latent Period | Manifest Illness | Prognosis |
|-----------|----------|---------------|---------------|-------------------|-----------|
| 0.7–2 | Mild hematopoietic | 2–6 h | 21–35 d | Moderate cytopenia | Survival >90% with supportive care |
| 2–6 | Moderate-severe hematopoietic | 1–2 h | 7–21 d | Severe pancytopenia, infections, hemorrhage | Survival with aggressive support (G-CSF, transfusions); LD50/60 ~3.5–4.5 Gy |
| 6–10 | GI syndrome + hematopoietic | <1 h | 5–7 d | GI mucosal sloughing, sepsis, hemorrhage | Survival possible with stem cell transplant |
| >10 | Cerebrovascular syndrome | Minutes | None | Cerebral edema, seizures, coma, cardiovascular collapse | Fatal within 48 hours; no effective treatment |

**Prodrome (0–48h post-exposure):**
- Nausea, vomiting, diarrhea — onset time inversely correlates with dose
- Vomiting within 1 hour = >4 Gy dose estimate
- Vomiting within 30 minutes = >6 Gy
- Vomiting within 10 minutes = >8 Gy (likely fatal without SCT)
- Other: headache, fatigue, fever, erythema (>3 Gy), parotid swelling (>4 Gy)

**Andrews Lymphocyte Depletion Kinetics (Biodosimetry):**
- Absolute lymphocyte count (ALC) at 24h and 48h post-exposure predicts dose
- ALC 1,000–1,500/µL at 48h → ~1–2 Gy
- ALC 500–1,000/µL at 48h → ~2–4 Gy
- ALC <500/µL at 48h → >4 Gy
- ALC <100/µL at 48h → >8 Gy (lethal range)

## Critical Actions

1. **Establish radiation safety perimeter.** Contact radiation safety officer (RSO) or health physics team. Use radiation survey meters (Geiger-Mueller, ionization chamber) to define contamination zones. Background radiation: 0.1–0.2 µSv/h. Contaminated zone: >2× background. Hot Zone: >100 µSv/h.

2. **Triage radiation casualties using dose estimation.** Three rapid triage tools:
   - **Time to vomiting:** <1h = high dose (>4 Gy), priority for cytokine therapy. >4h or no vomiting = lower dose.
   - **ALC at 24–48h:** Gold standard for dose estimation in the first 72h.
   - **Dicentric chromosome assay:** Definitive biodosimetry but requires 48–72h for results. Send samples early.

3. **Treat combined injury patients first.** Radiation + trauma (blast, burns) has synergistic mortality. Perform trauma resuscitation (ATLS) without delay. Surgical wounds must be debrided and closed within 36–48h of irradiation — the latent period closes, and wound healing fails after bone marrow suppression onset.

4. **Decontaminate externally contaminated patients.** Remove clothing (eliminates 90% of external contamination). Wash skin with soap and tepid water — gentle, no abrasion (breaks in skin increase incorporation). Survey with GM meter after each wash cycle. Target: <2× background. Wounds decontaminated before intact skin. Irrigate contaminated wounds with copious NS.

5. **Administer potassium iodide (KI) for radioiodine exposure within 4 hours.**
   - Adults: KI 130 mg PO × 1 dose
   - Children 3–18 years: KI 65 mg PO
   - Children 1 month–3 years: KI 32 mg PO
   - Neonates <1 month: KI 16 mg PO
   - Effective only for I-131 exposure (nuclear detonation fallout, reactor accident). Useless for Cs-137, Co-60, or other isotopes.
   - Efficacy >90% if given within 4h of exposure, ~50% at 12h, negligible at 24h.

6. **Initiate cytokine therapy within 24 hours for estimated dose >2 Gy.**
   - Filgrastim (G-CSF): 10 mcg/kg/day SC (round to nearest vial: 300 or 480 mcg). Continue until ANC >1,000/µL for 3 consecutive days.
   - Pegfilgrastim: 6 mg SC × 1 dose. Repeat weekly if ANC does not recover.
   - Sargramostim (GM-CSF): 250 mcg/m²/day SC — alternative if filgrastim unavailable.
   - Early cytokine therapy reduces hematopoietic syndrome mortality from 50% to <20% for doses 3–7 Gy.

7. **Internal decontamination for incorporated radionuclides:**
   - Cs-137: Prussian blue (Radiogardase) 3 g PO TID (adults), 1 g PO TID (children 2–12 years). Continue for 30 days minimum. Reduces Cs-137 biological half-life from 70 days to 30 days.
   - Plutonium/Americium/Curium (transuranic elements): Ca-DTPA 1 g IV over 3–4 min within 24h, then switch to Zn-DTPA 1 g IV daily. Nebulized Ca-DTPA 1 g for inhalation exposure.
   - Uranium: Sodium bicarbonate 2 ampules (84 mEq) in 1 L D5W IV to alkalinize urine (target urine pH >7.5) — reduces nephrotoxicity.
   - Tritium (H-3): Forced oral hydration 3–4 L/day to accelerate excretion.

8. **Serial CBC with differential q6h for first 48h, then q12h through day 7.** Lymphocyte kinetics are the primary biodosimetry tool. Plot ALC on Andrews nomogram. Repeat at 24h, 48h, 72h, and day 7. Neutrophil nadir predicts timing of maximal infection risk.

## Differential Diagnosis

| Presentation | Radiation Syndrome | Non-Radiation Differential |
|-------------|-------------------|---------------------------|
| Acute nausea/vomiting post-exposure | ARS prodrome | Acute gastroenteritis, food poisoning, anxiety/psychogenic vomiting (extremely common in radiation scares) |
| Progressive pancytopenia | Hematopoietic syndrome | Aplastic anemia, chemotherapy toxicity, overwhelming sepsis |
| Bloody diarrhea + fever at 7–14 days | GI syndrome | C. difficile colitis, ischemic colitis, inflammatory bowel disease flare |
| Seizure + altered mental status post-exposure | Cerebrovascular syndrome (>10 Gy) | TBI (combined injury), status epilepticus, hyponatremia |
| Skin erythema progressing to ulceration | Cutaneous radiation syndrome | Thermal burn, chemical burn, necrotizing fasciitis |

**Worried Well vs. Actual Exposure:**
- In radiation events, expect 5–10 worried-well patients for every actual exposure. Mass psychogenic illness (vomiting from anxiety) mimics ARS prodrome.
- Differentiate: radiation survey with GM meter (contaminated vs. clean), exposure history (proximity, duration, shielding), ALC at 24h (normal ALC rules out significant exposure).

## Workup

**Initial (0–6h):**
- Radiation survey of all patients with GM counter (counts per minute) before and after decontamination
- CBC with manual differential (ALC baseline)
- BMP (baseline renal function — uranium nephrotoxicity, IV fluid management)
- Amylase (>2× ULN at 24h correlates with >4 Gy; parotid gland sensitivity to radiation)
- Blood for cytogenetic biodosimetry (dicentric chromosome assay) — 10 mL heparinized blood, send to REAC/TS or designated biodosimetry lab
- Blood type and screen
- Urinalysis (baseline, internal contamination assessment — urine bioassay for Cs-137, U, Pu)
- Nasal swabs bilaterally (count on GM meter — positive suggests inhalation of radioactive particles)
- Wound survey with GM counter if any open wounds

**Serial Monitoring (6h–7d):**
- CBC with differential q6h × 48h, then q12h through day 7, then daily
- Plot ALC on Andrews nomogram at 24h, 48h, 72h
- BMP daily (electrolyte management, renal function monitoring)
- Blood cultures if febrile (neutropenic fever protocol applies once ANC <500)
- Fecal and urine bioassays for internal contamination (serial collections over 72h)

**Imaging:**
- CXR: baseline (combined injury assessment, aspiration)
- CT as indicated for combined injuries (blast, penetrating)
- No radiation-specific imaging required

## Treatment

**Hematopoietic Syndrome (2–6 Gy):**
- Filgrastim 10 mcg/kg/day SC starting within 24h, continue until ANC recovery (>1,000 × 3 days)
- Antimicrobial prophylaxis when ANC <500/µL:
  - Levofloxacin 500 mg PO/IV daily (fluoroquinolone prophylaxis)
  - Fluconazole 400 mg PO/IV daily (antifungal prophylaxis)
  - Acyclovir 400 mg PO TID (HSV prophylaxis if seropositive)
- Neutropenic fever (ANC <500 + temp >38.3°C): piperacillin-tazobactam 4.5 g IV q6h (or meropenem 1 g IV q8h if penicillin allergy). Add vancomycin 15–20 mg/kg IV q8–12h if hemodynamically unstable, catheter-related infection suspected, or MRSA risk factors.
- Platelet transfusion: threshold <10,000/µL (or <50,000 if active bleeding)
- pRBC transfusion: hemoglobin <7 g/dL (or <10 if cardiovascular disease)
- Irradiated blood products only (prevent transfusion-associated GVHD in immunocompromised patient)
- Stem cell transplant (SCT): reserve for dose >7 Gy with HLA-matched donor available and absence of GI/cerebrovascular syndrome. Decision point: day 7–14 if ALC <100 and no recovery on cytokines.

**GI Syndrome (6–10 Gy):**
- All hematopoietic syndrome treatments above PLUS:
- Aggressive IV fluid resuscitation: LR or NS to replace massive GI losses (5–10 L/day may be needed)
- Ondansetron 4 mg IV q4–6h (or granisetron 1 mg IV q12h) for intractable vomiting
- TPN when enteral nutrition fails (GI mucosal sloughing → malabsorption)
- Broad-spectrum antibiotics for GI translocation: meropenem 1 g IV q8h + vancomycin 15–20 mg/kg IV q8–12h
- Loperamide 4 mg PO initially then 2 mg after each loose stool (max 16 mg/day) — controversial, but reduces fluid losses

**Cerebrovascular Syndrome (>10 Gy):**
- Universally fatal. No effective treatment.
- Comfort care: morphine 2–4 mg IV q2h PRN, midazolam 2 mg IV q4h PRN for seizures/agitation
- Antiemetics for prodromal vomiting
- If combined injury with otherwise survivable trauma: treat trauma aggressively while recognizing radiation dose is unsurvivable. This is an ethics and resource allocation decision.

**Cutaneous Radiation Syndrome:**
- Erythema (>3 Gy): cool compresses, topical corticosteroids (triamcinolone 0.1% cream BID)
- Desquamation: silver sulfadiazine cream, non-adherent dressings
- Deep ulceration (>10 Gy local): surgical debridement, skin grafting, possible amputation
- Pain management: gabapentin 300 mg PO TID escalating to 1200 mg TID for neuropathic component

## Disposition

**Dose-Based Triage and Disposition:**

| Estimated Dose | Category | Disposition |
|---------------|----------|-------------|
| <0.7 Gy | Minimal | Decontaminate, reassure, outpatient ALC at 48h. Discharge. |
| 0.7–2 Gy | Delayed (T2) | Outpatient with CBC q2–3 days for 30 days. Cytokine therapy if ALC trending down. |
| 2–6 Gy | Immediate (T1) | Admit. Cytokine therapy. Reverse isolation when ANC <500. Survival likely with treatment. |
| 6–10 Gy | Immediate (T1) | ICU admission. Cytokine therapy + full supportive care. SCT consultation. Guarded prognosis. |
| >10 Gy | Expectant (T3) | Comfort care. No curative treatment exists. If combined injury: address trauma surgically only if radiation dose uncertain. |

**Decontamination Disposition:**
- External contamination <2× background after washing: cleared for admission to uncontrolled ward
- Persistent contamination: continue decontamination, isolate in designated radiation ward
- Internal contamination: admit for chelation/decorporation therapy, serial bioassays

**Combined Injury Priorities:**
- All surgical interventions within 36–48h of exposure (before marrow failure onset)
- Wound closure, fracture fixation, burn debridement — complete before latent period ends
- After marrow nadir: surgery carries unacceptable infection and hemorrhage risk

**Psychological Casualties:**
- Expect 5–10× more worried-well than actual exposure patients
- Triage with radiation survey (GM counter): negative survey + no proximity = reassurance and discharge
- Provide fact sheets, radiation dose information, and follow-up contact numbers
- Mass anxiolytic administration is not appropriate — psychological first aid and accurate information reduce panic

## Pitfalls

1. **Delaying trauma care to perform radiation survey.** In combined injury (blast + radiation), trauma kills faster than radiation. Start ATLS primary survey immediately. Decontamination and radiation survey occur in parallel, not before, trauma resuscitation. A contaminated patient is not dangerous to providers in standard PPE (gloves, gown, N95) — gamma irradiation risk from surface contamination is minimal at arm's length.

2. **Failing to obtain serial lymphocyte counts.** ALC at 24h and 48h is the single most important prognostic tool after radiation exposure. A single normal CBC means nothing — the value is in the trend. A drop from 2,000 to 500 in 24h = high-dose exposure requiring cytokine therapy. Without serial counts, dose estimation relies on vomiting time alone (less accurate).

3. **Administering KI for non-iodine radiation sources.** KI protects the thyroid from radioactive iodine (I-131) only. It is useless for Cs-137, Co-60, Ir-192, or any non-iodine radionuclide. In a dirty bomb scenario (most likely Cs-137 or Co-60), KI provides zero benefit and may cause adverse effects (allergic reaction, neonatal hypothyroidism). Identify the isotope before distributing KI.

4. **Mistaking psychogenic vomiting for ARS prodrome.** Mass radiation events generate mass anxiety. Psychogenic nausea and vomiting mimic ARS prodrome. Differentiate: psychogenic vomiting occurs immediately with situational awareness, lacks diarrhea, and ALC at 24h is normal. ARS vomiting has a predictable dose-dependent latency. Radiation survey confirms or excludes exposure.

5. **Performing surgery after the latent period closes.** Surgical wounds made during marrow suppression (after day 7–14) will not heal, become infected, and hemorrhage. All operative interventions must be completed within 36–48 hours of exposure, during the latent period. After that window: only life-saving emergency surgery with broad-spectrum antibiotic coverage and platelet support.

6. **Using non-irradiated blood products.** Irradiated patients are profoundly immunosuppressed. Transfusion-associated graft-versus-host disease (TA-GVHD) from donor lymphocytes in non-irradiated blood products is fatal. All blood products (pRBC, platelets, FFP) must be irradiated (25 Gy) before transfusion. CMV-negative or leukoreduced products preferred.

### System Overwhelm

Radiation MCIs generate a uniquely prolonged resource crisis — the acute phase lasts weeks, not hours:

- **Biodosimetry bottleneck:** Dicentric chromosome assay is the definitive dose estimator but requires specialized laboratories (REAC/TS, Armed Forces Radiobiology Research Institute). Processing capacity: ~100 samples/day nationally. In a nuclear detonation with thousands of exposures, clinical biodosimetry (ALC kinetics, vomiting time) must substitute for laboratory confirmation.
- **Cytokine supply:** Filgrastim is the critical medication. A single patient requires 300–480 mcg/day for 14–21 days. 100 patients = 30,000–50,000 vials. The Strategic National Stockpile maintains reserves, but distribution takes 12–24 hours. Begin cytokine therapy with local stock and expand to SNS supply.
- **Blood product demand:** Pancytopenic patients require platelet and pRBC transfusions for 2–6 weeks. A single patient may consume 50+ platelet units and 20+ pRBC units over the course of hematopoietic syndrome. Multiply by hundreds of patients → regional and national blood supply is overwhelmed. Activate nationwide blood mobilization.
- **Isolation capacity:** Neutropenic patients require reverse isolation (HEPA-filtered positive-pressure rooms). Standard hospital capacity: 10–20 isolation rooms. If 200 patients become neutropenic simultaneously, conventional isolation is impossible. Cohort patients in clean areas, HEPA filters at doorways, strict hand hygiene, restrict all visitors.
- **Duration of care:** Unlike other MCIs that resolve in hours to days, radiation hematopoietic syndrome requires 30–60 days of inpatient management. Hospitals caring for radiation patients cannot return to normal operations for months. Regional load-sharing is essential from day 1.
- **Psychological impact:** Nuclear/radiological events generate uniquely intense fear disproportionate to actual health risk (especially for RDD/dirty bomb, where radiation dose is often sublethal). Expect massive worried-well surge (10:1 or higher ratio). Establish radiation screening stations with GM counters at hospital entrances and community sites to rapidly identify and reassure unexposed individuals.
