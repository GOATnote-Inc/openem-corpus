---
id: lateral-canthotomy
condition: Lateral Canthotomy and Cantholysis
aliases: [lateral cantholysis, orbital decompression, canthotomy for orbital compartment syndrome]
icd10: [H05.011, H05.012, H05.013, H05.019]
esi: 1
time_to_harm:
  irreversible_injury: "< 60-90 minutes (permanent vision loss)"
  death: "Not directly life-threatening"
  optimal_intervention_window: "< 60 minutes from symptom onset"
mortality_if_delayed: "Not life-threatening; primary risk is permanent monocular blindness if decompression delayed >60-90 minutes"
category: procedural
track: tier1
confusion_pairs:
  - condition: acute-angle-closure-glaucoma
    differentiators:
      - "Acute angle closure glaucoma: IOP elevated (40-80 mmHg) but orbit is soft and non-tense; no proptosis; cornea is hazy/edematous; mid-dilated fixed pupil; severe eye pain with halos; treatment is topical timolol, pilocarpine, and acetazolamide — NOT canthotomy"
      - "Orbital compartment syndrome: IOP elevated (>40 mmHg) with tense, proptotic globe; resistance to retropulsion; relative afferent pupillary defect (RAPD); vision loss; periorbital ecchymosis or swelling; treatment is lateral canthotomy"
      - "Critical rule: IOP >40 with a tense orbit and RAPD = orbital compartment syndrome requiring canthotomy; IOP >40 with a soft orbit and corneal edema = angle closure requiring medical management"
  - condition: retrobulbar-hemorrhage
    differentiators:
      - "Retrobulbar hemorrhage is the most common CAUSE of orbital compartment syndrome — they are not separate diagnoses but a cause-effect pair"
      - "Retrobulbar hemorrhage without compartment syndrome: mild proptosis, periorbital ecchymosis, intact vision, IOP normal or mildly elevated — observe with serial exams"
      - "Retrobulbar hemorrhage WITH compartment syndrome: tense orbit, IOP >40, RAPD, vision loss — immediate canthotomy"
sources:
  - type: review
    ref: "Yung CW, Moorthy RS, Lindley D, et al. Efficacy of lateral canthotomy and cantholysis in orbital hemorrhage. Ophthal Plast Reconstr Surg. 1994;10(2):137-141."
    pmid: "8086361"
  - type: review
    ref: "Lima V, Burt B, Leibovitch I, et al. Orbital compartment syndrome: the ophthalmic surgical emergency. Surv Ophthalmol. 2009;54(4):441-449."
    pmid: "19539832"
  - type: pubmed
    ref: "Rowh AD, Ufberg JW, Chan TC, et al. Lateral canthotomy and cantholysis: emergency management of orbital compartment syndrome. J Emerg Med. 2015;48(3):325-330."
    pmid: "25497896"
  - type: review
    ref: "Ballard SR, Enzenauer RW, O'Donnell T, et al. Emergency lateral canthotomy and cantholysis: a simple procedure to preserve vision from an orbital compartment syndrome. J Spec Oper Med. 2009;9(3):26-32."
    pmid: "19739473"
  - type: guideline
    ref: "American Academy of Ophthalmology. Orbital Compartment Syndrome. EyeWiki. Updated 2024."
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
# Lateral Canthotomy and Cantholysis

## Recognition

**Orbital Compartment Syndrome (OCS):**
The orbit is a closed bony compartment (open only anteriorly). Increased retrobulbar pressure compresses the optic nerve and central retinal artery, causing ischemic optic neuropathy and retinal ischemia. Permanent vision loss occurs within 60-90 minutes of sustained elevated pressure.

**Etiologies:**
- Retrobulbar hemorrhage (most common): post-trauma, post-surgical (blepharoplasty, orbital surgery), spontaneous (anticoagulation, coagulopathy)
- Orbital cellulitis with abscess
- Orbital emphysema (post-sinus fracture with nose blowing)
- Orbital edema from anaphylaxis, burns, or massive fluid resuscitation

