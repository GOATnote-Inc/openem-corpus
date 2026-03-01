---
id: wpw-syndrome
condition: Wolff-Parkinson-White Syndrome
aliases: [WPW, Wolff-Parkinson-White, ventricular pre-excitation syndrome, WPW pattern]
icd10: [I45.6]
esi: 2
time_to_harm:
  irreversible_injury: "< 30 minutes"
  death: "< 1 hour"
  optimal_intervention_window: "< 15 minutes"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2015 ACC/AHA/HRS Guideline for the Management of Adult Patients With Supraventricular Tachycardia. Circulation. 2016;133(14):e506-e574."
  - type: guideline
    ref: "2019 ESC Guidelines for the Management of Patients With Supraventricular Tachycardia. Eur Heart J. 2020;41(5):655-720."
  - type: review
    ref: "Brugada J, et al. Wolf-Parkinson-White Syndrome: Diagnosis, Risk Assessment, and Therapy. Diagnostics. 2024;14(3):296."
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
# Wolff-Parkinson-White Syndrome

## Recognition

**Baseline ECG (WPW pattern):**
- Short PR interval (< 120 ms)
- Delta wave (slurred upstroke of QRS)
- Wide QRS (> 120 ms)
- Secondary ST-T wave changes

**Arrhythmia presentations:**

*Orthodromic AVRT (70-80% of WPW arrhythmias):*
- Narrow complex regular tachycardia (150-250 bpm)
- Antegrade conduction via AV node, retrograde via accessory pathway
- Clinically indistinguishable from typical AVNRT/SVT

*Antidromic AVRT (5-10%):*
- Wide complex regular tachycardia (150-250 bpm)
- Antegrade via accessory pathway, retrograde via AV node
- Must differentiate from VT

*Atrial fibrillation with pre-excitation (LIFE-THREATENING):*
- Irregularly irregular wide complex tachycardia
- Rates 200-300+ bpm possible (bypassing AV node rate control)
- Variable QRS morphology (fusion beats)
- Can degenerate to ventricular fibrillation

**Red flags for degeneration to VF:**
- Shortest pre-excited RR interval < 250 ms
- Heart rate > 250 bpm
- Hemodynamic instability

## Critical Actions

| Action | Target |
|---|---|
| 12-lead ECG | < 5 minutes |
| Identify pre-excitation | Immediate |
| Cardioversion if unstable | < 5 minutes |

1. **Identify presence of pre-excitation** before treating any tachyarrhythmia — delta waves on baseline ECG or wide irregular tachycardia
2. **Unstable patient (any WPW arrhythmia):** Synchronized cardioversion 100-200 J biphasic immediately
3. **AF with pre-excitation (stable):** Procainamide 20-50 mg/min IV (max 17 mg/kg) OR ibutilide 1 mg IV over 10 min. These slow accessory pathway conduction.
4. **Orthodromic AVRT (narrow complex, stable):** Vagal maneuvers first, then adenosine 6 mg rapid IV push (may use 12 mg if no response)
5. **ABSOLUTELY AVOID in pre-excited AF:** AV nodal blockers — adenosine, verapamil, diltiazem, digoxin, beta-blockers. These block the AV node, forcing all conduction down the accessory pathway → VF and death.
6. **Defibrillation:** Unsynchronized at 200 J biphasic if VF develops
7. **Electrophysiology consultation** for catheter ablation (definitive treatment)

## Differential Diagnosis

- **AVNRT** — narrow complex SVT without pre-excitation on baseline ECG
- **Ventricular tachycardia** — wide complex regular tachycardia; assume VT until proven otherwise in wide complex tachycardia
- **Atrial fibrillation without pre-excitation** — irregularly irregular but narrow QRS
- **Atrial flutter with variable block** — may appear irregularly irregular; look for flutter waves
- **Mahaim fiber tachycardia** — LBBB morphology wide complex tachycardia with normal PR at baseline
- **Bundle branch reentry VT** — wide complex tachycardia in dilated cardiomyopathy

## Workup

- **12-lead ECG:** Both during tachycardia AND after conversion to sinus rhythm (look for delta waves)
- **Continuous telemetry:** Mandatory
- **Labs:** BMP, magnesium, troponin (if hemodynamic compromise), TSH
- **Echocardiography:** Rule out structural heart disease (Ebstein anomaly associated with WPW)
- **Electrophysiology study:** Outpatient for risk stratification and ablation planning

## Treatment

### Orthodromic AVRT (Narrow Complex, Stable)
- Vagal maneuvers (modified Valsalva with leg elevation)
- Adenosine 6 mg rapid IV push → 12 mg → 12 mg (flush with 20 mL NS)
- If refractory: procainamide 20-50 mg/min IV (max 17 mg/kg) or synchronized cardioversion

### Antidromic AVRT (Wide Complex, Stable)
- Procainamide 20-50 mg/min IV (max 17 mg/kg)
- Ibutilide 1 mg IV over 10 min (may repeat once)
- Synchronized cardioversion if refractory

### Atrial Fibrillation with Pre-excitation
- **First-line:** Synchronized cardioversion 120-200 J biphasic
- **Pharmacologic (if stable):** Procainamide 20-50 mg/min IV (max 17 mg/kg) — slows accessory pathway conduction
- Ibutilide 1 mg IV over 10 min — alternative
- **CONTRAINDICATED:** Adenosine, verapamil, diltiazem, digoxin, beta-blockers, amiodarone IV (controversial — may block AV node preferentially)

### Definitive Treatment
- Catheter ablation of accessory pathway — success rate > 95%, recurrence < 5%
- EP referral for all symptomatic WPW patients

## Disposition

- **ICU/telemetry admission:** Post-cardioversion, hemodynamic instability, recurrent arrhythmias, AF with pre-excitation
- **Observation:** Stable orthodromic AVRT after successful conversion — minimum 4-6 hours monitoring
- **Discharge with EP follow-up:** Stable conversion, no recurrence, known WPW with first uncomplicated episode
- **Transfer criteria:** Transfer to facility with EP capability if recurrent arrhythmia or failed cardioversion

## Pitfalls

1. **Giving AV nodal blockers in pre-excited atrial fibrillation.** Adenosine, verapamil, diltiazem, digoxin, and beta-blockers block conduction through the AV node while leaving the accessory pathway uninhibited. This forces all atrial impulses (potentially 300+/min) directly to the ventricles → ventricular fibrillation → death. This is the single most dangerous medication error in WPW.

2. **Misidentifying pre-excited AF as polymorphic VT.** Pre-excited AF produces wide complex irregular tachycardia with variable QRS morphology that mimics polymorphic VT. The treatment is cardioversion for both, but the key distinction matters for post-conversion management and ongoing treatment decisions.

3. **Failing to obtain a post-conversion ECG.** After converting WPW tachycardia, the sinus rhythm ECG showing delta waves confirms the diagnosis and documents the pathway location. Without it, the diagnosis may be missed, and the patient may be discharged without appropriate EP referral.

4. **Treating wide complex tachycardia as SVT with aberrancy.** In the ED, wide complex tachycardia should be assumed to be VT until proven otherwise. However, in known WPW, antidromic AVRT must be considered. Procainamide is appropriate for both VT and antidromic AVRT.

5. **IV amiodarone in pre-excited AF.** Although amiodarone is often considered a "safe" antiarrhythmic, IV amiodarone has predominant AV nodal blocking effects acutely and has been associated with VF in pre-excited AF. Use procainamide or cardioversion instead.
