---
id: intraosseous-access
condition: Intraosseous Access
aliases: [IO access, IO line, intraosseous infusion, EZ-IO, IO needle]
icd10: [Z53.09, T80.219A]
esi: 1
time_to_harm:
  irreversible_injury: "< 10 minutes (delayed medication/fluid delivery in arrest)"
  death: "< 15 minutes without vascular access in arrest"
  optimal_intervention_window: "< 60 seconds from decision to IO placement"
category: procedural
track: tier1
sources:
  - type: guideline
    ref: "Panchal AR, Bartos JA, Cabanas JG, et al. Part 3: Adult Basic and Advanced Life Support: 2020 AHA Guidelines for CPR and ECC. Circulation. 2020;142(16_suppl_2):S366-S468."
    pmid: "33081529"
  - type: review
    ref: "Petitpas F, Guenezan J, Vendeuvre T, et al. Use of intra-osseous access in adults: a systematic review. Crit Care. 2016;20:102."
    pmid: "27075364"
  - type: pubmed
    ref: "Leidel BA, Kirchhoff C, Bogner V, et al. Comparison of intraosseous versus central venous vascular access in adults under resuscitation in the emergency department with inaccessible peripheral veins. Resuscitation. 2012;83(1):40-45."
    pmid: "21893385"
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition. American College of Surgeons. 2018."
  - type: review
    ref: "Anson JA. Vascular access in resuscitation: is there a role for the intraosseous route? Anesthesiology. 2014;120(4):1015-1031."
    pmid: "24694847"
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
# Intraosseous Access

## Recognition

**Indications:**
- Cardiac arrest when IV access not immediately available (AHA: IO is acceptable alternative to IV for drug delivery in arrest)
- Failed peripheral IV access after 2 attempts or 90 seconds in critically ill patients
- Pediatric resuscitation: IO is first-line vascular access in children when rapid IV access fails
- Hypovolemic shock, septic shock, or anaphylaxis requiring emergent vascular access
- Burns with >30% TBSA (peripheral access impossible due to skin involvement)
- Status epilepticus requiring emergent benzodiazepine/antiepileptic delivery

**Contraindications:**
- Fracture in the target bone (extravasation of fluids into soft tissue)
- Previous IO attempt in the same bone within 24-48 hours (risk of extravasation through prior cortical defect)
- Overlying cellulitis or infection at insertion site
- Prosthetic joint or hardware at the target site
- Osteopetrosis or osteogenesis imperfecta (bone too dense or too fragile)
- Known vascular insufficiency of the target extremity (relative)

**Key Principle:** IO access is a bridge — convert to standard IV or central venous access within 24 hours. IO lines should not remain in place > 24 hours (increased infection and osteomyelitis risk).

## Critical Actions

| Action | Target |
|--------|--------|
| Decision to IO placement | After 2 failed PIV attempts or 90 seconds |
| Needle through cortex | < 10 seconds with powered device |
| Aspiration of marrow | Immediate post-insertion confirmation |
| Fluid/medication delivery | < 60 seconds from IO placement |

1. **Select insertion site** — proximal tibia (default), proximal humerus (best flow rates in adults), distal tibia, distal femur (pediatric)
2. **Select needle size** — based on patient weight and device
3. **Insert IO needle** through cortex into medullary space
4. **Confirm placement** — aspiration of bone marrow, flush without extravasation
5. **Administer medications/fluids** — all ACLS medications can be given IO at same dose as IV
6. **Flush with 10 mL NS** before each medication — IO medications require a flush to enter central circulation

## Differential Diagnosis

**Alternative Vascular Access:**

| Alternative | When to Prefer |
|-------------|---------------|
| Peripheral IV (ultrasound-guided) | First-line; attempt before IO unless arrest/peri-arrest |
| Central venous catheter | Longer-term access; vasopressor infusion; CVP monitoring |
| Venous cutdown | When all percutaneous access fails and IO contraindicated |
| Umbilical vein catheter | Neonatal resuscitation (first 1-2 weeks of life) |

