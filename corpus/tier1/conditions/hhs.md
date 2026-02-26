---
id: hhs
condition: Hyperosmolar Hyperglycemic State
aliases: [HHS, hyperosmolar hyperglycemic nonketotic coma, HHNC, HONK, hyperosmolar nonketotic state]
icd10: [E11.00, E11.01]
esi: 1
time_to_harm: "< 24 hours"
mortality_if_delayed: "5-20% overall; exceeds DKA mortality by 5-10x"
category: endocrine-metabolic
track: tier1
sources:
  - type: guideline
    ref: "2009 ADA Consensus Statement: Hyperglycemic Crises in Adult Patients With Diabetes. Diabetes Care 2009;32(7):1335-1343"
  - type: review
    ref: "Kitabchi AE et al. Hyperglycemic Crises in Adult Patients With Diabetes. Diabetes Care 2009;32(7):1335-1343"
    pmid: "19564476"
  - type: review
    ref: "Pasquel FJ, Umpierrez GE. Hyperosmolar Hyperglycemic State: A Historic Review of the Clinical Presentation, Diagnosis, and Treatment. Diabetes Care 2014;37(11):3124-3131"
    pmid: "25342831"
  - type: review
    ref: "Fadini GP et al. Characteristics and Outcomes of the Hyperosmolar Hyperglycemic Syndrome in a Cohort of 51 Consecutive Cases at a Single Center. Diabetes Res Clin Pract 2011;94(2):172-179"
    pmid: "21752485"
  - type: guideline
    ref: "2023 ISPAD Clinical Practice Consensus Guidelines: DKA and Hyperglycemic Hyperosmolar State"
  - type: review
    ref: "Stoner GD. Hyperosmolar Hyperglycemic State. Am Fam Physician 2017;96(11):729-736"
    pmid: "29431405"
last_updated: "2026-02-19"
compiled_by: agent
reviewed_by: "Brandon Dent, MD — Board Certified Emergency Medicine"
review_date: "2026-02-27"
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
# Hyperosmolar Hyperglycemic State

## Recognition

**Diagnostic Criteria (all required):**
1. Glucose > 600 mg/dL
2. Effective serum osmolality > 320 mOsm/kg
3. pH > 7.30 and bicarb > 18 mEq/L (minimal or absent ketoacidosis)
4. Absent or small urine/serum ketones

**Effective serum osmolality** = 2[Na+] + glucose/18 (BUN excluded because it freely crosses cell membranes and does not contribute to tonicity).

**Presentation:**
- Insidious onset over days to weeks (unlike DKA which evolves in hours)
- Profound dehydration: average free water deficit 8-12 L (100-200 mL/kg)
- Altered mental status ranging from lethargy to coma (correlates with osmolality; obtundation typical when osmolality > 340 mOsm/kg)
- Tachycardia, hypotension, orthostasis, poor skin turgor, dry mucous membranes
- Focal neurologic deficits (hemiparesis, hemianopia, aphasia) that reverse with treatment — often mistaken for stroke
- Seizures (focal or generalized) in 10-25% of cases
- No Kussmaul respirations (no significant acidosis to compensate)
- No fruity breath (absent or minimal ketosis)
- Hypothermia is common; fever may be masked despite underlying infection

**Typical Patient:**
- Elderly (mean age 60-70 years), type 2 DM
- Nursing home resident or impaired access to free water (dementia, immobility, sedation)
- Often undiagnosed or undertreated DM
- Pediatric HHS is rare but carries high mortality (especially obese adolescents with new-onset type 2 DM)

**Precipitants:**
- Infection: 40-60% of cases (UTI, pneumonia, sepsis most common)
- Medication noncompliance or insulin omission
- New-onset diabetes (up to 20% of HHS presentations)
- Acute illness: MI, stroke, pancreatitis, PE
- Medications: glucocorticoids, thiazides, phenytoin, atypical antipsychotics (olanzapine, quetiapine), beta-blockers, calcium channel blockers
- Endocrine: Cushing syndrome, thyrotoxicosis, acromegaly
- Procedures: surgery, total parenteral nutrition, peritoneal dialysis with dextrose

**HHS-DKA Overlap:**
- Approximately 30% of patients present with features of both HHS and DKA (glucose > 600, osmolality > 320, AND pH < 7.30 or bicarb < 18 with ketosis)
- Overlap presentations carry higher mortality than either syndrome alone
- Treat with combined approach: aggressive fluids for HHS + insulin and gap-closing strategy for DKA

## Critical Actions

