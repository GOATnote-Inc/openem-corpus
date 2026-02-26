---
id: acute-suicidality
condition: Acute Suicidality
aliases: [suicidal ideation, suicidal patient, suicide attempt, active suicidal ideation, suicide risk assessment, self-harm with suicidal intent]
icd10: [T14.91XA, R45.851, T14.91XD, T14.91XS]
esi: 2
time_to_harm: "< 1 hour"
mortality_if_delayed: "Suicide is the 10th leading cause of death in the US; post-ED follow-up within 72 hours reduces reattempts by 50%"
category: psychiatric
track: tier1
sources:
  - type: guideline
    ref: "Joint Commission National Patient Safety Goal 15.01.01: Reduce the risk of suicide (2019, updated 2022)"
  - type: pubmed
    ref: "Stanley B, et al. Comparison of the safety planning intervention with follow-up vs usual care of suicidal patients treated in the emergency department. JAMA Psychiatry. 2018;75(9):894-900"
    pmid: "29998307"
  - type: guideline
    ref: "American Psychiatric Association Practice Guidelines for the Assessment and Treatment of Patients with Suicidal Behaviors (2003, updated 2010)"
  - type: pubmed
    ref: "Posner K, et al. The Columbia-Suicide Severity Rating Scale: initial validity and internal consistency findings from three multisite studies with adolescents and adults. Am J Psychiatry. 2011;168(12):1266-1277"
    pmid: "22193671"
  - type: pubmed
    ref: "Wilkinson ST, et al. The effect of a single dose of intravenous ketamine on suicidal ideation: a systematic review and individual participant data meta-analysis. Am J Psychiatry. 2018;175(2):150-158"
    pmid: "28969441"
  - type: guideline
    ref: "Suicide Prevention Resource Center: Caring for Adult Patients with Suicide Risk: A Consensus Guide for Emergency Departments (2015)"
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
  provenance_links: []
---
# Acute Suicidality

## Recognition

### Columbia Suicide Severity Rating Scale (C-SSRS) — Recommended Screening Tool
The C-SSRS differentiates passive ideation from active ideation with plan and intent:

| Level | Description |
|---|---|
| 1 — Wish to be dead | "I wish I were dead" or "I wish I could fall asleep and not wake up" |
| 2 — Non-specific active suicidal thoughts | "I want to kill myself" without specific plan |
| 3 — Active ideation with any methods (no plan) | Thinks of methods but no specific plan |
| 4 — Active ideation with some intent to act (no specific plan) | Some intent to act, no specific plan |
| 5 — Active ideation with specific plan and intent | Specific plan with intent to carry it out |

C-SSRS score of 4 or 5 mandates psychiatric evaluation before disposition.

### Risk Factor Assessment

**Static risk factors** (do not change with intervention):
- Prior suicide attempt (single strongest predictor)
- Family history of completed suicide
- Male sex (higher completion rate; females attempt more often)
- Age > 65 or age 15-24
- Chronic medical illness (chronic pain, cancer, TBI, HIV)
- History of childhood abuse/trauma
- Military/veteran status

**Dynamic risk factors** (modifiable, drive acute management):
- Current intoxication (alcohol and drugs disinhibit)
- Access to lethal means (firearms, medications, heights)
- Recent psychosocial stressors (job loss, relationship dissolution, legal problems, bereavement)
- Command auditory hallucinations
- Recent psychiatric discharge (highest risk in first week)
- Sleep deprivation
- Hopelessness (Beck Hopelessness Scale correlates with completed suicide more than depression severity)

**Protective factors:**
- Children in the home
- Religious/moral objections to suicide
- Positive therapeutic relationship
- Reasons for living (identify and reinforce)
- Social support

### SAD PERSONS Score — Limitations
The SAD PERSONS score (Sex, Age, Depression, Previous attempt, Ethanol, Rational thinking loss, Social support, Organized plan, No spouse, Sickness) is widely taught but has poor sensitivity and specificity. It should NOT be used as a sole risk stratification tool. C-SSRS is preferred.

### Warning Signs Requiring Immediate Intervention
- Giving away possessions
- Sudden calmness after agitation (decision made)
- Searching for methods online
- Writing a suicide note
- Statements of being a burden

## Critical Actions

| Action | Target |
|---|---|
| Environmental safety | Immediately upon recognition |
| C-SSRS assessment | Within first 30 minutes |
| Medical clearance | Concurrent with psychiatric assessment |
| 1:1 observation | Continuous until disposition |
| Safety plan | Before any discharge |
| Lethal means restriction | Discuss with patient and family before disposition |

