---
id: breech-precipitous-delivery
condition: Breech Precipitous Delivery
aliases: [emergency vaginal breech delivery, breech extraction, precipitous breech birth, ED breech delivery]
icd10: [O32.1XX0, O62.3, O80, O83.0]
esi: 1
time_to_harm:
  irreversible_injury: "< 5 minutes (head entrapment → fetal anoxia)"
  death: "< 8 minutes without delivery of after-coming head"
  optimal_intervention_window: "Immediate upon recognition of breech in active delivery"
category: procedural
track: tier1
confusion_pairs:
  - condition: cord-prolapse
    differentiators:
      - "Cord prolapse: palpable or visible umbilical cord ahead of the presenting part; fetal bradycardia; management is manual elevation of the presenting part off the cord and emergent cesarean — NOT vaginal delivery"
      - "Breech precipitous delivery: breech presentation with imminent or active vaginal delivery; the fetus is already delivering and cesarean is no longer an option; management is assisted vaginal breech delivery using specific maneuvers"
      - "Critical rule: cord prolapse with a breech presentation requires cesarean (elevate presenting part, fill bladder, OR); a breech that is already delivering through the introitus requires vaginal delivery — different pathways entirely"
  - condition: perimortem-cesarean-delivery
    differentiators:
      - "Perimortem cesarean: maternal cardiac arrest is the trigger; performed for maternal resuscitation"
      - "Breech precipitous delivery: maternal hemodynamics are intact; the problem is obstetric — a malpresentation requiring specific delivery maneuvers"
      - "Critical rule: if the breech is visible at the introitus and delivery is imminent, vaginal delivery is faster and safer than emergency cesarean"
sources:
  - type: guideline
    ref: "ACOG Committee Opinion No. 745: Mode of Term Singleton Breech Delivery. Obstet Gynecol. 2018;132(2):e60-e63."
    pmid: "30045204"
  - type: guideline
    ref: "RCOG Green-top Guideline No. 20b: Management of Breech Presentation. Royal College of Obstetricians and Gynaecologists. 2017."
  - type: review
    ref: "Kotaska A. Inappropriate use of randomised trials to evaluate complex phenomena: case study of vaginal breech delivery. BMJ. 2004;329(7473):1039-1042."
    pmid: "15514354"
  - type: pubmed
    ref: "Hofmeyr GJ, Hannah M, Lawrie TA. Planned caesarean section for term breech delivery. Cochrane Database Syst Rev. 2015;(7):CD000166."
    pmid: "26196961"
  - type: review
    ref: "Crofts JF, Bartlett C, Ellis D, et al. Training for shoulder dystocia: a trial of simulation using low-fidelity and high-fidelity mannequins. Obstet Gynecol. 2006;108(6):1477-1485."
    pmid: "17138783"
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
# Breech Precipitous Delivery

## Recognition

**Definition:** Vaginal delivery of a breech-presenting fetus that arrives in the ED actively delivering or with delivery imminent (crowning breech, buttocks visible at introitus). This is NOT an elective vaginal breech birth — it is an emergency where cesarean is no longer feasible because delivery is in progress.

**Breech Presentation Types:**
- **Frank breech** (65%): hips flexed, knees extended — buttocks present first; most favorable for vaginal delivery
- **Complete breech** (10%): hips and knees flexed — buttocks and feet present together
- **Footling breech** (25%): one or both feet present below the buttocks — highest risk of cord prolapse and head entrapment

**When This Occurs in the ED:**
- Undiagnosed breech in precipitous labor (no prenatal care, no prior ultrasound)
- Known breech with premature labor arriving too late for cesarean
- Out-of-hospital delivery in progress on arrival

**Key Assessment on Arrival:**
- Cervical dilation: if fully dilated with breech at introitus, vaginal delivery is the plan
- Fetal presentation and type: palpate for sacrum (breech) vs. skull (vertex); anus and genitalia help orient
- Fetal heart tones: continuous monitoring if available; bradycardia <100 bpm warrants urgent delivery
- Estimated gestational age: premature breech has higher risk of head entrapment (smaller body, relatively larger head)
- Cord prolapse: feel for pulsatile cord alongside presenting part — if present, this changes the algorithm entirely (see cord-prolapse)

**Indications for Vaginal Breech Delivery (in ED context):**
- Breech is delivering spontaneously through the introitus — no time for cesarean
- Cervix is fully dilated with breech descending rapidly
- OR not available or not achievable in the time remaining

**Contraindications to Vaginal Breech (if time permits cesarean):**
- Footling breech (highest cord prolapse risk)
- Estimated fetal weight >3.8 kg (head entrapment risk)
- Hyperextended fetal head on imaging (star-gazing fetus — spinal cord injury risk)
- Prior classical (vertical) uterine incision
- These contraindications are moot if delivery is already happening

## Critical Actions

| Action | Target |
|--------|--------|
| OB consultation and neonatology | Immediately upon recognition |
| Continuous fetal monitoring | Throughout delivery |
| Hands-off until umbilicus | Allow spontaneous descent to umbilicus |
| Delivery of after-coming head | < 5 minutes from delivery of umbilicus |

