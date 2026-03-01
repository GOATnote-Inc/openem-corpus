---
id: shock-undifferentiated
condition: "Shock — Undifferentiated Emergency Evaluation"
aliases: [shock, hypotension, cardiovascular collapse, undifferentiated shock, circulatory failure, hemodynamic instability]
icd10: [R57.9, R57.0, R57.1, R57.8, R65.21]
esi: 1
time_to_harm:
  irreversible_injury: "< 30 minutes (end-organ damage from sustained hypoperfusion)"
  death: "< 60 minutes (untreated shock of any etiology)"
  optimal_intervention_window: "< 15 minutes (identify type, begin targeted resuscitation)"
category: presentations
condition_type: presentation
chief_complaint: "Shock/Hypotension"
differential_categories:
  - category: life-threatening
    conditions:
      - hemorrhagic-shock
      - sepsis
      - cardiac-tamponade
      - tension-pneumothorax
      - pulmonary-embolism
      - stemi
      - acute-heart-failure
      - anaphylaxis
      - aortic-dissection
      - ruptured-aaa
      - adrenal-crisis
      - cardiac-arrest
      - right-ventricular-failure
  - category: emergent
    conditions:
      - acute-valvular-emergency
      - hypertrophic-cardiomyopathy-emergency
      - takotsubo-cardiomyopathy
      - acute-respiratory-failure
      - ards
      - spinal-cord-injury
      - pericarditis-myocarditis
      - pulmonary-hypertension-crisis
      - thyroid-storm
      - toxic-shock-syndrome
  - category: urgent
    conditions:
      - diabetic-ketoacidosis
      - hhs
      - hyperkalemia
      - hypothermia
  - category: non-emergent
    conditions: []
red_flags:
  - "MAP < 65 mmHg or SBP < 90 mmHg"
  - "Altered mental status"
  - "Mottled skin, delayed capillary refill > 3 seconds"
  - "Lactate > 4 mmol/L"
  - "Oliguria (< 0.5 mL/kg/hr)"
  - "Tachycardia > 120 with hypotension"
  - "Paradoxical bradycardia with hypotension (neurogenic shock, beta-blocker toxicity)"
  - "Distended neck veins with hypotension (obstructive shock)"
  - "Unilateral absent breath sounds (tension pneumothorax)"
decision_rules:
  - name: "RUSH Exam (Rapid Ultrasound in Shock and Hypotension)"
    citation: "Perera P et al. The RUSH exam: Rapid Ultrasound in SHock in the evaluation of the critically ill. Emerg Med Clin North Am. 2010;28(1):29-56."
    pmid: "19945597"
  - name: "SOFA Score"
    citation: "Vincent JL et al. The SOFA (Sepsis-related Organ Failure Assessment) score to describe organ dysfunction/failure. Intensive Care Med. 1996;22(7):707-710."
    pmid: "8844239"
track: tier1
sources:
  - type: guideline
    ref: "Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock. 2021."
    doi: "10.1007/s00134-021-06506-y"
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition. American College of Surgeons. 2018."
  - type: review
    ref: "Vincent JL, De Backer D. Circulatory shock. N Engl J Med. 2013;369(18):1726-1734."
    pmid: "24171518"
  - type: pubmed
    ref: "Perera P et al. The RUSH exam: Rapid Ultrasound in SHock in the evaluation of the critically ill. Emerg Med Clin North Am. 2010;28(1):29-56."
    pmid: "19945597"
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
# Shock — Undifferentiated Emergency Evaluation

## Recognition

Shock is defined as inadequate tissue oxygen delivery relative to metabolic demand. It is a clinical diagnosis based on signs of end-organ hypoperfusion — NOT simply a blood pressure threshold. Patients can be in shock with a "normal" blood pressure (compensated shock), and hypotension can exist without shock.

**Four categories of shock (identify rapidly — treatment differs):**

