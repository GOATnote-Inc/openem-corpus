---
id: cavernous-sinus-thrombosis
condition: Cavernous Sinus Thrombosis
aliases: [CST, septic cavernous sinus thrombosis, cavernous sinus thrombophlebitis]
icd10: [G08, I67.6]
esi: 1
time_to_harm:
  irreversible_injury: "< 24 hours (cranial nerve palsies, visual loss from optic nerve ischemia)"
  death: "< 48-72 hours without treatment (intracranial extension, meningitis, brain abscess)"
  optimal_intervention_window: "< 6 hours from recognition — IV antibiotics and anticoagulation"
mortality_if_delayed: "Historical mortality 30-50% pre-antibiotics; current mortality 20-30% with treatment; permanent cranial nerve deficit in 50%"
category: neurological
track: tier1
sources:
  - type: review
    ref: "Bhatia K, Jones NS. Septic cavernous sinus thrombosis secondary to sinusitis: are anticoagulants indicated? A review of the literature. J Laryngol Otol. 2002;116(9):667-676."
    pmid: "12437795"
  - type: pubmed
    ref: "Ebright JR, Pace MT, Niazi AF. Septic thrombosis of the cavernous sinuses. Arch Intern Med. 2001;161(22):2671-2676."
    pmid: "11732931"
  - type: review
    ref: "Platt MP et al. Cavernous sinus thrombosis. In: Infections of the Ears, Nose, Throat, and Sinuses. 2018. Springer."
  - type: pubmed
    ref: "Southwick FS, Richardson EP Jr, Swartz MN. Septic thrombosis of the dural venous sinuses. Medicine (Baltimore). 1986;65(2):82-106."
    pmid: "3512953"
  - type: review
    ref: "Desa V, Green R. Cavernous sinus thrombosis: current therapy. J Oral Maxillofac Surg. 2012;70(9):2085-2091."
    pmid: "22326173"
last_updated: "2026-02-26"
compiled_by: agent
reviewed_by: "Brandon Dent, MD — Board Certified Emergency Medicine"
review_date: "2026-02-27"
risk_tier: A
confusion_pairs:
  - condition: acute-angle-closure-glaucoma
    differentiators:
      - "CST: bilateral proptosis and cranial nerve palsies"
      - "Glaucoma: unilateral, no cranial nerve involvement, corneal edema"
      - "CST: fever and sinusitis history typical"
  - condition: orbital-cellulitis
    differentiators:
      - "Orbital cellulitis: unilateral; CST frequently progresses to bilateral"
      - "CST: cranial nerve III, IV, V1, V2, VI palsies; orbital cellulitis typically only CN VI"
      - "CST: bilateral cavernous sinus involvement on MRI/MRV"
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
# Cavernous Sinus Thrombosis

## Recognition

**Definition:** Cavernous sinus thrombosis (CST) is a septic or aseptic thrombosis of the cavernous sinuses — paired dural venous sinuses lateral to the sella turcica through which cranial nerves III, IV, V1, V2, and VI traverse alongside the internal carotid artery. Septic CST is most commonly caused by contiguous spread of infection from the paranasal sinuses, orbit, face, or teeth via valveless facial and ophthalmic veins.

**Anatomy — Why It Matters:**
- The cavernous sinuses communicate across midline via intercavernous sinuses → unilateral infection progresses to bilateral involvement in 36 hours on average
- Valveless facial veins (angular, ophthalmic) provide direct retrograde spread from the dangerous triangle of the face (nasolabial folds, nose, upper lip)
- CN III (oculomotor), CN IV (trochlear), CN V1 (ophthalmic trigeminal), CN V2 (maxillary trigeminal), CN VI (abducens) all traverse or border the cavernous sinus

**Clinical Features:**

| Feature | Notes |
|---------|-------|
| **Headache** | Severe, retro-orbital or frontal; progressive over hours to days |
| **Periorbital edema and proptosis** | Initially unilateral, progresses to bilateral in 24-48 hours (pathognomonic) |
| **Chemosis** | Conjunctival edema from impaired venous drainage |
| **Cranial nerve palsies** | CN VI first (abducens — most medial position); then CN III, IV; lateral gaze palsy → complete ophthalmoplegia |
| **Fever** | Present in > 90% of septic CST |
| **Visual loss** | Optic nerve ischemia from compression or thrombosis of ophthalmic veins |
| **Papilledema** | Raised intracranial pressure from impaired venous drainage |
| **Facial sensory changes** | V1/V2 distribution numbness (forehead, cheek) |
| **Altered mental status** | Meningeal extension, intracranial hypertension, or sepsis |

**Primary Sources of Infection:**
- Sinusitis (sphenoid most common — shares wall with cavernous sinus; also ethmoid, frontal)
- Orbital/periorbital cellulitis
- Dental abscess (maxillary teeth)
- Facial skin infections (furuncle, abscess in dangerous triangle)
- Otitis media/mastoiditis (less common route)

**Microbiology:**
- Staphylococcus aureus (60-70%, including MRSA)
- Streptococcus species (20%)
- Gram-negative rods (Proteus, E. coli — from dental/sinus source)
- Anaerobes (polymicrobial in dental/sinus origin)
- Fungi (Aspergillus, Mucor) — immunocompromised patients, diabetics

