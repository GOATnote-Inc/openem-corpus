---
id: complicated-uti
condition: Complicated Urinary Tract Infection
aliases: [complicated UTI, cUTI, urosepsis, catheter-associated UTI, CAUTI, emphysematous pyelonephritis, obstructed infected kidney, UTI with obstruction]
icd10: [N39.0, N30.90, T83.511A, N13.6]
esi: 3
time_to_harm: "< 6 hours if obstructed or septic; hours to days if uncomplicated host factors"
mortality_if_delayed: "Urosepsis mortality 20-40% if source control delayed; emphysematous pyelonephritis 13-25%"
category: genitourinary
track: tier1
sources:
  - type: review
    ref: "Wagenlehner FME, Bjerklund Johansen TE, Cai T, et al. Epidemiology, definition and treatment of complicated urinary tract infections. Nat Rev Urol. 2020;17(10):586-600"
    pmid: "32843751"
    doi: "10.1038/s41585-020-0362-4"
  - type: guideline
    ref: "Hooton TM, Bradley SF, Cardenas DD, et al. Diagnosis, Prevention, and Treatment of Catheter-Associated Urinary Tract Infection in Adults: 2009 International Clinical Practice Guidelines from the IDSA. Clin Infect Dis. 2010;50(5):625-663"
    pmid: "20175247"
  - type: guideline
    ref: "Gupta K, Hooton TM, Naber KG, et al. International Clinical Practice Guidelines for the Treatment of Acute Uncomplicated Cystitis and Pyelonephritis in Women: 2010 Update by IDSA/ESCMID. Clin Infect Dis. 2011;52(5):e103-e120"
    pmid: "21292654"
    doi: "10.1093/cid/ciq257"
  - type: review
    ref: "Guliciuc M, Maier AC, Maier IM, et al. The Urosepsis — A Literature Review. Medicina (Kaunas). 2021;57(9):872"
    pmid: "34577795"
  - type: meta-analysis
    ref: "Zhong H, Fang C, Fan Y, et al. A systematic review and meta-analysis of risk factors and treatment choices in emphysematous pyelonephritis. Int Urol Nephrol. 2022;54(5):1001-1012"
    pmid: "35103928"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: C
validation:
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  schema_version: "2.0"
  guideline_version_reference: null
  provenance_links: []
---
# Complicated Urinary Tract Infection

> **Scope:** This file covers UTI with complicating host or anatomic factors — urosepsis, UTI with obstruction, emphysematous pyelonephritis, catheter-associated UTI, UTI in immunocompromised or elderly patients with altered mental status. For uncomplicated upper tract infection, see [pyelonephritis.md](pyelonephritis.md).

## Recognition

**Definition:** A urinary tract infection occurring in the presence of structural or functional abnormalities of the urinary tract, or in a host with factors that increase the risk of treatment failure, recurrence, or severe outcomes. The distinction from uncomplicated UTI drives empiric antibiotic selection, imaging decisions, duration of therapy, and disposition.

**Complicating Factors:**
- Urinary tract obstruction (stone, stricture, tumor, BPH)
- Indwelling urinary catheter or ureteral stent
- Male sex
- Pregnancy (see pyelonephritis.md for pregnancy-specific management)
- Diabetes mellitus (especially poorly controlled)
- Immunosuppression (transplant, HIV, chronic steroids, chemotherapy)
- Renal transplant
- Anatomic or functional urinary tract abnormality (neurogenic bladder, vesicoureteral reflux, urinary diversion)
- Recent urologic instrumentation or surgery
- Healthcare-associated infection
- Elderly with functional or cognitive impairment
- Renal insufficiency

**Microbiology:**
- Escherichia coli remains dominant (50-65%) but less predominant than in uncomplicated UTI
- Klebsiella pneumoniae (10-15%)
- Proteus mirabilis (associated with struvite stones and catheter encrustation)
- Pseudomonas aeruginosa (catheter-associated, healthcare exposure, structural abnormality)
- Enterococcus spp. (urinary instrumentation, prior antibiotics)
- ESBL-producing Enterobacteriaceae (increasing; prior antibiotics, healthcare exposure, travel to endemic areas)
- Polymicrobial infections more common than in uncomplicated UTI, particularly with catheters

