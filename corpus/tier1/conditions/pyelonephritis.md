---
id: pyelonephritis
condition: Acute Pyelonephritis
aliases: [pyelo, upper UTI, kidney infection, upper urinary tract infection]
icd10: [N10, N11.0, N11.1, N12, N13.6, O23.00, O23.01, O23.02, O23.03]
esi: 2
time_to_harm: "< 6-12 hours if obstructed or septic"
mortality_if_delayed: "2-10% if complicated/septic; < 1% if uncomplicated and treated"
category: genitourinary
track: tier1
sources:
  - type: guideline
    ref: "2011 IDSA/ESCMID Clinical Practice Guideline for the Treatment of Acute Uncomplicated Cystitis and Pyelonephritis in Women"
    pmid: "21292654"
    doi: "10.1093/cid/ciq257"
  - type: guideline
    ref: "2022 AUA/CUA/SUFU Guideline on Recurrent Urinary Tract Infections"
  - type: guideline
    ref: "2021 Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock"
    pmid: "34599691"
  - type: review
    ref: "Colgan R et al. Diagnosis and Treatment of Acute Pyelonephritis in Women. Am Fam Physician 2011;84(5):519-526"
    pmid: "21888302"
  - type: review
    ref: "Johnson JR, Russo TA. Acute Pyelonephritis in Adults. N Engl J Med 2018;378(1):48-59"
    pmid: "29298155"
    doi: "10.1056/NEJMcp1702758"
  - type: guideline
    ref: "2018 ACOG Committee Opinion No. 717: Sulfonamides, Nitrofurantoin, and Risk of Birth Defects"
last_updated: "2026-02-18"
compiled_by: agent
risk_tier: B
validation:
  automated_consistency_check: "2026-02-18"
  dose_range_validator: "2026-02-19"
  unit_normalization_check: "2026-02-19"
  cross_file_consistency_check: "2026-02-19"
  citation_presence_check: "2026-02-19"
  duplicate_content_check: "2026-02-19"
  outlier_detection_flag: clear
  schema_version: "2.0"
  provenance_links: []
---
# Acute Pyelonephritis

## Recognition

**Definition:** Bacterial infection of the renal parenchyma and collecting system, typically ascending from the lower urinary tract. Distinguishing upper from lower UTI matters because pyelonephritis carries risk of sepsis, abscess, and renal damage.

**Classification:**
- **Uncomplicated:** Premenopausal, non-pregnant female with normal urinary tract anatomy and function
- **Complicated:** Any of the following:
  - Male sex
  - Pregnancy
  - Urinary tract obstruction (stone, stricture, tumor, BPH)
  - Indwelling catheter or ureteral stent
  - Immunosuppression (diabetes, HIV, transplant, chronic steroids)
  - Renal transplant
  - Anatomic/functional urinary tract abnormality
  - Recent urologic instrumentation
  - Healthcare-associated infection

**Microbiology:**
- Escherichia coli (75-90% of uncomplicated cases)
- Klebsiella pneumoniae (5-10%)
- Proteus mirabilis (associated with struvite stones)
- Enterococcus spp. (especially with urinary instrumentation)
- Staphylococcus saprophyticus (young women, cystitis > pyelonephritis)
- Pseudomonas aeruginosa (catheter-associated, healthcare exposure)
- ESBL-producing Enterobacteriaceae (increasing prevalence; recent antibiotics, healthcare exposure, travel to endemic regions)

**Presentation:**
- Fever (often > 38.5°C / 101.3°F) — the hallmark distinguishing pyelo from simple cystitis
- Flank pain (unilateral most common)
- Costovertebral angle (CVA) tenderness — present in 85-90%
- Nausea, vomiting
- Malaise, rigors
- Lower urinary tract symptoms may or may not be present (dysuria, frequency, urgency in 50-70%)
- Abdominal pain (may mimic intra-abdominal pathology)

**Exam Findings:**
- CVA tenderness (percussion tenderness at the 12th rib posteriorly)
- Fever, tachycardia
- Suprapubic tenderness (concomitant cystitis)
- Abdominal guarding (if severe or abscess present)
- Assess for sepsis: altered mental status, hypotension, tachycardia, tachypnea

## Critical Actions

