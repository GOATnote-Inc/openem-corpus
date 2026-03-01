---
id: palpitations-evaluation
condition: "Palpitations — Emergency Evaluation"
aliases: [palpitations, heart racing, heart pounding, heart fluttering, irregular heartbeat, skipped beats]
icd10: [R00.2, R00.0, R00.1]
esi: 3
time_to_harm:
  irreversible_injury: "< 30 minutes (VT degenerating to VF)"
  death: "< 10 minutes (ventricular fibrillation, pre-excited AF in WPW)"
  optimal_intervention_window: "< 60 minutes (identify and treat hemodynamically significant arrhythmia)"
category: presentations
condition_type: presentation
chief_complaint: "Palpitations"
differential_categories:
  - category: life-threatening
    conditions:
      - ventricular-tachycardia
      - torsades-de-pointes
      - long-qt-syndrome
      - wpw-syndrome
      - stemi
      - pulmonary-embolism
      - cardiac-tamponade
      - hypertrophic-cardiomyopathy-emergency
  - category: emergent
    conditions:
      - atrial-fibrillation-rvr
      - svt
      - unstable-bradycardia
      - complete-heart-block
      - sick-sinus-syndrome
      - thyroid-storm
      - acute-heart-failure
      - pheochromocytoma-crisis
      - anaphylaxis
  - category: urgent
    conditions:
      - acute-coronary-syndrome-nstemi
      - hyperkalemia
      - hypoglycemia
      - sympathomimetic-toxidrome
      - serotonin-syndrome
  - category: non-emergent
    conditions:
      - benign-palpitations
      - panic-attack
red_flags:
  - "Hemodynamic instability (hypotension, altered mental status)"
  - "Syncope or near-syncope with palpitations"
  - "Chest pain with palpitations"
  - "Wide-complex tachycardia on ECG"
  - "Known structural heart disease"
  - "Family history of sudden cardiac death < 50"
  - "Palpitations with exertion"
  - "Irregular irregular rhythm with HR > 150 (AF with RVR)"
  - "History of WPW or prior SVT"
  - "New heart failure symptoms (dyspnea, edema, orthopnea)"
  - "Drug use (cocaine, amphetamines, energy drinks)"
decision_rules:
  - name: "Brugada Criteria (Wide-Complex Tachycardia)"
    citation: "Brugada P et al. A new approach to the differential diagnosis of a regular tachycardia with a wide QRS complex. Circulation. 1991;83(5):1649-1659."
    pmid: "2022022"
  - name: "CHA2DS2-VASc Score (AF Stroke Risk)"
    citation: "Lip GY et al. Refining clinical risk stratification for predicting stroke and thromboembolism in atrial fibrillation using a novel risk factor-based approach: the Euro Heart Survey on Atrial Fibrillation. Chest. 2010;137(2):263-272."
    pmid: "19762550"
track: tier1
sources:
  - type: guideline
    ref: "2023 ACC/AHA/ACCP/HRS Guideline for Diagnosis and Management of Atrial Fibrillation"
    doi: "10.1161/CIR.0000000000001193"
  - type: guideline
    ref: "2015 ACC/AHA/HRS Guideline for the Management of Adult Patients With Supraventricular Tachycardia"
    doi: "10.1016/j.jacc.2015.08.856"
  - type: guideline
    ref: "2017 AHA/ACC/HRS Guideline for Management of Patients With Ventricular Arrhythmias and the Prevention of Sudden Cardiac Death"
    doi: "10.1016/j.jacc.2017.10.054"
  - type: pubmed
    ref: "Raviele A et al. Management of patients with palpitations: a position paper from the European Heart Rhythm Association. Europace. 2011;13(7):920-934."
    pmid: "21697315"
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
# Palpitations — Emergency Evaluation

## Recognition

Palpitations account for approximately 1-2% of ED visits. The majority (85-90%) are benign (PACs, PVCs, sinus tachycardia, anxiety). However, 10-15% have a cardiac arrhythmia, and a subset of these are life-threatening. The ED task is to capture the rhythm during symptoms, identify high-risk features, and distinguish benign from dangerous causes.

**Patient description mapping:**
- "Skipped beats" or "flip-flops" → PACs/PVCs (most common)
- "Racing" or "pounding" with sudden onset/offset → SVT, AF, VT
- "Fluttering" → AF, atrial flutter, SVT
- "Regular rapid" → SVT, VT, sinus tachycardia
- "Irregular" → AF, multifocal atrial tachycardia, frequent PACs

