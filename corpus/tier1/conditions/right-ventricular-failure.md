---
id: right-ventricular-failure
condition: Acute Right Ventricular Failure
aliases: [RV failure, acute RV dysfunction, right heart failure, RV infarction, cor pulmonale acute]
icd10: [I50.810, I50.811, I50.813]
esi: 1
time_to_harm:
  irreversible_injury: "< 2 hours"
  death: "< 6 hours"
  optimal_intervention_window: "< 1 hour"
category: cardiovascular
track: tier1
sources:
  - type: review
    ref: "Harjola VP, et al. Contemporary Management of Acute Right Ventricular Failure: A Statement from the Heart Failure Association and the Working Group on Pulmonary Circulation and Right Ventricular Function of the ESC. Eur J Heart Fail. 2016;18(3):226-241."
  - type: review
    ref: "Lahm T, et al. Assessment of Right Ventricular Function in the Research Setting: Knowledge Gaps and Pathways to Progress. An NHLBI Workshop Report. Am J Respir Crit Care Med. 2018;198(4):e15-e29."
  - type: guideline
    ref: "2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure. J Am Coll Cardiol. 2022;79(17):e263-e421."
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
# Acute Right Ventricular Failure

## Recognition

**Presentation:**
- Hypotension, tachycardia, cardiogenic shock
- Elevated JVP, hepatojugular reflux
- Peripheral edema, hepatomegaly, ascites (in subacute/chronic decompensation)
- Clear lung fields (unlike LV failure) — critical distinguishing feature
- Right-sided S3 gallop
- Tricuspid regurgitation murmur (pansystolic, increases with inspiration — Carvallo sign)

**Hemodynamic profile:**
- Elevated CVP (> 15 mmHg)
- Low cardiac output, low mixed venous O2 saturation
- Normal or low PCWP (unless biventricular failure)
- RV dilation with septal shift compressing LV (ventricular interdependence)

**Common acute etiologies:**
- **Massive pulmonary embolism** — most common acute cause; sudden onset dyspnea, pleuritic chest pain
- **RV myocardial infarction** — inferior MI extending to RV; ST elevation in V4R
- **Acute respiratory distress syndrome** — hypoxic pulmonary vasoconstriction
- **Acute pulmonary hypertension crisis** — decompensation of chronic PH
- **Post-cardiac surgery** — post-cardiotomy, post-transplant
- **Tension pneumothorax** — impaired venous return
- **Sepsis** — RV depression from circulating inflammatory mediators

## Critical Actions

| Action | Target |
|---|---|
| Bedside echo | < 15 minutes |
| Identify etiology | < 30 minutes |
| Volume optimization | < 30 minutes |
| Vasopressor initiation if shock | < 15 minutes |

1. **Identify and treat the underlying cause** — PE requires thrombolysis/embolectomy, RV MI requires PCI, pneumothorax requires decompression
2. **Optimize RV preload** — cautious fluid challenge (250-500 mL NS over 15-30 min) if CVP low. AVOID volume overloading — excessive preload worsens RV dilation and septal shift, reducing LV filling
3. **Vasopressors to maintain RV coronary perfusion:**
   - Norepinephrine 0.05-0.5 mcg/kg/min IV (maintains systemic BP and RV coronary perfusion, mild inotropic effect) — first-line
   - Vasopressin 0.01-0.04 units/min IV (does not increase PVR)
4. **Inotropic support:**
   - Dobutamine 2.5-10 mcg/kg/min IV (augments RV contractility; avoid in hypotension without vasopressor)
   - Milrinone 0.375-0.75 mcg/kg/min IV (inotropy + pulmonary vasodilation; loading dose often omitted due to hypotension risk)
5. **Reduce RV afterload:**
   - Inhaled nitric oxide 20-40 ppm (selective pulmonary vasodilator, no systemic hypotension)
   - Inhaled epoprostenol 20,000-50,000 ng/mL at 50 mL/hr via continuous nebulization
6. **Avoid intubation if possible** — positive pressure ventilation reduces venous return and increases RV afterload. If intubating: low tidal volumes (6 mL/kg), low PEEP, avoid hypercapnia.
7. **Mechanical support:** VA-ECMO for refractory cardiogenic shock as bridge to recovery or definitive therapy

## Differential Diagnosis

