---
id: benign-palpitations
condition: Benign Palpitations
aliases: [palpitations, premature atrial contractions, PACs, premature ventricular contractions, PVCs, benign ectopy, functional palpitations]
icd10: [R00.2, I49.1, I49.3, I49.40, I49.49]
esi: 4
time_to_harm: "N/A — benign in structurally normal heart; see escalation_triggers for emergency differential"
category: cardiovascular
track: tier1
disposition_default: outpatient
escalation_triggers:
  - "Palpitations with syncope or presyncope — high-risk arrhythmia until proven otherwise"
  - "Palpitations with chest pain and diaphoresis — ACS"
  - "Palpitations with dyspnea and SpO2 <95% — PE, heart failure, or respiratory cause"
  - "Hemodynamic instability: hypotension, altered mental status"
  - "Wide-complex tachycardia on ECG — ventricular tachycardia until proven otherwise"
  - "QTc prolongation >500 ms — torsades de pointes risk"
  - "Delta waves (Wolff-Parkinson-White pattern) on ECG — accessory pathway, risk of pre-excited atrial fibrillation"
  - "Known structural heart disease (prior MI, cardiomyopathy, CHF, HCM) with new palpitations"
  - "Family history of sudden cardiac death or inherited arrhythmia syndrome (Long QT, Brugada, ARVC)"
  - "HR >150 bpm on ECG or monitor during symptoms — SVT or atrial flutter"
confusion_pairs:
  - condition: ventricular-tachycardia
    differentiators:
      - "Benign PVCs: isolated or in bigeminy; narrow complex (if retrograde) or LBBB/RBBB morphology with compensatory pause; returns to baseline sinus rhythm between beats"
      - "VT: sustained wide-complex tachycardia (≥3 beats at >100 bpm); hemodynamic compromise possible; AV dissociation, fusion beats, or capture beats on ECG"
      - "Benign ectopy: no structural heart disease, normal QT, normal ECG at baseline"
      - "VT: prior MI, cardiomyopathy, or other structural disease is the strongest predictor; absence of structural disease significantly reduces VT risk"
  - condition: svt
    differentiators:
      - "Benign palpitations/PACs: isolated skipped beats, brief flutter, non-sustained; sinus rhythm with ectopy on ECG"
      - "SVT: sustained narrow-complex tachycardia with HR 150-250 bpm; abrupt onset/offset; may require vagal maneuvers or adenosine"
      - "ECG during symptoms is the critical differentiator; ambulatory monitoring if symptoms are paroxysmal"
sources:
  - type: pubmed
    ref: "Raviele A, Giada F, Bergfeldt L, et al. Management of patients with palpitations: a position paper from the European Heart Rhythm Association. Europace. 2011;13(7):920-934."
    pmid: "21697315"
  - type: review
    ref: "Abbott AV. Diagnostic approach to palpitations. Am Fam Physician. 2005;71(4):743-750."
    pmid: "15742913"
  - type: pubmed
    ref: "Zimetbaum P, Josephson ME. Evaluation of patients with palpitations. N Engl J Med. 1998;338(19):1369-1373."
    pmid: "9571258"
  - type: pubmed
    ref: "Krahn AD, Klein GJ, Yee R, Takle-Newhouse T, Norris C. Use of an extended monitoring strategy in patients with problematic syncope. REVEAL Investigators. Circulation. 1999;99(3):406-410."
    pmid: "9918528"
  - type: review
    ref: "Thavendiranathan P, Bagai A, Khoo C, Dorian P, Bhatt DL. Does this patient with palpitations have a cardiac arrhythmia? JAMA. 2009;301(19):2020-2026."
    pmid: "19454641"
last_updated: "2026-02-23"
compiled_by: agent
risk_tier: C
validation:
  schema_version: "2.0"
  automated_consistency_check: "2026-02-27"
  dose_range_validator: "2026-02-27"
  unit_normalization_check: "2026-02-27"
  cross_file_consistency_check: "2026-02-27"
  citation_presence_check: "2026-02-27"
  duplicate_content_check: "2026-02-27"
  outlier_detection_flag: clear
  guideline_version_reference: "EHRA Position Paper 2011 (referenced); JAMA Rational Clinical Examination 2009"
  provenance_links: []
