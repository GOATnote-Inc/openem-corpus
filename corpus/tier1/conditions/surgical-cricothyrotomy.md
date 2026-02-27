---
id: surgical-cricothyrotomy
condition: Surgical Cricothyrotomy
aliases: [emergency surgical airway, cricothyroidotomy, front of neck access, FONA, cric]
icd10: [T88.4XXA, Z53.09]
esi: 1
time_to_harm:
  irreversible_injury: "< 4 minutes (anoxic brain injury from failed oxygenation)"
  death: "< 8 minutes without oxygenation"
  optimal_intervention_window: "< 30 seconds from CICO declaration"
mortality_if_delayed: "CICO event mortality 25-50% when surgical airway delayed; procedure success rate >90% when performed within 30 seconds of CICO declaration"
category: procedural
track: tier1
confusion_pairs:
  - condition: difficult-airway-management
    differentiators:
      - "Difficult airway management: the overarching algorithm encompassing all airway strategies from RSI to surgical airway; cricothyrotomy is the final rescue step"
      - "Surgical cricothyrotomy: a specific procedure performed when all non-surgical techniques have failed (CICO); it is the endpoint of the difficult airway algorithm, not a standalone decision"
      - "Critical rule: surgical cricothyrotomy should not be a standalone plan except in complete upper airway obstruction (expanding neck hematoma, massive angioedema, laryngeal fracture) where oral/nasal access is anatomically impossible"
sources:
  - type: guideline
    ref: "Apfelbaum JL, Hagberg CA, Connis RT, et al. 2022 American Society of Anesthesiologists Practice Guidelines for Management of the Difficult Airway. Anesthesiology. 2022;136(1):31-81."
    pmid: "34762729"
  - type: guideline
    ref: "Frerk C, Mitchell VS, McNarry AF, et al. Difficult Airway Society 2015 guidelines for management of unanticipated difficult intubation in adults. Br J Anaesth. 2015;115(6):827-848."
    pmid: "26556848"
  - type: pubmed
    ref: "Cook TM, Woodall N, Frerk C; Fourth National Audit Project. Major complications of airway management in the UK: results of the Fourth National Audit Project. Br J Anaesth. 2011;106(5):617-631."
    pmid: "21447488"
  - type: review
    ref: "Bair AE, Panacek EA, Wisner DH, et al. Cricothyrotomy: a 5-year experience at one institution. J Emerg Med. 2003;24(2):151-156."
    pmid: "12609644"
  - type: pubmed
    ref: "Langvad S, Hyldmo PK, Nakstad AR, et al. Emergency cricothyrotomy: a systematic review. Scand J Trauma Resusc Emerg Med. 2013;21:43."
    pmid: "23759277"
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
# Surgical Cricothyrotomy

## Recognition

**Definition:** Emergency surgical airway access through the cricothyroid membrane when oral and nasal intubation and supraglottic airway devices have failed (CICO — Can't Intubate, Can't Oxygenate).

**Indications:**
- CICO: failed endotracheal intubation (>=3 attempts) AND failed supraglottic airway AND failed bag-mask ventilation
- Complete upper airway obstruction not amenable to oral/nasal techniques:
  - Massive angioedema (tongue, oropharynx, supraglottic)
  - Expanding neck hematoma compressing the airway
  - Laryngeal fracture with airway disruption
  - Massive oropharyngeal hemorrhage precluding visualization
  - Fixed upper airway obstruction (tumor, foreign body above the glottis)
  - Severe maxillofacial trauma with distorted anatomy

**Contraindications (relative — in a true CICO, there are no absolute contraindications):**
- Age <10-12 years: needle cricothyrotomy with jet ventilation preferred (smaller cricothyroid membrane, risk of subglottic stenosis); however, surgical cricothyrotomy is performed in children if needle cric fails
- Tracheal transection with retracted distal segment: the distal trachea retracts into the mediastinum — cricothyrotomy accesses the proximal segment but not the distal airway; emergent tracheostomy or direct tracheal intubation in the wound is required
- Laryngotracheal disruption at the cricothyroid level: direct surgical exploration needed

