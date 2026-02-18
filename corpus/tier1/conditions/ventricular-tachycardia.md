---
id: ventricular-tachycardia
condition: Ventricular Tachycardia
aliases: [VT, V-tach, ventricular tach, wide complex tachycardia, WCT, monomorphic VT, polymorphic VT, pulseless VT]
icd10: [I47.2, I47.20, I47.21, I47.29, I49.01]
esi: 1
time_to_harm: "< 5 minutes"
mortality_if_delayed: "Pulseless VT degenerates to VF and death within minutes without defibrillation"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2020 AHA Guidelines for CPR and Emergency Cardiovascular Care — Part 7: Adult Advanced Cardiovascular Life Support"
    doi: "10.1161/CIR.0000000000000916"
  - type: guideline
    ref: "2017 AHA/ACC/HRS Guideline for Management of Patients with Ventricular Arrhythmias and the Prevention of Sudden Cardiac Death"
    doi: "10.1161/CIR.0000000000000549"
  - type: pubmed
    ref: "Brugada P, et al. A New Approach to the Differential Diagnosis of a Regular Tachycardia with a Wide QRS Complex. Circulation. 1991"
    pmid: "2022022"
  - type: pubmed
    ref: "Vereckei A, et al. New Algorithm Using Only Lead aVR for Differential Diagnosis of Wide QRS Complex Tachycardia. Heart Rhythm. 2008"
    pmid: "18180024"
    doi: "10.1016/j.hrthm.2007.09.020"
  - type: guideline
    ref: "2015 ESC Guidelines for the Management of Patients with Ventricular Arrhythmias and the Prevention of Sudden Cardiac Death"
    doi: "10.1093/eurheartj/ehv316"
  - type: pubmed
    ref: "Ortiz M, et al. Randomized Comparison of Intravenous Procainamide vs Amiodarone for the Acute Treatment of Tolerated Wide QRS Tachycardia (PROCAMIO Trial). Eur Heart J. 2017"
    pmid: "27354046"
    doi: "10.1093/eurheartj/ehw230"
last_updated: "2026-02-18"
compiled_by: agent
reviewed_by: null
---

# Ventricular Tachycardia

## Recognition

**Definition:** >= 3 consecutive ventricular beats at rate > 100 bpm (typically 140-280 bpm)
- **Non-sustained VT (NSVT):** < 30 seconds, terminates spontaneously
- **Sustained VT:** >= 30 seconds or requires intervention due to hemodynamic collapse
- **Monomorphic VT:** uniform QRS morphology — typically from a single re-entrant circuit (structural heart disease, prior MI, cardiomyopathy)
- **Polymorphic VT:** varying QRS morphology beat-to-beat — ischemia, electrolyte derangement, or channelopathy

**ECG characteristics of VT (wide complex tachycardia):**
- QRS duration > 120 ms (usually > 140 ms)
- Rate usually 140-280 bpm, regular (monomorphic) or irregular (polymorphic)
- AV dissociation (independent P waves — pathognomonic if present)
- Fusion beats and capture beats (highly specific for VT)
- Concordance (all precordial leads positive or all negative)
- Northwest axis (extreme axis deviation)
- Absence of RS complex in any precordial lead

**Brugada criteria for VT vs SVT with aberrancy (apply sequentially — if any step is YES, diagnose VT):**
1. Absence of RS complex in all precordial leads? -> VT
2. R-to-S interval > 100 ms in any precordial lead? -> VT
3. AV dissociation present? -> VT
4. Morphology criteria in V1 and V6 not consistent with RBBB or LBBB aberrancy? -> VT
- Sensitivity 98.7%, specificity 96.5% for VT diagnosis

**Vereckei aVR algorithm (simpler alternative):**
1. Initial R wave in aVR? -> VT
2. Initial r or q > 40 ms in aVR? -> VT
3. Notch on descending limb of predominantly negative QRS in aVR? -> VT
4. Vi/Vt ratio <= 1 in aVR? -> VT

**Key principle:** In wide complex tachycardia, VT is the diagnosis until proven otherwise. In patients with structural heart disease, WCT is VT > 80% of the time. Treating VT as SVT (e.g., with verapamil) causes cardiovascular collapse and death.

**Torsades de pointes (TdP):**
- Polymorphic VT in the setting of prolonged QT interval (QTc > 500 ms)
- "Twisting of the points" — sinusoidal waveform of increasing then decreasing QRS amplitude
- Causes: drugs (antiarrhythmics [sotalol, procainamide, amiodarone], antibiotics [fluoroquinolones, azithromycin, methadone], antipsychotics, antiemetics), hypokalemia, hypomagnesemia, congenital long QT syndromes

## Critical Actions

