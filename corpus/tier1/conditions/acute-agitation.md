---
id: acute-agitation
condition: Acute Agitation
aliases: [agitated delirium, acute behavioral emergency, excited delirium]
icd10: [R45.1, R45.6]
esi: 2
time_to_harm: "< 1 hour"
mortality_if_delayed: "Risk of sudden death with excited delirium, positional asphyxia"
category: psychiatric
track: tier1
sources:
  - type: guideline
    ref: "Nordstrom K, et al. AAEP Project BETA Overview: Best Practices in Evaluation and Treatment of Agitation. West J Emerg Med. 2012;13(1):3-10"
    pmid: "22461914"
  - type: guideline
    ref: "Wilson MP, Pepper D, Currier GW, et al. AAEP Project BETA Psychopharmacology Workgroup Consensus Statement. West J Emerg Med. 2012;13(1):26-34"
    pmid: "22461918"
  - type: pubmed
    ref: "Riddell J, Tran A, Bengiamin R, et al. Ketamine as a First-Line Treatment for Severely Agitated ED Patients. Am J Emerg Med. 2017;35(7):1000-1004"
    pmid: "28237385"
  - type: meta-analysis
    ref: "Gonçalves-Bradley DC, et al. Rapid Tranquilization of the Agitated Patient in the ED: Systematic Review and Network Meta-Analysis. Am J Emerg Med. 2022;53:119-128"
    pmid: "34823192"
  - type: review
    ref: "Takeuchi A, Ahern TL, Henderson SO. Excited Delirium Syndrome: Defining Based on a Review of the Literature. J Emerg Med. 2011;41(5):549-555"
    pmid: "21440403"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: B
validation:
  schema_version: "2.0"
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  guideline_version_reference: null
  provenance_links: []
---

# Acute Agitation

The #1 psychiatric emergency. Undifferentiated agitation demands simultaneous management of safety AND diagnostic evaluation. The agitated patient who "looks psychiatric" can be hypoglycemic, hypoxic, or herniating. Treat the behavior, then find the cause.

---

## Recognition

### Clinical Presentation
- Psychomotor hyperactivity, verbal or physical aggression, inability to remain still
- Spectrum: mild restlessness to combative/violent behavior
- Use a validated scale (Richmond Agitation-Sedation Scale [RASS] or Behavioral Activity Rating Scale [BARS]) to quantify severity and track response

### Red Flags for Medical Etiology
- Age > 40 with no psychiatric history
- Acute onset (minutes to hours, not days)
- Vital sign abnormalities: fever, tachycardia, hypertension, hypoxia
- Altered sensorium, visual hallucinations, fluctuating consciousness
- Focal neurological deficits
- Head trauma or signs of trauma
- Known medical comorbidities (diabetes, liver disease, HIV, seizure disorder)
- New medication or recent medication change

### Risk Assessment
- Immediate danger to self or others: escalate to chemical sedation without delay
- Excited delirium features: hyperthermia, diaphoresis, extraordinary strength, pain tolerance, tachycardia, rhabdomyolysis risk, sudden cardiac arrest risk
- Always assume a weapon may be present; maintain safe distance, clear the room of sharps and throwable objects

---

## Critical Actions

### 1. Scene Safety
- Alert security before entering the room
- Remove potential weapons, IV poles, sharps containers
- Maintain a clear exit path; never position yourself between the patient and the door

### 2. De-escalation (First-Line)
- Speak calmly, use short sentences, offer choices ("Would you like water or a blanket?")
- Identify and address unmet needs (pain, hunger, fear, disorientation)
- Maintain safe distance (2 arm-lengths)
- Avoid confrontation, do not argue with delusions
- Effective de-escalation prevents 50-80% of restraint events (Project BETA)

### 3. Chemical Sedation (When De-escalation Fails)
Onset times and specific protocols below. Choose agent based on suspected etiology.

| Agent | Dose | Route | Onset | Redose |
|---|---|---|---|---|
| **Droperidol** | 5-10 mg | IM | 5-10 min | May repeat 5 mg IM q15-20 min |
| **Ketamine** | 4-5 mg/kg | IM | 3-5 min | 2 mg/kg IM if needed at 10 min |
| **B52 cocktail** | Diphenhydramine 50 mg + haloperidol 5 mg + lorazepam 2 mg | IM (single injection or 3 separate) | 10-20 min | Half-dose components at 30 min |
| **Olanzapine** | 10 mg | IM | 15-30 min | 5-10 mg IM q2h (max 30 mg/day) |
| **Midazolam** | 5 mg (0.05-0.1 mg/kg) | IM/IV | IM: 5-10 min; IV: 1-2 min | 2.5-5 mg q10-15 min |

### 4. Physical Restraints (Last Resort)
- Apply only when chemical sedation is inadequate AND patient poses imminent danger
- Use 4-point leather restraints in supine position
- **Never prone restrain** -- positional asphyxia risk
- Monitor q15 min: respiratory status, circulation to extremities, mental status
- Document ongoing need; reassess for removal q1h
- Order chemical sedation simultaneously; restraints are a bridge, not a treatment

