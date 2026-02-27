---
id: massive-hemoptysis
condition: Massive Hemoptysis
aliases: [massive pulmonary hemorrhage, exsanguinating hemoptysis, life-threatening hemoptysis]
icd10: [R04.9, R04.89]
esi: 1
time_to_harm:
  irreversible_injury: "< 30 minutes (asphyxiation from airway flooding precedes hemorrhagic shock)"
  death: "< 1 hour — death is from asphyxiation, not exsanguination (anatomic dead space is only 150 mL)"
  optimal_intervention_window: "Immediate airway protection and bleeding-side isolation"
mortality_if_delayed: "Mortality 50-80% without intervention; death is from asphyxiation, not exsanguination"
category: respiratory
track: tier1
sources:
  - type: review
    ref: "Sakr L, Dutau H. Massive hemoptysis: an update on the role of bronchoscopy in diagnosis and management. Respiration. 2010;80(1):38-58."
    pmid: "20090288"
  - type: pubmed
    ref: "Yoon W et al. CT angiography of the bronchial arteries and management of massive hemoptysis by bronchial arterial embolization. Korean J Radiol. 2002;3(1):45-55."
    pmid: "11919480"
  - type: review
    ref: "Jean-Baptiste E. Clinical assessment and management of massive hemoptysis. Crit Care Med. 2000;28(5):1642-1647."
    pmid: "10834728"
  - type: pubmed
    ref: "Fartoukh M et al. An integrated approach to diagnosis and management of severe haemoptysis in patients admitted to the intensive care unit: a case series from a referral centre. Respir Res. 2007;8(1):11."
    pmid: "17302979"
  - type: guideline
    ref: "Davidson K, Shojaee S. Managing massive hemoptysis. Chest. 2020;157(1):77-88."
    pmid: "31374211"
last_updated: "2026-02-26"
compiled_by: agent
reviewed_by: "Brandon Dent, MD — Board Certified Emergency Medicine"
review_date: "2026-02-27"
risk_tier: A
confusion_pairs:
  - condition: pulmonary-embolism
    differentiators:
      - "PE: hemoptysis is typically small-volume, blood-streaked sputum"
      - "Massive hemoptysis: frank blood > 100 mL/hr or airway compromise"
      - "PE: pleuritic chest pain and dyspnea dominate over hemoptysis"
validation:
  schema_version: "2.0"
  automated_consistency_check: "2026-02-27"
  dose_range_validator: "2026-02-27"
  unit_normalization_check: "2026-02-27"
  cross_file_consistency_check: "2026-02-27"
  citation_presence_check: "2026-02-27"
  duplicate_content_check: "2026-02-27"
  outlier_detection_flag: clear
  provenance_links: []
---
# Massive Hemoptysis

## Recognition

**Definition:** Massive hemoptysis is expectoration of blood exceeding 100 mL/hour or > 600 mL/24 hours, or any volume causing hemodynamic instability or gas exchange impairment. The critical threat is asphyxiation from airway flooding — the tracheobronchial dead space is only 150 mL, making even modest hemorrhage lethal if it fills the airway before it can be cleared.

**Common Causes:**

| Category | Examples |
|----------|----------|
| **Infectious** | Tuberculosis (leading cause worldwide), lung abscess, aspergilloma (mycetoma), necrotizing pneumonia |
| **Malignancy** | Bronchogenic carcinoma, endobronchial metastases, carcinoid |
| **Vascular** | Pulmonary arteriovenous malformation, bronchial artery aneurysm, aortobronchial fistula |
| **Autoimmune** | Granulomatosis with polyangiitis (Wegener), Goodpasture syndrome, Behçet disease |
| **Iatrogenic** | Pulmonary artery catheter perforation, post-bronchoscopy biopsy, anticoagulation |
| **Cardiac** | Mitral stenosis (bronchial venous congestion), left heart failure |
| **Coagulopathy** | Anticoagulation, DIC, thrombocytopenia |
| **Traumatic** | Pulmonary contusion, tracheobronchial disruption |

**Clinical Assessment:**
- Confirm hemoptysis (not hematemesis or epistaxis with aspiration)
- Estimate volume: patient descriptions are unreliable — observed volume in a basin or suction canister
- Identify bleeding side if possible: patient often knows which side is "gurgling"

| Feature | Notes |
|---------|-------|
| **Frank blood expectoration** | Bright red, frothy, alkaline pH (vs hematemesis: coffee-ground, acidic) |
| **Respiratory distress** | Hypoxia from blood flooding alveoli; may progress to complete airway obstruction |
| **Lateralizing symptoms** | Patient leans to one side, describes gurgling from one lung |
| **Hemodynamic instability** | Late finding — asphyxiation kills before hemorrhagic shock in most cases |

