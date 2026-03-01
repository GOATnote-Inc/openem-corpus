---
id: emergency-thoracotomy-approach
condition: Emergency Thoracotomy Approach
aliases: [ED thoracotomy approach, clamshell thoracotomy, anterolateral thoracotomy, left thoracotomy]
icd10: [S26.01XA, S27.1XXA, Z53.09]
esi: 1
time_to_harm:
  irreversible_injury: "< 5 minutes"
  death: "< 10 minutes without intervention in penetrating thoracic arrest"
  optimal_intervention_window: "< 15 minutes from loss of signs of life"
mortality_if_delayed: "Survival: penetrating cardiac 10-35%, penetrating thoracic 8-15%, blunt < 2%; drops to near zero beyond 15 minutes of arrest"
category: procedural
track: tier1
sources:
  - type: guideline
    ref: "Seamon MJ, Haut ER, Van Arendonk K, et al. An evidence-based approach to patient selection for emergency department thoracotomy: A practice management guideline from EAST. J Trauma Acute Care Surg. 2015;79(1):159-173."
    pmid: "26091330"
  - type: guideline
    ref: "Burlew CC, Moore EE, Moore FA, et al. Western Trauma Association critical decisions in trauma: resuscitative thoracotomy. J Trauma Acute Care Surg. 2012;73(6):1359-1363."
    pmid: "23188227"
  - type: review
    ref: "Wise D, Davies G, Coats T, et al. Emergency thoracotomy: how to do it. Emerg Med J. 2005;22(1):22-24."
    pmid: "15611536"
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition. American College of Surgeons. 2018."
  - type: pubmed
    ref: "Rhee PM, Acosta J, Bridgeman A, et al. Survival after emergency department thoracotomy: review of published data from the past 25 years. J Am Coll Surg. 2000;190(3):288-298."
    pmid: "10703854"
last_updated: "2026-03-01"
compiled_by: agent
risk_tier: A
confusion_pairs:
  - condition: resuscitative-thoracotomy
    differentiators:
      - "Resuscitative thoracotomy: the full procedure including pericardiotomy, cardiac repair, aortic cross-clamping, and internal massage"
      - "Emergency thoracotomy approach: focuses on the incision technique and access — the entry pathway used for resuscitative thoracotomy, lung hilum clamping, or operative exposure"
      - "This entry covers the surgical approach and incision options; resuscitative-thoracotomy covers the therapeutic interventions performed once access is obtained"
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
# Emergency Thoracotomy Approach

## Recognition

**Indications (EAST 2015 — patient selection is the critical decision):**

| Mechanism | Signs of Life | Recommendation |
|-----------|---------------|----------------|
| Penetrating cardiac | Lost within 15 min of ED | Strongly recommended |
| Penetrating thoracic (non-cardiac) | Lost within 15 min | Conditionally recommended |
| Penetrating extrathoracic | Lost within 15 min | Conditionally recommended |
| Blunt injury | Lost within 10 min | Conditionally recommended |
| Blunt without any signs of life at scene | None | Not recommended |

**Signs of Life:**
- Pupillary reactivity
- Spontaneous movement or respiratory effort
- Organized cardiac electrical activity
- Measurable blood pressure

**Approach Selection:**
- **Left anterolateral thoracotomy** — default for ED thoracotomy; accesses heart, left lung, descending aorta
- **Clamshell (bilateral anterolateral + transverse sternotomy)** — when bilateral access needed or right-sided injury
- **Right anterolateral thoracotomy** — right lung hilum, right atrium (rarely used alone in ED)

**Pre-Requisites:**
- Bilateral finger thoracostomy already performed (rule out tension pneumothorax)
- ETT in place with confirmed placement
- MTP activated; O-negative blood running
- Trauma surgery notified

## Critical Actions

| Action | Target |
|--------|--------|
| Decision to open chest | < 2 minutes from arrest |
| Skin to pleural space | < 60 seconds |
| Pericardiotomy complete | < 3 minutes from incision |
| Trauma surgery in OR | Within 30 minutes |

