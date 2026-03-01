---
id: biological-mass-casualty
condition: Biological Mass Casualty Event
aliases: [bioterrorism mass casualty, biological attack, bioweapon incident, infectious mass casualty]
icd10: [Z20.810, Z03.818]
esi: 1
time_to_harm:
  irreversible_injury: "hours to days depending on agent"
  death: "< 24 hours (inhalational anthrax), < 48 hours (pneumonic plague)"
  optimal_intervention_window: "< 24 hours post-exposure for prophylaxis; < 48 hours for treatment"
category: disaster-mci
track: tier1
sources:
  - type: cdc
    ref: "CDC Emergency Preparedness and Response: Bioterrorism Agents/Diseases. Updated 2023"
  - type: guideline
    ref: "ACEP Clinical Policy: Bioterrorism Preparedness in Emergency Medicine, 2020"
  - type: consensus-statement
    ref: "Hendricks KA, et al. Centers for Disease Control and Prevention Expert Panel Meetings on Prevention and Treatment of Anthrax in Adults. Emerg Infect Dis 2014;20(2):e130687"
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
# Biological Mass Casualty Event

## Recognition

**Epidemiologic clues to intentional biological release:**
- Unusual cluster of illness (same symptoms, same time, same geographic area)
- Disease not endemic to the region
- Unusual age distribution for the disease
- Multiple patients presenting with rapidly fatal pneumonia, mediastinitis, or hemorrhagic illness
- Dead animals in the same area
- Unusual routes of exposure (inhalational disease from typically GI/cutaneous pathogen)
- Single confirmed case of smallpox, inhalational anthrax, or pneumonic plague = presumed bioterrorism

**CDC Category A Agents (highest priority):**

| Agent | Disease | Key Features | Incubation |
|---|---|---|---|
| Bacillus anthracis | Anthrax | Widened mediastinum, hemorrhagic meningitis | 1-5 days (up to 60) |
| Yersinia pestis | Pneumonic plague | Hemoptysis, rapidly fatal pneumonia | 1-6 days |
| Variola major | Smallpox | Synchronous centrifugal vesicular rash | 7-17 days |
| Clostridium botulinum | Botulism | Descending symmetric paralysis, clear sensorium | 12-72 hours |
| Francisella tularensis | Tularemia | Pneumonia, ulceroglandular disease | 3-5 days |
| Filoviruses | Viral hemorrhagic fever | Hemorrhage, shock, multi-organ failure | 2-21 days |

**Inhalational anthrax (most likely bioterrorism agent):**
- Prodrome: fever, malaise, myalgia, non-productive cough (mimics influenza)
- Rapid deterioration: dyspnea, stridor, cyanosis, shock
- CXR: widened mediastinum (mediastinal lymphadenopathy), pleural effusions
- Hemorrhagic meningitis in 50%
- Near 100% fatal without treatment; 45% fatal even with treatment

## Critical Actions

| Action | Target |
|---|---|
| Recognize the pattern | Epidemiologic awareness |
| Activate hospital emergency plan | Upon suspicion |
| Notify public health authorities | Immediately (MANDATORY) |
| Isolate patients | Based on agent (droplet vs airborne) |
| Begin empiric treatment | < 2 hours |
| Request SNS (Strategic National Stockpile) | Through public health chain |

1. **Activate hospital incident command system (HICS)**
2. **Notify local/state health department AND CDC Emergency Operations Center (770-488-7100)** — IMMEDIATELY upon suspicion
3. **Implement appropriate isolation:**
   - Pneumonic plague: droplet precautions
   - Smallpox: airborne + contact precautions; negative pressure room
   - Anthrax: standard precautions (not person-to-person)
   - Viral hemorrhagic fever: airborne + contact + eye protection; BSL-4 referral
4. **Begin empiric antibiotics** for anthrax or plague based on clinical presentation (do NOT wait for confirmation)
5. **Coordinate with public health for mass prophylaxis** (Strategic National Stockpile deployment)
6. **Establish decontamination if aerosolized exposure suspected**

## Differential Diagnosis

- Community-acquired pneumonia (gradual onset, typical CXR infiltrates)
- Influenza (seasonal, no mediastinal widening)
- SARS-CoV-2 or other respiratory virus outbreak (PCR testing differentiates)
- Chemical exposure (immediate symptoms, not delayed incubation)
- Tularemia vs community-acquired atypical pneumonia
- Meningococcemia (petechial rash, but endemic pattern)
- Hemorrhagic fever vs severe dengue, leptospirosis, hantavirus
- Botulism from foodborne source (common source outbreak without intentional release)
- Smallpox vs varicella (synchronous centrifugal rash vs asynchronous centripetal)

## Workup

### Initial (ED — Do NOT Delay Treatment)
- **Blood cultures x 2** (before antibiotics if possible — but do NOT delay treatment)
- **CBC with differential:** leukocytosis (anthrax, plague), thrombocytopenia (VHF)
- **BMP, LFTs, coagulation studies:** organ dysfunction assessment
- **Lactate:** sepsis marker
- **CXR:** widened mediastinum (anthrax), consolidation (plague, tularemia)
- **CT chest with contrast:** mediastinal lymphadenopathy, pleural effusions (anthrax)
- **Lumbar puncture:** if meningitis suspected — hemorrhagic CSF in anthrax meningitis

