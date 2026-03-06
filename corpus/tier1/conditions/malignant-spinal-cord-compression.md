---
id: malignant-spinal-cord-compression
condition: Malignant Spinal Cord Compression
aliases: [MSCC, metastatic spinal cord compression, epidural spinal cord compression, oncologic spinal emergency]
icd10: [G95.20, C79.49]
esi: 2
time_to_harm: "< 24 hours — neurological deficits become irreversible without emergent treatment; ambulatory status at presentation is the strongest predictor of outcome"
category: neurological
track: tier1
confusion_pairs:
  - condition: cauda-equina-syndrome
    differentiators:
      - "MSCC: known malignancy, back pain progressing to weakness, upper motor neuron signs above conus (hyperreflexia, Babinski, clonus)"
      - "CES: lower motor neuron signs (areflexia, flaccidity), saddle anesthesia, urinary retention, may have disc herniation history"
      - "MSCC often multilevel; CES typically single-level disc or mass at/below L1-L2"
  - condition: spinal-cord-compression
    differentiators:
      - "MSCC: known cancer history, progressive back pain worse at night/supine, multilevel involvement common"
      - "Non-malignant cord compression: acute trauma or disc herniation, typically single level, no constitutional symptoms"
      - "MSCC: pathological fracture on imaging, epidural soft tissue mass; non-malignant: disc herniation, stenosis, hematoma"
  - condition: spinal-epidural-abscess
    differentiators:
      - "MSCC: known malignancy, insidious onset over weeks, no fever, normal or mildly elevated inflammatory markers"
      - "Epidural abscess: fever, IVDU or recent spinal procedure, rapid progression over days, elevated WBC/ESR/CRP, ring-enhancing collection on MRI"
      - "Both present with progressive back pain and neurological deficit — MRI with gadolinium distinguishes"
sources:
  - type: pubmed
    ref: "Patchell RA et al. Direct decompressive surgical resection in the treatment of spinal cord compression caused by metastatic cancer: a randomised trial. Lancet. 2005;366(9486):643-648"
    pmid: "16112300"
  - type: pubmed
    ref: "Loblaw DA et al. Systematic review of the diagnosis and management of malignant extradural spinal cord compression: report of the ESMO-EANO task force. J Clin Oncol. 2005;23(9):2028-2037"
    pmid: "15774794"
  - type: guideline
    ref: "NICE Clinical Guideline CG75: Metastatic spinal cord compression in adults — risk assessment, diagnosis and management. 2008 (updated 2019)"
  - type: pubmed
    ref: "Rades D et al. Prognostic factors for local control and survival after radiotherapy of metastatic spinal cord compression. Brain. 2002;125(Pt 7):1519-1530"
    pmid: "12077002"
last_updated: "2026-03-06"
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
# Malignant Spinal Cord Compression

## Recognition

Oncologic emergency affecting 5-10% of cancer patients. Breast, lung, and prostate carcinoma account for the majority of cases. Thoracic spine involved in 60-70%, lumbar 20-30%, cervical 10%.

**Key presentation pattern:** Back pain (present in 90%) precedes neurological deficit by days to weeks. Pain is characteristically worse at night and in the supine position, distinguishing it from mechanical back pain.

**Clinical features:**
- Progressive back pain — worse with recumbency, Valsalva, percussion over spinous process
- Weakness — typically begins as gait difficulty, progresses to paraparesis
- Upper motor neuron signs below the level of compression: hyperreflexia, Babinski sign, clonus, spasticity
- Sensory level — band of hyperesthesia at the compression level, numbness below
- Bowel/bladder dysfunction — late finding; urinary retention, overflow incontinence, constipation
- Pathological fracture — sudden onset of pain may indicate vertebral body collapse

**CRITICAL:** Ambulatory status at the time of treatment initiation is the strongest predictor of ambulatory status after treatment. Patients who are still walking have a 70-90% chance of remaining ambulatory; patients who are paraplegic have < 10% chance of regaining ambulation.

**High-risk cancer types:** Breast, lung, prostate (most common); renal cell carcinoma, multiple myeloma, lymphoma, thyroid, melanoma.