**Clinical Subtypes:**

### Urosepsis
- Sepsis originating from the urogenital tract; accounts for approximately 25% of all sepsis cases
- Obstructive uropathy is the cause in ~78% of urosepsis cases
- Presents with SIRS/sepsis criteria: fever, tachycardia, hypotension, altered mental status, elevated lactate
- May progress rapidly to septic shock, particularly with obstruction

### UTI in Elderly with Altered Mental Status
- Elderly patients may present with acute confusion, lethargy, or functional decline as the only manifestation
- Classic urinary symptoms (dysuria, frequency, urgency) are frequently absent
- Bacteriuria is common in the elderly; AMS + bacteriuria does not automatically equal UTI — exclude other causes of delirium (medication, metabolic, CNS pathology)
- Pyuria with systemic signs (fever, hemodynamic changes) supports diagnosis

### Emphysematous Pyelonephritis
- Necrotizing, gas-forming infection of the renal parenchyma
- 90% occur in patients with diabetes mellitus
- CT demonstrates gas within or surrounding the kidney — diagnostic
- Mortality 13-25% (higher with bilateral involvement, thrombocytopenia, shock)
- Classified by Huang-Tseng system (Class 1-4 based on gas distribution)
- E. coli (most common), Klebsiella, Proteus

### Obstructed Infected Kidney (Pyonephrosis)
- Infected hydronephrosis — pus under pressure in the collecting system
- Antibiotics alone are insufficient; requires emergent decompression
- Presents as pyelonephritis unresponsive to antibiotics, sepsis with hydronephrosis on imaging
- Delay in drainage leads to rapid clinical deterioration and renal loss

### Catheter-Associated UTI (CAUTI)
- Defined as UTI in a patient with an indwelling urinary catheter (or catheter removed within prior 48 hours) with symptoms attributable to the urinary tract
- Asymptomatic bacteriuria with a catheter is near-universal and should NOT be treated (no benefit, promotes resistance)
- Treat only if systemic signs: fever >= 38.0°C, rigors, hemodynamic instability, altered mental status, or flank pain — not for cloudy/malodorous urine alone
- Remove or replace the catheter before obtaining culture (biofilm on the old catheter yields colonizing organisms, not the causative pathogen)

### UTI in Immunocompromised
- Renal transplant recipients: UTI is the most common infection post-transplant; risk of graft pyelonephritis and bacteremia is high; empiric coverage should be broader
- HIV/AIDS: increased risk of complicated UTI, particularly with CD4 < 200
- Neutropenic patients: may lack pyuria; treat based on clinical suspicion (see neutropenic-fever.md)

## Critical Actions

1. **Identify complicating factors immediately.** The presence of obstruction, catheter, immunosuppression, or structural abnormality fundamentally changes management. A "UTI" in a diabetic patient with a ureteral stone is a different disease than cystitis in a healthy young woman.
2. **Obtain urine culture BEFORE antibiotics** — mandatory in all complicated UTI. Guides de-escalation and detects resistance patterns that are more prevalent in this population.
3. **Blood cultures x 2** — for all patients with systemic signs, fever, or suspected urosepsis. Positive in 20-30% of complicated pyelonephritis and urosepsis cases.
4. **Administer empiric antibiotics within 1 hour** if sepsis criteria met; within 2-3 hours otherwise.
5. **CT abdomen/pelvis with IV contrast** — obtain in all complicated UTI to evaluate for obstruction, abscess, emphysematous changes, and anatomic abnormalities. This is not optional for complicated presentations.
6. **Emergent urology consultation** for obstructed infected kidney (pyonephrosis) or emphysematous pyelonephritis. Obstructed infection requires drainage (nephrostomy tube or ureteral stent), not just antibiotics.
7. **For CAUTI: remove or replace the catheter** before obtaining the culture specimen. Initiate antibiotics only for systemic signs — not for asymptomatic bacteriuria.
8. **Aggressive IV fluid resuscitation** — 30 mL/kg crystalloid within first 3 hours if septic (per Surviving Sepsis Campaign). Vasopressors if MAP < 65 mmHg despite adequate fluids.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Uncomplicated pyelonephritis | No complicating host or anatomic factors; premenopausal non-pregnant female with normal urinary tract. See pyelonephritis.md. |
| Nephrolithiasis without infection | Colicky flank pain, hematuria, no fever, no pyuria (or minimal). CT shows stone without perinephric changes. |
| Renal abscess / perinephric abscess | Prolonged symptoms > 5 days, failure to respond to antibiotics, CT shows rim-enhancing fluid collection. May coexist with complicated UTI. |
| Acute prostatitis | Male with perineal pain, exquisitely tender prostate on DRE, fever, pyuria. Complicated UTI and acute prostatitis overlap significantly. |
| Cholangitis | RUQ pain, jaundice, fever (Charcot triad). Elevated bilirubin and alkaline phosphatase. Biliary dilation on imaging. |
| Intra-abdominal abscess | Fever, localized tenderness, CT with rim-enhancing collection remote from kidney. |
| Delirium from non-urinary cause | In elderly patients with AMS and incidental bacteriuria — exclude medications, metabolic derangements, stroke, subdural hematoma before attributing AMS to UTI. |
| Xanthogranulomatous pyelonephritis | Chronic destructive granulomatous process, nonfunctioning kidney on CT, often mimics renal malignancy. Surgical pathology diagnosis. |

