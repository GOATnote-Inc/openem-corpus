---
id: benzodiazepine-overdose
condition: Benzodiazepine Overdose
aliases: [benzo overdose, benzodiazepine toxicity, benzo poisoning, sedative-hypnotic overdose, benzodiazepine intoxication]
icd10: [T42.4X1A, T42.4X2A, T42.4X4A, T42.6X1A]
esi: 2
time_to_harm: "< 1 hour (respiratory arrest in large ingestion or co-ingestion)"
mortality_if_delayed: "Isolated benzodiazepine OD mortality low (<1%); co-ingestion with opioids or ethanol: 5-15%"
category: toxicologic
track: tier1
sources:
  - type: guideline
    ref: "ACMT Position Statement: Flumazenil Use in Benzodiazepine Overdose. American College of Medical Toxicology. J Med Toxicol. 2018"
  - type: pubmed
    ref: "Penninga EI, Graudal N, Ladekarl MB, Jürgens G. Adverse events associated with flumazenil treatment for the management of suspected benzodiazepine intoxication — a systematic review with meta-analyses of randomised trials. Basic Clin Pharmacol Toxicol. 2016;118(1):37-44"
    pmid: "26096314"
  - type: pubmed
    ref: "Hojer J, Baehrendtz S, Gustafsson L. Benzodiazepine poisoning: experience of 702 admissions to an intensive care unit during a 14-year period. J Intern Med. 1989;226(2):117-122"
    pmid: "2769176"
  - type: pubmed
    ref: "Gaudreault P, Guay J, Thivierge RL, Verdy I. Benzodiazepine poisoning: clinical and pharmacological considerations and treatment. Drug Saf. 1991;6(4):247-265"
    pmid: "1888441"
  - type: pubmed
    ref: "Jones CM, McAninch JK. Emergency department visits and overdose deaths from combined use of opioids and benzodiazepines. Am J Prev Med. 2015;49(4):493-501"
    pmid: "26143953"
last_updated: "2026-02-18"
compiled_by: agent
risk_tier: B
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
# Benzodiazepine Overdose

## Recognition

### Classic Presentation
- CNS depression: sedation, drowsiness progressing to obtundation and coma
- Slurred speech, ataxia, incoordination
- Respiratory depression (hypoventilation, decreased respiratory rate, hypoxia)
- Hypotension (mild; severe hypotension suggests co-ingestion)
- Hypothermia (mild)
- Hyporeflexia
- Anterograde amnesia
- Normal or mildly dilated pupils (unlike opioids — miosis)

### Key Distinguishing Features
| Feature | Isolated Benzo OD | Benzo + Opioid | Benzo + Ethanol |
|---|---|---|---|
| Pupils | Normal to mildly dilated | Miotic (pinpoint) | Normal |
| Respiratory depression | Moderate | Severe | Severe |
| Response to flumazenil | Reversal of sedation | Partial (opioid effect persists) | Partial |
| Response to naloxone | None | Reversal of opioid component | None |
| Mortality risk | Low (~1%) | High (synergistic) | Moderate-High |

### Duration of Action by Agent
| Benzodiazepine | Onset | Duration | Half-life |
|---|---|---|---|
| Midazolam | 1-5 min IV | 1-2 hr | 1.5-2.5 hr |
| Alprazolam | 15-30 min PO | 4-6 hr | 6-12 hr |
| Lorazepam | 5-15 min IV | 6-8 hr | 10-20 hr |
| Diazepam | 1-5 min IV | 6-12 hr | 20-100 hr (active metabolites) |
| Clonazepam | 30-60 min PO | 8-12 hr | 18-50 hr |
| Chlordiazepoxide | 30-60 min PO | 12-24 hr | 24-48 hr (active metabolites) |

### Red Flags Suggesting Co-Ingestion or Alternate Diagnosis
- Profound coma (GCS < 6) — isolated benzo OD rarely causes deep coma
- Severe hypotension (SBP < 90)
- Pinpoint pupils (opioid co-ingestion)
- Seizures (paradoxical with benzos — consider TCA, sympathomimetic, or withdrawal as alternate diagnosis)
- Metabolic acidosis (ASA, methanol, ethylene glycol co-ingestion)
- Cardiac conduction abnormalities (TCA co-ingestion — wide QRS)

## Critical Actions

| Action | Target |
|---|---|
| Airway assessment and management | Immediately |
| Pulse oximetry and capnography | Continuous monitoring |
| IV access | Within minutes |
| Naloxone trial | If opioid co-ingestion suspected (miosis, RR < 12) |
| Glucose check | Immediately (exclude hypoglycemia) |
| Co-ingestion screening | Within 1 hour |
| ECG | Within 15 minutes |