## Workup

**Pre-Procedure Assessment:**
- Identify insertion site free of fracture, infection, and prior IO attempts
- Palpate landmarks
- Assess for contraindications (prior surgery, prosthetics)

**Site Selection and Landmarks:**

| Site | Landmark | Advantages |
|------|----------|-----------|
| Proximal tibia | 1-2 cm below tibial tuberosity, medial flat surface | Easiest landmarks; most commonly taught; 94% first-attempt success |
| Proximal humerus | Greater tubercle; arm adducted and internally rotated (hand on umbilicus) | Highest flow rates (5 L/hr under pressure); faster drug delivery to central circulation |
| Distal tibia | 1-2 cm above medial malleolus, midline on flat tibial surface | Alternative when proximal tibia unavailable |
| Distal femur (pediatric) | 1-2 cm above lateral femoral condyle, midline anterior surface | Young children with immature proximal tibia |
| Sternum (adults only) | Mid-sternum; requires specialized device (FAST1) | Accessible during CPR; high flow rates |

**Equipment:**

| Item | Specification |
|------|---------------|
| EZ-IO driver | Battery-powered drill (Teleflex Arrow EZ-IO) |
| Needle set | Pink (15 mm, 3-39 kg pediatric), Blue (25 mm, adult ≥40 kg), Yellow (45 mm, excess tissue/large adult) |
| Manual IO needle | Cook or Jamshidi needle (backup if powered device unavailable) |
| 10 mL syringe | For marrow aspiration and flush |
| Saline flush | 10 mL NS for each flush |
| Pressure bag | For fluid infusion (gravity alone is slow through IO) |
| Lidocaine 2% | 20-40 mg (1-2 mL) IO for conscious patients — marrow infusion is painful |
| Extension tubing | Connect IO hub to IV tubing |

## Treatment

### Proximal Tibia — EZ-IO (Standard Technique)

**Step 1: Position**
- Patient supine, knee slightly flexed (towel roll behind knee)
- Expose the leg fully; palpate tibial tuberosity

**Step 2: Identify Insertion Site**
- Palpate tibial tuberosity (bony prominence below the patella)
- Move 1-2 cm medial and 1-2 cm inferior — onto the flat anteromedial tibial surface
- The site should feel flat and smooth (no ridges or tenderness suggesting fracture)

**Step 3: Insert IO Needle**
- Stabilize the leg (do NOT place your hand behind the leg — risk of through-and-through puncture)
- Hold EZ-IO driver perpendicular to the bone surface (90 degrees)
- Apply gentle downward pressure and activate the drill
- Advance until a "give" or "pop" is felt as the needle penetrates the cortex and enters the medullary space
- The black line on the needle should be visible above the skin surface (if not, needle may be too short)

**Step 4: Confirm Placement**
- Remove the trocar (inner stylet)
- Attach 10 mL syringe and aspirate — bone marrow (dark blood-tinged fluid) confirms placement
- Note: aspiration fails in ~30% of correctly placed IOs (marrow packed with fat/debris) — absence of aspirate does NOT rule out correct placement
- Flush with 10 mL NS: flush should flow freely without subcutaneous swelling (extravasation)
- If extravasation occurs: remove needle, do NOT reattempt in same bone; move to contralateral tibia or different site

**Step 5: Administer Medications/Fluids**
- **Conscious patients:** inject lidocaine 2% preservative-free, 20-40 mg (1-2 mL) IO slowly over 60 seconds before flush — marrow space infusion causes significant pain
- Flush 10 mL NS bolus before and after each medication
- Fluids: attach pressure bag (300 mmHg) for rapid infusion — gravity alone delivers only 10-15 mL/min; pressure infusion achieves 80-125 mL/min (tibial) or up to 5 L/hr (humeral)
- All ACLS medications at standard IV doses: epinephrine 1 mg, amiodarone 300 mg, etc.

