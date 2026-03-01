---
id: spontaneous-bacterial-peritonitis
condition: Spontaneous Bacterial Peritonitis
aliases: [SBP, primary peritonitis, ascitic fluid infection]
icd10: [K65.2]
esi: 2
time_to_harm: "< 6-12 hours (mortality increases 3.3% per hour of delayed paracentesis)"
category: gastrointestinal
track: tier1
sources:
  - type: guideline
    ref: "AASLD Practice Guidance: Portal Hypertensive Bleeding in Cirrhosis, Hepatology 2022;76(1):252-273"
  - type: review
    ref: "Emergency Management of Spontaneous Bacterial Peritonitis — A Clinical Review, Turk J Emerg Med 2017;17(1):8-13"
  - type: guideline
    ref: "EASL Clinical Practice Guidelines: Management of Patients with Decompensated Cirrhosis, J Hepatol 2018;69(2):406-460"
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
# Spontaneous Bacterial Peritonitis

## Recognition

**Presentation:**
- Cirrhotic patient with ascites presenting with any of:
  - Abdominal pain or tenderness (present in ~75%)
  - Fever (> 38°C in 50-80%)
  - Altered mental status (worsening hepatic encephalopathy)
  - Unexplained clinical deterioration
- May be asymptomatic (up to 30% of cases) — diagnose on paracentesis

**High-risk populations:**
- Prior SBP episode (70% 1-year recurrence without prophylaxis)
- Ascitic fluid protein < 1.5 g/dL
- GI hemorrhage in cirrhotic patient
- Child-Pugh C cirrhosis (MELD > 15)
- Hospitalized cirrhotic with any acute decompensation

**Exam findings:**
- Abdominal distension with shifting dullness (ascites)
- Diffuse abdominal tenderness (may be subtle)
- Rebound tenderness (uncommon — peritoneal response blunted in cirrhosis)
- Signs of chronic liver disease: spider angiomata, palmar erythema, jaundice, gynecomastia

## Critical Actions

1. **Diagnostic paracentesis immediately** — do not delay for any reason; each hour delay increases mortality 3.3%
2. **Send ascitic fluid:** cell count with differential, albumin, total protein, culture (inoculate blood culture bottles at bedside — 10 mL per bottle)
3. **Diagnosis:** ascitic fluid PMN count ≥ 250 cells/mm³ = SBP; treat immediately, do not wait for cultures
4. **Start empiric antibiotics immediately after paracentesis:**
   - Community-acquired: cefotaxime 2 g IV q8h (first-line) or ceftriaxone 2 g IV daily
   - Nosocomial: piperacillin-tazobactam 4.5 g IV q6h or meropenem 1 g IV q8h
5. **IV albumin:**
   - 1.5 g/kg albumin (20%) at time of diagnosis
   - 1 g/kg albumin (20%) at 48 hours
   - Prevents hepatorenal syndrome, reduces mortality by 30%
6. **Hold beta-blockers** — carvedilol and propranolol worsen hemodynamics in SBP
7. **Avoid nephrotoxic agents** — no NSAIDs, aminoglycosides, or IV contrast
8. **Repeat paracentesis at 48 hours** to confirm PMN decrease ≥ 25%

## Differential Diagnosis

- **Secondary bacterial peritonitis** — polymicrobial on culture, ascitic protein > 1 g/dL, glucose < 50 mg/dL, LDH > ULN; requires imaging to identify surgical source (perforated viscus, abscess)
  - Runyon criteria for secondary: 2 of 3 (protein > 1, glucose < 50, LDH > ULN)
- **Malignant ascites with peritoneal carcinomatosis** — cytology positive, elevated CEA/CA-125 in ascitic fluid
- **Tuberculous peritonitis** — lymphocyte-predominant ascitic fluid, adenosine deaminase elevated, AFB culture
- **Pancreatic ascites** — elevated amylase in ascitic fluid (> 1000 U/L), history of pancreatitis
- **Chylous ascites** — milky fluid, triglycerides > 200 mg/dL

## Workup

- **Diagnostic paracentesis (mandatory):**
  - Ascitic fluid PMN count ≥ 250 cells/mm³ = SBP
  - Culture: inoculate at bedside into aerobic and anaerobic blood culture bottles (10 mL each)
  - Ascitic fluid albumin and total protein
  - Ascitic fluid glucose, LDH (if secondary peritonitis suspected)
  - Gram stain (low sensitivity ~25%)
