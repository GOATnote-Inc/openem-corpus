---
id: hyponatremia-severe
condition: Severe Hyponatremia
aliases: [acute hyponatremia, symptomatic hyponatremia, severe hyponatremia, water intoxication, hyponatremic encephalopathy]
icd10: [E87.1]
esi: 2
time_to_harm:
  irreversible_injury: "< 6 hours"
  death: "< 24 hours"
  optimal_intervention_window: "< 1 hour"
category: endocrine-metabolic
track: tier1
sources:
  - type: guideline
    ref: "Spasovski G et al. Clinical practice guideline on diagnosis and treatment of hyponatraemia. Eur J Endocrinol. 2014;170(3):G1-G47"
  - type: guideline
    ref: "Sterns RH. Treatment Guidelines for Hyponatremia: Stay the Course. Clin J Am Soc Nephrol. 2024;19(1):129-135"
  - type: guideline
    ref: "Verbalis JG et al. Diagnosis, Evaluation, and Treatment of Hyponatremia: Expert Panel Recommendations. Am J Med. 2013;126(10 Suppl 1):S1-S42"
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
# Severe Hyponatremia

## Recognition

**Severity classification:**
- Mild: Na 130-135 mEq/L — often asymptomatic
- Moderate: Na 120-129 mEq/L — nausea, confusion, headache
- Severe: Na < 120 mEq/L — seizures, coma, respiratory arrest, brain herniation

**Symptoms by severity:**
- **Moderate:** nausea, headache, confusion, gait instability, falls
- **Severe:** vomiting, seizures, obtundation, coma, noncardiogenic pulmonary edema, respiratory arrest, brain herniation (cerebral edema)

**Acuity matters more than absolute level:**
- Acute (< 48 hours): higher risk of cerebral edema and herniation; more aggressive correction indicated
- Chronic (> 48 hours): brain has adapted; more vulnerable to osmotic demyelination syndrome (ODS) with rapid correction
- Unknown duration: treat as chronic unless strong evidence of acute onset

**Common etiologies:**
- Hypovolemic: diuretics (especially thiazides), vomiting, diarrhea, third-spacing
- Euvolemic: SIADH (most common inpatient cause), hypothyroidism, adrenal insufficiency, water intoxication (psychogenic polydipsia, ecstasy/MDMA use)
- Hypervolemic: CHF, cirrhosis, nephrotic syndrome, advanced renal failure

## Critical Actions

1. **If severe symptoms (seizures, coma, herniation):** 3% hypertonic saline 100 mL IV bolus over 10 minutes; may repeat up to 3 times (max 300 mL) until symptoms improve
2. **Target initial correction:** raise Na 4-6 mEq/L in first 1-2 hours (sufficient to reverse life-threatening symptoms)
3. **Maximum correction rate:** < 8 mEq/L in first 24 hours; < 18 mEq/L in first 48 hours (to prevent ODS)
4. **Check serum Na q2h** during active correction
5. **Identify and treat underlying cause** — volume status assessment, serum and urine osmolality, urine sodium
6. **Desmopressin clamp** if overcorrection occurs or anticipated

## Differential Diagnosis

- Pseudohyponatremia (hyperglycemia, hyperlipidemia, paraproteinemia — check serum osmolality)
- Hyperglycemia-induced hyponatremia (correct Na: add 1.6 mEq/L for each 100 mg/dL glucose above 100)
- Hypothyroidism (check TSH)
- Adrenal insufficiency (check cortisol, ACTH)
- SIADH (euvolemic, urine osm > 100, urine Na > 40)
- Beer potomania (low solute intake)
- Cerebral salt wasting (post-neurosurgery, hypovolemic)
- Drug-induced SIADH (SSRIs, carbamazepine, cyclophosphamide, oxytocin, ecstasy)

## Workup

- **Serum sodium** — confirm on BMP; recheck q2h during treatment
- **Serum osmolality** — low (< 280 mOsm/kg) = true hypotonic hyponatremia; normal/high = pseudohyponatremia
- **Urine osmolality** — > 100 mOsm/kg = impaired water excretion; < 100 = appropriate dilution (psychogenic polydipsia)
- **Urine sodium** — < 20 mEq/L = hypovolemic; > 40 mEq/L = SIADH, adrenal insufficiency, or diuretics
- **Glucose** — correct Na for hyperglycemia (+1.6 mEq/L per 100 mg/dL glucose above 100)
- **TSH, cortisol** — exclude hypothyroidism and adrenal insufficiency
- **CBC, BMP, LFTs, BNP** — assess for underlying disease (CHF, cirrhosis)
- **Uric acid** — low in SIADH
- **CT head** — if altered mental status, seizure, or suspicion for cerebral edema or CNS pathology