**Clinical Diagnosis — All Five Features:**
1. **Proptosis** — globe displaced anteriorly
2. **Tense orbit** — resistance to retropulsion (firm globe that does not compress posteriorly)
3. **Elevated IOP** — >40 mmHg by tonometry (normal 10-21 mmHg)
4. **Relative afferent pupillary defect (RAPD)** — the affected pupil dilates paradoxically with the swinging flashlight test
5. **Decreased visual acuity** — ranging from blurred vision to no light perception

**Additional Findings:**
- Periorbital ecchymosis and swelling
- Restricted extraocular movements (ophthalmoplegia)
- Chemosis (conjunctival edema)
- Subconjunctival hemorrhage
- Pain with eye movement
- Elevated IOP may be the first measurable sign before vision changes

**Decision Trigger:**
IOP >40 mmHg + RAPD + tense orbit = perform lateral canthotomy immediately. Do NOT wait for ophthalmology consultation. Do NOT obtain CT imaging before the procedure if clinical findings are present.

**Uncooperative or Unconscious Patient:**
- RAPD and visual acuity cannot be assessed in sedated/intubated patients
- In the setting of facial/orbital trauma with proptosis and a tense orbit: check IOP with Tono-Pen — if >40 mmHg, perform canthotomy empirically
- CT orbit (if already obtained for trauma workup) showing proptosis with retrobulbar hemorrhage and tenting of the posterior globe (taut optic nerve) supports the diagnosis

## Critical Actions

| Action | Target |
|--------|--------|
| Recognize orbital compartment syndrome | < 5 minutes from presentation |
| Lateral canthotomy and cantholysis | < 15 minutes from recognition |
| IOP recheck | Immediately post-procedure |
| Ophthalmology consultation | After canthotomy is completed |

1. **Measure IOP** with Tono-Pen or Goldmann tonometry — >40 mmHg confirms compartment syndrome in the appropriate clinical context
2. **Perform lateral canthotomy and cantholysis** — this is the decompression procedure; do not defer to ophthalmology if they are not immediately available
3. **Recheck IOP post-procedure** — target <20 mmHg; if IOP remains elevated, the inferior cantholysis is incomplete — repeat
4. **Ophthalmology consultation** for definitive management, hematoma evacuation, and follow-up

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Acute angle-closure glaucoma | IOP elevated but orbit is soft (non-tense); no proptosis; corneal edema/haze; mid-dilated fixed pupil; nausea/vomiting; unilateral red eye; treated medically, not with canthotomy |
| Orbital cellulitis | Fever, erythema, warmth; proptosis and restricted EOMs present; IOP may be normal; CT shows preseptal/postseptal inflammation; treated with IV antibiotics; canthotomy only if concurrent compartment syndrome |
| Preseptal cellulitis | Periorbital swelling and erythema; no proptosis; normal EOMs; normal visual acuity; normal IOP |
| Cavernous sinus thrombosis | Bilateral proptosis and ophthalmoplegia; CN III, IV, V1/V2, VI palsies; septic appearance; CT/MRV demonstrates filling defect in cavernous sinus |
| Traumatic globe rupture | Irregular pupil (teardrop), decreased IOP (hypotony), positive Seidel test; do NOT perform tonometry or canthotomy — immediate ophthalmology and eye shield |
| Orbital blowout fracture without OCS | Enophthalmos (sunken globe, not proptosis); restricted upgaze from inferior rectus entrapment; normal IOP; CT shows fracture without hemorrhage |

**Bail-Out Options:**
- If canthotomy fails to reduce IOP: the inferior crus cantholysis is incomplete — re-identify and completely divide the inferior limb of the lateral canthal tendon
- If IOP remains >40 after complete cantholysis: ophthalmology must perform surgical orbital decompression (bone removal or hematoma evacuation in OR)
- Needle decompression of retrobulbar hemorrhage is NOT standard practice — risk of globe perforation and optic nerve injury is high

## Workup