## Workup

**Labs:**
- **Urinalysis with microscopy:**
  - Pyuria (> 10 WBC/hpf) — supports infection; may be absent in neutropenic patients
  - Bacteriuria, leukocyte esterase, nitrites
  - Nitrite-negative does not exclude UTI (Enterococcus, Pseudomonas, Staphylococcus do not produce nitrites)
  - WBC casts — pathognomonic for upper tract involvement
- **Urine culture with sensitivities** — mandatory; obtain BEFORE antibiotics. For CAUTI, obtain from a newly placed catheter (not the colonized indwelling catheter).
- **Blood cultures x 2** — all patients with systemic signs, hemodynamic instability, or immunosuppression
- **CBC:** Leukocytosis with left shift; leukopenia suggests severe sepsis or immunosuppression
- **BMP:** Creatinine (obstructive nephropathy, baseline renal function), electrolytes, glucose (DKA can coexist with UTI in diabetics)
- **Lactate** — obtain in all patients with systemic signs. > 2 mmol/L concerning; > 4 mmol/L indicates septic shock.
- **Procalcitonin** — may help distinguish upper from lower tract involvement (> 0.25 ng/mL suggests upper tract)
- **Hepatic panel** — if cholangitis in the differential
- **Coagulation studies** — if septic or DIC suspected
- **Pregnancy test** — all reproductive-age females

**Imaging:**
- **CT abdomen/pelvis with IV contrast** — indicated in virtually all complicated UTI:
  - Obstruction (hydronephrosis, obstructing stone, mass)
  - Gas within or surrounding kidney (emphysematous pyelonephritis)
  - Renal or perinephric abscess
  - Anatomic abnormalities
  - Perinephric fat stranding, renal enlargement, focal hypoperfusion
- **Renal ultrasound** — acceptable initial study if CT is contraindicated (pregnancy, contrast allergy, severe renal insufficiency). Detects hydronephrosis reliably but less sensitive for gas, stones < 5 mm, and parenchymal detail.
- **KUB** — limited utility; may show gas overlying the kidney in emphysematous pyelonephritis but CT is far superior

## Treatment

### Empiric Antibiotics — Complicated UTI (Non-Septic)

| Agent | Dose | Notes |
|-------|------|-------|
| **Ceftriaxone** | 2 g IV q24h | First-line for most complicated UTI requiring admission. Broad gram-negative coverage. |
| **Ciprofloxacin** | 400 mg IV q12h | Alternative if cephalosporin allergy (non-anaphylactic). Transition to 500 mg PO BID when tolerating PO. Check local resistance patterns (E. coli fluoroquinolone resistance exceeds 20% in many areas). |
| **Levofloxacin** | 750 mg IV q24h | Alternative fluoroquinolone |
| **Ampicillin** 2 g IV q4h + **gentamicin** 5 mg/kg IV q24h | | If Enterococcus suspected (prior cultures, urinary instrumentation) |

