---
id: acute-heart-failure
condition: Acute Heart Failure
aliases: [acute decompensated heart failure, ADHF, flash pulmonary edema, cardiogenic pulmonary edema, CHF exacerbation]
icd10: [I50.21, I50.23, I50.31, I50.33, I50.41, I50.43, I50.9]
esi: 2
time_to_harm: "< 1 hour"
mortality_if_delayed: "In-hospital mortality 4-10%; cardiogenic shock mortality 40-50%"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure"
    doi: "10.1161/CIR.0000000000001063"
  - type: guideline
    ref: "2021 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure"
    doi: "10.1093/eurheartj/ehab368"
  - type: pubmed
    ref: "Mebazaa A et al. Recommendations on pre-hospital and early hospital management of acute heart failure: a consensus paper. Eur J Heart Fail. 2015;17(6):544-558"
    pmid: "25999021"
  - type: pubmed
    ref: "Hollenberg SM et al. 2019 ACC Expert Consensus Decision Pathway on Risk Assessment, Management, and Clinical Trajectory of Patients Hospitalized With Heart Failure. J Am Coll Cardiol. 2019;74(15):1966-2011"
    pmid: "31526538"
last_updated: "2026-02-18"
compiled_by: agent
reviewed_by: null
verification:
  pmids_verified: "2026-02-18"
  audit_completed: "2026-02-18"
---

# Acute Heart Failure

## Recognition

**Clinical profiles (classify on arrival):**

| Profile | Congestion | Perfusion | Description |
|---|---|---|---|
| Warm and wet | Yes | Adequate | Most common ED presentation (~70%) |
| Cold and wet | Yes | Poor | Cardiogenic shock with congestion |
| Cold and dry | No | Poor | Low-output state, often over-diuresed |
| Warm and dry | No | Adequate | Compensated; unlikely acute HF |

**Signs of congestion (wet):**
- Dyspnea (exertional, orthopnea, paroxysmal nocturnal dyspnea)
- Jugular venous distension
- Pulmonary crackles/rales (may be absent in chronic HF)
- S3 gallop
- Peripheral edema, ascites, hepatojugular reflux
- Weight gain

**Signs of hypoperfusion (cold):**
- Cool extremities, mottled skin
- Narrow pulse pressure (< 25 mmHg)
- Altered mental status, oliguria
- Hypotension (SBP < 90 mmHg)

**Precipitants to identify:**
- ACS/ischemia, arrhythmia (new AFib with RVR), valvular emergency (acute MR, aortic stenosis)
- Medication/dietary noncompliance
- Hypertensive emergency, infection/sepsis
- Anemia, thyroid disease, pulmonary embolism
- Renal failure, toxic ingestion

## Critical Actions

| Action | Target |
|---|---|
| IV access, cardiac monitor, SpO2 | Immediate |
| Noninvasive positive pressure ventilation (NIPPV) | Within 5 minutes if respiratory distress |
| IV nitroglycerin or nitroprusside | Within 15 minutes if SBP > 100 |
| Diuretic administration | Within 30 minutes |
| Bedside echo | Within 15 minutes |

1. **NIPPV** (BiPAP): start at 10/5 cmH2O, titrate to work of breathing; reduces intubation rates and mortality (3CPO trial); use CPAP 5-10 cmH2O if BiPAP unavailable
2. **Nitroglycerin** 400 mcg SL, repeat q5min; start IV at 20-200 mcg/min; titrate aggressively for flash pulmonary edema — this is the primary intervention for hypertensive acute HF
3. **Furosemide** 40 mg IV if diuretic-naive; 1-2.5x home oral dose IV if already on loop diuretics; assess urine output at 2 hours
4. **Identify and treat precipitant** — ECG for ischemia/arrhythmia; troponin; chest X-ray
5. **Bedside echocardiography:** Assess EF, regional wall motion, valvular function, pericardial effusion, RV dilation

## Differential Diagnosis

- COPD/asthma exacerbation (wheezing, history, hyperinflation on CXR)
- Pneumonia (fever, consolidation, productive cough)
- Pulmonary embolism (pleuritic pain, RV dilation on echo, risk factors)
- ARDS (bilateral infiltrates, identified insult, no cardiomegaly, normal BNP)
- Pericardial tamponade (JVD, muffled sounds, pericardial effusion on echo)
- Severe anemia causing high-output failure
- Nephrotic syndrome or cirrhosis (edema from hypoalbuminemia)
- Tension pneumothorax (unilateral absent breath sounds)

## Workup

- **BNP or NT-proBNP:** BNP > 400 pg/mL or NT-proBNP > 900 pg/mL (age-adjusted) supports diagnosis; BNP < 100 pg/mL effectively excludes acute HF
- **Troponin:** ACS as precipitant; type 2 MI from demand ischemia
- **BMP:** Creatinine (cardiorenal syndrome), potassium (arrhythmia risk, diuretic effects), sodium (hyponatremia indicates poor prognosis), bicarbonate (metabolic acidosis in shock)
- **CBC:** Anemia, leukocytosis
- **Hepatic panel:** Congestive hepatopathy
- **Lactate:** Elevated in cardiogenic shock; marker of hypoperfusion
- **ECG:** Ischemia, arrhythmia, LVH, bundle branch block
- **Chest X-ray:** Cardiomegaly, cephalization of vessels, interstitial/alveolar edema, pleural effusions, Kerley B lines
- **Point-of-care ultrasound:** B-lines (>= 3 per lung zone = pulmonary edema), pleural effusion, IVC assessment, cardiac function
- **ABG/VBG** if severe respiratory distress or intubation planned

