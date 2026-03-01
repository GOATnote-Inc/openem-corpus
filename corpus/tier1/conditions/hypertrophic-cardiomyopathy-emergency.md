---
id: hypertrophic-cardiomyopathy-emergency
condition: Hypertrophic Cardiomyopathy — Emergency Presentations
aliases: [HCM, HOCM, hypertrophic obstructive cardiomyopathy, idiopathic hypertrophic subaortic stenosis, IHSS]
icd10: [I42.1, I42.2]
esi: 2
time_to_harm:
  irreversible_injury: "< 30 minutes (sudden cardiac arrest)"
  death: "< 30 minutes"
  optimal_intervention_window: "< 10 minutes (defibrillation)"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2024 AHA/ACC/AMSSM/HRS/PACES/SCMR Guideline for the Management of Hypertrophic Cardiomyopathy. Circulation. 2024;149(23):e1239-e1311."
  - type: guideline
    ref: "2023 ESC Guidelines for the Management of Cardiomyopathies. Eur Heart J. 2023;44(37):3503-3626."
  - type: review
    ref: "Maron BJ, et al. Hypertrophic Cardiomyopathy. Lancet. 2013;381(9862):242-255."
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
# Hypertrophic Cardiomyopathy — Emergency Presentations

## Recognition

**Emergency presentations:**
- Sudden cardiac arrest (VF/VT) — may be first manifestation, especially in young athletes
- Syncope or presyncope — exertional (LVOT obstruction) or arrhythmic (VT/VF)
- Acute heart failure — dyspnea, orthopnea, pulmonary edema
- Chest pain — demand ischemia from hypertrophied myocardium, microvascular disease
- Rapid atrial fibrillation — poorly tolerated due to diastolic dysfunction and loss of atrial kick

**Physical exam (obstructive HCM):**
- Harsh crescendo-decrescendo systolic murmur at left sternal border
- Murmur increases with Valsalva, standing (decreased preload)
- Murmur decreases with squatting, passive leg raise (increased preload)
- Bisferiens pulse (double systolic peak)
- S4 gallop
- Brisk, hyperdynamic carotid upstroke

**ECG findings:**
- LVH with strain pattern (deep S in V1-V2, tall R in V5-V6, ST depression, T-wave inversion)
- Deep Q waves in lateral leads (septal hypertrophy mimics prior MI)
- LA enlargement
- May have WPW pattern (associated with HCM in some genetic subtypes)

**Risk factors for sudden cardiac death (2024 AHA/ACC):**
- Prior cardiac arrest or sustained VT
- Family history of SCD attributable to HCM
- Maximum LV wall thickness >= 30 mm
- Unexplained syncope
- NSVT on ambulatory monitoring
- LV apical aneurysm
- LV systolic dysfunction (EF < 50%)
- Extensive late gadolinium enhancement on CMR (>= 15% of LV mass)

## Critical Actions

| Action | Target |
|---|---|
| Defibrillation if VF/VT | Immediate |
| ECG | < 10 minutes |
| Bedside echo | < 30 minutes |
| Avoid vasodilators/inotropes | Immediate |

1. **Cardiac arrest:** Standard ACLS — defibrillation for VF/VT, CPR, epinephrine per protocol
2. **Acute LVOT obstruction with hemodynamic compromise:**
   - IV normal saline bolus 500-1000 mL (increase preload → widen LVOT)
   - Phenylephrine 100-200 mcg IV bolus, then 0.5-2 mcg/kg/min (increase afterload → reduce gradient)
   - Esmolol 500 mcg/kg IV bolus, then 50-200 mcg/kg/min (reduce HR and contractility)
   - Position patient supine with legs elevated
3. **AVOID in obstructive HCM:** Diuretics, vasodilators (nitroglycerin, nitroprusside), inotropes (dobutamine, milrinone), digoxin, IABP — all worsen LVOT obstruction
4. **Atrial fibrillation:** Restore sinus rhythm urgently — loss of atrial contribution is poorly tolerated
   - Amiodarone 150 mg IV over 10 min for rate/rhythm control
   - Synchronized cardioversion 100-200 J if hemodynamically unstable
5. **Anticoagulation for AF** — CHA2DS2-VASc score applies; HCM itself increases stroke risk in AF

## Differential Diagnosis

