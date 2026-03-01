---
id: hypercalcemia-emergency
condition: Hypercalcemia Emergency
aliases: [hypercalcemic crisis, severe hypercalcemia, malignant hypercalcemia, calcium crisis]
icd10: [E83.52]
esi: 2
time_to_harm:
  irreversible_injury: "< 24 hours"
  death: "< 48 hours"
  optimal_intervention_window: "< 6 hours"
category: endocrine-metabolic
track: tier1
sources:
  - type: guideline
    ref: "Society for Endocrinology. Endocrine Emergency Guidance: Emergency management of acute hypercalcaemia in adult patients. Endocr Connect. 2016;5(5):G9-G11"
  - type: guideline
    ref: "Minisola S et al. Investigation and management of hypercalcaemia. BMJ. 2024;386:e077523"
  - type: guideline
    ref: "Mirrakhimov AE. Hypercalcemia of Malignancy: An Update on Pathogenesis and Management. N Am J Med Sci. 2015;7(11):483-493"
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
# Hypercalcemia Emergency

## Recognition

**Severity classification (corrected calcium):**
- Mild: 10.5-11.9 mg/dL (2.6-3.0 mmol/L) — often asymptomatic
- Moderate: 12.0-13.9 mg/dL (3.0-3.5 mmol/L) — symptomatic
- Severe / crisis: >= 14.0 mg/dL (>= 3.5 mmol/L) — life-threatening

**Corrected calcium = measured Ca + 0.8 x (4.0 - albumin)**

**Clinical presentation ("stones, bones, groans, thrones, and psychiatric overtones"):**
- **Renal:** polyuria, polydipsia, nephrolithiasis, acute kidney injury
- **GI:** nausea, vomiting, constipation, anorexia, pancreatitis, ileus
- **Neuropsychiatric:** confusion, lethargy, psychosis, coma, muscle weakness
- **Cardiac:** shortened QT interval, ST elevation (mimics STEMI), bradycardia, heart block, cardiac arrest
- **Musculoskeletal:** bone pain, pathologic fractures

**Common etiologies (>90% due to 2 causes):**
- Primary hyperparathyroidism (most common outpatient cause; mild-moderate elevation)
- Malignancy-associated (most common inpatient cause; often severe): humoral (PTHrP), osteolytic metastases, 1,25-dihydroxyvitamin D production (lymphoma)
- Other: granulomatous disease (sarcoidosis, TB), vitamin D toxicity, thiazide diuretics, immobilization, milk-alkali syndrome, thyrotoxicosis

## Critical Actions

1. **Aggressive IV fluid resuscitation** — NS 200-500 mL/hr (goal 3-6 L in first 24h); adjust for cardiac/renal reserve
2. **Calcitonin 4 IU/kg SQ or IM q12h** — rapid onset (2-4 hours); bridges to bisphosphonate effect; tachyphylaxis after 48-72h
3. **Zoledronic acid 4 mg IV over 15 min** — definitive antiresorptive; onset 2-4 days, peak effect 4-7 days
4. **Correct hypokalemia and hypomagnesemia** before calcium correction
5. **ECG** — monitor for short QT, arrhythmias; continuous telemetry if Ca > 14
6. **Identify underlying cause** — PTH, PTHrP, vitamin D metabolites

## Differential Diagnosis

- Pseudohypercalcemia (tourniquet artifact, paraproteinemia)
- Primary hyperparathyroidism (elevated PTH, mild-moderate calcium)
- Malignancy-associated hypercalcemia (suppressed PTH, elevated PTHrP or 1,25-D)
- Granulomatous disease (sarcoidosis, TB — elevated 1,25-dihydroxyvitamin D)
- Vitamin D toxicity (supplement history, elevated 25-hydroxyvitamin D)
- Thiazide diuretics (medication history)
- Thyrotoxicosis (elevated T3/T4, suppressed TSH)
- Milk-alkali syndrome (calcium supplement + antacid history)
- Immobilization (prolonged bedrest, especially in Paget disease)
- Adrenal insufficiency (coexisting features)

## Workup

