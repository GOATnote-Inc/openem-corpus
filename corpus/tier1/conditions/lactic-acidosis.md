---
id: lactic-acidosis
condition: Lactic Acidosis
aliases: [hyperlactatemia, type A lactic acidosis, type B lactic acidosis, elevated lactate]
icd10: [E87.2]
esi: 2
time_to_harm:
  irreversible_injury: "< 6 hours"
  death: "< 24 hours"
  optimal_intervention_window: "< 1 hour"
category: endocrine-metabolic
track: tier1
sources:
  - type: guideline
    ref: "Kraut JA, Madias NE. Lactic Acidosis. N Engl J Med. 2014;371(24):2309-2319"
  - type: guideline
    ref: "Andersen LW et al. Etiology and Therapeutic Approach to Elevated Lactate Levels. Mayo Clin Proc. 2013;88(10):1127-1140"
  - type: consensus-statement
    ref: "Seheult J et al. Lactic acidosis: Clinical implications and management strategies. Cleve Clin J Med. 2017;82(9):615-624"
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
# Lactic Acidosis

## Recognition

**Definition:**
- Lactate > 2 mmol/L = hyperlactatemia
- Lactate > 4 mmol/L with pH < 7.35 = lactic acidosis
- Severe: lactate > 10 mmol/L (mortality > 80%)

**Classification:**
- **Type A (hypoxic/ischemic)** — inadequate oxygen delivery: shock (septic, cardiogenic, hypovolemic), cardiac arrest, severe anemia, respiratory failure, mesenteric ischemia, limb ischemia, CO poisoning
- **Type B (non-hypoxic)** — normal tissue perfusion:
  - B1: underlying disease (hepatic failure, malignancy, DKA, seizures, pheochromocytoma)
  - B2: drugs/toxins (metformin, nucleoside reverse transcriptase inhibitors, linezolid, propofol, cyanide, ethanol, acetaminophen, salicylates, epinephrine/vasopressors)
  - B3: inborn errors of metabolism

**Clinical presentation (nonspecific — driven by underlying cause):**
- Tachypnea, Kussmaul breathing (respiratory compensation)
- Tachycardia, hypotension
- Altered mental status, confusion
- Nausea, vomiting, abdominal pain
- Warm, flushed skin (early sepsis) or cool, mottled skin (cardiogenic shock)
- Oliguria (inadequate organ perfusion)

**Lactate as prognostic marker:**
- Lactate > 4 mmol/L: mortality ~30%
- Lactate > 10 mmol/L: mortality > 80%
- Lactate clearance > 10% in 6 hours associated with improved survival
- Serial lactate trending more informative than single value

## Critical Actions

1. **Identify and treat the underlying cause** — this IS the treatment; lactic acidosis is a symptom, not a disease
2. **Sepsis protocol** if suspected: blood cultures x 2, broad-spectrum antibiotics within 1 hour (piperacillin-tazobactam 4.5 g IV or meropenem 1 g IV), 30 mL/kg crystalloid bolus
3. **Hemodynamic resuscitation** — IV crystalloid (LR preferred over NS); vasopressors if refractory to fluids (norepinephrine 0.05-0.5 mcg/kg/min)
4. **Ensure adequate oxygenation** — intubate if respiratory failure; target SpO2 > 94%
5. **Serial lactate** q2-4h — track clearance; goal > 10% reduction per 2 hours
6. **Recheck ABG/VBG** — monitor pH, bicarbonate, lactate simultaneously

## Differential Diagnosis

- Sepsis/septic shock (most common cause of elevated lactate in ED)
- Cardiogenic shock (low cardiac output, elevated CVP)
- Hypovolemic shock (hemorrhage, dehydration)
- Mesenteric ischemia (abdominal pain out of proportion to exam, elevated lactate, metabolic acidosis)
- Diabetic ketoacidosis (hyperglycemia, ketonuria, anion gap)
- Toxic ingestion (metformin, cyanide, carbon monoxide, ethylene glycol)
- Seizures (transient lactate elevation resolves within hours)
- Severe asthma/respiratory failure (respiratory muscle fatigue)
- Hepatic failure (impaired lactate clearance)
- Thiamine deficiency (beriberi — type B, especially in alcoholics and post-gastric bypass)
- Malignancy (tumor lysis, Warburg effect)

## Workup