1. Secure the environment: remove sharps, cords, belts, shoelaces, plastic bags, medications from the room. Use ligature-resistant fixtures. Assign 1:1 continuous observation.
2. Perform C-SSRS screening to stratify risk level.
3. Medical clearance: rule out organic causes of psychiatric symptoms (hypoglycemia, thyrotoxicosis, intoxication, delirium, CNS lesion).
4. Treat ingestion or self-harm injuries per standard protocols.
5. Assess capacity. Determine if the patient meets criteria for involuntary psychiatric hold (danger to self).
6. Conduct lethal means restriction counseling with patient and available family/support persons.
7. Complete a Safety Planning Intervention (Stanley-Brown) if disposition is outpatient.

## Differential Diagnosis

Organic causes of suicidal ideation/altered behavior to rule out:

- **Intoxication/withdrawal:** Alcohol, benzodiazepines, stimulants, opioids (obtain toxicology screen, BAL)
- **Hypoglycemia:** Check point-of-care glucose
- **Thyroid storm/myxedema:** TSH if clinical suspicion
- **Delirium:** Infection, metabolic derangement, medication side effects (anticholinergic toxicity, corticosteroids)
- **CNS lesion:** New-onset psychiatric symptoms in absence of psychiatric history warrant CT head
- **Medication-induced suicidality:** SSRIs (black box warning in <25 years), isotretinoin, corticosteroids, interferon-alpha, mefloquine, montelukast
- **Autoimmune encephalitis:** Anti-NMDA receptor encephalitis presents with psychiatric symptoms in young women; dyskinesias and seizures follow

## Workup

Medical clearance workup:

- **Point-of-care glucose:** Mandatory for all psychiatric presentations
- **Urine drug screen:** Amphetamines, benzodiazepines, cannabinoids, cocaine, opioids, PCP
- **Blood alcohol level:** Intoxication complicates assessment; reassess suicidality when sober (BAL < 0.08)
- **Acetaminophen level and salicylate level:** Mandatory after any ingestion or if ingestion cannot be excluded
- **CBC, BMP:** If clinical suspicion for infection, dehydration, metabolic derangement
- **TSH:** If new-onset psychiatric symptoms, first presentation, or clinical suspicion
- **Pregnancy test (urine hCG):** Reproductive-age patients; perinatal mood disorders
- **ECG:** If tricyclic antidepressant or other cardiotoxic ingestion suspected
- **CT head without contrast:** New-onset psychiatric symptoms without psychiatric history, focal neurological deficits, or age > 50 with first presentation
- **Toxicology labs as indicated:** Lithium level, specific drug levels based on ingestion history

### Assessment During Intoxication
A patient who is intoxicated and endorsing suicidal ideation requires:
1. Medical stabilization and treatment of the intoxication
2. 1:1 observation throughout
3. Reassessment of suicidal ideation after sobriety (BAL < 0.08 or clinically sober)
4. Psychiatric evaluation only after medical clearance and sobriety

## Treatment

### Environmental Safety (Immediate)
- Ligature-resistant room (no anchor points above doorknob height)
- Remove all sharps, cords, belts, shoelaces, plastic bags
- 1:1 continuous visual observation (arms-length if high risk)
- Metal detector or wand screening per institutional protocol
- Limit items in room: no glass, no plastic utensils, paper gowns only if elopement risk

### Acute Agitation Management
- **Verbal de-escalation first** (CPI or equivalent technique)
- **Mild-moderate agitation:** Lorazepam 2 mg PO/IM or midazolam 5 mg IM
- **Severe agitation, cooperative:** Olanzapine 10 mg PO (ODT)
- **Severe agitation, uncooperative:** Midazolam 5 mg IM + haloperidol 5 mg IM + diphenhydramine 50 mg IM ("B52" combination: substitute ziprasidone 20 mg IM for haloperidol if preferred)
- **Do NOT combine IM olanzapine and IM benzodiazepines** (risk of respiratory depression and death)
- **Ketamine for refractory agitation with suicidal ideation:** 4 mg/kg IM or 1-2 mg/kg IV over 1-2 minutes. Provides rapid anxiolysis. Emerging evidence for anti-suicidal properties of sub-anesthetic ketamine (0.5 mg/kg IV over 40 minutes), but ED use for this specific indication is not yet standard.

### Safety Planning Intervention (Stanley-Brown Model)
Collaborative, structured plan completed with the patient:
1. Warning signs the patient recognizes before a crisis
2. Internal coping strategies (distraction, self-soothing)
3. People and social settings that provide distraction
4. People the patient can ask for help (with contact info)
5. Professionals/agencies to contact in crisis (Crisis Lifeline 988, Crisis Text Line text HOME to 741741, local crisis team)
6. Making the environment safe (lethal means restriction plan)