**Pre-Procedure (do not delay procedure for workup if clinical diagnosis is clear):**
- **Tono-Pen IOP measurement:** >40 mmHg confirms compartment physiology
- **Visual acuity:** assess with Snellen chart, finger counting, hand motion, light perception, or no light perception — document baseline before the procedure
- **Pupillary exam:** RAPD (Marcus Gunn pupil) indicates optic nerve dysfunction
- **Extraocular movement assessment:** restricted in OCS
- **Slit lamp exam:** rule out globe rupture (Seidel test) — if positive, do NOT perform canthotomy; place eye shield and consult ophthalmology

**Equipment:**
- Tono-Pen (handheld tonometer)
- Iris scissors or small straight scissors
- Toothed forceps (Bishop-Harmon or Adson)
- Needle driver
- Hemostats (straight and curved) x2
- 1% lidocaine with epinephrine (1:100,000)
- 5 mL syringe with 27-gauge needle
- Sterile gauze, 4x4 pads
- Topical ophthalmic anesthetic: proparacaine 0.5% or tetracaine 0.5%

**Imaging (do not delay procedure):**
- CT orbit without contrast: retrobulbar hemorrhage (hyperdense material posterior to globe), proptosis, globe tenting, foreign body
- CT is useful for trauma workup and surgical planning but should NOT delay canthotomy

**Labs:**
- CBC, BMP, PT/INR, PTT — if coagulopathy is suspected as etiology
- Type and screen if surgical orbital decompression anticipated

## Treatment

### Step-by-Step: Lateral Canthotomy and Inferior Cantholysis

**1. Topical Anesthesia:**
- Instill proparacaine 0.5% drops into the affected eye (2-3 drops)
- Wait 30-60 seconds for onset

**2. Local Anesthesia:**
- Inject 1% lidocaine with epinephrine (1:100,000) into the lateral canthus
- Use a 27-gauge needle; infiltrate 1-2 mL into the skin and subcutaneous tissue at the lateral canthal angle
- The epinephrine provides hemostasis — do not omit it

