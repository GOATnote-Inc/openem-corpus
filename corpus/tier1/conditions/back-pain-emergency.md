---
id: back-pain-emergency
condition: "Back Pain — Emergency Evaluation"
aliases: [back pain, low back pain, thoracic back pain, spine pain, acute back pain ED]
icd10: [M54.9, M54.5, M54.6, R29.3]
esi: 3
time_to_harm:
  irreversible_injury: "< 24 hours (cauda equina with bladder dysfunction)"
  death: "< 2 hours (ruptured AAA, aortic dissection, epidural abscess with sepsis)"
  optimal_intervention_window: "< 48 hours (cauda equina surgical decompression)"
category: presentations
condition_type: presentation
chief_complaint: "Back Pain"
differential_categories:
  - category: life-threatening
    conditions:
      - ruptured-aaa
      - aortic-dissection
      - spinal-epidural-abscess
      - cauda-equina-syndrome
      - spinal-cord-compression
      - spinal-cord-injury
  - category: emergent
    conditions:
      - pyelonephritis
      - acute-pancreatitis
      - cervical-spine-fracture
  - category: urgent
    conditions:
      - urolithiasis
      - acute-low-back-pain-red-flags
  - category: non-emergent
    conditions:
      - acute-muscle-strain
red_flags:
  - "Saddle anesthesia (cauda equina syndrome)"
  - "New urinary retention or incontinence"
  - "Bilateral leg weakness or progressive neurological deficit"
  - "Pulsatile abdominal mass with back pain (AAA)"
  - "IV drug use with fever and back pain (epidural abscess)"
  - "Known malignancy with new back pain (cord compression)"
  - "Trauma with midline tenderness"
  - "Age > 50 with new onset back pain"
  - "Fever with back pain"
  - "Pain at rest or nocturnal pain awakening from sleep"
  - "Anticoagulation with back pain and neurological symptoms (epidural hematoma)"
  - "Recent spinal procedure with new symptoms"
decision_rules:
  - name: "Canadian C-Spine Rule"
    citation: "Stiell IG et al. The Canadian C-Spine Rule for radiography in alert and stable trauma patients. JAMA. 2001;286(15):1841-1848."
    pmid: "11597285"
  - name: "NEXUS Criteria"
    citation: "Hoffman JR et al. Validity of a set of clinical criteria to rule out injury to the cervical spine in patients with blunt trauma. N Engl J Med. 2000;343(2):94-99."
    pmid: "10891516"
track: tier1
sources:
  - type: guideline
    ref: "ACEP Clinical Policy: Critical Issues in the Evaluation and Management of Emergency Department Patients With Acute Low Back Pain. Ann Emerg Med. 2022."
  - type: guideline
    ref: "ACP Clinical Practice Guideline: Noninvasive Treatments for Acute, Subacute, and Chronic Low Back Pain. Ann Intern Med. 2017;166(7):514-530."
    pmid: "28192789"
  - type: review
    ref: "Della-Giustina DA. Emergency department evaluation and treatment of back pain. Emerg Med Clin North Am. 2015;33(2):311-326."
    pmid: "25892725"
  - type: pubmed
    ref: "Stiell IG et al. The Canadian C-Spine Rule for radiography in alert and stable trauma patients. JAMA. 2001;286(15):1841-1848."
    pmid: "11597285"
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
# Back Pain — Emergency Evaluation

## Recognition

Back pain accounts for 2-4% of ED visits. The vast majority (> 95%) is mechanical/musculoskeletal and self-limited. The ED task is to identify the 1-5% with life-threatening or emergent causes requiring immediate intervention — primarily vascular catastrophe, cord compression, and spinal infection.

**Critical distinction:** The ED evaluation of back pain is a red-flag screening exercise, not a comprehensive back pain workup. If no red flags are present, the patient has mechanical back pain and imaging/labs are not indicated.

**Red flag categories (must screen for ALL):**

1. **Vascular:** AAA rupture, aortic dissection
2. **Infection:** Spinal epidural abscess, discitis/osteomyelitis, pyelonephritis
3. **Neurological compromise:** Cauda equina syndrome, cord compression, progressive motor deficit
4. **Malignancy:** Spinal metastases with cord compression
5. **Trauma:** Vertebral fracture (including osteoporotic)
6. **Visceral referral:** Pancreatitis, renal colic, perforated viscus, retroperitoneal hemorrhage

**Key history elements:**
- Age: > 50 with new onset → consider malignancy, AAA, vertebral fracture
- Onset and mechanism: trauma (fracture), insidious (infection, malignancy), sudden (vascular)
- Location: midline (vertebral body, disc, cord) vs paraspinal (muscular) vs flank (renal)
- Neurological symptoms: weakness, numbness, bowel/bladder dysfunction (cauda equina)
- Constitutional symptoms: fever, weight loss, night sweats (infection, malignancy)
- Risk factors: IVDU (epidural abscess), immunosuppression, cancer history, osteoporosis, anticoagulation
- Nocturnal/rest pain: suggests malignancy or infection (not positional/mechanical)

## Critical Actions