## Critical Actions

| Action | Target |
|---|---|
| Dexamethasone 10 mg IV bolus | Immediately upon clinical suspicion — do NOT wait for MRI |
| MRI entire spine with gadolinium | Emergent (< 4 hours) |
| Radiation oncology consult | Within 2 hours of confirmed diagnosis |
| Neurosurgical consult | Within 2 hours if surgical candidate |

1. **Start dexamethasone immediately:** 10 mg IV bolus upon clinical suspicion. Do NOT delay steroids for imaging confirmation. The risk of one steroid dose in the absence of compression is negligible; the cost of delay is permanent paralysis.
2. **MRI entire spine with and without gadolinium:** Image the entire spine — multilevel disease in 30% of cases. Single-region imaging misses additional compression sites.
3. **Maintain dexamethasone:** 4 mg IV q6h after initial bolus. High-dose regimen (96 mg IV bolus) for rapidly progressive neurological deficit — higher complication rate but may preserve function in deteriorating patients.
4. **Consult radiation oncology and neurosurgery simultaneously.** Treatment decision (surgery vs. radiation vs. combined) depends on tumor histology, number of compression levels, spinal stability, and patient functional status.
5. **Bladder catheterization** if urinary retention present (bladder scan > 200 mL post-void residual).
6. **VTE prophylaxis:** Enoxaparin 40 mg SC daily — these patients are at high thrombotic risk from immobility and malignancy.
7. **Pain management:** Morphine 2-4 mg IV q2-4h PRN for severe pain. Dexamethasone itself provides significant analgesic effect via edema reduction.

## Differential Diagnosis

| Condition | Key Distinguishing Features |
|---|---|
| Cauda equina syndrome | Lower motor neuron signs (areflexia, flaccidity), saddle anesthesia, urinary retention, typically single-level disc herniation at/below L1-L2 |
| Spinal epidural abscess | Fever, IVDU/recent procedure, rapid progression, elevated WBC/ESR/CRP, ring-enhancing collection on MRI |
| Spinal epidural hematoma | Anticoagulation use, acute onset, hyperacute MRI signal, no enhancing mass |
| Transverse myelitis | Intramedullary cord signal (not extrinsic compression), no epidural mass, often post-viral, may have optic neuritis (NMO) |
| Vertebral compression fracture (osteoporotic) | No epidural mass, no neurological deficit (unless retropulsion), no enhancement on MRI, history of osteoporosis |
| Guillain-Barre syndrome | Ascending areflexic paralysis, no sensory level, normal spinal MRI, CSF albuminocytologic dissociation |
| Leptomeningeal carcinomatosis | Multifocal cranial nerve palsies, CSF cytology positive, diffuse meningeal enhancement on MRI |

## Workup

- **MRI entire spine with gadolinium:** Gold standard. Defines location, extent, degree of compression, number of levels. Sensitivity > 93%, specificity > 97%. Image entire spine regardless of symptom localization.
- **CT myelography:** If MRI contraindicated (pacemaker, certain metallic implants) or unavailable. Invasive but provides equivalent anatomic information.
- **Plain radiographs:** Low sensitivity (< 60% for early disease). May show vertebral body collapse, pedicle erosion ("winking owl" sign on AP view), pathological fracture.
- **CT spine without contrast:** Useful for bony anatomy and surgical planning; does not adequately visualize the spinal cord or epidural space.
- **Labs:** CBC, BMP, coagulation studies, calcium (hypercalcemia of malignancy), LDH, alkaline phosphatase.
- **Tumor markers if unknown primary:** PSA, serum/urine protein electrophoresis (SPEP/UPEP), CA 15-3 (breast), CEA.
- **CT chest/abdomen/pelvis:** Staging workup if new cancer diagnosis or unknown primary.
- **Post-void residual** by bladder scan.

## Treatment