1. **Obtain urine culture BEFORE antibiotics** — mandatory in all pyelonephritis cases (unlike uncomplicated cystitis). Guides de-escalation and detects resistance.
2. **Blood cultures x 2** — if admission criteria met, sepsis suspected, or complicated pyelonephritis. Positive in 15-30% of admitted pyelonephritis patients.
3. **Start empiric antibiotics within 1 hour** if septic; otherwise within 2-3 hours of presentation.
4. **CT abdomen/pelvis with IV contrast** — if concern for obstruction, abscess, or failure to respond to antibiotics at 48-72 hours. Obstructed pyelonephritis is a urologic emergency requiring urgent decompression.
5. **IV fluid resuscitation** — for dehydration from vomiting, fever, and poor oral intake. Aggressive resuscitation if septic (30 mL/kg crystalloid within first 3 hours per Surviving Sepsis Campaign).
6. **Assess for complicated features** — pregnancy, obstruction, immunosuppression, male sex, recent instrumentation, indwelling hardware. These change antibiotic choice, imaging decisions, and disposition.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Lower UTI (cystitis) | Dysuria, frequency, urgency WITHOUT fever, flank pain, or systemic symptoms. CVA tenderness absent. |
| Nephrolithiasis | Colicky flank pain radiating to groin, hematuria, no fever (unless concurrent infection/pyonephrosis). CT shows stone. |
| Renal abscess / perinephric abscess | Prolonged symptoms (> 5 days), failure to respond to antibiotics, CT shows rim-enhancing fluid collection |
| Appendicitis | RLQ pain, periumbilical onset, McBurney point tenderness, positive Rovsing. UA may have mild pyuria from adjacent inflammation. |
| Cholecystitis | RUQ pain, Murphy sign, postprandial, ultrasound shows gallstones/wall thickening |
| Lower lobe pneumonia | Cough, pleuritic pain, may refer to flank/abdomen. CXR diagnostic. |
| Ruptured ovarian cyst | Sudden unilateral pelvic/flank pain, no fever, negative UA, ultrasound diagnostic |
| Musculoskeletal back pain | No fever, no pyuria, no CVA tenderness, pain reproduced with movement |

## Workup

**Labs:**
- **Urinalysis with microscopy:**
  - Pyuria (> 10 WBC/hpf) — present in > 95%. Absence argues strongly against pyelonephritis.
  - Bacteriuria
  - Leukocyte esterase, nitrites (nitrite-negative does not exclude: Enterococcus and Pseudomonas do not produce nitrites)
  - WBC casts — pathognomonic for pyelonephritis (present in ~20%)
  - Hematuria (common, non-specific)
- **Urine culture with sensitivities** — mandatory. Obtain BEFORE antibiotics. Threshold: >= 10,000 CFU/mL with pyuria is diagnostic (some labs use >= 100,000).
- **Blood cultures x 2** — if admitting, septic, or complicated pyelonephritis
- **CBC:** Leukocytosis with left shift; bandemia supports systemic infection
- **BMP:** Creatinine (assess renal function, especially if obstruction suspected), electrolytes (vomiting/dehydration)
- **Lactate** — if sepsis suspected. > 2 mmol/L concerning for sepsis; > 4 mmol/L indicates septic shock.
- **Procalcitonin** — may help distinguish upper from lower UTI (> 0.25 ng/mL suggests upper tract involvement); aids antibiotic duration decisions
- **Pregnancy test** — all reproductive-age females. Pyelonephritis in pregnancy changes antibiotic selection and mandates admission.

**Imaging:**
- **Not routinely indicated** for uncomplicated pyelonephritis in young, healthy, non-pregnant women responding to antibiotics
- **CT abdomen/pelvis with IV contrast** — obtain if:
  - Concern for urinary obstruction (stone, tumor, stricture)
  - Failure to improve after 48-72 hours of appropriate antibiotics
  - Suspected renal or perinephric abscess
  - Complicated pyelonephritis (diabetes, immunosuppression, history of stones, structural abnormalities)
  - Male pyelonephritis (always consider obstruction)
  - Findings: perinephric fat stranding, renal enlargement, focal hypoperfusion, abscess (rim-enhancing collection), hydronephrosis, stones
- **Renal ultrasound** — alternative if CT contraindicated (pregnancy, contrast allergy, renal insufficiency). Detects hydronephrosis and abscess but less sensitive for stones and parenchymal detail.
- **MRI without gadolinium** — preferred in pregnancy if imaging needed beyond ultrasound

## Treatment

