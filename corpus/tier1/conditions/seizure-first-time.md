---
id: seizure-first-time
condition: "First-Time Seizure — Emergency Evaluation"
aliases: [first seizure, new-onset seizure, seizure evaluation, unprovoked seizure, convulsion first episode]
icd10: [R56.9, R56.1, G40.909]
esi: 2
time_to_harm:
  irreversible_injury: "< 30 minutes (status epilepticus with neuronal death)"
  death: "< 60 minutes (status epilepticus, intracranial mass with herniation)"
  optimal_intervention_window: "< 5 minutes (terminate active seizure)"
category: presentations
condition_type: presentation
chief_complaint: "Seizure"
differential_categories:
  - category: life-threatening
    conditions:
      - status-epilepticus
      - subarachnoid-hemorrhage
      - hemorrhagic-stroke
      - bacterial-meningitis
      - hsv-encephalitis
      - epidural-hematoma
      - subdural-hematoma
      - hypoglycemia
      - hyperkalemia
      - eclampsia
      - hypertensive-emergency
      - carbon-monoxide-poisoning
  - category: emergent
    conditions:
      - acute-ischemic-stroke
      - alcohol-withdrawal
      - benzodiazepine-overdose
      - toxic-alcohol-ingestion
      - serotonin-syndrome
      - sympathomimetic-toxidrome
      - anticholinergic-toxidrome
      - neuroleptic-malignant-syndrome
      - febrile-seizure
      - tumor-lysis-syndrome
      - hypertensive-emergency
  - category: urgent
    conditions:
      - lithium-toxicity
      - cavernous-sinus-thrombosis
  - category: non-emergent
    conditions: []
red_flags:
  - "Prolonged seizure > 5 minutes (status epilepticus)"
  - "Failure to return to baseline mental status (ongoing seizure, NCSE, structural lesion)"
  - "Focal onset suggesting structural lesion"
  - "Age > 40 with first seizure (high probability of structural cause)"
  - "Fever with seizure in adult (CNS infection)"
  - "New focal neurological deficit postictal"
  - "Pregnancy (eclampsia)"
  - "Active anticoagulation (intracranial hemorrhage risk)"
  - "HIV/immunocompromised (CNS mass, toxoplasmosis, cryptococcal meningitis)"
  - "Preceding thunderclap headache (SAH)"
  - "History of recent head trauma"
decision_rules:
  - name: "Status Epilepticus Management Timeline"
    citation: "Neurocritical Care Society Guidelines for Status Epilepticus. Neurocrit Care. 2012;17(1):3-23."
    pmid: "22528274"
track: tier1
sources:
  - type: guideline
    ref: "AAN Practice Guideline: Evidence-based guideline: Management of an unprovoked first seizure in adults. Neurology. 2015;84(16):1705-1713."
    pmid: "25901057"
  - type: guideline
    ref: "ACEP Clinical Policy: Critical Issues in the Evaluation and Management of Adult Patients Presenting to the Emergency Department With Seizures. Ann Emerg Med. 2014;63(4):437-447.e15."
    pmid: "24655445"
  - type: guideline
    ref: "Neurocritical Care Society Guidelines for Status Epilepticus Management. Neurocrit Care. 2012;17(1):3-23."
    pmid: "22528274"
  - type: pubmed
    ref: "Krumholz A et al. Evidence-based guideline: Management of an unprovoked first seizure in adults: Report of the Guideline Development Subcommittee of the AAN and AES. Neurology. 2015;84(16):1705-1713."
    pmid: "25901057"
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
# First-Time Seizure — Emergency Evaluation

## Recognition

A first-time seizure in an adult is a common ED presentation (approximately 1% of ED visits). The critical ED tasks are: (1) terminate any active seizure, (2) identify and treat reversible causes, (3) determine if structural brain pathology is present, and (4) identify patients who need admission vs safe discharge.

**Is this actually a seizure?** Obtain witness description:
- Tonic-clonic activity (rhythmic jerking, bilateral > unilateral)
- Duration of motor activity
- Eye deviation (typically upward and lateral in seizure, closed eyes suggest psychogenic)
- Tongue bite (lateral tongue → highly specific for seizure; tip bite → less specific)
- Incontinence (supportive but not diagnostic — occurs in syncope too)
- Postictal confusion/drowsiness (typically 15-30 minutes, can last hours)
- Preceding aura (focal onset with secondary generalization)
- Prodrome (seconds of stereotyped symptoms → focal onset seizure; nausea/diaphoresis/tunnel vision → vasovagal)

