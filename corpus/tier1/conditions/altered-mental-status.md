---
id: altered-mental-status
condition: "Altered Mental Status — Emergency Evaluation"
aliases: [AMS, altered LOC, confusion, delirium, encephalopathy, obtundation, lethargy, altered sensorium]
icd10: [R41.82, R40.4, R41.0]
esi: 2
time_to_harm:
  irreversible_injury: "< 60 minutes (hypoglycemia, stroke, status epilepticus)"
  death: "< 30 minutes (herniation, status epilepticus, severe hypoglycemia)"
  optimal_intervention_window: "< 30 minutes (glucose, naloxone, antibiotics for meningitis)"
category: presentations
condition_type: presentation
chief_complaint: "Altered Mental Status"
differential_categories:
  - category: life-threatening
    conditions:
      - acute-ischemic-stroke
      - hemorrhagic-stroke
      - subarachnoid-hemorrhage
      - status-epilepticus
      - bacterial-meningitis
      - hsv-encephalitis
      - hypoglycemia
      - diabetic-ketoacidosis
      - opioid-overdose
      - carbon-monoxide-poisoning
      - sepsis
      - traumatic-brain-injury
      - epidural-hematoma
      - subdural-hematoma
      - hepatic-abscess
      - hyperkalemia
      - acute-hepatic-failure
      - thyroid-storm
      - cardiac-arrest
  - category: emergent
    conditions:
      - hhs
      - adrenal-crisis
      - alcohol-withdrawal
      - benzodiazepine-overdose
      - acetaminophen-overdose
      - toxic-alcohol-ingestion
      - serotonin-syndrome
      - neuroleptic-malignant-syndrome
      - anticholinergic-toxidrome
      - sympathomimetic-toxidrome
      - heat-stroke
      - hypothermia
      - hypertensive-emergency
      - tumor-lysis-syndrome
  - category: urgent
    conditions:
      - acute-psychosis
      - acute-agitation
      - lithium-toxicity
  - category: non-emergent
    conditions: []
red_flags:
  - "Acute onset (minutes to hours) — suggests vascular, toxic, or metabolic"
  - "Fever with nuchal rigidity — meningitis/encephalitis"
  - "Focal neurological deficit — stroke, mass lesion"
  - "Pinpoint pupils — opioid toxicity"
  - "Markedly dilated pupils — anticholinergic toxidrome, sympathomimetic"
  - "Hypoglycemia (glucose < 60 mg/dL)"
  - "Seizure preceding altered state"
  - "Papilledema — elevated ICP"
  - "Battle sign or raccoon eyes — basilar skull fracture"
  - "Cherry-red skin or carboxyhemoglobin exposure — CO poisoning"
  - "Track marks — IV drug use, opioid/stimulant toxicity"
decision_rules:
  - name: "Glasgow Coma Scale (GCS)"
    citation: "Teasdale G, Jennett B. Assessment of coma and impaired consciousness. A practical scale. Lancet. 1974;2(7872):81-84."
    pmid: "4136544"
  - name: "AEIOU-TIPS Mnemonic (differential framework)"
    citation: "Standard EM teaching framework for altered mental status differential diagnosis."
track: tier1
sources:
  - type: guideline
    ref: "ACEP Clinical Policy: Critical Issues in the Evaluation and Management of Adult Patients Presenting to the Emergency Department With Altered Mental Status. Ann Emerg Med. 2017;69(6):e69-e88."
  - type: review
    ref: "Kanich W et al. Altered mental status: evaluation and etiology in the ED. Am J Emerg Med. 2002;20(7):613-617."
    pmid: "12442240"
  - type: guideline
    ref: "2019 IDSA Practice Guidelines for Bacterial Meningitis"
  - type: guideline
    ref: "AHA/ASA Guidelines for the Early Management of Patients With Acute Ischemic Stroke. 2019."
    doi: "10.1161/STR.0000000000000211"
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
# Altered Mental Status — Emergency Evaluation

## Recognition

