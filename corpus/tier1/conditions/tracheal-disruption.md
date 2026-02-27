---
id: tracheal-disruption
condition: Tracheobronchial Disruption
aliases: [tracheobronchial injury, bronchial rupture, tracheal tear, airway disruption, TBI]
icd10: [S27.50XA, S27.51XA, S27.59XA, S12.8XXA]
esi: 1
time_to_harm:
  irreversible_injury: "< 30 minutes (tension pneumothorax, complete airway loss)"
  death: "< 1 hour without airway control and decompression"
  optimal_intervention_window: "Immediate — secure airway distal to injury, decompress tension pneumothorax"
mortality_if_delayed: "Overall mortality 30%; prehospital mortality 30-80% depending on mechanism; delayed diagnosis increases mortality 2-3 fold"
category: respiratory
track: tier1
sources:
  - type: pubmed
    ref: "Kiser AC et al. Blunt tracheobronchial injuries: treatment and outcomes. Ann Thorac Surg. 2001;71(6):2059-2065."
    pmid: "11426793"
  - type: review
    ref: "Symbas PN, Justicz AG, Ricketts RR. Rupture of the airways from blunt trauma: treatment of complex injuries. Ann Thorac Surg. 1992;54(1):177-183."
    pmid: "1610233"
  - type: pubmed
    ref: "Rossbach MM et al. Management of major tracheobronchial injuries: a 28-year experience. Ann Thorac Surg. 1998;65(1):182-186."
    pmid: "9456114"
  - type: guideline
    ref: "EAST Practice Management Guidelines: Penetrating neck trauma. Eastern Association for the Surgery of Trauma."
  - type: review
    ref: "Welter S. Repair of tracheobronchial injuries. Thorac Surg Clin. 2014;24(1):41-50."
    pmid: "24295659"
last_updated: "2026-02-26"
compiled_by: agent
reviewed_by: "Brandon Dent, MD — Board Certified Emergency Medicine"
review_date: "2026-02-27"
risk_tier: A
confusion_pairs:
  - condition: tension-pneumothorax
    differentiators:
      - "Simple tension pneumothorax resolves with chest tube; persistent air leak suggests tracheobronchial injury"
      - "Tracheobronchial disruption: massive persistent air leak despite large-bore chest tube"
      - "Tracheobronchial disruption: fallen lung sign on CXR (lung falls laterally rather than collapsing medially)"
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
# Tracheobronchial Disruption

## Recognition

**Definition:** Tracheobronchial disruption (TBD) is a partial or complete tear of the trachea or mainstem/lobar bronchi from blunt or penetrating trauma. Most blunt injuries occur within 2.5 cm of the carina (80%). The injury is rare (< 1% of blunt chest trauma) but lethal — 30-80% die before reaching the hospital.

**Mechanism:**
- Blunt: deceleration injury (MVC, fall), direct crush (steering wheel), blast wave
- Penetrating: GSW, stab wound to neck or chest
- Iatrogenic: endotracheal intubation (posterior membranous tracheal tear), tracheostomy, rigid bronchoscopy

**Injury Patterns:**

| Location | Frequency | Mechanism |
|----------|-----------|-----------|
| **Within 2.5 cm of carina** | 80% of blunt injuries | Shear forces at fixed point |
| **Right mainstem bronchus** | Most common bronchial injury | Shorter, wider, less protected |
| **Cervical trachea** | Penetrating > blunt | Direct injury, zone II/III neck |
| **Posterior membranous wall** | Iatrogenic tears | ETT overinflation, traumatic intubation |

**Clinical Features:**

| Feature | Notes |
|---------|-------|
| **Massive subcutaneous emphysema** | Rapidly progressive, may extend from neck to abdomen; crepitus on palpation |
| **Pneumothorax with persistent air leak** | Chest tube does not resolve pneumothorax; continuous bubbling in water seal; lung fails to re-expand |
| **Hemoptysis** | Blood in airway from mucosal disruption |
| **Respiratory distress** | Hypoxia, stridor, dyspnea |
| **Pneumomediastinum** | Air tracking along fascial planes; visible on CXR and CT |
| **"Fallen lung sign"** | Lung collapses laterally and inferiorly (away from hilum) rather than medially — pathognomonic on CXR |
| **Sternal fracture** | Associated finding with severe deceleration mechanism |