### Empiric Antibiotics — Urosepsis / Critically Ill

| Agent | Dose | Notes |
|-------|------|-------|
| **Piperacillin-tazobactam** | 4.5 g IV q6h (extended infusion over 4 hours preferred) | Broad gram-negative including Pseudomonas, plus anaerobes. First-line for septic or critically ill patients. |
| **Meropenem** | 1 g IV q8h | ESBL-producing organisms, prior treatment failure, or severely ill. Reserve carbapenems when possible. |
| **Cefepime** | 2 g IV q8h | Pseudomonas coverage; alternative to piperacillin-tazobactam |

- Add **vancomycin 15-20 mg/kg IV** if gram-positive cocci on gram stain, concern for Enterococcus with hemodynamic instability, or MRSA risk factors (indwelling hardware, recent healthcare exposure).
- De-escalate based on culture and sensitivity results within 48-72 hours.
- Transition IV to oral when afebrile > 24-48 hours, tolerating PO, and clinically improving.
- **Total duration:** 10-14 days for complicated UTI; 5-7 days may be sufficient for catheter-related UTI if the catheter is removed and clinical response is rapid.

### Source Control — Obstructed Infected Kidney

- **Urologic emergency** — antibiotics alone will not resolve an obstructed, infected collecting system.
- Emergent consultation for decompression:
  - **Percutaneous nephrostomy tube** (interventional radiology) — preferred in unstable or septic patients
  - **Ureteral stent placement** (urology) — preferred if patient stable enough for OR
- Target decompression within 6-12 hours; sooner if hemodynamically unstable or worsening despite antibiotics.
- Definitive stone management is deferred until the infection is cleared (typically 4-6 weeks later).

### Emphysematous Pyelonephritis

- **Broad-spectrum IV antibiotics** — piperacillin-tazobactam 4.5 g IV q6h or meropenem 1 g IV q8h
- **Percutaneous drainage** — first-line interventional approach; mortality lower than with emergent nephrectomy (10% vs. 26%)
- **Nephrectomy** — reserved for failed percutaneous drainage, Class 3B/4 with septic shock, or nonfunctioning kidney
- Emergent urology and interventional radiology consultation
- ICU admission for hemodynamic monitoring

### CAUTI-Specific Management

- **Remove or replace** the indwelling catheter — reduces treatment failure and recurrence
- Obtain urine culture from the new catheter
- If catheter can be removed entirely, do so
- Treat for 7 days if symptoms resolve promptly; 10-14 days if delayed response
- **Do NOT treat asymptomatic bacteriuria** in catheterized patients — no mortality benefit, promotes resistance

### Sepsis Management (Cross-Reference: sepsis.md)

- IV crystalloid 30 mL/kg within first 3 hours for hypotension or lactate >= 4 mmol/L
- Norepinephrine 0.05-0.5 mcg/kg/min for MAP < 65 mmHg despite fluids
- Hydrocortisone 50 mg IV q6h if vasopressor-refractory shock
- Repeat lactate at 2-4 hours

## Disposition

**Admission Criteria (most complicated UTI requires admission):**
- Urosepsis or hemodynamic instability
- Obstructed infected kidney (pyonephrosis) — requires emergent decompression
- Emphysematous pyelonephritis — ICU or step-down with surgical consultation
- Intractable nausea/vomiting precluding oral therapy
- Immunocompromised (poorly controlled diabetes, transplant, HIV, chronic steroids)
- Acute kidney injury or obstructive uropathy
- Failed outpatient therapy (persistent symptoms > 48-72 hours on appropriate antibiotics)
- Pregnancy with complicated UTI (all require admission)
- Elderly with AMS attributable to UTI
- Unreliable follow-up

**ICU Admission:**
- Septic shock requiring vasopressors
- Emphysematous pyelonephritis with hemodynamic instability
- Obstructed infected kidney with sepsis
- Respiratory failure
- Multi-organ dysfunction

