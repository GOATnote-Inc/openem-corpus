---
id: transcutaneous-pacing
condition: Transcutaneous Pacing
aliases: [TCP, external pacing, transcutaneous cardiac pacing, noninvasive pacing]
icd10: [I49.5, I44.1, I44.2, R00.1]
esi: 1
time_to_harm:
  irreversible_injury: "< 5 minutes (end-organ hypoperfusion from bradycardia)"
  death: "< 10 minutes in unstable bradycardia with hemodynamic collapse"
  optimal_intervention_window: "Immediate upon recognition of hemodynamically unstable bradycardia"
category: procedural
track: tier1
sources:
  - type: guideline
    ref: "Panchal AR, Bartos JA, Cabanas JG, et al. Part 3: Adult Basic and Advanced Life Support: 2020 AHA Guidelines for CPR and ECC. Circulation. 2020;142(16_suppl_2):S366-S468."
    pmid: "33081529"
  - type: guideline
    ref: "Kusumoto FM, Schoenfeld MH, Barrett C, et al. 2018 ACC/AHA/HRS Guideline on the Evaluation and Management of Patients With Bradycardia and Cardiac Conduction Delay. J Am Coll Cardiol. 2019;74(7):e51-e156."
    pmid: "30412709"
  - type: review
    ref: "Mancini ME, Diekema DS, Hoadley TA, et al. Part 3: Ethical Issues: 2015 AHA Guidelines Update for CPR and ECC. Circulation. 2015;132(18 Suppl 2):S383-S396."
    pmid: "26472992"
  - type: textbook
    ref: "Roberts JR, Custalow CB, Thomsen TW. Roberts and Hedges' Clinical Procedures in Emergency Medicine and Acute Care, 7th Edition. Elsevier. 2019."
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
# Transcutaneous Pacing

## Recognition

**Indications:**
- Hemodynamically unstable bradycardia (HR < 50 with hypotension, altered mental status, chest pain, acute heart failure) refractory to atropine
- Second-degree AV block Type II (Mobitz II) — high risk of progression to complete heart block
- Third-degree (complete) AV block with hemodynamic instability
- New bifascicular or trifascicular block in the setting of acute MI (especially anterior MI with new LBBB + RBBB + hemiblock)
- Bradyasystolic cardiac arrest (low success rate but bridge to transvenous pacing)
- Overdose-induced bradycardia (beta-blocker, calcium channel blocker, digoxin) refractory to pharmacologic therapy
- Bridge to transvenous pacing in any unstable bradycardia

**Contraindications:**
- Severe hypothermia (< 30 degrees C) — the heart is resistant to electrical stimulation; rewarm first
- Asystolic cardiac arrest > 20 minutes without other interventions (futile)
- Do not delay CPR to set up pacing in arrest — TCP is adjunctive, not primary

**Key Principle:** TCP is a bridge. Plan for transvenous pacing (TVP) as soon as TCP achieves hemodynamic stabilization.

## Critical Actions

| Action | Target |
|--------|--------|
| Pad placement | < 30 seconds |
| Pacing initiated | < 60 seconds from decision |
| Electrical capture confirmed | Within 2 minutes of pacing initiation |
| Hemodynamic response confirmed | Palpable pulse correlating with paced rhythm |
| Transvenous pacing | Within 1-2 hours of TCP initiation |

1. **Apply pacing pads** in anterior-posterior configuration
2. **Set initial rate** to 60-80 bpm
3. **Set initial current output** to maximum (if arrest) or start at 0 mA and increase (if conscious)
4. **Identify electrical capture** on cardiac monitor (wide QRS after each pacing spike)
5. **Confirm mechanical capture** — palpable pulse or arterial waveform correlating with paced complexes
6. **Sedate the patient** — TCP is painful at threshold currents
7. **Arrange transvenous pacing**

## Differential Diagnosis

**Alternative Treatments for Unstable Bradycardia:**

| Treatment | When to Use |
|-----------|------------|
| Atropine 1 mg IV q3-5min (max 3 mg) | First-line for symptomatic bradycardia; ineffective in Mobitz II and complete heart block (infranodal) |
| Dopamine 5-20 mcg/kg/min IV | Chronotropic support; bridge while setting up TCP |
| Epinephrine 2-10 mcg/min IV | Chronotropic and inotropic support; useful in arrest |
| Isoproterenol 2-10 mcg/min IV | Pure chronotrope; risk of hypotension; use if above fail |
| Transvenous pacing | Definitive temporary pacing; more reliable capture; requires procedural expertise |
| Glucagon 3-10 mg IV bolus | Beta-blocker/CCB overdose; followed by 3-5 mg/hr infusion |

## Workup

**Pre-Procedure Assessment:**
- 12-lead ECG: identify rhythm, level of AV block, ischemic changes
- Vital signs with continuous monitoring
- Identify and treat reversible causes: hyperkalemia (calcium, insulin/dextrose, albuterol), hypothermia (active warming), drug toxicity (specific antidotes), acute MI (reperfusion)
- Confirm atropine has been attempted (unless clearly infranodal block)

**Equipment:**

| Item | Specification |
|------|---------------|
| Defibrillator/pacer | With transcutaneous pacing capability (biphasic preferred) |
| Pacing pads | Self-adhesive multifunction pads (NOT standard defibrillation pads on some older devices — confirm pacing capability) |
| Cardiac monitor | Continuous ECG with visible pacing spikes |
| Sedation | Midazolam 1-2 mg IV, fentanyl 25-50 mcg IV, or ketamine 0.5-1 mg/kg IV for conscious patients |
| Backup | Equipment for transvenous pacing if capture fails |

