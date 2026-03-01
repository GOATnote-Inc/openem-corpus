---
id: hemolytic-uremic-syndrome
condition: Hemolytic Uremic Syndrome
aliases: [HUS, typical HUS, atypical HUS, aHUS, STEC-HUS, diarrhea-associated HUS]
icd10: [D59.3]
esi: 2
time_to_harm:
  irreversible_injury: "< 48 hours (irreversible renal damage)"
  death: "< 72 hours (hyperkalemia, uremia, cerebral edema)"
  optimal_intervention_window: "< 24 hours"
category: hematologic
track: tier1
sources:
  - type: guideline
    ref: "ASH Education: Atypical Hemolytic Uremic Syndrome — Diagnosis, Management, and Discontinuation of Therapy. Hematology, 2024"
  - type: review
    ref: "Hemolytic Uremic Syndrome in Emergency Medicine. Medscape, 2024"
  - type: guideline
    ref: "KDIGO Clinical Practice Guideline for Acute Kidney Injury, 2012 (referenced for HUS-AKI management)"
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
# Hemolytic Uremic Syndrome

## Recognition

**Classic triad:**
- Microangiopathic hemolytic anemia (MAHA) — schistocytes, low haptoglobin, elevated LDH
- Thrombocytopenia
- Acute kidney injury (oliguria/anuria, elevated creatinine, azotemia)

**Typical HUS (STEC-HUS, 90% of pediatric cases):**
- Preceded by bloody diarrhea (5-10 days prior) — Shiga toxin-producing E. coli (O157:H7 most common)
- Primarily affects children age 6 months to 5 years
- Abdominal pain, vomiting
- Pallor, jaundice, petechiae
- Oliguria/anuria developing 5-10 days after diarrhea onset
- Neurologic complications: lethargy, seizures, stroke (25-30%)

**Atypical HUS (aHUS, 10% of cases):**
- No preceding diarrheal illness
- Complement-mediated thrombotic microangiopathy
- Any age; recurrent episodes
- More severe renal failure (60-70% progress to ESRD without complement inhibitor therapy)
- Triggers: pregnancy, infections, surgery, autoimmune disease

**Red flags for severe disease:**
- Anuria > 24 hours
- WBC > 20,000 (poor prognostic marker in typical HUS)
- Seizures or focal neurologic deficits
- Severe hypertension

## Critical Actions

1. **Aggressive IV fluid resuscitation** — early volume expansion before anuria develops reduces dialysis requirement in STEC-HUS
2. **Monitor urine output strictly** — Foley catheter for accurate measurement
3. **Check and treat hyperkalemia** — ECG, emergent K management if > 6.0 mEq/L
4. **Nephrology consultation** — for dialysis planning if oliguria/anuria develops
5. **Send ADAMTS13 activity** to differentiate from TTP (ADAMTS13 > 10% in HUS, < 10% in TTP)
6. **For suspected atypical HUS:** Consider early eculizumab initiation after hematology/nephrology consultation
7. **Do NOT give antibiotics for STEC infection** — may increase toxin release and worsen HUS

## Differential Diagnosis

- Thrombotic thrombocytopenic purpura (TTP) — neurologic symptoms predominate, renal failure milder, ADAMTS13 < 10%
- DIC — abnormal coagulation (PT, fibrinogen); DIC has a clear trigger
- ITP — isolated thrombocytopenia without MAHA or renal failure
- Autoimmune hemolytic anemia — positive Coombs, no schistocytes
- Malignant hypertension with MAHA — severely elevated BP
- Shigella dysentery — may also trigger HUS
- Bilateral renal vein thrombosis — flank pain, hematuria, absence of hemolysis
- Acute glomerulonephritis — active sediment, low complement, no hemolysis

## Workup

- **CBC with peripheral smear** — schistocytes, low platelets, anemia
- **Reticulocyte count** — elevated
- **LDH, indirect bilirubin, haptoglobin** — hemolysis markers
- **Direct Coombs (DAT)** — negative
- **BMP** — elevated creatinine, BUN; hyperkalemia; metabolic acidosis
- **Urinalysis** — hematuria, proteinuria
- **PT/INR, aPTT, fibrinogen** — NORMAL (distinguishes from DIC)
- **ADAMTS13 activity** — > 10% (rules out TTP)
- **Stool culture and Shiga toxin assay** (STEC PCR) — for typical HUS
- **Complement studies (if aHUS suspected):** C3, C4, factor H, factor I, MCP (CD46), anti-factor H antibodies
- **Blood type and crossmatch** — anticipate transfusion
- **Urine output** — strict I&O monitoring

