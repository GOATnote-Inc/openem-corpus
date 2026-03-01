---
id: hypernatremia-severe
condition: Severe Hypernatremia
aliases: [acute hypernatremia, severe hypernatremia, hypernatremic dehydration, sodium excess]
icd10: [E87.0]
esi: 2
time_to_harm:
  irreversible_injury: "< 12 hours"
  death: "< 48 hours"
  optimal_intervention_window: "< 6 hours"
category: endocrine-metabolic
track: tier1
sources:
  - type: guideline
    ref: "Sterns RH. Hypernatremia. In: UpToDate (based on systematic review). 2024"
  - type: guideline
    ref: "Muhsin SA, Mount DB. Evaluation and management of hypernatremia in adults: clinical perspectives. Korean J Intern Med. 2023;38(3):290-302"
  - type: consensus-statement
    ref: "Adrogue HJ, Madias NE. Hypernatremia. N Engl J Med. 2000;342(20):1493-1499"
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
# Severe Hypernatremia

## Recognition

**Severity classification:**
- Mild: Na 146-150 mEq/L
- Moderate: Na 151-159 mEq/L
- Severe: Na >= 160 mEq/L (high mortality: 40-60% when Na > 160)

**Clinical presentation (primarily neurologic — brain shrinkage):**
- Irritability, restlessness (early)
- Lethargy, confusion, obtundation
- Hyperreflexia, muscle twitching, tremor
- Seizures (usually on overcorrection, not from hypernatremia itself)
- Coma (Na > 160)
- Intracerebral hemorrhage (bridging veins torn from brain shrinkage)
- Fever (hypothalamic dysfunction)
- Intense thirst (preserved sensorium patients)

**Common etiologies:**
- **Decreased water intake** (most common): elderly with impaired thirst, altered mental status, restricted access to water, intubated ICU patients
- **Increased water losses:** diabetes insipidus (central or nephrogenic), osmotic diuresis (hyperglycemia, mannitol, urea), diarrhea, insensible losses (fever, burns)
- **Sodium excess** (rare): iatrogenic (hypertonic saline, sodium bicarbonate), salt ingestion, hyperaldosteronism, Cushing syndrome

## Critical Actions

1. **Assess volume status** — if hypovolemic with hemodynamic instability, resuscitate with NS FIRST (before free water correction)
2. **Calculate free water deficit:** FWD = TBW x [(Na/140) - 1], where TBW = 0.6 x body weight (men) or 0.5 x body weight (women)
3. **Determine acuity and set correction rate:**
   - Acute (< 48h): correct Na rapidly, 1-2 mEq/L/hr (risk of cerebral edema low; brain has not adapted)
   - Chronic (> 48h or unknown): correct no faster than 10-12 mEq/L per 24 hours (brain has adapted; rapid correction causes cerebral edema)
4. **Administer free water** — enteral preferred (oral or NG tube); D5W IV if enteral not feasible
5. **Monitor Na q2-4h** during correction
6. **Treat underlying cause** — diabetes insipidus, remove offending agent, address impaired water access

## Differential Diagnosis

- Diabetes insipidus — central (low ADH, responds to desmopressin) vs nephrogenic (ADH-resistant)
- Osmotic diuresis (DKA, mannitol, urea) — elevated serum osmolality with polyuria
- Dehydration (pure water loss) — elderly, infants, impaired thirst
- Iatrogenic sodium loading (sodium bicarbonate, hypertonic saline)
- Hyperaldosteronism (hypertension, hypokalemia)
- Cushing syndrome (cortisol excess)
- Essential hypernatremia (reset osmostat — rare)

## Workup

- **BMP:** sodium, potassium, glucose, BUN, creatinine, bicarbonate
- **Serum osmolality** — elevated (> 295 mOsm/kg)
- **Urine osmolality and urine sodium:**
  - High urine osm (> 600) + low urine Na: extrarenal water loss (dehydration, GI losses)
  - Low urine osm (< 300): diabetes insipidus
  - High urine osm + high urine Na: sodium loading or osmotic diuresis
