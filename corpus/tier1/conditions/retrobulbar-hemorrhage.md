---
id: retrobulbar-hemorrhage
condition: Retrobulbar Hemorrhage (Orbital Compartment Syndrome)
aliases: [orbital compartment syndrome, retrobulbar hematoma, OCS, orbital hemorrhage]
icd10: [H05.231, H05.232, H05.233, H05.239]
esi: 1
time_to_harm:
  irreversible_injury: "< 60-90 minutes (retinal ischemia from elevated intraorbital pressure)"
  death: "Not applicable (vision-threatening, not life-threatening)"
  optimal_intervention_window: "< 60 minutes — lateral canthotomy must be performed before permanent visual loss"
category: ophthalmologic
track: tier1
sources:
  - type: review
    ref: "Lima V et al. Orbital compartment syndrome: the ophthalmic surgical emergency. Surv Ophthalmol. 2009;54(4):441-449."
    pmid: "19539832"
  - type: pubmed
    ref: "Rowh AD, Ufberg JW, Chan TC, et al. Lateral canthotomy and cantholysis: emergency management of orbital compartment syndrome. J Emerg Med. 2015;48(3):325-330."
    pmid: "25497897"
  - type: review
    ref: "Yung CW, Moorthy RS, Lindley D, et al. Periocular infections. Emerg Med Clin North Am. 2008;26(1):57-72."
  - type: pubmed
    ref: "Vassallo S et al. Traumatic retrobulbar hemorrhage: emergent lateral canthotomy and cantholysis. J Emerg Med. 2016;50(1):141-145."
  - type: guideline
    ref: "American Academy of Ophthalmology. Orbital trauma and fractures. Preferred Practice Pattern. 2023."
last_updated: "2026-02-26"
compiled_by: agent
reviewed_by: "Brandon Dent, MD — Board Certified Emergency Medicine"
review_date: "2026-02-27"
risk_tier: A
confusion_pairs:
  - condition: acute-angle-closure-glaucoma
    differentiators:
      - "Retrobulbar hemorrhage: proptosis present; glaucoma: no proptosis"
      - "Retrobulbar hemorrhage: post-traumatic or post-surgical context"
      - "Glaucoma: mid-dilated, fixed pupil; corneal edema; shallow anterior chamber"
  - condition: orbital-cellulitis
    differentiators:
      - "Orbital cellulitis: fever, erythema, gradual onset over days"
      - "Retrobulbar hemorrhage: acute onset minutes to hours after trauma/surgery"
      - "Orbital cellulitis: CT shows soft tissue stranding; hemorrhage: high-density fluid"
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
# Retrobulbar Hemorrhage (Orbital Compartment Syndrome)

## Recognition

**Definition:** Retrobulbar hemorrhage is bleeding into the retrobulbar space that increases intraorbital pressure, compressing the optic nerve and central retinal artery. The orbit is a confined, non-expandable bony compartment — any volume expansion (blood, gas, edema) directly increases pressure on the globe, optic nerve, and vascular supply. Orbital compartment syndrome (OCS) occurs when intraorbital pressure exceeds perfusion pressure of the central retinal artery, causing retinal ischemia.

**Causes:**
- Facial/orbital trauma (most common — blunt and penetrating)
- Post-surgical (blepharoplasty, orbital surgery, sinus surgery, retrobulbar block)
- Anticoagulation (spontaneous in therapeutic anticoagulation)
- Valsalva (straining, vomiting, coughing) in predisposed patients
- Orbital fracture repair (post-operative)

**Clinical Features:**

| Feature | Notes |
|---------|-------|
| **Proptosis** | Acute, firm; globe displaced anteriorly; resistance to retropulsion |
| **Decreased visual acuity** | Progressive — from blurred vision to no light perception |
| **Afferent pupillary defect (APD)** | Marcus Gunn pupil — swinging flashlight test shows dilation of the affected pupil when light swings to it |
| **Elevated IOP** | > 40 mmHg (normal 10-21); measured by Tono-Pen or Goldmann tonometry |
| **Periorbital swelling and ecchymosis** | Tense, often with subconjunctival hemorrhage |
| **Restricted extraocular movements** | Ophthalmoplegia from increased orbital pressure on cranial nerves and extraocular muscles |
| **Pain** | Deep, aching orbital pain; worsens with eye movement |
| **Cherry-red spot on fundoscopy** | Indicates central retinal artery occlusion (late finding — do not wait for this) |

