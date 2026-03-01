---
id: syncope
condition: "Syncope — Emergency Evaluation"
aliases: [syncope, fainting, passing out, loss of consciousness, LOC, blackout]
icd10: [R55, R55.0]
esi: 2
time_to_harm:
  irreversible_injury: "< 1 hour (cardiac syncope with sustained arrhythmia)"
  death: "< 30 minutes (ventricular arrhythmia, aortic dissection, PE)"
  optimal_intervention_window: "< 60 minutes (identify high-risk cause)"
category: presentations
condition_type: presentation
chief_complaint: "Syncope"
differential_categories:
  - category: life-threatening
    conditions:
      - pulmonary-embolism
      - aortic-dissection
      - cardiac-tamponade
      - stemi
      - ventricular-tachycardia
      - complete-heart-block
      - ruptured-aaa
      - subarachnoid-hemorrhage
      - torsades-de-pointes
      - long-qt-syndrome
      - hypertrophic-cardiomyopathy-emergency
  - category: emergent
    conditions:
      - unstable-bradycardia
      - sick-sinus-syndrome
      - svt
      - hemorrhagic-shock
      - ectopic-pregnancy
      - aortic-transection
      - wpw-syndrome
      - acute-valvular-emergency
  - category: urgent
    conditions:
      - deep-vein-thrombosis
      - pacemaker-malfunction
      - atrial-fibrillation-rvr
  - category: non-emergent
    conditions:
      - benign-palpitations
red_flags:
  - "Syncope during exertion"
  - "Syncope while supine or seated"
  - "Preceding palpitations or chest pain"
  - "Family history of sudden cardiac death < age 50"
  - "Known structural heart disease or cardiomyopathy"
  - "New neurological deficit after event"
  - "Recurrent syncope with minimal prodrome"
  - "Age > 60 with no prodromal symptoms"
  - "Active anticoagulation (risk of traumatic hemorrhage)"
  - "ECG abnormality (prolonged QTc, Brugada pattern, WPW, new bundle branch block)"
decision_rules:
  - name: "San Francisco Syncope Rule (SFSR)"
    citation: "Quinn JV et al. Derivation of the San Francisco Syncope Rule to predict patients with short-term serious outcomes. Ann Emerg Med. 2004;44(3):224-232."
    pmid: "15332063"
  - name: "Canadian Syncope Risk Score"
    citation: "Thiruganasambandamoorthy V et al. Development of the Canadian Syncope Risk Score to predict serious adverse events after emergency department assessment of syncope. CMAJ. 2016;188(12):E289-E298."
    pmid: "27378464"
  - name: "Boston Syncope Rule"
    citation: "Grossman SA et al. A novel approach to predicting 30-day adverse events in emergency department patients with syncope using the Boston Syncope criteria. Acad Emerg Med. 2007;14(5):434-441."
    pmid: "17456554"
track: tier1
sources:
  - type: guideline
    ref: "2017 ACC/AHA/HRS Guideline for the Evaluation and Management of Patients with Syncope"
    doi: "10.1016/j.jacc.2017.03.003"
  - type: guideline
    ref: "2018 ESC Guidelines for the diagnosis and management of syncope. Eur Heart J. 2018;39(21):1883-1948."
    doi: "10.1093/eurheartj/ehy037"
  - type: guideline
    ref: "ACEP Clinical Policy: Critical Issues in the Evaluation and Management of Adult Patients Presenting to the Emergency Department With Syncope. Ann Emerg Med. 2007;49(4):431-444."
    pmid: "17371707"
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
# Syncope — Emergency Evaluation

## Recognition

Syncope accounts for 1-3% of ED visits and 1-6% of hospital admissions. It is defined as transient loss of consciousness due to cerebral hypoperfusion, with rapid onset, short duration, and spontaneous complete recovery. The critical ED task is not to diagnose the specific cause of syncope in most cases, but to risk stratify for life-threatening etiologies.