---

## Recognition

Palpitations — the subjective awareness of heartbeat — account for approximately 16% of primary care visits and a significant proportion of ED visits. The majority of palpitations arise from benign causes: premature atrial contractions (PACs), premature ventricular contractions (PVCs), anxiety, caffeine, or sinus tachycardia. The key emergency task is identifying the minority with life-threatening arrhythmia using a structured risk-stratification approach.

### Common Benign Causes of Palpitations
- **PACs (premature atrial contractions)**: most common; often described as a "skipped beat" or "flip-flop" — the pause after the ectopic beat and the strong compensatory sinus beat are what patients feel
- **PVCs (premature ventricular contractions)**: similar sensation; uniform PVCs in structurally normal heart are benign; LBBB or RBBB morphology on ECG; compensatory pause; suppressed by exercise (distinguishes from exercise-induced arrhythmia)
- **Sinus tachycardia**: anxiety, dehydration, caffeine, fever, anemia, thyrotoxicosis, stimulant use
- **Anxiety/panic-related**: palpitations plus hyperventilation, chest tightness, paresthesias
- **Alcohol, caffeine, or stimulant use**: common, dose-dependent, resolves with cessation

### Clinical History Features That Stratify Risk
High-yield questions:
- **Onset/offset**: abrupt onset and offset = arrhythmia (SVT, AF); gradual = sinus tachycardia or ectopy
- **Associated symptoms**: syncope or presyncope with palpitations = high-risk (admission); dyspnea alone = intermediate
- **Circumstances**: during exercise (concern for exercise-induced VT or HCM); at rest; with position change (common for AVRT)
- **Structural heart disease**: prior MI, known cardiomyopathy, HF — single strongest predictor of arrhythmia
- **Family history**: sudden cardiac death, inherited channelopathy (Long QT, Brugada)
- **Medications and substances**: QT-prolonging drugs, stimulants, cocaine, amphetamines, thyroid medication

### High-Risk vs. Low-Risk Features

| Feature | Low-Risk (Likely Benign) | High-Risk (Arrhythmia Concern) |
|---------|--------------------------|-------------------------------|
| Associated symptoms | None or anxiety | Syncope, presyncope, chest pain, dyspnea |
| Duration | Brief, seconds | Sustained, minutes |
| Onset/offset | Gradual | Abrupt |
| During exercise | No | Yes |
| Structural heart disease | No | Yes |
| Family history sudden death | No | Yes |
| ECG | Normal | WPW, QTc >500ms, delta waves, BBB |

## Critical Actions

1. Obtain 12-lead ECG within the first 10 minutes of ED arrival — cardiac rhythm during or immediately after symptoms is the highest-yield diagnostic test. Standard ECG identifies the cause in approximately 40% of palpitation presentations.
2. Attach continuous cardiac monitor with rhythm strip documentation if symptoms are ongoing or recurrent.
3. Apply structured risk stratification: if syncope with palpitations — high risk, admit; if palpitations alone with normal ECG and no structural disease — low risk, discharge with ambulatory monitoring.
4. Check medications list for QT-prolonging agents (antipsychotics, fluoroquinolones, macrolides, antiarrhythmics, methadone).
5. For palpitations that have resolved at presentation: if ECG is normal and structural heart disease is absent, arrange outpatient ambulatory ECG monitoring (event monitor or Holter).

## When NOT to Escalate

Benign palpitations are appropriate for outpatient management when ALL of the following are met:
- Symptoms have resolved at time of evaluation
- 12-lead ECG shows normal sinus rhythm (or isolated ectopy with RBBB/LBBB morphology without delta waves)
- No syncope or presyncope
- No hemodynamic instability
- No significant structural heart disease (no prior MI, cardiomyopathy, CHF, or congenital heart disease)
- QTc <500 ms
- No delta waves (WPW pattern) on ECG
- No family history of sudden cardiac death or inherited channelopathy
- Benign precipitant identifiable (caffeine, anxiety, dehydration, stimulant, fever)

Admission and telemetry are NOT required for: isolated PACs or PVCs in a structurally normal heart, sinus tachycardia with identifiable cause, or resolved palpitations with a normal ECG and low-risk history.