| Type | Mechanism | Key Signs | POCUS Findings |
|---|---|---|---|
| **Hypovolemic** | Volume loss (hemorrhage, dehydration) | Flat neck veins, tachycardia, cool extremities | Small hyperdynamic heart, flat IVC |
| **Distributive** | Vasodilation (sepsis, anaphylaxis, neurogenic) | Warm extremities (early sepsis), flushed (anaphylaxis), spinal level (neurogenic) | Hyperdynamic heart, plethoric IVC (neurogenic), variable (sepsis) |
| **Cardiogenic** | Pump failure (MI, myocarditis, valvular) | JVD, pulmonary edema, cool extremities, S3 gallop | Dilated poorly contractile LV, B-lines (pulmonary edema) |
| **Obstructive** | Mechanical obstruction (PE, tamponade, tension pneumo) | JVD, muffled heart sounds (tamponade), absent breath sounds (tension pneumo), RV strain (PE) | Pericardial effusion (tamponade), RV dilation (PE), absent lung sliding (pneumothorax) |

**Clinical indicators of shock (may be present before hypotension):**
- Tachycardia (compensatory — may be absent with beta-blockers, spinal cord injury, or terminal bradycardia)
- Altered mental status (agitation, confusion, obtundation)
- Skin signs: mottling (knees, elbows), cool clammy extremities (hypovolemic/cardiogenic), warm flushed (distributive)
- Capillary refill > 3 seconds
- Decreased urine output (< 0.5 mL/kg/hr)
- Metabolic acidosis with elevated lactate (> 2 mmol/L concerning, > 4 mmol/L shock physiology)

**Vital sign interpretation pitfalls:**
- "Normal" BP with tachycardia in young patient = compensated shock (may have lost 30%+ blood volume)
- Bradycardia with hypotension = neurogenic shock, beta-blocker/CCB toxicity, or terminal/agonal event
- Hypothermia with shock = sepsis (ominous), environmental exposure, adrenal crisis, myxedema coma

## Critical Actions

| Action | Target |
|---|---|
| Identify shock | < 2 minutes |
| 2 large-bore IVs + crystalloid bolus | < 5 minutes |
| RUSH exam (bedside ultrasound) | < 10 minutes |
| Identify shock type | < 15 minutes |
| Vasopressors if fluid-refractory | < 30 minutes |
| Source control (if applicable) | < 60 minutes |

**Evaluation algorithm:**

1. **Recognize shock.** MAP < 65 (or SBP < 90), OR evidence of end-organ hypoperfusion (AMS, mottling, oliguria, lactate > 4) regardless of blood pressure.

2. **Simultaneous resuscitation and diagnosis.** DO NOT delay resuscitation for workup.
   - 2 large-bore (16-18G) peripheral IVs. IO access if peripheral access fails.
   - Crystalloid bolus: NS or LR 30 mL/kg for hypovolemic and distributive shock. CAUTION: smaller boluses (250-500 mL) and reassess in cardiogenic shock (excess fluid worsens pulmonary edema).
   - Place patient on continuous monitoring (cardiac, SpO2, BP cycling q3-5 min or arterial line).

3. **RUSH exam (Rapid Ultrasound in SHock) — the key bedside tool:**
   - **PUMP (heart):** Contractility (hyperdynamic = hypovolemic/distributive; depressed = cardiogenic), pericardial effusion (tamponade), RV dilation (PE, RV failure)
   - **TANK (volume status):** IVC (< 2 cm with > 50% respiratory variation = hypovolemic; > 2 cm with < 50% variation = cardiogenic/obstructive). Lung sliding (absent = pneumothorax). B-lines (pulmonary edema). Free fluid (hemorrhage).
   - **PIPES (vasculature):** Aorta (AAA, dissection), femoral veins (DVT → PE)

