---
id: resuscitative-thoracotomy
condition: Resuscitative Thoracotomy
aliases: [ED thoracotomy, emergency department thoracotomy, EDT, clamshell thoracotomy]
icd10: [Z53.09, S26.01XA, S27.1XXA]
esi: 1
time_to_harm:
  irreversible_injury: "< 5 minutes"
  death: "< 10 minutes without intervention"
  optimal_intervention_window: "< 15 minutes from loss of signs of life"
mortality_if_delayed: "Overall survival 7-15% for penetrating trauma, <2% for blunt; survival drops to near zero beyond 15 minutes of pulseless arrest"
category: procedural
track: tier1
confusion_pairs:
  - condition: cardiac-tamponade
    differentiators:
      - "Cardiac tamponade: pericardiocentesis is first-line if patient has pulse; tamponade with ongoing hemorrhage or cardiac arrest from penetrating trauma requires thoracotomy for definitive repair"
      - "Resuscitative thoracotomy: indicated when pericardiocentesis fails or is insufficient, when cardiac arrest is present, or when direct cardiac repair is required"
      - "Critical rule: penetrating trauma + cardiac arrest + prior signs of life = thoracotomy, not pericardiocentesis"
  - condition: tension-pneumothorax
    differentiators:
      - "Tension pneumothorax: needle/finger decompression and tube thoracostomy resolve the pathology; thoracotomy is not required unless massive air leak suggests bronchial injury"
      - "Resuscitative thoracotomy: indicated for traumatic arrest, not isolated pneumothorax; bilateral decompression should precede thoracotomy in trauma arrest algorithm"
      - "Critical rule: decompress both hemithoraces before committing to thoracotomy — tension physiology resolves with tube thoracostomy"
sources:
  - type: guideline
    ref: "Seamon MJ, Haut ER, Van Arendonk K, et al. An evidence-based approach to patient selection for emergency department thoracotomy: A practice management guideline from the Eastern Association for the Surgery of Trauma. J Trauma Acute Care Surg. 2015;79(1):159-173."
    pmid: "26091330"
  - type: guideline
    ref: "Burlew CC, Moore EE, Moore FA, et al. Western Trauma Association critical decisions in trauma: resuscitative thoracotomy. J Trauma Acute Care Surg. 2012;73(6):1359-1363."
    pmid: "23188227"
  - type: review
    ref: "Wise D, Davies G, Coats T, et al. Emergency thoracotomy: how to do it. Emerg Med J. 2005;22(1):22-24."
    pmid: "15611536"
  - type: pubmed
    ref: "Rhee PM, Acosta J, Bridgeman A, et al. Survival after emergency department thoracotomy: review of published data from the past 25 years. J Am Coll Surg. 2000;190(3):288-298."
    pmid: "10703854"
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition. American College of Surgeons. 2018."
last_updated: "2026-02-26"
compiled_by: agent
reviewed_by: "Brandon Dent, MD — Board Certified Emergency Medicine"
review_date: "2026-02-27"
risk_tier: A
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
# Resuscitative Thoracotomy

## Recognition

**Indications (EAST 2015 Guidelines):**

| Mechanism | Signs of Life | Recommendation |
|-----------|---------------|----------------|
| Penetrating cardiac injury | Lost within 15 min of ED arrival | Strongly recommended |
| Penetrating thoracic injury (non-cardiac) | Lost within 15 min | Conditionally recommended |
| Penetrating extrathoracic injury | Lost within 15 min | Conditionally recommended |
| Blunt injury | Lost within 10 min | Conditionally recommended |
| Blunt injury | No signs of life in field | Not recommended |

**Signs of Life:**
- Pupillary reactivity
- Spontaneous movement or respiratory effort
- Organized cardiac electrical activity on monitor
- Measurable or palpable blood pressure

**Contraindications:**
- Penetrating trauma: no signs of life AND >15 minutes of CPR
- Blunt trauma: no signs of life AND >10 minutes of CPR
- Blunt trauma without any signs of life at scene (prehospital asystole)
- Non-survivable injury (e.g., massive open cranial destruction)

**Decision Triggers:**
- Penetrating thoracic trauma with cardiac arrest or peri-arrest and recent signs of life
- Cardiac tamponade unresponsive to pericardiocentesis
- Massive hemothorax with exsanguinating hemorrhage (chest tube output >1500 mL immediate)
- Air embolism from penetrating lung injury
- Need for aortic cross-clamping to redirect blood flow to brain and coronary circulation in subdiaphragmatic hemorrhage

**Survival by Mechanism (EAST data):**
- Penetrating cardiac: 10-35%
- Penetrating thoracic non-cardiac: 8-15%
- Penetrating abdominal: 3-5%
- Blunt trauma: < 2%

## Critical Actions

| Action | Target |
|--------|--------|
| Decision to perform thoracotomy | < 2 minutes from arrest |
| Skin to pericardium | < 3 minutes |
| Aortic cross-clamp (if needed) | Immediately after pericardiotomy |
| Trauma surgery in OR | Within 30 minutes of ED thoracotomy |