**Time-Critical Decision:**
- Retinal ischemia becomes irreversible after 60-90 minutes of elevated intraorbital pressure
- Clinical diagnosis — do NOT delay intervention for imaging
- Any patient with acute proptosis + decreased vision + APD + elevated IOP after trauma or surgery requires immediate lateral canthotomy

## Critical Actions

1. **Lateral canthotomy and inferior cantholysis immediately.** This is a bedside emergency procedure performed by the emergency physician — do not wait for ophthalmology. Decompress the orbit by releasing the lateral canthal tendon. IOP should decrease by ≥ 50% within minutes. Technique detailed in Treatment section.

2. **Measure IOP before and after canthotomy.** Tono-Pen or Goldmann: IOP > 40 mmHg confirms compartment syndrome. Post-canthotomy IOP should drop to < 20 mmHg. If IOP remains elevated after inferior cantholysis, perform superior cantholysis.

3. **Check visual acuity and pupillary response before and after the procedure.** Document with Snellen or counting fingers/light perception. APD (Marcus Gunn pupil) on swinging flashlight test indicates optic nerve compromise. Improvement in APD after canthotomy is a positive prognostic sign.

4. **Ophthalmology consultation.** Emergent for operative orbital decompression if canthotomy/cantholysis fails to adequately reduce IOP and restore vision. Ophthalmology should evaluate even after successful canthotomy for definitive management.

5. **CT orbits without contrast if etiology unclear.** Identifies retrobulbar hematoma location (intraconal vs extraconal), orbital fractures, foreign bodies. Do NOT delay canthotomy for CT in an obvious clinical presentation.

6. **Treat elevated IOP medically as adjunct.** Timolol 0.5% 1 drop topically, acetazolamide 500 mg IV, mannitol 1-2 g/kg IV over 30-45 minutes. These are temporizing measures — they do not replace surgical decompression.

7. **Reverse anticoagulation if applicable.** Vitamin K 10 mg IV, 4-factor PCC 25-50 units/kg for warfarin. Idarucizumab for dabigatran. Direct pressure and hemostasis after canthotomy.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Orbital cellulitis** | Gradual onset over days; fever; erythema and warmth; leukocytosis; CT shows soft tissue stranding without high-density hemorrhage |
| **Acute angle-closure glaucoma** | No proptosis; mid-dilated fixed pupil; corneal edema (hazy cornea); shallow anterior chamber; no trauma history |
| **Cavernous sinus thrombosis** | Bilateral involvement; multiple cranial nerve palsies (III, IV, V1, V2, VI); fever; sinusitis history |
| **Thyroid eye disease** | Gradual onset; bilateral proptosis; euthyroid or hyperthyroid; extraocular muscle enlargement on CT with tendon sparing |
| **Orbital tumor** | Gradual proptosis over weeks to months; no acute visual loss; MRI shows enhancing mass |
| **Ruptured globe** | Irregular pupil (teardrop sign); positive Seidel test (fluorescein streaming); hypotony (low IOP); penetrating mechanism; do NOT check IOP if suspected |

## Workup

**Bedside (before any imaging):**
- Visual acuity (Snellen chart, counting fingers, light perception, no light perception)
- Pupillary exam: afferent pupillary defect (swinging flashlight test)
- IOP measurement (Tono-Pen): > 40 mmHg = compartment syndrome
- Globe integrity: rule out ruptured globe before any pressure on eye (Seidel test with fluorescein)
- Extraocular movements
- Fundoscopy if time permits (do not delay canthotomy): retinal pallor, cherry-red spot, disc edema

**Imaging (after or concurrent with decompression):**
- CT orbits without contrast: retrobulbar high-density collection, globe tenting (posterior scleral flattening), proptosis measurement, fractures, foreign bodies
- CT with contrast if vascular lesion suspected (AVM, aneurysm)
- MRI orbits for subacute presentations or suspected tumor

**Labs:**
- CBC, coagulation studies (PT/INR, aPTT) — especially in anticoagulated patients
- Type and screen if significant hemorrhage or surgery anticipated

## Treatment

**Lateral Canthotomy and Cantholysis — Step-by-Step:**

