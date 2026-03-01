---
id: pulmonary-hypertension-crisis
condition: Pulmonary Hypertension Crisis
aliases: [PH crisis, pulmonary hypertensive crisis, acute pulmonary hypertension decompensation, PAH crisis, right heart failure from PH]
icd10: [I27.0, I27.20, I27.21, I27.29]
esi: 1
time_to_harm:
  irreversible_injury: "< 1 hour"
  death: "< 2 hours"
  optimal_intervention_window: "< 30 minutes"
category: respiratory
track: tier1
sources:
  - type: guideline
    ref: "2022 ESC/ERS Guidelines for the Diagnosis and Treatment of Pulmonary Hypertension. Eur Heart J. 2022;43(38):3618-3731."
  - type: review
    ref: "Hoeper MM, et al. Intensive Care, Right Ventricular Support and Lung Transplantation in Patients With Pulmonary Hypertension. Eur Respir J. 2019;53(1):1801906."
  - type: review
    ref: "Price LC, et al. Management of Pulmonary Hypertension in the Intensive Care Unit. Eur Respir Rev. 2019;28(151):180098."
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
# Pulmonary Hypertension Crisis

## Recognition

**Presentation:**
- Acute dyspnea, hypoxemia, syncope or presyncope
- Systemic hypotension from RV failure (SBP < 90)
- Elevated JVP, peripheral edema, hepatomegaly
- Clear lung fields (RV failure, not LV failure)
- Loud P2, right-sided S3/S4, tricuspid regurgitation murmur
- Altered mental status from low cardiac output

**Precipitants:**
- Medication non-compliance or abrupt PH medication withdrawal (especially IV prostacyclins — can be rapidly fatal)
- Infection/sepsis
- Pulmonary embolism (superimposed on chronic PH)
- Arrhythmia (especially atrial fibrillation/flutter — loss of atrial kick is poorly tolerated)
- Surgery or anesthesia (positive pressure ventilation increases RV afterload)
- Pregnancy (absolute contraindication in severe PAH)
- Volume overload

**Hemodynamics:**
- Mean PA pressure > 25 mmHg (often > 60 mmHg in crisis)
- Cardiac index < 2.0 L/min/m2
- CVP > 15 mmHg
- Mixed venous O2 saturation < 60% (ominous)

## Critical Actions

| Action | Target |
|---|---|
| Bedside echo | < 10 minutes |
| Restore PH-specific therapy | Immediate |
| Inhaled pulmonary vasodilator | < 15 minutes |
| Vasopressor for systemic BP | < 10 minutes |

1. **Do NOT withdraw PH-specific therapy** — if patient on IV epoprostenol or treprostinil, ensure infusion is running and central line is patent. Abrupt prostacyclin withdrawal can cause fatal rebound PH.
2. **Inhaled pulmonary vasodilator:**
   - Inhaled nitric oxide 20-40 ppm (selective pulmonary vasodilator — no systemic hypotension)
   - OR inhaled epoprostenol 20,000-50,000 ng/mL continuously nebulized at 50 mL/hr
3. **Systemic vasopressor to maintain RV coronary perfusion:**
   - Norepinephrine 0.05-0.5 mcg/kg/min IV (first-line — maintains systemic BP without significantly increasing PVR)
   - Vasopressin 0.01-0.04 units/min IV (does not increase PVR; good adjunct)
   - AVOID phenylephrine (pure alpha-agonist increases PVR)
4. **Inotropic support for RV failure:**
   - Dobutamine 2-10 mcg/kg/min IV (augments RV contractility + mild pulmonary vasodilation)
   - Milrinone 0.375-0.75 mcg/kg/min IV (phosphodiesterase-3 inhibitor — inotropy + pulmonary vasodilation; loading dose often omitted due to hypotension)
5. **Cautious IV fluid** — 250 mL NS bolus ONLY if clearly hypovolemic (low CVP). Excessive fluid worsens RV dilation and septal shift.
6. **Avoid intubation if possible** — positive pressure ventilation dramatically increases RV afterload. If unavoidable: pre-treat with norepinephrine, use low PEEP, avoid hypercapnia, low tidal volumes.
7. **Treat precipitant:** Infection → antibiotics; PE → anticoagulation/thrombolysis; AF → restore sinus rhythm (amiodarone 150 mg IV); medication non-compliance → restart therapy immediately

## Differential Diagnosis

- **Massive PE** — acute onset, may have chronic PH as substrate; CTA diagnostic
- **Acute RV myocardial infarction** — ST elevation in V4R, troponin elevation; coronary angiography
- **Cardiac tamponade** — pulsus paradoxus, equalized diastolic pressures; echo diagnostic
- **Acute decompensated heart failure (LV)** — bilateral crackles, elevated PCWP
- **Septic shock** — distributive pattern; may precipitate RV failure in PH patients
- **Tension pneumothorax** — absent breath sounds, tracheal deviation