1. **Bilateral chest decompression** with finger thoracostomy before thoracotomy — rule out tension pneumothorax as reversible cause
2. **Endotracheal intubation** — secure airway; ventilation required for post-thoracotomy management
3. **Massive transfusion protocol activation** — type O-negative uncrossmatched blood running before incision
4. **Left anterolateral thoracotomy** — position supine with left arm abducted 90 degrees; incision at 5th intercostal space from sternum to posterior axillary line
5. **Pericardiotomy** — open pericardium anterior to the phrenic nerve; evacuate clot and blood
6. **Direct cardiac repair** — control hemorrhage with digital pressure or skin stapler; horizontal mattress sutures with 3-0 prolene for cardiac lacerations (avoid coronary arteries)
7. **Aortic cross-clamping** — compress descending thoracic aorta against vertebral body; apply DeBakey aortic clamp to redirect flow to brain and heart
8. **Internal cardiac massage** — bimanual (two-handed) compression, base to apex; rate 80-100/min
9. **Internal defibrillation** — 30 J with internal paddles for VF; place paddles directly on anterior and posterior surfaces of the heart

## Differential Diagnosis

Before committing to thoracotomy, rapidly exclude or address:

| Alternative | Distinguishing Features |
|-------------|------------------------|
| Tension pneumothorax | Bilateral finger thoracostomy first — if hemodynamics restore, thoracotomy is unnecessary |
| Cardiac tamponade (non-traumatic) | Medical tamponade (uremic, malignant) — pericardiocentesis is primary; thoracotomy only for traumatic tamponade failing needle drainage |
| Massive hemothorax alone | Tube thoracostomy with autotransfusion; if output >1500 mL immediate or >200 mL/hr for 4 hours, proceed to OR; thoracotomy for arrest only |
| Abdominal hemorrhage | Aortic cross-clamping via thoracotomy redirects flow, but definitive control requires laparotomy — thoracotomy is a bridge |
| Air embolism | Aspirate air from RV and aortic root; Trendelenburg, clamp pulmonary hilum on injured side |

**Bail-Out Options:**
- If left thoracotomy provides insufficient access: extend to clamshell (bilateral anterolateral) by dividing the sternum transversely with Gigli saw or heavy scissors
- If cardiac repair beyond ED capability: Foley catheter balloon tamponade through the wound, transfer to OR
- If the wrong hemithorax is opened: extend to clamshell rather than closing and opening the other side

## Workup

**Pre-Procedure (performed simultaneously with decision-making):**
- FAST exam: pericardial fluid, free abdominal fluid, hemothorax — must take < 60 seconds
- Bilateral chest decompression: finger thoracostomy at 5th ICS anterior axillary line
- Endotracheal tube confirmed in place with capnography

**Equipment Tray (must be immediately available):**
- 10-blade scalpel (No. 10 preferred for skin)
- Finochietto rib spreader (large)
- Metzenbaum scissors (long)
- DeBakey aortic cross-clamp
- Satinsky vascular clamp
- Toothed tissue forceps
- Needle drivers (2)
- 3-0 Prolene sutures on SH needle
- 0-silk ties
- Gigli saw (for clamshell extension)
- Internal defibrillator paddles (30 J)
- Foley catheter (for balloon tamponade of cardiac wounds)
- Skin stapler (rapid temporary closure of cardiac lacerations)
- Laparotomy pads

**Labs (drawn but do not delay procedure):**
- Type and crossmatch (activate MTP)
- CBC, BMP, coagulation panel
- ABG/VBG, lactate
- Thromboelastography (TEG) if available

## Treatment

### Step-by-Step: Left Anterolateral Thoracotomy

**1. Positioning and Incision:**
- Patient supine, left arm abducted 90 degrees or extended overhead
- Incision from left sternal border to posterior axillary line along the 5th intercostal space (level of the nipple in males, inframammary fold in females)
- Cut through skin, subcutaneous tissue, and muscle layers with scalpel in one stroke
- Enter the intercostal space above the 6th rib (avoid the neurovascular bundle running along the inferior border of the 5th rib)

**2. Rib Spreading:**
- Insert Finochietto rib spreader with the handle directed toward the axilla (this avoids handle interference with cardiac access)
- Open progressively — aggressive but controlled; rib fracture is acceptable

**3. Pericardiotomy:**
- Identify the pericardium anterior to the descending aorta
- Grasp with forceps and incise with Metzenbaum scissors
- Incise longitudinally, ANTERIOR and PARALLEL to the phrenic nerve (the phrenic nerve runs on the lateral surface of the pericardium)
- Evacuate clot and blood manually — clot removal alone restores cardiac filling

