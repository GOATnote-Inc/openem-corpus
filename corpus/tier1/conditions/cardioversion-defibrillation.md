---
id: cardioversion-defibrillation
condition: Cardioversion and Defibrillation
aliases: [synchronized cardioversion, electrical cardioversion, DCCV, defibrillation, shock]
icd10: [I49.01, I48.0, I48.1, I47.1, I47.2]
esi: 1
time_to_harm:
  irreversible_injury: "< 4 minutes (anoxic brain injury in VF/pVT arrest)"
  death: "< 10 minutes in VF/pVT without defibrillation"
  optimal_intervention_window: "< 3 minutes from VF onset; survival decreases 7-10% per minute"
mortality_if_delayed: "VF survival decreases 7-10% per minute without defibrillation; beyond 10 minutes, survival < 5%"
category: procedural
track: tier1
sources:
  - type: guideline
    ref: "Panchal AR, Bartos JA, Cabanas JG, et al. Part 3: Adult Basic and Advanced Life Support: 2020 AHA Guidelines for CPR and ECC. Circulation. 2020;142(16_suppl_2):S366-S468."
    pmid: "33081529"
  - type: guideline
    ref: "Link MS, Berkow LC, Kudenchuk PJ, et al. Part 7: Adult Advanced Cardiovascular Life Support: 2015 AHA Guidelines Update for CPR and ECC. Circulation. 2015;132(18 Suppl 2):S444-S464."
    pmid: "26472995"
  - type: pubmed
    ref: "Stiell IG, Walker RG, Nesbitt LP, et al. BIPHASIC Trial: a randomized comparison of fixed lower versus escalating higher energy levels for defibrillation in out-of-hospital cardiac arrest. Circulation. 2007;115(12):1511-1517."
    pmid: "17353444"
  - type: guideline
    ref: "January CT, Wann LS, Calkins H, et al. 2019 AHA/ACC/HRS Focused Update of the 2014 Guideline for the Management of Patients With Atrial Fibrillation. J Am Coll Cardiol. 2019;74(1):104-132."
    pmid: "30703431"
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
# Cardioversion and Defibrillation

## Recognition

**Defibrillation (Unsynchronized Shock) — Indications:**
- Ventricular fibrillation (VF)
- Pulseless ventricular tachycardia (pVT)
- Polymorphic VT (even with pulse — treat as VF)
- VF/pVT cardiac arrest — defibrillation is THE definitive treatment; every second of delay reduces survival

**Synchronized Cardioversion — Indications:**
- Unstable supraventricular tachycardia (SVT) with hemodynamic compromise (hypotension, AMS, chest pain, acute HF)
- Unstable atrial fibrillation or atrial flutter with rapid ventricular response
- Unstable monomorphic ventricular tachycardia with pulse
- Elective cardioversion of atrial fibrillation/flutter (after anticoagulation assessment)

**Hemodynamic Instability Requiring Immediate Cardioversion:**
- SBP < 90 mmHg
- Altered mental status
- Acute pulmonary edema
- Ongoing chest pain with ischemic changes
- Signs of shock (cool extremities, mottled skin, poor perfusion)

**Contraindications:**
- Digitalis toxicity with atrial fibrillation: cardioversion may induce refractory VF; treat with digoxin-specific Fab fragments first
- Multifocal atrial tachycardia (MAT): not amenable to cardioversion; treat underlying cause (COPD, hypomagnesemia)
- Sinus tachycardia: not a primary arrhythmia — treat the cause (pain, hypovolemia, fever, PE)

## Critical Actions

| Action | Target |
|--------|--------|
| Defibrillation in VF/pVT | < 3 minutes from arrest recognition |
| Shock delivery (synchronized) | < 10 minutes from decision in unstable tachycardia |
| Rhythm reassessment | Immediately after shock, then 2 min if in arrest |
| Post-shock CPR (arrest) | Resume immediately for 2 minutes before rhythm check |

**Defibrillation Protocol (VF/pVT Arrest):**
1. Recognize VF/pVT on monitor
2. Charge defibrillator during CPR — minimize hands-off time
3. Clear patient, deliver shock
4. Resume CPR immediately for 2 minutes (do NOT pause to check rhythm)
5. Recheck rhythm after 2-minute CPR cycle
6. Repeat shock if still VF/pVT; escalate energy if available