**Classic Triad (suggestive of TBD):**
1. Pneumothorax that fails to resolve with chest tube
2. Massive subcutaneous emphysema out of proportion to apparent injury
3. Persistent large air leak through chest tube drainage system

## Critical Actions

1. **Secure the airway.** If the patient is breathing spontaneously and maintaining oxygenation, do not rush intubation — an uncontrolled attempt may convert a partial tear to a complete disruption. If intubation is required: fiberoptic-guided intubation is preferred to advance the ETT past the injury under direct visualization. For complete tracheal transection, pass the ETT through the wound into the distal trachea if necessary.

2. **Decompress tension pneumothorax.** Needle decompression followed by large-bore chest tube (28-36 Fr). Place chest tube to suction. If air leak is massive and lung does not re-expand: suspect tracheobronchial injury. Place a SECOND chest tube if air leak volume exceeds drainage capacity of first tube.

3. **Avoid positive pressure ventilation if possible.** PPV forces air through the disruption, worsening pneumomediastinum, subcutaneous emphysema, and tension pneumothorax. If mechanical ventilation is unavoidable: low tidal volumes (4-6 mL/kg), low peak inspiratory pressures, and high respiratory rate. Selective mainstem intubation of the uninjured bronchus may be necessary.

4. **Emergent bronchoscopy for diagnosis and injury characterization.** Flexible bronchoscopy in the ED identifies the location and extent of the disruption. Rigid bronchoscopy in the OR for operative planning. Bronchoscopy is the gold standard diagnostic test for TBD.

5. **Thoracic surgery consultation immediately.** Complete transection, injuries > 1/3 circumference, and injuries with persistent air leak require operative repair (primary anastomosis). Small partial tears (< 1/3 circumference) may be managed conservatively with close observation.

6. **CT chest with IV contrast.** Identifies pneumomediastinum, tracheal/bronchial wall defect, associated injuries (vascular, esophageal). CT has 85-100% sensitivity for TBD when combined with clinical suspicion.

7. **Evaluate for associated injuries.** Esophageal injury (present in 20-30% of penetrating TBD), great vessel injury, spinal injury, pulmonary contusion. These injuries frequently co-exist and affect operative planning.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Simple pneumothorax** | Resolves with chest tube; no persistent air leak; lung re-expands fully |
| **Tension pneumothorax** | Initial decompression and chest tube resolve the tension; no ongoing massive air leak |
| **Esophageal perforation** | Pneumomediastinum present but no air leak through chest tube; contrast esophagram positive; chest tube drainage may be purulent/salivary |
| **Pulmonary laceration** | Parenchymal air leak; usually self-limited; CT shows intraparenchymal injury, not central airway disruption |
| **Diaphragmatic rupture** | Abdominal viscera in chest on CXR; no subcutaneous emphysema; no air leak |
| **Laryngeal fracture** | Dysphonia, stridor, anterior neck tenderness; CT shows laryngeal cartilage fracture; injury is supraglottic, not tracheobronchial |

## Workup

**Imaging:**
- CXR: pneumomediastinum, pneumothorax (especially persistent after chest tube), subcutaneous emphysema, fallen lung sign, tracheal air column disruption
- CT chest with IV contrast: tracheal/bronchial wall defect, extraluminal air adjacent to airway, mediastinal air, Macklin effect (linear air along bronchovascular bundles)
- CT angiography of chest: exclude concurrent aortic injury (common with same mechanism)

**Bronchoscopy (gold standard):**
- Flexible bronchoscopy: identifies location, length, and depth of tear; mucosal disruption, exposed cartilage rings, false passage
- Rigid bronchoscopy: better visualization for operative planning; allows ventilation during procedure

**Laboratory:**
- CBC, type and crossmatch (prepare for OR)
- ABG (assess oxygenation, ventilation)
- Coagulation studies

**Associated Injury Workup:**
- CT neck with IV contrast (cervical tracheal injury, vascular injury)
- Esophagography or esophagoscopy (concurrent esophageal injury)
- CTA great vessels

## Treatment

**Non-Operative Management (selected cases):**
- Tear < 1/3 airway circumference, no mediastinitis, no respiratory compromise
- Humidified oxygen, cough suppression (codeine 30 mg PO q4-6h), head of bed elevated
- Serial bronchoscopy at 1-2 weeks to assess healing
- Antibiotics only if concurrent contamination or pneumonia

