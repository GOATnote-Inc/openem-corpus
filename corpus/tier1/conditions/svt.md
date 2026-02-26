---
id: svt
condition: Supraventricular Tachycardia
aliases: [SVT, PSVT, paroxysmal supraventricular tachycardia, AVNRT, AVRT, narrow complex tachycardia, reentrant tachycardia]
icd10: [I47.1, I47.10, I47.19]
esi: 2
time_to_harm: "< 2 hours"
mortality_if_delayed: "Hemodynamic collapse with sustained rapid rate; degeneration to VF in pre-excited SVT (WPW)"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "Page RL, Joglar JA, Caldwell MA, et al. 2015 ACC/AHA/HRS Guideline for the Management of Adult Patients With Supraventricular Tachycardia. J Am Coll Cardiol. 2016;67(13):e27-e115"
    pmid: "26409259"
    doi: "10.1016/j.jacc.2015.08.856"
  - type: guideline
    ref: "Brugada J, Katritsis DG, Arbelo E, et al. 2019 ESC Guidelines for the management of patients with supraventricular tachycardia. Eur Heart J. 2020;41(5):655-720"
    pmid: "31504425"
    doi: "10.1093/eurheartj/ehz467"
  - type: pubmed
    ref: "Appelboam A, Reuben A, Mann C, et al. Postural modification to the standard Valsalva manoeuvre for emergency treatment of supraventricular tachycardias (REVERT): a randomised controlled trial. Lancet. 2015;386(10005):1747-1753"
    pmid: "26314489"
    doi: "10.1016/S0140-6736(15)61485-4"
  - type: meta-analysis
    ref: "Alabed S, Sabouni A, Providencia R, et al. Adenosine versus intravenous calcium channel antagonists for supraventricular tachycardia. Cochrane Database Syst Rev. 2017;10:CD005154"
    pmid: "29025197"
    doi: "10.1002/14651858.CD005154.pub4"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: B
validation:
  automated_consistency_check: "2026-02-27"
  dose_range_validator: "2026-02-27"
  unit_normalization_check: "2026-02-27"
  cross_file_consistency_check: "2026-02-27"
  citation_presence_check: "2026-02-27"
  duplicate_content_check: "2026-02-27"
  outlier_detection_flag: clear
  schema_version: "2.0"
  provenance_links: []
---
# Supraventricular Tachycardia

## Recognition

**ECG findings:**
- Regular narrow complex tachycardia (QRS < 120 ms) at 150-250 bpm
- P waves absent, retrograde, or buried in QRS (AVNRT) or inverted after QRS (AVRT)
- Abrupt onset and termination (paroxysmal)
- Rate often fixed — no variability with respiration or activity changes
- Pseudo R' in V1 or pseudo S in II/III/aVF (retrograde P waves in AVNRT)

**Subtypes by mechanism:**
- AVNRT (60%): dual AV nodal pathways; most common SVT in adults
- AVRT (30%): accessory pathway (orthodromic = narrow complex; antidromic = wide complex)
- Atrial tachycardia (10%): ectopic atrial focus; may show warm-up/cool-down pattern

**Symptoms:**
- Palpitations (acute onset, "fluttering" sensation)
- Chest pain, dyspnea, lightheadedness
- Presyncope or syncope (rare unless prolonged or structural heart disease)
- Polyuria (ANP release from atrial stretch — classic historical feature)
- Anxiety, diaphoresis

**Hemodynamic instability indicators:**
- SBP < 90 mmHg or MAP < 65 mmHg
- Altered mental status
- Acute pulmonary edema
- Ongoing ischemic chest pain with ECG changes
- Signs of end-organ hypoperfusion (mottling, oliguria)

## Critical Actions

| Action | Target |
|---|---|
| 12-lead ECG | < 5 minutes |
| Hemodynamic assessment | Immediate |
| Vagal maneuvers (modified Valsalva) | First intervention |
| Adenosine if vagal maneuvers fail | Within 10 minutes |
| Synchronized cardioversion if unstable | Without delay |

1. **Unstable patient:** Synchronized cardioversion at 50-100 J biphasic; sedate with etomidate 0.2-0.3 mg/kg IV or midazolam 2-5 mg IV if time permits
2. **Stable patient — stepwise approach:**
   - Modified Valsalva first (REVERT technique): patient seated semi-recumbent at 45 degrees, blow into 10 mL syringe for 15 seconds, immediately lay supine with passive leg raise to 45 degrees for 15 seconds (43% conversion rate vs 17% standard Valsalva)
   - Carotid sinus massage (unilateral, 5-10 seconds) — contraindicated if carotid bruit, known carotid stenosis, or recent stroke
3. **Adenosine** if vagal maneuvers fail:
   - 6 mg rapid IV push via large-bore antecubital IV, followed immediately by 20 mL NS rapid flush
   - If no conversion in 1-2 minutes: 12 mg rapid IV push with flush
   - If still no conversion: 12 mg rapid IV push with flush (third dose)
   - Warn patient: transient chest tightness, dyspnea, flushing, sense of impending doom lasting 10-15 seconds
   - Record continuous rhythm strip during administration — diagnostic even if no conversion