**Key history elements:**
- Onset and offset: sudden (SVT, VT, AF paroxysm) vs gradual (sinus tachycardia, anxiety)
- Duration: seconds (PACs/PVCs), minutes-hours (SVT, AF), persistent (sinus tachycardia)
- Triggers: caffeine, alcohol, exercise, dehydration, stress, medications
- Associated symptoms: syncope/near-syncope (hemodynamic compromise → VT, SVT, high-degree block), chest pain (ACS, SVT with demand ischemia), dyspnea (AF with RVR, PE, HF)
- Prior episodes: recurrent paroxysmal palpitations with sudden termination by vagal maneuvers = SVT
- Structural heart disease: prior MI, HF, cardiomyopathy, valvular disease → VT risk
- Family history: sudden death, cardiomyopathy, long QT, Brugada, HCM
- Medications: digoxin, QTc-prolonging drugs, stimulants, decongestants, herbal supplements
- Substances: cocaine, amphetamines, energy drinks, alcohol, cannabis

**Physical exam during symptoms:**
- Rapid regular rhythm → SVT or VT
- Irregularly irregular → AF
- Cannon A waves in JVP → AV dissociation (VT or complete heart block)
- Systolic murmur worsening with Valsalva → HCM
- Thyromegaly, tremor, exophthalmos → hyperthyroidism

## Critical Actions

| Action | Target |
|---|---|
| 12-lead ECG (during symptoms if possible) | < 10 minutes |
| Continuous cardiac monitoring | Immediate |
| Assess hemodynamic stability | < 2 minutes |
| Synchronized cardioversion if unstable tachyarrhythmia | Immediate |

**Evaluation algorithm:**

1. **12-lead ECG immediately.** The ECG during symptoms is the most valuable test. If symptoms have resolved, the resting ECG still provides critical information (WPW, Brugada, long QT, prior MI, LVH).

2. **Assess hemodynamic stability.** Unstable (hypotension, altered consciousness, severe chest pain, acute HF) → immediate treatment regardless of rhythm diagnosis:
   - Wide-complex tachycardia, unstable → synchronized cardioversion 100-200J biphasic
   - Narrow-complex tachycardia, unstable → synchronized cardioversion 50-100J biphasic
   - Symptomatic bradycardia → atropine 0.5 mg IV → transcutaneous pacing

3. **Categorize the rhythm:**

   **Wide-complex tachycardia (QRS > 120 ms):**
   - Assume VT until proven otherwise (correct > 80% of the time)
   - Apply Brugada criteria for WCT differentiation: absence of RS in all precordial leads, RS interval > 100 ms, AV dissociation, morphology criteria → all favor VT
   - VT treatment: amiodarone 150 mg IV over 10 min, or procainamide 20-50 mg/min IV (max 17 mg/kg), or synchronized cardioversion
   - Do NOT give adenosine to undifferentiated WCT (may cause degeneration of pre-excited AF in WPW to VF)
   - Do NOT give verapamil/diltiazem to WCT (may cause cardiovascular collapse in VT)
   - Irregular WCT → pre-excited AF (WPW) → procainamide or cardioversion. NEVER AV nodal blockers (adenosine, diltiazem, verapamil, digoxin, beta-blockers) → can cause VF

   **Narrow-complex tachycardia (QRS <= 120 ms):**
   - Regular → SVT: vagal maneuvers (modified Valsalva with leg elevation) → adenosine 6 mg rapid IV push with flush → adenosine 12 mg → rate control or cardioversion
   - Irregular → AF with RVR: rate control (diltiazem 0.25 mg/kg IV over 2 min, or metoprolol 5 mg IV q5min x 3) if > 48 hours or unknown duration with adequate anticoagulation. Cardioversion if < 48 hours or hemodynamically unstable.

4. **If symptoms have resolved and ECG is normal:**
   - Review for WPW (short PR < 120 ms, delta wave, wide QRS)
   - Review for Brugada pattern (coved ST elevation V1-V3)
   - Review for long QT (QTc > 500 ms is high risk)
   - Review for HCM markers (LVH, deep septal Q waves)
   - Review for prior MI (pathologic Q waves — arrhythmia substrate)

5. **Extended monitoring** if ECG non-diagnostic and symptoms concerning: 4-6 hours of telemetry monitoring in ED or observation unit.

## Differential Diagnosis