## Treatment

### Severe Symptomatic (Seizures, Coma, Herniation)
- **3% hypertonic saline 100 mL IV bolus over 10 minutes**
- Repeat q10 min up to 3 times (max 300 mL) if symptoms persist
- Goal: raise Na 4-6 mEq/L in first 1-2 hours
- Check Na after each bolus
- Switch to slow correction once symptoms resolve

### Moderate Symptomatic (Nausea, Confusion, Headache)
- **3% hypertonic saline** continuous infusion: start 0.5-2 mL/kg/hr
- Alternatively: 3% NaCl 100 mL over 10 min single bolus
- Target: raise Na by 4-6 mEq/L in first 6 hours
- Check Na q2-4h

### Correction Rate Limits
- **Maximum 8 mEq/L in 24 hours** (10 mEq/L per European guidelines; 8 mEq/L per some US experts for high-risk patients)
- **Maximum 18 mEq/L in 48 hours**
- High-risk for ODS: hypokalemia, alcoholism, malnutrition, liver disease, Na < 105 — target < 6 mEq/L in 24h

### Overcorrection Management (Desmopressin Clamp)
- **Desmopressin (DDAVP) 2 mcg IV q6-8h** — re-lowers sodium by promoting free water retention
- Administer D5W 3-6 mL/kg/hr IV to re-lower Na
- Initiate proactively if correction rate exceeds target
- Particularly important when cause is removed (e.g., thiazide stopped, volume repleted) — sodium can autocorrect rapidly

### Cause-Specific Treatment
- **SIADH:** fluid restriction 800-1000 mL/day; tolvaptan 15 mg PO daily (vasopressin receptor antagonist; monitor Na q6h for first 24h — cannot use hypertonic saline simultaneously)
- **Hypovolemic:** NS resuscitation (monitor for autocorrection as ADH suppression occurs)
- **Adrenal insufficiency:** hydrocortisone 100 mg IV
- **Hypothyroidism:** levothyroxine (chronic hyponatremia; not acutely corrective)
- **Hypervolemic (CHF, cirrhosis):** fluid restriction, diuretics, treat underlying cause

## Disposition

- **Na < 120 mEq/L or severe symptoms:** ICU with q2h sodium monitoring
- **Na 120-125 with moderate symptoms:** monitored bed, q4h sodium
- **Na 125-130, mild symptoms, identified cause:** may observe in ED, initiate treatment, and discharge with close outpatient follow-up if reliable
- **Any patient receiving hypertonic saline:** ICU for minimum 24 hours
- **Desmopressin clamp:** ICU monitoring

## Pitfalls

1. **Correcting too fast.** Overcorrection of chronic hyponatremia causes osmotic demyelination syndrome (ODS / central pontine myelinolysis) — devastating, irreversible quadriplegia and locked-in syndrome. Limit to < 8 mEq/L per 24 hours.

2. **Not anticipating autocorrection.** When the cause is removed (thiazide stopped, volume repleted, cortisol given), ADH suppression causes rapid water diuresis and can exceed safe correction rates within hours. Monitor urine output and Na closely.

3. **Using NS for symptomatic hyponatremia.** Normal saline (Na 154 mEq/L) may worsen hyponatremia in SIADH (urine osm > serum osm means NS free water is retained). Only 3% hypertonic saline reliably raises Na in symptomatic cases.

4. **Forgetting to correct for glucose.** Hyperglycemia causes osmotic water shift that dilutes sodium. Corrected Na = measured Na + 1.6 x (glucose - 100)/100. Treating hyperglycemia will raise sodium — factor this into correction rate calculations.

5. **Not checking urine osmolality and sodium.** These two tests distinguish the cause of hyponatremia (SIADH vs. volume depletion vs. polydipsia). Without them, treatment is a guess.

6. **Administering tolvaptan with hypertonic saline.** Concurrent use causes unpredictable, potentially dangerous overcorrection. Use one or the other — never both.