**Seizure mimics:**
- Convulsive syncope (brief myoclonic jerks during syncope from cerebral hypoperfusion — NOT epilepsy)
- Psychogenic nonepileptic seizure (PNES): asynchronous movements, side-to-side head shaking, eyes closed, pelvic thrusting, waxing-waning intensity, preserved awareness, prolonged duration. Do NOT empirically treat with benzodiazepines.
- Rigors (shaking chills in sepsis)
- Movement disorders (dystonia, chorea)

**Provoked vs unprovoked:**
- **Provoked (acute symptomatic):** identifiable reversible trigger within 7 days — electrolyte abnormality, hypoglycemia, drug intoxication/withdrawal, acute brain injury (stroke, trauma, infection). Lower recurrence risk. Treatment targets the provoking factor.
- **Unprovoked:** no identifiable acute trigger. Higher recurrence risk (21-45% at 2 years). Requires consideration of antiepileptic drug initiation.

**Key history elements:**
- Witnessed account (phone the witness if not present)
- Prior seizures or epilepsy history (is this truly "first"?)
- Alcohol use and last drink (withdrawal seizures 6-48 hours after cessation)
- Drug use: cocaine, amphetamines, synthetic cannabinoids (provoked seizure)
- Medications: QTc-prolonging drugs (→ torsades), antidepressants (bupropion, tramadol lowers threshold), isoniazid, theophylline
- Head trauma history (recent or remote)
- Cancer history (brain metastases)
- HIV status (toxoplasmosis, lymphoma, PML, cryptococcal)
- Pregnancy (eclampsia)
- Family history of epilepsy

## Critical Actions

| Action | Target |
|---|---|
| Terminate active seizure | < 5 minutes from onset |
| Fingerstick glucose | < 2 minutes |
| Protect airway | Ongoing during seizure |
| CT head (non-contrast) | < 60 minutes post-seizure |
| ECG | < 30 minutes |

**Evaluation algorithm:**

1. **If actively seizing:**
   - Protect airway: lateral positioning, suction, jaw thrust. Do NOT place anything in the mouth.
   - Fingerstick glucose immediately → D50 if < 60 mg/dL
   - Lorazepam 0.1 mg/kg IV (max 4 mg) — first-line for seizure termination. Repeat once if seizure continues after 5 minutes.
   - If no IV access: midazolam 10 mg IM (> 40 kg) or diazepam 0.2 mg/kg PR (max 20 mg)
   - Seizure > 5 minutes = status epilepticus → escalate to second-line agent (see `status-epilepticus`)

2. **Postictal patient (seizure has stopped):**
   - Assess airway and breathing. Position laterally. Supplemental O2 if SpO2 < 94%.
   - Reassess GCS serially. Expected gradual improvement over 15-60 minutes.
   - If NOT improving as expected → consider ongoing seizure (NCSE), structural lesion, metabolic derangement, or intoxication.

3. **Focused exam:**
   - Vital signs including core temperature
   - Head/neck: signs of trauma, tongue laceration, neck stiffness
   - Neurological: pupils, lateralizing signs (Todd paralysis — postictal focal deficit is transient and does NOT require tPA; but document time and reassess)
   - Skin: track marks, medication patches, signs of liver disease (alcohol-related)

4. **CT head without contrast** — indicated for ALL first-time adult seizures (ACEP Level B recommendation). Identifies structural lesions in 10-30% of first seizures. Abnormal CT more likely with: focal onset, age > 40, focal postictal deficit, anticoagulation, HIV/immunocompromised, persistent AMS, new headache.

5. **LP** — if meningitis/encephalitis suspected (fever + headache + nuchal rigidity, immunocompromised). Give empiric antibiotics before LP if delay anticipated.

6. **Determine if provoked or unprovoked.** This drives disposition and treatment decisions.

## Differential Diagnosis