**Operative Repair:**
- Indications: complete transection, tear > 1/3 circumference, persistent air leak despite chest tubes, inability to ventilate, progressive mediastinal emphysema
- Technique: primary repair with interrupted absorbable sutures (4-0 PDS); buttress with intercostal muscle flap, pericardial flap, or omental flap
- Approach: right posterolateral thoracotomy for right mainstem and distal tracheal injuries; left posterolateral thoracotomy for left mainstem; cervical collar incision for cervical tracheal injuries

**Airway Management Strategies:**
- Spontaneous ventilation preferred during bronchoscopy and surgical approach
- Fiberoptic intubation past the injury
- Selective mainstem intubation of uninjured side
- Jet ventilation through rigid bronchoscope
- Cardiopulmonary bypass or ECMO for complete bilateral disruption or carinal injury (rare)

**Cervical Tracheal Injury (penetrating):**
- Direct wound exploration in OR
- Primary repair with interrupted absorbable sutures
- Strap muscle flap interposition between tracheal and esophageal repair lines if concurrent esophageal injury

## Disposition

**All confirmed tracheobronchial injuries require admission** to a trauma center with thoracic surgery and bronchoscopy capability.

**Transfer if:**
- No thoracic surgery on site
- Secure airway (fiberoptic intubation if needed), place chest tubes, minimize positive pressure ventilation during transport

**Complications:**
- Tracheal stenosis (10-20% — presents weeks to months later with progressive dyspnea/stridor)
- Bronchopleural fistula
- Mediastinitis (if delayed diagnosis)

## Pitfalls

1. **Diagnosing "simple" pneumothorax and not reassessing after chest tube placement.** The hallmark of tracheobronchial injury is a pneumothorax that does not resolve with a functioning chest tube. A persistent air leak with failure of the lung to re-expand must prompt bronchoscopy. Do not place additional chest tubes hoping to manage the air leak without determining the source.

2. **Aggressive positive pressure ventilation worsening the injury.** High peak inspiratory pressures and large tidal volumes force air through the disruption, worsening subcutaneous emphysema, pneumomediastinum, and potentially converting a partial tear to a complete transection. If mechanical ventilation is unavoidable, use the lowest pressures and tidal volumes that maintain adequate oxygenation.

3. **Attempting conventional direct laryngoscopy intubation in a patient with tracheal disruption.** Blind advancement of an ETT through a disrupted trachea may create a false passage or convert a partial tear to complete transection. Fiberoptic-guided intubation allows visualization of the injury and deliberate passage of the ETT distal to the disruption. If fiberoptic is unavailable and intubation is emergent, advance the ETT carefully with a bougie under video laryngoscopy.

4. **Missing the injury due to delayed presentation.** Up to 50% of tracheobronchial injuries present in a delayed fashion (days to weeks) with atelectasis, recurrent pneumonia, or progressive stenosis. A history of significant blunt chest trauma with unexplained lobar atelectasis or recurrent pneumonia should prompt bronchoscopy.

5. **Failing to evaluate for concurrent esophageal injury in penetrating neck/chest trauma.** Esophageal injury is present in 20-30% of penetrating tracheobronchial injuries. A missed esophageal perforation leads to mediastinitis with mortality > 50%. Esophagoscopy or contrast esophagram must be performed when TBD is diagnosed in penetrating trauma.

6. **Relying on a negative chest X-ray to exclude tracheobronchial injury.** Up to 10% of patients with tracheobronchial disruption have no pneumomediastinum on initial chest radiograph, particularly with small tears where the disrupted mucosa acts as a flap valve or when peribronchial tissue tamponades the air leak. Subcutaneous emphysema may also be absent initially. In a patient with a mechanism consistent with TBD (high-energy deceleration, direct crush, penetrating neck/chest trauma) and clinical findings such as hemoptysis or persistent air leak, a normal CXR does not exclude the diagnosis — CT and bronchoscopy are required.

7. **Advancing an endotracheal tube past the site of disruption, creating a false passage into the mediastinum or pleural space.** Blind ETT advancement through a tracheal tear can exit the airway through the disruption, resulting in loss of ventilation, tension pneumomediastinum, or mediastinal contamination. This converts a survivable injury into an airway catastrophe. If intubation is required, fiberoptic bronchoscopy-guided intubation allows direct visualization of the injury and controlled advancement of the ETT distal to the disruption. If fiberoptic is unavailable, advance the tube over a bougie under video laryngoscopy with extreme caution, stopping immediately if resistance is encountered.