1. Assess airway, breathing, circulation. Position patient in recovery position if protecting airway; intubate if GCS < 8 or inability to maintain airway/oxygenation.
2. Apply continuous pulse oximetry and capnography.
3. Establish IV access. Administer dextrose 25 g IV (D50W 50 mL) if glucose < 60 mg/dL.
4. If opioid co-ingestion suspected: naloxone 0.4-2 mg IV/IM/IN. Titrate to respiratory effort, not consciousness.
5. Obtain ECG (rule out TCA co-ingestion — QRS > 100 ms).
6. Send co-ingestion labs: acetaminophen level, salicylate level, ethanol level, BMP, CBC, VBG, LFTs.
7. Activated charcoal 50 g PO/NGT if ingestion < 1 hour AND airway protected (intubated or GCS ≥ 14 with intact gag reflex).

## Differential Diagnosis

- Opioid overdose (miosis, respiratory depression, response to naloxone)
- Ethanol intoxication (breath odor, elevated ethanol level)
- GHB/GBL overdose (rapid fluctuation in consciousness, myoclonus, vomiting)
- Barbiturate overdose (similar presentation; longer duration, more cardiovascular depression)
- Tricyclic antidepressant overdose (wide QRS, seizures, anticholinergic signs)
- Carbon monoxide poisoning (headache, exposure history, cherry-red skin rare)
- Hypoglycemia (diaphoresis, tremor, rapid response to dextrose)
- Post-ictal state (tongue bite, incontinence, witnessed seizure)
- Hepatic encephalopathy (chronic liver disease stigmata, asterixis, elevated ammonia)
- CNS infection (fever, meningismus, focal deficits)
- Stroke (focal neurologic deficits, asymmetry)
- "Z-drug" overdose (zolpidem, zaleplon — similar toxidrome to benzodiazepines)

## Workup

### Bedside
- **Point-of-care glucose:** Exclude hypoglycemia
- **ECG:** QRS duration (>100 ms suggests TCA co-ingestion → sodium bicarbonate), QTc prolongation
- **Pulse oximetry and continuous capnography:** Monitor for hypoventilation before desaturation occurs

### Laboratory
- **Acetaminophen level:** Screen all intentional overdoses (co-ingestion is common and occult)
- **Salicylate level:** Screen all intentional overdoses
- **Ethanol level:** Synergistic respiratory depression with benzodiazepines
- **BMP:** Electrolytes, glucose, renal function, anion gap
- **VBG:** pH, pCO2 (respiratory acidosis from hypoventilation)
- **CBC:** Baseline
- **LFTs:** If chronic use or hepatic metabolism relevant
- **Urine drug screen:** Confirms benzodiazepine exposure but does NOT change acute management. False negatives common (UDS does not detect many synthetic benzodiazepines: clonazepam, lorazepam, alprazolam, midazolam may test negative on immunoassay).
- **Serum benzodiazepine levels:** Not clinically useful in acute management; do not order.

### Imaging
- **CXR:** If aspiration suspected (witnessed vomiting while obtunded)
- **CT head:** If altered mental status does not improve as expected, focal neurologic deficits, or history of trauma

## Treatment

### Supportive Care (Mainstay)
- **Airway management:** Jaw thrust, oropharyngeal airway, bag-valve-mask ventilation as temporizing measures. Endotracheal intubation if unable to maintain airway or oxygenation. RSI with propofol or etomidate (avoid additional benzodiazepines for RSI).
- **IV fluids:** Normal saline 20 mL/kg bolus for hypotension. Vasopressors (norepinephrine 0.05-0.5 mcg/kg/min) if refractory — suggest co-ingestion or alternate diagnosis.
- **Warming:** Active rewarming if hypothermic (forced-air warming blanket)

### Activated Charcoal
- **Activated charcoal 50 g PO** (1 g/kg in pediatrics) if:
  - Ingestion within 1 hour
  - Airway protected (GCS ≥ 14 with intact gag, or intubated)
  - No vomiting
- Contraindicated if: decreased consciousness without airway protection, caustic co-ingestion, anticipated need for endoscopy

### Flumazenil (Use With Extreme Caution)
- **Competitive GABA-A antagonist** — reverses benzodiazepine effect
- **Dose:** 0.2 mg IV over 30 seconds. If no response at 60 seconds: 0.3 mg IV. Then 0.5 mg IV every 60 seconds. Maximum initial cumulative dose: 3 mg. If partial response, may titrate to 5 mg total.
- **Onset:** 1-2 minutes. **Duration:** 45-90 minutes.
- **Re-sedation risk:** Flumazenil duration (45-90 min) is shorter than most benzodiazepines. Patient may re-sedate after initial reversal. Requires prolonged monitoring.