| Action | Target |
|---|---|
| Pulse check | Immediate (within 10 seconds) |
| Defibrillation (pulseless VT) | < 2 minutes |
| Synchronized cardioversion (unstable VT with pulse) | < 5 minutes |
| 12-lead ECG (stable VT with pulse) | Immediate |

**Pulseless VT:**
1. Defibrillate immediately: biphasic 120-200 J (use 200 J if device-specific dose unknown)
2. Resume CPR for 2 minutes
3. Epinephrine 1 mg IV/IO after second shock, repeat q3-5min
4. Amiodarone 300 mg IV/IO bolus after third shock; second dose 150 mg IV/IO
5. Repeat defibrillation at maximum energy between each cycle
6. Lidocaine alternative: 1-1.5 mg/kg IV first dose, then 0.5-0.75 mg/kg q5-10min (max 3 mg/kg)
7. Identify and treat reversible causes (ischemia, electrolytes, toxins)

**Unstable VT with pulse (hypotension, altered mental status, ischemic chest pain, acute heart failure):**
1. Synchronized cardioversion: start at 100 J biphasic, escalate to 200 J, then 300 J, then 360 J if unsuccessful
2. Sedation if patient is conscious: midazolam 2-5 mg IV or etomidate 0.2-0.3 mg/kg IV or ketamine 1-2 mg/kg IV
3. If cardioversion fails: amiodarone 150 mg IV over 10 minutes, then repeat cardioversion

**Stable VT with pulse (monomorphic):**
1. 12-lead ECG
2. Procainamide 20-50 mg/min IV infusion until: arrhythmia terminates, hypotension, QRS widens > 50%, or total dose 17 mg/kg reached; then maintenance 1-4 mg/min
   - PROCAMIO trial showed procainamide superior to amiodarone for stable monomorphic VT termination
3. Amiodarone 150 mg IV over 10 minutes; may repeat 150 mg x1; then 1 mg/min infusion x6 hours, then 0.5 mg/min x18 hours (max 2.2 g/24 hours)
4. Lidocaine 1-1.5 mg/kg IV bolus, then 0.5-0.75 mg/kg q5-10min (max 3 mg/kg); maintenance 1-4 mg/min
5. Elective synchronized cardioversion if pharmacologic therapy fails

## Differential Diagnosis

**Wide complex tachycardia differential:**
- Ventricular tachycardia (most common cause — assume until proven otherwise)
- SVT with aberrant conduction (pre-existing or rate-related bundle branch block)
- SVT with pre-excitation (WPW with antidromic conduction)
- Hyperkalemia with sinus tachycardia (widened QRS mimicking VT)
- Sodium channel blocker toxicity (TCA, flecainide, propafenone)
- Ventricular paced rhythm with underlying SVT
- Artifact (movement, shivering, electrical interference)

**Polymorphic VT differential:**
- Torsades de pointes (prolonged QT)
- Polymorphic VT with normal QT (acute ischemia until proven otherwise)
- Catecholaminergic polymorphic VT (exercise-induced, typically young patients)
- Brugada syndrome
- Short QT syndrome

## Workup

- **12-lead ECG:** during tachycardia (capture VT morphology) and after termination (baseline QRS, QT interval, ischemic changes, pre-excitation)
- **Continuous telemetry monitoring**
- **BMP:** K+, Mg2+, Ca2+ (electrolyte-driven arrhythmia), BUN/Cr
- **Troponin:** serial; acute ischemia is the most common trigger for new-onset VT
- **CBC, coagulation studies**
- **TSH** if new-onset arrhythmia without obvious cause
- **Drug levels:** digoxin, antiarrhythmic levels if applicable
- **Toxicology screen** if overdose suspected
- **Point-of-care echocardiography:** LV function, wall motion abnormalities, structural heart disease
- **QTc measurement** on baseline ECG (prolonged QT -> torsades de pointes risk)
- **Chest X-ray:** cardiomegaly, pulmonary edema
- **Formal echocardiography** (inpatient): EF, cardiomyopathy, valvular disease
- **Cardiac catheterization** if ischemia suspected as trigger

## Treatment

### Torsades de Pointes

Treatment differs fundamentally from monomorphic VT:
- **Magnesium sulfate 2 g IV over 2-5 minutes** (first-line regardless of serum Mg level); repeat 2 g IV in 15 minutes if ineffective
- **Isoproterenol 2-10 mcg/min IV infusion** to increase heart rate and shorten QT (bridge to pacing)
- **Overdrive pacing:** transvenous at rate 100-120 bpm to suppress pause-dependent TdP
- **Correct underlying cause:** stop QT-prolonging drugs, correct hypokalemia (target K+ > 4.0 mEq/L), correct hypomagnesemia
- **Do NOT give amiodarone, procainamide, or sotalol** — these prolong QT and worsen TdP
- **Defibrillation (unsynchronized) if pulseless** or hemodynamically unstable: biphasic 120-200 J; synchronized cardioversion is unreliable in polymorphic rhythms

