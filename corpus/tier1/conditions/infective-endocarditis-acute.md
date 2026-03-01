---
id: infective-endocarditis-acute
condition: Acute Infective Endocarditis
aliases: [IE, bacterial endocarditis, acute IE, subacute bacterial endocarditis, SBE]
icd10: [I33.0, I33.9]
esi: 2
time_to_harm:
  irreversible_injury: "< 24 hours (embolic stroke, valve destruction)"
  death: "< 48 hours (septic shock, acute valve failure)"
  optimal_intervention_window: "< 1 hour for antibiotics"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2015 AHA Scientific Statement: Infective Endocarditis in Adults — Diagnosis, Antimicrobial Therapy, and Management of Complications. Circulation. 2015;132(15):1435-1486."
  - type: guideline
    ref: "2023 ESC Guidelines for the Management of Endocarditis. Eur Heart J. 2023;44(39):3948-4042."
  - type: review
    ref: "Cahill TJ, et al. Infective Endocarditis. Lancet. 2016;387(10021):882-893."
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
# Acute Infective Endocarditis

## Recognition

**Classic presentation (may be absent in up to 50%):**
- Fever (90%) — may be absent in elderly, immunocompromised, or partially treated patients
- New or changed cardiac murmur (85%) — regurgitant murmur (mitral > aortic)
- Embolic phenomena: stroke, splenic infarct, renal infarct, septic pulmonary emboli (right-sided IE)

**Peripheral stigmata:**
- Janeway lesions (painless erythematous lesions on palms/soles — septic emboli)
- Osler nodes (painful nodules on fingers/toes — immune complex)
- Splinter hemorrhages (linear hemorrhages in nail beds)
- Roth spots (retinal hemorrhages with pale center)
- Petechiae (conjunctival, oral mucosa, skin)

**Acute vs subacute:**
- **Acute IE:** S. aureus — high fevers, rapid valve destruction, septic shock, days to onset
- **Subacute IE:** Viridans streptococci, enterococci — insidious onset over weeks, constitutional symptoms

**Risk factors:**
- IV drug use (tricuspid valve, S. aureus — right-sided IE)
- Prosthetic heart valves
- Prior IE
- Structural heart disease (bicuspid aortic valve, MVP with MR)
- Poor dentition, recent dental procedures
- Healthcare exposure (indwelling catheters, hemodialysis)

**Modified Duke Criteria:**
- 2 major, or 1 major + 3 minor, or 5 minor = definite IE
- Major: positive blood cultures (typical organisms), positive echocardiography (vegetation, abscess, new dehiscence)
- Minor: predisposing condition, fever > 38°C, vascular phenomena, immunologic phenomena, suggestive blood cultures

## Critical Actions

| Action | Target |
|---|---|
| Blood cultures (3 sets) | < 30 minutes |
| Empiric antibiotics | Within 1 hour of suspected diagnosis |
| Echocardiography | < 12 hours (TEE preferred) |
| Cardiac surgery consultation | Within 24 hours |

1. **Obtain 3 sets of blood cultures from separate venipuncture sites** within 30 minutes — BEFORE antibiotics (unless hemodynamically unstable)
2. **Empiric antibiotics immediately after cultures:**
   - **Native valve:** Vancomycin 15-20 mg/kg IV q8-12h (target trough 15-20 mcg/mL) + ceftriaxone 2 g IV q12h
   - **Prosthetic valve:** Vancomycin 15-20 mg/kg IV q8-12h + gentamicin 1 mg/kg IV q8h + rifampin 300 mg PO q8h
   - **IVDU/right-sided:** Vancomycin 15-20 mg/kg IV q8-12h (cover MRSA) ± ceftriaxone 2 g IV q12h
3. **Echocardiography** — TEE preferred over TTE for superior sensitivity (sensitivity: TEE 95% vs TTE 60%). TTE acceptable as initial study if TEE not immediately available.
4. **Cardiac surgery consultation** within 24 hours — assess for surgical indications
5. **ID consultation** — mandatory for all IE cases to guide antimicrobial therapy

## Differential Diagnosis

- **Bacteremia without endocarditis** — may have positive cultures but no valve involvement on echo
- **Nonbacterial thrombotic endocarditis (marantic endocarditis)** — cancer, SLE, antiphospholipid syndrome
- **Rheumatic fever** — migratory polyarthritis, younger patients, strep pharyngitis history
- **Atrial myxoma** — intracardiac mass on echo, embolic events, constitutional symptoms
- **SLE (Libman-Sacks endocarditis)** — sterile vegetations, positive ANA
- **Fever of unknown origin** — IE is a classic cause; must be excluded in any FUO with risk factors

## Workup

