---
id: hypophosphatemia-severe
condition: Severe Hypophosphatemia
aliases: [hypophosphatemia, phosphate depletion, severe phosphorus deficiency, refeeding hypophosphatemia]
icd10: [E83.39]
esi: 2
time_to_harm:
  irreversible_injury: "< 24 hours"
  death: "< 48 hours"
  optimal_intervention_window: "< 6 hours"
category: endocrine-metabolic
track: tier1
sources:
  - type: guideline
    ref: "Geerse S et al. Treatment of hypophosphatemia in the intensive care unit: a review. Crit Care. 2010;14(4):R147"
  - type: guideline
    ref: "Marinella MA. Refeeding Syndrome and Hypophosphatemia. J Intensive Care Med. 2005;20(3):155-159"
  - type: consensus-statement
    ref: "Gaasbeek A, Meinders AE. Hypophosphatemia: an update on its etiology and treatment. Am J Med. 2005;118(10):1094-1101"
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
# Severe Hypophosphatemia

## Recognition

**Severity classification:**
- Mild: 2.0-2.5 mg/dL (0.65-0.81 mmol/L) — usually asymptomatic
- Moderate: 1.0-2.0 mg/dL (0.32-0.65 mmol/L) — may have symptoms
- Severe: < 1.0 mg/dL (< 0.32 mmol/L) — life-threatening; symptomatic

**Clinical manifestations (typically only when PO4 < 1.0 mg/dL):**
- **Neuromuscular:** weakness (generalized, proximal), rhabdomyolysis, respiratory muscle failure (difficulty weaning from ventilator), paresthesias, tremor, seizures, encephalopathy, coma
- **Hematologic:** hemolytic anemia (ATP depletion → RBC membrane rigidity), platelet dysfunction, leukocyte dysfunction
- **Cardiac:** cardiomyopathy, decreased cardiac output, arrhythmias
- **Respiratory:** respiratory failure from diaphragmatic weakness; failure to wean from mechanical ventilation
- **Metabolic:** impaired oxygen delivery (decreased 2,3-DPG → left-shifted oxyhemoglobin curve)

**Common etiologies:**
- **Refeeding syndrome** (most dangerous context): nutrition resumed after prolonged starvation → insulin surge → intracellular phosphate shift
- **Chronic alcoholism** (poor intake + increased renal losses)
- **DKA treatment** (insulin drives phosphate intracellularly)
- **Respiratory alkalosis** (intracellular phosphate shift)
- **Hungry bone syndrome** (post-parathyroidectomy; calcium and phosphate rapidly deposited in bone)
- **Medications:** antacids (aluminum/magnesium bind phosphate in gut), acetazolamide, insulin, corticosteroids, catecholamines
- **Vitamin D deficiency**
- **Sepsis/critical illness**

## Critical Actions

1. **IV phosphate replacement** for severe hypophosphatemia (< 1.0 mg/dL) or any symptomatic patient
2. **Potassium phosphate or sodium phosphate IV:** 0.08-0.16 mmol/kg (5-10 mg/kg) over 6 hours; use potassium phosphate if K low, sodium phosphate if K normal/high
3. **Recheck phosphorus and calcium q6h** during replacement — hypocalcemia is the main risk of rapid phosphate infusion
4. **Treat underlying cause** — refeeding: slow nutrition advancement; DKA: phosphate will partially correct with insulin and hydration
5. **Monitor for respiratory failure** — severe hypophosphatemia causes diaphragmatic weakness; check FVC if symptomatic
6. **Supplemental potassium and magnesium** — commonly co-depleted

## Differential Diagnosis

- Refeeding syndrome (malnourished patient started on nutrition; hypophosphatemia + hypokalemia + hypomagnesemia)
- DKA (hyperglycemia, ketonemia; phosphate drops during treatment)
- Respiratory alkalosis-induced transcellular shift (hyperventilation; transient)
- Chronic alcoholism (multifactorial depletion)
- Hyperparathyroidism (elevated PTH, hypercalcemia, low phosphate)
- Vitamin D deficiency (low calcium, low phosphate, elevated PTH)
- Tumor-induced osteomalacia (FGF23-secreting tumor; low phosphate, low 1,25-D)
- Fanconi syndrome (proximal tubular dysfunction; glycosuria, aminoaciduria, phosphaturia)

## Workup

