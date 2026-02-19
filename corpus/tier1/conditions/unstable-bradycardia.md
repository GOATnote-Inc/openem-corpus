---
id: unstable-bradycardia
condition: Unstable Bradycardia
aliases: [symptomatic bradycardia, unstable bradycardia, hemodynamically significant bradycardia, high-degree AV block, complete heart block, third-degree AV block]
icd10: [R00.1, I44.1, I44.2, I45.9, I49.5]
esi: 1
time_to_harm: "< 10 minutes"
mortality_if_delayed: "Cardiac arrest imminent if perfusing rhythm not restored"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2020 AHA/ACC Guideline for Management of Patients With Bradycardia and Cardiac Conduction Delay"
    doi: "10.1161/CIR.0000000000000628"
  - type: guideline
    ref: "2020 AHA ACLS Guidelines: Bradycardia Algorithm"
  - type: guideline
    ref: "2015 AHA Guidelines Update for CPR and Emergency Cardiovascular Care: Part 7 — Adult Advanced Cardiovascular Life Support"
    doi: "10.1161/CIR.0000000000000261"
  - type: pubmed
    ref: "Kusumoto FM, et al. 2018 ACC/AHA/HRS Guideline on the Evaluation and Management of Patients With Bradycardia and Cardiac Conduction Delay"
    pmid: "30412709"
    doi: "10.1161/CIR.0000000000000628"
  - type: review
    ref: "Sidhu S, Marine JE. Evaluating and managing bradycardia. Trends Cardiovasc Med. 2020;30(5):265-272"
    pmid: "31311698"
last_updated: "2026-02-18"
compiled_by: agent
reviewed_by: null
verification:
  pmids_verified: "2026-02-18"
  audit_completed: "2026-02-18"
  dosing_crosscheck: "2026-02-19"
---

# Unstable Bradycardia

## Recognition

### Definition
Heart rate < 60 bpm (or rate insufficient to maintain adequate perfusion) with signs/symptoms of hemodynamic instability.

### Signs of Instability
- Hypotension (SBP < 90 mmHg)
- Altered mental status (confusion, syncope, presyncope)
- Signs of shock (diaphoresis, pallor, mottled skin, delayed capillary refill)
- Chest pain / acute ischemia
- Acute heart failure (pulmonary edema, dyspnea)

### ECG Classification

**Sinus Bradycardia:**
- Regular rhythm, P waves before every QRS
- Causes: physiologic (athletes), medications, hypothyroidism, increased ICP, inferior MI

**First-Degree AV Block:**
- PR interval > 200 ms, all P waves conducted
- Rarely causes instability alone

**Second-Degree AV Block — Mobitz Type I (Wenckebach):**
- Progressive PR prolongation then dropped QRS
- Usually at AV node level, often benign; rarely causes hemodynamic compromise

**Second-Degree AV Block — Mobitz Type II:**
- Fixed PR interval with intermittent dropped QRS (no progressive prolongation)
- Infranodal (His-Purkinje) disease; high risk of progression to complete heart block
- Wide QRS common

**Third-Degree (Complete) AV Block:**
- Complete AV dissociation; P waves march through independently of QRS
- Narrow escape rhythm (junctional, 40-60 bpm) or wide escape rhythm (ventricular, 20-40 bpm)
- Wide QRS escape = unreliable, high risk of asystole

**High-Degree AV Block:**
- Multiple consecutive P waves not conducted (2:1 or higher ratios)
- Treat as emergent regardless of symptoms

### Common Etiologies
| Category | Examples |
|---|---|
| Medications | Beta-blockers, calcium channel blockers (diltiazem, verapamil), digoxin, amiodarone, clonidine, organophosphates |
| Cardiac | Acute MI (especially inferior/RV), myocarditis, endocarditis, post-cardiac surgery, infiltrative disease (sarcoid, amyloid) |
| Metabolic | Hyperkalemia, hypothyroidism, hypothermia |
| Neurologic | Increased intracranial pressure (Cushing response), spinal cord injury |
| Other | Obstructive sleep apnea, carotid sinus hypersensitivity |

## Critical Actions

| Action | Target |
|---|---|
| 12-lead ECG | Immediately; identify rhythm and block type |
| Atropine 1 mg IV push | First-line for symptomatic bradycardia |
| Transcutaneous pacing | If atropine fails or high-degree/third-degree block |
| IV chronotropic infusion | Dopamine or epinephrine if pacing unavailable or bridge to transvenous |
| Identify and treat reversible cause | Hyperkalemia, medication toxicity, MI |
| Cardiology/EP consultation | For transvenous pacing or definitive management |

