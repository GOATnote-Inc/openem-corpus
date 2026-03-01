---
id: cervical-spine-fracture
condition: Cervical Spine Fracture
aliases: [C-spine fracture, cervical vertebral fracture, neck fracture, Jefferson fracture, hangman fracture, odontoid fracture]
icd10: [S12.000A, S12.100A, S12.200A, S12.300A, S12.400A, S12.500A, S12.600A]
esi: 1
time_to_harm:
  irreversible_injury: "minutes (with cord compression)"
  death: "< 1 hour (high cervical injury)"
  optimal_intervention_window: "< 4 hours for cord decompression"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition, American College of Surgeons, 2018"
  - type: guideline
    ref: "Stiell IG et al. The Canadian C-Spine Rule for Radiography in Alert and Stable Trauma Patients. JAMA. 2001;286(15):1841-1848"
  - type: guideline
    ref: "Hoffman JR et al. Validity of a Set of Clinical Criteria to Rule Out Injury to the Cervical Spine in Patients with Blunt Trauma (NEXUS). NEJM. 2000;343(2):94-99"
  - type: guideline
    ref: "AO Spine Subaxial Cervical Spine Injury Classification (SLIC) System, 2007"
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
# Cervical Spine Fracture

## Recognition

**Mechanism:** MVC, fall from height, diving injury, axial loading, hyperflexion/hyperextension, sports injury, assault.

**Common fracture patterns:**
- **Jefferson fracture (C1):** Axial loading — burst fracture of atlas ring
- **Odontoid fracture (C2):** Type I (tip avulsion), Type II (base of dens — unstable, most common), Type III (extends into C2 body)
- **Hangman fracture (C2):** Bilateral C2 pars interarticularis fracture — hyperextension
- **Subaxial (C3-C7):** Flexion teardrop, burst fracture, facet dislocation (unilateral or bilateral), clay-shoveler (C7 spinous process avulsion)
- **Bilateral facet dislocation:** Complete ligamentous disruption — highly unstable, associated with cord injury

**Red flags for spinal cord injury:**
- Midline cervical tenderness
- Neurological deficit: weakness, numbness, paresthesias in any extremity
- Diaphragmatic breathing (C3-C5 injury — phrenic nerve)
- Priapism (spinal shock)
- Neurogenic shock: hypotension + bradycardia (loss of sympathetic tone)

**Clinical decision rules (to rule OUT imaging need in alert, stable patients):**
- **Canadian C-Spine Rule:** More sensitive (99.4%), applicable if GCS 15, stable, age > 16
  - High-risk: age ≥ 65, dangerous mechanism, paresthesias → image
  - Low-risk: simple rear-end MVC, sitting in ED, ambulatory, delayed onset neck pain, no midline tenderness → assess ROM
  - Unable to actively rotate neck 45° left and right → image
- **NEXUS:** All 5 criteria must be met to clear: no midline tenderness, no focal neuro deficit, normal alertness, no intoxication, no distracting injury

## Critical Actions

| Action | Target |
|---|---|
| Cervical immobilization | Immediate (pre-hospital) |
| CT C-spine | < 30 minutes |
| MRI C-spine | < 4 hours if neuro deficit |
| Spine surgery consult | < 1 hour if unstable fracture or neuro deficit |

1. **Maintain strict cervical spine immobilization** — rigid collar, logroll only, in-line stabilization during intubation
2. **ATLS primary survey** — airway with C-spine protection (video laryngoscopy with manual in-line stabilization preferred)
3. **CT cervical spine** — standard of care for trauma imaging (plain radiographs inadequate, miss 50%+ of fractures)
4. **Urgent MRI** if neurological deficit — evaluate cord compression, edema, ligamentous injury, epidural hematoma
5. **Treat neurogenic shock** (hypotension + bradycardia): IV crystalloid bolus 1-2 L, then norepinephrine 0.05-0.3 mcg/kg/min to MAP ≥ 85 mmHg. Avoid phenylephrine (reflex bradycardia worsens)
6. **Methylprednisolone** — NOT routinely recommended (NASCIS III controversial; AO Spine/Congress of Neurological Surgeons guidelines recommend against). Consider on case-by-case basis within 8 hours of injury only after neurosurgical consultation.

## Differential Diagnosis

