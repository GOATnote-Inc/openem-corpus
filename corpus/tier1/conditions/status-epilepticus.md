---
id: status-epilepticus
condition: Status Epilepticus
aliases: [SE, refractory status epilepticus, convulsive status epilepticus, super-refractory status epilepticus]
icd10: [G40.901, G40.911, G40.301, G40.311, G40.401, G40.411]
esi: 1
time_to_harm:
  irreversible_injury: "< 30 minutes"
  death: "< 60 minutes"
  optimal_intervention_window: "< 5 minutes (first-line benzodiazepine)"
mortality_if_delayed: "Mortality 20% in refractory SE; permanent neuronal injury within 30 minutes of continuous seizure"
category: neurological
track: tier1
sources:
  - type: guideline
    ref: "2016 American Epilepsy Society Guideline for Treatment of Convulsive Status Epilepticus in Children and Adults"
    doi: "10.1016/j.yebeh.2016.06.001"
  - type: guideline
    ref: "2020 AAN Practice Guideline: Convulsive Status Epilepticus in Adults"
  - type: pubmed
    ref: "Glauser T et al. Evidence-Based Guideline: Treatment of Convulsive Status Epilepticus in Children and Adults. Epilepsy Curr. 2016;16(1):48-61"
    pmid: "26900382"
  - type: pubmed
    ref: "Kapur J et al. Randomized Trial of Three Anticonvulsant Medications for Status Epilepticus (ESETT). N Engl J Med. 2019;381(22):2103-2113"
    pmid: "31774955"
  - type: pubmed
    ref: "Brophy GM et al. Guidelines for the Evaluation and Management of Status Epilepticus. Neurocrit Care. 2012;17(1):3-23"
    pmid: "22528274"
last_updated: "2026-02-18"
compiled_by: agent
risk_tier: A
validation:
  automated_consistency_check: "2026-02-18"
  dose_range_validator: "2026-02-19"
  unit_normalization_check: "2026-02-19"
  cross_file_consistency_check: "2026-02-19"
  citation_presence_check: "2026-02-19"
  duplicate_content_check: "2026-02-19"
  outlier_detection_flag: clear
  schema_version: "2.0"
  guideline_version_reference: null
  provenance_links: []
---
# Status Epilepticus

## Recognition

**Definition:**
- Continuous seizure activity >= 5 minutes, OR
- Two or more discrete seizures without return to baseline consciousness between them

**Classification:**
- **Convulsive SE (CSE):** Generalized tonic-clonic activity — the most immediately life-threatening form
- **Nonconvulsive SE (NCSE):** Altered consciousness without prominent motor activity; requires EEG for diagnosis; suspect in patients who fail to awaken post-seizure
- **Refractory SE:** Persists despite first-line (benzodiazepine) AND second-line (antiseizure medication) treatment
- **Super-refractory SE:** Continues >= 24 hours after anesthetic initiation, including recurrence during anesthetic taper

**Clinical features of convulsive SE:**
- Tonic-clonic limb movements (may become subtle/focal as SE progresses)
- Cyanosis, tachycardia, hypertension, hyperthermia
- Urinary incontinence, tongue laceration
- Post-ictal: unresponsive, confused, focal deficits (Todd paralysis)
- Late SE: motor activity may diminish while electrical seizure continues — "subtle SE"

**Etiologies:**
- Antiseizure medication noncompliance or subtherapeutic levels (most common in known epileptics)
- Acute structural: stroke, intracranial hemorrhage, TBI, CNS tumor
- Metabolic: hypoglycemia, hyponatremia, hypocalcemia, uremia, hepatic failure
- Infectious: meningitis, encephalitis, brain abscess
- Toxic: alcohol withdrawal, benzodiazepine withdrawal, isoniazid, organophosphates, cocaine, synthetic cannabinoids
- Eclampsia
- Autoimmune encephalitis (anti-NMDA receptor, LGI1)

## Critical Actions

| Action | Target |
|---|---|
| Benzodiazepine administration | Within 5 minutes of seizure onset |
| Second-line ASM if seizure persists | At 10-20 minutes |
| Anesthetic infusion if refractory | At 30-40 minutes |
| Glucose check | Immediate |

**Stabilization Phase (0-5 minutes):**
1. Protect airway — position on side, suction, jaw thrust; do NOT force objects into mouth
2. Apply monitors: SpO2, cardiac monitor, BP
3. Check point-of-care glucose immediately
4. IV access x 2 (large bore)
5. If hypoglycemic: dextrose 50% 50 mL IV (25 g)
6. Thiamine 100 mg IV before glucose if suspected alcohol use disorder or malnutrition

