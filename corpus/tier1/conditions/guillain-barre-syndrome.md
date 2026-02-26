---
id: guillain-barre-syndrome
condition: "Guillain-Barr\xE9 Syndrome"
aliases: [GBS, acute inflammatory demyelinating polyradiculoneuropathy, AIDP, ascending paralysis]
icd10: [G61.0]
esi: 2
time_to_harm: "< 48 hours for respiratory failure"
mortality_if_delayed: "3-7% mortality; 20% persistent disability"
category: neurological
track: tier1
sources:
  - type: guideline
    ref: "AAN Practice Parameter: Immunotherapy for Guillain-Barré Syndrome. Neurology. 2003;61(6):736-740"
    pmid: "14504313"
  - type: review
    ref: "Shahrizaila N, et al. Guillain-Barré syndrome. Lancet. 2021;397:1214-1228"
    pmid: "33647239"
  - type: review
    ref: "Willison HJ, Jacobs BC, van Doorn PA. Guillain-Barré syndrome. Lancet. 2016;388:717-727"
    pmid: "26948435"
  - type: review
    ref: "Leonhard SE, et al. Diagnosis and management of GBS in ten steps. Nat Rev Neurol. 2019;15:671-683"
    pmid: "31541214"
  - type: guideline
    ref: "EAN/PNS Guideline on diagnosis and treatment of Guillain-Barré syndrome. Eur J Neurol. 2023"
    pmid: "37814552"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: B
validation:
  schema_version: "2.0"
  automated_consistency_check: "2026-02-27"
  dose_range_validator: "2026-02-27"
  unit_normalization_check: "2026-02-27"
  cross_file_consistency_check: "2026-02-27"
  citation_presence_check: "2026-02-27"
  duplicate_content_check: "2026-02-27"
  outlier_detection_flag: clear
  provenance_links: []
---

## Recognition

### Core Presentation
- **Ascending symmetric weakness** beginning in distal lower extremities, progressing proximally over hours to days (nadir typically 2-4 weeks)
- **Areflexia or hyporeflexia** -- universal finding; absent ankle jerks earliest sign
- **Sensory symptoms** (paresthesias, numbness) common but motor weakness dominates
- **Post-infectious onset** in ~70%: symptoms begin 1-4 weeks after antecedent illness
  - Campylobacter jejuni (most common, ~30%), CMV, EBV, Mycoplasma pneumoniae, Zika virus, SARS-CoV-2, influenza

### Variants

| Variant | Key Features |
|---------|-------------|
| AIDP | Classic ascending weakness + areflexia; demyelinating on NCS; most common form in North America/Europe |
| AMAN | Pure motor axonal; no sensory involvement; strongly associated with C. jejuni; more common in Asia |
| AMSAN | Motor + sensory axonal; severe course, poor recovery |
| Miller Fisher syndrome | Ophthalmoplegia + ataxia + areflexia; anti-GQ1b antibodies (>90%); minimal limb weakness |
| Pharyngeal-cervical-brachial | Oropharyngeal weakness, neck flexor weakness, upper limb weakness; mimics brainstem stroke or botulism |
| Bifacial weakness with paresthesias | Bilateral facial palsy + distal paresthesias; reflexes may be preserved early |

### Red Flags Triggering GBS Workup
- Bilateral weakness progressing over hours to days
- Loss of deep tendon reflexes in a patient presenting with weakness
- Recent GI or respiratory illness followed by weakness
- Bilateral facial palsy
- Respiratory distress with proximal weakness

## Critical Actions

### Immediate (First 60 Minutes)
1. **Airway assessment** -- do NOT wait for respiratory distress to measure pulmonary function
2. **Measure NIF and FVC** at bedside (portable spirometry)
3. Continuous cardiac monitoring (autonomic instability)
4. Peripheral IV access x2
5. NPO if bulbar weakness present

### Respiratory Monitoring -- The "20/30/40 Rule"
Intubate if ANY of the following:
- **FVC < 20 mL/kg** (or < 1 L in average adult)
- **NIF (MIP) weaker than -30 cmH2O** (i.e., -25 or -20)
- **FVC decline > 30%** from baseline over serial measurements
- **FVC < 15 mL/kg** -- near-mandatory intubation threshold

Serial measurements q2-4h in any patient not yet intubated. Trend matters more than single value.

Additional intubation triggers:
- Inability to count to 20 in single breath
- Orthopnea or paradoxical breathing (diaphragm fatigue)
- Bulbar dysfunction with aspiration risk
- Rapid clinical deterioration regardless of numbers

**Do not rely on SpO2 alone** -- desaturation is a late finding in neuromuscular respiratory failure. ABG may show early hypercapnia before hypoxemia.

### Immunotherapy -- Start Within 2 Weeks of Symptom Onset

