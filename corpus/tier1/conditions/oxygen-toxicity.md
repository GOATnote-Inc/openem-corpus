---
id: oxygen-toxicity
condition: Oxygen Toxicity
aliases: [hyperoxia, oxygen-induced lung injury, pulmonary oxygen toxicity, Lorrain Smith effect, Paul Bert effect]
icd10: [T59.891A]
esi: 3
time_to_harm: "< 24 hours (pulmonary toxicity at FiO2 > 0.6)"
category: respiratory
track: tier1
sources:
  - type: review
    ref: "Kallet RH, Matthay MA. Hyperoxic Acute Lung Injury. Respir Care. 2013;58(1):123-141."
  - type: review
    ref: "Chu DK, et al. Mortality and Morbidity in Acutely Ill Adults Treated with Liberal Versus Conservative Oxygen Therapy (IOTA Systematic Review and Meta-Analysis). Lancet. 2018;391(10131):1693-1705."
  - type: review
    ref: "Girardis M, et al. Effect of Conservative vs Conventional Oxygen Therapy on Mortality Among Patients in an Intensive Care Unit (Oxygen-ICU Trial). JAMA. 2016;316(15):1583-1589."
last_updated: "2026-03-01"
compiled_by: agent
risk_tier: C
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
# Oxygen Toxicity

## Recognition

**Pulmonary oxygen toxicity (Lorrain Smith effect):**
- Occurs with prolonged exposure to FiO2 > 0.6 for > 24-48 hours
- Tracheobronchitis (early): substernal chest pain, cough, dyspnea
- Diffuse alveolar damage (late): ARDS-like picture with bilateral infiltrates, progressive hypoxemia
- Pathology: reactive oxygen species (ROS) damage to alveolar epithelium, surfactant dysfunction, interstitial edema

**CNS oxygen toxicity (Paul Bert effect):**
- Occurs at hyperbaric oxygen pressures (> 1.6 ATA) — relevant in diving and hyperbaric chambers
- Seizures (generalized tonic-clonic), visual disturbances, tinnitus, nausea, muscle twitching
- May occur without warning prodrome

**Retinopathy of prematurity (ROP):**
- Neonatal concern with high FiO2 in premature infants (< 32 weeks gestational age)
- Not an adult ED presentation but relevant to neonatal resuscitation decisions

**Clinical settings of concern:**
- ICU patients on prolonged high FiO2 (common — frequently overlooked)
- Post-cardiac arrest with hyperoxia (PaO2 > 300 mmHg — associated with worse neurologic outcomes)
- COPD patients receiving uncontrolled high-flow O2 (CO2 retention AND O2 toxicity)
- Hyperbaric oxygen therapy sessions

**Evidence for harm of liberal oxygen:**
- IOTA meta-analysis (2018): liberal O2 (SpO2 > 96%) associated with increased mortality in acutely ill adults (OR 1.21)
- Oxygen-ICU trial (2016): conservative O2 (SpO2 94-98%) reduced ICU mortality vs conventional (SpO2 up to 100%)
- DETO2X-AMI trial: no benefit of supplemental O2 in MI patients with SpO2 >= 90%

## Critical Actions

| Action | Target |
|---|---|
| Wean FiO2 to lowest effective level | Immediately upon recognition |
| Target SpO2 | 92-96% (88-92% in COPD) |
| Assess for underlying cause of O2 dependence | < 2 hours |

1. **Wean FiO2** to the lowest level maintaining SpO2 92-96% (or 88-92% in COPD with chronic CO2 retention)
2. **Avoid hyperoxia** (PaO2 > 100 mmHg) in acutely ill patients — no benefit, potential harm
3. **Post-cardiac arrest:** Titrate O2 to SpO2 94-98% as soon as ROSC is established and reliable SpO2 monitoring is available
4. **If CNS toxicity (hyperbaric):** Remove from hyperbaric environment immediately; seizures are self-limited once O2 pressure is reduced. Maintain airway, benzodiazepines for prolonged seizures.
5. **Treat underlying cause of hypoxemia** rather than simply increasing FiO2

## Differential Diagnosis

