---
id: sepsis
condition: Sepsis and Septic Shock
aliases: [sepsis, septic shock, severe sepsis, systemic infection, SIRS with infection]
icd10: [A41.9, R65.20, R65.21]
esi: 1
time_to_harm: "< 1 hour"
mortality_if_delayed: "7.6% increase per hour of delayed antibiotics in septic shock"
category: infectious
track: tier1
sources:
  - type: guideline
    ref: "2021 Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock"
  - type: guideline
    ref: "Sepsis-3: Third International Consensus Definitions for Sepsis and Septic Shock (2016)"
  - type: guideline
    ref: "2023 Surviving Sepsis Campaign Research Priorities"
last_updated: "2026-02-18"
compiled_by: agent
reviewed_by: null
---

# Sepsis and Septic Shock

## Recognition

### Sepsis-3 Definitions

**Sepsis:** Life-threatening organ dysfunction caused by a dysregulated host response to infection. Operationalized as suspected infection + acute increase in SOFA score >= 2.

**Septic shock:** Sepsis with persistent hypotension requiring vasopressors to maintain MAP >= 65 mmHg AND serum lactate > 2 mmol/L despite adequate volume resuscitation.

### qSOFA (Quick SOFA) - Bedside Screening
- Respiratory rate >= 22/min
- Altered mentation (GCS < 15)
- Systolic BP <= 100 mmHg
- Score >= 2 associated with poor outcomes; prompts further assessment. Not a diagnostic criterion.

### SOFA Score Components (baseline = 0 for all unless known prior dysfunction)
- PaO2/FiO2 ratio
- Platelet count
- Bilirubin
- Cardiovascular (MAP and vasopressor requirements)
- GCS
- Creatinine or urine output

### Clinical Clues by Source
| Source | Findings |
|---|---|
| Pulmonary | Cough, hypoxia, crackles, consolidation on CXR |
| Urinary | Dysuria, flank pain, pyuria, CVA tenderness |
| Abdominal | Tenderness, rigidity, distension, peritoneal signs |
| Skin/soft tissue | Cellulitis, crepitus, purulent drainage, necrotizing fasciitis |
| CNS | Meningismus, photophobia, altered mental status |
| Line-related | Erythema/purulence at catheter site, tunneled line without other source |

### High-Risk Populations
- Immunosuppressed (transplant, chemotherapy, HIV with CD4 < 200, chronic steroids)
- Extremes of age (neonates, elderly)
- Indwelling devices (central lines, urinary catheters, prosthetic joints)
- Asplenic patients (encapsulated organisms: pneumococcus, meningococcus, H. influenzae)
- IV drug users (endocarditis, epidural abscess)

## Critical Actions

| Action | Target |
|---|---|
| Lactate measurement | Within 30 minutes of recognition |
| Blood cultures (2 sets) | Before antibiotics, but do NOT delay antibiotics |
| Broad-spectrum antibiotics | Within 1 hour of sepsis recognition |
| IV crystalloid 30 mL/kg | Initiate within 1 hour for hypotension or lactate >= 4 |
| Vasopressors | If MAP < 65 after initial fluid resuscitation |
| Repeat lactate | Within 2-4 hours if initial lactate elevated |

1. Obtain blood cultures (2 sets, 2 sites) immediately
2. Administer broad-spectrum antibiotics within 1 hour
3. Initiate aggressive crystalloid resuscitation (30 mL/kg for hypotension or lactate >= 4 mmol/L)
4. Measure serum lactate
5. Reassess volume status and tissue perfusion frequently
6. Start vasopressors if MAP < 65 mmHg despite fluids

## Differential Diagnosis

- Cardiogenic shock (elevated JVP, pulmonary edema, echo shows poor EF)
- Hemorrhagic shock (tachycardia, flat neck veins, identify bleeding source)
- Anaphylaxis (urticaria, angioedema, exposure history)
- Adrenal crisis (known adrenal insufficiency or chronic steroid use, hypoglycemia, hyponatremia)
- Thyroid storm (fever, tachycardia, agitation, thyroid history)
- Drug overdose/toxidrome (medication history, toxicology)
- Pancreatitis (epigastric pain, elevated lipase, imaging)
- Pulmonary embolism (pleuritic pain, hypoxia, DVT risk factors)
- Neurogenic shock (spinal cord injury, bradycardia with hypotension)

## Workup

- **Blood cultures:** 2 sets (aerobic + anaerobic) from 2 separate sites before antibiotics
- **Lactate:** STAT venous or arterial; drives resuscitation targets
- **CBC with differential:** Leukocytosis, leukopenia, bandemia, thrombocytopenia
- **BMP:** Creatinine (AKI), glucose, electrolytes (anion gap acidosis)
- **Hepatic function panel:** Bilirubin, transaminases (hepatic dysfunction in SOFA)
- **Coagulation studies:** PT/INR, aPTT, fibrinogen (DIC screening)
- **Procalcitonin:** Supports bacterial etiology; useful for antibiotic de-escalation (not for initial decision)
- **Urinalysis and urine culture**
- **Chest X-ray:** Pneumonia, ARDS
- **CT abdomen/pelvis with IV contrast** if intra-abdominal source suspected
- **Lumbar puncture** if meningitis/encephalitis suspected (after CT if indicated)
- **Point-of-care ultrasound:** IVC collapsibility for volume assessment, cardiac function, lung B-lines, free fluid

## Treatment

### Empiric Antibiotics (administer within 1 hour)