1. **Call OB, anesthesia, and neonatology** — this is a high-risk delivery; every available resource should be at bedside. If OB cannot arrive before delivery, the EP delivers the baby.
2. **Position the patient** — lithotomy position with buttocks at edge of bed; McRoberts position (hips hyperflexed) is NOT used for breech — it is for shoulder dystocia in cephalic deliveries.
3. **Do NOT pull on the baby** — the cardinal rule of breech delivery. Traction on the body causes arm extension and head deflection, both of which cause entrapment. Allow gravity and maternal expulsive effort.
4. **Hands-off technique until the umbilicus delivers** — support the body loosely; do not grasp or apply downward traction.
5. **After umbilicus delivers:** gently extract a loop of umbilical cord to prevent traction. Then assist with delivery of arms and head using specific maneuvers (below).
6. **Episiotomy** — generous mediolateral episiotomy to maximize soft-tissue space for the after-coming head. Cut early, not late.

## Differential Diagnosis

| Scenario | Distinguishing Features | Management |
|----------|------------------------|------------|
| Vertex precipitous delivery | Skull presenting; no malpresentation; standard delivery technique | Support perineum, controlled delivery of head, check for nuchal cord |
| Shoulder presentation/transverse lie | Shoulder or arm presenting; cannot deliver vaginally | Emergent cesarean section — no vaginal delivery possible |
| Cord prolapse with breech | Pulsatile cord felt alongside or ahead of presenting part | Elevate presenting part off cord, fill bladder (500 mL NS via Foley), emergent cesarean |
| Footling breech with foot at introitus | Foot visible before buttocks; cervix may not be fully dilated | High risk — if cervix not fully dilated, the foot can deliver through an incomplete cervix that then traps the head; cesarean preferred if achievable |
| Compound presentation | Extremity alongside the presenting part | Gentle reduction of the extremity; if unsuccessful, cesarean |

**Alternative Techniques / Bail-Out:**
- If head is entrapped and all maneuvers fail: Zavanelli maneuver (replace the body into the uterus and perform emergency cesarean) — this is a desperation maneuver with high morbidity
- Symphysiotomy: surgical division of the pubic symphysis to increase pelvic diameter — rarely performed in developed settings but described in resource-limited environments
- Duhrssen incisions: three cervical incisions at 2, 6, and 10 o'clock to enlarge an incompletely dilated cervix trapping the head — high hemorrhage risk

## Workup

**Pre-Delivery Assessment (performed in <2 minutes):**
- Fetal heart tones: Doppler or continuous electronic fetal monitoring
- Cervical exam: confirm full dilation (10 cm) and breech presentation
- Palpate for cord: rule out cord prolapse
- Estimate fetal weight and gestational age (fundal height, patient history)
- Type and screen (anticipate possible hemorrhage or emergent cesarean)

**Equipment at Bedside:**
- Warm towels and blankets (wrap the fetal body as it delivers to prevent cold-stimulated gasping)
- Sterile gloves, gown
- Episiotomy scissors (Mayo scissors)
- Cord clamps x2, scissors for cord cutting
- Piper forceps (for after-coming head — if available)
- Neonatal warmer, resuscitation equipment, intubation kit
- Oxygen for maternal supplementation
- Oxytocin 10 units IV ready (for post-delivery uterine atony)
- Suction (DeLee suction trap for neonatal airway)

**Do NOT delay delivery for imaging.** Ultrasound to confirm presentation is useful only if time permits. If the breech is visible, the diagnosis is made.

## Treatment

### Step-by-Step: Assisted Vaginal Breech Delivery

**Phase 1: Spontaneous Delivery to Umbilicus (HANDS OFF)**
- Allow the breech to deliver spontaneously with maternal pushing
- Support the baby's body loosely with a warm towel — do NOT pull or apply downward traction
- The sacrum should rotate to the anterior position (sacrum facing up)
- Once the umbilicus delivers, gently extract a loop of cord

**Phase 2: Delivery of the Legs (if Frank Breech)**
- In frank breech, the legs are extended alongside the body
- Pinard maneuver: apply pressure to the popliteal fossa of each leg, causing knee flexion and spontaneous leg delivery
- Sweep each leg out gently

**Phase 3: Delivery of the Arms**

*Lovset Maneuver (rotational technique for nuchal arms):*
- Grasp the fetal pelvis with both thumbs on the sacrum (never grasp the abdomen — risk of visceral injury)
- Rotate the body 90 degrees so one shoulder is anterior (under the pubic symphysis)
- The anterior arm delivers spontaneously or with gentle downward sweep across the chest
- Rotate 180 degrees in the opposite direction, bringing the other shoulder anterior
- Deliver the second arm with the same downward sweep

*If arms are extended above the head (nuchal arms):*
- Lovset rotation usually resolves this
- If rotation fails: hook a finger over the fetal elbow and sweep the arm down across the face and chest — deliver one arm at a time

**Phase 4: Delivery of the After-Coming Head**