1. **Equipment:** 18-gauge needle, 3-5 mL lidocaine 1% with epinephrine, hemostat or straight Kelly clamp, iris scissors or straight fine scissors, toothed forceps
2. **Anesthesia:** Inject 1-2 mL lidocaine 1% with epinephrine at the lateral canthus (lateral corner of the eye)
3. **Canthotomy:** Clamp the lateral canthus with hemostat for 1-2 minutes (hemostasis). Then cut through the full thickness of the lateral canthus with scissors — a 1-2 cm horizontal incision from the lateral canthus toward the lateral orbital rim
4. **Inferior cantholysis:** With the lower lid retracted inferiorly by forceps, identify the taut inferior crus of the lateral canthal tendon. Cut this band with scissors directed toward the orbital floor. The lower lid should become freely mobile (no longer taut against the orbital rim)
5. **Reassess:** Check IOP (should drop ≥ 50%), visual acuity, and pupillary response
6. **If IOP remains elevated:** Perform superior cantholysis (cut the superior crus similarly)
7. **Post-procedure:** Apply antibiotic ointment (erythromycin). Ice packs. Head of bed elevated 30°

**Medical IOP Reduction (adjunctive, not definitive):**
- Timolol 0.5% 1 drop topically (reduces aqueous production)
- Acetazolamide 500 mg IV (carbonic anhydrase inhibitor, reduces aqueous production)
- Mannitol 1-2 g/kg IV over 30-45 min (osmotic agent, reduces vitreous volume)
- Brimonidine 0.2% 1 drop topically

**Operative Orbital Decompression:**
- Indicated if canthotomy/cantholysis fails to reduce IOP adequately
- Performed by ophthalmology or oculoplastics in OR
- Bone removal (medial wall, orbital floor) to expand orbital volume

## Disposition

**All patients with orbital compartment syndrome require:**
- Ophthalmology evaluation (emergent if not already consulted)
- Hospital admission for serial visual acuity checks and IOP monitoring (q2-4h for 24-48 hours)
- Post-canthotomy wound care and follow-up repair (canthal reconstruction at 5-7 days if needed)

**Transfer if:**
- No ophthalmology available — perform canthotomy BEFORE transfer, not after arrival at receiving facility
- Time to definitive ophthalmologic care > 60 minutes

**Visual Prognosis:**
- Canthotomy within 60 minutes: good visual outcome in most cases
- Delayed > 2 hours: permanent visual loss likely
- Complete optic nerve ischemia > 90 minutes: irreversible blindness

## Pitfalls

1. **Waiting for ophthalmology consultation before performing lateral canthotomy.** This is an emergency physician procedure. Retinal ischemia becomes irreversible after 60-90 minutes. Ophthalmology consultation delays of 30-60 minutes are common. Every emergency physician must be able to perform lateral canthotomy and cantholysis at the bedside. The procedure is low-risk and high-yield.

2. **Performing canthotomy without cantholysis.** Canthotomy alone (cutting the skin and conjunctiva at the lateral canthus) does not adequately decompress the orbit. The lateral canthal tendon (specifically the inferior crus) must be transected (cantholysis) to release the lower lid from the orbital rim and allow orbital volume expansion. Failure to perform the cantholysis step is the most common technical error.

3. **Ordering CT before performing canthotomy in an obvious presentation.** Acute proptosis + decreased vision + APD + elevated IOP after trauma = orbital compartment syndrome. The clinical diagnosis is sufficient to proceed with canthotomy. CT takes 30-60 minutes including transport and is unnecessary before the procedure. Imaging can be obtained after decompression.

4. **Compressing the globe to check IOP in a patient with possible ruptured globe.** Before IOP measurement, rule out globe rupture: irregular pupil (teardrop sign), 360° subconjunctival hemorrhage, visible uveal tissue, flat anterior chamber. If globe rupture is suspected, do NOT measure IOP — place a rigid eye shield, give antibiotics (moxifloxacin 400 mg IV), and consult ophthalmology for operative repair.

5. **Attributing post-traumatic periorbital swelling to simple contusion without checking vision and IOP.** Retrobulbar hemorrhage develops within minutes to hours after orbital trauma. Any patient with periorbital trauma, proptosis, and visual complaints must have visual acuity and IOP checked. A "black eye" that is firm and proptotic with decreasing vision is orbital compartment syndrome.