- **Blood cultures:** 3 sets (aerobic + anaerobic) from separate venipuncture sites. Obtain before antibiotics. If culture-negative suspected: hold antibiotics and repeat cultures; consider serology for Bartonella, Coxiella, Brucella.
- **Echocardiography:** TEE is the gold standard for IE diagnosis. Assess for vegetations, abscess, pseudoaneurysm, fistula, valve perforation, new regurgitation.
- **Labs:** CBC (anemia, leukocytosis), ESR/CRP (elevated), BMP, UA (hematuria from immune complex glomerulonephritis or emboli), RF (positive in ~50% of subacute IE), complement levels (may be low)
- **ECG:** New conduction abnormalities (PR prolongation, new LBBB) suggest perivalvular abscess — urgent surgical indication
- **CT head:** If neurologic symptoms — stroke, mycotic aneurysm, brain abscess
- **CT abdomen:** Splenic abscess, renal infarcts
- **CT chest:** Septic pulmonary emboli (right-sided IE) — multiple peripheral nodular infiltrates, cavitation

## Treatment

### Empiric Therapy (adjust when cultures result)
- **Native valve community-acquired:** Vancomycin 15-20 mg/kg IV q8-12h + ceftriaxone 2 g IV q12h
- **Prosthetic valve:** Vancomycin 15-20 mg/kg IV q8-12h + gentamicin 1 mg/kg IV q8h + rifampin 300 mg PO q8h
- **Culture-directed therapy:** De-escalate as soon as organism and susceptibilities identified

### Pathogen-Specific Therapy
- **MSSA:** Nafcillin/oxacillin 2 g IV q4h x 6 weeks (native) or + rifampin + gentamicin (prosthetic)
- **MRSA:** Vancomycin 15-20 mg/kg IV q8-12h x 6 weeks; or daptomycin 8-10 mg/kg IV daily
- **Viridans streptococci (penicillin-susceptible):** Penicillin G 12-18 million units/day IV continuous or divided q4h x 4 weeks; or ceftriaxone 2 g IV daily x 4 weeks
- **Enterococcus:** Ampicillin 2 g IV q4h + gentamicin 1 mg/kg IV q8h (or ceftriaxone 2 g IV q12h if gentamicin-intolerant)

### Surgical Indications (within 24-48 hours)
- Heart failure from valve dysfunction
- Uncontrolled infection (persistent bacteremia > 5-7 days, abscess, fistula)
- Prevention of embolism: vegetation > 10 mm with embolic event, or > 15 mm on anterior mitral leaflet
- Prosthetic valve endocarditis with dehiscence, obstruction, or abscess
- Fungal endocarditis (nearly always requires surgery)

## Disposition

- **ICU admission:** Septic shock, acute heart failure, stroke, post-operative
- **Telemetry/step-down:** Hemodynamically stable IE requiring IV antibiotics and monitoring
- **ID consultation:** Mandatory for all cases
- **Cardiac surgery consultation:** Within 24 hours for all left-sided IE
- **Transfer:** Transfer to a center with cardiac surgery capability if surgical indications present
- **Duration of therapy:** 4-6 weeks IV antibiotics (2 weeks inpatient, remainder may be outpatient in selected cases per 2023 ESC partial oral therapy pathway)

## Pitfalls

1. **Administering antibiotics before obtaining blood cultures.** Three sets of blood cultures are essential for microbiologic diagnosis and directing therapy. Premature antibiotics sterilize cultures in 36-48% of cases, leading to culture-negative endocarditis and prolonged empiric therapy. Exception: hemodynamically unstable patients should receive antibiotics immediately.

2. **Relying on TTE to exclude endocarditis.** TTE sensitivity for vegetations is only ~60% (lower for prosthetic valves and small vegetations). A negative TTE does not rule out IE. TEE (sensitivity ~95%) should be performed when clinical suspicion is moderate-to-high, in all prosthetic valves, and when TTE is non-diagnostic.

3. **Missing perivalvular abscess on ECG.** New PR prolongation or conduction abnormalities in a patient with IE strongly suggest aortic root abscess — a surgical emergency. Serial ECGs should be obtained during IE treatment.

4. **Failing to consider IE in IVDU patients with pulmonary symptoms.** Right-sided endocarditis (tricuspid valve) causes septic pulmonary emboli presenting as bilateral patchy infiltrates, cough, pleuritic chest pain, and hemoptysis — often misdiagnosed as community-acquired pneumonia. Blood cultures should be obtained in any IVDU patient with fever and pulmonary infiltrates.

5. **Discharging a patient with persistent bacteremia before excluding IE.** S. aureus bacteremia requires repeat cultures at 48-72 hours and echocardiography to exclude IE. Up to 25% of S. aureus bacteremia is complicated by endocarditis. Never discharge without documented culture clearance and echocardiography.
