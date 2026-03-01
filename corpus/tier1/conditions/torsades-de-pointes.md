---
id: torsades-de-pointes
condition: Torsades de Pointes
aliases: [TdP, polymorphic VT with prolonged QT, twisting of the points]
icd10: [I47.20, I47.21]
esi: 1
time_to_harm:
  irreversible_injury: "< 5 minutes"
  death: "< 10 minutes"
  optimal_intervention_window: "< 2 minutes"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2020 AHA/ACC Guideline for Management of Patients With Ventricular Arrhythmias and the Prevention of Sudden Cardiac Death. Circulation. 2018;138(13):e272-e391."
  - type: review
    ref: "Drew BJ, et al. Prevention of Torsade de Pointes in Hospital Settings: A Scientific Statement From the AHA. Circulation. 2010;121(8):1047-1060."
  - type: pubmed
    ref: "Tzivoni D, et al. Treatment of Torsade de Pointes With Magnesium Sulfate. Circulation. 1988;77(2):392-397."
  - type: review
    ref: "Nachimuthu S, et al. Drug-induced QT interval prolongation: mechanisms and clinical management. Ther Adv Drug Saf. 2012;3(5):241-253."
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
# Torsades de Pointes

## Recognition

**ECG hallmarks:**
- Polymorphic ventricular tachycardia with characteristic "twisting" of QRS axis around the baseline
- Preceded by prolonged QTc interval (> 500 ms significantly increases risk)
- "Short-long-short" initiation sequence: PVC → compensatory pause → another PVC triggering the run
- Rate 150-300 bpm
- Typically self-terminating but may degenerate to ventricular fibrillation

**Distinguishing from polymorphic VT without QT prolongation:**
- TdP = polymorphic VT + prolonged QT interval
- Polymorphic VT with normal QT = treat as ischemic VT (different management)

**Common causes — acquired (> 90%):**
- QT-prolonging drugs: antiarrhythmics (sotalol, dofetilide, procainamide, amiodarone), antibiotics (fluoroquinolones, macrolides), antipsychotics (haloperidol, droperidol, ziprasidone), methadone, ondansetron (high dose)
- Electrolyte derangements: hypokalemia, hypomagnesemia, hypocalcemia
- Bradycardia (increases QT duration)
- Structural heart disease, intracranial pathology, hypothermia

**Congenital long QT syndrome (< 10%):**
- LQT1 (KCNQ1), LQT2 (KCNH2), LQT3 (SCN5A) most common subtypes
- Family history of sudden cardiac death, recurrent syncope with exertion or emotional stress

## Critical Actions

| Action | Target |
|---|---|
| Defibrillation if pulseless | Immediate |
| IV magnesium | < 2 minutes |
| QTc assessment on baseline ECG | Immediate |
| Correct K+ to > 4.0 mEq/L | < 30 minutes |

1. **Pulseless TdP:** Unsynchronized defibrillation 200 J biphasic. Follow ACLS pulseless VT/VF protocol.
2. **Magnesium sulfate 2 g IV over 2-5 minutes** — FIRST-LINE regardless of serum Mg level. Follow with infusion 1-4 g/hr to maintain Mg > 2 mmol/L. Effective even with normal serum magnesium.
3. **Correct hypokalemia aggressively** — target K+ 4.5-5.0 mEq/L. KCl 10-20 mEq/hr IV via central line (max 40 mEq/hr in extremis).
4. **Increase heart rate** to shorten QT interval:
   - Overdrive pacing (transvenous preferred, rate 90-110 bpm) — most effective
   - Isoproterenol 2-10 mcg/min IV titrated to HR 90-110 bpm (ACQUIRED long QT ONLY — CONTRAINDICATED in congenital LQTS)
5. **Discontinue ALL QT-prolonging medications** immediately
6. **Lidocaine 1-1.5 mg/kg IV bolus** then 1-4 mg/min infusion — shortens QT and suppresses PVCs (safe in both acquired and congenital LQTS)

## Differential Diagnosis