4. **Obtain 12-lead ECG in sinus rhythm** after conversion to evaluate for pre-excitation (delta wave = WPW), structural heart disease, or other baseline abnormalities

## Differential Diagnosis

| Diagnosis | Key Distinguishing Features |
|---|---|
| Sinus tachycardia | Gradual onset/offset, rate varies with activity/stimulus, upright P waves in II, rate rarely > 150 bpm unless physiologic stress |
| Atrial flutter | Sawtooth flutter waves at ~300 bpm (best seen in II, III, aVF, V1); ventricular rate typically 150 bpm (2:1 block) or 75 bpm (4:1); may be revealed with adenosine |
| Atrial fibrillation | Irregularly irregular RR intervals, absent P waves, fibrillatory baseline |
| Multifocal atrial tachycardia | Irregular, >= 3 distinct P wave morphologies, varying PR intervals; associated with COPD, hypoxia |
| Ventricular tachycardia | Wide complex (QRS > 120 ms), AV dissociation, fusion/capture beats, concordance in precordial leads; assume VT until proven otherwise in wide complex tachycardia |
| Antidromic AVRT (WPW) | Wide complex, regular; delta wave on baseline ECG; treat as VT if uncertain |
| Junctional tachycardia | Narrow complex, rate 60-130 bpm, may be nonparoxysmal; associated with digoxin toxicity, inferior MI, myocarditis |

## Workup

- **12-lead ECG:** Confirm narrow complex regular tachycardia; assess for pre-excitation (delta wave), ischemia, prior MI
- **Continuous telemetry:** Monitor during vagal maneuvers and adenosine administration
- **BMP:** Electrolytes (potassium, magnesium, calcium), renal function
- **Magnesium level:** Hypomagnesemia may perpetuate arrhythmia
- **TSH:** Hyperthyroidism as trigger (not urgent but obtain during workup)
- **Troponin:** Demand ischemia from sustained tachycardia, particularly if chest pain or ECG changes
- **CBC:** Anemia as exacerbating factor
- **Chest X-ray:** Cardiomegaly, pulmonary edema if heart failure suspected
- **Pregnancy test:** Women of reproductive age (affects drug choices)
- **Point-of-care echocardiography:** If concern for structural heart disease or hemodynamic compromise

## Treatment

### Vagal Maneuvers (First-Line)

**Modified Valsalva (REVERT technique):**
- Semi-recumbent position at 45 degrees
- Forceful expiration against closed glottis (blow into 10 mL syringe) for 15 seconds at 40 mmHg pressure
- Immediately lay patient flat and elevate legs to 45 degrees for 15 seconds
- Conversion rate 43% (vs 17% standard Valsalva per REVERT trial)

**Carotid sinus massage:**
- Unilateral, firm pressure over carotid bifurcation for 5-10 seconds
- Contraindicated: carotid bruit, known carotid stenosis, recent stroke/TIA
- Perform with continuous ECG monitoring and IV access

### Adenosine (Second-Line if Vagal Maneuvers Fail)

- **First dose:** 6 mg rapid IV push through large-bore (18G or larger) antecubital IV
- **Technique:** Rapid push followed immediately by 20 mL NS flush via stopcock or two-syringe technique; elevate arm
- **Second dose:** 12 mg rapid IV push if no conversion in 1-2 minutes
- **Third dose:** 12 mg rapid IV push if second dose fails
- **Half-life:** < 10 seconds; must be delivered rapidly to reach heart before degradation
- **Dose adjustments:**
  - Reduce initial dose to 3 mg in patients on carbamazepine or dipyridamole, heart transplant recipients, or central line administration
  - Increase dose if on theophylline or caffeine (competitive antagonism); may need 12 mg first dose or 18 mg subsequent doses
- **Contraindications:** Second- or third-degree heart block, sick sinus syndrome (without pacemaker), severe asthma/COPD (relative — use with caution, have bronchodilator available)

### Calcium Channel Blockers (If Adenosine Fails, No WPW)

- **Diltiazem:** 0.25 mg/kg IV over 2 minutes (typical 15-20 mg); repeat at 0.35 mg/kg after 15 minutes if needed
- **Verapamil:** 2.5-5 mg IV over 2 minutes; repeat 5-10 mg after 15-30 minutes if needed (max 20 mg total)
- Avoid in hypotension (SBP < 90), decompensated HF, concurrent IV beta-blocker use

### Beta-Blockers (If Adenosine Fails, No WPW)

- **Metoprolol:** 5 mg IV over 2 minutes; repeat q5min up to 15 mg total
- **Esmolol:** 500 mcg/kg IV bolus over 1 minute, then 50-200 mcg/kg/min infusion (advantage: ultra-short acting, titratable)
- Avoid in acute HF, hypotension, severe asthma/COPD