**Synchronized Cardioversion Protocol (Unstable Tachycardia with Pulse):**
1. Attach monitoring, establish IV access
2. Sedate if hemodynamics allow (see medications below)
3. Select "SYNC" mode on defibrillator
4. Select appropriate energy
5. Confirm sync markers on R-waves on screen
6. Clear patient, hold "shock" button (may have brief delay as device waits for R-wave)
7. If unsuccessful, increase energy and repeat
8. If rhythm degenerates to VF: turn OFF sync, defibrillate at full energy

## Differential Diagnosis

**Alternative Treatments by Rhythm:**

| Rhythm | Stable | Unstable |
|--------|--------|----------|
| SVT | Vagal maneuvers → adenosine 6 mg → 12 mg IV | Synchronized cardioversion |
| Atrial fibrillation (RVR) | Rate control (diltiazem, metoprolol) | Synchronized cardioversion |
| Atrial flutter | Rate control → elective cardioversion | Synchronized cardioversion |
| Monomorphic VT (with pulse) | Amiodarone 150 mg IV over 10 min; procainamide 20-50 mg/min | Synchronized cardioversion |
| Polymorphic VT (with pulse) | Treat as VF → unsynchronized defibrillation | Unsynchronized defibrillation |
| Torsades de pointes | Magnesium 2 g IV; isoproterenol; overdrive pacing | Unsynchronized defibrillation |

## Workup

**Pre-Procedure Assessment:**
- Identify rhythm on 12-lead ECG (if time permits in unstable patients) or monitor strip
- Determine stability: BP, mental status, signs of hypoperfusion
- For elective AF cardioversion: confirm anticoagulation status (>= 3 weeks therapeutic anticoagulation OR TEE showing no left atrial thrombus)
- Check electrolytes: K+, Mg2+ (correct hypokalemia and hypomagnesemia before elective cardioversion)

**Equipment:**

| Item | Specification |
|------|---------------|
| Defibrillator | Biphasic preferred; with sync capability |
| Pads | Self-adhesive defibrillation pads (anterior-lateral or anterior-posterior) |
| Airway equipment | BVM, suction, intubation supplies (sedation may cause apnea) |
| IV access | Functional IV line for medication administration |
| Monitoring | Continuous ECG, SpO2, BP, ETCO2 |
| Sedation medications | See below |
| Resuscitation medications | Epinephrine, amiodarone, lidocaine (for arrest) |

## Treatment

### Energy Levels — Biphasic Defibrillator

**Defibrillation (Unsynchronized):**

| Rhythm | First Shock | Subsequent Shocks |
|--------|------------|-------------------|
| VF / pVT | 120-200 J (device-specific; if unknown, use maximum) | Escalating or maximum energy |
| Polymorphic VT | 120-200 J (treat as VF) | Escalating or maximum energy |

**Synchronized Cardioversion:**

| Rhythm | Initial Energy | Escalation |
|--------|---------------|------------|
| Narrow-complex SVT | 50-100 J | 100 → 200 → 300 → 360 J |
| Atrial flutter | 50-100 J | 100 → 200 → 300 J |
| Atrial fibrillation | 120-200 J | 200 → 300 → 360 J |
| Monomorphic VT | 100 J | 200 → 300 → 360 J |

**Monophasic Defibrillator (if biphasic unavailable):**
- VF/pVT: 360 J for all shocks
- Synchronized cardioversion: same progression but generally higher starting energies

### Pad Placement

**Anterior-Lateral (Standard):**
- Right pad: right infraclavicular area below the clavicle
- Left pad: left mid-axillary line, 5th-6th intercostal space (lateral to the nipple)

**Anterior-Posterior:**
- Anterior: left parasternal, V2-V3 position
- Posterior: left infrascapular area
- May provide superior current delivery for cardioversion, especially in obese patients

### Sedation for Cardioversion (Elective or Unstable with Adequate Time)

| Agent | Dose | Onset | Notes |
|-------|------|-------|-------|
| Propofol | 0.5-1 mg/kg IV | 30 sec | Shortest recovery; hypotension risk |
| Etomidate | 0.1-0.2 mg/kg IV | 30 sec | Hemodynamically neutral; myoclonus |
| Midazolam | 0.05-0.1 mg/kg IV | 1-2 min | Longer recovery; amnestic |
| Ketamine | 1-1.5 mg/kg IV | 1 min | Hemodynamically stable; emergence reactions |
| Fentanyl | 1 mcg/kg IV | 2-3 min | Added for analgesia; combine with sedative |