4. **Categorize and treat simultaneously:**

   **Hypovolemic shock:**
   - Hemorrhagic: IV crystalloid → pRBC. Find source: FAST exam (intra-abdominal), CXR (hemothorax), pelvic binder (pelvic fracture), OR for surgical bleeding. Massive transfusion protocol (1:1:1) for ongoing hemorrhage.
   - Non-hemorrhagic: dehydration (DKA, HHS, GI losses, burns, third-spacing). Crystalloid resuscitation. Treat underlying cause.

   **Distributive shock:**
   - Septic: Crystalloid 30 mL/kg → norepinephrine 0.05-0.5 mcg/kg/min if MAP < 65 despite fluids → vasopressin 0.03-0.04 units/min as second agent → broad-spectrum antibiotics within 1 hour → source control.
   - Anaphylactic: Epinephrine 0.3-0.5 mg IM (1:1000) → repeat q5-15 min → epinephrine infusion 0.1-0.5 mcg/kg/min if refractory → IV fluids 1-2 L bolus → adjuncts (H1/H2 blockers, steroids). See `anaphylaxis`.
   - Neurogenic: spinal cord injury above T6. Bradycardia + hypotension + warm extremities. Crystalloid → norepinephrine (or phenylephrine) → atropine for bradycardia. Maintain MAP > 85-90 for spinal cord perfusion.

   **Cardiogenic shock:**
   - Small fluid boluses ONLY (250 mL, reassess). Excess fluid worsens pulmonary edema.
   - Norepinephrine 0.05-0.5 mcg/kg/min first-line vasopressor (NOT dopamine — associated with more arrhythmias).
   - Dobutamine 2-20 mcg/kg/min for inotropy if needed.
   - Emergent cardiology: cath lab for STEMI/NSTEMI, mechanical circulatory support (IABP, Impella), surgical consultation for valvular catastrophe.
   - NIV/BIPAP for pulmonary edema if patient is alert and breathing.

   **Obstructive shock:**
   - Tension pneumothorax: needle decompression (14G, 2nd ICS midclavicular or 5th ICS anterior axillary line) followed by tube thoracostomy. Clinical diagnosis — do NOT delay for CXR.
   - Cardiac tamponade: emergent pericardiocentesis (see `emergency-pericardiocentesis`). Volume loading (250-500 mL bolus) as temporizing measure. Definitive: surgical pericardial window.
   - Massive PE: systemic thrombolysis (alteplase 100 mg IV over 2 hours), or catheter-directed therapy, or surgical embolectomy. Heparin bolus 80 units/kg. Volume loading cautiously (500 mL — excess fluid worsens RV failure). See `pulmonary-embolism`.

5. **If vasopressors needed:**
   - First-line for most shock: Norepinephrine 0.05-0.5 mcg/kg/min (alpha + beta-1)
   - Second-line: Vasopressin 0.03-0.04 units/min (non-catecholamine, synergistic)
   - Cardiogenic (inotropy needed): Dobutamine 2-20 mcg/kg/min or milrinone 0.375-0.75 mcg/kg/min
   - Anaphylaxis: Epinephrine infusion 0.1-0.5 mcg/kg/min
   - Pure vasoplegia: Phenylephrine 0.5-5 mcg/kg/min (pure alpha — use if tachyarrhythmia limits norepinephrine)
   - Peripheral vasopressors are safe for short-term use (< 12 hours) via large-bore IV. Do NOT delay vasopressors waiting for central line placement.

## Differential Diagnosis