1. Assess airway, breathing, circulation; attach continuous cardiac monitoring and pulse oximetry
2. Obtain 12-lead ECG immediately
3. If unstable: administer atropine 1 mg IV push; may repeat every 3-5 minutes to maximum 3 mg total
4. If atropine ineffective or high-degree/third-degree block: initiate transcutaneous pacing immediately
5. Start chronotropic infusion if pacing not available or as bridge: dopamine 5-20 mcg/kg/min IV OR epinephrine 2-10 mcg/min IV
6. Obtain IV access (2 large-bore), STAT labs (K, Mg, Ca, TSH, digoxin level if applicable), troponin
7. Treat reversible causes concurrently

## Differential Diagnosis

- Acute myocardial infarction (inferior/RV MI — ST elevation in II, III, aVF; right-sided leads)
- Hyperkalemia (peaked T waves, wide QRS, sine wave)
- Beta-blocker overdose (hypotension, hypoglycemia)
- Calcium channel blocker overdose (hypotension, hyperglycemia)
- Digoxin toxicity (bidirectional VT, scooped ST segments, nausea, visual changes)
- Hypothyroidism (myxedema coma: hypothermia, altered mentation, hypoglycemia)
- Hypothermia (Osborn/J waves, core temp < 35C)
- Increased intracranial pressure (Cushing triad: hypertension, bradycardia, irregular respirations)
- Organophosphate poisoning (SLUDGE/DUMBELS, miosis, bronchorrhea)
- Sick sinus syndrome (alternating tachycardia-bradycardia)
- Lyme disease with carditis (history of tick exposure, erythema migrans, PR prolongation)

## Workup

- **12-lead ECG:** Identify rhythm, block type, ischemic changes, hyperkalemia features; obtain right-sided leads (V4R) if inferior ST elevation
- **Continuous cardiac monitoring:** Telemetry for rhythm changes
- **BMP:** Potassium (hyperkalemia is immediately treatable cause), calcium, magnesium, glucose, creatinine
- **Troponin:** Acute coronary syndrome as cause of conduction disease
- **TSH:** Hypothyroidism
- **Digoxin level:** If patient on digoxin
- **Drug levels:** Beta-blocker or calcium channel blocker levels if overdose suspected
- **Core temperature:** Hypothermia
- **Point-of-care ultrasound:** Cardiac function, pericardial effusion, RV dilation (RV infarct)
- **Chest X-ray:** Cardiomegaly, pulmonary edema, pacemaker lead position if present
- **CT head:** If increased ICP suspected (Cushing triad)

## Treatment

### Atropine
- **Dose:** 1 mg IV push; repeat every 3-5 minutes; maximum total dose 3 mg
- Mechanism: Vagolytic — increases sinus rate and AV conduction
- **Effective for:** Sinus bradycardia, first-degree AV block, Mobitz Type I
- **Ineffective/unreliable for:** Mobitz Type II, third-degree AV block (infranodal), denervated transplant hearts — proceed directly to pacing
- Do NOT use doses < 0.5 mg (paradoxical bradycardia)

### Transcutaneous Pacing (TCP)
- **Indication:** Atropine failure, Mobitz Type II, third-degree AV block, any unstable bradycardia unresponsive to medications
- **Technique:**
  - Apply pads: anterior (left sternal border or apex) and posterior (left infrascapular)
  - Set rate to 60-80 bpm
  - Start output at 0 mA, increase gradually until electrical capture (pacer spike followed by wide QRS with corresponding pulse)
  - Typical capture threshold: 50-100 mA; increase 10 mA above threshold for safety margin
  - Confirm mechanical capture: palpate femoral pulse (most reliable), verify BP
- **Sedation:** Fentanyl 1 mcg/kg IV + midazolam 1-2 mg IV for conscious patients (pacing is painful)
- **Failure to capture:** Increase output to maximum (200 mA), reposition pads, ensure good skin contact, verify connections

### Chronotropic Infusions
- **Dopamine:** 5-20 mcg/kg/min IV infusion; beta-1 agonist effect at this range; titrate to heart rate and BP
- **Epinephrine:** 2-10 mcg/min IV infusion; use if dopamine unavailable or inadequate; potent chronotrope and inotrope
- **Isoproterenol:** 2-10 mcg/min IV infusion; pure beta-agonist; useful for torsades or transplant hearts; avoid in ischemia (increases myocardial O2 demand)

### Medication-Specific Antidotes

**Beta-blocker toxicity:**
- Glucagon 5-10 mg IV bolus, then 1-5 mg/hr infusion (bypasses beta-receptor via cAMP)
- High-dose insulin euglycemic therapy (HIET): insulin 1 unit/kg IV bolus, then 1 unit/kg/hr infusion; co-administer dextrose 50% 25 g IV bolus, then D10W infusion; monitor glucose q15 min
- IV lipid emulsion (Intralipid 20%): 1.5 mL/kg IV bolus, then 0.25 mL/kg/min infusion for lipophilic beta-blocker overdose