### Lethal Means Restriction Counseling
- Firearms: Ask directly about access. Counsel voluntary temporary transfer to a trusted person, gun safe with lock, or law enforcement storage. Access to firearms is the single strongest environmental risk factor for completed suicide.
- Medications: Limit quantities dispensed. Lock up or remove stockpiled medications from the home.
- Other: Bridge barriers, safe storage of ropes/cords, car keys

### Psychiatric Hold (Involuntary Commitment)
Criteria vary by state but generally require:
- Danger to self (imminent risk of suicide)
- Inability or unwillingness to contract for safety (safety contracts have NO evidence and should NOT be relied upon)
- Lack of adequate outpatient safety plan or support

Document: specific statements, behaviors, risk factors, and clinical reasoning supporting the hold.

## Disposition

### Admission Criteria
- C-SSRS level 4-5 (active ideation with intent or plan)
- Recent high-lethality attempt (hanging, firearm, jumping, high-dose ingestion)
- Psychosis with command hallucinations to harm self
- Intoxication with persistent suicidal ideation after sobriety
- Unable to identify reasons for living, no protective factors
- No safe discharge environment (lethal means not removable, no support system)

### Voluntary vs Involuntary Admission
- **Voluntary:** Patient agrees to psychiatric admission. Preferred when possible.
- **Involuntary (psychiatric hold):** When patient refuses admission but meets criteria for imminent danger to self. Duration varies by state (typically 72 hours for initial hold).

### Discharge Criteria (Lower-Risk Patients Only)
- C-SSRS level 1-2 with identified dynamic trigger that has resolved
- No access to lethal means (confirmed with collateral)
- Completed Safety Planning Intervention
- Outpatient follow-up confirmed within 72 hours (reduces reattempt rate by approximately 50%)
- Caring contact (phone call from ED within 24-48 hours)
- Family/support person present at discharge, understands plan
- Patient is sober and medically cleared

### Follow-Up
- Outpatient psychiatric follow-up within 72 hours
- Caring contacts (brief phone/text check-ins from ED at 24h, 48h, 1 week, 1 month)
- Bridge prescription if medication adjustment needed (limit quantity dispensed)
- Provide 988 Suicide and Crisis Lifeline number (call or text 988)

## Pitfalls

1. **Relying on "safety contracts" or "no-suicide contracts."** These have zero evidence for reducing suicide risk. They create false reassurance and are not a substitute for proper risk assessment, Safety Planning Intervention, and disposition.

2. **Discharging an intoxicated patient who denies suicidal ideation.** Alcohol and substances impair judgment and disinhibit. A patient who was suicidal while intoxicated must be reassessed after achieving sobriety. Suicidal ideation while intoxicated predicts future attempts.

3. **Using the SAD PERSONS score as the primary risk stratification tool.** SAD PERSONS has poor sensitivity and specificity. Use the C-SSRS, clinical interview, and assessment of static and dynamic risk factors for disposition decisions.

4. **Failing to ask about firearms.** Access to a firearm increases suicide completion risk 3-fold. Direct, nonjudgmental inquiry about firearm access is mandatory. Counsel on temporary off-site storage.

5. **Skipping medical clearance.** Organic causes of suicidal behavior include hypoglycemia, intoxication, delirium, CNS lesions, and medication side effects. Point-of-care glucose, toxicology screen, and focused medical evaluation are required before attributing symptoms to primary psychiatric illness.

6. **Not checking acetaminophen and salicylate levels after an ingestion.** Co-ingestion is common. Acetaminophen toxicity is clinically silent for 24-48 hours. Order levels on every patient with known or possible ingestion.

7. **Discharging without a Safety Planning Intervention and confirmed follow-up.** The Stanley-Brown Safety Planning Intervention is the only evidence-based brief intervention shown to reduce suicidal behavior post-ED visit. Outpatient follow-up within 72 hours halves reattempt rates. Both are required before discharge.

8. **Leaving the patient unsupervised.** Patients at risk for suicide require 1:1 continuous observation in a safe environment. Bathroom breaks, transport to radiology, and shift changes are high-risk moments for elopement or self-harm.

9. **Anchoring on a psychiatric diagnosis and missing medical pathology.** First-episode psychosis in a patient >40 without psychiatric history warrants neuroimaging. New suicidality with headache warrants CT. Anti-NMDA receptor encephalitis presents with psychiatric symptoms.

10. **Dismissing suicidal ideation in adolescents as "attention-seeking."** Adolescents who express suicidal ideation are at elevated risk for attempt and completion. Every expression of suicidal ideation warrants formal C-SSRS assessment regardless of perceived intent.