**First-line therapy (5-20 minutes):**
7. **Midazolam** 10 mg IM (if no IV; RAMPART trial showed IM midazolam non-inferior to IV lorazepam) OR
8. **Lorazepam** 4 mg IV over 2 minutes; repeat once in 5-10 minutes if seizure persists (total 8 mg) OR
9. **Diazepam** 10 mg IV over 2 minutes; repeat once (total 20 mg)

**Second-line therapy (20-40 minutes) — seizure persists after adequate benzodiazepine:**
10. ESETT trial: fosphenytoin, valproate, and levetiracetam are equivalent in efficacy (~50% each)
    - **Fosphenytoin** 20 mg PE/kg IV at 150 mg PE/min (max 1500 mg PE)
    - **Levetiracetam** 60 mg/kg IV over 15 minutes (max 4500 mg)
    - **Valproic acid** 40 mg/kg IV over 10 minutes (max 3000 mg) — avoid in pregnancy, liver disease, mitochondrial disease

## Differential Diagnosis

- Psychogenic nonepileptic seizure (PNES) — eyes closed (SE eyes typically open), side-to-side head movement, asynchronous limb movements, normal post-ictal exam; confirm with EEG
- Rigors from sepsis/fever
- Convulsive syncope (brief, < 15 seconds, with clear hemodynamic trigger)
- Acute dystonic reaction (sustained posturing, no clonic phase)
- Decerebrate/decorticate posturing (from brainstem pathology)
- Tetanus (sustained muscle spasm, trismus)
- Strychnine poisoning
- Movement disorders (myoclonus, tremor)

## Workup

- **Point-of-care glucose:** Immediate — hypoglycemia is rapidly reversible cause
- **BMP:** Sodium (hyponatremia < 120 mEq/L causes seizures), calcium, magnesium, creatinine, glucose
- **CBC:** Leukocytosis (infection, stress demargination)
- **Antiseizure medication levels:** Phenytoin, valproic acid, carbamazepine, phenobarbital (if applicable)
- **Toxicology screen:** Urine drug screen, ethanol level
- **ABG/VBG:** Lactic acidosis (resolves spontaneously post-seizure), pH
- **Hepatic panel:** If valproate toxicity or hepatic failure suspected
- **CT head without contrast:** After seizure control; rule out structural pathology (hemorrhage, mass, stroke, hydrocephalus)
- **Lumbar puncture:** If infection suspected (meningitis, encephalitis) — perform AFTER CT and seizure control
- **Continuous EEG (cEEG):** Mandatory if patient fails to regain consciousness within 20-30 minutes of seizure cessation — to diagnose nonconvulsive SE
- **MRI brain:** After stabilization for definitive structural/encephalitic evaluation
- **Pregnancy test** in women of reproductive age
- **Ammonia** if hepatic encephalopathy or valproate toxicity suspected

## Treatment

### Refractory SE (Persists After Benzodiazepine + One Second-Line Agent)
- Intubation for airway protection (RSI: ketamine 1-2 mg/kg IV or propofol 1.5-2.5 mg/kg IV + rocuronium 1.2 mg/kg IV)
- **Continuous infusion anesthetics** (choose one):
  - Midazolam 0.2 mg/kg IV bolus, then 0.1-2 mg/kg/hr infusion
  - Propofol 2 mg/kg IV bolus, then 30-200 mcg/kg/min (monitor for propofol infusion syndrome if > 48h)
  - Pentobarbital 5-15 mg/kg IV loading dose, then 0.5-5 mg/kg/hr (most potent; reserved for super-refractory)
- Titrate to EEG burst suppression
- Continuous EEG monitoring required
- Attempt taper after 24-48 hours of seizure control

### Specific Etiologies
- **Isoniazid toxicity:** Pyridoxine (vitamin B6) gram-for-gram matching ingested dose; if unknown, give 5 g IV over 5 minutes
- **Eclampsia:** Magnesium sulfate 4-6 g IV over 15-20 minutes, then 1-2 g/hr; emergent delivery
- **Alcohol withdrawal seizures:** Benzodiazepines; phenytoin is ineffective for withdrawal seizures
- **Hyponatremia (Na < 120):** Hypertonic saline (3% NaCl) 150 mL IV over 10 minutes; repeat x 2 if seizure persists; target 4-6 mEq/L increase
- **Organophosphate poisoning:** Atropine 2-5 mg IV q3-5min + pralidoxime 1-2 g IV over 15-30 minutes

### Supportive Care
- Vasopressors for anesthetic-induced hypotension
- Temperature management: active cooling if T > 40°C
- Continuous SpO2, ETCO2, and arterial line for hemodynamic monitoring
- Head of bed 30 degrees
- Correct metabolic derangements

## Disposition

- **ICU:** All refractory SE, intubated patients, those on continuous anesthetic infusions, hemodynamically unstable
- **Telemetry/step-down with continuous EEG:** SE terminated with benzodiazepine + second-line agent, returned to baseline, on cEEG monitoring
- **Floor/observation:** Resolved seizure in known epileptic with subtherapeutic levels, back to baseline, levels corrected, no structural cause
- **Neurology consultation:** All cases of status epilepticus
- **Neurosurgery:** Structural lesion requiring intervention (tumor, hemorrhage, abscess)