Altered mental status (AMS) is a broad presentation encompassing any change in cognition, awareness, or consciousness — from mild confusion to coma. It represents one of the most diagnostically challenging ED presentations because the differential spans every organ system. The mnemonic AEIOU-TIPS provides a systematic framework.

**AEIOU-TIPS differential framework:**
- **A** — Alcohol, Acidosis (DKA, lactic, toxic)
- **E** — Epilepsy (seizure, postictal, nonconvulsive status), Encephalopathy, Endocrine (thyroid, adrenal)
- **I** — Infection (meningitis, encephalitis, sepsis, UTI in elderly)
- **O** — Overdose, Oxygen (hypoxia, CO poisoning)
- **U** — Uremia, metabolic derangement
- **T** — Trauma, Temperature (heat stroke, hypothermia)
- **I** — Insulin (hypoglycemia, DKA, HHS)
- **P** — Psychiatric, Poisoning
- **S** — Stroke, SAH, Space-occupying lesion (tumor, abscess, hemorrhage), Shock

**Key history (from EMS, family, bystanders — patient often cannot provide):**
- Baseline mental status (dementia vs new confusion)
- Rapidity of onset: acute vs insidious
- Recent medications and medication changes
- Access to drugs, alcohol, toxic substances
- Recent head trauma
- Prior psychiatric history, prior similar episodes
- Fever, infection symptoms
- Last known normal time (for potential stroke)

**Vital sign clues:**
- Hyperthermia: infection, serotonin syndrome, NMS, anticholinergic toxidrome, heat stroke, thyroid storm
- Hypothermia: environmental exposure, myxedema coma, sepsis (late), opioid overdose
- Hypertension + bradycardia: Cushing response (elevated ICP)
- Tachycardia + hypotension: sepsis, hemorrhage, toxidromes

**Pupil examination (critical in AMS):**
- Pinpoint: opioids, pontine hemorrhage, organophosphate poisoning
- Dilated bilateral: anticholinergic, sympathomimetic, post-cardiac arrest
- Unilateral dilation (anisocoria): uncal herniation, CN III palsy → emergent CT
- Normal reactive: metabolic cause most likely

## Critical Actions

| Action | Target |
|---|---|
| Fingerstick glucose | < 2 minutes from arrival |
| Airway assessment + GCS | < 5 minutes |
| Core temperature | < 5 minutes |
| Naloxone if opioid suspected | < 5 minutes |
| Head CT (non-contrast) if focal deficit or GCS ≤ 8 | < 25 minutes |
| Empiric antibiotics if meningitis suspected | < 60 minutes (do NOT delay for LP) |

**Immediate evaluation algorithm:**

1. **Airway, Breathing, Circulation.** GCS ≤ 8 → intubation likely needed. Protect airway before diagnostic workup. Have suction ready.

2. **Fingerstick glucose immediately.** Glucose < 60 mg/dL → dextrose 50% (D50) 25-50 mL IV (1 amp). Thiamine 100 mg IV first if chronic alcoholism or malnourishment suspected (prevent Wernicke encephalopathy). Hypoglycemia is the most rapidly reversible life-threatening cause.

3. **Naloxone** if any suspicion for opioid toxicity (pinpoint pupils, respiratory depression, track marks, found with paraphernalia): naloxone 0.4 mg IV/IM, repeat q2-3 min to max 10 mg. Titrate to respiratory effort, not full consciousness. IN naloxone 4 mg if no IV access.

4. **Targeted physical exam:**
   - Pupils (see above)
   - Nuchal rigidity (meningitis — but absence does not exclude)
   - Lateralizing signs (stroke, mass lesion)
   - Skin: track marks, needle marks, medication patches (fentanyl), rash (meningococcemia, TEN), cherry-red (CO), jaundice (hepatic), diaphoresis
   - Odor: fruity (DKA), garlic (organophosphate), alcohol
   - Muscle tone: rigidity (NMS, serotonin syndrome), flaccidity (opioid, BZD)
   - Deep tendon reflexes: clonus + hyperreflexia (serotonin syndrome), areflexia (GBS, deep sedation)

