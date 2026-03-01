---
id: metabolic-acidosis-evaluation
condition: Metabolic Acidosis - Emergency Evaluation
aliases: [anion gap metabolic acidosis, AGMA, non-anion gap metabolic acidosis, NAGMA, metabolic acidosis workup]
icd10: [E87.2, E87.4]
esi: 2
time_to_harm: "< 6 hours"
category: endocrine-metabolic
track: tier1
sources:
  - type: guideline
    ref: "Emmett M. Approach to Patients With High Anion Gap Metabolic Acidosis: Core Curriculum 2021. Am J Kidney Dis. 2021;78(2):312-321"
  - type: guideline
    ref: "Kraut JA, Madias NE. Metabolic Acidosis: Pathophysiology, Diagnosis and Management. Nat Rev Nephrol. 2010;6(5):274-285"
  - type: consensus-statement
    ref: "Berend K et al. Physiological approach to assessment of acid-base disturbances. N Engl J Med. 2014;371(15):1434-1445"
last_updated: "2026-03-01"
compiled_by: agent
risk_tier: B
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
# Metabolic Acidosis - Emergency Evaluation

## Recognition

**Identification:**
- pH < 7.35 with low HCO3 (< 22 mEq/L) on ABG/VBG
- Respiratory compensation: expected pCO2 = (1.5 x HCO3) + 8 (+/- 2) (Winter's formula); if measured pCO2 exceeds expected → concurrent respiratory acidosis

**Step 1: Calculate the anion gap:**
- AG = Na - (Cl + HCO3); normal = 8-12 mEq/L
- **Correct for albumin:** corrected AG = calculated AG + 2.5 x (4.0 - albumin); low albumin hides a gap
- AG > 20: always pathologic
- AG 12-20: borderline; evaluate in clinical context

**Step 2: If elevated AG — calculate delta-delta:**
- Delta gap = (AG - 12) / (24 - HCO3)
- Ratio < 1: concurrent non-AG metabolic acidosis
- Ratio 1-2: pure AG metabolic acidosis
- Ratio > 2: concurrent metabolic alkalosis (or pre-existing elevated HCO3)

**Step 3: If elevated AG — check osmolar gap:**
- Osmolar gap = measured osm - calculated osm
- Calculated osm = 2(Na) + glucose/18 + BUN/2.8
- Osmolar gap > 10: consider toxic alcohol ingestion (methanol, ethylene glycol)

## Critical Actions

1. **ABG or VBG** — confirm metabolic acidosis, assess compensation
2. **Calculate anion gap (corrected for albumin)**
3. **Point-of-care lactate** — most common cause of AG metabolic acidosis in ED
4. **Point-of-care glucose** — DKA screening
5. **If elevated osmolar gap:** obtain ethylene glycol and methanol levels; start fomepizole 15 mg/kg IV empirically while awaiting levels
6. **Identify and treat underlying cause immediately** — time-sensitive etiologies (sepsis, toxic ingestion, mesenteric ischemia)

## Differential Diagnosis

### Anion Gap Metabolic Acidosis (MUDPILES / GOLD MARKET)
- **M**ethanol
- **U**remia (renal failure)
- **D**iabetic ketoacidosis (and starvation/alcoholic ketoacidosis)
- **P**ropylene glycol, paraldehyde
- **I**soniazid, iron
- **L**actic acidosis (sepsis, shock, ischemia, seizures)
- **E**thylene glycol
- **S**alicylates

### Non-Anion Gap Metabolic Acidosis (Hyperchloremic)
- **GI bicarbonate loss:** diarrhea (most common), fistulae, ileostomy
- **Renal tubular acidosis (RTA):** Type 1 (distal), Type 2 (proximal), Type 4 (hypoaldosteronism)
- **Medications:** acetazolamide, topiramate, amphotericin B
- **Normal saline excess** (dilutional, iatrogenic)
- **Ureteral diversion** (ileal conduit)

### Mixed Acid-Base Disorders
- AG metabolic acidosis + non-AG metabolic acidosis (delta-delta < 1)
- AG metabolic acidosis + metabolic alkalosis (delta-delta > 2)
- Triple acid-base disorders possible (e.g., alcoholic patient with vomiting + ketoacidosis + respiratory alkalosis)

## Workup

- **ABG or VBG** — pH, pCO2, HCO3, pO2
- **BMP:** Na, K, Cl, HCO3, BUN, creatinine, glucose
- **Anion gap** = Na - (Cl + HCO3); correct for albumin
- **Serum osmolality** (measured) — calculate osmolar gap
- **Lactate** — most common cause of AGMA in ED
- **Ketones:** serum beta-hydroxybutyrate (more accurate than urine ketones)
- **Salicylate level** — if AG acidosis of unclear etiology; mixed respiratory alkalosis + metabolic acidosis is classic
- **Ethylene glycol and methanol levels** — if elevated osmolar gap
- **Urinalysis:** calcium oxalate crystals (ethylene glycol), ketones
- **Urine electrolytes:** urine AG = urine (Na + K) - Cl
  - Negative urine AG: GI bicarbonate loss (diarrhea) — appropriate renal response
  - Positive urine AG: renal tubular acidosis — impaired renal acid excretion
- **Urine pH:** > 5.5 in distal RTA despite systemic acidosis
- **Serum albumin** — for AG correction
- **LFTs, lipase** — hepatic failure, pancreatitis
- **Toxicology panel** as clinically indicated

## Treatment

### General Principles
- **Treat the cause, not the pH.** Acidosis is a marker of underlying disease.
- **Bicarbonate therapy is rarely indicated** except in specific situations (see below).

### Cause-Specific Treatment

**DKA:**
- Insulin regular 0.1 units/kg/hr IV infusion (after K > 3.3)
- IV NS bolus 1-2 L, then 250-500 mL/hr
- Potassium replacement: add KCl 20-40 mEq/L to each liter of fluid if K < 5.3

**Toxic Alcohol (Methanol/Ethylene Glycol):**
- **Fomepizole** 15 mg/kg IV loading dose, then 10 mg/kg IV q12h — blocks alcohol dehydrogenase
- Emergent hemodialysis if pH < 7.25, renal failure, visual symptoms (methanol), high levels
- Folate 50 mg IV q6h (methanol) or thiamine 100 mg IV + pyridoxine 50 mg IV (ethylene glycol)

**Lactic Acidosis:**
- Resuscitate underlying cause (see lactic-acidosis condition file)
- Bicarbonate only if pH < 7.1 with hemodynamic instability

**Salicylate Poisoning:**
- Sodium bicarbonate infusion: 150 mEq NaHCO3 in 1 L D5W at 1.5-2x maintenance; target urine pH 7.5-8.0
- Emergent hemodialysis if salicylate > 100 mg/dL, renal failure, pulmonary edema, altered mental status
- Do NOT intubate unless absolutely necessary — loss of compensatory hyperventilation causes rapid pH decline and death

**Renal Failure:**
- Emergent hemodialysis for severe acidosis (pH < 7.1), refractory hyperkalemia, volume overload
- Sodium bicarbonate as temporizing measure

### Bicarbonate Therapy (Limited Indications)
- pH < 6.9: sodium bicarbonate 50-100 mEq IV (may improve vasopressor responsiveness)
- pH 6.9-7.1 with hemodynamic compromise: consider bicarbonate
- Salicylate poisoning: bicarbonate drip for urine alkalinization (enhances renal elimination)
- Severe non-AG acidosis (bicarbonate loss): bicarbonate replacement indicated
- **NOT indicated:** routine use in DKA (corrects with insulin), routine use in lactic acidosis (evidence of harm)

## Disposition

- **Severe acidosis (pH < 7.2) or identified critical etiology:** ICU admission
- **Moderate acidosis (pH 7.2-7.3) with identified treatable cause:** monitored bed
- **Mild non-AG acidosis from diarrhea, responding to fluids:** may observe in ED and discharge with follow-up
- **Toxic alcohol ingestion:** ICU, toxicology/nephrology consultation
- **DKA:** insulin drip in ICU or step-down per institutional protocol

## Pitfalls

1. **Not correcting the anion gap for albumin.** Each 1 g/dL decrease in albumin below 4.0 reduces the AG by ~2.5 mEq/L. A "normal" AG of 12 in a patient with albumin of 2.0 is actually a corrected AG of 17 — an anion gap acidosis.

2. **Not calculating the delta-delta.** Mixed acid-base disorders are common. Without the delta-delta ratio, a concurrent non-AG acidosis or metabolic alkalosis will be missed.

3. **Missing toxic alcohol ingestion.** Methanol and ethylene glycol poisoning present as AG metabolic acidosis with elevated osmolar gap. Early in ingestion, osmolar gap is high but AG may be normal. Late, AG rises as toxic metabolites accumulate and osmolar gap may normalize. Check both.

4. **Intubating a salicylate-poisoned patient without matching their minute ventilation.** Severely acidotic patients compensate with profound hyperventilation. If intubated, the ventilator must match their pre-intubation minute ventilation (often > 20 L/min). Failure causes precipitous pH drop and cardiac arrest.

5. **Giving bicarbonate for DKA.** Bicarbonate does not improve outcomes in DKA and may worsen hypokalemia and paradoxical CSF acidosis. Insulin and fluids correct the acidosis.

6. **Attributing elevated lactate to sepsis without considering the full differential.** Mesenteric ischemia, toxic ingestion, seizures, and thiamine deficiency all cause elevated lactate. A persistently elevated lactate despite adequate sepsis treatment should trigger re-evaluation.
