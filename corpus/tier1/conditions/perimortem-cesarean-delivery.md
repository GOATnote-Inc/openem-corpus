---
id: perimortem-cesarean-delivery
condition: Perimortem Cesarean Delivery
aliases: [resuscitative hysterotomy, perimortem C-section, PMCD, emergency cesarean in arrest]
icd10: [O75.82, O99.11, O75.1]
esi: 1
time_to_harm:
  irreversible_injury: "< 4 minutes (fetal neurological injury)"
  death: "< 10 minutes maternal and fetal without delivery"
  optimal_intervention_window: "< 4 minutes from maternal cardiac arrest"
mortality_if_delayed: "Fetal survival 70% if delivered within 5 minutes of maternal arrest; drops to <10% after 10 minutes. Maternal ROSC improves in 30-40% after aortocaval relief"
category: procedural
track: tier1
confusion_pairs:
  - condition: amniotic-fluid-embolism
    differentiators:
      - "Amniotic fluid embolism: perimortem cesarean is a resuscitative maneuver for maternal benefit (aortocaval decompression) AND fetal rescue; AFE is a potential etiology of the arrest, not a differential for the procedure"
      - "Perimortem cesarean: performed regardless of arrest etiology; the procedure itself improves maternal hemodynamics by relieving IVC compression from the gravid uterus"
      - "Critical rule: do not delay perimortem cesarean to diagnose the cause of arrest — the etiology is investigated after delivery"
  - condition: cord-prolapse
    differentiators:
      - "Cord prolapse: emergent cesarean is indicated but in the OR with anesthesia if maternal hemodynamics are stable; the urgency is fetal, not maternal"
      - "Perimortem cesarean: maternal cardiac arrest is the trigger; performed at bedside without anesthesia; the primary goal is maternal resuscitation via aortocaval decompression"
      - "Critical rule: cord prolapse with a pulsatile maternal rhythm is an OR cesarean; cord prolapse with maternal arrest is a perimortem cesarean at bedside"
sources:
  - type: guideline
    ref: "Jeejeebhoy FM, Zelop CM, Lipman S, et al. Cardiac Arrest in Pregnancy: A Scientific Statement From the American Heart Association. Circulation. 2015;132(18):1747-1773."
    pmid: "26472867"
  - type: pubmed
    ref: "Katz VL, Dotters DJ, Droegemueller W. Perimortem cesarean delivery. Obstet Gynecol. 1986;68(4):571-576."
    pmid: "3528956"
  - type: guideline
    ref: "Lipman S, Cohen S, Einav S, et al. The Society for Obstetric Anesthesia and Perinatology consensus statement on the management of cardiac arrest in pregnancy. Anesth Analg. 2014;118(5):1003-1016."
    pmid: "24781570"
  - type: review
    ref: "Einav S, Kaufman N, Sela HY. Maternal cardiac arrest and perimortem caesarean delivery: evidence or expert-based? Resuscitation. 2012;83(10):1191-1200."
    pmid: "22521449"
  - type: guideline
    ref: "AHA/ACLS Guidelines for Cardiac Arrest in Pregnancy. 2020 Update."
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
# Perimortem Cesarean Delivery

## Recognition

**Definition:** Cesarean delivery performed during maternal cardiac arrest as a resuscitative maneuver. The primary indication is maternal — aortocaval decompression improves venous return and cardiac output by 30-40%. Fetal rescue is a secondary benefit.

**The 4-Minute Rule (Katz 1986):**
- If ROSC is not achieved within 4 minutes of maternal cardiac arrest, begin perimortem cesarean
- Target: delivery within 5 minutes of arrest onset (1 minute for the procedure itself)
- This timeline is based on fetal neurological outcomes AND the physiologic benefit of uterine evacuation to maternal resuscitation
- The 4-minute rule applies when the uterus is at or above the umbilicus (approximately >=20 weeks gestation)

**Indications:**
- Maternal cardiac arrest with fundal height at or above the umbilicus (>=20 weeks)
- CPR in progress without ROSC after 4 minutes of standard ACLS
- The procedure is performed regardless of fetal viability — the primary goal is maternal resuscitation

**Maternal Indications (primary):**
- Aortocaval decompression: the gravid uterus at >=20 weeks compresses the IVC and aorta in the supine position, reducing cardiac output by 30-40% even with optimal CPR
- Improved chest compliance after uterine evacuation
- Reduced oxygen consumption after delivery

**Fetal Indications (secondary):**
- Viable fetus (>=23-24 weeks): delivery enables neonatal resuscitation
- Non-viable fetus (<23 weeks): delivery still indicated for maternal benefit

**Contraindications:**
- Fundal height below the umbilicus (<20 weeks) — uterus does not cause significant aortocaval compression
- Obvious non-survivable maternal injury (e.g., decapitation, massive cranial destruction)
- Known prolonged maternal downtime (>25 minutes without CPR)

