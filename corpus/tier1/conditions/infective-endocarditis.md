---
id: infective-endocarditis
condition: Infective Endocarditis
aliases: [IE, bacterial endocarditis, subacute bacterial endocarditis, SBE, acute endocarditis, prosthetic valve endocarditis, PVE]
icd10: [I33.0, I33.9]
esi: 2
time_to_harm: "< 24-72 hours (embolic events, valve destruction, heart failure)"
mortality_if_delayed: "In-hospital mortality 15-30%; S. aureus IE mortality 25-47% with delayed diagnosis"
category: infectious
track: tier1
sources:
  - type: guideline
    ref: "Baddour LM, Wilson WR, Bayer AS, et al. Infective Endocarditis in Adults: Diagnosis, Antimicrobial Therapy, and Management of Complications: A Scientific Statement From the American Heart Association. Circulation. 2015;132(15):1435-1486"
    pmid: "26373316"
  - type: review
    ref: "Cahill TJ, Prendergast BD. Infective endocarditis. Lancet. 2016;387(10021):882-893"
    pmid: "26341945"
  - type: pubmed
    ref: "Murdoch DR, Corey GR, Hoen B, et al. Clinical Presentation, Etiology, and Outcome of Infective Endocarditis in the 21st Century: The International Collaboration on Endocarditis-Prospective Cohort Study. Arch Intern Med. 2009;169(5):463-473"
    pmid: "19273776"
  - type: pubmed
    ref: "Li JS, Sexton DJ, Mick N, et al. Proposed Modifications to the Duke Criteria for the Diagnosis of Infective Endocarditis. Clin Infect Dis. 2000;30(4):633-638"
    pmid: "10770721"
  - type: guideline
    ref: "Fowler VG, Durack DT, Selton-Suty C, et al. The 2023 Duke-ISCVID Criteria for Infective Endocarditis: Updating the Modified Duke Criteria. Clin Infect Dis. 2023;77(4):518-526"
    pmid: "37138445"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: B
validation:
  automated_consistency_check: "2026-02-27"
  dose_range_validator: "2026-02-27"
  unit_normalization_check: "2026-02-27"
  cross_file_consistency_check: "2026-02-27"
  citation_presence_check: "2026-02-27"
  duplicate_content_check: "2026-02-27"
  outlier_detection_flag: clear
  schema_version: "2.0"
  provenance_links: []
---
# Infective Endocarditis

## Recognition

**Definition:** Infection of the endocardial surface of the heart, most commonly involving native or prosthetic heart valves. Caused by bacteria (or rarely fungi) that seed damaged endothelium and form infected vegetations.

**The diagnostic challenge:** IE is frequently missed on initial ED visits. Mean time from symptom onset to diagnosis is 2-5 weeks. Patients present with nonspecific symptoms (fever, malaise, weight loss) and are often treated for other diagnoses before IE is considered.

### Clinical Presentation

**Acute IE (S. aureus):**
- Abrupt onset, high fever, rigors, rapidly progressive
- Rapid valve destruction, septic emboli, heart failure within days
- Often affects normal valves

**Subacute IE (S. viridans, HACEK):**
- Insidious onset over weeks to months
- Low-grade fever, night sweats, weight loss, fatigue, arthralgias
- Often misdiagnosed as viral illness, malignancy, or autoimmune disease

**Symptoms and Signs:**
- Fever (80-90%) — may be absent in elderly, immunocompromised, or partially treated
- New or changing cardiac murmur (48-85%) — new regurgitant murmur is highly specific
- Embolic phenomena (20-50%): stroke, splenic infarct, renal infarct, septic pulmonary emboli (right-sided IE)
- Splenomegaly (15-50%)
- Petechiae (10-40%): conjunctival, oral mucosa, extremities
- Splinter hemorrhages: linear subungual hemorrhages
- Osler nodes: tender nodules on finger/toe pads (immune complex-mediated, uncommon)
- Janeway lesions: painless erythematous/hemorrhagic macules on palms and soles (septic microemboli)
- Roth spots: retinal hemorrhages with pale centers (rare)