5. **CT head without contrast** if: focal neurological deficit, GCS ≤ 13, signs of elevated ICP, trauma, anticoagulation use, headache, new seizure. Do NOT delay for CT in meningitis — give antibiotics first.

6. **Lumbar puncture** if meningitis/encephalitis suspected: after CT shows no mass effect. If CT will delay > 30 minutes, give empiric antibiotics AND dexamethasone BEFORE CT.

7. **Toxicology screen + additional labs** based on clinical picture (see Workup).

## Differential Diagnosis

### Life-Threatening
- **Acute ischemic stroke** (`acute-ischemic-stroke`): sudden focal deficit, last known normal time critical for tPA window (< 4.5 hours)
- **Hemorrhagic stroke** (`hemorrhagic-stroke`): sudden headache + deficit, often hypertensive
- **Subarachnoid hemorrhage** (`subarachnoid-hemorrhage`): thunderclap headache → obtundation, nuchal rigidity
- **Status epilepticus** (`status-epilepticus`): sustained or recurrent seizures. Nonconvulsive status epilepticus (NCSE) is a major occult cause of AMS — patient appears confused/obtunded without obvious convulsions. Requires EEG to diagnose.
- **Bacterial meningitis** (`bacterial-meningitis`): fever, headache, nuchal rigidity, photophobia. Classic triad present in < 50% of cases. Altered consciousness is late and ominous.
- **HSV encephalitis** (`hsv-encephalitis`): behavioral changes, temporal lobe seizures, fever. Acyclovir must be given empirically if suspected.
- **Hypoglycemia** (`hypoglycemia`): glucose < 60 mg/dL. Diaphoresis, tremor, confusion → seizure → coma. Rapidly fatal if untreated.
- **DKA** (`diabetic-ketoacidosis`): Kussmaul breathing, fruity breath, polyuria/polydipsia, glucose > 250, anion gap acidosis
- **Opioid overdose** (`opioid-overdose`): pinpoint pupils, respiratory depression, GCS depression
- **CO poisoning** (`carbon-monoxide-poisoning`): headache, confusion, multiple household members affected, cherry-red coloring (late), carboxyhemoglobin level (pulse ox unreliable)
- **Sepsis** (`sepsis`): infection source + SIRS criteria + organ dysfunction. Altered mental status is an SOFA criteria point.
- **Traumatic brain injury** (`traumatic-brain-injury`): history of head trauma, may be occult in elderly or intoxicated
- **Epidural hematoma** (`epidural-hematoma`): lucid interval then rapid deterioration, temporal bone fracture
- **Subdural hematoma** (`subdural-hematoma`): elderly, anticoagulated, chronic alcoholism. May have minor or forgotten trauma.
- **Hyperkalemia** (`hyperkalemia`): K+ > 6.5 → cardiac arrhythmia → arrest. ECG changes: peaked T waves, widened QRS.
- **Acute hepatic failure** (`acute-hepatic-failure`): jaundice, coagulopathy, encephalopathy. Ammonia level elevated.
- **Thyroid storm** (`thyroid-storm`): hyperthermia, tachycardia, agitation → delirium → coma
- **Post-cardiac arrest** (`cardiac-arrest`): post-anoxic encephalopathy