**Etiologies of Maternal Cardiac Arrest (BEAUCHOPS mnemonic):**
- **B**leeding/DIC
- **E**mbolism (pulmonary, amniotic fluid)
- **A**nesthetic complications
- **U**terine atony
- **C**ardiac disease (peripartum cardiomyopathy, MI, arrhythmia)
- **H**ypertension/eclampsia
- **O**ther (sepsis, anaphylaxis)
- **P**lacental abruption/previa
- **S**earch for reversible causes (H's and T's)

## Critical Actions

| Action | Target |
|--------|--------|
| Manual left uterine displacement | Immediate at arrest onset |
| Decision to perform cesarean | 4 minutes from arrest onset |
| Delivery (skin to delivery) | < 1 minute (5 minutes total from arrest) |
| Neonatology at bedside | Before incision |

1. **Call maternal code team** — OB, anesthesia, neonatology, NICU, blood bank. Do not wait for the full team to arrive before starting CPR or making the decision.

2. **Manual left uterine displacement** — first intervention; tilt uterus to the left manually with one hand while CPR continues; do NOT use a left lateral tilt position (degrades CPR quality)

3. **Standard ACLS with pregnancy modifications:**
   - No dose modification for epinephrine or vasopressors
   - Standard defibrillation energy (biphasic 120-200 J) — do not reduce for pregnancy
   - Remove fetal monitors — they interfere with resuscitation and provide no actionable data
   - IV access above the diaphragm (femoral access impaired by aortocaval compression)

4. **At 4 minutes: begin perimortem cesarean at the bedside.** Do not transfer to OR. Do not wait for OB. The emergency physician performs this procedure if OB is not immediately present.

5. **Activate massive transfusion protocol** — hemorrhage is common post-delivery; type O-negative running before incision

6. **Neonatal resuscitation team at bedside** with warmer, intubation equipment, and surfactant for premature delivery

## Differential Diagnosis

The procedure itself has no differential — it is an intervention, not a diagnosis. The differential applies to the etiology of maternal cardiac arrest:

| Etiology | Key Differentiators |
|----------|---------------------|
| Amniotic fluid embolism | Sudden collapse during labor or within 30 min postpartum; DIC developing rapidly; bedside echo shows LV dysfunction |
| Massive pulmonary embolism | RV dilation on bedside echo; consider tPA 50 mg IV during arrest |
| Placental abruption | Vaginal bleeding, rigid uterus, fetal distress preceding arrest |
| Eclampsia/magnesium toxicity | Seizure preceding arrest; hypertension; give calcium gluconate 1 g IV for Mg toxicity |
| Peripartum cardiomyopathy | Heart failure symptoms in late pregnancy/early postpartum; echo shows dilated LV with reduced EF |
| Hemorrhagic shock | Ongoing visible hemorrhage; DIC; massive transfusion required |
| Local anesthetic toxicity | Arrest during or immediately after regional anesthesia; give lipid emulsion 20% 1.5 mL/kg IV bolus |

**Alternative Techniques:**
- Classical (vertical) midline incision is the standard for perimortem cesarean — faster than low transverse, does not require bladder dissection
- If the operator is experienced with low transverse cesarean and can deliver in <1 minute, either approach is acceptable
- Clamshell thoracotomy may be required if arrest etiology is suspected thoracic (massive PE, aortic dissection)

## Workup

**Pre-Procedure Assessment (performed in <60 seconds during CPR):**
- Estimate gestational age: fundal height at or above umbilicus = >=20 weeks
- Confirm cardiac arrest: no pulse, CPR in progress
- Clock the arrest time: the 4-minute timer starts at witnessed arrest or arrival of code team for unwitnessed arrest

**Equipment (must be immediately available on every L&D unit and in every ED):**
- 10-blade scalpel (the ONLY essential instrument)
- Bandage scissors (for extending incision)
- Kelly clamps x2 (for cord clamping)
- Suction
- Sterile towels for neonatal wrapping
- Neonatal warmer and resuscitation equipment

**Sterile Prep:**
- Betadine splash only — do not scrub; do not drape; do not gown/glove beyond what takes <10 seconds
- The priority is speed, not sterility — infection is treated; death from delayed delivery is not

**Labs (drawn during CPR, results do not change the decision to deliver):**
- Type and crossmatch (activate MTP)
- CBC, BMP, coags, fibrinogen
- ABG/VBG, lactate
- Kleihauer-Betke (postpartum to assess fetomaternal hemorrhage)

## Treatment

### Step-by-Step: Classical Vertical Midline Perimortem Cesarean

**1. CPR Continues Throughout — do not stop compressions for the procedure.**

**2. Incision:**
- Vertical midline skin incision from just below the xiphoid process to the symphysis pubis
- Use the 10-blade scalpel; cut through skin, subcutaneous fat, linea alba in one deliberate stroke
- If unsure of depth, make a smaller initial incision and extend — but do NOT waste time on tentative shallow passes

**3. Enter the Peritoneum:**
- Identify the peritoneum (thin, glistening membrane)
- Nick with the scalpel and extend with scissors or fingers
- The bladder is inferior — stay superior to avoid bladder injury (the full bladder in pregnancy is displaced superiorly)