### Life-Threatening
- **Hemorrhagic shock** (`hemorrhagic-shock`): trauma, GI bleed, ruptured AAA, ruptured ectopic, postpartum hemorrhage. Cool, tachycardic, flat IVC on POCUS.
- **Septic shock** (`sepsis`): infection + hypotension refractory to 30 mL/kg crystalloid + lactate > 2. Warm initially → cool/mottled late. Source identification critical.
- **Cardiac tamponade** (`cardiac-tamponade`): JVD, muffled heart sounds, hypotension (Beck triad). Pulsus paradoxus > 10 mmHg. POCUS: pericardial effusion with RV diastolic collapse.
- **Tension pneumothorax** (`tension-pneumothorax`): unilateral absent breath sounds, tracheal deviation (late), hypotension, JVD. Clinical diagnosis → immediate needle decompression.
- **Massive PE** (`pulmonary-embolism`): acute dyspnea, hypotension, RV dilation on POCUS, S1Q3T3 or right heart strain on ECG. CT-PA if stable enough; empiric thrombolysis if too unstable for CT.
- **Cardiogenic shock from MI** (`stemi`, `acute-heart-failure`): chest pain, ST changes, depressed LV function on POCUS, pulmonary edema. Emergent cath lab.
- **Anaphylaxis** (`anaphylaxis`): allergen exposure, urticaria, bronchospasm, hypotension. Epinephrine IM immediately.
- **Aortic dissection** (`aortic-dissection`): tearing pain, pulse deficit, BP differential, aortic root dilation on POCUS. Stanford A → surgical emergency.
- **Ruptured AAA** (`ruptured-aaa`): age > 60, abdominal/back pain, pulsatile mass, shock. Bedside aortic US → OR if unstable.
- **Adrenal crisis** (`adrenal-crisis`): hypotension refractory to fluids and vasopressors, hyponatremia, hyperkalemia, chronic steroid use with acute stressor. Hydrocortisone 100 mg IV immediately (do NOT wait for cortisol level).
- **Post-cardiac arrest** (`cardiac-arrest`, `post-cardiac-arrest-syndrome`): post-ROSC shock from myocardial stunning, reperfusion injury
- **RV failure** (`right-ventricular-failure`): isolated RV failure from PE, RV infarction, pulmonary hypertension

### Emergent
- **Acute valvular emergency** (`acute-valvular-emergency`): acute mitral regurgitation (chordae rupture), acute aortic insufficiency (dissection, endocarditis), prosthetic valve thrombosis
- **HCM with obstruction** (`hypertrophic-cardiomyopathy-emergency`): dynamic LVOT obstruction, worse with dehydration and tachycardia. Treat with volume, phenylephrine, esmolol. Avoid inotropes/vasodilators.
- **Takotsubo** (`takotsubo-cardiomyopathy`): post-stress cardiomyopathy, apical ballooning, mimics MI
- **ARDS** (`ards`): severe hypoxemia with bilateral infiltrates, may cause distributive or cardiogenic shock
- **Neurogenic shock** (`spinal-cord-injury`): spinal cord injury above T6, loss of sympathetic tone → bradycardia + hypotension + warm extremities
- **Myocarditis** (`pericarditis-myocarditis`): viral prodrome, troponin elevation, depressed LV function, young patient
- **Pulmonary hypertension crisis** (`pulmonary-hypertension-crisis`): known PAH with acute decompensation, RV failure
- **Thyroid storm** (`thyroid-storm`): tachycardia, hyperthermia, AMS, high-output state → eventual cardiovascular collapse
- **Toxic shock syndrome** (`toxic-shock-syndrome`): fever, diffuse rash, hypotension, multiorgan involvement

### Urgent
- **DKA** (`diabetic-ketoacidosis`): volume depletion → hypovolemic shock, anion gap acidosis
- **HHS** (`hhs`): profound dehydration (often 8-10L deficit), hyperosmolality
- **Hyperkalemia** (`hyperkalemia`): K+ > 6.5 → bradycardia → arrest
- **Hypothermia** (`hypothermia`): core temp < 30°C → cardiovascular collapse

## Workup

**All patients in shock — obtained simultaneously with resuscitation:**
- Point-of-care glucose
- RUSH exam (POCUS — heart, IVC, lungs, aorta, free fluid)
- ECG (STEMI, arrhythmia, RV strain)
- CBC, BMP, hepatic panel, coagulation studies
- Lactate (ABG or VBG)
- Type and crossmatch
- Blood cultures x 2 (before antibiotics if sepsis suspected)
- Troponin

**Based on shock type:**
- **Hypovolemic:** FAST exam, CXR, pelvic XR, hemoglobin trend
- **Distributive (sepsis):** Procalcitonin, urinalysis, CXR, CT as source dictates, LP if meningitis suspected
- **Cardiogenic:** Echocardiography (formal), BNP/NT-proBNP, troponin trend, CXR, cath lab activation for ACS
- **Obstructive:** CTA chest (PE), POCUS pericardial effusion (tamponade), CXR (pneumothorax — but clinical diagnosis for tension)
- **Cortisol level** if adrenal crisis suspected (send but do NOT wait to treat — give hydrocortisone empirically)