**3. Identify Landmarks:**
- The lateral canthus is the junction where the upper and lower eyelids meet laterally
- The lateral canthal tendon connects the tarsal plates of both eyelids to the lateral orbital rim (Whitnall's tubercle)
- The inferior crus (inferior limb) of the lateral canthal tendon is the target for cantholysis — it is the structure compressing the inferior orbit

**4. Canthotomy (Skin Incision):**
- Place a hemostat across the lateral canthus from the canthal angle toward the lateral orbital rim, compressing for 30-60 seconds (reduces bleeding)
- Remove the hemostat
- Using iris scissors, cut the skin and orbicularis muscle horizontally from the lateral canthal angle toward the lateral orbital rim — incision length 1-2 cm
- This is the canthotomy — it opens the skin but does not decompress the orbit

**5. Inferior Cantholysis (the decompressive step):**
- With the lateral canthotomy incision open, grasp the lower eyelid with toothed forceps and retract inferiorly
- Identify the inferior crus of the lateral canthal tendon — it is a taut white band running from the inferior tarsal plate to the lateral orbital rim
- Using scissors, cut this tendon completely — strumming it with the scissors confirms the correct structure (it feels like a guitar string)
- When the inferior crus is fully divided, the lower eyelid releases and falls away from the globe
- The globe should immediately become less tense

**6. Confirm Decompression:**
- Recheck IOP with Tono-Pen — target <20 mmHg
- If IOP remains >40, the cantholysis is incomplete — re-examine the wound and divide any remaining tendon fibers
- If IOP remains elevated after complete cantholysis: consider superior cantholysis (divide the superior crus as well), though this is less commonly needed

**7. Post-Procedure Care:**
- Do not suture the canthotomy wound — it heals secondarily or is repaired by ophthalmology
- Apply erythromycin ophthalmic ointment to the wound and eye
- Ice packs to the orbit
- Elevate head of bed 30 degrees
- Serial IOP checks every 1-2 hours

### Medical Adjuncts (temporizing, not definitive)
- Timolol 0.5% ophthalmic solution 1 drop to affected eye (reduces aqueous humor production)
- Acetazolamide 500 mg IV (reduces aqueous humor production — systemic effect)
- Mannitol 1-2 g/kg IV over 30 minutes (osmotic agent — reduces orbital edema)
- These are bridges only — canthotomy is the definitive decompression

### Anticoagulation Reversal
If the patient is on anticoagulation and retrobulbar hemorrhage is expanding:
- Warfarin: 4-factor PCC (Kcentra) 25-50 units/kg IV; vitamin K 10 mg IV
- DOACs: idarucizumab 5 g IV for dabigatran; andexanet alfa or 4-factor PCC for factor Xa inhibitors
- Reversal is adjunctive — do not delay canthotomy for reversal

## Disposition

- **Post-canthotomy with IOP normalized:** Admit for observation, serial IOP checks, and ophthalmology follow-up within 12-24 hours
- **Persistent elevated IOP after cantholysis:** Emergent ophthalmology consultation for surgical orbital decompression (OR)
- **Vision loss at presentation:** Admit; prognosis depends on duration of ischemia — vision recovery is unlikely after >90 minutes of sustained IOP >40
- **Bilateral orbital compartment syndrome (rare, severe facial trauma):** Bilateral canthotomy; ICU admission; ophthalmology and trauma surgery
- **Transfer:** If ophthalmology not available, perform canthotomy before transfer; this is an EP procedure — do not defer

## Pitfalls

1. **Waiting for ophthalmology consultation before performing canthotomy.** Permanent vision loss occurs within 60-90 minutes. Ophthalmology consultation frequently takes longer. Lateral canthotomy is within the emergency physician's scope of practice and must be performed without delay.

2. **Obtaining CT before performing canthotomy when clinical diagnosis is clear.** CT confirms the etiology but does not change the immediate management. A patient with proptosis, tense orbit, IOP >40, and RAPD requires canthotomy regardless of CT findings.

3. **Performing canthotomy (skin incision) without cantholysis (tendon release).** The canthotomy alone does not decompress the orbit. The orbital compartment pressure is maintained by the lateral canthal tendon, specifically the inferior crus. Cutting only skin is insufficient. The tendon must be divided.

4. **Incomplete inferior cantholysis.** The most common reason for persistent elevated IOP after the procedure. The inferior crus must be completely divided. If IOP remains >40, re-examine the wound, identify residual tendon fibers, and divide them completely.

5. **Performing canthotomy on a ruptured globe.** Globe rupture is a contraindication. Perform a Seidel test (fluorescein streaming from the wound site) before the procedure. If the globe is ruptured, place an eye shield, administer IV antibiotics (ceftriaxone 1 g IV + fluoroquinolone), and consult ophthalmology for emergent surgical repair.

6. **Confusing orbital compartment syndrome with acute angle-closure glaucoma.** Both have elevated IOP. Angle closure has a soft orbit, corneal edema, and no proptosis. OCS has a tense orbit, proptosis, and RAPD. Treating angle closure with canthotomy is unnecessary; failing to treat OCS with canthotomy causes blindness.

7. **Omitting epinephrine from the local anesthetic.** The lateral canthal region is vascular. Without epinephrine, bleeding obscures the surgical field and makes identification of the inferior crus difficult. Use 1% lidocaine with 1:100,000 epinephrine.

### Complication Management
- **Hemorrhage from canthotomy site:** direct pressure with gauze; the hemostat crush technique before incision minimizes this; persistent bleeding usually from the lateral palpebral artery — pressure resolves it
- **Cosmetic deformity of the lateral canthus:** ophthalmology repairs this electively (lateral canthoplasty); the acute priority is vision preservation
- **Injury to the lacrimal gland or duct:** the lacrimal gland is superior and should not be in the surgical field if the incision is directed laterally; epiphora (tearing) post-procedure warrants ophthalmology follow-up
- **Globe perforation during anesthetic injection:** rare; use a 27-gauge needle and inject superficially into the skin, not deep into the orbit