- **Urine output monitoring** — polyuria suggests DI or osmotic diuresis
- **Desmopressin challenge** (1-2 mcg IV/SQ): if urine osm increases > 50% → central DI; if no response → nephrogenic DI
- **Glucose** — hyperglycemia with osmotic diuresis
- **CT head** — if altered mental status, to exclude intracranial hemorrhage (complication of brain shrinkage)
- **Pituitary MRI** — if central DI suspected (not emergent)

## Treatment

### Volume Resuscitation (If Hemodynamically Unstable)
- **NS (0.9% NaCl) IV bolus** — restores intravascular volume first
- Do NOT use free water (D5W) as initial resuscitation in shock — does not remain intravascular
- Once hemodynamically stable, transition to free water replacement

### Free Water Replacement
- **Enteral free water** (oral or NG tube) — preferred; most physiologic
- **D5W IV** — if enteral not feasible; remember D5W is effectively free water once dextrose metabolized
- **Half-normal saline (0.45% NaCl)** — alternative; provides 50% free water
- **Rate calculation:** administer calculated free water deficit over 48-72 hours (for chronic) PLUS ongoing losses

### Correction Rate
- **Acute hypernatremia (< 48h):** 1-2 mEq/L/hr correction; may target normalization within 24h
- **Chronic hypernatremia (> 48h or unknown):** max 10-12 mEq/L per 24 hours
- **Overcorrection risk:** cerebral edema and seizures from rapid correction of chronic hypernatremia
- Monitor Na q2-4h and adjust infusion rate

### Diabetes Insipidus
- **Central DI:** desmopressin 1-2 mcg IV/SQ q12h or 10-20 mcg intranasal; titrate to urine output
- **Nephrogenic DI:** remove offending agent (lithium, amphotericin); thiazide diuretics paradoxically reduce urine output (hydrochlorothiazide 25 mg PO daily); low-sodium diet; NSAIDs (indomethacin 25 mg PO TID) for severe cases
- Continue free water replacement while treating DI

### Ongoing Losses
- Account for insensible losses: ~10 mL/kg/day; increase for fever, tachypnea
- Account for urinary losses: match urine free water clearance
- Total fluid = free water deficit + maintenance + ongoing losses

## Disposition

- **Na >= 160 or neurologic symptoms:** ICU with q2-4h sodium monitoring
- **Na 150-159, mild symptoms, identified cause:** monitored bed, q4-6h sodium
- **Na < 150, asymptomatic, clear etiology (dehydration):** may treat in ED and arrange close follow-up if reliable
- **Central DI, new diagnosis:** endocrinology consultation, pituitary MRI as inpatient
- **All patients receiving IV free water:** admission for sodium monitoring

## Pitfalls

1. **Correcting chronic hypernatremia too fast.** Rapid correction of chronic hypernatremia (> 12 mEq/L in 24h) causes cerebral edema and seizures. The brain has accumulated idiogenic osmoles; these take time to dissipate.

2. **Using D5W for initial resuscitation in shock.** D5W distributes throughout total body water and provides minimal intravascular volume expansion. Resuscitate with NS first, then transition to free water once hemodynamically stable.

3. **Not accounting for ongoing losses.** Free water deficit calculations assume a closed system. Patients with diabetes insipidus, osmotic diuresis, or ongoing GI losses will continue to lose free water. The infusion rate must include deficit + maintenance + ongoing losses.

4. **Missing diabetes insipidus.** Polyuria with dilute urine (< 300 mOsm/kg) in the setting of hypernatremia is DI until proven otherwise. A desmopressin challenge distinguishes central from nephrogenic DI and guides treatment.

5. **Forgetting to monitor sodium frequently.** Hypernatremia correction requires q2-4h sodium checks. Undercorrection prolongs the dangerous state; overcorrection causes cerebral edema. Adjust infusion rates based on each measurement.

6. **Not addressing the underlying cause of impaired water access.** Many cases of hypernatremia in the elderly and hospitalized are preventable. Ensure patients have access to free water and can request it.