**Community-acquired, unknown source:**
- Vancomycin 25-30 mg/kg IV (actual body weight; loading dose) PLUS
- Piperacillin-tazobactam 4.5 g IV q6h (extended infusion over 4 hours preferred)
- OR cefepime 2 g IV q8h + metronidazole 500 mg IV q8h as alternative

**Healthcare-associated / immunocompromised:**
- Vancomycin 25-30 mg/kg IV PLUS
- Meropenem 1 g IV q8h (or 2 g q8h if critically ill/CNS infection)
- Add micafungin 100 mg IV daily if candidemia risk (TPN, abdominal surgery, prolonged ICU, broad-spectrum antibiotics)

**Suspected meningitis:**
- Vancomycin 25-30 mg/kg IV PLUS
- Ceftriaxone 2 g IV q12h PLUS
- Ampicillin 2 g IV q4h (if age > 50 or immunocompromised, for Listeria coverage)
- Dexamethasone 0.15 mg/kg IV q6h x 4 days (give BEFORE or WITH first antibiotic dose)

**Suspected necrotizing fasciitis:**
- Vancomycin 25-30 mg/kg IV PLUS
- Piperacillin-tazobactam 4.5 g IV q6h PLUS
- Clindamycin 900 mg IV q8h (toxin suppression)
- EMERGENT surgical consultation for debridement

**Neutropenic fever (ANC < 500):**
- Cefepime 2 g IV q8h or meropenem 1 g IV q8h
- Add vancomycin if hemodynamically unstable, skin/catheter infection suspected, or MRSA colonized

### Fluid Resuscitation
- Balanced crystalloid (lactated Ringer's) preferred over normal saline (SSC 2021 weak recommendation)
- 30 mL/kg within first 3 hours for hypotension or lactate >= 4 mmol/L
- Reassess after each 500 mL bolus with POCUS (IVC, lung, cardiac)
- Avoid albumin as first-line; may consider if substantial crystalloid already given

### Vasopressors
- **Norepinephrine:** First-line, 0.1-0.5 mcg/kg/min IV (titrate to MAP >= 65)
- **Vasopressin:** 0.03 units/min IV (fixed dose), add as second agent when norepinephrine 0.25-0.5 mcg/kg/min insufficient
- **Epinephrine:** 0.1-0.5 mcg/kg/min IV, add as third-line or if cardiac dysfunction prominent
- **Phenylephrine:** Avoid; associated with splanchnic vasoconstriction and worse outcomes in sepsis
- **Peripheral vasopressors:** Acceptable via large-bore peripheral IV for up to 24 hours while obtaining central access

### Corticosteroids
- **Hydrocortisone 50 mg IV q6h** if vasopressor-refractory shock (escalating doses despite adequate fluids)
- Duration: typically 7 days, then taper or stop when vasopressors discontinued
- Do NOT use dexamethasone for septic shock (does not provide mineralocorticoid activity)

### Source Control
- Drain abscesses (percutaneous or surgical)
- Remove infected devices (central lines, prostheses)
- Debride necrotic tissue
- Decompress obstructed viscus (biliary, urinary)
- Goal: within 6-12 hours of identification; sooner if necrotizing fasciitis or bowel perforation

### Resuscitation Targets
- MAP >= 65 mmHg
- Lactate clearance (decreasing trend; re-measure at 2-4 hours)
- Urine output >= 0.5 mL/kg/hr
- Capillary refill < 3 seconds
- Improving mental status

## Disposition

- **Septic shock:** ICU admission, arterial line for continuous BP monitoring, central venous access
- **Sepsis with organ dysfunction but hemodynamically stable:** ICU or step-down depending on vasopressor needs and respiratory status
- **Sepsis without shock, responding to fluids:** Monitored floor bed; reassess within 6 hours
- **Low-risk sepsis (responsive to initial fluids, lactate normalizing, identified source):** May observe in ED with serial reassessment before floor admission
- **Never discharge a patient with sepsis from the ED.** Even those appearing well after initial resuscitation can deteriorate rapidly.

## Pitfalls

1. **Delaying antibiotics to obtain cultures.** Draw cultures, then immediately administer antibiotics. Never wait for culture results, LP results, or imaging before giving antibiotics in septic shock.

2. **Using qSOFA as a diagnostic tool rather than a screening tool.** A qSOFA < 2 does NOT exclude sepsis. It was designed for bedside prognostication, not diagnosis. Use clinical judgment and SOFA scoring.

3. **Attributing altered mental status to "baseline" in elderly patients.** Acute confusion is an organ dysfunction marker. Assume sepsis until proven otherwise in elderly patients with altered mentation and any infection risk.

4. **Over-resuscitating with crystalloid without reassessing.** Fluid overload worsens outcomes, especially in ARDS. Reassess with POCUS after every 500-1000 mL. Start vasopressors early if MAP remains < 65 despite 1-2 L.

5. **Failing to identify and control the source.** Antibiotics alone will not resolve undrained abscesses, obstructed viscera, or necrotizing infections. Imaging and surgical consultation are part of first-hour management when source is uncertain.

6. **Not considering occult sources in patients with negative initial workup.** Endocarditis, epidural abscess, prosthetic joint infection, and C. difficile colitis may not be apparent on initial evaluation. Broaden the search when cultures are negative and the patient is not improving.

7. **Underdosing vancomycin.** Use actual body weight for the loading dose (25-30 mg/kg). A 100 kg patient needs 2.5-3 g, not the traditional 1 g.