## Treatment

### Pad Placement

**Anterior-Posterior (Preferred):**
- Anterior pad: left parasternal area, V2-V3 position (over the heart)
- Posterior pad: directly behind the anterior pad on the back, between the spine and left scapula
- This configuration provides the most direct current path through the myocardium

**Anterior-Lateral (Alternative):**
- Right pad: right infraclavicular area
- Left pad: left mid-axillary line at level of 5th-6th intercostal space (cardiac apex)
- Used when posterior access is limited (backboard, spinal precautions)

### Initiating Pacing

**In Cardiac Arrest (Bradyasystolic):**
1. Apply pads
2. Set rate to 80 bpm
3. Set output to maximum (typically 200 mA)
4. Activate pacing
5. If capture is achieved, slowly decrease mA until capture is lost — the threshold
6. Set output to 10% above threshold (or 5-10 mA above)
7. Continue CPR between attempts if no capture

**In Conscious Patient with Unstable Bradycardia:**
1. Apply pads
2. Sedate before pacing if hemodynamics allow: midazolam 1-2 mg IV + fentanyl 25-50 mcg IV; or ketamine 0.5-1 mg/kg IV (maintains hemodynamics)
3. Set rate to 60-80 bpm (or 10-20 bpm above intrinsic rate)
4. Start output at 0 mA, increase by 10 mA increments until electrical capture
5. Typical capture threshold: 40-80 mA (higher in obesity, emphysema, pericardial effusion)
6. Set final output 5-10 mA above threshold

### Confirming Capture

**Electrical Capture:**
- Pacing spike followed by wide QRS complex on monitor
- T-wave visible after each QRS
- Consistent 1:1 pacing spike to QRS relationship
- Caution: pacing artifact can mimic QRS — do not rely on monitor alone

**Mechanical Capture (CRITICAL — must confirm):**
- Palpable pulse that correlates with the paced rate (check femoral or carotid — peripheral pulses may be difficult to feel due to muscle contractions)
- Arterial waveform on pulse oximetry or arterial line correlating with paced rate
- Improvement in blood pressure
- Electrical capture without mechanical capture = pacing is ineffective (the heart is not contracting in response to the electrical stimulus — increase output or consider transvenous pacing)

### Pain Management
- TCP causes painful skeletal muscle contractions at therapeutic current levels
- Conscious patients require sedation/analgesia before or immediately after pacing initiation
- Fentanyl 25-50 mcg IV + midazolam 1-2 mg IV
- Ketamine 0.5-1 mg/kg IV (preferred in hypotension — maintains hemodynamics)

### Post-Procedure
- Continuous monitoring: ECG, BP, SpO2, pacing output
- Reassess capture with any patient movement or position change (pad displacement)
- Arrange transvenous pacing within 1-2 hours — TCP is painful, has variable capture, and is a bridge only
- Treat underlying cause of bradycardia concurrently

## Disposition

- **Successful capture with hemodynamic improvement:** ICU admission; cardiology consultation for transvenous pacing
- **Failed capture (no electrical or mechanical capture at maximum output):** continue pharmacologic chronotropic support (dopamine, epinephrine); emergent transvenous pacing; consider causes of pacing failure (lead placement, effusion, electrolyte abnormality)
- **Successful capture but ongoing hemodynamic instability:** transvenous pacing urgently; consider additional vasopressor/inotropic support; investigate concurrent pathology (MI, sepsis, PE)
- **Transfer:** if transvenous pacing unavailable, maintain TCP during transfer; ensure backup defibrillator/pacer and sedation available en route

## Pitfalls

1. **Confirming electrical capture without verifying mechanical capture.** Pacing artifacts on the monitor can be mistaken for QRS complexes. The patient may show electrical spikes without actual myocardial contraction (PEA equivalent). Always confirm mechanical capture with a palpable pulse at the paced rate. Use femoral pulse palpation — skeletal muscle twitching from pacing makes radial pulse assessment unreliable.

2. **Not sedating the conscious patient.** TCP causes painful chest wall muscle contractions at therapeutic current levels (40-80+ mA). Failure to sedate causes patient distress, movement that dislodges pads, and sympathetic surges that worsen hemodynamics. Administer analgesia/sedation before or immediately after initiating pacing.

3. **Using TCP as definitive treatment instead of a bridge.** TCP has unreliable long-term capture, causes significant patient discomfort, and prevents meaningful patient assessment or movement. Arrange transvenous pacing within 1-2 hours. Do not rely on TCP overnight.

4. **Starting at low current output in cardiac arrest.** In bradyasystolic arrest, start at maximum output (200 mA) to achieve capture as fast as possible, then titrate down. Incrementally increasing mA from zero wastes critical time in a patient without perfusion.

5. **Failing to treat the underlying cause of bradycardia.** TCP addresses the rate but not the etiology. Hyperkalemia (calcium + insulin/dextrose), acute MI (reperfusion), drug toxicity (glucagon for beta-blocker, calcium for CCB, digoxin Fab), and hypothermia (rewarming) all require concurrent treatment.

6. **Pad placement too close together or over bone.** Pads placed over the sternum or too close together create a current path that bypasses the myocardium. Optimal anterior-posterior placement ensures the current traverses the heart. Replace pads if capture is not achieved with proper settings.