**Step 6: Secure**
- Apply EZ-Stabilizer (adhesive stabilization device) or tape
- Connect extension tubing to IO hub

### Proximal Humerus — EZ-IO

**Step 1:** Adduct and internally rotate arm (hand on abdomen)
**Step 2:** Palpate greater tubercle — most prominent lateral bony point with arm in this position; insertion site is on the most prominent part of the tubercle
**Step 3:** Use 45 mm (yellow) needle in obese patients, 25 mm (blue) in average adults
**Step 4:** Insert at 90 degrees to skin, drill through cortex
**Step 5:** Confirm, flush, secure — same as tibial technique
**Key advantage:** drug delivery from humeral IO reaches central circulation in 2-3 seconds (vs 10-15 seconds from tibial)

### Manual IO Insertion (Jamshidi Needle)
- Same landmarks as EZ-IO
- Grasp handle, apply firm downward pressure with a twisting/rotating motion
- Feel cortical "pop" when entering medullary space
- Remove inner trocar, aspirate, flush, confirm
- Slower and requires more force than powered devices; 85-90% first-attempt success (vs 94% EZ-IO)

### Pediatric Considerations
- Proximal tibia is default site in all ages including neonates
- Use pink (15 mm) needle for 3-39 kg
- In infants: tibial tuberosity is less prominent — palpate the flat tibial surface 1 fingerbreadth below the tuberosity
- Avoid growth plates — insertion site should be on the tibial shaft, NOT the epiphysis
- IO flow rates are lower in infants — use pressure bag for bolus fluid delivery

### Post-Procedure
- Remove IO within 24 hours and convert to IV or central line
- Monitor insertion site for swelling, erythema, compartment syndrome
- Document: site, device, number of attempts, confirmation method

## Disposition

- **Successful IO in arrest/resuscitation:** continue resuscitation; convert to definitive IV access when feasible
- **Successful IO in critical illness:** ICU admission; plan for central or peripheral IV within 24 hours
- **Failed IO (extravasation, no flow):** attempt contralateral limb or different site; do NOT reattempt same bone
- **Compartment syndrome (rare but devastating):** high index of suspicion if leg swells after IO placement; measure compartment pressures; fasciotomy if pressures > 30 mmHg or within 30 mmHg of diastolic

## Pitfalls

1. **Delaying IO access while repeatedly attempting peripheral IVs in arrest.** In cardiac arrest, every minute without drug delivery worsens outcomes. AHA guidelines recommend IO after 2 failed PIV attempts or 90 seconds. IO should not be a "last resort" — it is a rapid, reliable first-line alternative.

2. **Inserting IO into a fractured bone.** Fluids extravasate through the fracture site into soft tissue, providing no vascular delivery and causing compartment syndrome. Always assess the target limb for signs of fracture before insertion.

3. **Not flushing before medication delivery.** Medications pool in the marrow space without reaching central circulation unless pushed with a 10 mL NS flush. Every medication must be followed by a flush. This is the most common cause of "IO medications don't work."

4. **Leaving IO in place > 24 hours.** Osteomyelitis risk increases significantly after 24 hours of IO dwell time. Convert to standard IV access as soon as the patient is stabilized. IO is a bridge, not a destination.

5. **Gravity infusion expecting rapid flow rates.** IO flow under gravity alone is only 10-15 mL/min. For volume resuscitation, a pressure bag at 300 mmHg is required to achieve clinically useful flow rates (80-125 mL/min tibial, up to 300 mL/min humeral).

6. **Failure to provide IO lidocaine in conscious patients.** Marrow space infusion is extremely painful. In conscious or semi-conscious patients, inject lidocaine 2% preservative-free 20-40 mg IO slowly before flush and infusion. Omitting this causes severe pain and potential hemodynamic response.

7. **Placing IO through a growth plate in children.** Growth plate injury can cause growth arrest. The insertion site must be on the tibial shaft distal to the physis. Ensure the needle enters the flat metaphyseal/diaphyseal bone, not the epiphyseal region.
