---
id: acute-low-back-pain-red-flags
condition: Acute Low Back Pain with Red Flags
aliases: [back pain red flags, low back pain emergency, back pain with neurological deficit, emergent back pain]
icd10: [M54.50, M54.59]
esi: 3
time_to_harm: "< 24-48 hours (cauda equina, epidural abscess, epidural hematoma); days to weeks (malignancy, osteomyelitis)"
mortality_if_delayed: "Low mortality for most etiologies; permanent neurological disability (paraplegia, bowel/bladder dysfunction) in 30-70% with delayed diagnosis of cauda equina, epidural abscess, or epidural hematoma"
category: musculoskeletal
track: tier1
sources:
  - type: guideline
    ref: "Chou R et al. Diagnosis and Treatment of Low Back Pain: A Joint Clinical Practice Guideline from the ACP and APS. Ann Intern Med 2007;147(7):478-491"
    pmid: "17909209"
  - type: guideline
    ref: "Qaseem A et al. Noninvasive Treatments for Acute, Subacute, and Chronic Low Back Pain: A Clinical Practice Guideline from the ACP. Ann Intern Med 2017;166(7):514-530"
    pmid: "28192789"
  - type: review
    ref: "Deyo RA, Weinstein JN. Low back pain. N Engl J Med 2001;344(5):363-370"
    pmid: "11172169"
  - type: meta-analysis
    ref: "Downie A et al. Red flags to screen for malignancy and fracture in patients with low back pain: systematic review. BMJ 2013;347:f7095"
    pmid: "24335669"
  - type: pubmed
    ref: "Verhagen AP et al. Red flags presented in current low back pain guidelines: a review. Eur Spine J 2016;25(9):2788-2802"
    pmid: "27376468"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: C
validation:
  automated_consistency_check: "2026-02-27"
  dose_range_validator: "2026-02-27"
  unit_normalization_check: "2026-02-27"
  cross_file_consistency_check: "2026-02-27"
  citation_presence_check: "2026-02-27"
  duplicate_content_check: "2026-02-27"
  outlier_detection_flag: clear
  schema_version: "2.0"
  provenance_links: []
---
# Acute Low Back Pain with Red Flags

## Recognition

**Epidemiology:** Low back pain accounts for 2-3% of all ED visits. Approximately 85% of acute low back pain is mechanical and has no specific pathoanatomic diagnosis. Serious underlying pathology (fracture, malignancy, infection, cauda equina syndrome) accounts for < 5% of presentations, but these are the cases that cause permanent disability or death when missed.

**Framework:** The purpose of the ED evaluation is NOT to diagnose the specific cause of back pain in every patient. It is to identify the subset with red flags that warrant emergent workup and to safely disposition the rest. This file provides the evaluation framework. For management of specific diagnoses, see `cauda-equina-syndrome.md` and `spinal-epidural-abscess.md`.

### Red Flags Requiring Emergent Evaluation

**Neurological Emergency (minutes-to-hours matter):**
- **Saddle anesthesia** — perineal numbness (S2-S5); test with pinprick bilaterally
- **Urinary retention or new incontinence** — bladder scan for post-void residual (PVR); PVR > 200 mL is abnormal
- **Fecal incontinence** — loss of anal sphincter tone on digital rectal exam
- **Bilateral lower extremity weakness** — especially progressive
- **Progressive neurological deficit** — worsening motor or sensory function over hours to days

**Infectious (hours-to-days matter):**
- **Fever + back pain** — spinal epidural abscess until proven otherwise, especially with any risk factor
- **IVDU + back pain** — IVDU is the single strongest risk factor for epidural abscess (present in 25-50% of SEA cases)
- **Recent spinal procedure + fever + back pain** — direct inoculation risk
- **Immunosuppression + fever + back pain** — diabetes, HIV, chronic steroids, chemotherapy

**Malignancy (days matter):**
- **Cancer history + new back pain** — metastatic spinal cord compression; breast, lung, prostate, renal, myeloma most common
- **Unexplained weight loss + back pain** (> 10 kg over 6 months)
- **Age > 50 with new-onset back pain** and no improvement after 4-6 weeks (lower threshold for imaging)
- **Night pain that wakes the patient** and does not improve with position changes
- **Pain worse supine** (opposite of mechanical pain pattern)

**Vascular/Structural:**
- **Anticoagulation + back pain** — spinal epidural hematoma; can present hours to days after starting anticoagulation or post-procedure
- **Significant trauma + back pain** — vertebral fracture, especially in osteoporotic patients; low-energy falls in elderly count as significant
- **Known aortic aneurysm + acute back pain** — ruptured AAA; see `ruptured-aaa.md`
- **Age > 70 or chronic corticosteroid use + back pain after fall** — insufficiency fracture threshold is low