### Microbiology

| Organism | Frequency | Clinical Context |
|----------|-----------|-----------------|
| S. aureus | 30-40% (most common overall) | Acute native valve, IVDU, healthcare-associated, prosthetic valve |
| Viridans group streptococci | 17-20% | Subacute native valve, poor dentition, dental procedures |
| Enterococcus spp. | 10-15% | GU/GI procedures, elderly, healthcare-associated |
| Coagulase-negative staphylococci | 8-12% | Prosthetic valve (early), cardiac devices |
| HACEK group | 2-3% | Subacute, large vegetations, culture-negative initially (slow-growing) |
| Fungi (Candida, Aspergillus) | 1-2% | Prosthetic valve, IVDU, immunocompromised, central lines |
| Culture-negative | 5-10% | Prior antibiotic use, fastidious organisms (Bartonella, Coxiella, Tropheryma whipplei) |

### Risk Factors

- **Prosthetic heart valve** — highest individual risk; early (<60 days) vs. late
- **IV drug use** — right-sided IE (tricuspid valve 70-85%), S. aureus predominant
- **Prior IE** — recurrence rate 2-6% per year
- **Structural heart disease:** rheumatic heart disease, bicuspid aortic valve, mitral valve prolapse with regurgitation
- **Congenital heart disease** — particularly cyanotic lesions, unrepaired VSD
- **Poor dentition/recent dental procedures**
- **Cardiac implantable electronic devices** (pacemakers, ICDs)
- **Healthcare exposure:** central venous catheters, hemodialysis, recent surgery
- **Degenerative valve disease** in elderly patients (increasing epidemiology)

### Modified Duke Criteria (2023 Duke-ISCVID Update)

**Definite IE:** 2 major criteria, OR 1 major + 3 minor, OR 5 minor

**Possible IE:** 1 major + 1 minor, OR 3 minor

**Major Criteria:**
1. **Positive blood cultures:**
   - Typical IE organism from 2 separate cultures (S. aureus, viridans streptococci, S. gallolyticus, HACEK, Enterococcus without primary focus)
   - Persistently positive cultures: 2 cultures drawn >12 hours apart, OR all of 3 or majority of >=4 cultures positive (first and last drawn >=1 hour apart)
   - Single positive culture for Coxiella burnetii or anti-phase I IgG titer >1:800
2. **Evidence of endocardial involvement:**
   - Echocardiography: vegetation, abscess, pseudoaneurysm, intracardiac fistula, valvular perforation, new partial dehiscence of prosthetic valve
   - Cardiac CT: vegetation, abscess, pseudoaneurysm, intracardiac fistula, valvular perforation, new dehiscence of prosthetic valve
   - 18F-FDG PET/CT: abnormal metabolic activity involving native or prosthetic valve or ascending aortic graft (>3 months postoperative)
   - New valvular regurgitation (change in existing murmur not sufficient)

**Minor Criteria:**
1. Predisposing condition: prosthetic valve, prior IE, cardiac device, congenital heart disease, valvulopathy, IVDU
2. Fever >= 38.0 C
3. Vascular phenomena: major arterial emboli, septic pulmonary infarcts, mycotic aneurysm, intracranial hemorrhage, conjunctival hemorrhage, Janeway lesions
4. Immunologic phenomena: glomerulonephritis, Osler nodes, Roth spots, positive rheumatoid factor
5. Microbiologic evidence not meeting major criterion

## Critical Actions