1. **Aggressive IV fluid resuscitation** — NS (0.9% NaCl) 1-1.5 L/hr for the first 1-2 hours (15-20 mL/kg/hr). This is the single most important intervention. Fluids alone reduce glucose by 75-100 mg/dL/hr via dilution and improved renal perfusion.
2. **Reassess corrected sodium after initial fluid bolus** — If corrected Na is high or normal: switch to 0.45% NS at 250-500 mL/hr. If corrected Na is low: continue NS at 250-500 mL/hr. Target total fluid replacement of 50% of estimated deficit in first 12 hours, remainder over next 12-24 hours.
3. **Check potassium before insulin** — If K < 3.3 mEq/L: hold insulin, give 20-40 mEq/hr KCl until K > 3.3. If K 3.3-5.3: give 20-30 mEq K per liter of IV fluids and start insulin. If K > 5.3: hold K replacement, recheck in 2 hours, start insulin.
4. **Insulin infusion at LOWER rate than DKA** — Regular insulin 0.05-0.1 units/kg/hr IV continuous (DKA uses 0.1-0.14 units/kg/hr). Do NOT bolus. Rapid glucose reduction causes osmolality to drop precipitously, risking cerebral edema. Target glucose decline: 50-75 mg/dL/hr (no faster).
5. **Add dextrose when glucose reaches 300 mg/dL** — Switch to D5 0.45% NS. Continue insulin to normalize osmolality. Target glucose 250-300 mg/dL until osmolality < 315 mOsm/kg and patient is alert.
6. **Thromboprophylaxis** — Enoxaparin 40 mg SC daily or heparin 5,000 units SC q8-12h. HHS confers high VTE risk due to hyperviscosity, immobility, and endothelial dysfunction.
7. **Search for precipitant** — Blood cultures, UA, CXR, ECG, troponin, lipase. Infection is the trigger in 40-60% of cases and may be masked by hypothermia.
8. **Monitor q1-2h** — Glucose, BMP (Na, K, Cl, bicarb), calculated osmolality, I/O, mental status. Serial neurologic checks for cerebral edema.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Diabetic ketoacidosis (DKA) | Glucose usually 250-600, pH < 7.30, bicarb < 18, elevated anion gap, significant ketosis, onset over hours (see `diabetic-ketoacidosis.md`) |
| HHS-DKA overlap | Glucose > 600 + osmolality > 320 + pH < 7.30 + ketosis; present in ~30% of hyperglycemic crises |
| Acute ischemic stroke | Focal deficits, but HHS itself causes reversible focal deficits (hemiparesis, aphasia); check glucose before calling stroke code |
| Sepsis with hyperglycemia | Glucose elevated but usually < 600, osmolality < 320, infection source identified; stress hyperglycemia |
| Myxedema coma | Altered mental status, hypothermia, but glucose normal or low, TSH elevated, no hyperosmolality |
| Uremic encephalopathy | AMS with elevated BUN/Cr, but no extreme hyperglycemia or hyperosmolality |
| Nonconvulsive status epilepticus | Prolonged AMS; EEG required to distinguish; HHS itself can cause seizures |

## Workup

**Point-of-Care:**
- Glucose (fingerstick) — note: many POC glucometers cap at 500-600 mg/dL and display "HIGH"; send serum glucose
- VBG (pH, pCO2, electrolytes)
- POC lactate (elevated suggests sepsis, tissue hypoperfusion, or mesenteric ischemia)
- Urinalysis (glucose, ketones, infection)
- ECG (peaked T waves for hyperkalemia, ischemia as precipitant, arrhythmia)

**Labs:**
- BMP: glucose, Na, K, Cl, bicarb, BUN, Cr
- Corrected Na = measured Na + 1.6 x [(glucose - 100) / 100] (critical — Na falsely depressed by hyperglycemia)
- Effective serum osmolality = 2[Na+] + glucose/18 (target: confirms > 320 mOsm/kg)
- Anion gap = Na - (Cl + HCO3) — elevated gap suggests DKA overlap, lactic acidosis, or AKI
- Beta-hydroxybutyrate (to quantify ketosis; < 3 mmol/L expected in pure HHS)
- CBC with differential (leukocytosis common from stress demargination; WBC > 25,000 raises concern for infection)
- Phosphate, magnesium, calcium (deplete during treatment)
- HbA1c (distinguishes chronic hyperglycemia from acute stress)
- Blood cultures x2 (if infection suspected)
- Procalcitonin (adjunct for bacterial infection when leukocytosis is ambiguous)
- Troponin (MI as precipitant)
- Lipase (pancreatitis as precipitant)
- Coagulation studies (PT/INR, PTT, fibrinogen) — DIC can complicate HHS
- CK (rhabdomyolysis from immobility and volume depletion)

