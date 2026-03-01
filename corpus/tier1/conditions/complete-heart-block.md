---
id: complete-heart-block
condition: Complete Heart Block (Third-Degree AV Block)
aliases: [third-degree AV block, 3rd degree heart block, complete AV block, CHB]
icd10: [I44.2]
esi: 2
time_to_harm:
  irreversible_injury: "< 1 hour"
  death: "< 2 hours"
  optimal_intervention_window: "< 30 minutes"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2018 ACC/AHA/HRS Guideline on the Evaluation and Management of Patients With Bradycardia and Cardiac Conduction Delay. Circulation. 2019;140(8):e382-e482."
  - type: guideline
    ref: "2021 ESC Guidelines on Cardiac Pacing and Cardiac Resynchronization Therapy. Eur Heart J. 2021;42(35):3427-3520."
  - type: guideline
    ref: "2020 AHA ACLS Guidelines for Bradycardia with a Pulse Algorithm."
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
# Complete Heart Block (Third-Degree AV Block)

## Recognition

**Presentation:**
- Syncope or presyncope (Stokes-Adams attacks)
- Profound bradycardia (ventricular rate 20-40 bpm with infranodal block, 40-60 bpm with junctional escape)
- Fatigue, dyspnea, altered mental status, chest pain
- Cannon A waves on JVP examination
- Variable intensity S1 on auscultation

**ECG criteria:**
- Complete AV dissociation: P waves and QRS complexes at independent rates
- Atrial rate > ventricular rate
- No consistent PR interval
- Narrow QRS escape (junctional, rate ~40-60 bpm) = block at AV node level
- Wide QRS escape (ventricular, rate ~20-40 bpm) = block below His bundle — higher risk

**Etiologies:**
- Acute inferior MI (often transient, nodal level) — most common reversible cause
- Anterior MI (infranodal, high mortality, often permanent)
- Drug toxicity: beta-blockers, calcium channel blockers, digoxin, amiodarone
- Hyperkalemia, Lyme disease, endocarditis, post-cardiac surgery
- Degenerative conduction disease (Lenegre disease, Lev disease)

## Critical Actions

| Action | Target |
|---|---|
| 12-lead ECG | < 5 minutes from arrival |
| Hemodynamic assessment | Immediate |
| Transcutaneous pacing (if unstable) | < 10 minutes |
| Cardiology consultation | < 30 minutes |

1. **Assess hemodynamic stability** — hypotension, AMS, chest pain, or acute HF = unstable
2. **Atropine 1 mg IV** — first-line for symptomatic bradycardia; repeat q3-5min (max 3 mg). Effective for nodal block (narrow QRS escape); often ineffective for infranodal block (wide QRS)
3. **Transcutaneous pacing** — apply immediately if atropine fails or wide QRS escape. Set rate 60-80 bpm, increase mA until electrical and mechanical capture. Sedation with midazolam 1-2 mg IV or fentanyl 25-50 mcg IV
4. **Transvenous pacing** — if TCP fails or prolonged pacing needed. Right IJ or femoral vein approach
5. **Vasopressors as bridge** — dopamine 5-20 mcg/kg/min IV or epinephrine 2-10 mcg/min IV infusion if pacing unavailable
6. **Reverse treatable causes** — stop offending drugs, correct hyperkalemia (calcium gluconate 1 g IV), treat acute MI, check Lyme titers if endemic area
7. **Isoproterenol 2-10 mcg/min IV** — temporizing for infranodal block refractory to atropine (use cautiously in acute MI)

## Differential Diagnosis

- Second-degree AV block (Mobitz II) — some P waves conduct; can progress to CHB
- High-grade AV block — more P waves blocked than conducted but not complete dissociation
- Isorhythmic AV dissociation — similar rates of atrial and ventricular activity (benign, not true block)
- Hyperkalemia — wide QRS, peaked T waves; may mimic or cause CHB
- Junctional rhythm with retrograde P waves — distinguish from AV dissociation
- Drug-induced bradycardia — calcium channel blockers, beta-blockers, digoxin

