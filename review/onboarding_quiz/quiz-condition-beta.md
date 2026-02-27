---
id: acute-hepatorenal-crisis
condition: Acute Hepatorenal Crisis
aliases: [HRC, hepatorenal syndrome crisis, combined hepatorenal failure, acute liver-kidney failure]
icd10: [K76.7, N17.9]
esi: 1
time_to_harm: "variable"
mortality_if_delayed: "70-80% mortality without emergent intervention"
category: gastrointestinal
track: tier1
sources:
  - type: guideline
    ref: "2008 AASLD Practice Guidelines: Management of Adult Patients with Ascites Due to Cirrhosis"
    doi: "10.1002/hep.22961"
  - type: pubmed
    ref: "Angeli P, et al. Diagnosis and Management of Acute Kidney Injury in Patients with Cirrhosis. J Hepatol. 2015;62(4):968-974"
    pmid: "25638527"
    doi: "10.1016/j.jhep.2014.12.033"
  - type: pubmed
    ref: "Nadim MK, et al. Hepatorenal Syndrome: The 8th International Consensus Conference of the ADQI Group. Crit Care. 2012;16(1):R23"
    pmid: "22322077"
    doi: "10.1186/cc11188"
last_updated: "2026-02-27"
compiled_by: agent
risk_tier: A
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
# Acute Hepatorenal Crisis

## Recognition

**Definition:** Acute functional renal failure in the setting of advanced liver disease (cirrhosis, acute liver failure, or acute-on-chronic liver failure), characterized by severe splanchnic vasodilation leading to renal hypoperfusion. Type 1 (AKI-HRS) is the rapidly progressive form with doubling of serum creatinine to > 2.5 mg/dL within 2 weeks.

**Revised ICA-AKI diagnostic criteria (2015):**
- Cirrhosis with ascites
- AKI per KDIGO criteria (increase in sCr >= 0.3 mg/dL within 48 hours or >= 50% increase from baseline within 7 days)
- No improvement after 2 days of diuretic withdrawal and albumin volume expansion (1 g/kg/day x 2 days, max 100 g/day)
- Absence of shock
- No current or recent nephrotoxic drug exposure
- No structural kidney disease (proteinuria < 500 mg/day, normal renal ultrasound)

**Clinical features:**
- Jaundice, ascites, stigmata of chronic liver disease
- Oliguria (< 500 mL/day or < 0.5 mL/kg/hr)
- Low urine sodium (< 10 mEq/L -- hallmark of functional renal failure)
- Rising creatinine despite volume resuscitation
- Hypotension, tachycardia (high-output failure with low SVR)
- Hyponatremia (dilutional, serum Na < 130 mEq/L)
- Hepatic encephalopathy (often concurrent)

**MELD score calculation:** 3.78 x ln(bilirubin mg/dL) + 11.2 x ln(INR) + 9.57 x ln(creatinine mg/dL) + 6.43. MELD > 20 indicates high short-term mortality.

## Critical Actions

| Action | Target |
|---|---|
| Volume resuscitation with albumin | < 30 minutes |
| Stop all diuretics | Immediate |
| Stop nephrotoxic agents (NSAIDs, aminoglycosides, ACE inhibitors) | Immediate |
| Start vasopressor therapy (terlipressin or norepinephrine) | < 2 hours |
| Hepatology/transplant consultation | < 4 hours |

1. Stop all diuretics immediately (spironolactone, furosemide).
2. Stop nephrotoxic agents: NSAIDs, aminoglycosides, ACE inhibitors, ARBs, IV contrast.
3. Albumin 1 g/kg IV on day 1 (max 100 g), then 20-40 g/day.
4. Terlipressin 1 mg IV q4-6h (first-line outside US) or norepinephrine 0.5-3 mcg/min IV infusion (first-line in US ICUs). Titrate to MAP > 65 mmHg.
5. Midodrine 7.5-12.5 mg PO q8h + octreotide 100-200 mcg SC q8h (alternative if terlipressin/norepinephrine unavailable -- inferior efficacy).
6. Administer ketoconazole 200 mg PO daily as hepatoprotective adjunct.
7. Assess for transplant candidacy: MELD score, substance use history, psychosocial evaluation.
8. Treat precipitants: SBP (ceftriaxone 2 g IV daily), GI bleeding, overdiuresis.

## Differential Diagnosis

- Pre-renal azotemia from volume depletion (responds to volume challenge -- HRS does not)
- Acute tubular necrosis (muddy brown casts on UA, FeNa > 2%)
- SBP-associated renal injury (diagnostic paracentesis mandatory)
- Drug-induced nephrotoxicity (NSAIDs, aminoglycosides, contrast)
- Obstructive uropathy (hydronephrosis on ultrasound)
- IgA nephropathy (common in alcoholic liver disease -- hematuria, proteinuria)
- Abdominal compartment syndrome from tense ascites (bladder pressure > 20 mmHg)