**Imaging:**
- CXR (pneumonia as precipitant, pulmonary edema from aggressive fluids)
- CT head without contrast (if AMS out of proportion to osmolality, focal deficits persisting after glucose correction, or concern for cerebral edema)

## Treatment

### Phase 1: Resuscitation (0-2 hours)

**Fluids (highest priority):**
- NS (0.9% NaCl) 1-1.5 L/hr (15-20 mL/kg/hr) for 1-2 hours
- Average deficit is 8-12 L; do not attempt to replace all at once
- Titrate to hemodynamic response (MAP > 65, UOP > 0.5 mL/kg/hr)
- In elderly or heart failure patients: use smaller boluses (250-500 mL) with frequent reassessment for volume overload

**Potassium (before insulin):**
- K < 3.3 mEq/L: **HOLD insulin.** KCl 20-40 mEq/hr IV via central line (or 10 mEq/hr via peripheral IV). Recheck K q1h. Start insulin only after K > 3.3.
- K 3.3-5.3 mEq/L: KCl 20-30 mEq per liter of IV fluids. Start insulin.
- K > 5.3 mEq/L: Hold K replacement. Recheck in 2 hours. Start insulin (insulin will drive K intracellularly).

**Insulin:**
- Regular insulin 0.05-0.1 units/kg/hr IV continuous (NO bolus in HHS)
- Lower rate than DKA to avoid precipitous osmolality shifts
- Some protocols defer insulin for the first 1-2 hours, relying on fluids alone to reduce glucose, particularly if K is borderline low
- Target glucose decline: 50-75 mg/dL/hr. If glucose drops > 100 mg/dL/hr, reduce insulin rate by 50%.

### Phase 2: Continued Management (2-24 hours)

**Fluids:**
- After initial resuscitation, reassess corrected Na:
  - Corrected Na normal or high: 0.45% NS at 250-500 mL/hr
  - Corrected Na low: continue NS (0.9%) at 250-500 mL/hr
- When glucose reaches 300 mg/dL: switch to D5 0.45% NS at 150-250 mL/hr
- Target: replace 50% of estimated free water deficit in first 12 hours, remainder over next 12-24 hours
- Monitor I/O strictly; Foley catheter for accurate UOP

**Insulin:**
- Continue insulin infusion at 0.05-0.1 units/kg/hr
- When glucose reaches 300 mg/dL: reduce insulin to 0.02-0.05 units/kg/hr
- Do NOT stop insulin until: osmolality < 315 mOsm/kg AND patient is alert AND glucose < 300 mg/dL
- In HHS-DKA overlap: continue insulin until anion gap closes (< 12) as with DKA protocol

**Electrolyte Monitoring:**
- K: check q1-2h for first 6 hours, then q2-4h. Replace aggressively to target 4-5 mEq/L.
- Phosphate: replace if < 1.0 mg/dL — K-Phos 20-30 mmol IV over 6 hours (replaces K and PO4 simultaneously). Excessive phosphate replacement causes hypocalcemia.
- Magnesium: replace if < 1.5 mg/dL — MgSO4 2 g IV over 1 hour.

**Osmolality:**
- Recalculate effective osmolality q2h
- Target decline: 3-8 mOsm/kg/hr (no faster — rapid decline causes cerebral edema)
- If osmolality dropping > 8 mOsm/kg/hr: slow fluids, reduce insulin rate, add dextrose

### Thromboprophylaxis

- Enoxaparin 40 mg SC daily (CrCl > 30 mL/min) OR
- Heparin 5,000 units SC q8h (if CrCl < 30 mL/min or high bleeding risk)
- Continue until patient is ambulatory
- HHS carries higher VTE risk than DKA due to hyperviscosity and prolonged immobility

### Bicarbonate

- NOT routinely indicated in HHS (pH is typically > 7.30)
- If HHS-DKA overlap with pH < 6.9: NaHCO3 100 mEq in 400 mL sterile water + 20 mEq KCl, infuse at 200 mL/hr. Recheck VBG in 2 hours.

### Transition to Subcutaneous Insulin

- Give SC insulin 1-2 hours BEFORE stopping IV infusion (overlap prevents rebound hyperglycemia)
- Basal-bolus: 0.5-0.8 units/kg/day as 50% basal (glargine or detemir) + 50% bolus (lispro or aspart)
- Do not transition until: osmolality < 315 mOsm/kg, glucose < 300 mg/dL, patient is alert and eating, hemodynamically stable
- For patients not previously on insulin: start 0.3-0.5 units/kg/day (lower end for elderly, renal impairment)

