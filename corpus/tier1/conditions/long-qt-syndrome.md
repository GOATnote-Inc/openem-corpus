---
id: long-qt-syndrome
condition: Long QT Syndrome
aliases: [LQTS, prolonged QT, congenital LQTS, acquired long QT, Romano-Ward syndrome]
icd10: [I45.81]
esi: 2
time_to_harm: "< 1 hour if TdP develops"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2017 AHA/ACC/HRS Guideline for Management of Patients With Ventricular Arrhythmias and the Prevention of Sudden Cardiac Death. J Am Coll Cardiol. 2018;72(14):e91-e220."
  - type: review
    ref: "Schwartz PJ, et al. Congenital Long QT Syndrome: A Focus on Risk Stratification and Management. J Am Coll Cardiol Clin Electrophysiol. 2022."
  - type: review
    ref: "Abutaleb ARA, et al. A comprehensive review of long QT syndrome pathogenesis and treatment. Heart Rhythm Open. 2024."
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
# Long QT Syndrome

## Recognition

**ECG findings:**
- Corrected QT interval (QTc) > 470 ms in males, > 480 ms in females (Bazett formula: QTc = QT/√RR)
- QTc > 500 ms = high risk for TdP
- T-wave morphology varies by subtype:
  - LQT1: broad-based T waves
  - LQT2: notched or bifid T waves
  - LQT3: late-onset peaked T waves with long ST segment
- T-wave alternans (beat-to-beat T-wave amplitude variation) — ominous, signals imminent arrhythmia

**Congenital LQTS presentations:**
- Syncope (especially exertional in LQT1, auditory startle in LQT2, sleep/rest in LQT3)
- Seizure-like episodes (misdiagnosed as epilepsy in up to 30%)
- Cardiac arrest/sudden cardiac death — may be first presentation
- Family history of sudden death, drowning, or unexplained syncope in young relatives
- Schwartz score >= 3.5 = high probability of LQTS

**Acquired LQTS — common offenders:**
- Antiarrhythmics: sotalol, dofetilide, procainamide, quinidine
- Antibiotics: fluoroquinolones, macrolides (azithromycin, erythromycin)
- Antipsychotics: haloperidol, droperidol, ziprasidone, quetiapine
- Others: methadone, ondansetron (IV > 16 mg), TCAs, citalopram
- Electrolytes: hypokalemia, hypomagnesemia, hypocalcemia

## Critical Actions

| Action | Target |
|---|---|
| 12-lead ECG with QTc measurement | < 10 minutes |
| Medication reconciliation | Immediate |
| Electrolyte check (K+, Mg2+, Ca2+) | < 15 minutes |
| Discontinue QT-prolonging drugs | Immediate |

1. **Measure QTc on 12-lead ECG** — use Bazett correction; manually calculate if automated measurement unreliable
2. **Discontinue ALL QT-prolonging medications** immediately
3. **Correct electrolytes:** K+ target 4.5-5.0 mEq/L, Mg2+ > 2.0 mg/dL
4. **If QTc > 500 ms:** Admit to telemetry, serial ECG monitoring, hold all QT-prolonging agents
5. **If TdP occurs:** Magnesium sulfate 2 g IV, overdrive pacing — see torsades-de-pointes entry
6. **Congenital LQTS with syncope:** Beta-blocker initiation (nadolol 1 mg/kg/day PO or propranolol 2-3 mg/kg/day PO divided), avoid IV beta-blockers acutely unless under EP guidance
7. **Restrict activity** — no competitive sports (especially swimming for LQT1) until EP evaluation

## Differential Diagnosis

- Epilepsy — syncope from LQTS misdiagnosed as seizure in up to 30% of congenital LQTS patients
- Vasovagal syncope — lack of prodrome and exertional trigger suggests cardiac etiology
- Brugada syndrome — ST elevation in V1-V3, different ECG pattern
- Short QT syndrome — QTc < 340 ms with arrhythmia risk
- Catecholaminergic polymorphic VT (CPVT) — normal QTc, exercise-induced bidirectional VT
- Hypertrophic cardiomyopathy — syncope with exertion, but has LVH on ECG/echo

## Workup