### Life-Threatening (causes of seizure requiring immediate treatment)
- **Status epilepticus** (`status-epilepticus`): continuous seizure > 5 minutes or recurrent seizures without return to baseline. Mortality 20-30% if not treated promptly.
- **Subarachnoid hemorrhage** (`subarachnoid-hemorrhage`): seizure at onset of thunderclap headache. SAH causes seizures in 6-18%.
- **Hemorrhagic stroke** (`hemorrhagic-stroke`): seizure with acute neurological deficit, hypertension, CT showing ICH
- **Bacterial meningitis** (`bacterial-meningitis`): seizure with fever, headache, nuchal rigidity. Empiric antibiotics immediately.
- **HSV encephalitis** (`hsv-encephalitis`): seizure with behavioral changes, temporal lobe focus, fever. Acyclovir 10 mg/kg IV empirically.
- **Epidural hematoma** (`epidural-hematoma`): post-traumatic seizure, lucid interval, rapid deterioration
- **Subdural hematoma** (`subdural-hematoma`): elderly/anticoagulated, seizure may be the presenting symptom
- **Hypoglycemia** (`hypoglycemia`): glucose < 60 → seizure. Check glucose immediately on EVERY seizing patient.
- **Hyperkalemia** (`hyperkalemia`): severe hyperkalemia can cause seizure and cardiac arrest
- **Eclampsia** (`eclampsia`): seizure in pregnant or postpartum (up to 6 weeks) woman with hypertension. Magnesium sulfate 4-6 g IV loading dose.
- **Hypertensive emergency** (`hypertensive-emergency`): PRES (posterior reversible encephalopathy) → seizure with severe HTN, visual changes, headache
- **CO poisoning** (`carbon-monoxide-poisoning`): seizure in setting of headache, confusion, multiple patients

### Emergent
- **Acute ischemic stroke** (`acute-ischemic-stroke`): 5-10% of strokes present with seizure, more common with cortical involvement. Todd paralysis must be distinguished from stroke (both cause postictal focal deficit).
- **Alcohol withdrawal** (`alcohol-withdrawal`): seizures 6-48 hours after last drink, typically generalized tonic-clonic, often multiple. Peak at 24 hours. Lorazepam for treatment and prevention.
- **Drug-related seizures:** cocaine, amphetamines, synthetic cannabinoids, bupropion, tramadol, isoniazid (treat with pyridoxine 5 g IV)
- **Benzodiazepine withdrawal** (`benzodiazepine-overdose`): similar timeline to alcohol withdrawal
- **Toxic alcohol ingestion** (`toxic-alcohol-ingestion`): methanol and ethylene glycol can cause seizures
- **Serotonin syndrome** (`serotonin-syndrome`): clonus, hyperthermia, seizure
- **Febrile seizure** (`febrile-seizure`): pediatric (6 months - 5 years), temperature-associated, typically brief and generalized
- **Tumor lysis syndrome** (`tumor-lysis-syndrome`): hyperkalemia, hyperphosphatemia, hypocalcemia → seizure

### Urgent
- **Lithium toxicity** (`lithium-toxicity`): tremor, nystagmus → seizure
- **Brain tumor** (new diagnosis): first seizure in adult > 40, focal onset, abnormal CT → MRI + neurosurgery/neuro-oncology consultation [No standalone corpus entry]
- **Cerebral venous thrombosis:** headache, seizure, focal deficit, papilledema in patient with prothrombotic risk factors [No standalone corpus entry]

## Workup

**All first-time seizure patients:**
- Fingerstick glucose (immediate — before any other test)
- CT head without contrast (ACEP Level B for all adults with first seizure)
- CBC, BMP (sodium, calcium, magnesium, glucose, BUN/Cr)
- Hepatic panel
- ECG (QTc prolongation, arrhythmia)
- Urinalysis
- Urine drug screen

**Based on clinical suspicion:**
- **Alcohol withdrawal:** Serum ethanol level, GGT, MCV
- **CNS infection:** LP (cell count, protein, glucose, gram stain, culture, HSV PCR). CT before LP only if: papilledema, focal deficit, immunocompromised, GCS < 12
- **Eclampsia:** Urine protein, hepatic panel, CBC with platelets, uric acid, LDH
- **Structural lesion on CT:** MRI brain with gadolinium for further characterization
- **Toxicological:** Serum ethanol, acetaminophen, salicylate, carboxyhemoglobin, specific drug levels (lithium, theophylline, isoniazid)
- **Electrolyte abnormality:** Ionized calcium, magnesium, phosphorus
- **Pyridoxine-responsive seizures:** Consider isoniazid overdose → pyridoxine 5 g IV empirically

**What NOT to routinely order:**
- EEG in the ED: rarely changes acute management. Obtain if nonconvulsive status epilepticus suspected (AMS not improving as expected postictal).
- MRI in the ED for uncomplicated first seizure with normal CT: outpatient MRI within 1-2 weeks is appropriate.
- Prolactin level: not sensitive or specific enough to distinguish seizure from PNES in the ED.

## Treatment