**Key history elements (obtain from patient AND witnesses):**
- Position at time of event: supine/seated syncope is never vasovagal → high-risk
- Activity: exertional syncope → structural heart disease (HCM, aortic stenosis, ARVD) or arrhythmia
- Prodrome: nausea/warmth/diaphoresis/tunnel vision → vasovagal; sudden without warning → arrhythmic
- Duration of LOC: typically < 30 seconds for syncope. Prolonged → seizure or hemodynamic cause.
- Witnessed seizure activity: brief myoclonic jerks (< 15 seconds) are common in syncope (convulsive syncope) and do NOT indicate epilepsy
- Recovery: rapid and complete → syncope; prolonged confusion → seizure (postictal) or stroke
- Preceding chest pain, palpitations, dyspnea
- Recent medication changes, new antihypertensives, diuretics, QTc-prolonging drugs
- Family history of sudden death, cardiomyopathy, long QT, Brugada

**Etiologic categories:**
- **Cardiac (most dangerous):** arrhythmia (tachy or brady), structural (HCM, AS, tamponade), vascular (PE, aortic dissection, AAA rupture). 10-25% of syncope.
- **Reflex (most common):** vasovagal, situational (cough, micturition, defecation), carotid sinus hypersensitivity. 35-50%.
- **Orthostatic:** volume depletion, autonomic dysfunction, medication-induced. 10-25%.
- **Neurologic (rare as syncope cause):** SAH (typically headache-dominant). True neurologic syncope is uncommon; stroke/TIA rarely cause syncope unless posterior circulation.

## Critical Actions

| Action | Target |
|---|---|
| 12-lead ECG | < 10 minutes from arrival |
| Orthostatic vital signs | Within 15 minutes |
| Fingerstick glucose | < 5 minutes |
| Pregnancy test (women of reproductive age) | < 30 minutes |

**Evaluation algorithm:**

1. **Stabilize.** Assess hemodynamic stability. Persistent hypotension, active bleeding, or ongoing altered mentation → resuscitation bay.

2. **12-lead ECG within 10 minutes.** The single highest-yield test. Look for:
   - QTc prolongation (> 500 ms high risk, > 470 ms men / > 480 ms women warrants concern)
   - Brugada pattern (coved ST elevation V1-V2)
   - WPW (short PR, delta wave)
   - New bundle branch block, bifascicular block, trifascicular block
   - Pathologic Q waves (prior MI → arrhythmia substrate)
   - RV strain pattern (PE)
   - ST elevation or depression (ACS)
   - High-degree AV block, Mobitz II, complete heart block
   - Epsilon waves, T-wave inversions V1-V3 (ARVC)

3. **Determine if syncope was truly syncope.** Rule out seizure (tongue biting, prolonged postictal confusion, witnessed tonic-clonic activity > 30 seconds), stroke (persistent focal deficit), hypoglycemia, trauma with LOC.

4. **Risk stratify.** Apply Canadian Syncope Risk Score or institutional protocol:
   - **High-risk features:** abnormal ECG, cardiac history, exertional, supine/seated onset, preceding palpitations/chest pain, age > 60 without prodrome, family history of sudden death
   - **Low-risk features:** classic vasovagal prodrome, positional (standing to seated), young patient with normal ECG, isolated episode

5. **Orthostatic vitals.** Supine then standing at 1 and 3 minutes. Positive: SBP drop > 20 mmHg or DBP drop > 10 mmHg, or HR increase > 30 bpm.

6. **Targeted exam:**
   - Cardiovascular: murmurs (aortic stenosis, HCM — dynamic outflow obstruction worsens with Valsalva), irregular rhythm, pulse deficits
   - Neurological: focal deficits (stroke), tongue laceration (seizure)
   - Rectal exam: if occult GI bleeding suspected as cause of orthostatic syncope
   - Trauma assessment: head, c-spine, extremities from the fall itself

## Differential Diagnosis

