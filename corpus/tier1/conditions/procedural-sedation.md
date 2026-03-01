---
id: procedural-sedation
condition: Procedural Sedation
aliases: [procedural sedation and analgesia, PSA, conscious sedation, moderate sedation, ED sedation]
icd10: [Z51.81, T88.59XA]
esi: 2
time_to_harm: "Minutes (respiratory depression, aspiration, cardiovascular collapse from oversedation)"
category: procedural
track: tier1
sources:
  - type: guideline
    ref: "Godwin SA, Burton JH, Gerardo CJ, et al. Clinical Policy: Procedural Sedation and Analgesia in the Emergency Department. Ann Emerg Med. 2014;63(2):247-258."
    pmid: "24438649"
  - type: guideline
    ref: "Green SM, Roback MG, Kennedy RM, et al. Clinical Practice Guideline for Emergency Department Ketamine Dissociative Sedation: 2011 Update. Ann Emerg Med. 2011;57(5):449-461."
    pmid: "21256625"
  - type: pubmed
    ref: "Bellolio MF, Gilani WI, Barrionuevo P, et al. Incidence of Adverse Events in Adults Undergoing Procedural Sedation in the Emergency Department: A Systematic Review and Meta-Analysis. Acad Emerg Med. 2016;23(2):119-134."
    pmid: "26801209"
  - type: guideline
    ref: "ASA Practice Guidelines for Moderate Procedural Sedation and Analgesia 2018. Anesthesiology. 2018;128(3):437-479."
    pmid: "29334501"
  - type: textbook
    ref: "Roberts JR, Custalow CB, Thomsen TW. Roberts and Hedges' Clinical Procedures in Emergency Medicine and Acute Care, 7th Edition. Elsevier. 2019."
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
# Procedural Sedation

## Recognition

**Indications:**
- Fracture/dislocation reduction
- Cardioversion (see cardioversion-defibrillation)
- Abscess incision and drainage (large/deep)
- Laceration repair in uncooperative patients (especially pediatric)
- Foreign body removal
- Chest tube insertion (when time permits)
- Lumbar puncture in agitated patients
- Burn debridement
- Any painful ED procedure requiring more than local anesthesia

**Levels of Sedation (ASA Continuum):**

| Level | Responsiveness | Airway | Spontaneous Ventilation | CV Function |
|-------|---------------|--------|------------------------|-------------|
| Minimal (anxiolysis) | Normal to verbal | Unaffected | Unaffected | Unaffected |
| Moderate | Purposeful to verbal/tactile | No intervention needed | Adequate | Usually maintained |
| Deep | Purposeful to repeated/painful stimuli | May need intervention | May be inadequate | Usually maintained |
| General anesthesia | Unarousable | Intervention often required | Frequently inadequate | May be impaired |

**Target level for most ED procedures:** moderate to deep sedation

**Contraindications:**
- ASA class >= IV with hemodynamic instability (relative — risk-benefit assessment)
- Inability to manage airway complications (no equipment, no trained personnel)
- Known difficult airway without backup plan
- Active vomiting with aspiration risk (address first)
- Severe COPD/OSA with baseline hypoventilation (higher risk; use ketamine over propofol)

## Critical Actions

| Action | Target |
|--------|--------|
| Pre-sedation assessment | ASA class, airway assessment, fasting status |
| Equipment and personnel check | Before sedation |
| Continuous monitoring | SpO2, ETCO2, ECG, BP, visual observation |
| Time to discharge | Meet discharge criteria (modified Aldrete score >= 9) |

1. **Pre-sedation assessment** — ASA class, airway exam, medical history, medications, allergies, fasting status
2. **Obtain informed consent**
3. **Assemble equipment** — airway management supplies, monitoring, reversal agents
4. **Assign roles** — sedation provider (physician), monitoring nurse, proceduralist
5. **Administer sedation** — titrate to desired level
6. **Perform procedure** during sedation window
7. **Monitor recovery** — until discharge criteria met

## Differential Diagnosis

**Alternative Pain/Anxiety Management:**

| Alternative | When to Use |
|-------------|------------|
| Local/regional anesthesia alone | Small procedures; nerve blocks for fractures/dislocations |
| Hematoma block | Distal radius fracture reduction |
| Femoral nerve block | Hip fracture, femur fracture |
| Fascia iliaca block | Hip fracture (landmark or US-guided) |
| Intranasal fentanyl/midazolam | Pediatric anxiolysis for minor procedures |
| Nitrous oxide (50:50 N2O/O2) | Moderate analgesia; patient-administered; rapid onset/offset |
| Oral/IM sedation | Lower acuity; longer onset; less control |
| General anesthesia in OR | Procedures requiring prolonged deep sedation or paralysis |

