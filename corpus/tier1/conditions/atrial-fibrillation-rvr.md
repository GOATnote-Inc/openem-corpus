---
id: atrial-fibrillation-rvr
condition: Atrial Fibrillation with Rapid Ventricular Response
aliases: [AFib with RVR, rapid AFib, AF with fast ventricular rate, atrial fibrillation with rapid rate]
icd10: [I48.0, I48.19, I48.20, I48.91]
esi: 2
time_to_harm: "< 2 hours"
mortality_if_delayed: "Hemodynamic collapse if rate uncontrolled; stroke risk with delayed anticoagulation"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2023 ACC/AHA/ACCP/HRS Guideline for Diagnosis and Management of Atrial Fibrillation"
    doi: "10.1161/CIR.0000000000001193"
  - type: guideline
    ref: "2020 ESC Guidelines for the diagnosis and management of atrial fibrillation"
    doi: "10.1093/eurheartj/ehaa612"
  - type: pubmed
    ref: "Stiell IG et al. Canadian Cardiovascular Society atrial fibrillation guidelines 2010: management of recent-onset atrial fibrillation and flutter in the emergency department. Can J Cardiol. 2011;27(1):38-46"
    pmid: "21329861"
  - type: pubmed
    ref: "January CT et al. 2019 AHA/ACC/HRS Focused Update of the 2014 Guideline for Management of Patients with Atrial Fibrillation. Circulation. 2019;140(2):e125-e151"
    pmid: "30686041"
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
# Atrial Fibrillation with Rapid Ventricular Response

## Recognition

**ECG findings:**
- Irregularly irregular rhythm
- Absent P waves replaced by fibrillatory baseline
- Ventricular rate > 100 bpm (typically 110-180 bpm)
- Narrow QRS unless concurrent bundle branch block or accessory pathway

**Symptoms:**
- Palpitations, chest pain, dyspnea
- Lightheadedness, presyncope, syncope
- Fatigue, exercise intolerance
- Acute heart failure exacerbation (flash pulmonary edema)

**Hemodynamic instability indicators:**
- SBP < 90 mmHg
- Altered mental status
- Acute pulmonary edema
- Ongoing chest pain with ischemic ECG changes
- Signs of end-organ hypoperfusion

**Identify and treat precipitants:**
- Sepsis, pneumonia, PE, acute coronary syndrome
- Thyrotoxicosis, alcohol intoxication/withdrawal
- Post-surgical, electrolyte abnormalities (hypokalemia, hypomagnesemia)
- Medication noncompliance, stimulant use
- Decompensated heart failure

**Distinguish from AFib with pre-excitation (WPW):**
- Wide, irregular QRS with varying morphology
- Rate often > 200 bpm
- AV nodal blockers (diltiazem, verapamil, digoxin, adenosine) are CONTRAINDICATED — cause VF

## Critical Actions

| Action | Target |
|---|---|
| 12-lead ECG | < 10 minutes |
| Hemodynamic assessment | Immediate |
| Synchronized cardioversion if unstable | Without delay |
| Rate control if stable | Within 30 minutes |

1. **Unstable patient:** Synchronized cardioversion at 120-200 J biphasic; sedate with etomidate 0.2-0.3 mg/kg IV or midazolam 2-5 mg IV if time permits
2. **Stable patient — rate control strategy:**
   - Diltiazem 0.25 mg/kg IV over 2 minutes (typical dose 15-20 mg, max 20 mg); repeat at 0.35 mg/kg IV after 15 minutes if needed; infusion at 5-15 mg/hr
   - Metoprolol 5 mg IV q5min x 3 doses (avoid if acute HF, hypotension, bronchospasm)
3. **Magnesium** 2 g IV over 15 minutes — augments rate control, correct hypomagnesemia
4. **Assess CHA2DS2-VASc score** for anticoagulation decision
5. **Identify and treat underlying cause** (sepsis, ACS, PE, thyrotoxicosis)

## Differential Diagnosis

- Atrial flutter with variable block (sawtooth flutter waves at ~300 bpm)
- Multifocal atrial tachycardia (3 or more distinct P-wave morphologies; irregularly irregular but WITH P waves)
- SVT with irregular conduction
- Sinus tachycardia with frequent PACs
- AFib with pre-excitation (WPW) — wide, irregular, very rapid
- Artifact or motion artifact mimicking irregularity
- Ventricular tachycardia (wide complex; regular, not irregular)

## Workup

- **12-lead ECG:** Confirm rhythm, assess for ischemia, pre-excitation, LVH
- **CBC:** Assess for anemia, infection
- **BMP:** Potassium, magnesium, calcium, creatinine (electrolyte correction, renal dosing)
- **Magnesium level**
- **TSH:** Hyperthyroidism is reversible cause
- **Troponin:** Demand ischemia from tachycardia vs. ACS as trigger
- **BNP/NT-proBNP:** If heart failure suspected
- **Chest X-ray:** Pulmonary edema, pneumonia, cardiomegaly
- **Coagulation studies:** INR if on warfarin; baseline before anticoagulation
- **Toxicology screen** if stimulant use suspected
- **CT pulmonary angiography** if PE suspected
- **Point-of-care echocardiography:** Assess EF, wall motion, pericardial effusion

## Treatment

### Rate Control (First-Line for Most ED Patients)