- **Common organisms:** E. coli (40%), Klebsiella (10-15%), Streptococcus pneumoniae (10%), Enterococcus
- **Labs:** CBC, BMP (creatinine — baseline for hepatorenal syndrome), hepatic panel, INR, lactate, blood cultures (x2 sets)
- **Coagulopathy does NOT contraindicate paracentesis** — risk of bleeding is < 0.5% even with INR > 2 or platelets < 50,000
- **Imaging:** abdominal CT with IV contrast if secondary peritonitis suspected (abscess, perforation)

## Treatment

**Empiric antibiotics:**
- Community-acquired SBP:
  - Cefotaxime 2 g IV q8h (preferred — extensive trial data) x 5 days
  - Ceftriaxone 2 g IV daily (acceptable alternative)
  - PCN allergy: ciprofloxacin 400 mg IV q12h (avoid if on fluoroquinolone prophylaxis)
- Nosocomial or healthcare-associated SBP:
  - Piperacillin-tazobactam 4.5 g IV q6h
  - Meropenem 1 g IV q8h (if ESBL suspected)
  - Add vancomycin 15-20 mg/kg IV q12h if MRSA risk factors
- Duration: 5 days (minimum); extend if repeat paracentesis shows inadequate PMN response

**Albumin (MANDATORY — reduces mortality):**
- 1.5 g/kg (20% albumin) within 6 hours of diagnosis
- 1 g/kg (20% albumin) on day 3
- Albumin doses capped at 100 g and 67 g respectively per AASLD

**Hepatorenal syndrome prevention:**
- Albumin (as above) is the primary intervention
- Avoid nephrotoxins (aminoglycosides, NSAIDs, IV contrast)
- Monitor creatinine q12-24h
- If creatinine rises > 1.5: start albumin 1 g/kg/day + midodrine 7.5 mg PO TID + octreotide 100 mcg SC TID (hepatorenal type 1 protocol)

**SBP prophylaxis (secondary — lifelong):**
- Norfloxacin 400 mg PO daily OR trimethoprim-sulfamethoxazole DS PO daily
- Rifaximin 550 mg PO BID (alternative, emerging evidence)

## Disposition

- **Admit all patients with SBP**
- **ICU:** sepsis, hepatorenal syndrome, grade 3-4 encephalopathy, hemodynamic instability
- **Hepatology/GI consultation** for all cases
- **Transplant evaluation** — SBP is an indicator of severe portal hypertension; 1-year mortality after SBP is 30-50%
- **Repeat paracentesis at 48 hours** mandatory to confirm treatment response
- **Discharge criteria:** completing antibiotic course, PMN normalized, stable renal function, prophylaxis prescribed

## Pitfalls

1. **Delaying paracentesis.** In-hospital mortality increases 3.3% for each hour paracentesis is delayed. Any cirrhotic admitted with ascites should have paracentesis regardless of whether SBP is suspected — it is a screening procedure.

2. **Withholding paracentesis due to coagulopathy.** The risk of significant bleeding is < 0.5% even with INR > 2 or platelets < 50,000. Coagulopathy is NOT a contraindication. Do not transfuse FFP or platelets pre-procedure.

3. **Omitting albumin.** IV albumin reduces hepatorenal syndrome incidence from 33% to 10% and mortality from 29% to 10%. This is NOT optional supportive care — it is a cornerstone of SBP treatment.

4. **Missing secondary peritonitis.** If ascitic fluid shows PMN ≥ 250 with 2 of 3 Runyon criteria (protein > 1, glucose < 50, LDH > ULN), or if cultures are polymicrobial, suspect secondary peritonitis from perforation/abscess. CT and surgical consultation are mandatory.

5. **Continuing non-selective beta-blockers during SBP.** Carvedilol and propranolol worsen systemic hemodynamics in acute SBP. Hold until infection resolves and hemodynamics stabilize.

6. **Not prescribing secondary prophylaxis at discharge.** Without prophylaxis, SBP recurs in 70% within 1 year. Norfloxacin 400 mg daily or TMP-SMX DS daily is lifelong therapy.