### Confirmatory (Public Health/Reference Lab)
- **Anthrax:** blood culture (gram-positive rods, non-hemolytic), LRN rapid PCR
- **Plague:** sputum/blood culture (bipolar staining gram-negative rods), DFA
- **Smallpox:** vesicle fluid PCR (ONLY at LRN or CDC — do NOT culture in standard lab)
- **Botulinum toxin:** mouse bioassay (CDC reference lab)
- **Tularemia:** culture (BSL-3 required), serology
- **VHF:** RT-PCR at BSL-4 facility (CDC, USAMRIID)
- **Notify lab of suspected bioterrorism agent** — standard lab precautions insufficient for some agents

## Treatment

### Inhalational Anthrax (Begin Empirically If Suspected)
- **Ciprofloxacin 400 mg IV q8h** (or levofloxacin 750 mg IV q24h)
- PLUS **meropenem 2 g IV q8h** (or doripenem 500 mg IV q8h)
- PLUS **linezolid 600 mg IV q12h** (CNS penetration for meningitis)
- **Anthrax antitoxin:** raxibacumab 40 mg/kg IV or obiltoxaximab 16 mg/kg IV — request through CDC
- **Duration:** 14-21 days IV, then complete 60-day PO course (ciprofloxacin 500 mg PO BID or doxycycline 100 mg PO BID)

### Pneumonic Plague
- **Gentamicin 5 mg/kg IV q24h** (first-line)
- OR **streptomycin 1 g IM q12h** (historical gold standard; limited availability)
- OR **ciprofloxacin 400 mg IV q8h** or **doxycycline 100 mg IV q12h**
- **Duration:** 10-14 days
- **Droplet precautions** — person-to-person transmission

### Botulism
- **Botulinum antitoxin (BAT):** request from CDC Emergency Operations Center (770-488-7100)
- Administer as soon as possible — halts progression but does not reverse existing paralysis
- **Supportive care:** mechanical ventilation for respiratory failure (may need weeks-months)
- **Do NOT give aminoglycosides** (worsen neuromuscular blockade)

### Smallpox
- **Tecovirimat (TPOXX) 600 mg PO BID x 14 days** (FDA-approved; available from SNS)
- **Cidofovir 5 mg/kg IV weekly** (alternative; nephrotoxic)
- **Post-exposure vaccination** with ACAM2000 (live vaccinia) within 3-4 days of exposure
- **Airborne + contact isolation** — strict
- **Vaccinia immune globulin (VIG):** for immunocompromised patients

### Mass Post-Exposure Prophylaxis (PEP)
- **Anthrax PEP:** ciprofloxacin 500 mg PO BID x 60 days OR doxycycline 100 mg PO BID x 60 days + anthrax vaccine (3 doses)
- **Plague PEP:** doxycycline 100 mg PO BID x 7 days or ciprofloxacin 500 mg PO BID x 7 days
- **Pediatric anthrax PEP:** ciprofloxacin 15 mg/kg PO BID (max 500 mg) x 60 days
- **Pregnant women:** ciprofloxacin is acceptable for anthrax PEP (benefit outweighs risk)

## Disposition

- **Confirmed or suspected Category A agent:** admission; isolation per agent-specific requirements
- **Inhalational anthrax:** ICU admission (high mortality, rapid deterioration)
- **Pneumonic plague:** isolation ward; ICU if respiratory failure
- **Botulism:** ICU for airway monitoring and mechanical ventilation
- **Smallpox:** airborne isolation room (negative pressure); contact public health for designated smallpox treatment facility
- **Exposed but asymptomatic:** discharge on PEP with daily public health check-ins; mass dispensing site coordination
- **Transfer:** to designated biocontainment facility if viral hemorrhagic fever (4 national facilities in US)

## Pitfalls

1. **Failing to recognize the epidemiologic pattern.** Multiple patients with rapidly fatal pneumonia or mediastinal widening in the absence of trauma should trigger bioterrorism consideration. A single case of inhalational anthrax or smallpox in the modern era is bioterrorism until proven otherwise.

2. **Delaying public health notification.** The ED physician's role is recognition and notification. Do NOT attempt to confirm the diagnosis before calling public health. Early notification triggers Strategic National Stockpile deployment and mass prophylaxis — which saves thousands of lives.

3. **Sending samples to the standard hospital lab without warning.** Some agents (Francisella, Yersinia pestis) pose a risk to lab workers under standard BSL-2 conditions. Alert the lab to the clinical suspicion so they can implement enhanced precautions or divert to a Laboratory Response Network (LRN) facility.

4. **Not starting empiric antibiotics because the diagnosis is unconfirmed.** Inhalational anthrax has 45% mortality WITH treatment and near 100% without. Pneumonic plague has > 90% mortality if antibiotics are delayed > 24 hours. Treat empirically based on clinical and epidemiologic suspicion.

5. **Mistaking smallpox for varicella.** Smallpox lesions are synchronous (all at the same stage), centrifugal (more on face/extremities than trunk), and deep-seated. Varicella lesions are asynchronous (different stages simultaneously), centripetal (trunk-predominant), and superficial. In a mass event, this distinction determines quarantine of millions.