- **Serum phosphorus** — confirm severity; recheck q6h during IV replacement
- **Ionized calcium** — must monitor; IV phosphate can precipitate hypocalcemia
- **BMP:** potassium (co-depleted), magnesium (co-depleted), creatinine, glucose
- **Magnesium** — hypomagnesemia commonly coexists; must correct
- **CK** — rhabdomyolysis from hypophosphatemia
- **CBC with reticulocyte count, peripheral smear** — hemolytic anemia screen
- **ABG/VBG** — respiratory alkalosis as cause or consequence
- **PTH, 25-hydroxyvitamin D** — if etiology unclear
- **Urine phosphorus, fractional excretion of phosphate** — renal wasting (FEPhos > 5% with low serum = renal loss) vs GI/transcellular
- **Nutrition history** — assess refeeding risk (BMI < 16, prolonged NPO, anorexia nervosa, alcoholism)
- **LFTs, albumin, prealbumin** — nutritional assessment

## Treatment

### Severe (PO4 < 1.0 mg/dL) — IV Replacement Required
- **Potassium phosphate** 0.08-0.16 mmol/kg IV over 6 hours (if potassium < 4.0)
  - Example: 70 kg patient → 5.6-11.2 mmol phosphate over 6 hours
  - Maximum: 0.5 mmol/kg per 24 hours; max rate 7 mmol/hr
- **Sodium phosphate** — same dose; use if potassium elevated (> 5.0)
- Infusion rate: 1-3 mmol/hr (do NOT exceed 7 mmol/hr)
- Recheck phosphorus + calcium q6h; adjust infusion based on response
- Maximum infusion: no more than 30-45 mmol phosphate in 24 hours in most patients

### Moderate (PO4 1.0-2.0 mg/dL) — Oral or IV
- **Oral phosphate** (preferred if tolerating PO): Neutra-Phos 2 packets PO TID (500-750 mg elemental phosphorus per dose); or K-Phos Neutral 1-2 tablets PO TID
- **IV phosphate** if unable to take PO or critically ill: 0.08 mmol/kg over 6 hours

### Mild (PO4 2.0-2.5 mg/dL) — Oral Replacement
- Oral phosphate: Neutra-Phos 1-2 packets PO BID-TID
- Dietary counseling: dairy products, meat, nuts, whole grains
- Recheck in 24-48 hours

### Refeeding Syndrome Prevention
- Start nutrition slowly in at-risk patients: 10-20 kcal/kg/day, advance over 5-7 days
- Prophylactic phosphate, potassium, and magnesium replacement BEFORE starting nutrition
- Thiamine 200-300 mg IV BEFORE glucose/nutrition (prevents Wernicke)
- Monitor PO4, K, Mg daily for first 3-5 days of refeeding

### Concomitant Electrolyte Correction
- **Magnesium sulfate** 2 g IV over 1-2 hours (or MgO 400 mg PO BID)
- **Potassium:** replace to maintain K > 4.0 mEq/L
- Thiamine 200-300 mg IV in alcoholics/malnourished before any glucose

### Special Situations
- **DKA:** phosphate drops during insulin treatment; replace if < 1.0 or symptomatic. Do NOT routinely replace in mild hypophosphatemia during DKA (usually self-corrects).
- **Ventilator weaning failure:** check phosphorus; correct to > 2.0 before attributing failure to other causes.

## Disposition

- **PO4 < 1.0 mg/dL or symptomatic:** inpatient admission with IV replacement and q6h monitoring
- **PO4 1.0-2.0, asymptomatic, tolerating PO:** may treat in ED with oral phosphate, discharge with recheck in 24-48h
- **Refeeding syndrome:** admission to monitored bed; daily electrolytes for minimum 5 days
- **Respiratory failure from hypophosphatemia:** ICU with mechanical ventilation support
- **Rhabdomyolysis from hypophosphatemia:** admission per rhabdomyolysis protocol

## Pitfalls

1. **Not checking phosphorus in at-risk populations.** Phosphorus is not included on basic metabolic panels in many hospitals. It must be specifically ordered. Alcoholics, malnourished patients, DKA patients on treatment, and ICU patients on continuous renal replacement are all at high risk.

2. **Rapid IV phosphate infusion.** Infusion rates > 7 mmol/hr risk acute hypocalcemia (calcium phosphate precipitation), hyperphosphatemia rebound, and metastatic calcification. Slow is safe.

3. **Not correcting magnesium concurrently.** Magnesium depletion commonly accompanies phosphate depletion and impairs phosphate repletion. Correct both simultaneously.

4. **Starting full nutrition in a malnourished patient without electrolyte monitoring.** Refeeding syndrome occurs within 24-72 hours of nutrition initiation. Prophylactic electrolyte replacement and slow caloric advancement prevent this potentially fatal complication.

5. **Attributing ventilator weaning failure to pulmonary disease.** Severe hypophosphatemia causes diaphragmatic weakness. Any intubated patient who fails to wean should have phosphorus checked and corrected before attributing the failure to other causes.

6. **Oral phosphate in patients with nausea/diarrhea.** Oral phosphate supplements frequently cause nausea and diarrhea, limiting absorption. If the patient is already vomiting or has GI issues, use IV replacement.