### What is NOT a red flag (and should NOT get emergent imaging):
- Isolated low back pain without neurological symptoms, < 6 weeks duration
- Unilateral radiculopathy with intact strength and bladder function
- Chronic back pain without new or progressive features
- Paraspinal muscle spasm without fever

## Critical Actions

1. **Focused neurological exam in every back pain patient.** Must include: bilateral lower extremity motor strength (L2-S1 myotomes), sensation (light touch, pinprick including saddle area), deep tendon reflexes (patellar L3-L4, Achilles S1), straight leg raise, and assessment of gait. Document it.
2. **Ask about bladder and bowel function directly.** "Are you able to urinate normally? Any difficulty starting or stopping? Any leaking of urine or stool? Any numbness in the groin or between your legs?" Patients do not volunteer these symptoms.
3. **Bladder scan (PVR) if any urinary complaint or suspicion of cauda equina.** PVR > 200 mL is abnormal. PVR > 500 mL is strongly suggestive of cauda equina syndrome. This is the single most objective bedside test.
4. **Digital rectal exam if cauda equina suspected.** Document voluntary anal sphincter contraction as present or absent.
5. **Check temperature in every patient with back pain.** Fever + back pain = obtain ESR, CRP, blood cultures, and strongly consider MRI. Do not dismiss fever as coincidental.
6. **Emergent MRI for any neurological red flag.** Do not substitute CT or plain films. CT myelogram is the alternative only if MRI is contraindicated or unavailable.
7. **Start antibiotics before MRI if epidural abscess is suspected.** Vancomycin 25-30 mg/kg IV loading dose + ceftriaxone 2 g IV. Draw blood cultures first, but do not delay antibiotics if cultures will take time to collect.
8. **Consult spine surgery before MRI results if clinical suspicion is high for cauda equina or epidural abscess.** Parallel processing saves hours.

## Differential Diagnosis

| Condition | Red Flag Features | ED Workup |
|-----------|-------------------|-----------|
| **Cauda equina syndrome** | Saddle anesthesia, urinary retention (PVR > 200 mL), bilateral leg weakness, decreased rectal tone | Emergent MRI lumbar spine; see `cauda-equina-syndrome.md` |
| **Spinal epidural abscess** | Fever (50-65%), IVDU, immunosuppression, point midline tenderness, progressive pain over days; classic triad (fever, back pain, neuro deficit) present in only 13% | ESR/CRP, blood cultures, emergent MRI entire spine with gadolinium; see `spinal-epidural-abscess.md` |
| **Spinal epidural hematoma** | Anticoagulation, coagulopathy, post-procedural, acute-onset severe pain with rapid neuro decline | Emergent MRI, STAT coagulation studies, anticoagulation reversal |
| **Metastatic spinal cord compression** | Known malignancy, progressive pain over weeks, night pain, weight loss, pain worse supine | MRI entire spine with gadolinium, dexamethasone 10 mg IV |
| **Vertebral compression fracture** | Trauma (or minimal trauma in osteoporotic/steroid-treated patients), focal midline tenderness | Plain radiographs (initial); CT or MRI if neurological deficit |
| **Vertebral osteomyelitis/discitis** | Subacute course (weeks), fever (variable), IVDU, recent bacteremia, elevated ESR/CRP | ESR/CRP, blood cultures, MRI with gadolinium |
| **Abdominal aortic aneurysm (ruptured)** | Acute severe back/abdominal pain, hemodynamic instability, pulsatile abdominal mass, age > 60 | Bedside ultrasound, CT angiography if stable |
| **Mechanical low back pain (85%)** | No red flags, no neurological deficits, paraspinal tenderness, reproduced by movement, self-limited | No imaging if < 6 weeks; reassurance and symptomatic treatment |
| **Lumbar radiculopathy** | Unilateral, dermatomal pain radiating below knee, positive SLR, single myotome weakness possible | Outpatient MRI if not improving at 4-6 weeks; emergent MRI only if progressive motor deficit |

## Workup

### When to Image Emergently (MRI)
- Any cauda equina red flag (saddle anesthesia, urinary retention, bilateral weakness, fecal incontinence)
- Fever + back pain with risk factors for epidural abscess (IVDU, immunosuppression, recent spinal procedure)
- Anticoagulation + acute back pain with neurological symptoms (epidural hematoma)
- Known cancer + new back pain with neurological deficit
- Progressive bilateral neurological deficit from any cause