- **Aortic stenosis** — similar systolic murmur but does NOT increase with Valsalva; carotid upstroke is slow (parvus et tardus) vs brisk in HCM
- **Mitral regurgitation** — pansystolic murmur, radiates to axilla
- **STEMI** — ECG may show similar Q waves and ST-T changes; coronary angiography differentiates
- **Athlete's heart** — physiologic LVH; wall thickness < 15 mm, normal diastolic function, no obstruction
- **Hypertensive cardiomyopathy** — concentric LVH but usually < 15 mm; history of hypertension
- **Cardiac amyloidosis** — infiltrative pattern on echo, low voltage on ECG (opposite of HCM)
- **Subaortic membrane** — fixed obstruction; does not vary with Valsalva

## Workup

- **ECG:** LVH, strain pattern, deep Q waves, LA enlargement
- **Echocardiography:** Asymmetric septal hypertrophy (septum/posterior wall ratio > 1.3), SAM of mitral valve, LVOT gradient (resting and provocable), MR, LV function, LA size
- **Labs:** Troponin (may be elevated from demand ischemia), BNP/NT-proBNP, BMP, CBC
- **Cardiac MRI (non-acute):** Late gadolinium enhancement quantifies fibrosis burden — correlates with SCD risk
- **Holter monitor (outpatient):** Screen for NSVT

## Treatment

### Acute LVOT Obstruction
- IV fluids (NS 500-1000 mL)
- Phenylephrine 100-200 mcg IV bolus (pure alpha-agonist — increases afterload)
- Esmolol 500 mcg/kg bolus, then 50-200 mcg/kg/min
- Trendelenburg positioning

### Chronic Symptomatic Obstructive HCM
- First-line: Non-vasodilating beta-blocker — metoprolol succinate 25-200 mg PO daily or propranolol 40-160 mg PO TID
- Second-line: Verapamil 120-480 mg PO daily (AVOID if resting gradient > 100 mmHg or SBP < 90)
- Disopyramide 100-200 mg PO TID (negative inotrope — reduces LVOT gradient)
- Mavacamten 5 mg PO daily (cardiac myosin inhibitor — FDA-approved 2022, reduces LVOT gradient)
- Septal reduction therapy if refractory: surgical myectomy (gold standard) or alcohol septal ablation

### Atrial Fibrillation
- Rate control: beta-blocker or verapamil (avoid digoxin)
- Rhythm control: amiodarone 200-400 mg PO daily (most effective), or sotalol, flecainide
- Anticoagulation: warfarin or DOAC per CHA2DS2-VASc; lower threshold for anticoagulation in HCM patients

### SCD Prevention
- ICD implantation for secondary prevention (prior VF/sustained VT) — Class I
- ICD for primary prevention: >= 1 major risk factor with shared decision-making — Class IIa
- Exercise restriction: avoid competitive sports (2024 guideline permits shared decision-making for some low-intensity activities)

## Disposition

- **ICU admission:** Cardiac arrest survivor, cardiogenic shock, acute severe LVOT obstruction, hemodynamically unstable AF
- **Telemetry admission:** New-onset AF, syncope in known HCM, new diagnosis with symptoms
- **Discharge with urgent cardiology follow-up:** Known stable HCM with mild symptoms, established on therapy
- **EP/cardiology referral:** All new HCM diagnoses for SCD risk stratification and family screening

## Pitfalls

1. **Administering nitroglycerin or morphine to an HCM patient with chest pain.** Vasodilators and preload-reducing agents worsen LVOT obstruction by reducing ventricular volume, increasing the gradient, and causing hemodynamic collapse. Chest pain in HCM is from demand ischemia — treat with IV fluids and beta-blockers.

2. **Giving digoxin or inotropes for HCM-associated heart failure.** Positive inotropes increase contractility and worsen LVOT obstruction. Even in decompensated HCM, dobutamine and milrinone are contraindicated. IV fluids and beta-blockers are the mainstay.

3. **Misdiagnosing HCM as ACS based on ECG findings.** HCM commonly produces deep Q waves, ST depression, and T-wave inversions that mimic ischemia or prior MI. A young patient with LVH pattern and dynamic murmur needs echocardiography, not emergent cath lab activation (unless STEMI criteria clearly met).

4. **Failing to screen first-degree relatives.** HCM is autosomal dominant with variable penetrance. All first-degree relatives should undergo echocardiography and ECG screening. Genetic testing and counseling should be offered.

5. **Allowing competitive athletics without risk stratification.** HCM is the most common cause of sudden cardiac death in young athletes. Activity recommendations require comprehensive risk assessment including CMR with LGE and ICD discussion.