**Discharge (Uncommon for Complicated UTI):**
- Select patients with a well-defined, mild complicating factor (e.g., well-controlled diabetes, male sex as the only complicating factor) who are non-septic, tolerating PO, and have reliable follow-up within 24-48 hours
- Initial IV dose of ceftriaxone 2 g in the ED followed by oral fluoroquinolone (if susceptibility known or local resistance < 10%)
- Culture results must be followed; patient must understand return precautions
- Urology follow-up for any structural or obstructive pathology

**Urology Follow-Up (All Patients):**
- Any patient with a first complicated UTI should have urologic evaluation for underlying structural or functional abnormality
- Imaging follow-up for emphysematous pyelonephritis, abscess, or obstructive uropathy

## Pitfalls

1. **Treating asymptomatic bacteriuria in catheterized patients.** Bacteriuria is near-universal with indwelling catheters. Treating without systemic signs (fever, hemodynamic changes, altered mental status) promotes antibiotic resistance and Clostridioides difficile infection without clinical benefit. Culture only when systemic signs are present. Cloudy or malodorous urine alone is not an indication for antibiotics.

2. **Attributing altered mental status in the elderly to UTI without excluding other causes.** Bacteriuria and pyuria are common incidental findings in elderly patients. Before diagnosing "UTI causing AMS," exclude metabolic derangements (hypoglycemia, hyponatremia, hyperkalemia), medication effects (anticholinergics, opioids, benzodiazepines), stroke, subdural hematoma, and other sources of sepsis. AMS + positive UA is not an automatic diagnosis.

3. **Using antibiotics alone for an obstructed infected kidney.** Pyonephrosis (infected hydronephrosis) is a urologic emergency that requires drainage — nephrostomy tube or ureteral stent — in addition to antibiotics. Failure to decompress the obstructed collecting system leads to progressive sepsis, renal loss, and death despite adequate antibiotic coverage.

4. **Missing emphysematous pyelonephritis by not obtaining CT.** Gas-forming infection of the kidney carries 13-25% mortality and requires emergent intervention (percutaneous drainage or nephrectomy). A patient with diabetes, sepsis, and pyelonephritis who is not improving warrants CT abdomen/pelvis with IV contrast. Gas on imaging is diagnostic and changes management from medical to surgical.

5. **Underdosing ceftriaxone for complicated UTI.** The standard dose for complicated UTI and urosepsis is ceftriaxone 2 g IV q24h — not the 1 g dose used for uncomplicated pyelonephritis. Underdosing in the setting of higher bacterial burden, resistant organisms, and compromised host defenses risks treatment failure.

6. **Empirically using fluoroquinolones without checking local resistance patterns.** E. coli resistance to fluoroquinolones exceeds 20% in many US regions and is higher in complicated UTI populations (prior antibiotics, healthcare exposure, recurrent infections). Using ciprofloxacin or levofloxacin empirically when local resistance exceeds 10% risks treatment failure in a population already at higher risk for poor outcomes.

7. **Obtaining urine culture from a colonized indwelling catheter.** Biofilm on an existing catheter yields colonizing organisms that may not represent the causative pathogen. Remove or replace the catheter and obtain the culture specimen from the new catheter. This single step improves diagnostic accuracy and has been shown to improve treatment outcomes.

8. **Discharging a patient with an obstructive stone and pyuria/fever.** An infected obstructing stone is a surgical emergency, not an outpatient antibiotics problem. Even if the patient appears well in the ED, they are at high risk for rapid clinical deterioration. These patients require admission, IV antibiotics, and urology consultation for decompression.

9. **Failing to broaden empiric coverage in healthcare-associated or catheter-related complicated UTI.** These infections have a higher prevalence of Pseudomonas, ESBL-producing organisms, and Enterococcus. Ceftriaxone alone may be insufficient. Use piperacillin-tazobactam 4.5 g IV q6h or meropenem 1 g IV q8h when healthcare-associated pathogens are likely.

10. **Not involving urology for first-episode complicated UTI.** Every patient with a first complicated UTI deserves urologic evaluation for underlying structural or functional abnormality. Recurrent complicated UTI without workup means missing correctable pathology — strictures, stones, reflux, neurogenic bladder, or malignancy.