## Workup

- **12-lead ECG:** Identify escape rhythm morphology (narrow vs wide QRS), assess for STEMI
- **Continuous telemetry:** Mandatory
- **Labs:** BMP (potassium, calcium, magnesium), troponin, digoxin level (if applicable), TSH, Lyme titers (endemic areas)
- **Chest X-ray:** Assess for cardiomegaly, pulmonary edema
- **Echocardiography:** Evaluate ventricular function, structural heart disease
- **Prior ECGs for comparison:** Baseline conduction pattern

## Treatment

### Hemodynamically Unstable
- Atropine 1 mg IV q3-5min (max 3 mg) — limited efficacy in infranodal block
- Transcutaneous pacing — immediate if atropine fails
- Transvenous pacing — definitive temporary measure
- Dopamine 5-20 mcg/kg/min IV or epinephrine 2-10 mcg/min IV as bridge

### Hemodynamically Stable
- Continuous monitoring in telemetry bed
- Identify and treat reversible causes
- Cardiology consultation for permanent pacemaker evaluation

### Specific Etiologies
- **Acute inferior MI:** Often resolves within 2-7 days. Temporary pacing if symptomatic. Monitor closely.
- **Acute anterior MI:** High risk of permanent block. Early transvenous pacing. Likely needs permanent pacemaker.
- **Drug toxicity:** Discontinue offending agent. Calcium gluconate 1-3 g IV for CCB/hyperkalemia. Digoxin-specific Fab fragments (Digibind) for digoxin toxicity.
- **Lyme disease:** Ceftriaxone 2 g IV daily x 14-21 days. Most CHB resolves with antibiotics.
- **Hyperkalemia:** Calcium gluconate 1 g IV over 2-3 min, insulin 10 units IV + D50 25 g IV, sodium bicarbonate 50 mEq IV if acidotic.

### Permanent Pacemaker Indications
- Third-degree AV block with symptomatic bradycardia (Class I)
- Third-degree AV block with ventricular rate < 40 bpm while awake (Class I)
- Third-degree AV block post-cardiac surgery not expected to resolve (Class I)
- Third-degree AV block with cardiomegaly or LV dysfunction (Class I)

## Disposition

- **ICU/CCU admission:** All hemodynamically unstable patients, those requiring temporary pacing, acute MI with CHB
- **Telemetry admission:** Stable patients with new-onset CHB pending pacemaker evaluation
- **Transfer criteria:** Facilities without cardiology/electrophysiology or temporary pacing capability must transfer immediately
- **Never discharge:** New-onset complete heart block, even if asymptomatic — risk of sudden cardiac death from unreliable escape rhythm

## Pitfalls

1. **Relying on atropine for infranodal (wide QRS) block.** Atropine increases sinus rate and AV nodal conduction but does not improve infranodal conduction. It may paradoxically worsen block by increasing atrial rate without improving ventricular response. Proceed directly to pacing.

2. **Failing to obtain ECG in syncope workup.** Complete heart block causing Stokes-Adams attacks may present with preserved hemodynamics between episodes. A single normal-appearing moment does not exclude intermittent CHB. Telemetry is essential.

3. **Missing acute MI as the cause.** Inferior MI causes nodal CHB in ~15% of cases; anterior MI causes infranodal CHB with high mortality. Always check troponin and obtain 12-lead ECG looking for ST changes in the setting of new CHB.

4. **Confusing isorhythmic AV dissociation with CHB.** In isorhythmic dissociation, atrial and ventricular rates are similar — this is usually benign and does not require pacing. True CHB has atrial rate clearly exceeding ventricular rate.

5. **Delaying transcutaneous pacing while waiting for transvenous access.** TCP is a bridge, not a definitive therapy, but it is immediately available. Apply pads early in any unstable bradycardia. Do not wait for the proceduralist.