- Cervical strain/sprain (no fracture on CT, ligaments intact on MRI)
- Cervical disc herniation without fracture
- Central cord syndrome (disproportionate upper > lower extremity weakness, often in older patient with spondylosis + hyperextension)
- Spinal epidural hematoma (MRI diagnosis)
- Vertebral artery dissection (fracture through transverse foramen)
- Ankylosing spondylitis fracture (low-energy mechanism in stiff spine — unstable, high cord injury risk)
- DISH (diffuse idiopathic skeletal hyperostosis) — fractures like ankylosing spondylitis

## Workup

- **CT cervical spine** (C1 through T1) — multiplanar reformats, sagittal and coronal reconstructions
- **MRI C-spine** — indicated for neurological deficit, obtunded patient, suspected ligamentous injury, suspected cord injury
- **CTA neck** — if fracture involves transverse foramen (vertebral artery injury in 25-46%)
- **CT head** — concurrent TBI screening
- **Labs:** CBC, BMP, coagulation studies, type and screen, lactate
- **ASIA exam** — American Spinal Injury Association Impairment Scale: document motor and sensory level at presentation

## Treatment

**Immobilization:**
- Rigid cervical collar for stable fractures pending definitive management
- Halo vest for select C1/C2 fractures (stable Jefferson, Type II odontoid in elderly)
- Gardner-Wells tongs/halo traction for facet dislocations (closed reduction under fluoroscopy by spine surgery)

**Hemodynamic targets:**
- MAP ≥ 85 mmHg for 5-7 days with spinal cord injury (AO Spine guideline)
- Norepinephrine 0.05-0.3 mcg/kg/min IV first-line vasopressor
- Atropine 0.5-1 mg IV for symptomatic bradycardia (HR < 50 with hypotension)
- Avoid hypothermia — actively warm

**DVT prophylaxis (high risk with SCI):**
- Enoxaparin 30 mg SQ q12h starting 24-72 hours post-injury (after hemostasis confirmed)
- Pneumatic compression devices immediately

**Respiratory support:**
- C3-C5 injury: anticipate respiratory failure (phrenic nerve); early intubation
- Incentive spirometry, aggressive pulmonary toilet for lower cervical injuries

**Surgical indications:**
- Incomplete cord injury with persistent compression — emergent decompression (< 24 hours, ideally < 12 hours per STASCIS data)
- Bilateral facet dislocation with cord injury — emergent closed reduction → surgical stabilization
- Unstable fracture patterns (SLIC score ≥ 5): operative fixation
- Progressive neurological deterioration

## Disposition

- **ICU:** All patients with spinal cord injury, neurogenic shock, or respiratory compromise
- **Admit:** All unstable fractures, neurological deficits, obtunded patients
- **Spine surgery consult:** All fractures — timing depends on stability and neuro status
- **Transfer:** Level I trauma center with spine surgery if not available
- **Potential discharge (rare):** Isolated stable fracture (e.g., clay-shoveler C7 spinous process) with reliable follow-up, no neuro deficit, rigid collar, and spine surgery follow-up in 1-2 weeks

## Pitfalls

1. **Relying on plain radiographs to clear the C-spine.** Plain films miss > 50% of cervical fractures. CT is standard of care for trauma imaging.

2. **Missing odontoid Type II fracture in elderly patients after a ground-level fall.** Low-energy mechanism does not exclude unstable fracture, especially in osteoporotic patients. CT through C2 is mandatory.

3. **Failing to image the entire C-spine including C7-T1 junction.** The cervicothoracic junction is the most commonly missed region. CT must include T1 vertebral body.

4. **Attributing hypotension to hemorrhagic shock in a patient with cervical cord injury.** Neurogenic shock (hypotension + bradycardia) requires vasopressors, not just volume. Hemorrhagic shock has tachycardia; neurogenic shock has bradycardia. Both can coexist — treat hemorrhage first.

5. **Missing vertebral artery injury.** Fractures extending through the transverse foramen carry 25-46% risk of vertebral artery injury. CTA is required. Delayed stroke may occur.

6. **Clearing C-spine in intoxicated or obtunded patients clinically.** NEXUS and Canadian C-Spine Rule require alert, cooperative patients. Obtunded patients need CT; if negative but high clinical suspicion, MRI before collar removal.

7. **Failing to recognize ankylosing spondylitis or DISH as high-risk.** These patients fracture with minimal mechanism and fractures are inherently unstable (entire fused segment acts as long bone). Maintain full immobilization regardless of how minor the mechanism appears.