**Outpatient Management (Uncomplicated Pyelonephritis):**

Criteria: non-pregnant, non-septic, tolerating oral intake, no vomiting, no complicating factors, reliable follow-up.

| Agent | Dose | Duration | Notes |
|-------|------|----------|-------|
| **Ciprofloxacin** | 500 mg PO BID | 7 days | IDSA first-line if local resistance < 10%. Check local antibiogram. |
| **Levofloxacin** | 750 mg PO daily | 5 days | Alternative fluoroquinolone |
| **TMP-SMX** | 160/800 mg (DS) PO BID | 14 days | Use only if susceptibility confirmed (E. coli resistance ~25% in many regions). NOT for empiric use. |
| **Ceftriaxone** (initial) then oral step-down | 1 g IV/IM x 1 dose in ED, then ciprofloxacin or TMP-SMX PO | Per oral agent | Reasonable ED strategy: IV dose provides early bactericidal activity, oral agent for course completion |

- Give initial IV dose of ceftriaxone 1 g IM/IV in the ED before discharge if any concern about adequacy of oral regimen or time to oral antibiotic effect.
- Antiemetic (ondansetron 4-8 mg IV/ODT) before discharge if nausea.
- Oral hydration emphasized.
- Follow-up urine culture NOT routinely needed if symptoms resolve. Follow-up visit at 48-72 hours.

**Inpatient Management (Complicated or Requiring Admission):**

| Agent | Dose | Coverage |
|-------|------|----------|
| **Ceftriaxone** | 1 g IV q24h | First-line for most admitted patients. Good gram-negative coverage. |
| **Ciprofloxacin** | 400 mg IV q12h | Alternative if cephalosporin allergy; transition to oral 500 mg BID when tolerating PO |
| **Levofloxacin** | 750 mg IV q24h | Alternative fluoroquinolone |
| **Ampicillin** 2 g IV q4h + **gentamicin** 5 mg/kg IV q24h | | If Enterococcus suspected (urinary instrumentation, prior cultures) |

**Septic / Critically Ill:**

| Agent | Dose | Coverage |
|-------|------|----------|
| **Piperacillin-tazobactam** | 4.5 g IV q6h (extended infusion over 4h preferred) | Broad gram-negative including Pseudomonas, plus anaerobes |
| **Meropenem** | 1 g IV q8h | ESBL-producing organisms, prior treatment failure, severely ill |
| **Cefepime** | 2 g IV q8h | Pseudomonas coverage; alternative to piperacillin-tazobactam |

- Add **vancomycin 15-20 mg/kg IV q8-12h** if gram-positive cocci in clusters on gram stain or concern for MRSA (rare in UTI, but consider with indwelling hardware, recent healthcare exposure).
- De-escalate based on culture results within 48-72 hours.
- Transition IV to oral when afebrile > 24-48 hours, tolerating PO, and clinical improvement.
- Total antibiotic duration: 10-14 days for complicated pyelonephritis; 5-7 days for uncomplicated.

**Obstructed Pyelonephritis / Pyonephrosis:**
- Urologic emergency — antibiotics alone are insufficient
- Emergent urologic consultation for decompression:
  - Percutaneous nephrostomy tube (interventional radiology)
  - Ureteral stent placement (urology)
- Decompression within 6-12 hours; sooner if septic

**Renal / Perinephric Abscess:**
- Abscesses < 3-5 cm: IV antibiotics and serial imaging
- Abscesses >= 5 cm: CT-guided percutaneous drainage + IV antibiotics
- Surgical drainage if percutaneous approach fails

**Pregnancy-Specific Management:**
- ALL pyelonephritis in pregnancy requires admission (risk of preterm labor, sepsis, ARDS)
- **Ceftriaxone 1 g IV q24h** — first-line
- **Aztreonam 1 g IV q8h** — if cephalosporin allergy (severe/anaphylactic)
- **Ampicillin 2 g IV q4h + gentamicin 5 mg/kg IV q24h** — alternative
- **AVOID:** Fluoroquinolones (teratogenic, cartilage damage), TMP-SMX first trimester (neural tube defects) and near term (kernicterus), nitrofurantoin first trimester (congenital anomalies, per ACOG)
- Tocolytic monitoring if contractions develop
- Suppressive therapy after treatment: cephalexin 250-500 mg PO daily or nitrofurantoin 100 mg PO daily for remainder of pregnancy

## Disposition

