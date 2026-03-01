---
id: takotsubo-cardiomyopathy
condition: Takotsubo Cardiomyopathy
aliases: [stress cardiomyopathy, broken heart syndrome, apical ballooning syndrome, takotsubo syndrome]
icd10: [I51.81]
esi: 2
time_to_harm: "< 6 hours (cardiogenic shock, arrhythmia)"
category: cardiovascular
track: tier1
sources:
  - type: review
    ref: "Templin C, et al. Clinical Features and Outcomes of Takotsubo (Stress) Cardiomyopathy. N Engl J Med. 2015;373(10):929-938."
  - type: review
    ref: "Ghadri JR, et al. International Expert Consensus Document on Takotsubo Syndrome. Eur Heart J. 2018;39(22):2032-2046."
  - type: guideline
    ref: "2020 ESC Position Statement on Takotsubo Syndrome. Eur Heart J. 2020."
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
# Takotsubo Cardiomyopathy

## Recognition

**Typical presentation:**
- Postmenopausal woman (90% female, mean age 65-70)
- Preceded by intense emotional stress (grief, fear, anger) or physical stress (surgery, critical illness, ICU admission)
- Chest pain mimicking ACS
- Dyspnea, syncope
- ECG changes mimicking STEMI (ST elevation, T-wave inversion, QT prolongation)
- Mild troponin elevation (disproportionately low relative to degree of wall motion abnormality)
- BNP/NT-proBNP markedly elevated

**InterTAK Diagnostic Score (>= 70 = high probability):**
- Female sex (+25)
- Emotional trigger (+24)
- Physical trigger (+13)
- Absence of ST depression (except aVR) (+12)
- Psychiatric disorder history (+11)
- Neurologic disorder (+9)
- QTc prolongation (+6)

**Wall motion patterns:**
- Classic apical ballooning (75-80%) — apical akinesis/dyskinesis with basal hyperkinesis
- Midventricular variant (15%) — midwall akinesis
- Basal/reverse variant (5%) — basal akinesis with apical hyperkinesis
- Focal variant (rare)

**Modified Mayo Clinic Criteria:**
1. Transient LV wall motion abnormalities extending beyond single coronary territory
2. Absence of obstructive coronary disease or angiographic evidence of acute plaque rupture
3. New ECG abnormalities or modest troponin elevation
4. Absence of pheochromocytoma or myocarditis

## Critical Actions

| Action | Target |
|---|---|
| 12-lead ECG | < 10 minutes |
| Troponin | < 30 minutes |
| Treat as ACS until proven otherwise | Immediate |
| Echocardiography | < 2 hours |

1. **Treat as ACS initially** — STEMI-like presentation requires cath lab activation per STEMI protocol
2. **Coronary angiography** — required to exclude acute coronary occlusion; typically shows normal coronaries or non-obstructive disease
3. **Left ventriculography** during cath — classic apical ballooning pattern confirms diagnosis
4. **Echocardiography** — if cath lab not immediately available; document wall motion abnormality pattern
5. **Hemodynamic monitoring** — risk of LVOT obstruction (10-25%), cardiogenic shock (5-10%), LV thrombus
6. **Monitor for QTc prolongation** — risk of torsades de pointes; avoid QT-prolonging medications
7. **Correct underlying stressor** if physical trigger (sepsis, surgery, pheochromocytoma)

## Differential Diagnosis

- **STEMI** — cannot differentiate from takotsubo by ECG alone; coronary angiography required
- **Myocarditis** — younger patients, viral prodrome; cardiac MRI differentiates (late gadolinium enhancement pattern differs)
- **Pheochromocytoma** — catecholamine surge can cause identical wall motion abnormalities; must be excluded
- **ACS (NSTEMI)** — troponin elevation with obstructive coronary disease
- **Hypertrophic cardiomyopathy with obstruction** — may present similarly; echo differentiates
- **Subarachnoid hemorrhage** — can cause ECG changes and wall motion abnormalities via catecholamine surge

## Workup