- **12-lead ECG:** QTc measurement, T-wave morphology analysis
- **Serial ECGs:** If QTc borderline, exercise can unmask LQTS (QT fails to shorten appropriately)
- **Electrolytes:** K+, Mg2+, Ca2+, phosphorus — STAT
- **Complete medication review:** Check all current medications against QT-prolonging drug lists
- **Troponin:** If acute presentation with chest pain or hemodynamic compromise
- **TSH:** Hypothyroidism prolongs QT
- **Echocardiography:** Rule out structural heart disease
- **Genetic testing:** Referral for congenital LQTS (identifies subtype in ~75% of clinically diagnosed cases)
- **Family screening:** ECG of first-degree relatives if congenital LQTS suspected

## Treatment

### Acquired LQTS
- Remove offending agent(s)
- Correct K+ to 4.5-5.0 mEq/L (KCl 10-20 mEq/hr IV)
- Magnesium sulfate 2 g IV empirically, then recheck level
- Telemetry monitoring until QTc normalizes
- If TdP occurs: magnesium, overdrive pacing, isoproterenol 2-10 mcg/min IV

### Congenital LQTS — Acute Management
- Magnesium sulfate 2 g IV for active TdP
- Beta-blocker: nadolol 1 mg/kg/day PO (preferred long-term); propranolol 2-3 mg/kg/day PO divided (alternative)
- AVOID isoproterenol (can worsen congenital LQTS)
- For TdP storm: lidocaine 1-1.5 mg/kg IV bolus, then 1-4 mg/min infusion; overdrive pacing at 90-110 bpm
- Temporary pacing for bradycardia-triggered TdP (especially LQT3)

### Congenital LQTS — Subtype-Specific Considerations
- **LQT1:** Triggers = exertion (especially swimming). Beta-blockers highly effective. Avoid competitive sports.
- **LQT2:** Triggers = auditory stimuli, emotional stress. Beta-blockers effective. Maintain K+ > 4.0 mEq/L.
- **LQT3:** Triggers = rest/sleep. Beta-blockers less effective. Mexiletine 200 mg PO TID may shorten QT. ICD threshold lower.

### ICD Indications (per EP consultation)
- Cardiac arrest survivor
- Syncope despite beta-blocker therapy
- QTc > 550 ms (especially LQT2, LQT3)
- Family history of sudden cardiac death in LQTS

## Disposition

- **ICU admission:** Active TdP, QTc > 550 ms with symptoms, cardiac arrest survivor
- **Telemetry admission:** QTc > 500 ms, newly diagnosed congenital LQTS, symptomatic acquired LQTS
- **Discharge with urgent follow-up:** QTc 470-500 ms from reversible drug cause (after drug discontinued and QTc trending down), asymptomatic known LQTS on beta-blocker with stable QTc
- **EP referral:** All congenital LQTS (even asymptomatic), recurrent acquired LQTS, any patient with family history of sudden cardiac death

## Pitfalls

1. **Dismissing syncope as "vasovagal" in a young patient without checking QTc.** Congenital LQTS causes syncope in young, otherwise healthy patients. A 12-lead ECG with QTc measurement should be obtained in every young syncope patient, especially with exertional or auditory triggers.

2. **Using automated QTc measurements without verification.** Automated ECG algorithms frequently miscalculate QTc, especially with U waves, artifact, or tachycardia. Manual QT measurement from lead II or V5-V6 (longest QT) with Bazett correction is essential for clinical decisions.

3. **Prescribing QT-prolonging drugs without baseline ECG.** Many common medications (antibiotics, antiemetics, psychiatric drugs) prolong QT. Baseline and follow-up ECGs should be obtained, particularly when combining multiple QT-prolonging agents.

4. **Misdiagnosing LQTS-related syncope as epilepsy.** Up to 30% of congenital LQTS patients are initially misdiagnosed with epilepsy. Tonic-clonic movements from cerebral hypoperfusion during TdP mimic seizures. Any "seizure" patient with a normal neurologic workup needs an ECG.

5. **Failing to screen family members.** Congenital LQTS is autosomal dominant. First-degree relatives have a 50% chance of carrying the mutation. A single case should trigger family screening with ECGs and genetic counseling referral.