**Discharge (Outpatient Management):**
- Uncomplicated pyelonephritis in young, non-pregnant female
- Tolerating PO fluids and medications
- Not septic (no SIRS/qSOFA criteria)
- No vomiting or controlled with antiemetics
- No complicating factors
- Reliable follow-up within 48-72 hours
- Return precautions: worsening symptoms, inability to tolerate PO, fever > 48 hours on antibiotics, rigors

**Admission Criteria:**
- Sepsis or hemodynamic instability
- Intractable nausea/vomiting (unable to tolerate PO)
- Pregnancy
- Suspected or confirmed obstruction
- Immunocompromised (diabetes with poor control, HIV, transplant, chronic steroids)
- Concern for abscess
- Failed outpatient therapy (persistent fever > 48-72 hours on appropriate oral antibiotics)
- Unreliable follow-up or social situation precluding safe discharge
- Significant comorbidities (renal insufficiency, advanced age, frailty)
- Male pyelonephritis (higher rate of underlying structural abnormality)

**ICU Admission:**
- Septic shock requiring vasopressors
- Respiratory failure
- Obstructed pyelonephritis with sepsis

## Pitfalls

1. **Not obtaining urine culture before antibiotics.** Unlike simple cystitis, pyelonephritis mandates pre-treatment urine culture. Resistance rates for E. coli to fluoroquinolones exceed 20% in many regions and to TMP-SMX exceed 25%. Without culture, a resistant organism leaves the patient on ineffective therapy with a ticking clock toward abscess or sepsis.

2. **Assuming negative nitrites excludes UTI/pyelonephritis.** Enterococcus, Pseudomonas, Staphylococcus, and Acinetobacter do not reduce nitrates to nitrites. A UA with significant pyuria and leukocyte esterase but negative nitrites still supports pyelonephritis in the right clinical context.

3. **Discharging a pregnant patient with pyelonephritis.** Pyelonephritis in pregnancy carries 10-20% risk of complications including preterm labor, sepsis, and ARDS. All pregnant patients with pyelonephritis require admission for IV antibiotics, fetal monitoring, and observation. There is no outpatient management of pyelonephritis in pregnancy.

4. **Missing obstructed pyelonephritis.** Pyelonephritis with ureteral obstruction (stone, stricture, mass) does not respond to antibiotics alone — the obstructed, infected collecting system requires emergent drainage. Clues: known stone disease, persistent sepsis despite antibiotics, unilateral hydronephrosis on imaging, renal colic symptoms. CT abdomen/pelvis is diagnostic.

5. **Using nitrofurantoin for pyelonephritis.** Nitrofurantoin does not achieve therapeutic tissue or serum concentrations — it is concentrated only in urine and is effective only for lower UTI. Prescribing nitrofurantoin for pyelonephritis is a treatment failure waiting to happen.

6. **Empirically prescribing TMP-SMX without culture data.** E. coli resistance to TMP-SMX exceeds 25% in most US regions. IDSA guidelines recommend TMP-SMX for pyelonephritis only when susceptibility is confirmed. Using it empirically risks treatment failure in 1 in 4 patients.

7. **Failing to image a male patient with pyelonephritis.** Pyelonephritis in men is uncommon and almost always complicated by structural abnormality (BPH, stricture, stone, neurogenic bladder). CT with contrast is warranted to evaluate for obstruction, abscess, or anatomic cause. Do not treat and discharge without imaging workup.

8. **Attributing flank pain and pyuria to pyelonephritis when appendicitis or other intra-abdominal pathology is present.** The appendix and right ureter are anatomically adjacent. Appendicitis can cause mild pyuria from inflammation without infection. Maintain a broad differential — if the clinical picture does not fit straightforward pyelonephritis, image the abdomen.

9. **Stopping antibiotics at clinical improvement rather than completing the course.** Minimum duration is 5-7 days for uncomplicated (fluoroquinolone) and 10-14 days for complicated pyelonephritis. Premature discontinuation leads to relapse, treatment failure, and resistance selection. Communicate completion requirements clearly at discharge.

10. **Not reassessing the patient who does not improve in 48-72 hours.** Persistent fever or worsening symptoms after 48-72 hours of appropriate antibiotics should prompt imaging (CT with contrast) to evaluate for abscess, obstruction, or resistant organism. Do not reflexively broaden antibiotics — identify the structural or microbiological reason for failure.