### Polymorphic VT with Normal QT
- Treat as acute ischemia: emergent cardiology consultation, anticoagulation, catheterization
- Amiodarone 150 mg IV over 10 minutes (safe here because QT is not prolonged)
- Beta-blockade: esmolol 500 mcg/kg IV bolus then 50-200 mcg/kg/min
- Lidocaine 1-1.5 mg/kg IV bolus

### Refractory/Recurrent VT (Electrical Storm)
- Defined as >= 3 sustained VT episodes or appropriate ICD shocks in 24 hours
- Amiodarone loading + lidocaine (dual antiarrhythmic therapy)
- Esmolol 500 mcg/kg IV bolus then 50-200 mcg/kg/min or propranolol 1-3 mg IV q5min (stellate ganglion blockade sympatholysis)
- Deep sedation: propofol or general anesthesia
- Left stellate ganglion block (ultrasound-guided): bupivacaine 0.25% 10-15 mL
- Emergent catheter ablation consultation
- Mechanical circulatory support if hemodynamic compromise

### Pre-excitation (WPW) with AF
- **Do NOT give AV nodal blocking agents** (adenosine, beta-blockers, calcium channel blockers, digoxin) — can cause preferential conduction down accessory pathway and VF
- Procainamide 20-50 mg/min IV (slows accessory pathway conduction)
- Synchronized cardioversion if hemodynamically unstable

## Disposition

- **Pulseless VT/VF with ROSC:** ICU with continuous monitoring, targeted temperature management if indicated, cardiology consultation
- **Unstable VT requiring cardioversion:** ICU/CCU admission, continuous telemetry, antiarrhythmic infusion
- **Stable monomorphic VT:** CCU/telemetry admission, cardiology consultation, echocardiography, evaluate for ICD candidacy
- **Torsades de pointes:** ICU with continuous telemetry, isoproterenol drip or temporary pacing until QT normalizes
- **Electrical storm:** ICU, electrophysiology consultation, evaluate for emergent ablation
- **NSVT in structurally normal heart with normal K+/Mg2+, no ischemia:** observation on telemetry, outpatient electrophysiology follow-up if recurrent
- **ICD evaluation:** all patients surviving sustained VT or VF (secondary prevention) require ICD discussion before discharge

## Pitfalls

1. **Treating wide complex tachycardia as SVT.** Administering verapamil or diltiazem to VT causes vasodilation without terminating the arrhythmia, leading to refractory hypotension and cardiac arrest. When in doubt, it is VT.

2. **Using amiodarone for torsades de pointes.** Amiodarone prolongs QT and worsens torsades. Magnesium sulfate 2 g IV is first-line. Overdrive pacing is definitive.

3. **Delivering unsynchronized shocks for stable VT with pulse.** Unsynchronized shock during the relative refractory period induces VF. Use synchronized cardioversion for any rhythm with a pulse and identifiable QRS complexes.

4. **Failing to correct electrolytes.** Hypokalemia and hypomagnesemia lower the threshold for VT/VF and render antiarrhythmic drugs ineffective. Target K+ > 4.0 mEq/L and Mg2+ > 2.0 mg/dL.

5. **Not obtaining a 12-lead ECG during tachycardia.** The morphology during VT guides future electrophysiology study and ablation planning. Capture a 12-lead before terminating stable VT when possible.

6. **Giving AV nodal blockers in WPW with atrial fibrillation.** Adenosine, beta-blockers, calcium channel blockers, and digoxin can cause unopposed conduction down the accessory pathway, precipitating VF and cardiac arrest. Use procainamide or cardioversion.

7. **Assuming NSVT is benign.** In patients with structural heart disease (prior MI, cardiomyopathy, EF < 35%), NSVT is a risk marker for sudden cardiac death. Requires echocardiography, risk stratification, and electrophysiology referral.

8. **Not recognizing electrical storm early.** Three or more VT episodes in 24 hours (or ICD shocks) constitutes electrical storm. Single-agent antiarrhythmic therapy is often insufficient; dual therapy (amiodarone + lidocaine) with sympatholysis (esmolol) and deep sedation may be required.

9. **Relying on heart rate to differentiate VT from SVT.** VT can present at rates of 140-160 bpm, overlapping with SVT. Heart rate alone does not distinguish the two. Apply Brugada criteria or Vereckei algorithm to the 12-lead ECG.

10. **Failing to identify and treat the underlying trigger.** VT is usually a symptom of underlying disease — acute ischemia, cardiomyopathy, electrolyte derangement, or drug toxicity. Antiarrhythmic therapy without addressing the cause leads to recurrence.