### When to Image Urgently (within 24-48 hours)
- Known cancer + new back pain WITHOUT neurological deficit (outpatient MRI acceptable if reliable follow-up)
- Suspected osteomyelitis/discitis (fever, elevated inflammatory markers, risk factors) without neurological deficit
- Vertebral fracture with concern for instability but no neurological deficit

### When NOT to Image
- Acute mechanical low back pain < 6 weeks without red flags — imaging does not improve outcomes and leads to unnecessary interventions
- Chronic back pain without new neurological symptoms or progressive features
- Isolated unilateral radiculopathy with intact motor function and bladder function

### Labs (When Infection or Malignancy Suspected)
- **ESR** — most sensitive lab marker for epidural abscess (> 20 mm/h in > 95% of SEA cases; mean ~75 mm/h). Also elevated in malignancy and osteomyelitis.
- **CRP** — elevated in > 90% of SEA; mean ~100 mg/L. More rapidly responsive than ESR.
- **CBC** with differential — leukocytosis is neither sensitive nor specific (normal WBC in 35-40% of SEA)
- **Blood cultures x 2** — before antibiotics if infection suspected (positive in 60% of SEA)
- **BMP** — baseline
- **Coagulation studies** — if on anticoagulants or concern for epidural hematoma
- **Urinalysis** — rule out UTI as confounder for urinary symptoms

### Imaging Modalities
- **MRI with gadolinium** — gold standard for all serious spinal pathology. Image the entire lumbosacral spine for cauda equina; image the entire spine for suspected abscess (non-contiguous lesions in 10-15%).
- **CT myelogram** — acceptable alternative when MRI is contraindicated or unavailable
- **CT without contrast** — appropriate for vertebral fracture characterization
- **Plain radiographs** — limited utility; may show compression fracture, spondylolisthesis, or late osteomyelitis changes. Insufficient to rule out abscess, tumor, or cauda equina.
- **Bedside ultrasound** — for bladder volume (PVR) and abdominal aorta, not for spinal pathology

## Treatment

### Pain Management for Acute Low Back Pain

**First-line (all patients without contraindications):**

| Medication | Dose | Route | Notes |
|------------|------|-------|-------|
| **Acetaminophen** | 1000 mg q6h (max 4 g/day; 2 g/day if hepatic impairment) | PO or IV | Safe, effective, no anti-inflammatory effect |
| **Ibuprofen** | 400-600 mg q6h | PO | Preferred NSAID for back pain; equivalent to higher doses for analgesia |
| **Naproxen** | 250-500 mg q12h | PO | Longer duration; good for discharged patients |
| **Ketorolac** | 15-30 mg IV/IM (15 mg if age > 65, weight < 50 kg, or renal impairment) | IV or IM | Max 5 days total NSAID use with ketorolac; single dose in ED often sufficient |

**Second-line (adjuncts):**

| Medication | Dose | Route | Notes |
|------------|------|-------|-------|
| **Cyclobenzaprine** | 5-10 mg q8h | PO | Muscle relaxant; sedating. Use 5 mg in elderly. Short-term only (1-2 weeks). |
| **Methocarbamol** | 750-1500 mg q6h | PO | Less sedating than cyclobenzaprine. Reasonable alternative. |
| **Diazepam** | 5-10 mg PO x1 in ED | PO | Muscle relaxant effect; avoid at discharge (dependence risk). Single ED dose acceptable for severe spasm. |

**Third-line (severe pain refractory to above):**

| Medication | Dose | Route | Notes |
|------------|------|-------|-------|
| **Morphine** | 0.05-0.1 mg/kg IV titrated q15 min | IV | Use lowest effective dose; confounds neurological exam |
| **Oxycodone** | 5-10 mg q4-6h PRN | PO | Short course only (3-5 days) if NSAID/acetaminophen insufficient; avoid in patients needing serial neuro exams |

**Evidence-based notes:**
- NSAIDs are superior to acetaminophen alone for acute mechanical back pain (ACP 2017 guideline)
- Skeletal muscle relaxants provide modest short-term benefit; NNT ~5
- Systemic corticosteroids do NOT improve outcomes in acute low back pain and are NOT recommended
- Opioids should be avoided or used at lowest dose for shortest duration; no evidence of superiority over NSAIDs for acute back pain

### Specific Treatments by Etiology
- **Cauda equina syndrome** — emergent surgical decompression; see `cauda-equina-syndrome.md`
- **Spinal epidural abscess** — vancomycin 25-30 mg/kg IV + ceftriaxone 2 g IV q12h; emergent surgical drainage if neurological deficit; see `spinal-epidural-abscess.md`
- **Epidural hematoma** — anticoagulation reversal (4-factor PCC, vitamin K, idarucizumab, or andexanet alfa as appropriate) + emergent surgical evacuation
- **Metastatic cord compression** — dexamethasone 10 mg IV bolus, then 4 mg IV q6h; radiation oncology and neurosurgery consultation
- **Vertebral compression fracture** — pain control; orthopedic or neurosurgical follow-up; bracing in selected cases