## Disposition

**ICU Admission (mandatory for most HHS):**
- Osmolality > 320 mOsm/kg (by definition, all HHS at presentation)
- Altered mental status (GCS < 14)
- Hemodynamic instability (MAP < 65, requiring vasopressors, or UOP < 0.5 mL/kg/hr despite fluids)
- K < 3.3 mEq/L at presentation
- Glucose > 800 mg/dL
- Significant comorbidities (ACS, sepsis, acute stroke)
- HHS-DKA overlap (pH < 7.30 with hyperosmolality)

**Stepdown/Floor (rare at initial presentation):**
- Mild cases with improving osmolality and mental status after ED resuscitation
- Glucose trending reliably downward at 50-75 mg/dL/hr
- Stable hemodynamics, K > 3.5, no precipitant requiring ICU-level care
- Still requires telemetry and q2-4h lab monitoring

**Expected Hospital Course:**
- Longer than DKA: average 7-14 days (vs. 3-5 for DKA)
- Free water deficit takes days to fully correct
- Precipitant management often determines length of stay
- In-hospital mortality: 5-20% (predominantly in elderly with comorbidities)

## Pitfalls

1. **Treating HHS like DKA with high-dose insulin.** HHS requires LOWER insulin rates (0.05-0.1 units/kg/hr) compared to DKA (0.1-0.14 units/kg/hr). Aggressive insulin drops glucose rapidly without proportionally correcting osmolality, causing water to shift into brain cells. This osmotic gradient produces cerebral edema, which is often fatal.

2. **Giving an insulin bolus.** Unlike DKA protocols that sometimes include a 0.1 units/kg IV bolus, HHS protocols omit the bolus. The goal is gradual, controlled glucose reduction. Bolus insulin causes a precipitous glucose drop in the setting of extreme hyperosmolality.

3. **Starting insulin before correcting hypokalemia.** Identical pitfall to DKA but arguably more dangerous in HHS because the potassium deficit is larger (total body deficit 400-1000 mEq in HHS vs. 200-500 mEq in DKA). If K < 3.3 mEq/L, insulin drives K intracellularly and causes fatal arrhythmia. Replace K first.

4. **Underestimating volume deficit.** HHS patients are 8-12 L depleted on average (vs. 5-7 L in DKA). Inadequate fluid resuscitation is the most common error. Fluids alone reduce glucose by 75-100 mg/dL/hr; insulin without adequate fluids concentrates the remaining plasma and worsens hyperviscosity.

5. **Correcting osmolality too rapidly.** Target osmolality decline is 3-8 mOsm/kg/hr. Faster correction creates an osmotic gradient favoring water movement into brain cells, producing cerebral edema. If osmolality drops > 8 mOsm/kg/hr, slow fluids and reduce insulin rate.

6. **Misdiagnosing focal deficits as stroke.** HHS causes reversible focal neurologic deficits (hemiparesis, hemianopia, aphasia, seizures) in 10-25% of patients. These mimic acute ischemic stroke and resolve with osmolality correction. Always check glucose before activating a stroke code. Conversely, stroke can precipitate HHS — CT head and neurology consultation are appropriate if deficits persist after glucose correction.

7. **Forgetting thromboprophylaxis.** HHS produces a hypercoagulable state from hyperviscosity, dehydration, endothelial dysfunction, and immobility. VTE incidence is significantly higher than in DKA. Start pharmacologic prophylaxis (enoxaparin 40 mg SC daily or heparin 5,000 units SC q8h) on admission unless contraindicated.

8. **Stopping insulin when glucose reaches target without checking osmolality.** In HHS, glucose normalizes before osmolality does. Stopping insulin when glucose hits 300 mg/dL without confirming osmolality < 315 mOsm/kg and mental status improvement allows osmolality to plateau. Continue insulin with dextrose-containing fluids until osmolality and mental status normalize.

9. **Failing to search for a precipitant.** Infection triggers 40-60% of HHS. Hypothermia in HHS masks fever. A patient with glucose > 600 and WBC of 14,000 with a temperature of 36.0C may be septic. Obtain blood cultures, UA, CXR, and procalcitonin. Treat empirically if clinical suspicion is present.

10. **Missing HHS-DKA overlap.** Approximately 30% of hyperglycemic crises have features of both syndromes. Overlap presentations carry higher mortality. If a patient has glucose > 600 and osmolality > 320 (HHS features) PLUS pH < 7.30, bicarb < 18, and ketosis (DKA features), treat both: aggressive fluids for the hyperosmolality and insulin titrated to close the anion gap.