## Critical Actions

1. **IV antibiotics within 1 hour.** Vancomycin 25-30 mg/kg IV loading dose (MRSA coverage) + ceftriaxone 2 g IV q12h (gram-negatives, streptococci) + metronidazole 500 mg IV q8h (anaerobes). If fungal etiology suspected (diabetic, immunocompromised): add amphotericin B liposomal 5 mg/kg IV daily.

2. **MRI brain with MR venography (MRV) and gadolinium is the imaging modality of choice.** Demonstrates thrombus in cavernous sinus (filling defect on contrast-enhanced MRV), cavernous sinus expansion, and associated orbital/sinus pathology. CT venography is alternative if MRI unavailable. Non-contrast CT may show cavernous sinus enlargement but lacks sensitivity for early disease.

3. **Anticoagulation with heparin.** Unfractionated heparin IV — bolus 80 units/kg, then infusion 18 units/kg/hr, target aPTT 1.5-2.5x normal. Anticoagulation prevents thrombus propagation and improves venous drainage. Evidence is observational but consistently shows mortality benefit (mortality 30% with anticoagulation vs 50% without). Continue for 3-6 months with transition to warfarin.

4. **ENT and ophthalmology consultation immediately.** ENT for surgical drainage of primary sinus infection source. Ophthalmology for visual acuity monitoring, IOP measurement, and fundoscopic exam.

5. **Blood cultures x2 before antibiotics** (do not delay antibiotics for cultures). Culture any drainable primary source (sinus aspirate, abscess).

6. **Surgical source control.** Sphenoid sinusotomy or endoscopic sinus surgery for sinusitis-associated CST. I&D of orbital or facial abscess. Dental extraction for odontogenic source. Source control is essential — antibiotics alone are insufficient.

7. **Monitor ICP and visual acuity serially.** Deteriorating vision or worsening mental status may indicate need for emergent surgical decompression or thrombus removal.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Orbital cellulitis** | Usually unilateral; no contralateral progression; CN VI palsy may be present but no multiple cranial nerve involvement; responds to antibiotics without anticoagulation |
| **Orbital apex syndrome** | Overlapping CN involvement (II, III, IV, V1, VI); may be infectious, inflammatory, or neoplastic; MRI differentiates |
| **Mucormycosis (rhinocerebral)** | Black necrotic eschar on palate/turbinates; diabetic ketoacidosis or immunosuppression; rapidly progressive with tissue invasion |
| **Tolosa-Hunt syndrome** | Idiopathic granulomatous inflammation of cavernous sinus; painful ophthalmoplegia; no fever; MRI shows cavernous sinus enhancement; responds dramatically to corticosteroids |
| **Carotid-cavernous fistula** | Pulsatile proptosis, orbital bruit; no fever; post-traumatic or spontaneous; arterialized conjunctival vessels |
| **Superior sagittal sinus thrombosis** | Headache and papilledema dominate; seizures common; no cranial nerve palsies; MRV shows sagittal sinus filling defect |
| **Pituitary apoplexy** | Sudden headache, visual field deficit (bitemporal hemianopia), CN III palsy; MRI shows hemorrhage into pituitary adenoma; no fever |
| **Thyroid eye disease** | Bilateral proptosis; no fever; euthyroid or hyperthyroid; extraocular muscle enlargement on imaging with tendon sparing |

## Workup

**Imaging:**
- MRI brain + orbits with gadolinium and MR venography (gold standard): filling defect in cavernous sinus, expansion of sinus, orbital fat stranding, abnormal convexity of cavernous sinus wall
- CT sinus (to identify primary sinus infection source)
- CT venography if MRI not available (less sensitive for early CST)
- CT head without contrast as initial screen (exclude abscess, hemorrhage)

**Laboratory:**
- CBC with differential (leukocytosis with left shift)
- Blood cultures x2
- CRP, ESR (markedly elevated)
- BMP, LFTs
- Coagulation studies (PT/INR, aPTT — baseline before anticoagulation)
- Procalcitonin (distinguish bacterial from aseptic causes)
- D-dimer (elevated, but non-specific)

**Ophthalmologic Assessment:**
- Visual acuity (serial — q4-6h during acute phase)
- Pupillary exam (afferent pupillary defect indicates optic nerve compromise)
- IOP measurement (elevated from impaired venous drainage)
- Fundoscopy (papilledema, retinal venous engorgement)
- Extraocular movements (document cranial nerve deficits)

**Lumbar Puncture:**
- If meningitis suspected (altered mental status, nuchal rigidity)
- Send CSF for cell count, protein, glucose, culture, gram stain
- LP may show elevated opening pressure, pleocytosis, elevated protein

## Treatment

**Antibiotics (minimum 3-6 weeks IV, then oral transition):**
- Vancomycin 25-30 mg/kg IV loading dose, then 15-20 mg/kg IV q8-12h (target trough 15-20 mcg/mL)
- Ceftriaxone 2 g IV q12h
- Metronidazole 500 mg IV q8h
- Duration: 3-4 weeks IV minimum; total 6-8 weeks for septic CST
- If MSSA confirmed: switch vancomycin to nafcillin 2 g IV q4h
- If fungal: amphotericin B liposomal 5 mg/kg IV daily + surgical debridement