### Life-Threatening
- **Pulmonary embolism** (`pulmonary-embolism`): syncope is the presenting symptom in 10-15% of massive PE. Tachycardia, hypoxia, RV strain on ECG.
- **Aortic dissection** (`aortic-dissection`): syncope from cardiac tamponade, aortic insufficiency, or hypovolemia. Back pain, pulse deficits.
- **Cardiac tamponade** (`cardiac-tamponade`): pulsus paradoxus, JVD, muffled heart tones
- **Acute MI** (`stemi`): inferior STEMI with high-degree AV block commonly presents as syncope
- **Ventricular tachycardia** (`ventricular-tachycardia`): wide-complex tachycardia, history of structural heart disease, prior MI
- **Complete heart block** (`complete-heart-block`): profound bradycardia, cannon A waves, AV dissociation
- **Ruptured AAA** (`ruptured-aaa`): age > 60, abdominal/back pain, pulsatile abdominal mass, hypotension
- **Subarachnoid hemorrhage** (`subarachnoid-hemorrhage`): syncope at onset of thunderclap headache (6-10% present primarily with syncope)
- **Torsades de pointes** (`torsades-de-pointes`): prolonged QTc, characteristic polymorphic VT on telemetry
- **Long QT syndrome** (`long-qt-syndrome`): young patient, exertional syncope, family history of sudden death
- **HCM** (`hypertrophic-cardiomyopathy-emergency`): exertional syncope in young athlete, systolic murmur that increases with Valsalva

### Emergent
- **Unstable bradycardia** (`unstable-bradycardia`): symptomatic bradycardia (HR < 50), pauses, medication-related (beta-blockers, calcium channel blockers, digoxin)
- **Sick sinus syndrome** (`sick-sinus-syndrome`): tachycardia-bradycardia syndrome, elderly
- **SVT** (`svt`): palpitations preceding syncope, abrupt onset/offset
- **Hemorrhagic shock** (`hemorrhagic-shock`): GI bleed, trauma, ruptured ectopic, AAA
- **Ectopic pregnancy** (`ectopic-pregnancy`): reproductive-age female, abdominal pain, vaginal bleeding, positive hCG
- **Aortic transection** (`aortic-transection`): post-deceleration trauma mechanism
- **WPW syndrome** (`wpw-syndrome`): short PR, delta wave, risk of pre-excited AF degenerating to VF
- **Acute valvular emergency** (`acute-valvular-emergency`): acute aortic regurgitation (dissection), mitral chord rupture

### Urgent
- **DVT** (`deep-vein-thrombosis`): as harbinger of PE (unilateral leg swelling + syncope → evaluate for PE)
- **Pacemaker malfunction** (`pacemaker-malfunction`): failure to pace → bradycardic syncope
- **Atrial fibrillation with RVR** (`atrial-fibrillation-rvr`): rapid rate → decreased cardiac output

### Non-Emergent
- **Vasovagal syncope:** prodromal nausea, warmth, diaphoresis, standing position, trigger identified (pain, emotional stress, prolonged standing). Normal ECG. This is a diagnosis of confidence, not exclusion.
- **Orthostatic hypotension:** volume depletion, medications, autonomic neuropathy. Reproducible with orthostatic vitals.
- **Situational syncope:** cough, micturition, defecation, swallowing — clear temporal relationship.
- **Benign palpitations** (`benign-palpitations`): PACs/PVCs without structural heart disease

## Workup

**All patients:**
- 12-lead ECG (mandatory, Level A recommendation per ACEP)
- Orthostatic vital signs
- Point-of-care glucose
- Pregnancy test (all women of reproductive age)
- Continuous cardiac monitoring during ED stay

**Based on clinical suspicion:**
- **Cardiac syncope:** Troponin (if ACS suspected), echocardiography (structural disease), telemetry monitoring
- **PE:** Wells criteria → D-dimer → CTA chest
- **Hemorrhagic cause:** CBC, type and screen, FAST exam, stool guaiac
- **Aortic dissection/AAA:** CTA chest/abdomen/pelvis
- **SAH:** Head CT (without contrast), then LP if CT negative and suspicion persists
- **Metabolic:** BMP (electrolytes, renal function), glucose