- **Cardiac tamponade** — equalization of diastolic pressures, pulsus paradoxus, Beck triad
- **Constrictive pericarditis** — Kussmaul sign, pericardial knock
- **Massive PE** — acute onset dyspnea, tachycardia; RV dilation on echo; CTA diagnostic
- **Inferior MI with RV involvement** — ST elevation inferior leads and V4R; coronary angiography diagnostic
- **Tension pneumothorax** — tracheal deviation, absent breath sounds; needle decompression diagnostic and therapeutic
- **Severe sepsis** — distributive shock with RV depression; volume resuscitation and antibiotics
- **Left ventricular failure** — bilateral crackles, elevated PCWP; echo differentiates

## Workup

- **Bedside echocardiography:** RV dilation (RV:LV ratio > 1), RV hypokinesis, septal bowing into LV, tricuspid regurgitation, McConnell sign (RV free wall akinesis with apical sparing — suggests PE), TAPSE < 17 mm (RV systolic dysfunction)
- **ECG:** Right axis deviation, RV strain (T-wave inversions V1-V4), S1Q3T3 (PE), ST elevation V4R (RV MI), low voltage (tamponade)
- **CTA chest:** If PE suspected
- **Labs:** Troponin, BNP/NT-proBNP, BMP, lactate, ABG, CBC, coagulation studies
- **Right heart catheterization (if available):** CVP, PA pressures, PCWP, cardiac output — definitive hemodynamic assessment
- **Chest X-ray:** Enlarged cardiac silhouette, clear lung fields (vs bilateral infiltrates in LV failure)

## Treatment

### PE-Induced RV Failure
- Systemic thrombolysis: alteplase 100 mg IV over 2 hours (if massive PE with hemodynamic instability)
- Catheter-directed therapy or surgical embolectomy if thrombolysis contraindicated or fails
- Anticoagulation: heparin 80 units/kg bolus, then 18 units/kg/hr

### RV Myocardial Infarction
- Aggressive IV fluid resuscitation (NS 1-2 L bolus) — RV is preload-dependent
- AVOID nitroglycerin, diuretics, morphine (reduce preload → hemodynamic collapse)
- Emergent PCI for right coronary artery (most common culprit)
- Dobutamine 2-10 mcg/kg/min for refractory hypotension after volume loading

### Acute Pulmonary Hypertension Crisis
- Inhaled nitric oxide 20-40 ppm or inhaled epoprostenol
- IV epoprostenol 1-2 ng/kg/min, titrate (for severe decompensation)
- Avoid systemic vasodilators (cause dangerous hypotension)
- Norepinephrine for systemic perfusion

### General RV Support
- Maintain sinus rhythm — loss of atrial kick worsens RV function
- Correct hypoxemia and hypercapnia (both increase PVR)
- Minimize PEEP and inspiratory pressures if intubated
- VA-ECMO for refractory shock

## Disposition

- **ICU admission:** All acute RV failure with hemodynamic compromise
- **Cardiac catheterization lab:** RV MI for PCI, PE for catheter-directed therapy
- **Transfer:** Facilities without cardiac surgery, ECMO capability, or interventional cardiology
- **Never discharge:** Acute RV failure requires intensive monitoring and treatment of the underlying cause

## Pitfalls

1. **Aggressive fluid resuscitation in RV failure.** Unlike LV failure, the RV may initially be preload-responsive (especially in RV MI). However, excessive volume overloads the dilated RV, shifts the septum leftward, compresses the LV, and further reduces cardiac output. Fluid challenges should be small (250 mL) and reassessed by echo or CVP.

2. **Intubating without hemodynamic preparation.** Positive pressure ventilation increases RV afterload and reduces preload — potentially lethal in acute RV failure. If intubation is unavoidable, pre-treat with vasopressors (norepinephrine running before induction), use low-dose sedation, and minimize PEEP.

3. **Giving nitroglycerin or diuretics in RV myocardial infarction.** The RV in acute MI is preload-dependent. Reducing preload with nitrates, diuretics, or morphine causes precipitous hypotension. The classic teaching is: inferior MI + hypotension + clear lungs + elevated JVP = think RV infarction → give fluids, NOT diuretics.

4. **Missing RV infarction by not obtaining right-sided leads.** Standard 12-lead ECG may show only inferior STEMI. V4R (right-sided V4) is the single most sensitive lead for RV infarction — ST elevation >= 1 mm in V4R is diagnostic. Always obtain right-sided leads in inferior MI.

5. **Using systemic pulmonary vasodilators instead of inhaled agents.** IV vasodilators (sildenafil, epoprostenol IV in excess) cause systemic hypotension which reduces RV coronary perfusion pressure. Inhaled nitric oxide and inhaled epoprostenol selectively reduce PVR without systemic effects.