1. **Draw 3 sets of blood cultures from separate venipuncture sites** BEFORE starting antibiotics. Cultures should be drawn regardless of presence or absence of fever. At least 2 sets must be drawn; 3 sets detect >96% of bacteremias.
2. **Do NOT delay antibiotics in hemodynamically unstable or acutely ill patients.** Draw cultures and start empiric therapy simultaneously in septic or acutely decompensating patients.
3. **Obtain transthoracic echocardiography (TTE) urgently.** If TTE is negative or inadequate and clinical suspicion remains, transesophageal echocardiography (TEE) is required (sensitivity 90-95% vs. 50-70% for TTE).
4. **Assess for embolic complications:** Focused neurological exam for stroke; CT head if any neurological symptoms; CT abdomen for splenic/renal infarcts if abdominal pain.
5. **Consult cardiology and infectious disease early.** Both are standard of care. Surgical consultation if any complications (see Treatment).
6. **Evaluate for heart failure** — auscultate for new murmur, assess for pulmonary edema, obtain BNP. Heart failure is the leading indication for surgery and primary cause of death.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Sepsis/bacteremia without endocarditis | No vegetation on echo, cultures clear with source control, no new murmur |
| Rheumatic fever | Jones criteria, antecedent streptococcal pharyngitis, younger patients, negative blood cultures |
| Atrial myxoma | Tumor on echo (not vegetation), no fever/bacteremia, positional symptoms |
| Nonbacterial thrombotic endocarditis (marantic) | Associated with malignancy/hypercoagulability, sterile vegetations, negative cultures |
| Libman-Sacks endocarditis | SLE/antiphospholipid syndrome, sterile vegetations, negative cultures |
| Systemic vasculitis (PAN, GPA) | ANCA positive, multi-organ involvement, negative cultures, biopsy diagnostic |
| Occult malignancy (lymphoma) | B symptoms overlap, negative cultures, imaging/biopsy distinguish |
| Fever of unknown origin | IE is on the differential for FUO; blood cultures and echo are standard FUO workup |

## Workup

**Blood Cultures (critical — draw before antibiotics):**
- 3 sets (aerobic + anaerobic) from 3 separate venipuncture sites
- Draw regardless of fever status — bacteremia in IE is continuous, not paroxysmal
- At least 10 mL per bottle (yield increases with volume)
- If patient already on antibiotics: hold antibiotics for 48 hours if clinically safe, then re-culture. If not safe to hold, draw cultures anyway — they may still be positive.

**Echocardiography:**
- **TTE first:** Sensitivity 50-70% for native valve, 30-50% for prosthetic valve. Adequate initial screening in native valve with low clinical suspicion.
- **TEE required if:** TTE negative with moderate-high clinical suspicion, prosthetic valve, cardiac device, suspected abscess/fistula, or poor TTE acoustic windows.
- TEE sensitivity 90-95%, specificity 90%.
- Repeat echo in 5-7 days if initial study negative and suspicion persists.

**Laboratory:**
- CBC with differential (leukocytosis, anemia of chronic disease in subacute IE)
- BMP (creatinine — renal infarct, glomerulonephritis, drug dosing)
- Hepatic panel
- ESR and CRP (elevated in >90%; useful for monitoring treatment response)
- Urinalysis (microscopic hematuria in 30-50% from immune complex glomerulonephritis or renal emboli)
- Rheumatoid factor (positive in 25-50% of subacute IE)
- Procalcitonin
- Lactate
- BNP/NT-proBNP (heart failure assessment)
- Coagulation studies (DIC screening in acute IE)

**Imaging Beyond Echo:**
- CT head without contrast: if any neurological symptoms (stroke occurs in 20-40% of left-sided IE)
- CT abdomen with contrast: splenic abscess/infarct, renal infarct if abdominal pain
- CT chest: septic pulmonary emboli in right-sided IE (multiple peripheral nodular infiltrates, cavitation)
- Cardiac CT with ECG gating: emerging role for abscess, pseudoaneurysm, and prosthetic valve assessment
- 18F-FDG PET/CT: prosthetic valve/device IE diagnosis (now a major Duke-ISCVID criterion)

## Treatment

### Empiric Antibiotic Therapy (start after blood cultures drawn)

**Native valve, community-acquired:**
- **Vancomycin** 25-30 mg/kg IV loading dose (actual body weight), then 15-20 mg/kg IV q8-12h (target AUC/MIC 400-600)
- PLUS **ceftriaxone** 2 g IV q12h
- Covers MRSA, MSSA, streptococci, enterococci, and HACEK