*Mauriceau-Smellie-Veit Maneuver (primary technique):*
- Place the fetal body face-down on the operator's forearm
- Place the index and middle fingers of the hand supporting the face on the fetal maxilla (NOT in the mouth — avoid mandibular injury)
- The other hand straddles the fetal shoulders and neck, with the middle finger applying gentle flexion pressure on the occiput
- Apply steady downward traction until the hairline is visible under the pubic symphysis
- Then elevate the body (flex upward toward the maternal abdomen) to deliver the face, brow, and vertex over the perineum
- An assistant applies suprapubic pressure (Wigand-Martin maneuver) to maintain head flexion

*Burns-Marshall Technique (alternative):*
- Grasp the fetal feet and hold the body suspended vertically
- Gravity flexes the head
- The weight of the body gradually delivers the head
- Use only gentle traction — the head delivers by gravity and maternal effort

*Piper Forceps (if available and operator experienced):*
- Apply Piper forceps to the after-coming head
- The body is held upward by an assistant while the operator applies forceps from below (kneeling position)
- Controlled traction delivers the head with minimal trauma
- This is the safest method for the after-coming head when forceps are available

**Phase 5: Post-Delivery**
- Clamp and cut the cord
- Hand the neonate to the neonatal resuscitation team
- Assess for perineal lacerations and repair
- Deliver the placenta: controlled cord traction with counter-traction on the uterus
- Oxytocin 10-40 units in 1 L NS IV infusion for uterine contraction
- Assess for postpartum hemorrhage

### Emergency Scenario: Head Entrapment

Head entrapment is the most feared complication. If the Mauriceau maneuver fails:
1. **Suprapubic pressure** by an assistant — push the fetal head toward flexion
2. **Generous episiotomy** if not already performed — mediolateral, not midline
3. **Duhrssen incisions** if the cervix is the source of entrapment (not fully dilated): incise cervix at 2, 6, and 10 o'clock positions with scissors — expect hemorrhage
4. **Zavanelli maneuver** (replacement and cesarean): rotate the body to the pre-delivery position, push the body back into the uterus, perform emergency cesarean. Terbutaline 0.25 mg SC to relax the uterus before replacement.

## Disposition

- **Mother:** admit for postpartum observation; high risk for postpartum hemorrhage, cervical lacerations, and uterine atony
- **Neonate:** NICU or well-baby nursery based on gestational age, Apgar scores, and delivery complications; cord blood gas; brachial plexus exam; head ultrasound if traumatic delivery
- **If emergency cesarean performed instead:** ICU or post-anesthesia recovery; standard post-cesarean care
- **Transfer:** if neonatology/NICU not available and neonate requires resuscitation, arrange neonatal transport immediately

## Pitfalls

1. **Pulling on the body during delivery.** Traction on the breech body causes the arms to extend above the head (nuchal arms) and the head to deflect (extend), both of which increase the risk of head entrapment. The hands-off technique until the umbilicus delivers is the single most critical principle.

2. **Panicking and performing an emergency cesarean when the breech is already at the introitus.** Once the body is delivering vaginally, pushing it back and performing cesarean is more dangerous than completing the vaginal delivery. The decision point for cesarean is before the body delivers — once it starts, commit to vaginal delivery.

3. **Failing to cut an episiotomy for the after-coming head.** The after-coming head is the largest part of the fetus and must pass through the soft tissue last (unlike vertex delivery where the head molds during descent). A generous mediolateral episiotomy provides the space needed to prevent head entrapment.

4. **Placing fingers in the fetal mouth during the Mauriceau maneuver.** The fingers rest on the maxilla (cheekbones), NOT in the mouth. Downward pressure on the mandible fractures the jaw. This is the most common technical error.

5. **Not wrapping the fetal body in a warm towel during delivery.** Cold exposure triggers fetal gasping. Gasping with the head still in the birth canal causes aspiration of amniotic fluid and vaginal secretions. Warm towels maintain fetal temperature and prevent premature respiratory effort.

6. **Attempting breech delivery with an incompletely dilated cervix.** The body (smaller) can deliver through 7-8 cm dilation, but the head (larger) becomes trapped. If the cervix is not fully dilated and delivery is not imminent, cesarean is the correct pathway. Duhrssen incisions are a last resort, not a planned approach.

7. **Grasping the fetal abdomen instead of the pelvis.** When rotation or traction is required, hands must be on the bony pelvis (thumbs on sacrum, fingers on iliac crests). Grasping the abdomen causes splenic laceration, hepatic injury, or bowel perforation.

### Complication Management
- **Nuchal arms (arms trapped behind the head):** Lovset rotational maneuver; if this fails, hook a finger over the elbow and sweep each arm down across the chest individually
- **Head entrapment:** Mauriceau maneuver → suprapubic pressure → episiotomy → Duhrssen cervical incisions → Zavanelli maneuver with terbutaline 0.25 mg SC
- **Cord prolapse during delivery:** rapid completion of delivery is preferred over cesarean if the body is already delivering; keep cord warm and moist, minimize handling
- **Cervical spine injury in the neonate:** maintain inline stabilization; avoid excess traction on the head; monitor for hypotonia, apnea, bradycardia at birth