1. **Left anterolateral thoracotomy** — primary approach
2. **Pericardiotomy** — decompress tamponade
3. **Cardiac hemorrhage control** — digital pressure, staples, Foley catheter
4. **Aortic cross-clamp** — redirect blood to brain and heart
5. **Internal cardiac massage** — 80-100/min bimanual
6. **Internal defibrillation** — 30 J for VF
7. **Clamshell extension** — if access insufficient or right-sided injury identified

## Differential Diagnosis

**Before Committing to Thoracotomy:**

| Alternative | When to Pursue |
|-------------|---------------|
| Bilateral finger thoracostomy | FIRST — rule out tension pneumothorax as reversible cause |
| FAST exam | < 60 seconds — identifies tamponade (pericardial fluid) or abdominal hemorrhage |
| Tube thoracostomy alone | If massive hemothorax but patient has pulse — drain first; thoracotomy only if criteria met |
| REBOA | Subdiaphragmatic hemorrhage with thoracic access; can augment coronary and cerebral perfusion as bridge to OR |

## Workup

**Pre-Procedure (Simultaneous with Decision):**
- Bilateral finger thoracostomy → chest tubes
- ETT confirmed with ETCO2
- FAST exam (< 60 seconds) — pericardial effusion, free abdominal fluid
- MTP running: O-negative blood via rapid infuser through large-bore IVs (2x 14-16g PIV or cordis)
- Consent: not required in life-threatening emergency

**Thoracotomy Instrument Tray:**

| Instrument | Purpose |
|-----------|---------|
| No. 10 scalpel | Skin incision |
| Finochietto rib spreader (large) | Open chest; handle toward axilla |
| Metzenbaum scissors (long) | Pericardiotomy |
| DeBakey aortic cross-clamp | Descending aorta cross-clamping |
| Satinsky vascular clamp | Pulmonary hilum clamping |
| Toothed forceps | Tissue handling |
| 2 needle drivers | Suturing |
| 3-0 Prolene on SH needle | Cardiac repair |
| 0-silk ties | Vessel ligation |
| Gigli saw | Sternotomy for clamshell extension |
| Heavy scissors (Mayo) | Cut through cartilage for clamshell |
| Internal defibrillator paddles | 30 J for VF |
| Foley catheter | Balloon tamponade of cardiac wounds |
| Skin stapler | Rapid temporary cardiac wound closure |
| Laparotomy pads | Hemostasis and packing |

## Treatment

### Left Anterolateral Thoracotomy (Standard Approach)

**Step 1: Incision**
- Patient supine, left arm abducted 90 degrees
- Incision from left sternal border to posterior axillary line along the 5th intercostal space (nipple level in males, inframammary fold in females)
- Single stroke through skin, subcutaneous tissue, and muscle

**Step 2: Enter Pleural Space**
- Enter above the 6th rib to avoid the neurovascular bundle
- Use heavy scissors or finger dissection through the intercostals
- Rush of air/blood confirms pleural entry

**Step 3: Rib Spreading**
- Insert Finochietto rib spreader with handle directed toward the axilla (avoids interference with cardiac access)
- Open progressively — rib fracture is acceptable and expected

**Step 4: Pericardiotomy**
- Identify the pericardium — anterior to the descending aorta, gray-white structure
- Grasp with forceps, tent upward
- Open with Metzenbaum scissors ANTERIOR and PARALLEL to the phrenic nerve
- Incise longitudinally — evacuate clot and blood manually
- Clot removal alone may restore cardiac filling

**Step 5: Cardiac Assessment and Repair**
- Identify wound location
- Digital pressure for hemorrhage control
- Skin stapler across small lacerations (rapid temporization)
- Horizontal mattress sutures with 3-0 Prolene for larger wounds (avoid coronary arteries — suture PARALLEL to LAD/circumflex)
- Foley catheter through wound, inflate balloon 15-30 mL, gentle traction (tamponades while awaiting OR)