| Action | Target |
|---|---|
| Screen for red flags | < 10 minutes |
| Vascular assessment if AAA suspected | < 15 minutes (bedside US) |
| Neurological exam (strength, sensation, rectal tone) | < 15 minutes |
| MRI for suspected cauda equina/cord compression | < 4 hours |
| Empiric antibiotics for suspected epidural abscess with sepsis | < 60 minutes |

**Evaluation algorithm:**

1. **Screen for vascular emergency.** Age > 50 + sudden back/flank/abdominal pain + risk factors (AAA history, hypertension, smoking, connective tissue disorder):
   - Bedside aortic ultrasound: aortic diameter > 3 cm is aneurysmal, > 5 cm is at high rupture risk
   - Hemodynamically unstable with pulsatile mass → vascular surgery consultation and OR, NOT CT
   - If stable, CTA abdomen/pelvis for AAA or dissection

2. **Screen for neurological emergency.** Ask directly about:
   - Saddle anesthesia (perineal numbness — cauda equina)
   - Urinary retention or new incontinence (cauda equina — post-void residual > 200 mL is concerning)
   - Fecal incontinence or decreased rectal tone
   - Bilateral leg weakness or progressive unilateral motor deficit
   - If ANY neurological red flag → emergent MRI spine + neurosurgical/spine surgery consultation

3. **Screen for spinal infection.** IVDU + fever + back pain = epidural abscess until proven otherwise. Also consider in immunosuppressed, recent spinal procedure, distant infection source (bacteremia). Triad: fever + back pain + neurological deficit (classic but late — only 10-15% present with all three).

4. **Focused neurological exam:**
   - Motor: hip flexion (L2), knee extension (L3), ankle dorsiflexion (L4), great toe dorsiflexion (L5), ankle plantarflexion (S1)
   - Sensory: dermatomes L2-S2, saddle area (S2-S5)
   - Reflexes: patellar (L4), Achilles (S1)
   - Rectal tone and voluntary squeeze (S2-S4)
   - Straight leg raise (L4-S1 radiculopathy): positive if radiating pain below knee at < 60 degrees. Crossed SLR (contralateral pain) is highly specific for disc herniation.
   - Post-void residual (bladder scan) if urinary symptoms

5. **If no red flags identified:** Diagnose as mechanical back pain. No imaging needed. Treat symptomatically and discharge.

## Differential Diagnosis

### Life-Threatening
- **Ruptured AAA** (`ruptured-aaa`): age > 60, sudden onset back/abdominal/flank pain, hypotension, pulsatile mass. Often misdiagnosed as renal colic. Classic triad (pain, hypotension, pulsatile mass) present in < 50%.
- **Aortic dissection** (`aortic-dissection`): tearing interscapular pain, hypertension, pulse deficits. Stanford B dissection presents primarily as back pain.
- **Spinal epidural abscess** (`spinal-epidural-abscess`): IVDU, immunosuppressed, or recent spinal procedure + fever + back pain → progressive neurological deficit. MRI with gadolinium is diagnostic. 4-phase progression: back pain → radiculopathy → motor deficit → paralysis. Time from onset to paralysis can be hours.
- **Cauda equina syndrome** (`cauda-equina-syndrome`): saddle anesthesia, urinary retention (most sensitive early finding), bilateral sciatica, decreased rectal tone. Surgical decompression within 48 hours of onset of urinary symptoms for best outcomes.
- **Spinal cord compression** (`spinal-cord-compression`): known malignancy + new back pain + neurological deficit. MRI entire spine (skip lesions in 10%). Dexamethasone 10 mg IV loading dose + emergent radiation oncology/neurosurgery.
- **Spinal cord injury** (`spinal-cord-injury`): trauma mechanism, midline tenderness, neurological deficit. Immobilize, CT then MRI.

### Emergent
- **Pyelonephritis** (`pyelonephritis`): flank pain, fever, CVA tenderness, pyuria, bacteriuria. Septic pyelonephritis requires IV antibiotics and admission.
- **Acute pancreatitis** (`acute-pancreatitis`): epigastric pain radiating to back, nausea/vomiting, lipase elevation
- **Vertebral fracture** (`cervical-spine-fracture` for cervical): osteoporotic compression fracture (minimal/no trauma in elderly), burst fracture (axial load), chance fracture (flexion-distraction). CT for diagnosis. MRI if neurological symptoms.

### Urgent
- **Urolithiasis** (`urolithiasis`): colicky flank-to-groin pain, hematuria (absent in 10-15%), restlessness. CT KUB without contrast.
- **Acute low back pain with radiculopathy** (`acute-low-back-pain-red-flags`): unilateral leg pain > back pain, dermatomal distribution, positive SLR, preserved bladder function. Usually managed conservatively unless progressive motor deficit.

### Non-Emergent
- **Musculoskeletal back pain** (`acute-muscle-strain`): paraspinal tenderness, pain with motion, no neurological deficit, no red flags. 90-95% of ED back pain presentations. Self-limited.
- **Degenerative disc disease:** chronic, positional, no red flags
- **Ankylosing spondylitis:** inflammatory back pain (morning stiffness > 30 min, improvement with activity), young adult, HLA-B27