### 5. Monitoring Post-Sedation
- Continuous pulse oximetry, cardiac monitoring
- Airway equipment at bedside (especially after ketamine or combination regimens)
- Check glucose immediately if not already obtained

---

## Differential Diagnosis

| Category | Conditions |
|---|---|
| **Psychiatric** | Acute psychosis (schizophrenia, brief psychotic disorder), mania/hypomania, severe anxiety/panic, personality disorder crisis (borderline), PTSD flashback, catatonic excitement |
| **Medical** | Hypoglycemia, hypoxia/hypercarbia, head injury/ICH, meningitis/encephalitis, thyroid storm, hepatic encephalopathy, hypertensive encephalopathy, seizure (postictal), sepsis, cerebral hypoperfusion, urinary retention, electrolyte derangement (hyponatremia, hypercalcemia) |
| **Substance-related** | Sympathomimetic intoxication (cocaine, methamphetamine, bath salts), alcohol intoxication, PCP/ketamine intoxication, anticholinergic toxicity, alcohol withdrawal, benzodiazepine withdrawal, opioid withdrawal, serotonin syndrome, NMS |
| **Environmental** | Heatstroke, pain, sleep deprivation, ICU delirium |

---

## Workup

Priority: rule out life-threatening medical causes. Do not delay sedation for workup.

### Immediate (Before or Concurrent with Sedation)
- **Point-of-care glucose** -- hypoglycemia is the most common treatable mimic
- **Pulse oximetry** -- hypoxia
- **Temperature** -- fever (infection, NMS, serotonin syndrome, thyroid storm) or hyperthermia (excited delirium, sympathomimetics)
- **Cardiac monitor** -- dysrhythmias, QTc (relevant to antipsychotic choice)

### After Sedation Achieved
- **Basic metabolic panel** -- Na, Ca, glucose, renal function
- **CBC** -- leukocytosis (infection)
- **Hepatic panel** -- hepatic encephalopathy
- **Urinalysis** -- UTI (especially elderly)
- **Urine drug screen** -- sympathomimetics, PCP, benzodiazepines; note: many synthetic cathinones not detected
- **Blood alcohol level**
- **TSH** -- if thyrotoxicosis suspected
- **Lactate** -- sepsis, excited delirium (rhabdomyolysis)
- **CK** -- rhabdomyolysis (especially with prolonged agitation or restraints)
- **CT head** -- new-onset agitation without clear psychiatric history, trauma, focal deficits, anticoagulant use
- **Lumbar puncture** -- if meningitis/encephalitis suspected after CT
- **ECG** -- baseline QTc before antipsychotic administration when feasible; do not delay treatment for ECG

---

## Treatment

### Agent Selection by Etiology

**Undifferentiated agitation (etiology unclear):**
- First-line: **Droperidol 5 mg IM** -- fastest onset, favorable side-effect profile
- Alternative: **Midazolam 5 mg IM** if QTc concern or droperidol unavailable
- Severe/refractory: **Ketamine 4 mg/kg IM**

**Known/suspected psychosis:**
- **Droperidol 5-10 mg IM** or **Haloperidol 5-10 mg IM**
- **Olanzapine 10 mg IM** (do NOT combine with parenteral benzodiazepines -- FDA black box warning for respiratory depression; separate administration by at least 1 hour)
- **Ziprasidone 20 mg IM** (alternative second-generation antipsychotic)

**Known/suspected substance intoxication:**
- Sympathomimetics (cocaine, methamphetamine): **Benzodiazepines first-line** -- midazolam 5 mg IM/IV or lorazepam 2 mg IV. Avoid antipsychotics as monotherapy (lower seizure threshold, impair heat dissipation)
- Alcohol intoxication: **B52 cocktail** or **droperidol 5-10 mg IM**
- PCP: **Benzodiazepines** (midazolam 5 mg IM); ketamine 4-5 mg/kg IM for refractory cases
- Anticholinergic toxicity: **Benzodiazepines only** (avoid antipsychotics -- worsen anticholinergic burden)

**Alcohol/benzodiazepine withdrawal:**
- **Benzodiazepines are definitive treatment**: diazepam 10-20 mg IV q10-15 min or midazolam 2-5 mg IV q5 min titrated to RASS 0 to -1
- Phenobarbital 10-15 mg/kg IV as adjunct or alternative in refractory cases

**Excited delirium / extreme behavioral emergency:**
- **Ketamine 4-5 mg/kg IM** -- most reliable single agent for severe agitation
- Intubation equipment at bedside; laryngospasm rate ~0.4%
- Aggressive cooling if hyperthermic (target temp < 39C)
- IV crystalloid resuscitation, monitor for rhabdomyolysis
- Anticipate need for ICU admission