## Workup

- **Bedside echocardiography:** RV dilation and hypertrophy, RV:LV ratio > 1, D-shaped septum (pressure overload), TAPSE < 17 mm, tricuspid regurgitation velocity (estimate PASP), pericardial effusion (ominous)
- **ECG:** RV strain (T-wave inversions V1-V4), right axis deviation, RVH, P-pulmonale, atrial arrhythmias
- **Labs:** BNP/NT-proBNP (prognostic marker; > 1000 pg/mL = severe), troponin (RV ischemia), lactate, BMP, LFTs (hepatic congestion)
- **ABG:** Hypoxemia, possible hypercapnia
- **CTA chest:** If PE on differential
- **Right heart catheterization:** Definitive hemodynamics — defer until stabilized unless needed to guide management acutely
- **Mixed venous O2 saturation:** < 60% = critically low cardiac output

## Treatment

### Hemodynamic Support
- Norepinephrine 0.05-0.5 mcg/kg/min (first-line vasopressor)
- Vasopressin 0.01-0.04 units/min (adjunct; PVR-neutral)
- Dobutamine 2-10 mcg/kg/min (RV inotropy)
- Milrinone 0.375-0.75 mcg/kg/min (inotropy + pulmonary vasodilation)

### Pulmonary Vasodilation
- Inhaled nitric oxide 20-40 ppm (first-line for acute PH crisis in ICU)
- Inhaled epoprostenol via continuous nebulization (alternative, less expensive than iNO)
- IV epoprostenol 1-2 ng/kg/min, titrate up slowly (for severe PAH decompensation — requires central line, ICU monitoring)
- IV treprostinil as alternative to epoprostenol

### Arrhythmia Management
- AF/flutter: restore sinus rhythm urgently — synchronized cardioversion if unstable; amiodarone 150 mg IV over 10 min then 1 mg/min x 6 hours for rhythm control
- Avoid beta-blockers (reduce RV contractility — contraindicated in decompensated PH)
- Avoid calcium channel blockers (except in rare responders identified by formal vasoreactivity testing)

### Mechanical Circulatory Support
- VA-ECMO for refractory shock as bridge to recovery or transplant
- Right ventricular assist device (RVAD) in select cases

### AVOID
- Aggressive fluid loading (worsens RV dilation → septal shift → LV compression)
- Intubation if possible (positive pressure ventilation worsens PH)
- Phenylephrine (increases PVR)
- Beta-blockers (reduce RV contractility)

## Disposition

- **ICU admission:** All PH crisis patients — continuous hemodynamic monitoring, vasopressor/inotrope management
- **PH specialty center transfer:** Patients with known PH decompensating at non-specialty facility. Contact PH center for guidance.
- **Do NOT transfer unstable patients** — stabilize first, then arrange critical care transport with ongoing vasopressors and inhaled vasodilators
- **Mortality:** In-hospital mortality for PH crisis with cardiogenic shock is 30-50%

## Pitfalls

1. **Abruptly discontinuing IV prostacyclin (epoprostenol/treprostinil).** Even brief interruptions (minutes) can cause fatal rebound pulmonary hypertension. If a PH patient presents with a malfunctioning pump, central line occlusion, or empty medication cassette, this is a life-threatening emergency. Restart prostacyclin immediately — if IV access unavailable, use SC treprostinil or inhaled epoprostenol as bridge.

2. **Volume loading a patient in PH crisis.** The RV in PH is already volume-overloaded and pressure-overloaded. Additional fluid worsens RV dilation, shifts the septum, and compresses the LV — reducing cardiac output further. Give fluids only if CVP is clearly low and patient is hypovolemic.

3. **Intubating without hemodynamic preparation.** Positive pressure ventilation in PH crisis can precipitate cardiovascular collapse. The combination of increased RV afterload (from positive pressure) and decreased preload (from reduced venous return) is lethal. If intubation is unavoidable: pre-treat with vasopressors, use low PEEP, avoid induction agents that cause vasodilation (propofol), and prepare for peri-intubation arrest.

4. **Using phenylephrine for hypotension.** Phenylephrine is a pure alpha-agonist that increases systemic vascular resistance AND pulmonary vascular resistance. This worsens RV afterload. Use norepinephrine (which has beta-1 inotropic effects) or vasopressin (PVR-neutral) instead.

5. **Diagnosing PH crisis as "just COPD exacerbation" without echo.** Patients with group 3 PH (from lung disease) can decompensate with right heart failure superimposed on a COPD exacerbation. Bedside echo showing RV dilation with septal bowing changes management entirely. Always echo the dyspneic patient who is not responding to standard bronchodilator therapy.