## Workup

**No imaging needed if:**
- Age < 50, no red flags, no neurological deficit, no constitutional symptoms, mechanical pain pattern → musculoskeletal back pain. Treat and discharge.

**Imaging indications:**
- **MRI spine (with gadolinium):** Gold standard for cauda equina, cord compression, epidural abscess, discitis/osteomyelitis, spinal metastases. Obtain emergently (< 4 hours) if neurological compromise suspected.
- **CT abdomen/pelvis (CTA if vascular):** AAA, aortic dissection, renal pathology, retroperitoneal pathology
- **CT spine (without contrast):** Vertebral fracture (post-trauma), burst fracture assessment, bony metastases
- **Bedside ultrasound:** Aortic diameter (AAA screen), hydronephrosis (renal cause)

**Labs (only if red flags present):**
- CBC, BMP (infection, renal)
- ESR/CRP (infection, malignancy — ESR > 20 with cancer history has high sensitivity for spinal metastasis)
- Urinalysis (pyelonephritis, urolithiasis)
- Blood cultures (if fever/infection suspected)
- Lipase (pancreatitis)
- Post-void residual (bladder scan): > 200 mL concerning for cauda equina

## Treatment

Treatment is etiology-specific. For mechanical back pain:

- **NSAIDs first-line:** Ibuprofen 600-800 mg PO q8h or naproxen 500 mg PO q12h. Ketorolac 15-30 mg IV/IM for severe pain.
- **Acetaminophen:** 1 g PO q6h (adjunctive)
- **Muscle relaxants:** Cyclobenzaprine 5-10 mg PO q8h PRN (sedating — warn about driving). Methocarbamol 750-1500 mg PO q6h (less sedating alternative). Evidence for benefit is limited.
- **Opioids:** Reserve for severe pain not controlled by NSAIDs. Short course only (3-5 days). Oxycodone 5-10 mg PO q4-6h PRN.
- **Do NOT prescribe:** Systemic steroids for mechanical back pain (no evidence of benefit). Gabapentin for acute sciatica (no evidence). Bed rest (harmful — encourage activity as tolerated).
- **Epidural abscess suspected:** Vancomycin 25-30 mg/kg IV + cefepime 2 g IV (or ceftriaxone 2 g IV) while awaiting MRI
- **Cord compression from malignancy:** Dexamethasone 10 mg IV bolus, then 4 mg IV q6h

## Disposition

- **Immediate OR/intervention:** Ruptured AAA, progressive cauda equina, epidural abscess with neurological deficit
- **ICU:** Aortic dissection, sepsis from epidural abscess, spinal cord injury with neurogenic shock
- **Admission:** Epidural abscess on IV antibiotics, cauda equina (post-decompression), cord compression for radiation/surgery, vertebral fracture with instability, pyelonephritis requiring IV antibiotics
- **Observation:** Suspected cauda equina with equivocal MRI, pending neurosurgery consultation
- **Discharge with follow-up:**
  - Mechanical back pain without red flags: PCP follow-up in 1-2 weeks, return precautions for weakness/numbness/bladder dysfunction
  - Stable radiculopathy without progressive deficit: primary care or spine follow-up in 1-2 weeks, strict return precautions
  - Urolithiasis: pain controlled, no infection, stone < 10 mm
- **Return precautions (mandatory verbal and written):** "Return immediately for new or worsening weakness in legs, numbness in genital/perineal area, inability to urinate, loss of bowel control, or fever."

## Pitfalls

1. **Missing cauda equina syndrome in the patient treated for "back pain."** Ask EVERY back pain patient about bladder function, saddle numbness, and bilateral leg symptoms. Perform rectal tone exam if any suspicion. Urinary retention is the most sensitive early finding — check post-void residual.

2. **Diagnosing renal colic without considering ruptured AAA.** Both present with flank/back pain. Any male > 60 with "first-time renal colic" requires aortic evaluation. Bedside US of the aorta takes 30 seconds and can be life-saving.

3. **Dismissing epidural abscess because fever is absent.** Fever is absent in up to 50% of epidural abscesses at presentation. The combination of IVDU + back pain warrants MRI regardless of temperature. Progressive neurological deficit from epidural abscess is irreversible once established.

4. **Imaging every patient with mechanical back pain.** Lumbar spine X-rays and MRI in patients without red flags are not indicated, lead to incidental findings, increase healthcare costs, and do not improve outcomes. Imaging changes management only when red flags are present.

5. **Failing to examine rectal tone.** Decreased rectal tone is a late but critical finding in cauda equina syndrome. Many clinicians skip this exam. It is mandatory when cauda equina is on the differential.

6. **Attributing progressive bilateral leg weakness to "bilateral sciatica."** Bilateral radiculopathy from disc herniation is rare. Bilateral symptoms suggest central canal pathology (cauda equina, cord compression, epidural abscess) and require emergent MRI.

7. **Missing spinal metastases in patients with known cancer.** New back pain in any patient with a history of breast, lung, prostate, renal, thyroid, or multiple myeloma is metastatic until proven otherwise. ESR/CRP and MRI. Cord compression from metastases requires dexamethasone immediately.