**What NOT to order routinely:**
- Head CT: not indicated for simple syncope without head trauma, focal deficit, or headache (ACEP Choosing Wisely)
- EEG: syncope is NOT seizure — myoclonic jerks during syncope are cerebral hypoperfusion, not epilepsy
- Carotid ultrasound: carotid stenosis does not cause syncope (bilateral total occlusion required to impair consciousness)
- MRI brain: not indicated unless posterior circulation stroke suspected (vertigo, diplopia, ataxia + syncope)

## Treatment

Treatment is cause-specific. Stabilization measures:

- **IV access** with NS bolus 500 mL-1 L for orthostatic hypotension/volume depletion
- **Continuous telemetry** for all patients during ED evaluation
- **Transcutaneous pacing** pads placed for high-degree AV block or symptomatic bradycardia (see `transcutaneous-pacing`)
- **Atropine 0.5 mg IV** for symptomatic bradycardia (may repeat q3-5min, max 3 mg)
- **Cardioversion/defibrillation** for sustained VT with hemodynamic compromise (see `cardioversion-defibrillation`)
- **IV magnesium 2 g over 10 minutes** for torsades de pointes
- **Hold offending medications:** antihypertensives, beta-blockers, CCBs, QTc-prolonging drugs
- Defer to specific condition entries for definitive management

## Disposition

- **ICU/CCU:** Sustained VT, high-degree AV block requiring pacing, massive PE, aortic dissection, cardiac tamponade, hemodynamic instability
- **Telemetry admission:** Abnormal ECG, suspected cardiac syncope, structural heart disease, exertional syncope, recurrent syncope without diagnosis
- **Observation:** First syncope in patient > 60 with no high-risk features, pending echocardiography and monitoring
- **Discharge with close follow-up (24-72 hours):**
  - Classic vasovagal with clear trigger AND normal ECG AND age < 60
  - Orthostatic with identifiable reversible cause (medication, dehydration) AND resolved with fluids/medication adjustment
  - Isolated episode with no high-risk features
  - Arrange cardiology follow-up if any concern for cardiac etiology, even if low-risk
- **Avoid discharge if:** syncope during exertion, syncope supine, family history of sudden death, abnormal ECG, structural heart disease, recurrent without prodrome

## Pitfalls

1. **Reflexively ordering head CT for syncope without neurological findings.** Syncope is cerebral hypoperfusion, not a structural brain problem. Head CT without focal deficit, headache, or trauma from the fall is low-yield and delays the real workup (ECG, telemetry, cardiac evaluation).

2. **Mistaking convulsive syncope for a seizure.** Brief myoclonic jerks (< 15 seconds) during syncope are caused by cerebral hypoperfusion, not epileptic activity. Tongue laceration (tip, not lateral), urinary incontinence, and brief jerks do NOT confirm seizure. Lateral tongue biting and prolonged (> 30 second) tonic-clonic activity favor seizure.

3. **Dismissing syncope in young athletes as vasovagal.** Exertional syncope in a young person requires evaluation for HCM, long QT, ARVC, anomalous coronary arteries, and commotio cordis. Family history of sudden death < 50 is an absolute red flag.

4. **Failing to consider ruptured ectopic pregnancy.** Every female of reproductive age presenting with syncope requires a pregnancy test. Ruptured ectopic can present as syncope with minimal or no abdominal pain.

5. **Over-reliance on the San Francisco Syncope Rule.** The SFSR has been inconsistently validated externally. No single clinical decision rule for syncope is sensitive enough to use as the sole basis for discharge. Combine clinical judgment with structured risk assessment.

6. **Missing posterior circulation stroke presenting as syncope.** While anterior circulation stroke rarely causes syncope, basilar artery occlusion can present with syncope plus vertigo, diplopia, ataxia, or cranial nerve deficits. Perform a thorough neurological exam.

7. **Attributing syncope to "dehydration" without evaluating for hemorrhage.** Occult GI bleeding (melena, positive guaiac), ruptured AAA, and ruptured ectopic all cause syncope through hypovolemia. Check hemoglobin, perform rectal exam if indicated.

8. **Failure to review medication list for QTc-prolonging drugs.** Many common medications prolong QTc (fluoroquinolones, ondansetron, antipsychotics, methadone). Drug-induced torsades is a preventable cause of syncope and sudden death.