- **Polymorphic VT without QT prolongation** — usually ischemic etiology; treat with amiodarone and revascularization (NOT magnesium as primary therapy)
- **Ventricular fibrillation** — no organized QRS morphology; defibrillate regardless
- **Monomorphic VT** — constant QRS morphology; different management (amiodarone, procainamide)
- **SVT with aberrancy** — regular narrow-complex origin with bundle branch block
- **Artifact** — patient movement can mimic polymorphic wide complex rhythm

## Workup

- **12-lead ECG:** Measure QTc (Bazett correction: QTc = QT/√RR). QTc > 500 ms = high risk. Review for congenital vs acquired pattern.
- **Electrolytes:** STAT K+, Mg2+, Ca2+, phosphorus
- **Medication review:** Identify ALL QT-prolonging agents (check CredibleMeds.org database)
- **Troponin:** Rule out ischemia as cause of polymorphic VT
- **TSH:** Hypothyroidism can prolong QT
- **Continuous telemetry with QTc monitoring**
- **Family history:** Sudden cardiac death, recurrent syncope, known LQTS — suggests congenital

## Treatment

### Acute Episode
- Magnesium sulfate 2 g IV over 2-5 min, then 1-4 g/hr infusion
- KCl replacement to target K+ 4.5-5.0 mEq/L
- Overdrive pacing at 90-110 bpm (most effective for recurrent episodes)
- Isoproterenol 2-10 mcg/min IV (acquired LQTS only)
- Lidocaine 1-1.5 mg/kg IV bolus, then 1-4 mg/min infusion

### AVOID
- Amiodarone (prolongs QT — will worsen TdP)
- Procainamide (prolongs QT)
- Sotalol (prolongs QT)
- Class IA and class III antiarrhythmics in general
- Isoproterenol in congenital LQTS (may paradoxically worsen)

### Congenital Long QT Syndrome (Acute)
- Magnesium sulfate 2 g IV
- Overdrive pacing or IV beta-blocker (esmolol 500 mcg/kg IV bolus then 50-200 mcg/kg/min) — beta-blockers are protective in congenital LQTS (opposite of acquired)
- Lidocaine 1-1.5 mg/kg IV for breakthrough arrhythmia
- Long-term: nadolol, ICD placement per EP consultation

### Post-Resuscitation
- Continuous Mg infusion for 24-48 hours
- Serial QTc monitoring q4-6h
- Hold all QT-prolonging meds until QTc normalizes
- Genetic testing referral if congenital LQTS suspected

## Disposition

- **ICU admission:** All patients with TdP episodes, patients requiring temporary pacing or isoproterenol infusion
- **Telemetry with continuous QTc monitoring:** Patients with QTc > 500 ms on QT-prolonging drugs (even without TdP episode)
- **Transfer criteria:** Facilities without temporary pacing or EP consultation capability
- **Never discharge:** Any patient with documented TdP, regardless of current rhythm stability

## Pitfalls

1. **Treating TdP with amiodarone.** Amiodarone prolongs the QT interval and worsens TdP. This is the opposite of its role in monomorphic VT/VF. Magnesium and overdrive pacing are the correct treatments. This error occurs when the rhythm is misclassified as "VT" without checking the QT interval.

2. **Giving isoproterenol to a patient with congenital LQTS.** Isoproterenol increases heart rate (beneficial in acquired LQTS) but can paradoxically lengthen QT and trigger arrhythmias in congenital LQTS, particularly LQT1 and LQT2. Use beta-blockers instead for congenital LQTS.

3. **Failing to check the QT interval on the baseline ECG before treating polymorphic VT.** Polymorphic VT with a normal QT is an entirely different entity (usually ischemic) requiring amiodarone and revascularization. TdP (polymorphic VT + prolonged QT) requires magnesium and overdrive pacing. The QT interval determines the treatment algorithm.

4. **Not correcting electrolytes aggressively enough.** Standard K+ replacement (10 mEq/hr) is inadequate for active TdP. Push K+ at 20-40 mEq/hr via central line, and give magnesium empirically regardless of level. Recurrent TdP in the setting of uncorrected hypokalemia is refractory to all other therapies.

5. **Failing to identify the offending medication.** Multiple common medications prolong QT, including drugs patients may have started recently (antibiotics, antiemetics, psychiatric medications). A thorough medication reconciliation is essential, and ALL QT-prolonging agents must be stopped.