## Workup

**Pre-Sedation Checklist:**

| Assessment | Details |
|-----------|---------|
| ASA classification | I-II: standard risk; III: increased risk, proceed with caution; IV-V: anesthesia consultation |
| Airway assessment | Mallampati, neck mobility, mouth opening, MOANS for BVM difficulty |
| Fasting status | ACEP 2014: fasting is NOT required for ED procedural sedation; does not reduce aspiration risk; do NOT delay for NPO status |
| Allergies | Propofol (egg/soy — clinically insignificant cross-reactivity), latex |
| Medications | MAOIs (avoid meperidine), anticoagulants, respiratory depressants |
| Medical history | OSA, COPD, hepatic disease, renal disease, seizure history |

**Equipment:**

| Item | Specification |
|------|---------------|
| Monitoring | Continuous SpO2, waveform capnography (ETCO2), cardiac monitor, BP |
| Airway | BVM, oral/nasal airways, laryngoscope, ETT, SGA, suction |
| IV access | Functional IV line; saline flush available |
| Reversal agents | Flumazenil 0.2 mg IV (benzodiazepine reversal); naloxone 0.04-0.4 mg IV (opioid reversal) |
| Medications | Sedative and analgesic agents (see below) |
| Suction | Yankauer connected and tested |
| Oxygen | Nasal cannula at 2-4 L/min; NRB available |

## Treatment

### Sedation Agent Selection

| Agent | Dose | Onset | Duration | Best For | Key Risks |
|-------|------|-------|----------|----------|-----------|
| **Propofol** | 1 mg/kg IV bolus, then 0.5 mg/kg q2-3min PRN | 30-45 sec | 5-10 min | Short procedures; rapid recovery; cardioversion | Hypotension; apnea; no analgesia (combine with opioid) |
| **Ketamine** | 1-2 mg/kg IV over 60 sec; or 4 mg/kg IM | IV: 1 min; IM: 3-5 min | IV: 15-20 min; IM: 20-30 min | Pediatric sedation; hemodynamically unstable; asthma | Emergence reactions (15% adults, 1-5% children); laryngospasm (0.3%); vomiting (7-26%) |
| **Etomidate** | 0.1-0.15 mg/kg IV | 30-60 sec | 5-15 min | Short procedures; elderly; cardiac disease | Myoclonus; adrenal suppression (single dose clinically insignificant for sedation) |
| **Propofol + Ketamine ("ketofol")** | 0.5 mg/kg each, mixed or sequential | 30-60 sec | 10-15 min | Balanced sedation + analgesia; lower propofol dose = less hypotension | Requires two medications; limited evidence advantage over either alone |
| **Fentanyl + Midazolam** | Fentanyl 1 mcg/kg + midazolam 0.05 mg/kg IV | 2-3 min | 30-60 min | Moderate sedation for shorter procedures; titratability | Respiratory depression (synergistic); prolonged sedation in elderly/hepatic disease |
| **Nitrous oxide (50% N2O / 50% O2)** | Self-administered via demand valve | 1-2 min | 5 min after cessation | Minor procedures; laceration repair; pediatric | Nausea; contraindicated in pneumothorax, bowel obstruction, middle ear surgery |

### Ketamine Specifics (Most Common ED Sedation Agent)

**Adult dosing:**
- IV: 1-1.5 mg/kg IV push over 60 seconds; additional 0.5 mg/kg IV q5-10min PRN
- IM: 4-5 mg/kg IM (if no IV access)
- Emergence reaction prophylaxis: midazolam 0.03 mg/kg IV (controversial — ACEP guideline does not mandate)
- Ondansetron 4 mg IV (reduces vomiting; administer before ketamine)

**Pediatric dosing:**
- IV: 1-2 mg/kg IV push over 60 seconds
- IM: 4-5 mg/kg IM
- Recovery: 60-120 minutes (longer than adults)
- Emergence reactions rare in children < 10 years (< 5%)

**Contraindications to ketamine:**
- Age < 3 months (relative — limited safety data)
- Active psychosis or schizophrenia (relative)
- Previously documented ketamine allergy
- Conditions where increased BP is harmful: prior concern about ICP elevation has been largely refuted; ketamine is safe in TBI

### Propofol Specifics