**Native valve, IVDU (right-sided suspected):**
- **Vancomycin** 25-30 mg/kg IV loading dose, then 15-20 mg/kg IV q8-12h
- PLUS **ceftriaxone** 2 g IV q12h
- If septic and Pseudomonas considered: substitute **cefepime** 2 g IV q8h for ceftriaxone

**Prosthetic valve (early, <1 year):**
- **Vancomycin** 25-30 mg/kg IV loading dose, then 15-20 mg/kg IV q8-12h
- PLUS **gentamicin** 1 mg/kg IV q8h (synergy dosing; monitor levels and renal function)
- PLUS **rifampin** 300-450 mg PO/IV q8h (add after blood cultures clear — rifampin in active bacteremia may worsen outcomes)

**Prosthetic valve (late, >1 year):**
- Treat as native valve empiric regimen initially
- Adjust based on culture results

**Culture-negative IE:**
- Maintain empiric regimen
- Send serologies: Bartonella (IgG), Coxiella burnetii (phase I and II), Brucella, Legionella
- Consider 16S rRNA PCR on blood or valve tissue

### Pathogen-Directed Therapy (after culture and sensitivity)

| Organism | Regimen | Duration |
|----------|---------|----------|
| Viridans streptococci (PCN MIC <=0.12) | Penicillin G 12-18 million units/day IV continuous or q4h, OR ceftriaxone 2 g IV q24h | 4 weeks (native); 6 weeks (prosthetic) |
| Viridans streptococci (PCN MIC 0.12-0.5) | Penicillin G or ceftriaxone (above doses) PLUS gentamicin 3 mg/kg IV q24h x 2 weeks | 4 weeks |
| S. aureus (MSSA), native valve | Nafcillin or oxacillin 2 g IV q4h | 6 weeks |
| S. aureus (MRSA), native valve | Vancomycin 15-20 mg/kg IV q8-12h (AUC/MIC 400-600), OR daptomycin 8-10 mg/kg IV q24h | 6 weeks |
| S. aureus, prosthetic valve | Vancomycin (or nafcillin if MSSA) PLUS rifampin 300 mg PO q8h PLUS gentamicin 1 mg/kg IV q8h x 2 weeks | >=6 weeks |
| Enterococcus (ampicillin-susceptible) | Ampicillin 2 g IV q4h PLUS gentamicin 1 mg/kg IV q8h (or ceftriaxone 2 g IV q12h for double beta-lactam) | 4-6 weeks |
| HACEK organisms | Ceftriaxone 2 g IV q24h | 4 weeks (native); 6 weeks (prosthetic) |

### Surgical Indications (consult cardiac surgery early)

**Emergent/urgent surgery indicated for:**
- **Heart failure** from valvular regurgitation (most common surgical indication — reduces mortality from 50-80% to 10-25%)
- **Periannular abscess, fistula, or pseudoaneurysm** — antibiotics alone cannot eradicate
- **Persistent bacteremia** >5-7 days despite appropriate antibiotics and source control
- **Large mobile vegetation >10 mm** with embolic event — or >15 mm even without embolism (risk of further embolization)
- **Fungal endocarditis** (Candida, Aspergillus) — medical cure exceedingly rare
- **Prosthetic valve dehiscence or instability**
- **Recurrent emboli** despite appropriate therapy

**Timing considerations:**
- Surgery should not be delayed for completion of antibiotic course when there is a surgical indication
- Embolic stroke is NOT an absolute contraindication to surgery if no hemorrhagic conversion (may proceed after 72 hours if hemorrhage excluded by repeat CT)
- Hemorrhagic stroke: delay surgery at least 4 weeks

## Disposition

**ICU Admission:**
- Septic shock or hemodynamic instability
- Acute heart failure (flash pulmonary edema, cardiogenic shock)
- Acute embolic stroke with neurological deficit
- Ruptured mycotic aneurysm
- Post-cardiac surgery

**Inpatient (Cardiology/Medicine with ID co-management):**
- All confirmed or probable IE requires admission
- IV antibiotics for 4-6 weeks (OPAT may be arranged after initial stabilization)
- Serial echocardiography to monitor vegetation size and valve function
- Daily assessment for new embolic phenomena and heart failure