## Disposition

### Emergent Admission/Transfer
- Cauda equina syndrome (confirmed or strongly suspected) — neurosurgery, OR
- Spinal epidural abscess — neurosurgery + infectious disease
- Spinal epidural hematoma — neurosurgery, OR
- Metastatic cord compression with neurological deficit — neurosurgery + oncology
- Unstable vertebral fracture — spine surgery

### Discharge (majority of patients)
Appropriate for acute mechanical low back pain without red flags AND normal neurological exam.

**Discharge instructions must include:**
- Return immediately for: inability to urinate, new numbness in groin/perineum/buttocks, loss of bowel control, progressive weakness in either or both legs, new or worsening fever
- Written cauda equina precautions — these must be on the discharge paperwork
- Follow-up with primary care in 1-2 weeks if not improving
- Activity: remain active as tolerated. Bed rest does NOT improve outcomes and is not recommended.
- Avoid routine imaging referral for uncomplicated pain < 6 weeks

### Transfer
If facility lacks emergent MRI or spine surgery, arrange emergent transfer for any patient with neurological red flags. Start antibiotics and dexamethasone (as appropriate) before transfer. Perform and document a neurological exam before transport.

## Pitfalls

1. **Not asking about bladder and bowel function.** Patients with early cauda equina syndrome may not volunteer urinary symptoms. Direct questioning about difficulty initiating urination, new incontinence, or perineal numbness is mandatory in every back pain patient. Failure to ask is failure to diagnose.

2. **Skipping the bladder scan.** "The patient says they urinated" does not exclude retention. Overflow incontinence produces small voids while the bladder retains 500+ mL. A PVR is the objective, 30-second test that separates reassurance from emergent MRI. It should be reflexive in any back pain patient with urinary complaints.

3. **Ordering plain films instead of MRI for suspected cauda equina or epidural abscess.** X-rays cannot visualize the spinal canal, disc herniations, abscesses, or soft-tissue cord compression. They are useless for these diagnoses. MRI is the only appropriate emergent study. CT myelogram is the fallback if MRI is unavailable.

4. **Dismissing fever + back pain as "muscle strain plus viral illness."** This combination, especially in an IVDU, diabetic, or immunosuppressed patient, is epidural abscess until MRI says otherwise. ESR and CRP should be sent. The classic triad (fever, back pain, neurological deficit) is present in only 13% at initial presentation; waiting for all three guarantees a late diagnosis with irreversible deficits.

5. **Anchoring on "sciatica" when symptoms are bilateral.** Unilateral radiculopathy is common and usually benign. Bilateral radiculopathy is never benign. Bilateral leg symptoms with back pain — especially with any bowel/bladder complaint — demands emergent evaluation for cauda equina syndrome.

6. **Imaging the wrong levels or incomplete spine.** Epidural abscesses are non-contiguous in 10-15% of cases. An MRI of the lumbar spine alone may miss a thoracic abscess. For suspected infection: image the entire spine with gadolinium. For suspected cauda equina: image the entire lumbosacral region including the conus.

7. **Discharging a patient with back pain and progressive bilateral weakness for "outpatient MRI."** Progressive bilateral motor deficit is a surgical emergency. Outpatient MRI scheduled for next week results in irreversible paraplegia. If MRI is unavailable at your facility, transfer the patient. Do not schedule it and send them home.

8. **Relying on normal WBC to exclude infection.** WBC is normal in 35-40% of patients with epidural abscess. ESR (> 20 mm/h in > 95% of SEA) and CRP (elevated in > 90%) are far more sensitive screening labs. A normal WBC does not exclude spinal infection.

9. **Prescribing opioids as first-line for acute back pain.** Opioids are not superior to NSAIDs for acute mechanical back pain, carry addiction risk, cause constipation, and — critically — confound serial neurological exams in patients who may need reassessment. NSAIDs + acetaminophen are first-line. If opioids are used, prescribe the lowest dose for the shortest duration (3-5 days).

10. **Failing to give written cauda equina return precautions.** Disc herniations can progress. A patient discharged with mechanical back pain today may develop cauda equina syndrome tonight. Every back pain discharge must include explicit written instructions to return for inability to urinate, perineal numbness, bowel incontinence, or progressive bilateral leg weakness. Verbal instructions alone are medicolegally insufficient.