**Calcium channel blocker toxicity:**
- Calcium chloride 1-2 g IV (via central line) or calcium gluconate 3-6 g IV (peripheral OK); repeat every 15-20 minutes; no maximum dose in toxicity
- High-dose insulin euglycemic therapy (same protocol as beta-blocker toxicity) — first-line for CCB overdose with shock
- IV lipid emulsion for lipophilic agents (verapamil)

**Digoxin toxicity:**
- Digoxin-specific antibody fragments (Digibind/DigiFab): empiric dose 10-20 vials IV if acute life-threatening toxicity with unknown level; calculated dose if level known
- Do NOT use calcium in digoxin toxicity (risk of "stone heart" — sudden cardiac arrest; this is debated but standard practice is to avoid)
- Atropine may be effective for digoxin-induced bradycardia
- Correct hypokalemia (potentiates digoxin toxicity)

**Organophosphate poisoning:**
- Atropine 2-4 mg IV, double dose every 3-5 minutes until secretions dry
- Pralidoxime (2-PAM) 1-2 g IV over 15-30 minutes

### Transvenous Pacing
- Indicated when TCP fails, prolonged pacing needed, or as bridge to permanent pacemaker
- Requires central venous access (internal jugular or femoral preferred)
- Perform under fluoroscopy or ultrasound guidance if available
- Consult cardiology/EP for placement

### Treat Underlying Cause
- **Hyperkalemia:** Calcium gluconate 3 g IV, insulin 10 units IV + D50 25 g, albuterol 10-20 mg nebulized, sodium bicarbonate 150 mEq IV if acidotic
- **Inferior MI:** Reperfusion therapy (PCI), avoid nitroglycerin and morphine (preload-dependent), IV fluids for RV infarct
- **Hypothermia:** Active rewarming; pacing often ineffective until core temp > 30C

## Disposition

- **Hemodynamically unstable bradycardia requiring pacing or vasopressors:** ICU admission, continuous telemetry, cardiology consultation for transvenous pacing
- **Mobitz Type II or third-degree AV block (even if stabilized):** ICU or monitored bed; will likely require permanent pacemaker
- **Medication-induced bradycardia responding to antidotes:** ICU or monitored bed for at least 24 hours (longer for sustained-release preparations)
- **Sinus bradycardia or Mobitz Type I responsive to atropine with reversible cause identified and treated:** Monitored telemetry bed
- **New-onset Mobitz Type II or third-degree AV block:** Cardiology/EP consultation for permanent pacemaker evaluation before discharge
- Do NOT discharge patients with new high-degree AV block, syncope from bradycardia, or medication overdose requiring antidotes

## Pitfalls

1. **Administering atropine for Mobitz Type II or third-degree AV block and assuming it will work.** Atropine acts on the AV node. Infranodal block does not respond. Proceed directly to transcutaneous pacing.

2. **Using atropine doses < 0.5 mg.** Low-dose atropine causes paradoxical bradycardia via central vagal stimulation. Always give 1 mg IV push per dose.

3. **Failing to confirm mechanical capture during transcutaneous pacing.** Electrical capture (pacer spikes with QRS complexes on monitor) does not guarantee mechanical capture. Palpate a pulse (femoral is most reliable) and verify blood pressure.

4. **Not sedating conscious patients during transcutaneous pacing.** TCP causes significant pain from chest wall muscle contraction. Administer fentanyl and midazolam. Unmanaged pain causes catecholamine surge and patient non-compliance.

5. **Missing hyperkalemia as the cause.** Peaked T waves and wide QRS on ECG demand STAT potassium. Treat empirically with calcium gluconate 3 g IV if hyperkalemia suspected — this buys time while awaiting lab results.

6. **Forgetting to check a digoxin level in elderly patients on multiple cardiac medications.** Digoxin toxicity is common, especially with renal insufficiency, hypokalemia, or drug interactions (amiodarone, verapamil). Specific antidote (DigiFab) is immediately effective.

7. **Administering calcium in digoxin toxicity.** IV calcium in the setting of digoxin toxicity risks fatal arrhythmia. Confirm medication list before giving calcium for any cause of bradycardia.

8. **Stopping monitoring after atropine response.** Atropine's duration is 1-2 hours. Bradycardia frequently recurs, particularly with medication toxicity from sustained-release formulations. Maintain continuous monitoring and have pacing pads pre-applied.

9. **Failing to obtain right-sided ECG leads in inferior STEMI with bradycardia.** Right ventricular infarction causes bradycardia and is preload-dependent. Nitroglycerin and diuretics can cause cardiovascular collapse. IV fluid bolus is the correct treatment.

10. **Not considering high-dose insulin euglycemic therapy early in CCB or BB overdose.** HIET is first-line for hemodynamically significant calcium channel blocker overdose and effective for beta-blocker overdose. Initiate early — onset takes 15-30 minutes.