### Flumazenil Contraindications (CRITICAL)
Flumazenil is **contraindicated** in the following — administration may cause life-threatening seizures:
- **Chronic benzodiazepine use or dependence** (precipitates withdrawal seizures)
- **Co-ingestion with pro-convulsant drugs** (TCAs, cocaine, isoniazid, bupropion, tramadol, lithium)
- **Known seizure disorder**
- **Elevated intracranial pressure**
- **Unknown overdose** (if co-ingestant not determined, assume TCA until proven otherwise by ECG)
- **Wide QRS on ECG** (suggests TCA — flumazenil removes seizure protection)

### When Flumazenil IS Appropriate
- Known isolated benzodiazepine ingestion (e.g., witnessed pediatric ingestion of a single agent)
- Iatrogenic benzodiazepine oversedation (procedural sedation reversal)
- No history of chronic benzodiazepine use
- Normal ECG (narrow QRS, no conduction abnormalities)

### Monitoring
- Continuous pulse oximetry and capnography for minimum 4-6 hours
- If flumazenil given: monitor for minimum 2 hours AFTER last dose (re-sedation risk)
- Neuro checks every 30-60 minutes
- Serial GCS documentation

## Disposition

### Discharge Criteria (After Observation)
- GCS 15, normal vital signs for ≥ 4-6 hours after peak expected effect
- Normal oxygen saturation on room air
- Ambulating without ataxia
- Tolerating PO
- No evidence of co-ingestion requiring treatment
- If intentional: psychiatry evaluation completed and safe disposition plan
- If flumazenil was administered: minimum 2 hours observation after last dose without re-sedation

### Admission Criteria
- Persistent respiratory depression requiring supplemental O2 or ventilatory support
- GCS < 14 after 4-6 hours of observation
- Co-ingestion requiring treatment or monitoring (APAP, TCA, opioid)
- Aspiration pneumonitis
- Intubated patients → ICU
- Recurrent sedation after flumazenil (long-acting benzo)

### ICU Admission
- Intubation/mechanical ventilation
- Vasopressor requirement
- Significant co-ingestion (TCA with cardiac toxicity, opioid requiring naloxone infusion)
- Aspiration with respiratory failure

### Psychiatric Evaluation
- Mandatory for all intentional overdoses before discharge
- Assess suicide risk, access to medications, safety plan
- 1:1 observation until psychiatry clears

## Pitfalls

1. **Giving flumazenil to a patient with unknown ingestion or chronic benzodiazepine use.** Flumazenil precipitates severe, treatment-resistant withdrawal seizures in benzodiazepine-dependent patients. In the ED, most overdose patients have unknown or poly-drug ingestion. Default to supportive care. Flumazenil is reserved for known, isolated, acute benzodiazepine ingestion in non-dependent patients.

2. **Assuming isolated benzodiazepine overdose without screening for co-ingestion.** Co-ingestion with opioids, ethanol, TCAs, or acetaminophen is common and dramatically increases morbidity and mortality. Obtain APAP level, salicylate level, ethanol level, and ECG on every intentional overdose.

3. **Relying on urine drug screen to exclude benzodiazepine ingestion.** Standard immunoassay UDS has poor sensitivity for many common benzodiazepines (alprazolam, clonazepam, lorazepam, midazolam frequently test false-negative). A negative UDS does not exclude benzodiazepine overdose. Treat the clinical presentation.

4. **Discharging after flumazenil reversal without adequate observation.** Flumazenil has a half-life of 45-90 minutes — shorter than nearly every benzodiazepine. Re-sedation and respiratory depression will occur after flumazenil wears off. Observe for minimum 2 hours after last flumazenil dose.

5. **Failing to check a fingerstick glucose.** Hypoglycemia presents identically to sedative-hypnotic overdose (altered consciousness, diaphoresis). Every patient with altered mental status requires an immediate point-of-care glucose.

6. **Not obtaining an ECG to rule out TCA co-ingestion.** Tricyclic antidepressant overdose causes CNS depression mimicking benzodiazepine OD but with lethal cardiac toxicity (wide QRS, arrhythmias). A wide QRS (>100 ms) mandates sodium bicarbonate and absolutely contraindicates flumazenil.

7. **Using additional benzodiazepines for RSI in a benzodiazepine overdose patient.** If intubation is required, use non-benzodiazepine induction agents (propofol, etomidate, ketamine). Additional benzodiazepines will deepen and prolong the toxicity.

8. **Discharging intentional overdose patients without psychiatric evaluation.** All intentional benzodiazepine overdoses represent a suicide attempt or gesture until proven otherwise. Psychiatric evaluation is mandatory before discharge. Patients elope and reattempt.

9. **Waiting for desaturation before intervening on hypoventilation.** Capnography detects hypoventilation (rising EtCO2) before pulse oximetry detects desaturation. Monitor capnography in all significantly obtunded patients. A rising EtCO2 > 50 mmHg with declining mental status requires intervention.