### Corticosteroids
- **Standard dose:** Dexamethasone 10 mg IV bolus, then 4 mg IV q6h
- **High dose (for rapidly progressive deficit):** Dexamethasone 96 mg IV bolus, then 24 mg IV q6h x 3 days, then taper over 2 weeks. Associated with higher GI complication rate (perforation, hemorrhage) — reserve for patients with rapid neurological deterioration.
- Start proton pump inhibitor (pantoprazole 40 mg IV daily) with high-dose steroids.
- Monitor blood glucose q6h — steroid-induced hyperglycemia is common.

### Surgical Decompression
Patchell trial (Lancet 2005): Surgery + radiation superior to radiation alone. Significantly more patients maintained ambulation (84% vs. 57%) and regained ambulation (62% vs. 19%).

**Indications for surgery:**
- Single-level compression amenable to decompression
- Radioresistant tumor (renal cell, melanoma, sarcoma, non-small cell lung cancer)
- Spinal instability (SINS score >= 7)
- Neurological deterioration during radiation therapy
- Unknown tumor histology (tissue diagnosis needed)
- Good functional status (ECOG 0-2), life expectancy > 3 months

### Radiation Therapy
- First-line for radiosensitive tumors (lymphoma, myeloma, small cell lung cancer, breast, prostate)
- Multiple levels of compression
- Poor surgical candidates
- Postoperative adjuvant after decompression
- Standard fractionation: 30 Gy in 10 fractions or 20 Gy in 5 fractions
- Stereotactic body radiation therapy (SBRT) for oligometastatic disease or re-irradiation

### Supportive Care
- **Pain:** Morphine 2-4 mg IV q2-4h PRN; transition to long-acting opioid for chronic management
- **VTE prophylaxis:** Enoxaparin 40 mg SC daily
- **Bowel regimen:** Senna 8.6 mg PO BID + docusate 100 mg PO BID (opioid-related + immobility)
- **Physical therapy consultation** once stabilized

## Disposition

- **Operating room:** Rapidly progressive deficit, surgical candidate per criteria above
- **Oncology/neurosurgery admission:** All confirmed MSCC — coordinated radiation and/or surgical planning
- **ICU:** High cervical lesion with respiratory compromise, hemodynamic instability, post-operative monitoring
- **Transfer:** If facility lacks emergent MRI or spine surgery capability. Start dexamethasone 10 mg IV and morphine for pain BEFORE transfer. Do not delay treatment.
- **Discharge:** Not appropriate for confirmed or suspected MSCC

## Pitfalls

1. **Waiting for MRI confirmation before starting dexamethasone.** In a patient with known malignancy presenting with new back pain and neurological deficit, dexamethasone should be given immediately. Every hour of delay reduces the probability of neurological recovery. The steroid dose carries minimal risk even if compression is not confirmed.

2. **Imaging only the symptomatic spinal region.** Multilevel disease is present in 30% of MSCC cases. Whole-spine MRI is the standard of care. Missing a second compression site changes surgical planning and radiation field design.

3. **Attributing back pain in a cancer patient to "musculoskeletal strain."** New or worsening back pain in any patient with a history of breast, lung, prostate, renal, or myeloma should prompt urgent evaluation for MSCC. Night pain and pain worse with recumbency are red flags that distinguish malignant from mechanical back pain.

4. **Failing to assess ambulatory status as a prognostic marker.** Whether the patient can still walk at the time of treatment is the single most important prognostic variable. Patients should be treated as emergently as STEMI — delays convert ambulatory patients to paraplegic ones.

5. **Not consulting both radiation oncology and neurosurgery.** The Patchell trial demonstrated that combined surgery + radiation is superior to radiation alone for selected patients. Single-specialty consultation misses the opportunity for optimal multimodal treatment.

6. **Missing autonomic dysfunction.** Urinary retention, constipation, and orthostatic hypotension may be early signs of cord compression that are attributed to medications or comorbidities. New-onset urinary retention in a cancer patient warrants urgent spinal evaluation.

7. **Assuming radiosensitive tumors do not need surgical evaluation.** Even lymphoma and myeloma may require surgical stabilization if the spine is mechanically unstable (SINS score >= 7). Radiation treats the tumor but does not restore spinal stability.