### Emergent
- **HHS** (`hhs`): glucose > 600, serum osmolality > 320, minimal acidosis (vs DKA)
- **Adrenal crisis** (`adrenal-crisis`): hypotension, hyponatremia, hyperkalemia, chronic steroid use with acute stressor
- **Alcohol withdrawal** (`alcohol-withdrawal`): tremor, tachycardia, diaphoresis, visual hallucinations, seizures. Delirium tremens 48-96 hours after last drink.
- **Benzodiazepine overdose** (`benzodiazepine-overdose`): CNS depression, respiratory depression (especially with opioid co-ingestion)
- **Acetaminophen overdose** (`acetaminophen-overdose`): may be asymptomatic initially; delayed hepatic failure → encephalopathy
- **Toxic alcohol ingestion** (`toxic-alcohol-ingestion`): methanol (visual symptoms, osmolar gap), ethylene glycol (calcium oxalate crystals, osmolar + anion gap)
- **Serotonin syndrome** (`serotonin-syndrome`): clonus, hyperreflexia, agitation, hyperthermia. Serotonergic drug exposure.
- **NMS** (`neuroleptic-malignant-syndrome`): lead-pipe rigidity, hyperthermia, autonomic instability. Antipsychotic exposure.
- **Anticholinergic toxidrome** (`anticholinergic-toxidrome`): "hot as a hare, blind as a bat, dry as a bone, red as a beet, mad as a hatter." Dilated pupils, dry mucosa, urinary retention.
- **Sympathomimetic toxidrome** (`sympathomimetic-toxidrome`): agitation, diaphoresis, tachycardia, hypertension, dilated pupils, hyperthermia
- **Heat stroke** (`heat-stroke`): core temp > 40°C, CNS dysfunction, prior exertion or environmental exposure
- **Hypothermia** (`hypothermia`): core temp < 35°C, progressive confusion → coma
- **Hypertensive emergency** (`hypertensive-emergency`): SBP > 180 with encephalopathy (posterior reversible encephalopathy syndrome)
- **Tumor lysis syndrome** (`tumor-lysis-syndrome`): recent chemotherapy, hyperkalemia, hyperuricemia, hyperphosphatemia, hypocalcemia

### Urgent
- **Acute psychosis** (`acute-psychosis`): AMS must be organic until proven otherwise. Psychiatric diagnosis only after medical etiologies excluded.
- **Acute agitation** (`acute-agitation`): requires medical workup to exclude organic cause before attributing to psychiatric etiology.
- **Lithium toxicity** (`lithium-toxicity`): tremor, nystagmus, ataxia → confusion → seizure. Narrow therapeutic window.

## Workup

**All AMS patients:**
- Fingerstick glucose (bedside, immediate)
- CBC, BMP (electrolytes, glucose, BUN, creatinine, calcium)
- Hepatic panel (AST, ALT, bilirubin, albumin, alkaline phosphatase)
- Urinalysis (UTI is the most common cause of AMS in elderly — but do NOT anchor on positive UA without considering other causes)
- VBG or ABG (pH, lactate, CO2)
- 12-lead ECG
- Continuous monitoring (SpO2, HR, BP, cardiac telemetry)
- Core temperature (rectal — oral/temporal unreliable in AMS)

**Based on clinical suspicion:**
- **Stroke/ICH:** Non-contrast head CT → CTA head/neck if large vessel occlusion suspected. CT perfusion if within thrombectomy window.
- **Meningitis/encephalitis:** Blood cultures, LP (CSF cell count, protein, glucose, gram stain, culture, HSV PCR, cryptococcal antigen). Give empiric antibiotics BEFORE LP if any delay.
- **Toxicology:** Serum ethanol, acetaminophen level, salicylate level, UDS, extended toxicology panel, osmolality (calculate osmolar gap), carboxyhemoglobin
- **Metabolic:** Ammonia, TSH/free T4, cortisol, magnesium, phosphorus
- **Seizure:** EEG (for nonconvulsive status epilepticus — must have high index of suspicion in unexplained AMS)
- **Trauma:** CT head, C-spine imaging per NEXUS/Canadian C-Spine Rule

## Treatment

Treatment is etiology-specific. Immediate stabilization:

- **Airway protection:** GCS ≤ 8 → RSI (see `rapid-sequence-intubation`). Airway before diagnosis.
- **D50 (dextrose 50%):** 25-50 mL IV (1 amp = 25 g) for glucose < 60 mg/dL. Give thiamine 100 mg IV simultaneously if alcoholism/malnutrition suspected.
- **Naloxone:** 0.4 mg IV/IM/IN for suspected opioid toxicity, titrate to respiratory effort
- **Empiric meningitis treatment (if suspected):** Vancomycin 25-30 mg/kg IV + ceftriaxone 2 g IV + dexamethasone 0.15 mg/kg IV (before or with first antibiotic dose). Add acyclovir 10 mg/kg IV if encephalitis suspected.
- **Seizure management:** Lorazepam 0.1 mg/kg IV (max 4 mg) first-line for active seizures → levetiracetam 60 mg/kg IV (max 4500 mg) or fosphenytoin 20 mg PE/kg IV for ongoing seizures (see `status-epilepticus`)
- **Activated charcoal:** 1 g/kg PO (max 50 g) if toxic ingestion within 1-2 hours and intact airway/gag
- **Cooling:** Active cooling for heat stroke (target < 39°C within 30 min): ice water immersion, evaporative cooling, cold IV fluids
- **Flumazenil:** Generally AVOID in undifferentiated AMS. Risk of precipitating seizures in chronic benzodiazepine users or mixed ingestions. Reserve for known isolated BZD ingestion in BZD-naive patient.

## Disposition

- **ICU:** GCS ≤ 8, intubated, status epilepticus, meningitis/encephalitis, large stroke/ICH, hemodynamic instability, active toxidrome requiring monitoring
- **Step-down/telemetry:** AMS resolving with treatment (glucose correction, naloxone), metabolic derangement being corrected (DKA protocol), seizure requiring monitoring
- **Floor admission:** UTI with delirium in elderly (stable), mild electrolyte abnormalities, medication toxicity requiring observation
- **Observation:** Alcohol intoxication pending sobriety and reassessment, mild intoxication with improving mental status
- **Discharge:** Rarely appropriate for AMS. Only if cause clearly identified and fully resolved (e.g., hypoglycemia corrected with confirmed PO tolerance and adjusted medication, simple alcohol intoxication with return to baseline, vasovagal episode with transient confusion).
- **Psychiatric evaluation:** Only AFTER complete medical workup is negative. New-onset psychosis in a patient > 40 is organic until proven otherwise.

## Pitfalls

1. **Attributing AMS in the elderly to "UTI" without further workup.** Positive UA is common in elderly patients (asymptomatic bacteriuria prevalence 20-50% in institutionalized patients). Subdural hematoma, NCSE, medication toxicity, and metabolic derangements are frequently missed when "UTI" becomes the anchor.

2. **Failure to check glucose immediately.** Hypoglycemia mimics stroke, seizure, intoxication, and psychiatric disease. A 5-second fingerstick prevents all downstream diagnostic errors. This must be the first test performed.

3. **Missing nonconvulsive status epilepticus (NCSE).** Up to 8% of comatose patients and 37% of ICU patients with unexplained AMS are in NCSE. Without EEG, this diagnosis is invisible. Request EEG for any AMS without clear etiology, especially post-seizure patients who do not return to baseline.

4. **Assuming intoxication without considering trauma.** The intoxicated patient with AMS may also have a subdural hematoma, epidural hematoma, or cervical spine injury from a fall. CT head is mandatory if any concern for head injury, even if alcohol is clearly present.

5. **Delaying antibiotics for meningitis while awaiting LP or CT.** Time to antibiotics is the strongest predictor of mortality in bacterial meningitis. If meningitis is on the differential, give empiric antibiotics immediately. Blood cultures before antibiotics if possible, but do not delay antibiotics for anything.

6. **Not obtaining CO level.** Pulse oximetry reads carboxyhemoglobin as oxyhemoglobin. SpO2 will be falsely normal. Obtain carboxyhemoglobin on ABG or co-oximetry for any AMS patient, especially with headache, multiple patients from same household, or winter heating season.

7. **Anchoring on psychiatric diagnosis.** New-onset psychiatric symptoms (especially in patients > 40 without psychiatric history) are organic until proven otherwise. Anti-NMDA receptor encephalitis, thyroid storm, hepatic encephalopathy, and many toxidromes mimic primary psychiatric disease.

8. **Forgetting to examine for medication patches.** Fentanyl patches, clonidine patches, and scopolamine patches are easily missed and can cause profound AMS. Perform full skin survey.
