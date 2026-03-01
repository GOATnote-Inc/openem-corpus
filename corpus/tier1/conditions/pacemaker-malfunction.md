---
id: pacemaker-malfunction
condition: Pacemaker Malfunction
aliases: [pacemaker failure, failure to capture, failure to sense, pacemaker-mediated tachycardia, pacemaker dysfunction]
icd10: [T82.110A, T82.111A, T82.119A, T82.120A, T82.121A]
esi: 2
time_to_harm:
  irreversible_injury: "< 1 hour (pacemaker-dependent patients)"
  death: "< 2 hours"
  optimal_intervention_window: "< 30 minutes"
category: cardiovascular
track: tier1
sources:
  - type: review
    ref: "Mulpuru SK, et al. Cardiac Pacemakers: Function, Troubleshooting, and Management. J Am Coll Cardiol. 2017;69(2):189-210."
  - type: guideline
    ref: "2018 ACC/AHA/HRS Guideline on the Evaluation and Management of Patients With Bradycardia and Cardiac Conduction Delay. Circulation. 2019;140(8):e382-e482."
  - type: review
    ref: "Bernstein AD, et al. The NASPE/BPEG Generic Pacemaker Code (NBG Code). Pacing Clin Electrophysiol. 2002;25(2):260-264."
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
# Pacemaker Malfunction

## Recognition

**Types of malfunction:**

*Failure to capture:*
- Pacing spikes visible on ECG without subsequent P wave (atrial) or QRS complex (ventricular)
- Patient symptomatic: bradycardia, syncope, hypotension
- Causes: lead dislodgement (most common acutely), lead fracture, battery depletion, elevated pacing threshold (fibrosis, metabolic: hyperkalemia, acidosis, flecainide), myocardial perforation

*Failure to sense (undersensing):*
- Pacing spikes occurring despite native cardiac activity (compete with intrinsic rhythm)
- Pacing at inappropriate times — pacing spike falling on T wave risks R-on-T → VF
- Causes: lead dislodgement, lead insulation break, sensitivity programmed too low, electromagnetic interference

*Failure to pace (no output):*
- No pacing spikes when expected (below programmed rate with no intrinsic rhythm)
- Battery depletion (ERI/EOL), lead fracture (complete), circuit failure, oversensing
- May be catastrophic in pacemaker-dependent patients

*Oversensing:*
- Pacemaker inhibited by non-cardiac signals (muscle artifact, T-wave oversensing, EMI, lead fracture with make-break signals)
- Inappropriate pauses, symptomatic bradycardia
- Magnet application resolves (disables sensing → asynchronous pacing)

*Pacemaker-mediated tachycardia (PMT):*
- Dual-chamber pacemaker creates reentrant circuit: atrial sense → ventricular pace → retrograde atrial activation → sensed again → ventricular pace
- Tachycardia at or near upper tracking rate (~120-130 bpm)
- Magnet application breaks the circuit

**Pacemaker-dependent patients (highest risk):**
- Prior complete heart block with no escape rhythm
- Post-AV node ablation
- History of asystolic episodes

## Critical Actions

| Action | Target |
|---|---|
| 12-lead ECG | < 5 minutes |
| Assess hemodynamic stability | Immediate |
| Magnet available at bedside | Immediate |
| Transcutaneous pacing pads applied | < 5 minutes |

1. **Assess hemodynamic stability** — if unstable, initiate transcutaneous pacing immediately regardless of malfunction type
2. **12-lead ECG** — identify pacing spikes, relationship to P/QRS, native rhythm
3. **Apply magnet** over pulse generator:
   - Converts pacemaker to asynchronous mode (VOO or DOO) at fixed rate (~65-85 bpm)
   - Eliminates sensing — corrects oversensing and PMT
   - Tests capture threshold — if spikes appear with capture under magnet, undersensing was the issue
   - Does NOT fix failure to capture from lead fracture or battery depletion
4. **Atropine 1 mg IV** for symptomatic bradycardia if native rhythm present
5. **Transcutaneous pacing** — immediate for pacemaker-dependent patient with failure to capture/pace
6. **Electrolyte correction:** K+ > 3.5 mEq/L, Ca2+ normal range, correct acidosis
7. **Cardiology/EP consultation STAT** for device interrogation

## Differential Diagnosis