**Anatomy:**
- The cricothyroid membrane is located between the thyroid cartilage (superior) and the cricoid cartilage (inferior)
- Dimensions: approximately 9 mm height x 30 mm width in adults
- It is the most superficial and accessible point of the airway below the glottis
- **Landmarks:** palpate the thyroid cartilage notch (Adam's apple) → slide finger inferiorly over the thyroid cartilage prominence → the soft depression below the thyroid cartilage and above the cricoid ring is the cricothyroid membrane
- In obese or short-necked patients, landmarks are obscured — the "laryngeal handshake" technique (Levitan): use the non-dominant hand to stabilize the larynx with thumb and middle finger on the thyroid cartilage while the index finger palpates the membrane

## Critical Actions

| Action | Target |
|--------|--------|
| Declare CICO verbally | After failed oral + SGA attempts |
| Scalpel on skin | < 30 seconds from CICO declaration |
| Bougie through membrane | < 60 seconds from skin incision |
| Tube in trachea | < 90 seconds from skin incision |
| ETCO2 confirmation | Immediately after tube placement |

1. **Declare CICO** — verbal declaration to the entire team: "This is a CICO. I am performing a surgical airway."
2. **Position** — neck extended (unless c-spine precautions); expose the anterior neck fully
3. **Identify the cricothyroid membrane** — palpate landmarks; if not palpable, use the "4-finger" technique (index finger on sternal notch, identify the cricoid as the first firm ring above)
4. **Scalpel-bougie-tube technique** — described below
5. **Confirm placement with waveform capnography** — ETCO2 is mandatory
6. **Secure the tube** — suture or tape; place ventilator
7. **Call ENT/surgery** for formal conversion to tracheostomy within 24-72 hours

## Differential Diagnosis

Surgical cricothyrotomy is not a diagnostic procedure — it is a rescue airway. The "differential" refers to alternative front-of-neck access techniques:

| Technique | Indication | Notes |
|-----------|-----------|-------|
| Scalpel-bougie-tube (standard) | Adult CICO | Preferred technique (DAS 2015); fastest and most reliable |
| Scalpel-finger-tube | Adult CICO (no bougie available) | Palpation replaces bougie; slightly slower but effective |
| Needle cricothyrotomy + jet ventilation | Pediatric CICO (<10-12 years) | 14g angiocatheter through CTM; connect to jet ventilator at 15-25 psi; I:E ratio 1:4; temporizing only — barotrauma risk |
| Percutaneous cricothyrotomy (Seldinger) | Semi-elective front-of-neck access | Slower than open technique; not recommended for emergency CICO |
| Formal tracheostomy | Subglottic obstruction, tracheal transection | Requires surgical expertise; not an ED emergency procedure |
| Retrograde intubation | Relative CICO with some view | Rarely performed; wire passed retrograde through CTM, ETT threaded over wire orally |

**When NOT to perform cricothyrotomy:**
- Airway obstruction below the cricothyroid membrane (subglottic tumor, tracheal foreign body): cricothyrotomy enters above the obstruction — the tube will not bypass it; emergent tracheostomy or rigid bronchoscopy needed
- Laryngeal fracture with disrupted cricothyroid membrane: the anatomy is destroyed; direct exploration and intubation through the wound or tracheostomy is required

## Workup

**Pre-Procedure Setup (most of this should be ready before first intubation attempt):**

| Equipment | Specification |
|-----------|---------------|
| Scalpel | 10-blade or 20-blade (large, broad blade); avoid 11-blade (narrow, risk of deep penetration) |
| Bougie | 60 cm coude-tip gum elastic bougie |
| Endotracheal tube | 6.0 cuffed ETT (fits through adult CTM) or 6.0 Shiley tracheostomy tube |
| Tracheal hook | Useful for retracting tissue but not essential |
| 10 mL syringe | For cuff inflation |
| BVM and ETCO2 | For ventilation confirmation post-placement |
| Suction | Clear blood and secretions from the field |
| Gauze | 4x4 pads for hemostasis around the tube |
| Suture | 0-silk to secure tube to skin |

**Landmark Identification:**
- Palpate the thyroid notch → slide inferiorly over the thyroid cartilage → identify the soft horizontal depression (CTM) → palpate the cricoid ring inferior to it
- In obese/obscured anatomy: ultrasound-assisted identification of the CTM (if time permits and operator is experienced); otherwise, use the 4-finger palpation technique with the index finger starting at the sternal notch
- Mark the CTM with a pen or fingernail indent before first intubation attempt (anticipate CICO)

## Treatment

### Technique 1: Scalpel-Bougie-Tube (DAS 2015 — Recommended)

**Step 1: Stabilize the Larynx**
- Non-dominant hand: grasp the larynx with the thumb and middle finger on the thyroid cartilage (laryngeal handshake)
- Index finger palpates and confirms the CTM location
- Maintain this grip throughout the procedure — the larynx is mobile and will shift

**Step 2: Horizontal Stab Incision Through CTM**
- With the 10-blade scalpel in the dominant hand, make a single horizontal stab incision directly through the skin AND the cricothyroid membrane in one motion
- The scalpel enters the airway — a palpable "give" and rush of air confirms tracheal entry
- Incision length: approximately 2-3 cm horizontally
- Depth: controlled — the scalpel should penetrate the membrane but not plunge posteriorly into the esophagus; keep the blade angled cephalad (toward the head) to avoid the posterior tracheal wall

**Step 3: Maintain the Opening**
- Keep the scalpel blade in the incision and rotate it 90 degrees (blade now perpendicular) to tent the membrane open
- OR: insert a tracheal hook into the incision, hooking the inferior border of the thyroid cartilage and retracting cephalad

**Step 4: Insert the Bougie**
- Slide the coude-tip bougie through the incision into the trachea
- Direct it caudally (toward the feet) — palpable tracheal rings (click-click-click) confirm tracheal placement
- If the bougie advances >15 cm without resistance, it is in the esophagus — redirect

**Step 5: Railroad the Tube**
- Slide the 6.0 cuffed ETT over the bougie and advance into the trachea
- Rotate the tube 90 degrees counterclockwise as it enters the incision (the curve of the tube must direct the tip caudally)
- Advance until the cuff passes beyond the incision (approximately 2-3 cm past the membrane)
- Inflate the cuff with 5-10 mL air
- Remove the bougie

**Step 6: Confirm Placement**
- Attach BVM and ventilate
- Waveform capnography (ETCO2) is MANDATORY for confirmation
- Auscultate for bilateral breath sounds
- Observe chest rise

**Step 7: Secure the Tube**
- Suture the tube flange to the skin with 0-silk (2 sutures, one on each side)
- Apply tape as backup
- Place gauze around the tube to absorb blood

### Technique 2: Scalpel-Finger-Tube (Bougie Not Available)

**Step 1:** Vertical skin incision (4-5 cm) over the CTM — vertical reduces risk of vessel injury
**Step 2:** Bluntly spread subcutaneous tissue with fingers to expose the CTM
**Step 3:** Horizontal stab through the CTM with the scalpel
**Step 4:** Insert index finger through the incision into the trachea — confirm tracheal lumen by palpating tracheal rings
**Step 5:** Guide the 6.0 ETT alongside the finger into the trachea
**Step 6:** Inflate cuff, confirm with ETCO2, secure

### Needle Cricothyrotomy (Pediatric or Bridge)
- 14g angiocatheter through CTM at 45-degree caudal angle
- Aspirate air with saline-filled syringe to confirm tracheal entry
- Attach to jet ventilation: 15-25 psi, I:E ratio 1:4 (1 second inspiration, 4 seconds passive exhalation)
- Risk of barotrauma; monitor for subcutaneous emphysema
- This is a temporizing measure only — convert to surgical airway or definitive tracheostomy

### Post-Procedure
- Ventilator settings: volume control, TV 6 mL/kg IBW, PEEP 5 cmH2O, FiO2 100% initially
- CXR to confirm tube position and rule out pneumothorax, pneumomediastinum
- ENT or surgery consultation for conversion to formal tracheostomy within 24-72 hours
- Sedation and analgesia: propofol 5-50 mcg/kg/min + fentanyl 25-100 mcg/hr

## Disposition

- **Successful surgical airway:** ICU admission; ENT consultation for conversion to formal tracheostomy or decannulation plan within 24-72 hours
- **Failed surgical airway (rare — cannot ventilate through cric):** reassess placement; the tube may be pre-tracheal (false passage) — remove and re-attempt through the same incision; if anatomy is completely distorted, emergent tracheostomy by surgery
- **Post-procedure complications:** pneumothorax, pneumomediastinum, hemorrhage — manage each individually; obtain CXR immediately after placement
- **Transfer:** if ENT/surgery not available for conversion, stabilize and transfer with the cricothyrotomy tube in situ; do NOT attempt to replace with an oral ETT through an edematous/traumatized upper airway

## Pitfalls

1. **Hesitating to perform cricothyrotomy after CICO is recognized.** NAP4 data showed that delayed or failed surgical airway was the primary contributor to airway-related deaths. The cognitive barrier to cutting the neck is the most dangerous obstacle. Simulation training, premarking the CTM, and verbal CICO declaration protocols reduce hesitation.

2. **Making a vertical skin incision when using the scalpel-bougie-tube technique.** The DAS 2015 scalpel-bougie-tube method uses a horizontal stab through skin AND membrane simultaneously. A vertical skin incision is used for the scalpel-finger-tube method, where the membrane is exposed first. Mixing techniques causes confusion and delay.

3. **Creating a false passage anterior to the trachea.** The most common technical failure. The tube or bougie enters the pre-tracheal soft tissue instead of the tracheal lumen. Prevention: confirm tracheal entry with air aspiration or bougie tracheal rings. If ETCO2 is absent after insertion, the tube is pre-tracheal — remove and re-attempt through the same incision.

4. **Using a standard-size (7.0-8.0) ETT.** The cricothyroid membrane accommodates a 6.0 ETT or 6.0 Shiley tracheostomy tube. Forcing a larger tube through the membrane causes subglottic injury, creates a tight fit that impedes ventilation, and risks posterior tracheal wall perforation.

5. **Plunging the scalpel posteriorly through the trachea into the esophagus.** Controlled depth is essential. The posterior tracheal wall (membranous trachea) is thin and directly anterior to the esophagus. Angle the scalpel cephalad and control the depth of penetration. A 10-blade is safer than an 11-blade for this reason (broader blade distributes force).

6. **Not confirming placement with waveform capnography.** Blood in the airway, subcutaneous emphysema, and pre-tracheal tube placement all produce chest movement that mimics ventilation. ETCO2 is the only reliable confirmation of tracheal placement. No ETCO2 = tube is not in the trachea.

7. **Failing to premark the cricothyroid membrane before first intubation attempt.** In every anticipated or potentially difficult airway, the CTM should be palpated and marked before administering the paralytic. After multiple failed airway attempts with edema, bleeding, and positional changes, the landmarks become obscured. Marking the CTM at the outset converts a frantic search into a known target.

### Complication Management
- **Hemorrhage from anterior jugular veins or thyroid vasculature:** direct pressure with gauze packing around the tube; these are venous and respond to pressure; do NOT delay tube placement for hemostasis
- **Subcutaneous emphysema:** indicates pre-tracheal tube placement or tracheal wall injury; reassess tube position; if ventilating adequately, observe; if expanding, decompress if tension physiology develops
- **Posterior tracheal wall injury / esophageal perforation:** suspect if gastric contents appear in the tube or air leak persists despite cuff inflation; emergent surgical consultation
- **Subglottic stenosis (delayed):** occurs with prolonged cricothyrotomy tube in situ; convert to formal tracheostomy within 72 hours to reduce risk