**4. Cardiac Hemorrhage Control:**
- Identify the cardiac wound
- Digital pressure with a finger over the wound
- Skin stapler across small lacerations (rapid temporary closure)
- For larger wounds: horizontal mattress sutures with 3-0 Prolene on a pledgeted needle; suture parallel to coronary arteries to avoid ligation
- Foley catheter: insert through wound, inflate balloon with 15-30 mL saline, apply gentle traction — tamponades the wound until OR repair

**5. Aortic Cross-Clamping:**
- Retract the left lung anteriorly and superiorly
- Palpate the descending aorta against the vertebral bodies (it is the tubular structure against the spine, posterior and medial)
- Bluntly dissect areolar tissue surrounding the aorta
- Apply DeBakey aortic cross-clamp
- Cross-clamp maximizes coronary and cerebral perfusion during arrest; do not leave in place >30 minutes without releasing to limit ischemia-reperfusion injury

**6. Internal Cardiac Massage:**
- Two-handed technique: place the flat palm behind the heart, compress against the sternum from apex to base
- Rate 80-100 compressions/min
- Effective internal massage generates 2-3x the cardiac output of external chest compressions

**7. Internal Defibrillation:**
- For ventricular fibrillation: apply internal paddles directly on the heart
- Start at 30 J (internal threshold is much lower than transthoracic)
- Saline-soaked laparotomy pads between paddles and myocardium to optimize contact

**8. Hilar Cross-Clamping:**
- For massive pulmonary hemorrhage or air embolism: clamp the pulmonary hilum en masse with a Satinsky clamp on the affected side
- Prevents ongoing hemorrhage and air entrainment

### Post-Procedure
- If ROSC achieved: immediate transfer to OR for definitive repair
- Leave chest open — do not close in the ED
- Continue massive transfusion; calcium gluconate 1-2 g IV per 4 units pRBC
- Warm fluids — hypothermia worsens coagulopathy (target temp >35 degrees C)

## Disposition

- **ROSC achieved:** Immediate OR for definitive surgical repair; ICU postoperatively
- **No ROSC after 15 minutes of open cardiac massage with corrected tamponade and cross-clamp:** Terminate resuscitation
- **Transfer:** If the facility lacks trauma surgery capability and ROSC is achieved, arrange emergent transfer to Level I trauma center with chest left open, tube thoracostomy in place, and ongoing MTP

**Termination criteria:**
- Asystole after pericardiotomy, internal massage, and correction of all reversible causes
- No cardiac electrical activity after internal defibrillation and epinephrine
- Non-survivable injury identified (e.g., cardiac avulsion, transected great vessel not amenable to clamping)

## Pitfalls

1. **Performing thoracotomy for blunt trauma with no prehospital signs of life.** Survival is near zero. EAST guidelines specifically recommend against this. Reserve thoracotomy for blunt arrest with signs of life within 10 minutes of arrival or witnessed loss of vitals.

2. **Failing to decompress both hemithoraces before thoracotomy.** Bilateral tension pneumothorax is a reversible cause of traumatic arrest. Finger thoracostomy takes 30 seconds per side and avoids a futile thoracotomy when tube decompression restores circulation.

3. **Cutting the phrenic nerve during pericardiotomy.** The phrenic nerve runs along the lateral pericardial surface. Incise anterior and parallel to it. Phrenic transection causes permanent hemidiaphragm paralysis and postoperative respiratory compromise.

4. **Hesitation bias — delaying the decision while the survival window closes.** The entire value of ED thoracotomy depends on speed. The decision must be made within 2 minutes of arrest. Survival drops to near zero beyond 15 minutes of downtime. A delayed thoracotomy is a futile thoracotomy.

5. **Suturing across a coronary artery during cardiac repair.** Identify the LAD and circumflex before placing sutures. Horizontal mattress sutures parallel to coronary vessels. Coronary ligation causes immediate regional wall motion abnormality and VF.

6. **Leaving the aortic cross-clamp in place for >30 minutes.** Prolonged cross-clamping causes mesenteric and renal ischemia, acidosis, and reperfusion injury. Release periodically if hemodynamics allow. Communicate cross-clamp time to the trauma surgeon.

7. **Attempting thoracotomy without MTP activation.** Every patient undergoing ED thoracotomy requires massive transfusion. Activate MTP before knife-to-skin. O-negative blood must be running through large-bore IV access during the procedure.

8. **Using external defibrillation energy for internal defibrillation.** Internal defibrillation requires 30 J, not 200-360 J. Applying transthoracic energy to an open chest causes myocardial injury. Use internal paddles with dedicated low-energy settings.

### Complication Management
- **Inadvertent lung laceration from rib spreader:** pack and clamp hilum if bleeding is significant; lung parenchyma hemorrhage is usually low pressure and self-limited
- **Intercostal artery hemorrhage from incision:** ligate or clamp intercostal vessels; these are systemic pressure and bleed briskly
- **Rib fracture during spreading:** expected and acceptable; manage pain postoperatively if patient survives
- **Phrenic nerve injury:** if identified intraoperatively, primary repair with 7-0 nylon microsutures; otherwise manage postoperative respiratory compromise with diaphragm plication