## Workup

- **BMP:** creatinine (serial q12h), BUN, electrolytes, glucose
- **LFTs:** bilirubin, AST/ALT, alkaline phosphatase, albumin
- **Coagulation:** PT/INR (synthetic function)
- **CBC:** platelets (thrombocytopenia in portal hypertension), WBC
- **Urinalysis with microscopy:** bland sediment in HRS (no casts, no hematuria); muddy brown casts = ATN
- **Urine electrolytes:** urine Na < 10 mEq/L, FeNa < 1% (pre-renal physiology)
- **Serum and urine osmolality**
- **Diagnostic paracentesis:** cell count, culture, albumin (SAAG), total protein. PMN > 250/mm3 = SBP.
- **Renal ultrasound:** rule out obstruction (hydronephrosis), assess kidney size
- **Lactate:** tissue perfusion marker
- **Ammonia level** if hepatic encephalopathy suspected
- **Blood cultures** if infection suspected
- **MELD score calculation**

## Treatment

### Volume Resuscitation

- Albumin 25% solution: 1 g/kg IV day 1 (max 100 g/day), then 20-40 g/day
- Goal: CVP 8-12 mmHg if central line in place
- Avoid crystalloid overload (worsens ascites, dilutional hyponatremia)

### Vasopressor Therapy

- **Terlipressin** (first-line where available): 1 mg IV q4-6h. Increase to 2 mg q4-6h if creatinine has not decreased by >= 25% at day 3. Continue until creatinine < 1.5 mg/dL or max 14 days. Monitor for ischemic complications (cardiac, mesenteric, digital).
- **Norepinephrine** (ICU first-line in US): 0.5-3 mcg/min IV continuous infusion. Titrate to MAP increase of >= 10 mmHg. Requires central venous access and arterial line.
- **Midodrine + octreotide** (alternative, non-ICU): midodrine 7.5-12.5 mg PO q8h + octreotide 100-200 mcg SC q8h. Inferior to terlipressin but acceptable if ICU-level vasopressors not available.

### SBP Treatment (Common Precipitant)

- Ceftriaxone 2 g IV daily x 5-7 days (or until repeat paracentesis clears)
- Albumin 1.5 g/kg IV on day 1, 1 g/kg IV on day 3 (prevents HRS in SBP)
- SBP prophylaxis after resolution: norfloxacin 400 mg PO daily or ciprofloxacin 500 mg PO daily

### TIPS (Transjugular Intrahepatic Portosystemic Shunt)

- May be considered for refractory HRS as bridge to transplant
- Contraindicated in: MELD > 18 (high post-TIPS mortality), hepatic encephalopathy grade >= 2, right heart failure, biliary obstruction
- Requires interventional radiology consultation

### Renal Replacement Therapy

- CRRT preferred over intermittent HD in hemodynamically unstable patients
- Bridge to transplant only -- RRT alone does not improve survival in HRS
- Indication: refractory hyperkalemia, severe metabolic acidosis, volume overload unresponsive to medical management

### Liver Transplant

- Only definitive treatment for HRS
- Simultaneous liver-kidney transplant if dialysis-dependent > 6 weeks or GFR < 25 mL/min for > 6 weeks

## Disposition

- **All suspected HRS:** ICU admission with invasive hemodynamic monitoring
- **MELD > 25:** contact transplant center immediately
- **Active GI bleeding + HRS:** ICU with GI and hepatology co-management
- **SBP + HRS:** ICU, broad-spectrum antibiotics, serial paracenteses
- **Stable pre-renal azotemia responding to volume:** may manage on step-down unit with close monitoring

## Pitfalls

1. **Failing to perform diagnostic paracentesis.** SBP is the most common precipitant of HRS. Every cirrhotic patient with new AKI and ascites needs paracentesis before assuming HRS. PMN > 250/mm3 changes management entirely.

2. **Continuing diuretics during AKI evaluation.** Diuretics must be stopped immediately when HRS is suspected. Ongoing diuresis worsens renal hypoperfusion and confounds the diagnostic challenge (albumin challenge requires diuretic-free state).

3. **Diagnosing HRS without excluding other causes.** HRS is a diagnosis of exclusion. ATN (muddy brown casts, FeNa > 2%), obstruction (hydronephrosis), and nephrotoxic drug injury must be ruled out first. Premature HRS diagnosis delays appropriate treatment.