**Anticoagulation:**
- Unfractionated heparin IV: bolus 80 units/kg, infusion 18 units/kg/hr
- Target aPTT 1.5-2.5x normal (typically 60-80 seconds)
- Transition to warfarin (INR 2-3) or LMWH after acute phase
- Total anticoagulation duration: 3-6 months
- Contraindication to anticoagulation: active intracranial hemorrhage or mycotic aneurysm — obtain imaging before starting

**Surgical Source Control:**
- Endoscopic sphenoidotomy for sphenoid sinusitis
- External or endoscopic ethmoidectomy/frontal sinusotomy as indicated
- Orbital abscess drainage (subperiosteal or intraorbital)
- Dental extraction for odontogenic source
- Timing: within 24-48 hours of diagnosis

**Supportive:**
- Dexamethasone 10 mg IV q6h for 3-5 days if significant orbital edema with vision threat (controversial — may mask clinical progression; use with concurrent antibiotics only)
- ICP management if elevated: HOB 30°, osmotic therapy (mannitol 1 g/kg IV or hypertonic saline)
- Pain management: acetaminophen 1 g IV q6h; avoid NSAIDs if on anticoagulation

## Disposition

**All CST patients require ICU admission** for:
- Serial neurological and visual acuity monitoring (q4-6h)
- IV anticoagulation titration
- IV antibiotics (prolonged course)
- Surgical source control coordination

**Neurosurgery consultation** if:
- Intracranial extension (brain abscess, meningitis, subdural empyema)
- Consideration for direct thrombus intervention (rare)

**Transfer if:**
- No ICU, ENT, ophthalmology, or neurosurgery availability
- Stabilize with antibiotics and heparin before transport

**Prognosis:**
- Mortality: 20-30% with treatment (historically 80-100% before antibiotics)
- CN palsy resolution: 20-40% have residual cranial nerve deficits
- Visual prognosis: 10-15% permanent visual impairment

## Pitfalls

1. **Treating orbital cellulitis without considering progression to CST.** Orbital cellulitis (post-septal infection) is the most common precursor of CST. Bilateral proptosis, multiple cranial nerve palsies, or failure to improve on IV antibiotics at 24-48 hours mandates MRI with MRV to evaluate for CST. Unilateral orbital cellulitis that develops contralateral symptoms is CST until proven otherwise.

2. **Withholding anticoagulation due to concern for hemorrhagic conversion.** The historical fear of worsening hemorrhage with anticoagulation in septic CST is not supported by evidence. Observational data consistently show reduced mortality with heparin anticoagulation (30% vs 50%). The benefit of preventing thrombus propagation outweighs hemorrhagic risk. Obtain baseline imaging to exclude existing hemorrhage, then anticoagulate.

3. **Relying on CT alone to exclude CST.** Non-contrast CT has poor sensitivity for early CST. CT venography is better but still inferior to MRI/MRV. A normal CT does not exclude CST. If clinical suspicion is present (orbital symptoms + sinusitis + fever + cranial nerve palsies), obtain MRI with MRV even if CT is unremarkable.

4. **Missing the sphenoid sinus as the source.** Sphenoid sinusitis is the most dangerous sinus infection due to direct anatomic proximity to the cavernous sinus, but it is also the most easily missed — it does not cause facial tenderness or nasal congestion. Sphenoid sinusitis presents with vertex or occipital headache. Dedicated CT sinus with coronal reconstruction is required to evaluate the sphenoid.

5. **Failing to inspect the dangerous triangle of the face.** The nasolabial folds, nose, and upper lip drain via the angular and ophthalmic veins directly to the cavernous sinus without valves. A seemingly minor facial furuncle in this distribution can seed CST. Any facial infection in this region with periorbital symptoms warrants aggressive evaluation.

6. **Diagnosing preseptal cellulitis and discharging without imaging when post-septal extension or CST is possible.** Preseptal cellulitis (periorbital cellulitis) is anterior to the orbital septum and is managed with oral antibiotics. However, preseptal infection can extend post-septally and seed the cavernous sinus. Any preseptal cellulitis with proptosis, ophthalmoplegia, pain with eye movement, visual acuity changes, or fever requires CT with contrast and consideration of MRI/MRV. Discharging these patients on oral antibiotics without imaging risks missing early CST when anticoagulation and IV antibiotics can prevent cranial nerve destruction.

7. **Missing contralateral eye involvement that signals bilateral CST.** The intercavernous sinuses connect the left and right cavernous sinuses across the midline. Unilateral CST progresses to bilateral involvement in an average of 24–36 hours. Subtle contralateral findings — mild chemosis, early CN VI palsy (difficulty with lateral gaze), or slight proptosis on the opposite side — indicate bilateral CST and dramatically worsen prognosis. Every patient with unilateral CST requires serial examination of the contralateral eye at minimum q4–6 hours to detect progression.
