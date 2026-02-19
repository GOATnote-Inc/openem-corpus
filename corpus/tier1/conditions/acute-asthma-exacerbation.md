---
id: acute-asthma-exacerbation
condition: Acute Asthma Exacerbation
aliases: [asthma attack, acute severe asthma, status asthmaticus, asthma flare, acute bronchospasm]
icd10: [J45.21, J45.31, J45.41, J45.51, J45.901, J45.902]
esi: 2
time_to_harm: "< 30 minutes"
mortality_if_delayed: "Near-fatal asthma progresses to respiratory arrest within minutes; ~3,500 US deaths/year"
category: respiratory
track: tier1
sources:
  - type: guideline
    ref: "2023 Global Initiative for Asthma (GINA) Report: Global Strategy for Asthma Management and Prevention"
    url: "https://ginasthma.org/gina-reports/"
  - type: guideline
    ref: "2020 NIH National Asthma Education and Prevention Program (NAEPP) Expert Panel Report 4 (EPR-4) Focused Updates"
  - type: pubmed
    ref: "Rowe BH et al. Magnesium sulfate for treating exacerbations of acute asthma in the emergency department. Cochrane Database Syst Rev. 2000;(2):CD001490"
    pmid: "10796650"
  - type: pubmed
    ref: "Rodrigo GJ et al. Acute asthma in adults: a review. Chest. 2004;125(3):1081-1102"
    pmid: "15006973"
  - type: pubmed
    ref: "Camargo CA Jr et al. Managing asthma exacerbations in the emergency department: summary of the NAEPP Expert Panel Report 3 guidelines for the management of asthma exacerbations. J Emerg Med. 2009;37(2 Suppl):S6-S17"
    pmid: "19683665"
last_updated: "2026-02-18"
compiled_by: agent
risk_tier: B
validation:
  automated_consistency_check: "2026-02-18"
  dose_range_validator: "2026-02-19"
  unit_normalization_check: "2026-02-19"
  cross_file_consistency_check: "2026-02-19"
  citation_presence_check: "2026-02-19"
  duplicate_content_check: "2026-02-19"
  outlier_detection_flag: clear
  schema_version: "2.0"
  guideline_version_reference: null
  provenance_links: []
---
# Acute Asthma Exacerbation

## Recognition

**Severity classification:**

| Feature | Mild-Moderate | Severe | Life-Threatening |
|---|---|---|---|
| Speaks | Sentences | Words/phrases | Unable to speak |
| Respiratory rate | Increased | > 30/min | Variable, may be decreasing |
| Heart rate | < 120 | > 120 | Bradycardia (ominous) |
| SpO2 | > 92% | 90-92% | < 90% |
| PEF | > 50% predicted | 25-50% predicted | < 25% or unmeasurable |
| Accessory muscle use | Some | Significant | Paradoxical thoracoabdominal movement |
| Mental status | Alert, anxious | Agitated | Drowsy, confused |
| Auscultation | Expiratory wheeze | Inspiratory and expiratory wheeze | Silent chest (no air movement) |

**Life-threatening signs (impending respiratory arrest):**
- Silent chest on auscultation
- Inability to speak
- Bradycardia or hemodynamic instability
- Drowsiness, confusion, exhaustion
- Paradoxical thoracoabdominal movement
- Absence of tachycardia in severe distress
- PaCO2 normal or elevated (should be LOW in acute asthma from hyperventilation; normalization = fatigue and impending failure)

**Risk factors for fatal/near-fatal asthma:**
- Prior intubation or ICU admission for asthma
- >= 2 hospitalizations or >= 3 ED visits for asthma in past year
- Current or recent oral corticosteroid use
- Not using inhaled corticosteroids
- Overuse of SABA (> 1 canister/month)
- Psychiatric disease, psychosocial problems
- Food allergy in asthma patient

## Critical Actions

| Action | Target |
|---|---|
| Continuous albuterol nebulization or rapid MDI | Within 5 minutes |
| Systemic corticosteroids | Within 30 minutes |
| Reassess after initial treatment | At 15-20 minutes |
| Prepare for intubation if life-threatening features | Immediate |

1. **Inhaled short-acting beta-agonist (SABA):**
   - Albuterol 2.5-5 mg nebulized q15-20min x 3, then continuous nebulization 10-15 mg/hr for severe exacerbation
   - OR albuterol MDI 4-8 puffs q15-20min via spacer (equivalent efficacy to nebulizer in mild-moderate)