## Differential Diagnosis

| Condition | ECG Finding | Hemodynamics | Structural Disease Required? |
|-----------|------------|-------------|------------------------------|
| **PACs (benign)** | Premature P wave with narrow QRS, compensatory pause | Normal | No |
| **PVCs (benign)** | Wide complex (LBBB or RBBB morphology), no P wave, compensatory pause, suppressed by exercise | Normal | No |
| **Sinus tachycardia** | Rate 100-160, normal P-QRS-T morphology | Normal | No |
| **AVNRT (common SVT)** | Narrow complex, HR 150-250, P wave buried in or after QRS | Usually stable | No |
| **Atrial flutter** | Sawtooth baseline at 300 bpm, 2:1 or variable block, HR 150 bpm typical with 2:1 block | Usually stable | Often present |
| **Atrial fibrillation** | Irregularly irregular rhythm, no P waves, fibrillatory baseline | Variable | Often present |
| **VT (monomorphic)** | Wide complex at >100 bpm, AV dissociation, fusion/capture beats | Variable — can cause hemodynamic collapse | Usually prior MI or cardiomyopathy |
| **Torsades de pointes** | Polymorphic VT, twisting QRS axis around isoelectric line; QTc >500 ms at baseline | Unstable — degenerates to VF | QT-prolonging cause |
| **WPW with pre-excited AF** | Irregular wide complex tachycardia (delta waves at baseline); very rapid rate | Potentially unstable | Accessory pathway (congenital) |

## Workup

### All Palpitations — Required
- **12-lead ECG** (obtain during symptoms if possible; otherwise immediately on arrival): rate, rhythm, QTc, delta waves, ischemic changes, bundle branch block
- **SpO2** by pulse oximetry
- **Fingerstick glucose**: exclude hypoglycemia

### Targeted Labs (Based on Clinical Context)
- **TSH**: if symptoms suggest hyperthyroidism (tremor, weight loss, heat intolerance, heat flush) — thyroid disease causes sinus tachycardia and atrial fibrillation
- **CBC**: if anemia suspected (pallor, fatigue, dyspnea on exertion)
- **BMP/electrolytes**: hypokalemia and hypomagnesemia increase ectopy and arrhythmia risk; QTc prolongation worsens with electrolyte abnormalities
- **Troponin**: if chest pain with ACS features accompanies palpitations
- **Urine drug screen**: if stimulant use suspected (cocaine, amphetamines)

### When to Order Echocardiogram
- Suspected structural heart disease (new murmur, cardiomegaly on CXR, family history HCM, or prior MI)
- Exercise-induced palpitations or syncope
- Multiple PVCs (>10-15% of beats on Holter) — dilated cardiomyopathy from PVC burden
- NOT required for typical low-risk palpitations with normal ECG

### Ambulatory Monitoring (Outpatient Arrangement)
- **Holter monitor (24-48 hours)**: daily or near-daily symptoms — highest yield for frequent symptoms
- **Event monitor / patch monitor (2-4 weeks)**: symptoms occurring less frequently than daily; preferred for most outpatient palpitation workup
- **Implantable loop recorder**: recurrent unexplained palpitations or syncope where other monitoring has been non-diagnostic and clinical suspicion for arrhythmia is high

## Treatment

### Benign Ectopy (PACs, PVCs — Structurally Normal Heart)
- **Reassurance**: the primary treatment. Explain the benign nature, the physiological mechanism (ectopic depolarization), and that isolated ectopy in a structurally normal heart does not increase mortality.
- **Trigger reduction**: reduce caffeine, alcohol, stimulants; treat underlying anxiety, improve sleep hygiene
- **No antiarrhythmic medications required** for benign ectopy — antiarrhythmics carry proarrhythmic risk that outweighs benefit in structurally normal heart

### Symptomatic Benign PVCs Causing Functional Impairment
- **Beta-blockers** (metoprolol succinate 25-50 mg PO daily or atenolol 25-50 mg PO daily): reduces PVC burden; symptom relief in 50-60% of patients; first-line if pharmacotherapy is required
- **Calcium channel blockers** (verapamil 120-240 mg/day PO divided): alternative for beta-blocker-intolerant patients
- **Flecainide or propafenone**: effective for refractory PVCs in structurally normal heart; requires cardiology supervision; avoid in structural heart disease
- **Catheter ablation**: for highly symptomatic, refractory PAC or PVC burden (>10-15% of beats) causing functional impairment or PVC-induced cardiomyopathy — outpatient cardiology referral

