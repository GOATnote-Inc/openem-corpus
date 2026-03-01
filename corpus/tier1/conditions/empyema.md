---
id: empyema
condition: Empyema Thoracis
aliases: [empyema, thoracic empyema, pleural empyema, pyothorax, purulent pleuritis]
icd10: [J86.0, J86.9]
esi: 2
time_to_harm: "< 24 hours (if septic)"
category: respiratory
track: tier1
sources:
  - type: guideline
    ref: "2017 AATS Expert Consensus Guidelines for the Management of Empyema. J Thorac Cardiovasc Surg. 2017;153(6):e129-e146."
  - type: review
    ref: "Rahman NM, et al. Intrapleural Use of Tissue Plasminogen Activator and DNase in Pleural Infection (MIST2). N Engl J Med. 2011;365(6):518-526."
  - type: guideline
    ref: "2010 BTS Guidelines for the Management of Pleural Infection in Adults. Thorax. 2010;65(Suppl 2):ii41-ii53."
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
# Empyema Thoracis

## Recognition

**Presentation:**
- Fever persisting despite appropriate pneumonia antibiotics
- Pleuritic chest pain, productive cough
- Dyspnea, tachypnea
- Decreased breath sounds, dullness to percussion
- Toxic appearance in advanced cases
- May follow pneumonia (60%), thoracic surgery, esophageal perforation, subdiaphragmatic infection

**Stages:**
1. **Exudative (stage 1):** Thin free-flowing parapneumonic fluid, pH > 7.2, low WBC — antibiotics alone may suffice
2. **Fibrinopurulent (stage 2):** Increasing WBC, fibrin deposits, septations forming, pH < 7.2, glucose < 40 — requires drainage
3. **Organizing (stage 3):** Thick fibrous peel ("rind"), trapped lung — requires surgical decortication

**Microbiology:**
- Community-acquired: S. pneumoniae, Streptococcus milleri group, anaerobes, S. aureus
- Hospital-acquired: MRSA, gram-negatives (Klebsiella, E. coli, Pseudomonas), anaerobes

## Critical Actions

| Action | Target |
|---|---|
| Chest imaging + US | < 1 hour |
| Diagnostic thoracentesis | < 2 hours |
| Tube thoracostomy (if empyema confirmed) | < 4 hours |
| IV antibiotics | < 1 hour |

1. **Diagnostic thoracentesis** (US-guided) — send pH, glucose, LDH, protein, cell count, gram stain, aerobic + anaerobic culture
2. **Tube thoracostomy** if any of: purulent fluid, positive gram stain/culture, pH < 7.2, glucose < 40 mg/dL
3. **IV antibiotics** — empiric broad-spectrum coverage including anaerobes:
   - Community-acquired: ampicillin-sulbactam 3 g IV q6h OR ceftriaxone 2 g IV q24h + metronidazole 500 mg IV q8h
   - Hospital-acquired/MRSA risk: vancomycin 15-20 mg/kg IV q8-12h + piperacillin-tazobactam 4.5 g IV q6h
4. **CT chest with contrast** — assess extent, septations, lung parenchyma, guide drainage
5. **Thoracic surgery consultation** early — may need VATS decortication

## Differential Diagnosis

- **Complicated parapneumonic effusion** — precursor to empyema; pH 7.0-7.2 with negative cultures; still requires drainage
- **Lung abscess** — intraparenchymal cavity vs pleural collection; CT differentiates
- **Malignant effusion** — lymphocyte predominant, positive cytology, no purulence
- **Tuberculosis pleural effusion** — lymphocyte predominant, ADA > 40, AFB stain/culture
- **Hemothorax** — bloody fluid, hematocrit > 50% of serum; post-traumatic or spontaneous
- **Esophageal perforation with mediastinitis** — Boerhaave syndrome; air in mediastinum, high amylase in pleural fluid

## Workup