**Preserved EF (>= 40%):**
- Diltiazem 0.25 mg/kg IV bolus (max 20 mg) over 2 min, repeat 0.35 mg/kg IV at 15 min; drip 5-15 mg/hr
- OR metoprolol 5 mg IV q5min up to 15 mg; then metoprolol tartrate 25-50 mg PO q6h

**Reduced EF (< 40%) or acute HF:**
- Amiodarone 150 mg IV over 10 minutes, then 1 mg/min x 6 hours, then 0.5 mg/min x 18 hours
- Diltiazem and verapamil are relatively contraindicated in decompensated HF (negative inotropy)
- Digoxin 0.5 mg IV, then 0.25 mg IV q6h x 2 doses (slow onset 1-4 hours; adjunct, not sole agent)

**Target heart rate:** < 110 bpm at rest (RACE II trial supports lenient rate control)

### Rhythm Control (Acute Cardioversion)

**Electrical cardioversion:**
- Synchronized shock 120-200 J biphasic
- Indicated if: hemodynamic instability, AFib duration < 48 hours and patient desires rhythm control, pre-excited AFib

**Pharmacologic cardioversion (AFib duration < 48 hours or adequately anticoagulated):**
- Procainamide 15-17 mg/kg IV over 30-60 minutes (monitor for hypotension and QRS widening)
- Ibutilide 1 mg IV over 10 minutes (0.01 mg/kg for patients < 60 kg); repeat x 1 after 10 minutes if no conversion (monitor for torsades — requires 4-6h telemetry post-dose)
- Amiodarone 150 mg IV over 10 min (less effective acutely but safer in structural heart disease)

### Pre-excited AFib (WPW)
- Procainamide 15-17 mg/kg IV over 30-60 minutes
- OR synchronized cardioversion
- **CONTRAINDICATED:** Diltiazem, verapamil, digoxin, adenosine, beta-blockers

### Anticoagulation
- CHA2DS2-VASc >= 2 (men) or >= 3 (women): initiate anticoagulation
- Apixaban 5 mg PO BID or rivaroxaban 20 mg PO daily with food (preferred over warfarin per 2023 ACC/AHA guidelines)
- If cardioversion planned and duration >= 48 hours or uncertain: 3 weeks anticoagulation OR TEE to exclude LAA thrombus before cardioversion
- If duration < 48 hours and CHA2DS2-VASc >= 2: heparin bridge, then DOAC

### Electrolyte Repletion
- Potassium target > 4.0 mEq/L: KCl 40 mEq IV over 2-4 hours
- Magnesium 2 g IV over 15 minutes

## Disposition

- **Admit/observe:** New-onset AFib, hemodynamically unstable requiring drip, rate poorly controlled, acute HF, ACS trigger, new anticoagulation initiation in high-risk patients
- **Discharge from ED:** Known AFib, rate controlled (< 110 bpm), stable, no acute precipitant, reliable follow-up within 1-2 weeks
- **ICU:** Cardiogenic shock, cardioversion with hemodynamic instability, requiring multiple vasopressors
- **Cardiology follow-up:** All new-onset AFib (echocardiography, rhythm strategy discussion, anticoagulation)

## Pitfalls

1. **Using diltiazem or verapamil in AFib with pre-excitation (WPW).** AV nodal blockers enhance conduction down the accessory pathway and precipitate ventricular fibrillation. Any wide-complex irregular tachycardia should raise suspicion for pre-excited AFib.

2. **Attributing tachycardia to AFib without searching for the underlying trigger.** AFib with RVR is frequently a secondary response to sepsis, PE, ACS, thyrotoxicosis, or hemorrhage. Treating the rate without addressing the cause leads to decompensation.

3. **Cardioverting AFib of unknown or prolonged duration (>= 48 hours) without anticoagulation or TEE.** Risk of left atrial appendage thrombus embolization causing stroke. Duration is often uncertain — err toward anticoagulation.

4. **Aggressive rate control causing hypotension.** Diltiazem boluses in rapid succession without reassessing blood pressure. The elderly and those with reduced EF are particularly vulnerable. Titrate to rate < 110, not normal sinus rate.

5. **Giving IV beta-blockers and IV calcium channel blockers sequentially.** Dual AV nodal blockade causes severe bradycardia, heart block, and cardiac arrest. Choose one class. Wait for washout before switching.

6. **Overlooking hypokalemia and hypomagnesemia as perpetuating factors.** Electrolyte depletion sustains AFib and reduces efficacy of rate-control agents. Replete before escalating antiarrhythmics.

7. **Diagnosing "AFib with RVR" when the rhythm is actually multifocal atrial tachycardia (MAT).** MAT is irregularly irregular but has discrete P waves of varying morphology. Treatment is different: correct hypoxia, treat underlying lung disease, magnesium. AV nodal blockers are less effective.

8. **Failing to anticoagulate high-risk patients at discharge.** CHA2DS2-VASc scoring and anticoagulation initiation are ED responsibilities when the diagnosis is made in the ED. DOACs are preferred over warfarin.

9. **Using amiodarone as a rate-control agent in young patients without structural heart disease.** Amiodarone has significant long-term toxicity (thyroid, pulmonary, hepatic). Reserve for acute HF or when other agents fail. Diltiazem or metoprolol are first-line for rate control with preserved EF.