2. **Ipratropium bromide** 0.5 mg nebulized q20min x 3 doses (combined with albuterol for severe exacerbation; most benefit in first hour)
3. **Systemic corticosteroids:**
   - Methylprednisolone 125 mg IV (severe/life-threatening)
   - OR prednisone 40-60 mg PO (mild-moderate)
   - OR dexamethasone 0.6 mg/kg IV/PO (max 16 mg) — single dose non-inferior to multi-day prednisone in ED studies
4. **Magnesium sulfate** 2 g IV over 20 minutes for severe exacerbation not responding to initial treatment (reduces admission rates; Cochrane evidence)
5. **Continuous SpO2 monitoring, capnography if available**

## Differential Diagnosis

- COPD exacerbation (age, smoking history, partially reversible obstruction)
- Anaphylaxis (urticaria, angioedema, hypotension, allergen exposure)
- Foreign body aspiration (acute onset, unilateral wheeze, children/elderly)
- Vocal cord dysfunction (inspiratory stridor, flattened inspiratory loop on spirometry)
- Pulmonary embolism (pleuritic pain, risk factors, unilateral leg swelling)
- Heart failure (crackles, JVD, BNP elevation, cardiomegaly; "cardiac asthma")
- Pneumothorax (unilateral absent breath sounds, pleuritic pain)
- Pneumonia (fever, productive cough, consolidation)
- Endobronchial lesion/tumor
- Eosinophilic granulomatosis with polyangiitis (Churg-Strauss)

## Workup

- **Peak expiratory flow (PEF):** Before and after treatment; objective measure of severity and response
- **SpO2:** Continuous monitoring; supplemental O2 to maintain >= 93% (>= 95% in pregnancy)
- **ABG/VBG:** Only for severe/life-threatening exacerbation; PaCO2 >= 40 mmHg in acute asthma indicates impending respiratory failure
- **Chest X-ray:** NOT routine for uncomplicated exacerbation; obtain if: suspected pneumothorax, pneumonia, first episode of wheezing, subcutaneous emphysema, failure to respond to treatment
- **CBC:** Not routine; eosinophilia may indicate allergic trigger
- **BMP:** If prolonged continuous albuterol (hypokalemia from beta-agonist–driven intracellular potassium shift)
- **ECG:** If concern for cardiac cause of dyspnea or in patients on high-dose beta-agonists (tachyarrhythmia)
- **Lactate:** Elevated lactate in severe asthma is often from beta-agonist use (epinephrine-driven aerobic glycolysis), not tissue hypoperfusion — interpret in clinical context
- **Pregnancy test** in women of reproductive age (management differs)

## Treatment

### Mild-Moderate Exacerbation (Speaks in Sentences, SpO2 > 92%, PEF > 50%)
- Albuterol 2.5-5 mg nebulized q20min x 3 OR albuterol MDI 4-8 puffs q20min via spacer
- Prednisone 40-60 mg PO OR dexamethasone 12-16 mg PO (single dose)
- Reassess at 1 hour; if PEF > 70% predicted and symptoms resolved, discharge pathway

### Severe Exacerbation (Speaks in Words, SpO2 90-92%, PEF 25-50%)
- Continuous albuterol nebulization 10-15 mg/hr
- Ipratropium 0.5 mg nebulized q20min x 3 (combined with albuterol)
- Methylprednisolone 125 mg IV
- Magnesium sulfate 2 g IV over 20 minutes
- Supplemental O2 via nasal cannula or non-rebreather to maintain SpO2 >= 93%

### Life-Threatening/Near-Fatal Asthma
- All severe measures above PLUS:
- **Epinephrine** 0.3-0.5 mg IM (1:1000) if bronchospasm refractory to inhaled beta-agonists; can repeat q5-15min
- **Epinephrine IV** 5-20 mcg bolus (push-dose epi) for imminent arrest; infusion 0.1-0.5 mcg/kg/min for refractory bronchospasm
- **Ketamine** 0.5-1 mg/kg IV for bronchodilation and dissociative sedation if intubation anticipated
- **Terbutaline** 0.25 mg SC q20min x 3 doses (alternative to epinephrine)
- **Heliox** (70:30 or 80:20 helium:oxygen) — reduces work of breathing; limited by FiO2 requirement (cannot use if needing > 30-40% FiO2)
- **BiPAP** 10-12/5 cmH2O — may avert intubation; use with caution (risk of pneumothorax in hyperinflated lungs)