- **Pleural fluid analysis:**
  - pH < 7.2 = complicated/empyema (use blood gas analyzer, not litmus paper)
  - Glucose < 40 mg/dL
  - LDH > 1000 IU/L
  - WBC > 25,000-50,000/μL (neutrophil predominant)
  - Gram stain and culture (aerobic + anaerobic)
  - Positive gram stain or frank pus = empyema regardless of other values
- **CT chest with contrast:** Extent of collection, septations/loculations, pleural enhancement (split pleura sign = empyema), parenchymal disease, guide drainage
- **US chest:** Real-time guidance for thoracentesis, assess septations/complexity
- **Labs:** CBC (leukocytosis), CRP/ESR, blood cultures x 2, BMP, LFTs, albumin
- **Sputum culture:** If concurrent pneumonia

## Treatment

### Stage 1 (Exudative — Simple Parapneumonic)
- IV antibiotics alone if pH > 7.2, glucose > 40, negative gram stain/culture
- Serial imaging to monitor for progression
- Therapeutic thoracentesis if large and causing symptoms

### Stage 2 (Fibrinopurulent — Complicated/Empyema)
- Tube thoracostomy (12-14 Fr pigtail or 24-28 Fr surgical) + IV antibiotics
- **Intrapleural fibrinolytics (MIST2 protocol) for loculated empyema:**
  - tPA 10 mg + DNase (dornase alfa) 5 mg in 30 mL NS
  - Instill via chest tube, clamp for 1 hour, then drain
  - Repeat q12h x 3 days (6 total doses)
  - MIST2 result: 75% reduction in need for surgery
- Flush chest tube with 20 mL NS q6h to maintain patency
- Daily imaging to assess drainage adequacy

### Stage 3 (Organizing — Trapped Lung)
- VATS (video-assisted thoracoscopic surgery) decortication — gold standard
- Open thoracotomy with decortication for VATS failure or extensive disease
- Prolonged antibiotics (typically 4-6 weeks total)

### Antibiotic Duration
- IV antibiotics until clinical improvement (afebrile, WBC normalizing, drainage decreasing) — typically 7-14 days
- Transition to oral: amoxicillin-clavulanate 875/125 mg PO BID or clindamycin 300 mg PO QID
- Total duration: 3-6 weeks depending on clinical response

## Disposition

- **ICU admission:** Septic shock, respiratory failure, post-operative
- **Inpatient (surgical service):** All empyema patients for drainage, antibiotics, monitoring
- **Thoracic surgery consultation:** All stage 2-3 empyema, failed tube drainage, loculated collections
- **Follow-up imaging:** CXR weekly during treatment, CT at 4-6 weeks to assess resolution
- **Discharge:** Chest tube removed, afebrile >= 48 hours, WBC normalizing, tolerating oral antibiotics

## Pitfalls

1. **Not measuring pleural fluid pH and glucose.** These are the most important indicators of complicated parapneumonic effusion requiring drainage. pH < 7.2 and glucose < 40 mandate tube thoracostomy even if gram stain is negative. Failure to obtain these values leads to delayed drainage and progression to organized empyema.

2. **Using too small a chest tube without fibrinolytics.** Small-bore catheters (10-14 Fr) are adequate if combined with fibrinolytics for loculated empyema. Without fibrinolytics, thick purulent fluid and septations may clog small tubes. If using small tubes, add MIST2 protocol.

3. **Stopping antibiotics at 7-14 days regardless of clinical response.** Empyema requires prolonged antibiotic therapy (3-6 weeks total). Premature discontinuation leads to relapse. Continue until imaging shows resolution and inflammatory markers normalize.

4. **Delaying surgical consultation.** Early thoracic surgery involvement improves outcomes. Stage 2 empyema failing tube drainage + fibrinolytics after 3-5 days should proceed to VATS decortication rather than prolonged medical management. Stage 3 (organized) empyema almost always requires surgery.

5. **Attributing persistent fever during pneumonia to inadequate antibiotic coverage without imaging the pleural space.** The most common cause of pneumonia treatment failure is development of parapneumonic effusion or empyema. CT or US of the chest should be obtained for any patient with pneumonia not improving at 48-72 hours.