### Pre-excited SVT (Known or Suspected WPW)

- **CONTRAINDICATED:** Adenosine, diltiazem, verapamil, beta-blockers, digoxin — all block AV node preferentially, enhancing conduction through accessory pathway, risking VF
- **Procainamide:** 15-17 mg/kg IV at 20-50 mg/min (slows accessory pathway conduction); stop if QRS widens > 50%, hypotension occurs, or arrhythmia terminates
- **Amiodarone:** 150 mg IV over 10 minutes (second-line)
- **Synchronized cardioversion:** 50-100 J biphasic if hemodynamically unstable or pharmacotherapy fails

### Unstable SVT

- **Synchronized cardioversion:** Start at 50 J biphasic, escalate to 100 J, then 200 J if needed
- Procedural sedation: etomidate 0.2-0.3 mg/kg IV or midazolam 2-5 mg IV (do not delay cardioversion for sedation if patient is critically unstable)
- Pad placement: anterolateral or anteroposterior

## Disposition

- **Discharge from ED:** Known SVT converted to sinus rhythm, hemodynamically stable, no recurrence during observation (minimum 30-60 minutes post-conversion), no concerning etiology identified, reliable follow-up arranged
- **Observe:** First episode of SVT, prolonged episode, recurrent episodes during ED stay, persistent mild symptoms after conversion
- **Admit/telemetry:** Refractory SVT requiring infusion, hemodynamic instability requiring cardioversion, concern for WPW, significant comorbidities (structural heart disease, HF, coronary artery disease), troponin elevation
- **ICU:** SVT with hemodynamic collapse, requiring vasopressors, post-cardioversion with ongoing instability
- **Cardiology follow-up:** All first-episode SVT (EP study and ablation discussion), recurrent SVT despite medication, any pre-excitation on ECG (WPW — electrophysiology referral for ablation, which is curative in > 95% of cases)
- **Discharge medications (cardiology-guided):** Metoprolol tartrate 25-50 mg PO BID, diltiazem ER 120-240 mg PO daily, or flecainide 50-150 mg PO BID (pill-in-the-pocket strategy for infrequent episodes) — initiate in consultation with cardiology

## Pitfalls

1. **Misidentifying wide complex tachycardia as SVT with aberrancy.** When in doubt, treat wide complex tachycardia as ventricular tachycardia. Giving verapamil or diltiazem to a patient in VT causes cardiovascular collapse. Only 12-lead morphology criteria (Brugada algorithm, Vereckei aVR) or known prior bundle branch block justify treating as SVT with aberrancy.

2. **Administering adenosine too slowly or through a peripheral hand/wrist IV.** Adenosine half-life is under 10 seconds. Slow push or distal IV results in degradation before reaching the heart. Use a large-bore antecubital or central IV with rapid push and immediate 20 mL NS flush.

3. **Giving AV nodal blockers (adenosine, diltiazem, verapamil, digoxin) in pre-excited atrial fibrillation (WPW with AFib).** Pre-excited AFib is an irregular wide complex tachycardia with varying QRS morphology and rates > 200 bpm. AV nodal blockade removes the braking effect of the AV node, forcing all conduction through the accessory pathway, and precipitates ventricular fibrillation.

4. **Failing to record a rhythm strip during adenosine administration.** Even when adenosine does not terminate the tachycardia, the transient AV block provides diagnostic information. Atrial flutter waves, atrial tachycardia P waves, or an unchanged rate during AV block all narrow the differential and change management.

5. **Not obtaining a 12-lead ECG in sinus rhythm after conversion.** The post-conversion ECG is essential for detecting delta waves (WPW), prior MI (Q waves), LVH, or other baseline abnormalities that guide long-term management and risk stratification. This information is unavailable during tachycardia.

6. **Overlooking sinus tachycardia as a mimic.** A rate of 150 bpm with 1:1 P waves can look like SVT, particularly if P waves are buried in T waves. Sinus tachycardia is always secondary (sepsis, hypovolemia, PE, pain, anxiety). Treating the sinus tachycardia of sepsis with adenosine wastes time and misses the real emergency.

7. **Attributing hemodynamic instability to SVT without considering concurrent pathology.** SVT alone rarely causes shock in patients without structural heart disease. If a patient with SVT is hypotensive and altered, search for PE, sepsis, hemorrhage, ACS, or tension pneumothorax before assuming SVT is the sole etiology.

8. **Not warning patients about adenosine side effects.** Transient chest tightness, dyspnea, flushing, and a profound sense of impending doom are expected with adenosine and last 10-15 seconds. Without warning, patients panic and may interpret the sensation as a cardiac event, increasing agitation and catecholamine surge that promotes SVT recurrence.

9. **Discharging first-episode SVT without cardiology referral.** Electrophysiology study with catheter ablation is curative in over 95% of AVNRT and AVRT cases. Patients sent home on rate-control medications alone without EP referral may have avoidable recurrent episodes, ED visits, and rarely sudden death (in undiagnosed WPW).