- **Point-of-care lactate** — immediate; venous or arterial (venous acceptable for screening and trending)
- **ABG or VBG** — pH, pCO2, bicarbonate, anion gap
- **BMP:** anion gap calculation (AG = Na - Cl - HCO3; normal 8-12; elevated suggests AG metabolic acidosis)
- **CBC with differential** — infection, anemia
- **Blood cultures x 2** — before antibiotics if sepsis suspected
- **LFTs** — hepatic failure impairs lactate clearance
- **Troponin** — cardiac ischemia as cause or consequence
- **Procalcitonin** — sepsis marker
- **Coagulation studies** — DIC screen if sepsis or liver failure
- **CT abdomen with IV contrast** — mesenteric ischemia (if abdominal pain or suspicion)
- **CXR** — pneumonia, pulmonary edema
- **Toxicology:** metformin level, CO level, cyanide level as indicated by history
- **Thiamine level** — especially in alcoholics, malnourished patients

## Treatment

### Source Control (Priority)
- Identify and treat the cause: antibiotics for infection, surgery for ischemic bowel, PCI for MI, source drainage for abscess
- Stop offending medications: metformin, propofol, linezolid, nucleoside analogs

### Hemodynamic Resuscitation
- **Crystalloid IV:** lactated Ringer's 30 mL/kg bolus (sepsis); NS acceptable but risk of hyperchloremic acidosis with large volumes
- **Norepinephrine** 0.05-0.5 mcg/kg/min IV — first-line vasopressor for septic shock
- **Vasopressin** 0.04 units/min IV — second-line, added to norepinephrine
- **Dobutamine** 2-20 mcg/kg/min IV — if cardiogenic component (low cardiac output)
- Blood products if hemorrhagic: pRBC, target Hb > 7 g/dL (> 8 in cardiac disease)

### Respiratory Support
- Supplemental O2 to maintain SpO2 > 94%
- Intubation for respiratory failure, airway protection, or severe metabolic acidosis requiring respiratory compensation
- Caution: apnea during RSI in severely acidotic patients can cause rapid pH decline and cardiac arrest

### Sodium Bicarbonate (Limited Role)
- **NOT recommended routinely** — evidence does not support improved outcomes
- Consider sodium bicarbonate 8.4% 50-100 mEq IV only if pH < 7.1 AND refractory hemodynamic instability
- BICAR-ICU trial: possible mortality benefit when pH < 7.2 in AKI patients
- Risk: volume overload, hypernatremia, paradoxical intracellular acidosis, left-shift of oxyhemoglobin curve

### Thiamine
- **Thiamine 200-500 mg IV** — empiric in alcoholics, malnourished, post-bypass; treat before glucose (Wernicke prevention)
- Thiamine deficiency causes type B lactic acidosis (impaired pyruvate dehydrogenase)

### Renal Replacement Therapy
- Continuous renal replacement therapy (CRRT) for refractory acidosis with AKI
- Removes lactate and toxins; corrects acid-base more gently than bolus bicarbonate
- Especially useful in metformin-associated lactic acidosis (MALA)

### Metformin-Associated Lactic Acidosis (MALA)
- Discontinue metformin
- Aggressive IV hydration
- Sodium bicarbonate if pH < 7.1
- Emergent hemodialysis — metformin is dialyzable; indicated for severe MALA (pH < 7.0, lactate > 20)

## Disposition

- **Lactate > 4 mmol/L with hemodynamic instability:** ICU
- **Lactate > 4 mmol/L, hemodynamically stable, identified cause:** monitored bed with serial lactates
- **Lactate 2-4 mmol/L, resolving with treatment:** ED observation, may discharge if cause addressed and lactate normalizing
- **Lactate clearance < 10% at 6 hours:** escalate care, ICU admission
- **Mesenteric ischemia suspected:** emergent surgical consultation, CTA abdomen

## Pitfalls

1. **Treating the number instead of the cause.** Lactic acidosis is a marker of underlying pathology. Giving bicarbonate to normalize pH without addressing the cause (sepsis, ischemia, toxin) does not improve outcomes and may be harmful.

2. **Single lactate measurement without serial trending.** A single elevated lactate provides limited information. Lactate clearance (> 10% per 2 hours) is a better predictor of outcome than any single value.

3. **Attributing elevated lactate solely to sepsis.** Mesenteric ischemia, limb ischemia, carbon monoxide poisoning, cyanide exposure, and medication toxicity all cause lactic acidosis. Maintain a broad differential, especially when lactate does not clear with sepsis treatment.

4. **Using large volumes of NS instead of LR.** Large-volume NS resuscitation causes hyperchloremic metabolic acidosis that compounds existing lactic acidosis and may confuse interpretation. LR is preferred for large-volume resuscitation.

5. **Forgetting thiamine in alcoholic or malnourished patients.** Thiamine deficiency causes type B lactic acidosis through impaired pyruvate dehydrogenase. Lactate will not clear without thiamine repletion.

6. **Delay in recognizing mesenteric ischemia.** Elevated lactate with abdominal pain (especially "pain out of proportion to exam") in elderly or AF patients should prompt emergent CTA abdomen. Delayed diagnosis is uniformly fatal.