**IVIG (first-line in most EDs)**
- **0.4 g/kg IV daily x 5 days** (total 2 g/kg over 5 days)
- Infusion rate: start 0.01-0.02 mL/kg/min, advance to 0.04-0.08 mL/kg/min as tolerated
- Premedicate: acetaminophen 1000 mg PO + diphenhydramine 25-50 mg IV for infusion reactions
- Monitor for: anaphylaxis (check IgA level if not urgent), renal failure, aseptic meningitis, thromboembolism

**Plasma Exchange (PLEX) -- equally effective**
- 5 sessions over 10-14 days
- Exchange volume: 40-50 mL/kg per session (approximately 1-1.5 plasma volumes)
- Replacement fluid: 5% albumin (preferred) or FFP
- More effective than IVIG when started within 7 days of symptom onset
- Preferred if IVIG contraindicated (IgA deficiency, renal insufficiency)

**Do NOT combine IVIG + PLEX** -- no added benefit; IVIG after PLEX negates exchange effect.

**Do NOT give PLEX after IVIG** -- removes the immunoglobulin just administered.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Spinal cord compression** | Sensory level, upper motor neuron signs (hyperreflexia, Babinski), bladder dysfunction early, back pain at level |
| **Transverse myelitis** | Sensory level, bladder involvement, often hyperreflexic below level, MRI cord signal change |
| **Myasthenia gravis** | Fatigable weakness, ocular involvement predominates, reflexes preserved, no sensory symptoms, positive edrophonium/ice test |
| **Tick paralysis** | Ascending paralysis identical to GBS; search scalp/skin for embedded tick; rapid reversal with tick removal; NCS normal |
| **Botulism** | Descending paralysis (cranial nerves first), fixed dilated pupils, dry mouth, GI symptoms; EMG: incremental response |
| **Acute intermittent porphyria** | Abdominal pain, psychiatric symptoms, motor > sensory neuropathy, hyponatremia, elevated urine porphobilinogen |
| **Critical illness polyneuropathy** | Occurs in ICU setting, sepsis/MODS context; NCS: axonal pattern; no antecedent infection pattern |
| **Hypokalemic periodic paralysis** | Episodic, reflexes may be preserved, serum K+ low, no sensory findings, no CSF abnormalities |
| **Conversion disorder** | Inconsistent exam, give-way weakness, Hoover sign, normal reflexes, normal NCS/EMG |

## Workup

### ED Labs and Studies
- **Lumbar puncture**: Albuminocytologic dissociation (elevated CSF protein with normal WBC < 5 cells/mm3). NOTE: CSF may be normal in first week -- do not use normal LP to exclude GBS early in course
  - Typical CSF protein: 0.45-2.0 g/L (45-200 mg/dL)
  - If WBC > 50 cells/mm3, reconsider diagnosis (HIV, Lyme, CMV, sarcoidosis, lymphomatous meningitis)
- **FVC and NIF**: Serial measurements q2-4h; document trend
- **CBC, CMP, Mg, Phos**: Rule out electrolyte-driven weakness
- **ESR, CRP**: Nonspecific; baseline
- **Anti-ganglioside antibodies**: Anti-GM1 (AMAN), anti-GQ1b (Miller Fisher) -- send but do not wait for results to treat
- **Blood cultures**: If infectious trigger suspected
- **Stool culture for Campylobacter**: Epidemiologic interest; does not change acute management
- **IgA level**: Before IVIG if time permits (IgA deficiency = anaphylaxis risk)
- **Lyme serologies, HIV**: If clinically indicated

### Imaging
- **MRI spine with gadolinium**: Nerve root enhancement in GBS (cauda equina); primary role is excluding cord compression
- **CT head**: If altered mental status or atypical features

### Electrophysiology (Inpatient)
- **NCS/EMG**: Definitive classification (AIDP vs AMAN vs AMSAN). May be normal in first 1-2 weeks. Prolonged F-waves and absent H-reflex are earliest findings.

## Treatment

### Immunotherapy
See Critical Actions above for full IVIG and PLEX protocols.

### Corticosteroids -- NOT Effective
- **Steroids do not improve outcomes in GBS** (unlike CIDP)
- IV methylprednisolone does not hasten recovery and is not recommended
- Do not confuse GBS with CIDP -- CIDP responds to steroids, GBS does not

### Autonomic Instability Management
Present in ~70% of severe GBS; leading cause of death in ICU.

| Problem | Management |
|---------|-----------|
| **Hypertension** | Short-acting agents ONLY: labetalol 10-20 mg IV q10min (avoid long-acting antihypertensives; BP may swing to hypotension) |
| **Hypotension** | IV crystalloid bolus (500-1000 mL NS); if refractory, phenylephrine 40-100 mcg IV bolus or norepinephrine 0.05-0.3 mcg/kg/min infusion |
| **Bradycardia** | Atropine 0.5 mg IV, repeat q3-5min (max 3 mg); temporary pacing if refractory |
| **Tachyarrhythmia** | Short-acting beta-blockers (esmolol 500 mcg/kg IV bolus then 50-200 mcg/kg/min); avoid agents that depress AV conduction in patients with labile rhythms |
| **Ileus / urinary retention** | Bladder catheterization; bowel regimen; neostigmine 0.5-2.5 mg IV for acute colonic pseudo-obstruction (Ogilvie) |