## Treatment

### Typical HUS (STEC-Associated)
- **Supportive care is the mainstay**
- **IV fluids:** Isotonic crystalloid; aggressive early hydration (NS 20 mL/kg boluses, then maintenance) reduces need for dialysis
- **Renal replacement therapy:** Hemodialysis or peritoneal dialysis for: anuria > 24h, hyperkalemia unresponsive to medical therapy, severe metabolic acidosis, fluid overload, uremic encephalopathy
- **Transfuse PRBCs** if symptomatic anemia (Hgb < 6-7 g/dL); transfuse slowly to avoid fluid overload
- **Platelet transfusion:** Avoid if possible — may worsen thrombotic microangiopathy. Transfuse only for life-threatening hemorrhage.
- **Blood pressure management:** Amlodipine 0.1-0.2 mg/kg PO (pediatric) or nifedipine; avoid ACE inhibitors acutely (hyperkalemia risk)
- **Do NOT give antibiotics** for STEC infection — associated with increased risk of HUS progression
- **Do NOT give antimotility agents** — slow toxin clearance

### Atypical HUS (Complement-Mediated)
- **Eculizumab 900 mg IV q7 days x 4 weeks** (induction), then 1200 mg IV q14 days (maintenance)
  - Meningococcal vaccination required before or concurrent with first dose (risk of N. meningitidis infection)
  - If urgent, give meningococcal vaccine + prophylactic antibiotics (penicillin VK 250 mg PO BID or ciprofloxacin 500 mg PO BID) while completing vaccination series
- **Ravulizumab** (longer-acting C5 inhibitor) is an alternative: 2400-3000 mg IV (weight-based) loading, then q8 weeks
- **Plasma exchange (TPE):** May be used as bridge until eculizumab is available or if diagnosis uncertain between TTP and aHUS

### Hyperkalemia Management
- Calcium gluconate 10% 0.5-1 mL/kg IV (max 30 mL) for cardiac stabilization
- Regular insulin 0.1 units/kg IV + dextrose 0.5 g/kg IV
- Sodium bicarbonate 1-2 mEq/kg IV if acidotic
- Sodium polystyrene sulfonate or patiromer for ongoing management
- Emergent dialysis if refractory

## Disposition

- **All HUS patients:** Admit to ICU or pediatric ICU
- **Nephrology consultation** — mandatory (dialysis may be needed within hours)
- **Hematology consultation** — for ADAMTS13, complement workup, treatment decisions
- **Transfer** if facility lacks pediatric dialysis capability
- **Typical HUS outcomes:** ~75% recover renal function; 3-5% mortality; 25% have long-term renal sequelae
- **Atypical HUS without complement inhibitor:** 60-70% progress to ESRD
- **Isolation:** Contact precautions if STEC-associated (enteric precautions)
- **Reportable:** STEC infection/HUS is reportable to public health in most US states

## Pitfalls

1. **Giving antibiotics for STEC O157:H7 infection.** Antibiotics (especially fluoroquinolones and TMP-SMX) increase Shiga toxin release and are associated with higher rates of HUS development. Supportive care only for STEC diarrhea.

2. **Confusing HUS with TTP.** The key discriminator is ADAMTS13 activity: < 10% = TTP (plasma exchange); > 10% = HUS (supportive care or eculizumab). Both have MAHA + thrombocytopenia. Renal failure is more prominent in HUS; neurologic symptoms in TTP.

3. **Inadequate early fluid resuscitation.** Volume expansion before oliguria develops in STEC-HUS reduces the need for dialysis. Delayed or inadequate hydration worsens renal outcomes.

4. **Transfusing platelets routinely.** Platelet transfusion in thrombotic microangiopathies may worsen microvascular thrombosis. Reserve for life-threatening hemorrhage only.

5. **Missing atypical HUS.** Any patient with the HUS triad WITHOUT preceding diarrhea, with recurrent episodes, or with family history of TMA should be evaluated for complement-mediated aHUS. Early eculizumab dramatically improves outcomes.

6. **Delaying meningococcal vaccination before eculizumab.** Complement inhibition increases susceptibility to encapsulated organisms, particularly Neisseria meningitidis. Vaccinate before or concurrent with first dose, and maintain prophylactic antibiotics for 2 weeks after vaccination.