### Life-Threatening
- **Ventricular tachycardia** (`ventricular-tachycardia`): wide-complex tachycardia, structural heart disease, AV dissociation, capture/fusion beats. Monomorphic VT or polymorphic VT.
- **Torsades de pointes** (`torsades-de-pointes`): polymorphic VT with prolonged QTc baseline, "twisting of the points" morphology. Treat with IV magnesium 2 g, isoproterenol, or overdrive pacing.
- **Long QT syndrome** (`long-qt-syndrome`): congenital or acquired (drug-induced), risk of torsades and sudden death. QTc > 500 ms high risk.
- **WPW with pre-excited AF** (`wpw-syndrome`): irregular WCT with varying QRS morphology. AV nodal blockers are CONTRAINDICATED → VF. Procainamide or cardioversion.
- **STEMI** (`stemi`): palpitations from arrhythmia (VT, AF, heart block) as presenting feature of acute MI. Always obtain ECG looking for ST changes.
- **Pulmonary embolism** (`pulmonary-embolism`): sinus tachycardia or AF as presenting rhythm, palpitations with dyspnea/pleuritic pain
- **Cardiac tamponade** (`cardiac-tamponade`): tachycardia with hypotension, pulsus paradoxus
- **HCM** (`hypertrophic-cardiomyopathy-emergency`): exertional palpitations/syncope, young patient, systolic murmur. Risk of VT/VF and sudden death.

### Emergent
- **AF with RVR** (`atrial-fibrillation-rvr`): irregularly irregular, HR > 150, may precipitate HF, demand ischemia
- **SVT** (`svt`): regular narrow-complex tachycardia, HR 150-250, abrupt onset/offset. AVNRT most common.
- **Unstable bradycardia** (`unstable-bradycardia`): patient may perceive compensatory beats as palpitations
- **Complete heart block** (`complete-heart-block`): slow ventricular rate, AV dissociation, may perceive escape beats as palpitations
- **Sick sinus syndrome** (`sick-sinus-syndrome`): tachycardia-bradycardia alternation
- **Thyroid storm** (`thyroid-storm`): AF or sinus tachycardia with thyrotoxicosis, tremor, heat intolerance, weight loss
- **Acute heart failure** (`acute-heart-failure`): tachyarrhythmia precipitating or caused by decompensated HF
- **Pheochromocytoma crisis** (`pheochromocytoma-crisis`): episodic palpitations, hypertension, diaphoresis, headache
- **Anaphylaxis** (`anaphylaxis`): tachycardia with urticaria, wheezing, hypotension, exposure history

### Urgent
- **ACS** (`acute-coronary-syndrome-nstemi`): palpitations as anginal equivalent, arrhythmia from ischemia
- **Hyperkalemia** (`hyperkalemia`): bradycardia, peaked T waves, widened QRS → sine wave → arrest
- **Hypoglycemia** (`hypoglycemia`): adrenergic symptoms (palpitations, diaphoresis, tremor) from hypoglycemia
- **Sympathomimetic toxidrome** (`sympathomimetic-toxidrome`): cocaine, amphetamines causing tachycardia, hypertension, agitation
- **Serotonin syndrome** (`serotonin-syndrome`): tachycardia, clonus, agitation, hyperthermia

### Non-Emergent
- **Benign palpitations** (`benign-palpitations`): PACs, PVCs, sinus tachycardia from caffeine/dehydration/stress. Normal ECG, normal labs, no structural heart disease. Most common etiology.
- **Panic attack** (`panic-attack`): palpitations with anxiety, hyperventilation, paresthesias, sense of doom. Diagnosis of exclusion after cardiac evaluation.
- **Sinus tachycardia:** physiologic response to pain, fever, dehydration, anemia, anxiety, medications. Treat underlying cause.
- **Mitral valve prolapse:** mid-systolic click, late systolic murmur. Rarely causes clinically significant arrhythmia.

## Workup

**All patients:**
- 12-lead ECG (during symptoms if possible — this is the single most important test)
- Continuous cardiac monitoring for minimum 2-4 hours
- BMP (potassium, calcium, magnesium)
- CBC (anemia)
- TSH (if new-onset AF or clinical features of thyrotoxicosis)
- Troponin (if chest pain, dyspnea, or high-risk features)

**Based on clinical suspicion:**
- **Structural heart disease:** Echocardiography (HCM, valvular disease, LV function, wall motion)
- **PE:** Wells score → D-dimer → CTA
- **Toxicology:** UDS, specific drug levels
- **Electrophysiology referral:** WPW on resting ECG, recurrent SVT, unexplained syncope with palpitations, family history of sudden death
- **Extended monitoring (outpatient):** Holter monitor (24-48h), event recorder, or implantable loop recorder for infrequent but concerning symptoms

**What NOT to order:**
- Routine echocardiography for isolated palpitations with normal ECG and no risk factors (low yield)
- Stress testing in the ED for palpitations without ACS features
- Thyroid function tests if no clinical features of thyroid disease and known rhythm

