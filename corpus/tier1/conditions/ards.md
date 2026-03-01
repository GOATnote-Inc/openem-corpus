---
id: ards
condition: Acute Respiratory Distress Syndrome
aliases: [ARDS, adult respiratory distress syndrome, non-cardiogenic pulmonary edema, acute lung injury]
icd10: [J80]
esi: 1
time_to_harm:
  irreversible_injury: "< 6 hours"
  death: "< 24 hours"
  optimal_intervention_window: "< 2 hours (lung-protective ventilation)"
category: respiratory
track: tier1
sources:
  - type: guideline
    ref: "2024 ATS Clinical Practice Guideline: An Update on Management of Adult Patients With ARDS. Am J Respir Crit Care Med. 2024;209(1):24-36."
  - type: guideline
    ref: "2023 ESICM Guidelines on ARDS Definition, Phenotyping, and Respiratory Support Strategies. Intensive Care Med. 2023;49:727-759."
  - type: review
    ref: "ARDS Definition Task Force. Acute Respiratory Distress Syndrome: The Berlin Definition. JAMA. 2012;307(23):2526-2533."
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
# Acute Respiratory Distress Syndrome

## Recognition

**Berlin Definition criteria (all 4 required):**
1. **Timing:** Within 1 week of known clinical insult or new/worsening respiratory symptoms
2. **Imaging:** Bilateral opacities not fully explained by effusions, lobar/lung collapse, or nodules (CXR or CT)
3. **Origin of edema:** Not fully explained by cardiac failure or fluid overload (echocardiography to exclude)
4. **Oxygenation (on >= 5 cmH2O PEEP):**
   - Mild: P/F 200-300
   - Moderate: P/F 100-200
   - Severe: P/F < 100

**Common precipitants:**
- Pulmonary: pneumonia (most common), aspiration, inhalation injury, pulmonary contusion, near-drowning
- Extrapulmonary: sepsis (most common extrapulmonary), pancreatitis, massive transfusion (TRALI), burns, trauma, DIC

**Clinical presentation:**
- Acute onset dyspnea, tachypnea, hypoxemia refractory to supplemental O2
- Bilateral crackles on auscultation
- Increased work of breathing, accessory muscle use
- Often develops 24-72 hours after precipitating event

## Critical Actions

| Action | Target |
|---|---|
| Lung-protective ventilation | Immediately upon intubation |
| TV 6 mL/kg IBW | Within 30 minutes |
| Plateau pressure | < 30 cmH2O |
| Prone positioning (severe) | Within 12-24 hours |

1. **Intubation when indicated** — worsening hypoxemia despite HFNC/NIV, hemodynamic instability, encephalopathy
2. **Lung-protective ventilation (ARDSNet protocol):**
   - TV 6 mL/kg ideal body weight (may go to 4 mL/kg if Pplat exceeds 30)
   - Plateau pressure < 30 cmH2O
   - Driving pressure < 15 cmH2O (Pplat - PEEP)
   - PEEP per ARDSNet FiO2-PEEP table (higher PEEP strategy for moderate-severe)
   - Target SpO2 88-95%, PaO2 55-80 mmHg
   - Permissive hypercapnia acceptable (pH > 7.20)
3. **Prone positioning** (moderate-severe ARDS, P/F < 150): >= 16 hours/day (PROSEVA trial: 28-day mortality 16% vs 33% supine)
4. **Conservative fluid management** — target even or negative fluid balance once hemodynamically stable (FACTT trial)
5. **Treat underlying cause** — broad-spectrum antibiotics if infectious, source control for sepsis
6. **Corticosteroids** — dexamethasone 20 mg IV daily x 5 days, then 10 mg IV daily x 5 days (2024 ATS: conditional recommendation)
7. **Neuromuscular blockade** — consider cisatracurium 15 mg IV bolus, then 37.5 mg/hr for 48 hours in severe ARDS with P/F < 150 (controversial after ROSE trial — use if severe ventilator dyssynchrony)

## Differential Diagnosis

- **Cardiogenic pulmonary edema** — elevated BNP, S3, JVD, responds to diuresis; PCWP > 18 mmHg. Can coexist with ARDS.
- **Diffuse alveolar hemorrhage** — hemoptysis, dropping hemoglobin, progressively hemorrhagic BAL aliquots
- **Acute eosinophilic pneumonia** — peripheral eosinophilia, BAL eosinophils > 25%, steroid-responsive
- **Cryptogenic organizing pneumonia** — subacute course, migratory infiltrates, steroid-responsive
- **Lymphangitic carcinomatosis** — cancer history, interstitial pattern, progressive
- **Bilateral pneumonia without ARDS** — may meet imaging criteria; P/F ratio distinguishes

## Workup

