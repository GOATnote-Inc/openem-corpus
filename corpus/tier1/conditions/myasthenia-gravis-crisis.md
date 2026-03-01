---
id: myasthenia-gravis-crisis
condition: Myasthenic Crisis
aliases: [myasthenia gravis crisis, MG crisis, myasthenic exacerbation, cholinergic crisis]
icd10: [G70.01]
esi: 1
time_to_harm:
  irreversible_injury: "< 1 hour"
  death: "< 4 hours"
  optimal_intervention_window: "< 30 minutes"
category: neurological
track: tier1
sources:
  - type: guideline
    ref: "Myasthenia Gravis Foundation of America: Emergency Management of Myasthenia Gravis, 2024"
  - type: guideline
    ref: "Sanders DB et al. International consensus guidance for management of myasthenia gravis. Neurology. 2016;87(4):419-425"
  - type: guideline
    ref: "Guideline for the management of myasthenic syndromes. J Neurol Neurosurg Psychiatry. 2024;95:1-11"
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
# Myasthenic Crisis

## Recognition

**Classic presentation:**
- Progressive respiratory muscle weakness with dyspnea, orthopnea, tachypnea
- Bulbar weakness: dysarthria, dysphagia, inability to handle secretions
- Worsening generalized weakness, often preceded by infection or medication change
- Paradoxical abdominal breathing (diaphragmatic fatigue)

**Key diagnostics:**
- Negative inspiratory force (NIF) < -20 cmH2O (crisis threshold)
- Forced vital capacity (FVC) < 1 L or < 20 mL/kg (intubation threshold)
- Serial bedside FVC measurements (the 20/30/40 rule): intubate if FVC < 20 mL/kg, NIF < -30 cmH2O, or peak expiratory flow < 40 L/min
- ABG: hypercapnia is a late and ominous sign — do not wait for it

**Distinguish myasthenic from cholinergic crisis:**
- Myasthenic crisis: underdosing or disease flare; pupils normal or dilated
- Cholinergic crisis: excessive acetylcholinesterase inhibitors; miosis, bradycardia, bronchorrhea, diarrhea (SLUDGE signs)
- Edrophonium test historically used but unreliable and rarely performed in ED

**Common triggers:**
- Infection (most common, ~40%), especially pneumonia and UTI
- Medications: aminoglycosides, fluoroquinolones, beta-blockers, magnesium, phenytoin, neuromuscular blocking agents
- Surgery, emotional stress, pregnancy, thyroid dysfunction

## Critical Actions

1. **Assess airway immediately** — intubate early for FVC < 20 mL/kg, NIF < -20 cmH2O, or inability to protect airway; avoid succinylcholine (unpredictable response); use rocuronium at reduced dose (0.3-0.6 mg/kg)
2. **Hold acetylcholinesterase inhibitors** (pyridostigmine) during crisis — they increase secretions and complicate airway management
3. **Start IVIG 0.4 g/kg/day IV for 5 days** (total 2 g/kg) OR **plasmapheresis (PLEX) 5 exchanges over 7-14 days** — both equally effective; PLEX faster onset (days vs 1-2 weeks for IVIG)
4. **Identify and treat trigger** — blood cultures, UA, CXR; start empiric antibiotics if infection suspected (avoid aminoglycosides and fluoroquinolones)
5. **Do NOT initiate high-dose corticosteroids in the ED** — can worsen weakness in first 1-2 weeks; defer to inpatient neurology
6. **Continuous pulse oximetry and serial FVC q2-4h** even if patient appears stable

## Differential Diagnosis

- Cholinergic crisis (SLUDGE signs, excessive cholinesterase inhibitor dosing)
- Guillain-Barre syndrome (ascending weakness, areflexia, albuminocytologic dissociation on LP)
- Lambert-Eaton syndrome (proximal weakness improves with use, associated with SCLC)
- Botulism (descending paralysis, dilated pupils, bulbar onset)
- Acute stroke (focal deficits, asymmetric)
- Organophosphate poisoning (SLUDGE, miosis, exposure history)
- ALS (progressive, no fluctuation, upper and lower motor neuron signs)

## Workup

- **Serial FVC and NIF** at bedside — most critical monitoring tool
- **ABG:** assess ventilation; hypercapnia is late
- **CBC, BMP, magnesium, phosphate, TSH**
- **Anti-AChR antibodies** (positive in ~85% of generalized MG; result not available acutely)
- **Anti-MuSK antibodies** if AChR-negative
- **CT chest** for thymoma evaluation (non-urgent, can defer)
- **CXR, UA, blood cultures** to identify precipitating infection
- **ECG** — rule out cardiac involvement, baseline before treatment
- **Medication reconciliation** — identify offending agents

## Treatment

### Airway Management
- Early intubation preferred over emergent intubation
- Avoid succinylcholine: MG patients are resistant (need higher doses) and response unpredictable
- Rocuronium 0.3-0.6 mg/kg IV (reduced dose; MG patients are exquisitely sensitive to non-depolarizing agents)
- Sugammadex 16 mg/kg IV for reversal if needed
- Non-invasive ventilation (BiPAP) as bridge only if patient alert, cooperative, and managing secretions

### Immunotherapy
- **IVIG** 0.4 g/kg/day IV for 5 days (total 2 g/kg); premedicate with acetaminophen 650 mg PO and diphenhydramine 25-50 mg IV
- **PLEX** 5 exchanges (1-1.5 plasma volumes per exchange) over 7-14 days; requires central venous access
- PLEX contraindicated in sepsis; IVIG contraindicated in IgA deficiency and renal failure

### Supportive Care
- DVT prophylaxis: enoxaparin 40 mg SQ daily
- Stress ulcer prophylaxis if intubated
- Aspiration precautions: HOB elevated 30-45 degrees, NPO if bulbar dysfunction

## Disposition

- **All myasthenic crisis patients:** ICU admission with continuous monitoring
- **Impending crisis** (declining FVC 20-30 mL/kg): ICU or step-down with serial FVC q2-4h
- **Stable MG exacerbation** without respiratory compromise: neurology admission
- **Never discharge** a patient with declining respiratory parameters regardless of subjective improvement

## Pitfalls

1. **Relying on pulse oximetry instead of serial FVC.** Oxygen saturation remains normal until respiratory failure is imminent. FVC decline precedes desaturation by hours.

2. **Administering contraindicated medications.** Aminoglycosides, fluoroquinolones, magnesium sulfate, beta-blockers, and calcium channel blockers can precipitate or worsen crisis. Check every medication against the MG drug safety list.

3. **Starting high-dose corticosteroids in the ED.** Methylprednisolone or prednisone at high doses can cause transient worsening of weakness in 30-50% of patients within 1-2 weeks. Initiate only in monitored setting with IVIG/PLEX onboard.

4. **Using succinylcholine for RSI.** MG patients have reduced AChRs and are resistant to succinylcholine; paradoxically, higher doses risk Phase II block. Use rocuronium at reduced dosing.

5. **Failing to distinguish myasthenic from cholinergic crisis.** Cholinergic crisis (from pyridostigmine overdose) presents with similar weakness PLUS muscarinic signs (SLUDGE). Treatment is atropine and holding cholinesterase inhibitors — opposite of myasthenic crisis immunotherapy.