## Treatment

### Warm and Wet (Hypertensive, Congested, Adequate Perfusion)
This is the most common presentation and most responsive to ED treatment.

**Vasodilators (primary therapy):**
- Nitroglycerin IV 20-200 mcg/min; titrate aggressively in flash pulmonary edema; high-dose nitroglycerin (up to 400 mcg/min) is safe with BP monitoring
- Alternatively: nitroglycerin 400 mcg SL q5min while establishing IV access
- Nitroprusside 0.3-5 mcg/kg/min for refractory hypertensive HF (requires arterial line; cyanide risk with prolonged use)

**Diuretics:**
- Furosemide: 40 mg IV (diuretic-naive) or 1-2.5x home dose IV; reassess urine output at 2 hours
- If inadequate response: double the dose or add metolazone 5 mg PO (sequential nephron blockade)
- Bumetanide 1-2 mg IV as alternative to furosemide

**Respiratory support:**
- BiPAP 10/5 cmH2O, titrate IPAP to 15 cmH2O as needed
- Intubation if NIPPV fails, persistent SpO2 < 90%, or inability to protect airway

### Cold and Wet (Cardiogenic Shock)
- **Norepinephrine** 0.1-0.5 mcg/kg/min IV first-line vasopressor (preferred over dopamine per SOAP II trial)
- **Dobutamine** 2-20 mcg/kg/min IV for inotropy (augments cardiac output)
- **Milrinone** 0.375-0.75 mcg/kg/min IV (avoid loading dose; alternative inodilator; useful in beta-blocker–treated patients)
- Diuretics after perfusion restored
- Mechanical circulatory support (IABP, Impella, ECMO) per institutional protocol
- Urgent cardiology and cardiac surgery consultation

### Cold and Dry
- Cautious volume challenge: 250 mL NS IV over 15-30 minutes with reassessment
- Inotropes if no response to volume
- This profile is uncommon; reassess diagnosis

### Acute Valvular Emergency
- Acute mitral regurgitation (ruptured chordae/papillary muscle): vasodilators to reduce afterload, urgent surgical consultation
- Acute aortic regurgitation: nitroprusside, avoid IABP (worsens AR); urgent surgery
- Prosthetic valve thrombosis: thrombolysis or surgical thrombectomy

## Disposition

- **ICU:** Cardiogenic shock, requiring vasopressors/inotropes, intubated, mechanical circulatory support, acute valvular emergency
- **Telemetry/step-down:** Stable requiring IV diuresis, oxygen supplementation, monitoring for diuretic response
- **Observation unit (select patients):** Known HF, mild exacerbation, rapid response to single dose of diuretic, ambulatory and stable
- **Discharge criteria (rare from ED):** Symptom resolution, ambulating at baseline, adequate oxygenation on room air, oral medication regimen established, weight at or near dry weight, follow-up within 7 days
- **Cardiology follow-up** for all new-onset HF and decompensated HF within 7-14 days

## Pitfalls

1. **Withholding nitroglycerin in flash pulmonary edema.** Nitroglycerin is the most rapidly effective treatment for hypertensive acute HF. Diuretics take 30-60 minutes for effect. Aggressive IV nitroglycerin (starting 100-200 mcg/min) in patients with SBP > 140 is safe and rapidly reduces work of breathing.

2. **Treating all acute HF with furosemide first.** Patients presenting with flash pulmonary edema and hypertension are fluid-redistributed, not necessarily fluid-overloaded. Vasodilators reduce preload and afterload immediately; diuretics are adjunctive.

3. **Intubating before attempting NIPPV.** BiPAP rapidly reduces respiratory distress and avoids the hemodynamic collapse that frequently accompanies positive-pressure ventilation and sedation in acute HF. NIPPV should be first-line in all alert, cooperative patients.

4. **Using propofol or other vasodilating sedatives for intubation without vasopressor support.** Rapid sequence intubation with propofol in acute HF causes cardiovascular collapse. Use ketamine 1-2 mg/kg IV or etomidate 0.3 mg/kg IV. Push-dose epinephrine (10-20 mcg IV) should be at bedside.

5. **Failure to identify ACS as the precipitant.** Troponin and ECG are mandatory. Type 1 MI causing new HF requires emergent reperfusion, not just diuresis.

6. **Diagnosing pneumonia based on CXR and treating with antibiotics alone.** Bilateral alveolar infiltrates from pulmonary edema mimic pneumonia. BNP, history, and lung ultrasound differentiate. Missed HF treated as pneumonia leads to progressive volume overload.

7. **Giving IV fluids to hypotensive acute HF patients (cold and wet profile).** These patients need vasopressors and inotropes, not volume. Additional fluid worsens pulmonary congestion. Only the cold and dry profile warrants cautious volume challenge.

8. **Discharging new-onset heart failure from the ED.** New-onset HF requires inpatient workup: echocardiography, ischemia evaluation, and establishing baseline therapy (ACE inhibitor/ARB, beta-blocker, diuretic, SGLT2 inhibitor per 2022 AHA/ACC guidelines).

9. **Overlooking right ventricular failure.** Isolated RV failure (from PE, RV MI, pulmonary hypertension) presents with JVD and hypotension but clear lungs. Diuretics and nitroglycerin cause hemodynamic collapse. Volume-dependent physiology requires different management.