**Transfer:**
- Transfer to a center with cardiothoracic surgery capability if surgical indications exist and not available at current facility. Do not delay antibiotics for transfer.

**Discharge:**
- IE is NOT a discharge diagnosis from the ED
- If IE is suspected but not yet confirmed, admission for blood cultures and echocardiography is standard. Do not discharge and arrange "outpatient echo."

**Follow-Up (post-treatment):**
- Repeat echocardiography at completion of therapy to establish new baseline
- Blood cultures after 4-6 days of treatment to document clearance
- Dental evaluation for all patients to eliminate oral sources
- Long-term follow-up for relapse (highest risk in first 2 months)

## Pitfalls

1. **Failing to consider IE in patients with fever of unknown origin.** IE is a classic cause of FUO. Any patient with prolonged fever, new murmur, or embolic phenomena should have blood cultures and echocardiography. The diagnosis is frequently delayed by 2-5 weeks because clinicians do not include it early in the differential.

2. **Drawing blood cultures only once or from a single site.** A single set of cultures misses 5-20% of bacteremias. Three sets from separate venipuncture sites detect >96% of causative organisms. Volume matters — draw at least 10 mL per bottle. Insufficient culture technique leads to culture-negative IE and diagnostic uncertainty.

3. **Relying on TTE alone to exclude IE.** TTE sensitivity is 50-70% for native valve and 30-50% for prosthetic valve vegetations. A negative TTE does not rule out IE. TEE (sensitivity 90-95%) is mandatory when TTE is negative and clinical suspicion is moderate-to-high, for prosthetic valves, for cardiac devices, and when abscess is suspected.

4. **Missing right-sided IE in IVDU patients presenting with respiratory complaints.** Tricuspid valve IE produces septic pulmonary emboli, not left-sided systemic emboli. Patients present with cough, pleuritic chest pain, hemoptysis, and multiple peripheral lung nodules on CT — often misdiagnosed as pneumonia. Any febrile IVDU patient with bilateral pulmonary infiltrates has right-sided IE until proven otherwise.

5. **Anchoring on "negative cultures" in a patient already on antibiotics.** Prior antibiotic exposure (even a single dose of oral antibiotics from urgent care) can sterilize blood cultures. Culture-negative endocarditis occurs in 5-10% of cases. If clinical suspicion persists despite negative cultures, obtain serologies for fastidious organisms (Bartonella, Coxiella), request prolonged incubation, and consider 16S rRNA PCR on blood or excised valve tissue.

6. **Delaying surgical consultation until the patient is "failing" medical therapy.** Heart failure from valvular destruction is the primary cause of death in IE, and early surgery reduces mortality. Cardiac surgery should be consulted at the time of diagnosis in any patient with moderate-severe regurgitation, large vegetation, abscess, or prosthetic valve involvement — not after clinical deterioration.

7. **Attributing neurological symptoms to other causes without imaging.** Embolic stroke occurs in 20-40% of left-sided IE and may be the presenting symptom. Any patient with IE and new headache, focal deficit, visual change, or altered mentation requires urgent CT head. Mycotic aneurysm rupture causes subarachnoid or intracerebral hemorrhage and is rapidly fatal without intervention. CT angiography or MRA should follow if hemorrhage is found.

8. **Discharging a patient with persistent S. aureus bacteremia without echocardiography.** S. aureus bacteremia has a 25-30% prevalence of occult IE. All patients with S. aureus bloodstream infection require echocardiography (TEE preferred). Discharging with planned "outpatient follow-up cultures" without ruling out endocarditis risks missing the diagnosis during the window when complications are preventable.

9. **Underappreciating the embolic risk of large vegetations.** Vegetations >10 mm carry a 2-3x higher embolization rate, and the risk is highest in the first 2 weeks of antibiotic therapy. Surgery to prevent embolization is recommended for vegetations >10 mm with a prior embolic event and should be discussed for vegetations >15 mm regardless of symptoms. Waiting until embolization occurs (e.g., embolic stroke) to consider surgery sacrifices the prevention window.