**Dosing:**
- Load: 1 mg/kg IV over 30 seconds
- Supplemental: 0.5 mg/kg IV q2-3min as needed for procedure
- Reduce dose by 30-50% in elderly and hemodynamically unstable patients
- Pair with fentanyl 0.5-1 mcg/kg IV for analgesia

**Key considerations:**
- Causes dose-dependent hypotension (mean 10-15 mmHg drop) and respiratory depression
- Pre-treat with IV fluid 250-500 mL NS to mitigate hypotension
- No analgesia — must add fentanyl or regional block for painful procedures
- Fastest recovery of any IV sedation agent (~10 minutes to baseline)

### Monitoring During Sedation

- **Continuous pulse oximetry** — desaturation < 90% requires intervention
- **Waveform capnography (ETCO2)** — detects hypoventilation 30-60 seconds before desaturation; recommended for all moderate/deep sedation
- **ECG** — continuous cardiac rhythm
- **BP** — q5 min
- **Visual observation** — chest rise, skin color, level of consciousness
- **Dedicated monitoring provider** — NOT the proceduralist; one person whose sole job is monitoring the patient

### Managing Adverse Events

| Event | Intervention |
|-------|-------------|
| Apnea (< 15 sec) | Stimulate, jaw thrust, wait for spontaneous breathing |
| Prolonged apnea (> 15-30 sec) | BVM ventilation; consider naloxone/flumazenil if opioid/benzo |
| Desaturation (SpO2 < 90%) | Supplemental O2, chin lift, oral airway, BVM |
| Hypotension (SBP < 90) | IV fluid bolus 500 mL NS; reduce/hold propofol |
| Laryngospasm (ketamine) | Jaw thrust + positive pressure BVM; if refractory: succinylcholine 0.5-1 mg/kg IV |
| Emergence reaction (ketamine) | Midazolam 0.05 mg/kg IV; quiet, dark environment |
| Vomiting | Suction; turn patient lateral; ondansetron 4 mg IV |

### Post-Procedure
- Monitor until discharge criteria met
- Modified Aldrete Score >= 9/10: consciousness, activity, circulation, respiration, SpO2
- Minimum observation: 30 minutes after last medication dose (propofol/etomidate); 60-120 minutes (ketamine IM); variable (midazolam/fentanyl — until fully alert)
- Discharge with responsible adult; no driving for 24 hours

## Disposition

- **Uncomplicated sedation with full recovery:** discharge home with responsible adult; written instructions
- **Adverse event requiring airway intervention:** observe minimum 2 hours after event; admission if recurrent
- **Prolonged sedation (> 60 minutes post last dose):** evaluate for medication interaction, hepatic/renal impairment; observation unit or admission
- **Failed sedation (inadequate sedation despite maximum doses):** consider alternative agent, OR consultation for general anesthesia

## Pitfalls

1. **Fasting requirement delaying necessary procedures.** ACEP clinical policy (2014) states that preprocedural fasting is NOT required for ED procedural sedation. Aspiration is exceedingly rare (< 1:10,000 in ED sedation) and fasting status does not reduce this risk. Do not delay fracture reduction or other time-sensitive procedures for NPO status.

2. **Not using capnography during moderate/deep sedation.** Pulse oximetry detects desaturation 30-60 seconds after hypoventilation begins. Capnography detects apnea and hypoventilation in real time. Studies show capnography reduces hypoxic events by 17%. Waveform ETCO2 should be standard for all moderate/deep sedation.

3. **Using propofol without analgesia for painful procedures.** Propofol is a sedative-hypnotic with no analgesic properties. A patient sedated with propofol alone for fracture reduction will have pain-mediated catecholamine surges, movement, and require higher sedation doses. Add fentanyl 1 mcg/kg IV or regional anesthesia.

4. **Routinely pre-treating all ketamine patients with midazolam to prevent emergence reactions.** ACEP guidelines do not recommend routine midazolam pre-treatment. Emergence reactions occur in 10-20% of adults but are brief and self-limited. Midazolam prolongs recovery time and may not prevent emergence reactions. Reserve for patients with a history of emergence reactions.

5. **Administering ketamine IV too rapidly.** Rapid IV bolus (< 30 seconds) increases the risk of apnea and laryngospasm. Administer over 60 seconds. IM ketamine does not have this issue.

6. **Having the proceduralist also serve as the sedation monitor.** A provider focused on fracture reduction cannot simultaneously monitor respiratory status and SpO2. A dedicated monitoring provider (nurse or second physician) whose sole responsibility is observing the patient is mandatory during moderate/deep sedation.