**In hemodynamically unstable patients:** do NOT delay cardioversion for sedation. Shock first, sedate after if needed.

### Procedure

**Defibrillation:**
1. Continue CPR while defibrillator charges
2. Ensure sync mode is OFF
3. Announce "Charging" → "I am clear, you are clear, everybody is clear"
4. Confirm no one touching patient or bed
5. Deliver shock
6. Resume CPR immediately for 2 minutes

**Synchronized Cardioversion:**
1. Press SYNC button — confirm sync markers (small triangles or arrows) appear on each R-wave
2. Select energy level
3. Charge
4. Clear patient
5. Press and HOLD shock button (device waits for next R-wave to deliver)
6. NOTE: many defibrillators reset sync mode after each shock — must re-enable SYNC for each subsequent attempt
7. If rhythm changes to VF during cardioversion: turn off sync, defibrillate at full energy

### Post-Shock Management

**After Successful Defibrillation (ROSC):**
- Post-cardiac arrest care protocol
- 12-lead ECG, continuous monitoring
- Targeted temperature management (TTM)
- Coronary angiography if STEMI or suspected cardiac etiology
- Amiodarone 150 mg IV over 10 min then 1 mg/min x 6 hr then 0.5 mg/min x 18 hr (for recurrent VF/pVT)

**After Successful Cardioversion:**
- Monitor for at least 1-2 hours
- 12-lead ECG post-cardioversion to confirm rhythm
- Anticoagulation assessment for atrial fibrillation (CHADS2-VASc score)
- Antiarrhythmic if recurrence anticipated (amiodarone, flecainide, sotalol per cardiologist)

## Disposition

- **VF/pVT arrest with ROSC:** ICU admission; post-cardiac arrest care; cardiology consultation
- **Successful cardioversion for unstable SVT/AF:** observation 2-4 hours minimum; discharge if stable, no recurrence, and underlying cause treated
- **Recurrent VF/pVT despite multiple shocks:** continue ACLS; amiodarone/lidocaine; consider double sequential defibrillation; emergent cardiology/EP consultation
- **Failed cardioversion for AF:** rate control strategy; cardiology consultation; anticoagulation
- **Transfer:** stabilize and transfer with defibrillator, continuous monitoring, and ACLS medications

## Pitfalls

1. **Using synchronized mode for VF or polymorphic VT.** Sync mode searches for an R-wave to time the shock. In VF, there are no organized R-waves — the defibrillator will not discharge. Polymorphic VT has irregular morphology that may confuse sync algorithms. Both rhythms require UNSYNCHRONIZED defibrillation.

2. **Forgetting to re-activate sync mode between cardioversion shocks.** Most defibrillators automatically reset to unsynchronized mode after each shock delivery. If sync is not re-enabled, the next "cardioversion" is actually an unsynchronized shock, risking R-on-T VF.

3. **Delaying defibrillation for IV access, intubation, or medications.** In witnessed VF arrest, early defibrillation is the single most important intervention. Every minute of delay reduces survival by 7-10%. Shock first, establish access second. Do not delay defibrillation for epinephrine or amiodarone.

4. **Cardioverting atrial fibrillation without anticoagulation assessment.** Elective cardioversion of AF present > 48 hours (or unknown duration) without >= 3 weeks of therapeutic anticoagulation or a negative TEE carries a 5-7% risk of thromboembolic stroke. In hemodynamic emergency, cardiovert regardless — but be aware of the risk.

5. **Stopping CPR to "let the shock work."** Immediate resumption of CPR after defibrillation is essential — the post-shock heart often has organized electrical activity but not yet effective mechanical function. Two minutes of CPR after each shock allows the stunned myocardium to recover before rhythm recheck.

6. **Using inadequate energy for atrial fibrillation cardioversion.** AF has a higher defibrillation threshold than SVT or flutter. Starting at 50 J for AF frequently fails. Begin at 120-200 J biphasic for AF. Subtherapeutic shocks waste time and worsen patient discomfort.

7. **Shocking sinus tachycardia.** Sinus tachycardia is a physiologic response, not a primary arrhythmia. Cardioversion will not correct it and may cause harm. Identify and treat the underlying cause (hypovolemia, pain, fever, PE, sepsis).