### Intubation (Last Resort — High Risk in Severe Asthma)
- **Indications:** Respiratory arrest, declining consciousness, refractory hypoxemia despite maximal treatment
- **Induction:** Ketamine 1-2 mg/kg IV (bronchodilatory) + rocuronium 1.2 mg/kg IV
- **Ventilator strategy:** Permissive hypercapnia to avoid breath stacking and pneumothorax
  - Low respiratory rate (8-12 breaths/min)
  - Low tidal volume (6-8 mL/kg)
  - Prolonged expiratory time (I:E ratio 1:4 or greater)
  - Target plateau pressure < 30 cmH2O
  - Tolerate PaCO2 up to 80 mmHg with pH > 7.15
- Continue inhaled albuterol via ventilator circuit and IV bronchodilators

### Discharge Medications
- Prednisone 40-60 mg PO daily x 5 days (or dexamethasone if single-dose used in ED)
- Albuterol MDI with spacer q4-6h PRN
- Initiate or step up inhaled corticosteroid (budesonide/formoterol 200/6 mcg, 2 puffs BID)
- Asthma action plan
- Follow-up within 1-2 weeks

## Disposition

- **Intubated/ICU:** Life-threatening features, intubated, hemodynamically unstable, requiring continuous IV epinephrine
- **Admission:** Persistent symptoms after 3 hours of aggressive treatment, PEF < 40% after treatment, history of near-fatal asthma, unable to maintain SpO2 > 92% on room air, requiring continuous nebulization
- **Observation (4-6 hours):** Moderate symptoms responding to treatment; reassess PEF and clinical status
- **Discharge:** PEF >= 70% predicted, symptom resolution, ambulating comfortably, SpO2 >= 94% on room air, reliable access to medications and follow-up
- **Primary care/pulmonology follow-up** within 1-2 weeks for all ED visits for asthma

## Pitfalls

1. **Silent chest interpreted as "improving."** Absence of wheezing in a tachypneic, distressed patient indicates critical air trapping with near-zero airflow. This is life-threatening, not reassuring. Prepare for intubation.

2. **Normal or rising PaCO2 dismissed as unremarkable.** Acute asthma should produce hyperventilation and LOW PaCO2. A PaCO2 of 40 mmHg in an acutely distressed asthmatic indicates respiratory muscle fatigue and impending failure.

3. **Delaying systemic corticosteroids.** Corticosteroids take 4-6 hours to reach peak effect. Administer within 30 minutes of presentation. Every hour of delay extends the duration of the exacerbation and increases admission rates.

4. **Not using ipratropium in severe exacerbation.** Adding ipratropium to albuterol in the first hour of severe exacerbation reduces hospitalization. Benefit is greatest in severe disease and diminishes after the first hour.

5. **Breath stacking after intubation.** Mechanically ventilating asthmatic patients with high rates and inadequate expiratory time causes progressive hyperinflation (auto-PEEP), hypotension, and tension pneumothorax. Use low rate, low tidal volume, and long expiratory time. Disconnect from ventilator if sudden hemodynamic collapse (release trapped air).

6. **Attributing elevated lactate solely to sepsis or hypoperfusion.** Beta-agonist therapy (albuterol, epinephrine) drives aerobic glycolysis and produces lactate elevations up to 5-8 mmol/L. This is a pharmacologic effect, not a marker of inadequate resuscitation.

7. **Failure to assess for pneumothorax.** Patients on aggressive positive pressure or with severe air trapping are at risk for pneumothorax. Sudden deterioration, unilateral absent breath sounds, or hemodynamic instability warrants immediate point-of-care ultrasound or needle decompression if tension physiology is present.

8. **Discharging without corticosteroids or inhaled controller medication.** Discharge after an ED visit for asthma without a 5-day steroid course and controller inhaler initiation/escalation leads to early relapse. Every patient discharged after an exacerbation needs oral steroids and an ICS prescription.

9. **Using sedatives (benzodiazepines, opioids) in severe asthma.** Anxiolytics and opioids suppress respiratory drive and worsen hypercapnia. Agitation in severe asthma is driven by hypoxia and hypercarbia — treat the underlying respiratory failure, not the anxiety.