- **Ionized calcium** — most accurate; not affected by albumin
- **Corrected total calcium** — if ionized not immediately available
- **PTH (intact)** — elevated = hyperparathyroidism; suppressed = malignancy or other
- **PTHrP** — elevated in humoral hypercalcemia of malignancy
- **25-hydroxyvitamin D** — elevated in vitamin D toxicity
- **1,25-dihydroxyvitamin D** — elevated in granulomatous disease and lymphoma
- **BMP:** creatinine (AKI), potassium, magnesium, phosphate
- **Phosphate** — low in hyperparathyroidism; variable in malignancy
- **CBC** — anemia, cytopenias (malignancy)
- **ECG** — short QT interval, Osborn waves, arrhythmia
- **CXR** — pulmonary mass, lymphadenopathy, granulomatous disease
- **SPEP, UPEP** — multiple myeloma screen if unexplained
- **Lipase** — pancreatitis (complication of hypercalcemia)

## Treatment

### Volume Resuscitation (Immediate)
- **NS 200-500 mL/hr** — initial rate; goal 3-6 L in first 24 hours
- Reduce rate in elderly, CHF, renal failure — monitor for volume overload
- NS promotes calciuresis by inhibiting proximal tubular calcium reabsorption
- Monitor urine output (goal 200-300 mL/hr)

### Calcitonin (Rapid, Bridging)
- **Calcitonin (salmon)** 4 IU/kg SQ or IM q12h
- Onset 2-4 hours; calcium reduction 1-2 mg/dL
- Tachyphylaxis develops within 48-72 hours — NOT a standalone therapy
- No dose adjustment for renal impairment

### Bisphosphonates (Definitive Antiresorptive)
- **Zoledronic acid** 4 mg IV over 15 min — preferred; longer duration of action
- **Pamidronate** 60-90 mg IV over 2-4 hours — alternative; use 60 mg if Ca 12-13.5, 90 mg if Ca > 13.5
- Onset: 2-4 days; peak effect 4-7 days
- Contraindicated if CrCl < 30 mL/min (zoledronic acid); use denosumab instead

### Denosumab (Renal Failure)
- **Denosumab** 120 mg SQ — for patients with CrCl < 30 mL/min
- Onset: 4-10 days; peak 14-23 days
- Monitor for severe hypocalcemia (especially in renal failure)

### Loop Diuretics
- **Furosemide** 20-40 mg IV — ONLY after adequate volume resuscitation; NOT routine
- Promotes calciuresis; risk of volume depletion and electrolyte wasting
- Reserved for volume-overloaded patients or as adjunct to aggressive hydration

### Glucocorticoids (Specific Indications)
- **Hydrocortisone** 200 mg IV daily (or equivalent) — for granulomatous disease, lymphoma, vitamin D toxicity, myeloma
- Inhibits 1-alpha-hydroxylase (reduces 1,25-D production)
- Onset: 2-5 days; NOT useful in hyperparathyroidism

### Dialysis (Life-Threatening)
- Hemodialysis with low-calcium dialysate — for severe refractory hypercalcemia with renal failure or cardiac instability
- Most rapid method of calcium reduction

## Disposition

- **Ca >= 14 mg/dL or symptomatic:** inpatient admission with telemetry
- **Ca 12-14 mg/dL with mild symptoms:** 24h observation, initiate workup
- **Ca < 12 mg/dL, asymptomatic, known stable hyperparathyroidism:** outpatient follow-up
- **Suspected malignancy:** oncology consultation; staging workup
- **All admitted patients:** recheck calcium q6-12h until trending down

## Pitfalls

1. **Not correcting calcium for albumin.** Total calcium is falsely low in hypoalbuminemia (common in malignancy, critical illness). Use corrected calcium or ionized calcium for all clinical decisions.

2. **Giving furosemide before adequate hydration.** Furosemide without prior volume resuscitation worsens dehydration and hypercalcemia. Rehydrate first with 1-2 L NS, then consider furosemide only if volume-overloaded.

3. **Relying on calcitonin alone.** Calcitonin has rapid onset but tachyphylaxis within 48-72 hours makes it a bridge, not definitive therapy. Bisphosphonates or denosumab must be initiated simultaneously.

4. **Not checking PTH and PTHrP early.** The workup determines the cause and guides definitive treatment. PTH must be drawn before IV fluids normalize calcium (dilution effect).

5. **Forgetting ECG in moderate-to-severe hypercalcemia.** Short QT interval, arrhythmias, and heart block are life-threatening complications. Continuous telemetry is required for Ca >= 14 mg/dL.

6. **Using bisphosphonates in severe renal failure.** Zoledronic acid is nephrotoxic and contraindicated with CrCl < 30 mL/min. Use denosumab instead, with close monitoring for rebound hypocalcemia.