**4. Uterine Incision:**
- Identify the uterine fundus
- Make a vertical incision in the upper uterine body (classical incision) — this avoids the lower uterine segment where the bladder is attached
- Incise through the uterine wall; amniotic fluid will gush
- Extend the incision with bandage scissors to deliver the fetus

**5. Deliver the Fetus:**
- Reach into the uterus and deliver the fetus, head first if cephalic, feet first if breech
- Clamp and cut the cord with Kelly clamps
- Hand the neonate immediately to the neonatal resuscitation team
- Do NOT delay cord clamping — maternal resuscitation takes priority

**6. Deliver the Placenta:**
- Gentle traction on the cord with counter-traction on the uterus
- If the placenta does not deliver with gentle traction within 30-60 seconds, leave it; focus on uterine hemorrhage control and maternal resuscitation

**7. Uterine Hemorrhage Control:**
- Oxytocin 10 units IV bolus (diluted) plus 20-40 units in 1 L NS infusion
- Bimanual uterine massage
- Uterine packing if hemorrhage continues
- Methylergonovine 0.2 mg IM if no hypertension
- Carboprost 0.25 mg IM if no asthma
- Misoprostol 800-1000 mcg PR
- B-Lynch compression suture or hysterectomy for refractory hemorrhage (in OR)

**8. Continue Maternal Resuscitation:**
- After delivery, the aortocaval compression is relieved — chest compressions become more effective
- Reassess rhythm and pulse
- ROSC rates improve significantly after delivery (case series data: 39-54% ROSC post-delivery)
- Continue ACLS protocol; treat the underlying cause

### Post-Delivery
- Leave the abdominal incision open or loosely approximated if transferring to OR
- Continue MTP as needed
- Serial coagulation labs every 30 minutes
- Tranexamic acid 1 g IV over 10 min if hemorrhage persists

## Disposition

- **Maternal ROSC achieved:** ICU admission; definitive surgical repair of uterine incision in OR if not performed in ED; continuous hemodynamic monitoring; serial labs
- **Maternal ROSC not achieved:** Continue ACLS for at least 15-20 minutes post-delivery before termination; the post-delivery period has the highest likelihood of ROSC
- **Neonate:** NICU admission; cord blood gas; monitoring for hypoxic ischemic encephalopathy; therapeutic hypothermia if indicated (>=36 weeks with evidence of encephalopathy)
- **Transfer:** If facility lacks OB surgery and NICU — stabilize both patients and arrange emergent transfer; maternal hemorrhage control takes priority during transport

## Pitfalls

1. **Waiting for OB to arrive before starting the procedure.** The 4-minute window does not pause for consultant arrival. Every emergency physician must be trained and willing to perform perimortem cesarean. If OB arrives during the procedure, they take over; if not, the EP completes it.

2. **Attempting prolonged CPR without cesarean when fundal height is above the umbilicus.** Standard CPR is ineffective in late pregnancy due to aortocaval compression. After 4 minutes without ROSC, CPR alone will not restore circulation. Delivery is the resuscitative intervention.

3. **Transferring the patient to the OR for cesarean during cardiac arrest.** Moving an arresting patient degrades CPR quality and wastes the survival window. Perimortem cesarean is performed at the bedside — in the ED, on L&D, wherever the arrest occurs.

4. **Using a low transverse (Pfannenstiel) skin incision.** The vertical midline incision is faster and provides better exposure. Low transverse incisions require bladder dissection and take 2-3 minutes longer. In an arrest, every minute matters.

5. **Stopping CPR during the incision.** Chest compressions continue throughout the procedure. The surgeon operates from the patient's left side while the code team performs compressions. CPR stops only momentarily for rhythm checks.

6. **Delaying because gestational age is uncertain or fetus is previable.** The procedure is primarily for maternal resuscitation. A 16-week-sized uterus does not cause significant aortocaval compression and does not require delivery. A 24-week-sized uterus does, regardless of fetal viability expectations.

7. **Excessive focus on sterile technique.** A splash of betadine and gloves are sufficient. Full sterile prep, draping, and gowning cost 3-5 minutes that the mother and fetus do not have. Surgical site infection is treated with antibiotics; delayed delivery during arrest is treated with a body bag.

8. **Failing to activate neonatology and MTP before incision.** The neonate requires immediate resuscitation at delivery. The mother requires massive transfusion for post-delivery hemorrhage. Both resources must be en route before the scalpel touches skin.

### Complication Management
- **Uterine atony post-delivery:** bimanual massage, oxytocin, methylergonovine, carboprost, misoprostol in escalating sequence; B-Lynch suture or hysterectomy for refractory cases
- **Bladder injury from incision:** primary repair with 3-0 Vicryl in two layers; Foley catheter drainage for 7-14 days postoperatively
- **Bowel injury:** primary repair if clean contamination; diverting ostomy if fecal contamination — defer to surgical team
- **Massive hemorrhage from uterine incision:** uterine artery ligation, internal iliac artery ligation, or hysterectomy as definitive hemorrhage control