**Arterial line:** Place early for continuous BP monitoring and ABG sampling. Radial preferred.

## Treatment

See shock type-specific treatment above (Critical Actions section). Key principles:

1. **Resuscitate simultaneously with diagnosis.** Every minute in shock increases mortality and morbidity.
2. **Volume first** for hypovolemic and distributive shock (30 mL/kg crystalloid). Cautious volume (250 mL boluses) for cardiogenic and obstructive.
3. **Vasopressors if fluid-refractory.** Do NOT delay vasopressors for central line — peripheral vasopressors are safe short-term.
4. **Source control** is the definitive treatment in many shock states: OR for hemorrhage, drainage for abscess, ERCP for cholangitis, chest tube for pneumothorax, pericardiocentesis for tamponade.
5. **Stress-dose steroids:** Hydrocortisone 100 mg IV q8h if vasopressor-refractory septic shock or suspected adrenal insufficiency.
6. **Blood products** for hemorrhagic shock: massive transfusion protocol (1:1:1 pRBC:FFP:platelets), TXA 1 g IV over 10 min within 3 hours of injury.
7. **Avoid intubation if possible** — positive pressure ventilation reduces preload and can cause cardiac arrest in patients with hypovolemic, obstructive, or RV failure shock. If intubation necessary: ketamine or etomidate for induction, small tidal volumes, minimize PEEP initially, push-dose phenylephrine (100 mcg IV bolus) at bedside.

## Disposition

- **All patients in shock require ICU admission.** There are no exceptions. Shock is an ICU diagnosis.
- **Specific interventions determining disposition:**
  - OR: hemorrhagic shock requiring surgical control, ruptured AAA, Stanford A dissection, acute valvular emergency
  - Cath lab: cardiogenic shock from ACS
  - IR: embolization for hemorrhage, catheter-directed therapy for massive PE
  - ICU: all others (septic shock on vasopressors, post-ROSC, ARDS, post-thrombolysis PE, neurogenic shock)
- **Transfer:** Shock patients at facilities without ICU, surgical capability, or cath lab must be stabilized and transferred emergently.

## Pitfalls

1. **Relying on blood pressure alone to diagnose shock.** Young healthy patients compensate with tachycardia and vasoconstriction, maintaining "normal" blood pressure despite 30%+ blood volume loss. Tachycardia, altered mentation, mottling, elevated lactate, and oliguria are earlier indicators than hypotension.

2. **Giving large-volume crystalloid to cardiogenic shock.** Cardiogenic shock is a pump problem, not a volume problem. Excess fluid worsens pulmonary edema and RV distension. Small boluses (250 mL) with reassessment, early vasopressors, and inotropes are appropriate.

3. **Delaying vasopressors for central line placement.** Peripheral vasopressors (norepinephrine through large-bore IV) are safe for short-term use (< 12 hours). Starting vasopressors through a peripheral IV 10 minutes faster saves lives. Central access can be obtained after stabilization.

4. **Not performing RUSH exam.** Bedside ultrasound in undifferentiated shock is the single most valuable diagnostic tool. Cardiac contractility, IVC size, pericardial effusion, pneumothorax, free fluid, and aortic diameter can be assessed in < 5 minutes and determine the shock type.

5. **Missing obstructive shock.** Tension pneumothorax and cardiac tamponade are rapidly lethal but immediately treatable. JVD with hypotension (obstructive physiology) must trigger consideration of these diagnoses. A 30-second POCUS differentiates them.

6. **Positive pressure ventilation causing cardiac arrest.** Intubating a patient in hypovolemic or obstructive shock without pre-resuscitation causes loss of sympathetic drive (from sedation) and decreased preload (from positive pressure). Bolus fluids and push-dose vasopressors BEFORE induction. Use ketamine (preserves sympathetic tone). Have push-dose epinephrine (10-20 mcg IV) ready at bedside.

7. **Forgetting adrenal crisis.** Vasopressor-refractory shock in a patient on chronic steroids, with recent steroid discontinuation, or with no other clear etiology → give hydrocortisone 100 mg IV empirically. This can be life-saving and is harmless if wrong.