### Electrolyte Replacement (When Deficient)
- Potassium: correct hypokalemia to K+ >4.0 mEq/L to reduce ectopy (oral KCl preferred unless symptomatic or severe — IV KCl 20-40 mEq/hour in monitored setting)
- Magnesium: correct hypomagnesemia (magnesium sulfate 1-2 g IV over 10-20 minutes, or oral magnesium oxide 400-800 mg/day)

### Anxiety-Related Palpitations
- Treat underlying anxiety (CBT referral, SSRI if panic disorder present — see panic-attack.md)
- Avoid benzodiazepines as primary long-term treatment

## Disposition

### Discharge (Standard)
- Low-risk palpitations (criteria met above) with normal ECG, no syncope, no structural disease: discharge with outpatient Holter or event monitor arranged within 1-2 weeks
- Provide return precautions: return immediately for syncope, chest pain, dyspnea, or sustained palpitations >30 minutes
- PCP or cardiology follow-up for monitoring results

### Admit / Telemetry
- Syncope or presyncope associated with palpitations
- Wide-complex tachycardia (treat as VT until proven otherwise)
- QTc >500 ms or newly identified QT-prolonging drug requiring cardiac monitoring
- WPW pattern on ECG (electrophysiology referral)
- Hemodynamic instability
- Known structural heart disease with new palpitations

## Pitfalls

1. **Under-escalation: discharging a patient with wide-complex tachycardia labeled as "SVT with aberrancy."** Wide-complex tachycardia is VT until proven otherwise. Only electrophysiologists and experienced clinicians using validated algorithms (Brugada, Vereckei, Basel) should differentiate VT from SVT with aberrancy. In the undifferentiated ED patient with wide-complex tachycardia, treat as VT. Administering adenosine, verapamil, or diltiazem to VT can cause hemodynamic collapse and death.

2. **Over-escalation: admitting low-risk palpitations with normal ECG for telemetry monitoring.** Hospitalization and prolonged telemetry monitoring for low-risk palpitations (no syncope, no structural disease, normal ECG, resolved symptoms) does not improve outcomes compared to outpatient ambulatory monitoring, and exposes patients to hospital-acquired complications. Ambulatory monitoring is more likely to capture symptoms that occur in the patient's natural environment.

3. **Failing to check QTc and the medication list.** Drug-induced long QT is one of the most preventable causes of sudden cardiac death. Common culprits: antipsychotics (haloperidol, droperidol, quetiapine), fluoroquinolones (ciprofloxacin, levofloxacin), macrolides (azithromycin), antifungals, methadone, sotalol, amiodarone, tricyclic antidepressants. Any QTc >500 ms requires immediate medication reconciliation and electrophysiology consultation.

4. **Missing WPW on the ECG.** Wolff-Parkinson-White (delta waves: slurred QRS upstroke, short PR interval, wide QRS) must be identified at every ECG review. Pre-excited atrial fibrillation in WPW can conduct at extremely rapid rates (>300 bpm) through the accessory pathway, causing VF and sudden death. WPW with palpitations requires electrophysiology referral for ablation discussion — not routine discharge.

5. **Anchoring on benign diagnosis in the presence of structural heart disease.** The most important determinant of arrhythmia risk in palpitations is the presence of structural heart disease (prior MI, cardiomyopathy, CHF, HCM, congenital). A PVC that is benign in a 25-year-old with a structurally normal heart is potentially a VT trigger in a 55-year-old with a prior inferior MI and ejection fraction 35%. The structural heart disease history transforms the risk category.

6. **Reassuring without obtaining an ECG.** Physical examination cannot diagnose cardiac arrhythmia. A normal heart rate and rhythm auscultated in the ED after symptoms have resolved provides no information about the arrhythmia that caused symptoms. ECG is mandatory. If the patient presents symptom-free and the ECG is normal, the next step is ambulatory monitoring — not discharge with "cardiac monitoring normal."