- **12-lead ECG:** ST elevation (most common), diffuse T-wave inversions, QTc prolongation. Patterns often evolve over days.
- **Troponin:** Mild elevation (typically peak < 10x ULN). Markedly elevated troponin suggests true MI.
- **BNP/NT-proBNP:** Often markedly elevated (> 1000 pg/mL), disproportionate to troponin
- **Coronary angiography + left ventriculography:** Definitive — normal coronaries with characteristic wall motion abnormality
- **Echocardiography:** Regional wall motion abnormalities extending beyond single coronary territory; assess for LVOT obstruction (SAM of mitral valve), LV thrombus, MR
- **Cardiac MRI:** If diagnosis uncertain — distinguishes from myocarditis (no late gadolinium enhancement in acute phase of takotsubo, vs patchy in myocarditis)
- **Labs:** CBC, BMP, TSH, cortisol, plasma metanephrines (if pheochromocytoma suspected), coagulation studies
- **Serial ECGs:** QTc monitoring (risk of TdP peaks day 2-3)

## Treatment

### Hemodynamically Stable
- Supportive care — most recover in 1-4 weeks
- Beta-blocker: metoprolol 12.5-25 mg PO BID (if no LVOT obstruction or cardiogenic shock)
- ACE inhibitor: lisinopril 2.5-5 mg PO daily (for LV dysfunction)
- Diuretics: furosemide 20-40 mg IV PRN for pulmonary congestion
- Avoid catecholamines (dobutamine, milrinone, epinephrine) — may worsen catecholamine-mediated injury

### LVOT Obstruction (10-25% of cases)
- **AVOID** inotropes, vasodilators, diuretics, IABP — all worsen dynamic LVOT obstruction
- IV fluids for volume loading
- Phenylephrine 40-100 mcg IV bolus, then 0.5-2 mcg/kg/min (pure alpha-agonist increases afterload, reduces LVOT gradient)
- Esmolol 500 mcg/kg bolus then 50-200 mcg/kg/min (reduces contractility, widens LVOT)

### Cardiogenic Shock WITHOUT LVOT Obstruction
- Volume resuscitation first
- If vasopressors needed: norepinephrine 0.05-0.5 mcg/kg/min (preferred over dobutamine)
- Mechanical support (IABP, Impella) if refractory — but FIRST exclude LVOT obstruction by echo
- Levosimendan 0.1 mcg/kg/min IV (calcium sensitizer, available in some centers — preserves hemodynamics without catecholamine excess)

### LV Thrombus (incidence ~2-5%)
- Anticoagulation: heparin bridge to warfarin (target INR 2-3) for 3 months
- Repeat echo at 3 months to confirm resolution

### QTc Prolongation
- Hold ALL QT-prolonging medications
- Target K+ > 4.0, Mg2+ > 2.0
- If TdP develops: magnesium 2 g IV, overdrive pacing

## Disposition

- **ICU/CCU admission:** Cardiogenic shock, LVOT obstruction, severe LV dysfunction (EF < 30%), arrhythmias, LV thrombus
- **Telemetry admission:** Stable takotsubo with mild-moderate LV dysfunction, QTc monitoring
- **Follow-up echo:** At 1-3 months to confirm recovery (LV function normalizes in 95% within 4-8 weeks)
- **Recurrence rate:** ~5-10% lifetime; no proven prevention strategy

## Pitfalls

1. **Treating takotsubo-associated cardiogenic shock with inotropes/catecholamines.** Dobutamine and milrinone can worsen catecholamine-mediated myocardial injury and exacerbate LVOT obstruction. Volume resuscitation and mechanical support are preferred.

2. **Missing LVOT obstruction.** Up to 25% of takotsubo patients develop dynamic LVOT obstruction from basal hyperkinesis and SAM of the mitral valve. This changes management fundamentally — inotropes, vasodilators, IABP, and diuretics are all contraindicated. Bedside echo with Doppler across the LVOT must be performed before starting any hemodynamic support.

3. **Dismissing takotsubo as benign.** In-hospital mortality is 4-5%, comparable to ACS. Complications include cardiogenic shock, arrhythmias (VT/VF, TdP), LV thrombus with embolism, LV rupture (rare), and RV involvement (affects 25%). This is not a benign diagnosis.

4. **Failing to exclude pheochromocytoma.** Catecholamine-producing tumors can cause wall motion abnormalities identical to takotsubo. Plasma metanephrines should be checked, especially if there is no clear emotional/physical trigger or if episodes are recurrent.

5. **Not monitoring QTc.** QTc prolongation is common (mean ~500 ms) and peaks at day 2-3. TdP can occur. All QT-prolonging drugs should be stopped, and electrolytes should be optimized.
