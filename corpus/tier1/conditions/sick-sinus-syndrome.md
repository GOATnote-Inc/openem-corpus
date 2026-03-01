---
id: sick-sinus-syndrome
condition: Sick Sinus Syndrome
aliases: [SSS, sinus node dysfunction, SND, tachy-brady syndrome, bradycardia-tachycardia syndrome]
icd10: [I49.5]
esi: 2
time_to_harm: "< 2 hours if symptomatic bradycardia"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2018 ACC/AHA/HRS Guideline on the Evaluation and Management of Patients With Bradycardia and Cardiac Conduction Delay. Circulation. 2019;140(8):e382-e482."
  - type: guideline
    ref: "2021 ESC Guidelines on Cardiac Pacing and Cardiac Resynchronization Therapy. Eur Heart J. 2021;42(35):3427-3520."
  - type: review
    ref: "Semelka M, et al. Sick Sinus Syndrome: A Review. Am Fam Physician. 2013;87(10):691-696."
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
# Sick Sinus Syndrome

## Recognition

**Clinical presentations:**
- Syncope, presyncope, dizziness
- Fatigue, exercise intolerance
- Palpitations (during tachycardia phase)
- Cognitive impairment in elderly (chronotropic incompetence)

**ECG manifestations (may require prolonged monitoring):**
- Inappropriate sinus bradycardia (< 50 bpm) unresponsive to exercise or atropine
- Sinus pauses > 3 seconds
- Sinoatrial exit block
- Alternating bradycardia and atrial tachyarrhythmias (tachy-brady syndrome)
- Chronotropic incompetence (failure to achieve 80% of age-predicted max HR with exercise)
- Prolonged sinus node recovery time after cardioversion of atrial fibrillation

**Risk factors:**
- Age > 65 (most common cause: degenerative fibrosis of sinus node)
- Medications: beta-blockers, calcium channel blockers (verapamil, diltiazem), digoxin, amiodarone, lithium
- Post-cardiac surgery (especially atrial septal defect repair)
- Infiltrative diseases: amyloidosis, sarcoidosis, hemochromatosis

## Critical Actions

| Action | Target |
|---|---|
| 12-lead ECG | < 10 minutes |
| Hemodynamic assessment | Immediate |
| Medication review | < 15 minutes |

1. **Assess hemodynamic stability** — hypotension, AMS, chest pain, or acute HF requires emergent intervention
2. **Discontinue causative medications** — beta-blockers, CCBs, digoxin, antiarrhythmics
3. **Atropine 0.5-1 mg IV** for symptomatic bradycardia (may repeat q3-5min, max 3 mg). Often has limited or transient effect in SSS.
4. **Transcutaneous pacing** if atropine fails and patient hemodynamically unstable
5. **For tachy-brady syndrome:** Pacemaker must be placed before starting rate/rhythm control agents, as AV nodal blockers will worsen bradycardia phase
6. **Cardiology consultation** for pacemaker evaluation

## Differential Diagnosis

- **Physiologic sinus bradycardia** — athletes, sleep, increased vagal tone; asymptomatic
- **Drug-induced bradycardia** — resolve with drug discontinuation (not true SSS)
- **Hypothyroidism** — check TSH; reversible cause
- **Complete heart block** — AV dissociation rather than sinus node dysfunction
- **Carotid sinus hypersensitivity** — triggered by neck pressure; ventricular pause > 3 sec
- **Neurocardiogenic syncope** — vasovagal mechanism; normal baseline ECG

## Workup

- **12-lead ECG:** Baseline rhythm, rate, pauses, conduction intervals
- **Continuous telemetry:** Capture intermittent pauses and tachy-brady episodes
- **Labs:** TSH, BMP (K+, Ca2+), digoxin level (if applicable), troponin if concern for ischemia
- **Holter monitor (24-72 hour):** Outpatient — correlate symptoms with rhythm (if stable for discharge)
- **Event recorder or implantable loop recorder:** For infrequent symptoms
- **Echocardiography:** Assess for structural heart disease
- **Exercise stress test:** Document chronotropic incompetence

## Treatment

### Acute Symptomatic Bradycardia
- Atropine 0.5-1 mg IV q3-5min (max 3 mg)
- Transcutaneous pacing if atropine ineffective
- Dopamine 5-20 mcg/kg/min IV or epinephrine 2-10 mcg/min IV as temporizing measure
- Isoproterenol 2-10 mcg/min IV (chronotropic support)

### Tachy-Brady Syndrome
- Permanent pacemaker required BEFORE initiating rate/rhythm control
- Post-pacemaker: beta-blocker or CCB for tachycardia component, antiarrhythmics as needed
- Anticoagulation per CHA2DS2-VASc score if atrial fibrillation/flutter present

### Reversible Causes
- Discontinue offending medications (wait 5 half-lives before determining if SSS is intrinsic)
- Treat hypothyroidism: levothyroxine 1.6 mcg/kg/day PO
- Correct electrolyte abnormalities

### Permanent Pacemaker
- Dual-chamber (DDD) pacing preferred — maintains AV synchrony, reduces AF incidence
- Rate-responsive pacing for chronotropic incompetence
- Avoid single-chamber ventricular (VVI) pacing — associated with pacemaker syndrome and increased AF

## Disposition

- **Telemetry admission:** Symptomatic bradycardia, pauses > 3 seconds, tachy-brady requiring rate control, new diagnosis with hemodynamic symptoms
- **ICU admission:** Hemodynamic instability requiring temporary pacing or vasopressors
- **Discharge with outpatient follow-up:** Mild symptoms, drug-induced (drug discontinued), stable hemodynamics, Holter ordered
- **Cardiology referral:** All new-onset SSS for pacemaker evaluation
- **Transfer:** Facilities without cardiology or temporary pacing capability

## Pitfalls

1. **Starting rate or rhythm control agents for atrial fibrillation in tachy-brady syndrome without a pacemaker.** Beta-blockers, calcium channel blockers, and antiarrhythmics will suppress the tachycardia but exacerbate the bradycardia — potentially causing prolonged asystolic pauses or hemodynamic collapse. Pacemaker first, then treat the tachycardia.

2. **Attributing syncope in elderly patients to dehydration or orthostasis without ECG.** SSS is the most common indication for pacemaker implantation in the elderly. A 12-lead ECG and telemetry monitoring should be obtained in any elderly patient with unexplained syncope.

3. **Diagnosing SSS based on a single asymptomatic bradycardic ECG.** Sinus bradycardia is physiologic in athletes and during sleep. SSS requires correlation of symptoms with documented bradyarrhythmia. An isolated low heart rate without symptoms does not warrant pacing.

4. **Inadequate monitoring duration.** SSS is intermittent. A normal 12-lead ECG does not exclude SSS. Patients with concerning symptoms may need 24-72 hour Holter monitoring, event recorders, or implantable loop recorders to capture diagnostic episodes.