## Critical Actions

1. **Protect the non-bleeding lung.** Position the patient with the bleeding side DOWN (lateral decubitus). This uses gravity to prevent blood from flooding the contralateral lung. If the bleeding side is unknown, place patient in the position that provides the best oxygenation.

2. **Endotracheal intubation with the largest ETT possible (8.0+ mm).** Large bore ETT allows passage of bronchoscope for localization and intervention. 100% FiO2. If the bleeding side is identified, selective right or left mainstem intubation with a standard ETT to isolate the non-bleeding lung (advance ETT into the non-bleeding mainstem bronchus).

3. **Emergent bronchoscopy for localization and intervention.** Rigid bronchoscopy in OR is preferred for massive hemoptysis (allows suctioning of large clots, passage of instruments, maintained ventilation). Flexible bronchoscopy at bedside if rigid not immediately available — localizes bleeding site, permits endobronchial tamponade.

4. **Endobronchial tamponade.** Fogarty catheter (embolectomy catheter) through bronchoscope into bleeding segmental bronchus, inflate balloon to tamponade. Cold saline lavage (4°C, 50 mL aliquots) through bronchoscope promotes vasoconstriction. Topical epinephrine 1:20,000 (0.5 mL of 1:1000 diluted in 10 mL NS) via bronchoscope.

5. **Tranexamic acid 1 g IV over 10 minutes, may repeat once.** Nebulized TXA 500 mg in 5 mL NS is an adjunct for ongoing hemoptysis. IV TXA is evidence-supported for reducing bleeding volume while definitive therapy is arranged.

6. **Interventional radiology consultation for bronchial artery embolization (BAE).** BAE is the first-line definitive therapy for massive hemoptysis in hemodynamically stable patients. Success rate 70-90% for immediate bleeding control. CT angiography before BAE to map bronchial arterial anatomy.

7. **Correct coagulopathy.** Reverse anticoagulation (vitamin K 10 mg IV, 4-factor PCC 25-50 units/kg for warfarin; idarucizumab for dabigatran; andexanet alfa for factor Xa inhibitors). Platelets for < 50,000. FFP 15 mL/kg for INR > 1.5.

8. **Type and crossmatch, activate massive transfusion protocol if hemodynamically unstable.** Most patients with massive hemoptysis die from asphyxiation, not exsanguination — but blood loss can become significant with prolonged hemorrhage.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Hematemesis with aspiration** | History of GI symptoms (nausea, abdominal pain); coffee-ground or dark blood; acidic pH on litmus test; no frothy sputum |
| **Posterior epistaxis with aspiration** | Blood seen in posterior pharynx; anterior rhinoscopy or posterior endoscopy localizes source; no parenchymal lung lesion |
| **Pulmonary embolism** | Hemoptysis typically small-volume (blood-streaked sputum); pleuritic chest pain, dyspnea dominate; CTA shows filling defect |
| **Acute pulmonary edema** | Pink frothy sputum (not frank blood); bilateral crackles; elevated BNP; responds to diuresis and NIPPV |
| **Diffuse alveolar hemorrhage** | Bilateral infiltrates on CXR; sequential BAL becoming progressively bloodier; autoimmune or vasculitic associations; no focal endobronchial source |

## Workup

**Immediate:**
- CXR (localizes side of hemorrhage in 45-65%; mass, cavity, infiltrate)
- CBC, coagulation studies (PT/INR, aPTT, fibrinogen)
- Type and crossmatch
- BMP, ABG
- Sputum: AFB smear (tuberculosis), culture, cytology

**Definitive Imaging:**
- CT chest with angiography: identifies bleeding source, maps bronchial artery anatomy for embolization, detects mass/cavity/AVM
- CT angiography before bronchial artery embolization (guide IR to target vessels)

**Bronchoscopy:**
- Localizes bleeding to lobe/segment
- Therapeutic intervention (tamponade, cold saline, topical vasoconstrictors)
- Rigid bronchoscopy for active massive hemorrhage (allows ventilation during procedure)

**Additional (based on etiology):**
- AFB cultures, QuantiFERON-TB (tuberculosis)
- ANCA, anti-GBM antibodies (vasculitis, Goodpasture)
- Echocardiography (mitral stenosis, pulmonary hypertension)
- Sputum cytology (malignancy)

## Treatment

**Airway Protection:**
- Large-bore ETT (≥ 8.0 mm ID)
- Selective mainstem intubation to isolate non-bleeding lung if lateralized
- Double-lumen ETT (Carlens or Robertshaw tube) if available and experienced provider present — allows independent lung ventilation
- Bronchial blocker (Arndt or Cohen) through single-lumen ETT as alternative