**Step 6: Aortic Cross-Clamp**
- Retract left lung anteriorly and superiorly
- Identify descending aorta against the vertebral bodies (tubular, pulsatile or non-pulsatile)
- Blunt dissection of periaortic tissue
- Apply DeBakey clamp — redirects all cardiac output to brain and coronary circulation
- Maximum clamp time: 30 minutes; communicate to surgery

**Step 7: Internal Cardiac Massage**
- Bimanual: flat palm behind heart, compress against sternum, base to apex
- Rate: 80-100/min
- Generates 2-3x cardiac output of external CPR

**Step 8: Internal Defibrillation (if VF)**
- 30 J with internal paddles — NOT transthoracic energy levels
- Saline-soaked laparotomy pads between paddles and myocardium

### Clamshell Extension (Bilateral Access)

**When:** right-sided injury, bilateral pulmonary injury, or left thoracotomy provides insufficient exposure
**Technique:** extend the incision across the sternum to the right hemithorax at the same intercostal level; divide the sternum with Gigli saw or heavy scissors (cut through the costochondral cartilage)
**Advantage:** complete access to both hemithoraces, superior mediastinum, both lung hila

### Hilar Cross-Clamp
- For massive pulmonary hemorrhage or air embolism
- Apply Satinsky clamp to the pulmonary hilum en masse on the affected side
- Prevents ongoing hemorrhage and air entrainment

### Post-Procedure
- If ROSC: immediate transfer to OR for definitive repair (chest left open)
- Continue MTP; calcium gluconate 1-2 g IV per 4 units pRBC
- Warm all fluids (target temp > 35 degrees C)

## Disposition

- **ROSC achieved:** immediate OR for definitive surgical repair; ICU postoperatively
- **No ROSC after 15 minutes of open cardiac massage with tamponade released and cross-clamp applied:** terminate resuscitation
- **Transfer:** if ROSC achieved at a facility without trauma surgery, leave chest open, maintain tube thoracostomy and MTP, emergent transfer to Level I trauma center

**Termination Criteria:**
- Asystole after pericardiotomy, internal massage, and correction of all reversible causes
- No cardiac electrical activity after internal defibrillation and epinephrine
- Non-survivable injury (cardiac avulsion, great vessel transection not amenable to clamping)

## Pitfalls

1. **Performing thoracotomy for blunt arrest without signs of life.** Survival is near zero for blunt trauma without prehospital signs of life. EAST 2015 specifically recommends against this. Reserve for blunt arrest with signs of life within 10 minutes.

2. **Opening the wrong hemithorax.** Penetrating trauma dictates the side — if the wound is on the right, a right thoracotomy is needed for access to the right hilum and right atrium. If the wrong side is opened, extend to clamshell rather than closing and re-opening. A left thoracotomy can access the heart but not the right lung.

3. **Cutting the phrenic nerve during pericardiotomy.** The phrenic nerve runs along the lateral pericardium. Incise ANTERIOR and PARALLEL to it. Transection causes permanent hemidiaphragm paralysis and respiratory compromise in survivors.

4. **Applying transthoracic defibrillation energy (200-360 J) internally.** Internal defibrillation requires 30 J. Transthoracic energy levels applied directly to the myocardium cause thermal injury and myocardial necrosis.

5. **Not performing bilateral decompression before thoracotomy.** Bilateral tension pneumothorax is a reversible cause of traumatic arrest. Finger thoracostomy takes 30 seconds per side. If hemodynamics restore with decompression alone, thoracotomy is unnecessary.

6. **Attempting thoracotomy without MTP running.** Every patient undergoing ED thoracotomy will require massive transfusion. O-negative blood must be infusing before knife-to-skin. Failure to have blood products immediately available converts a survivable thoracotomy into a futile one.
