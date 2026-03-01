---
id: spontaneous-bacterial-peritonitis-infectious
condition: Spontaneous Bacterial Peritonitis (Infectious Focus)
aliases: [SBP, primary bacterial peritonitis, ascitic fluid infection]
icd10: [K65.2, K65.9]
esi: 2
time_to_harm: "< 24 hours (septic shock); 48-72 hours (multi-organ failure)"
category: infectious
track: tier1
sources:
  - type: guideline
    ref: "AASLD Practice Guidance: Diagnosis, Evaluation, and Management of Ascites, Spontaneous Bacterial Peritonitis and Hepatorenal Syndrome, 2021"
  - type: guideline
    ref: "EASL Clinical Practice Guidelines: Management of patients with decompensated cirrhosis, 2018"
  - type: guideline
    ref: "IDSA Practice Guidelines for the Diagnosis and Treatment of Intra-Abdominal Infections, 2024 Update"
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
# Spontaneous Bacterial Peritonitis (Infectious Focus)

## Recognition

**Presentation:**
- Fever, abdominal pain, abdominal tenderness (may be subtle in cirrhosis)
- Altered mental status, hepatic encephalopathy (may be only sign)
- Worsening ascites, ileus
- Unexplained clinical deterioration in a cirrhotic patient
- Hypothermia (in advanced cirrhosis)
- Hypotension, tachycardia

**High-risk population:**
- Cirrhosis with ascites (ascitic fluid protein < 1.5 g/dL)
- Prior SBP episode (1-year recurrence ~70%)
- Variceal hemorrhage
- Low complement levels in ascitic fluid

**Common pathogens:**
- Escherichia coli (most common)
- Klebsiella pneumoniae
- Streptococcus pneumoniae
- Enterococci
- Monomicrobial (polymicrobial suggests secondary peritonitis — surgical cause)

## Critical Actions

1. **Perform diagnostic paracentesis immediately** in any cirrhotic patient with ascites presenting with fever, abdominal pain, encephalopathy, renal failure, acidosis, or unexplained clinical deterioration
2. **Start empiric antibiotics within 1 hour** if ascitic PMN count >= 250 cells/mm3 — do NOT wait for culture results
3. **Administer IV albumin** (1.5 g/kg on day 1, 1 g/kg on day 3) — reduces hepatorenal syndrome and mortality
4. **Assess for secondary peritonitis** — polymicrobial culture, failure to respond at 48h, or surgical abdomen requires imaging and surgical consultation

## Differential Diagnosis

- Secondary bacterial peritonitis (perforated viscus) — polymicrobial, high protein, high LDH, low glucose in ascitic fluid; requires surgery
- Tuberculous peritonitis — lymphocytic predominance, high ADA (> 39 U/L)
- Peritoneal carcinomatosis — cytology positive, high protein
- Pancreatic ascites — high amylase in ascitic fluid
- Chylous ascites — milky appearance, high triglycerides
- Hepatorenal syndrome — may coexist; rising creatinine without response to volume

## Workup

- **Diagnostic paracentesis** (mandatory):
  - Cell count with differential: PMN >= 250 cells/mm3 is diagnostic
  - Ascitic fluid culture: inoculate blood culture bottles at bedside (aerobic + anaerobic, 10 mL each) — increases sensitivity from 50% to 80%
  - Total protein, albumin, glucose, LDH
  - Gram stain (low sensitivity, ~10%)
- **Blood cultures** (x2 sets) before antibiotics
- **CBC, BMP (creatinine, electrolytes), hepatic panel, coagulation studies**
- **Lactate, procalcitonin**
- **Runyon criteria for secondary peritonitis** (any 2 of: glucose < 50 mg/dL, protein > 1 g/dL, LDH > upper limit of normal for serum)
- **CT abdomen/pelvis with contrast** if secondary peritonitis suspected

## Treatment

### Empiric Antibiotics
- **First-line: Cefotaxime 2 g IV q8h** — covers > 90% of SBP isolates
- **Alternative: Ceftriaxone 2 g IV q24h** — equally effective, more convenient dosing
- **Duration:** 5 days minimum (response assessed by repeat paracentesis at 48h showing >= 25% decrease in PMN count)

**If fluoroquinolone prophylaxis failure:**
- Cefotaxime remains effective (> 90% susceptibility maintained)

**If nosocomial SBP or high ESBL risk:**
- Piperacillin-tazobactam 4.5 g IV q6h OR meropenem 1 g IV q8h
- Add vancomycin 15-20 mg/kg IV q8-12h if MRSA risk

**If penicillin allergy:**
- Ciprofloxacin 400 mg IV q12h (only if no prior fluoroquinolone prophylaxis)

### Albumin Infusion (Reduces Mortality)
- Day 1: Albumin 1.5 g/kg IV (especially if creatinine > 1 mg/dL, BUN > 30 mg/dL, or bilirubin > 4 mg/dL)
- Day 3: Albumin 1 g/kg IV

### Secondary Prophylaxis (After Recovery)
- Norfloxacin 400 mg PO daily OR trimethoprim-sulfamethoxazole DS 1 tab PO daily — indefinite in cirrhotics

## Disposition

- **Admit all SBP patients** — IV antibiotics and monitoring required
- **ICU admission** if: septic shock, hepatorenal syndrome, GI bleeding, severe encephalopathy
- **Repeat paracentesis at 48 hours** to confirm response (>= 25% PMN decrease)
- **Hepatology/GI consultation** for liver transplant evaluation if first SBP episode (1-year mortality ~30-50%)
- **Isolation:** Standard precautions
- **Reportable:** Not a reportable disease

## Pitfalls

1. **Failing to perform paracentesis in the cirrhotic patient with unexplained deterioration.** SBP may present only as worsening encephalopathy, renal failure, or hypothermia without classic peritonitis signs. Paracentesis is safe even with coagulopathy (INR or thrombocytopenia are NOT contraindications).

2. **Delaying antibiotics until culture results.** SBP cultures take 24-48 hours and are negative in ~40% of cases. PMN >= 250/mm3 = treat immediately.

3. **Missing secondary peritonitis.** Polymicrobial cultures, failure to improve at 48h, or Runyon criteria mandate CT and surgical evaluation. Treating secondary peritonitis as SBP is fatal.

4. **Omitting albumin infusion.** IV albumin reduces hepatorenal syndrome incidence from 33% to 10% and mortality from 29% to 10%. It is not optional.

5. **Not inoculating culture bottles at bedside.** Sending ascitic fluid to the lab in a tube rather than directly into blood culture bottles reduces sensitivity from ~80% to ~50%.

6. **Using aminoglycosides.** Aminoglycosides are nephrotoxic in cirrhosis and should never be used for SBP treatment.