### Dose Adjustments
- **Elderly (> 65 years):** Halve all doses. Start with haloperidol 2.5 mg IM or olanzapine 5 mg IM.
- **Pediatric:** Midazolam 0.1 mg/kg IM (max 5 mg). Olanzapine 0.1 mg/kg IM (max 10 mg) for adolescents. Ketamine 3-4 mg/kg IM.
- **Pregnancy:** Benzodiazepines preferred; avoid antipsychotics if possible; haloperidol is pregnancy category C (use if benefit outweighs risk).
- **Hepatic impairment:** Avoid or reduce benzodiazepines; prefer lorazepam (no hepatic oxidation).
- **Renal impairment:** Standard doses for most agents; avoid accumulation with repeated dosing.
- **QTc > 500 ms:** Avoid haloperidol, droperidol, ziprasidone. Use benzodiazepines or ketamine.

### Drug-Specific Precautions
- **Droperidol:** FDA black box for QTc prolongation (2001) based on high IV doses; IM doses of 5-10 mg have minimal QTc effect. Many EDs have returned to routine use. Obtain ECG when feasible but do not delay for it.
- **Ketamine:** Anticipate emergence reactions (10-20%); co-administer midazolam 2 mg IV/IM to reduce. Causes hypersalivation; consider glycopyrrolate 0.2 mg IV/IM. Transient rise in ICP/IOP is clinically insignificant in most scenarios.
- **Olanzapine:** Do NOT give with parenteral benzodiazepines. FDA warning based on 29 fatalities from respiratory depression with combination.
- **Haloperidol:** QTc prolongation dose-dependent. Akathisia and dystonia common; prophylax with diphenhydramine 25-50 mg or benztropine 1-2 mg.

---

## Disposition

### Safe for Psychiatric Evaluation When:
- Medically cleared: normal vitals, no focal neurological findings, glucose checked, toxicologic causes addressed
- Awake, oriented, no ongoing medical decompensation
- No residual respiratory depression or hemodynamic instability from sedation
- Can participate in psychiatric interview (even if still mildly irritable)

### Admission Criteria
- **ICU admission:** Excited delirium, rhabdomyolysis (CK > 5000), intubation after sedation, hemodynamic instability, unresolved medical cause (DKA, meningitis, status epilepticus)
- **Medical floor:** Ongoing medical workup required (e.g., new-onset psychosis in elderly requiring brain imaging + LP), moderate rhabdomyolysis, requiring frequent sedation redosing
- **Psychiatric admission:** Acute psychosis without medical cause, danger to self or others persists after medical clearance, unable to contract for safety
- **ED observation:** Intoxication expected to clear in < 12-24 hours, responding to treatment, stable vitals

### Discharge Criteria
- Etiology identified and treated (e.g., resolved intoxication, corrected hypoglycemia)
- No ongoing danger to self or others
- Back to baseline mental status
- Safe disposition plan confirmed (not to streets if altered)

---

## Pitfalls

1. **Attributing agitation to psychiatric cause without checking glucose.** Hypoglycemia kills faster than any psychiatric emergency. Point-of-care glucose is a 5-second test.

2. **Combining IM olanzapine with parenteral benzodiazepines.** FDA warning based on fatal respiratory depression. If a benzodiazepine was already given, choose a different antipsychotic (haloperidol, droperidol) or wait at least 1 hour.

3. **Prone restraint positioning.** Positional asphyxia risk is real and lethal, especially in obese patients, excited delirium, and after chemical sedation. Always restrain supine.

4. **Underdosing ketamine IM.** At 1-2 mg/kg IM, ketamine causes dysphoria without adequate sedation. Use 4-5 mg/kg IM for reliable effect. Weight-estimate, do not underestimate.

5. **Failing to monitor post-sedation.** Respiratory depression, aspiration, and rhabdomyolysis can develop after the patient "calms down." Continuous pulse oximetry and reassessment are mandatory.

6. **Using antipsychotic monotherapy for sympathomimetic intoxication.** Antipsychotics lower seizure threshold and impair thermoregulation. Cocaine and methamphetamine agitation requires benzodiazepines as the primary agent.

7. **Ignoring QTc before giving haloperidol or droperidol.** A QTc > 500 ms plus IV haloperidol is a torsades setup. If ECG is not feasible, prefer benzodiazepines or ketamine for the initial dose.

8. **Forgetting to check CK in prolonged agitation.** Any patient who has been agitated or restrained for > 30 minutes is at risk for rhabdomyolysis. CK, aggressive IV fluids, and urine output monitoring are needed.

9. **Leaving physical restraints on without chemical sedation or reassessment.** Restraints alone increase agitation, metabolic demand, and death risk. They are a bridge to chemical sedation, not a standalone treatment. Reassess q15 min.

10. **Anchoring on "frequent flyer" status.** The patient who presents weekly with alcohol-related agitation can also have a subdural hematoma, meningitis, or Wernicke encephalopathy. Each visit is a new evaluation.