- **Intrinsic bradycardia with functional pacemaker** — pacemaker firing appropriately but at programmed low rate; may need rate adjustment
- **Lead dislodgement** — most common early cause; CXR shows displaced lead
- **Battery depletion** — elective replacement indicator (ERI) or end of life (EOL); magnet test shows decreased rate
- **Electromagnetic interference** — MRI, cautery, TENS; resolves when source removed
- **Twiddler syndrome** — patient manipulation of pulse generator causing lead displacement; CXR diagnostic
- **Myocardial perforation** — chest pain, pericardial effusion, diaphragmatic pacing (hiccups), loss of capture

## Workup

- **12-lead ECG:** Identify pacing spikes, capture, sensing, pacing rate, relationship to native rhythm
- **Magnet test:** Apply magnet → observe for asynchronous pacing at fixed rate with capture → confirms battery and lead integrity
- **PA and lateral chest X-ray:** Lead position (dislodgement, perforation), lead integrity (fracture visible on X-ray), generator pocket
- **Device interrogation (by EP/cardiology):** Battery voltage, impedance, sensing/pacing thresholds, stored events, lead integrity diagnostics — definitive diagnostic study
- **Labs:** BMP (K+, Ca2+, Mg2+), ABG if acidosis suspected, drug levels (if on antiarrhythmics affecting threshold: flecainide, propafenone)
- **Echocardiography:** If perforation suspected — pericardial effusion, lead position
- **CT chest:** If lead perforation suspected and echo inconclusive

## Treatment

### Failure to Capture
- Increase pacing output if programmable bedside
- Correct metabolic causes: treat hyperkalemia (calcium gluconate 1 g IV, insulin/glucose, bicarbonate), correct acidosis
- Transcutaneous pacing as bridge
- Lead revision/replacement by EP

### Failure to Sense (Undersensing)
- Magnet application (temporary — converts to asynchronous mode)
- Reprogram sensitivity threshold (by EP)
- Lead revision if hardware failure

### Oversensing
- Magnet application — immediate fix (disables sensing)
- Reprogram sensitivity or sensing parameters (by EP)
- Lead revision if fracture causing artifact

### Failure to Pace (No Output)
- Transcutaneous pacing immediately
- Magnet application — if battery at ERI, magnet rate will be lower than programmed rate
- Generator replacement for battery depletion
- Lead replacement for fracture

### Pacemaker-Mediated Tachycardia
- Magnet application — breaks reentry by disabling atrial sensing
- Reprogram PVARP (post-ventricular atrial refractory period) — increases it to prevent retrograde P-wave sensing

### Hemodynamically Unstable — Any Cause
- Transcutaneous pacing: set rate 60-80, increase mA until capture
- Atropine 1 mg IV q3-5min (max 3 mg) for native rhythm support
- Dopamine 5-20 mcg/kg/min IV or epinephrine 2-10 mcg/min IV
- Transvenous pacing if prolonged need

## Disposition

- **ICU/telemetry admission:** All pacemaker-dependent patients with malfunction, hemodynamic instability, transcutaneous pacing required
- **Monitored bed:** Stable malfunction pending EP interrogation and management
- **Transfer:** Facilities without EP capability and device interrogation equipment
- **Discharge:** Only after device interrogation confirms malfunction resolved and device functioning properly; EP follow-up within 1-2 weeks

## Pitfalls

1. **Not having transcutaneous pacing pads applied on pacemaker-dependent patients with suspected malfunction.** Even if the patient is currently stable, pacemaker-dependent patients can deteriorate to asystole without warning. Pads should be applied prophylactically while awaiting EP consultation.

2. **Interpreting magnet behavior incorrectly.** A magnet over a pacemaker produces asynchronous pacing at a fixed rate (varies by manufacturer, typically 65-85 bpm). A magnet over an ICD disables tachyarrhythmia therapies (shocks) but does NOT affect pacing function. These are fundamentally different responses — know which device the patient has.

3. **Failing to check a CXR for lead position.** Lead dislodgement is the most common cause of early pacemaker malfunction. A PA and lateral CXR comparing current lead position to the post-implant film is a quick, essential diagnostic step that does not require device interrogation.

4. **Missing hyperkalemia as a cause of loss of capture.** Elevated potassium raises the myocardial pacing threshold, causing failure to capture. The ECG may show peaked T waves and widened QRS. Treatment of hyperkalemia (calcium gluconate 1 g IV, insulin/glucose) may restore pacemaker capture without hardware intervention.

5. **Applying a magnet to an ICD when a patient is in VT.** Placing a magnet on an ICD disables shock therapy. If the patient is having appropriate ICD shocks for VT/VF, a magnet will prevent lifesaving therapy. Conversely, if the patient is having inappropriate shocks (e.g., for AF or noise), a magnet is appropriate. Distinguish between appropriate and inappropriate therapy before applying.