**Key principle**: Use only short-acting vasoactive agents. Autonomic lability means a hypertensive crisis can become profound hypotension within minutes.

### Pain Management
Pain occurs in >50% of GBS patients. Neuropathic and musculoskeletal.
- Gabapentin 300 mg PO TID (titrate to 1200 mg TID)
- Carbamazepine 200 mg PO BID (alternative)
- Opioids for severe pain: morphine 2-4 mg IV q4h PRN
- NSAIDs for musculoskeletal pain: ketorolac 15-30 mg IV q6h (max 5 days)
- Avoid excessive sedation that masks respiratory decline

### DVT Prophylaxis
- Enoxaparin 40 mg SC daily (CrCl > 30) OR heparin 5000 units SC q8h (CrCl < 30)
- Sequential compression devices on admission
- High VTE risk: immobilized patients with weakness

### Other Supportive Care
- Stress ulcer prophylaxis: famotidine 20 mg IV q12h (if ICU)
- Physical therapy: early passive range of motion
- Nutrition: NG/OG tube feeding if bulbar weakness precludes PO
- Bowel regimen: senna + docusate; polyethylene glycol PRN

## Disposition

### ICU Admission Criteria (Admit ALL GBS Patients; ICU for Any of the Following)
- FVC < 20 mL/kg or declining trend
- NIF weaker than -30 cmH2O
- Bulbar dysfunction (dysphagia, dysarthria, aspiration risk)
- Rapidly progressive weakness
- Autonomic instability (labile BP, arrhythmia)
- Need for intubation or mechanical ventilation
- Inability to ambulate independently

### Floor Admission (Mild GBS Only)
- Ambulatory with mild distal weakness
- Stable FVC > 25 mL/kg with no decline on serial measurement
- No bulbar symptoms
- No autonomic instability
- Must have q4h neuro checks, q4-6h FVC/NIF monitoring, and telemetry

### Discharge from ED -- Almost Never Appropriate
- GBS is an admission diagnosis. Even mild presentations require inpatient monitoring because trajectory is unpredictable.
- Only exception: very mild suspected GBS (paresthesias only, normal strength, normal FVC) with next-day neurology follow-up and reliable return precautions. This is rare.

## Pitfalls

1. **Relying on SpO2 to assess respiratory status**: Neuromuscular respiratory failure causes hypoventilation with preserved oxygenation until late. By the time SpO2 drops, the patient is near arrest. Serial FVC/NIF are mandatory.

2. **Normal LP in the first week does not exclude GBS**: Albuminocytologic dissociation is present in only ~50% of patients in the first week. CSF protein may not peak until week 2-3. Treat based on clinical suspicion.

3. **Giving corticosteroids**: Steroids are ineffective in GBS (RCT evidence). This is not CIDP. Steroids waste time and add side effects. Withhold and start IVIG or PLEX.

4. **Combining IVIG and PLEX or sequencing them improperly**: IVIG after PLEX removes exchanged antibodies. PLEX after IVIG removes the therapeutic immunoglobulin. Choose one. Never combine.

5. **Failure to check for tick paralysis**: Ascending paralysis with areflexia is identical to GBS. A single embedded tick (often occult in scalp, axilla, perineum) causes paralysis that reverses within hours of removal. Full skin survey before committing to GBS diagnosis.

6. **Using long-acting antihypertensives for autonomic hypertension**: Blood pressure in GBS autonomic instability is labile. A long-acting agent given during a hypertensive spike may cause refractory hypotension 30 minutes later. Use only short-acting agents (labetalol IV, esmolol, nitroprusside).

7. **Delayed intubation**: Waiting for frank respiratory failure instead of acting on FVC/NIF trends. A declining FVC that has not yet crossed 20 mL/kg but has dropped 30% from baseline is an intubation indication. Crash intubation in a patient with autonomic instability carries high arrest risk.

8. **Missing Miller Fisher variant**: Ophthalmoplegia + ataxia + areflexia without significant limb weakness. May be dismissed as posterior fossa stroke, Wernicke encephalopathy, or brainstem lesion. Anti-GQ1b antibodies are confirmatory.

9. **Not trending FVC/NIF serially**: A single normal FVC at presentation does not exclude future respiratory failure. GBS progresses over days. Measurements must be repeated q2-4h and the trend plotted.

10. **Assuming GBS cannot cause bladder dysfunction**: While early/prominent bladder symptoms should prompt consideration of spinal cord lesion, up to 25% of GBS patients develop transient urinary retention. Do not exclude GBS solely on this basis.

11. **Forgetting DVT prophylaxis**: Immobilized paralyzed patients are at extreme VTE risk. Start pharmacologic prophylaxis on admission unless active bleeding.