**Bronchoscopic Interventions:**
- Cold saline lavage: 50 mL aliquots of 4°C NS via bronchoscope
- Topical epinephrine 1:20,000 via bronchoscope
- Fogarty balloon tamponade (insert via working channel, inflate in bleeding segment)
- Oxidized regenerated cellulose (Surgicel) packing
- Endobronchial electrocautery or argon plasma coagulation for visible endobronchial lesions

**Bronchial Artery Embolization (first-line definitive):**
- CT angiography to map bronchial arterial anatomy
- Selective catheterization and embolization with polyvinyl alcohol particles, gelatin sponge, or coils
- Avoid embolizing spinal arteries (artery of Adamkiewicz arises from left bronchial artery in 5%)
- Recurrence rate: 10-30% at 1 year

**Surgical Resection (last resort):**
- Lobectomy or pneumonectomy for localized disease (mass, aspergilloma, AVM) with failed BAE
- Emergency surgery mortality: 25-50% (vs 7-18% for elective resection)
- Indicated when BAE fails or is not feasible and hemorrhage continues

**Pharmacologic Adjuncts:**
- Tranexamic acid 1 g IV q8h (continuing after initial bolus)
- Nebulized TXA 500 mg q8h as adjunct
- Vasopressin 0.2-0.4 units/min IV infusion for refractory hemorrhage (off-label)

## Disposition

**All massive hemoptysis patients require ICU admission** with:
- Continuous monitoring, intubation equipment at bedside
- Interventional radiology and thoracic surgery on standby
- Type and crossmatch maintained for 48 hours after last hemorrhage

**Transfer if:**
- No interventional radiology (BAE capability)
- No thoracic surgery backup
- Stabilize airway (intubate if needed), position bleeding-side down, start TXA, and correct coagulopathy before transport

## Pitfalls

1. **Focusing on hemodynamic resuscitation rather than airway protection.** Death from massive hemoptysis is from asphyxiation, not exsanguination. The tracheobronchial dead space is only 150 mL — a relatively small volume of blood can completely obstruct gas exchange. The first priority is positioning (bleeding-side down), suctioning, and airway isolation. Volume resuscitation is secondary.

2. **Delaying intubation in a patient who is actively coughing up blood.** The patient with massive hemoptysis who is alert and coughing is maintaining their airway through cough clearance. The moment cough effectiveness decreases (fatigue, altered mental status, increasing blood volume), complete airway obstruction occurs rapidly. Intubate early with a large-bore ETT rather than waiting for respiratory arrest.

3. **Using a small ETT that prevents subsequent bronchoscopy.** A 7.0 mm ETT does not accommodate a therapeutic bronchoscope. Use ≥ 8.0 mm ETT to allow bronchoscope passage for localization and intervention. Planning ahead for bronchoscopy at the time of intubation avoids a tube exchange in a critically bleeding patient.

4. **Ordering CTA before stabilizing the airway.** CT requires supine positioning and transport — both of which worsen airway flooding. Stabilize the airway, position the patient, and achieve initial hemostasis before imaging. A CXR at bedside is adequate for initial lateralization.

5. **Missing aspergilloma as the cause in patients with prior TB or COPD.** Aspergilloma (fungal ball in a pre-existing lung cavity) is a leading cause of massive hemoptysis worldwide. CXR shows the classic "air crescent sign" — a mobile intracavitary mass. The definitive treatment is surgical resection or BAE, not antifungals (poor penetration into the avascular cavity).

6. **Placing the patient supine instead of bleeding-side down.** Supine positioning allows blood from the hemorrhaging lung to flow by gravity into the contralateral bronchial tree, flooding the only functional lung and causing bilateral asphyxiation. The patient must be placed in the lateral decubitus position with the bleeding side dependent — this confines blood to the already-affected lung and preserves gas exchange in the contralateral lung. If the bleeding side is unknown, place the patient in whichever lateral position produces the best oxygen saturation.

7. **Failing to isolate the bleeding lung with selective intubation.** When massive hemoptysis continues despite positioning and suctioning, a standard midtracheal ETT does not prevent blood from crossing to the non-bleeding lung. Advancing the ETT into the mainstem bronchus of the non-bleeding lung effectively isolates and protects it — this can be performed rapidly with a standard ETT, confirmed by auscultation and capnography. A double-lumen tube or bronchial blocker provides more controlled isolation but requires an experienced provider. Failure to isolate the bleeding lung is the most common correctable cause of death in massive hemoptysis.