- **ABG:** P/F ratio calculation (PaO2/FiO2 on current PEEP)
- **CXR (portable):** Bilateral opacities — diffuse, non-lobar distribution
- **CT chest:** If diagnosis uncertain — ground-glass opacities, consolidation, air bronchograms in dependent regions
- **Echocardiography:** Exclude cardiogenic pulmonary edema; assess RV function (ARDS can cause RV failure from high PVR)
- **Labs:** CBC, BMP, lactate, procalcitonin, blood cultures, sputum culture, BNP/NT-proBNP
- **BAL:** If infection etiology unclear, DAH suspected, or eosinophilic pneumonia on differential
- **Static compliance:** < 40 mL/cmH2O typical in ARDS
- **Point-of-care US:** Bilateral B-lines (diffuse), pleural irregularity, reduced lung sliding

## Treatment

### Ventilator Management (ARDSNet Protocol)
- TV: 6 mL/kg IBW (calculate: males = 50 + 2.3[height in inches - 60]; females = 45.5 + 2.3[height in inches - 60])
- RR: 20-35 to maintain minute ventilation (allow permissive hypercapnia)
- PEEP: Start 5-10, titrate per FiO2-PEEP table
- FiO2: Wean to lowest maintaining SpO2 88-95%
- Pplat check q4h: must be < 30 cmH2O; reduce TV to 5 or 4 mL/kg if exceeded
- Driving pressure (Pplat - PEEP): target < 15 cmH2O

### Prone Positioning (Moderate-Severe ARDS)
- Initiate within 12-24 hours if P/F < 150 on FiO2 >= 0.6 and PEEP >= 5
- Duration: >= 16 consecutive hours per session
- Continue daily until P/F > 150 on PEEP <= 10 and FiO2 <= 0.6 in supine
- Contraindications: open abdomen, unstable spine, anterior chest wounds

### Pharmacologic
- Corticosteroids: dexamethasone 20 mg IV daily x 5, then 10 mg IV daily x 5 (2024 ATS conditional recommendation; stronger evidence in COVID ARDS)
- Neuromuscular blockade: cisatracurium for severe dyssynchrony (must have continuous EEG or BIS monitoring, avoid prolonged use > 48h)
- Conservative fluids: target CVP < 4, diurese to even or negative balance when MAP stable off pressors

### Rescue Therapies (Refractory Severe ARDS)
- Inhaled pulmonary vasodilators: inhaled NO 20-40 ppm or inhaled epoprostenol (improves oxygenation but no mortality benefit — bridge therapy)
- Recruitment maneuvers: incremental PEEP (use cautiously — ART trial showed harm with aggressive recruitment)
- VV-ECMO: for P/F < 80 despite optimal ventilation, pH < 7.20 from respiratory acidosis, or refractory hypoxemia (EOLIA trial: consider early referral)

## Disposition

- **ICU admission:** All ARDS patients — mandatory for mechanical ventilation and monitoring
- **ECMO center transfer:** Severe ARDS failing conventional management — early transfer before patient too unstable
- **Prolonged ICU course:** Median 7-14 days on ventilator; prepare for tracheostomy discussion by day 10-14
- **Mortality:** Mild 27%, moderate 32%, severe 45% (Berlin Definition validation cohort)

## Pitfalls

1. **Using tidal volumes based on actual body weight rather than ideal body weight.** Obese patients receive dangerously high tidal volumes if TV is calculated from actual weight. Always use IBW (based on height) for ventilator settings. A 5'4" female weighing 120 kg should receive TV based on ~55 kg IBW, not 120 kg.

2. **Failing to initiate prone positioning in severe ARDS.** Proning reduces mortality by nearly 50% in severe ARDS (PROSEVA trial). Yet it remains underutilized. If P/F < 150 after 12-24 hours of optimized ventilation, prone the patient. The NNT is 6.

3. **Aggressive fluid resuscitation in ARDS.** After initial resuscitation for shock, transition to conservative fluid management. The FACTT trial demonstrated that conservative fluid strategy reduced duration of mechanical ventilation by 2.5 days. Every liter of excess fluid worsens pulmonary edema and oxygenation.

4. **Attributing bilateral infiltrates to "bilateral pneumonia" without calculating P/F ratio.** ARDS is frequently underdiagnosed because providers do not calculate the P/F ratio. Any patient with bilateral opacities and acute hypoxemia should have P/F calculated on current PEEP to determine if Berlin criteria are met.

5. **Delayed ECMO referral.** VV-ECMO should be considered early in severe ARDS (P/F < 80) rather than as a last resort. Transfer to an ECMO center should occur before the patient is too hemodynamically unstable to transport. Contact ECMO center for consultation when P/F remains < 100 despite optimal ventilation including proning.