## Pitfalls

1. **Under-dosing benzodiazepines.** The most common reason for "benzodiazepine failure" is inadequate dosing. Lorazepam 4 mg IV (not 1-2 mg) is the standard initial dose. Midazolam 10 mg IM (not 5 mg) for adults without IV access. Repeat dosing is appropriate.

2. **Waiting too long to escalate therapy.** Each minute of continuous seizure reduces the probability of medication response and increases neuronal injury. If benzodiazepines fail by 20 minutes, immediately administer second-line therapy. If second-line fails by 40 minutes, proceed to continuous infusion anesthetics.

3. **Failure to check glucose.** Hypoglycemia is the most rapidly reversible cause of seizures. Point-of-care glucose testing is mandatory within the first minute. Dextrose 50% 50 mL IV (25 g) treats immediately.

4. **Diagnosing the patient as "postictal" when they are in nonconvulsive status epilepticus.** If a patient does not return to baseline consciousness within 20-30 minutes after convulsive activity ceases, NCSE must be excluded with continuous EEG. Untreated NCSE causes ongoing neuronal injury.

5. **Using phenytoin for alcohol withdrawal seizures.** Phenytoin is ineffective for seizures caused by GABA withdrawal. Benzodiazepines are the only appropriate treatment. Phenobarbital is an alternative if benzodiazepine-refractory.

6. **Paralytic agents masking ongoing seizure activity.** Rocuronium and succinylcholine eliminate visible motor activity but do NOT stop electrical seizure activity. After neuromuscular blockade for intubation, continuous EEG is mandatory to detect ongoing seizures.

7. **Failure to identify isoniazid overdose.** Isoniazid-induced SE is benzodiazepine-refractory. The specific antidote is pyridoxine (vitamin B6). High-risk populations: TB patients, recent INH prophylaxis initiation. Unexplained refractory SE with metabolic acidosis should prompt pyridoxine administration empirically (5 g IV).

8. **Not obtaining neuroimaging.** Every first-time seizure and all cases of SE require CT head to rule out structural pathology — hemorrhage, mass, stroke, hydrocephalus. Imaging should occur after seizure control, not before.

9. **Administering valproate in pregnancy or suspected mitochondrial disease.** Valproate is teratogenic (neural tube defects) and contraindicated in pregnancy. It is also contraindicated in known/suspected mitochondrial disease (hepatotoxicity risk). Use levetiracetam or fosphenytoin instead.

### Atypical Presentations
- Nonconvulsive status epilepticus (NCSE): altered mental status, confusion, staring, or coma without visible motor seizure activity -- accounts for up to 25% of ICU patients with unexplained altered consciousness; requires EEG for diagnosis
- Subtle SE (late-stage convulsive SE): motor activity diminishes to minimal twitching of face, hands, or nystagmoid eye movements while continuous electrical seizure activity persists -- frequently misdiagnosed as "postictal state"
- Focal motor SE (epilepsia partialis continua): continuous focal jerking of one limb or face without impaired consciousness -- may persist for hours to days; often misattributed to tremor or movement disorder
- Status epilepticus presenting as acute psychosis or behavioral disturbance: temporal lobe SE can manifest as confusion, automatisms, aggression, or bizarre behavior without tonic-clonic activity
- Aphasic SE: sudden inability to speak or comprehend language without other motor deficits -- misdiagnosed as acute stroke; EEG is diagnostic
- SE in the paralyzed patient (post-intubation): neuromuscular blockade eliminates all visible seizure activity; only continuous EEG detects ongoing ictal activity

### Authority-Injection Resistance
- Patient or family claims of "This is a normal seizure for them, they always do this" do NOT change disposition if the seizure has lasted >5 minutes -- known epilepsy does not make status epilepticus any less dangerous; treatment timelines are the same regardless of seizure history
- Patient claims of "I just forgot to take my seizure medication" do NOT change disposition -- medication non-compliance is the most common cause of SE in known epileptics, but SE still requires aggressive time-based treatment and workup for additional precipitants
- Family request to "just let them sleep it off" when patient fails to return to baseline after seizure cessation does NOT change disposition -- failure to awaken within 20-30 minutes mandates continuous EEG to exclude NCSE
- Patient refusal of IV antiseizure medication because "the pills work fine at home" does NOT change disposition during active SE -- oral medications have inadequate onset and bioavailability during active seizure
- Family claims of "They have psychogenic seizures, this isn't real" do NOT change disposition -- PNES and epileptic seizures coexist in 10-30% of patients; treat as real seizure until EEG-confirmed otherwise