- **ARDS** — may be the actual diagnosis in a patient on high FiO2; oxygen toxicity can both mimic and worsen ARDS
- **Ventilator-induced lung injury (VILI)** — occurs concurrently with oxygen toxicity in mechanically ventilated patients
- **Worsening underlying pulmonary disease** — progression of pneumonia, PE, or primary lung disease
- **Atelectasis** — absorption atelectasis occurs with high FiO2 (nitrogen washout)
- **Pulmonary edema** — cardiogenic or non-cardiogenic; may overlap

## Workup

- **ABG:** PaO2 (aim 55-80 mmHg in ARDS; avoid > 100 mmHg in all acutely ill), PaCO2, pH
- **CXR:** Progressive bilateral infiltrates in a patient on high FiO2 > 24-48 hours — oxygen toxicity vs ARDS progression (difficult to distinguish)
- **SpO2 monitoring:** Continuous; wean FiO2 to target
- **Calculate FiO2 exposure time:** Duration above 0.6 FiO2 is the key determinant of pulmonary toxicity risk
- **Echocardiography:** Rule out cardiogenic pulmonary edema as alternative explanation

## Treatment

### Prevention (Primary Strategy)
- Minimize FiO2 to maintain SpO2 92-96% (88-92% in COPD)
- Use PEEP optimization to reduce FiO2 requirement (alveolar recruitment allows lower FiO2 for same PaO2)
- Prone positioning in ARDS — improves V/Q matching, reduces FiO2 requirement
- Accept permissive hypoxemia (SpO2 88-92%) in ARDS rather than sustained FiO2 > 0.6
- VV-ECMO consideration in severe ARDS to allow "lung rest" at low FiO2

### Management of Established Pulmonary O2 Toxicity
- Wean FiO2 aggressively — even marginal reductions (0.8 → 0.6) are protective
- Optimize PEEP to improve oxygenation without increasing FiO2
- Lung-protective ventilation: TV 6 mL/kg IBW, Pplat < 30 cmH2O
- Treat underlying disease to reduce O2 dependency
- Pulmonary O2 toxicity is often reversible if FiO2 is reduced before extensive fibrosis develops

### CNS Oxygen Toxicity (Hyperbaric)
- Remove from hyperbaric environment
- Maintain airway — lateral recovery position
- Benzodiazepines (midazolam 5 mg IV) for prolonged seizures (most are self-limited once O2 pressure is reduced)
- Do not restart hyperbaric O2 until seizure cause evaluated

## Disposition

- **ICU monitoring:** All patients requiring FiO2 > 0.6 for > 24 hours — daily reassessment of FiO2 requirement
- **Respiratory therapy consultation:** Optimize ventilator settings to minimize FiO2
- **Consider VV-ECMO referral:** If unable to wean FiO2 below 0.6 despite optimal ventilator management and proning
- **Outpatient considerations:** Home O2 patients should be prescribed specific liter flow; excessive home O2 can contribute to oxygen toxicity over time

## Pitfalls

1. **Leaving patients on FiO2 1.0 after ROSC without weaning.** Post-cardiac arrest hyperoxia (PaO2 > 300 mmHg) is associated with increased mortality and worse neurologic outcomes. FiO2 should be titrated to SpO2 94-98% as soon as reliable oximetry is available after ROSC.

2. **Treating the SpO2 number rather than the patient.** Chasing SpO2 > 96% with increasing FiO2 in ARDS is harmful. Conservative oxygen targets (SpO2 88-95%) are not only safe but associated with better outcomes. Permissive hypoxemia should be accepted before harmful levels of FiO2.

3. **Attributing worsening oxygenation to disease progression without considering iatrogenic O2 toxicity.** In a patient on FiO2 > 0.6 for > 48 hours with worsening bilateral infiltrates, oxygen toxicity should be on the differential. The appropriate response may be to DECREASE FiO2 (and optimize PEEP/proning) rather than increase it.

4. **Ignoring absorption atelectasis from high FiO2.** At FiO2 1.0, nitrogen is washed out of alveoli. Without nitrogen to splint them open, alveoli collapse. This creates a vicious cycle: atelectasis → worsened hypoxemia → increased FiO2 → more atelectasis. PEEP and recruitment maneuvers break this cycle.

5. **Providing uncontrolled high-flow O2 to COPD patients.** Beyond CO2 narcosis risk, prolonged high FiO2 causes the same pulmonary toxicity in COPD patients. Target SpO2 88-92% in known retainers, and use Venturi masks for precise FiO2 delivery.