## Treatment

Treatment is rhythm-specific:

- **SVT:** Modified Valsalva (blow against closed glottis for 15 seconds, then lie supine with legs elevated 45 degrees for 15 seconds) → adenosine 6 mg rapid IV push with 20 mL NS flush at antecubital or higher → adenosine 12 mg → cardioversion 50-100J if hemodynamically unstable
- **AF with RVR:** Rate control: diltiazem 0.25 mg/kg IV (max 20 mg) over 2 min, repeat 0.35 mg/kg if needed → infusion 5-15 mg/hr. OR metoprolol 5 mg IV q5min x 3. Avoid if decompensated HF → use amiodarone 150 mg IV over 10 min.
- **VT (stable):** Amiodarone 150 mg IV over 10 min → 1 mg/min infusion x 6h → 0.5 mg/min x 18h. OR procainamide 20-50 mg/min (max 17 mg/kg). Monitor QRS and BP.
- **VT (unstable):** Synchronized cardioversion 100-200J biphasic
- **Torsades:** Magnesium sulfate 2 g IV over 10 min. Isoproterenol infusion or overdrive pacing if refractory. Correct underlying QTc prolongation.
- **Pre-excited AF (WPW):** Procainamide 20-50 mg/min IV OR cardioversion. NEVER adenosine, diltiazem, beta-blockers, or digoxin.
- **Benign PVCs/PACs:** Reassurance. Reduce caffeine, alcohol, decongestants. Outpatient cardiology if frequent/symptomatic.
- **Sinus tachycardia:** Treat underlying cause (pain, fever, dehydration, anemia, PE, sepsis). Do NOT give beta-blockers to treat physiologic sinus tachycardia without identifying the cause.

## Disposition

- **ICU/CCU:** VT requiring ongoing antiarrhythmic infusion, recurrent VT/VF, pre-excited AF, new AF with hemodynamic instability, acute MI with arrhythmia
- **Telemetry:** New AF requiring rate control, SVT requiring observation post-conversion, bradyarrhythmia, palpitations with syncope and non-diagnostic workup
- **Observation (4-8 hours):** Resolved SVT post-adenosine, palpitations with borderline ECG findings, extended monitoring for infrequent symptoms
- **Discharge with follow-up:**
  - Isolated PACs/PVCs with normal ECG and no high-risk features
  - SVT converted with vagal maneuvers or adenosine, hemodynamically stable, no recurrence during observation
  - Sinus tachycardia with identified and treated cause (dehydration, caffeine)
  - Follow-up: cardiology referral if recurrent SVT, WPW on baseline ECG, family history of sudden death, syncope with palpitations, structural heart disease
  - Outpatient Holter/event monitor if symptoms infrequent and undiagnosed

## Pitfalls

1. **Treating wide-complex tachycardia as SVT with aberrancy.** In the ED, wide-complex tachycardia is VT until proven otherwise. Giving verapamil or diltiazem to VT can cause cardiovascular collapse. When in doubt, treat as VT.

2. **Giving AV nodal blockers in pre-excited AF (WPW).** Adenosine, diltiazem, verapamil, beta-blockers, and digoxin are ALL contraindicated in pre-excited AF. They block the AV node while allowing conduction down the accessory pathway → ventricular fibrillation. Use procainamide or cardioversion.

3. **Discharging a patient with WPW on resting ECG without electrophysiology referral.** WPW carries risk of sudden death from pre-excited AF degenerating to VF. All patients with WPW on ECG require electrophysiology evaluation for ablation, regardless of symptom severity.

4. **Diagnosing "anxiety" without ECG.** Palpitations are a cardinal feature of both SVT and panic attacks. An ECG during symptoms distinguishes them. If the arrhythmia has terminated, the resting ECG may still show WPW, long QT, or prior MI patterns. Never diagnose anxiety-related palpitations without a normal ECG.

5. **Missing PE presenting as palpitations.** PE commonly presents with sinus tachycardia or new AF. Palpitations with dyspnea, pleuritic pain, or risk factors for VTE should prompt PE evaluation.

6. **Ignoring family history of sudden death.** Family history of sudden cardiac death < 50 years old suggests inherited arrhythmia syndrome (long QT, Brugada, HCM, ARVC). These patients need cardiology/electrophysiology referral and ECG screening of family members.

7. **Not monitoring long enough.** Paroxysmal arrhythmias may not recur during a brief ED visit. If the clinical story is concerning (palpitations with syncope, exertional palpitations, structural heart disease) but the ECG is normal, 4-8 hours of monitoring or admission for telemetry is appropriate.