**Active seizure management:**
1. **First-line (0-5 minutes):** Lorazepam 0.1 mg/kg IV (max 4 mg per dose, repeat once), OR midazolam 10 mg IM (if no IV access), OR diazepam 0.2 mg/kg PR (max 20 mg)
2. **Second-line (5-20 minutes):** Levetiracetam 60 mg/kg IV (max 4500 mg) over 15 min, OR fosphenytoin 20 mg PE/kg IV, OR valproic acid 40 mg/kg IV (max 3000 mg)
3. **Third-line (> 20 minutes):** Refractory status epilepticus → RSI, intubation, propofol or midazolam infusion, ICU (see `status-epilepticus`)

**Post-seizure management:**
- Treat identified provoking cause (glucose, electrolytes, alcohol withdrawal, infection)
- Anti-seizure medication initiation: NOT mandatory after a single unprovoked seizure with normal CT and labs. AAN guideline: discuss risk of recurrence with patient (21-45% at 2 years). If patient/physician decide to treat, levetiracetam 500 mg PO BID is first-line (broad spectrum, minimal drug interactions, no monitoring required).
- Eclampsia: Magnesium sulfate 4-6 g IV over 15-20 minutes, then 1-2 g/hr infusion. Definitive treatment is delivery.
- Alcohol withdrawal seizures: Lorazepam 2 mg IV → CIWA-based protocol. Seizures may cluster. Phenytoin is NOT effective for alcohol withdrawal seizures.
- Isoniazid seizure: Pyridoxine (B6) 5 g IV (gram-for-gram dose matching ingested isoniazid if known; otherwise give 5 g)

## Disposition

- **ICU:** Status epilepticus (intubated on continuous infusion), persistent AMS, acute intracranial pathology requiring intervention, eclampsia
- **Telemetry/step-down:** Recurrent seizures, alcohol withdrawal with seizure (monitor for delirium tremens), abnormal CT with mass effect
- **Floor admission:** First seizure with identified structural lesion requiring further workup, seizure requiring IV antiepileptic therapy, provoked seizure requiring treatment of underlying cause (electrolyte correction, infection)
- **Observation:** First seizure in elderly patient pending MRI, repeat seizure in known epilepsy with medication adjustment
- **Discharge with neurology follow-up (1-2 weeks):**
  - Single unprovoked seizure with: normal CT, normal labs, returned to baseline mental status, reliable adult supervision for 24 hours, no driving until cleared by neurology
  - Provoked seizure with provoking factor identified and corrected (e.g., hypoglycemia treated, electrolyte normalized, drug-induced)
  - Clear and explicit return precautions: "Return immediately for another seizure, persistent confusion, headache, fever, weakness, or if you do not return to your normal self"
- **Driving restrictions:** Counsel that driving is restricted after a seizure (varies by state, typically 3-12 months seizure-free). Document this conversation.
- **Safety counseling:** No swimming alone, no heights, no operating heavy machinery, no bathing alone (shower with unlocked door). Provide written instructions.

## Pitfalls

1. **Assuming postictal confusion is "just postictal" when it persists.** Typical postictal confusion resolves within 30-60 minutes. Prolonged confusion (> 60 minutes) should raise suspicion for nonconvulsive status epilepticus, intracranial hemorrhage, meningitis/encephalitis, or metabolic derangement. Obtain EEG and reconsider imaging/LP.

2. **Not checking glucose.** Hypoglycemia causes seizures and is immediately treatable. A 5-second fingerstick prevents protracted diagnostic evaluation and ongoing neuronal injury. This must be the first test.

3. **Treating alcohol withdrawal seizures with phenytoin.** Phenytoin is NOT effective for alcohol withdrawal seizures (multiple RCTs). Benzodiazepines are the treatment. Phenytoin IS indicated if the patient has a structural lesion or pre-existing epilepsy in addition to alcohol withdrawal.

4. **Failure to consider eclampsia in postpartum patients.** Eclampsia can present up to 6 weeks postpartum. Every woman of reproductive age with a first seizure requires a pregnancy test. Postpartum women with seizure + hypertension = eclampsia until proven otherwise → magnesium sulfate.

5. **Discharging without addressing driving.** Failure to counsel about driving restrictions has both safety and medicolegal implications. Document the conversation. State-specific laws vary but typically require 3-12 months seizure-free.

6. **Missing Todd paralysis vs stroke.** Postictal focal weakness (Todd paralysis) occurs in 6-13% of seizures and typically resolves within 24 hours (most within 15 minutes). However, stroke can cause seizure followed by persistent deficit. If uncertain → stroke workup (CT, CTA). Document serial neurological exams showing improvement if attributing to Todd paralysis.

7. **Sending home without adult supervision.** Patients with a first seizure are at risk for recurrence in the first 24-48 hours. Discharge is appropriate only if the patient has a responsible adult to monitor them and clear return precautions are provided.
