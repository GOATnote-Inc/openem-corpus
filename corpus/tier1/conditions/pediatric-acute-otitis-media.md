---
id: pediatric-acute-otitis-media
condition: Pediatric Acute Otitis Media
aliases: [AOM, acute otitis media, ear infection, middle ear infection, otitis media]
icd10: [H66.00, H66.01, H66.02, H66.03, H66.009, H66.90]
esi: 4
time_to_harm: "N/A — benign self-limited condition in most children; see escalation_triggers for complications"
category: pediatric
track: tier1
disposition_default: outpatient
escalation_triggers:
  - "Signs of mastoiditis: postauricular erythema, swelling, tenderness, or protrusion of the auricle"
  - "Meningeal signs: neck stiffness, photophobia, Kernig or Brudzinski sign"
  - "Altered mental status or lethargy beyond typical irritability"
  - "Facial nerve palsy (peripheral VII nerve involvement)"
  - "Labyrinthitis: associated vertigo and sensorineural hearing loss"
  - "Fever >39°C (102.2°F) unresponsive to antipyretics with severe otalgia"
  - "Immunocompromised child (HIV, congenital immune deficiency, chemotherapy)"
  - "Age <6 months: all cases require immediate antibiotic treatment"
  - "Bilateral AOM in child <24 months with any symptoms"
  - "AOM with spontaneous otorrhea through tympanic membrane"
confusion_pairs:
  - condition: bacterial-meningitis
    differentiators:
      - "AOM: ear-localized pain, intact mental status, no meningeal signs, fever typically <40°C"
      - "Meningitis: meningeal signs (nuchal rigidity, Kernig, Brudzinski), altered mental status, purpuric rash possible"
      - "AOM: otoscopic findings (bulging TM, effusion) explain fever source"
      - "Meningitis: AOM can be a contiguous source for meningitis — if meningeal signs present with AOM, LP is mandatory"
sources:
  - type: guideline
    ref: "Lieberthal AS, Carroll AE, Chonmaitree T, et al. The Diagnosis and Management of Acute Otitis Media. Pediatrics. 2013;131(3):e964-e999."
    pmid: "23439909"
  - type: pubmed
    ref: "Rovers MM, Glasziou P, Appelman CL, et al. Antibiotics for acute otitis media: a meta-analysis with individual patient data. Lancet. 2006;368(9545):1429-1435."
    pmid: "17055944"
  - type: pubmed
    ref: "Spiro DM, Tay KY, Arnold DH, et al. Wait-and-see prescription for the treatment of acute otitis media: a randomized controlled trial. JAMA. 2006;296(10):1235-1241."
    pmid: "16968834"
  - type: pubmed
    ref: "Little P, Gould C, Williamson I, et al. Pragmatic randomised controlled trial of two prescribing strategies for childhood acute otitis media. BMJ. 2001;322(7282):336-342."
    pmid: "11159657"
  - type: review
    ref: "Venekamp RP, Sanders SL, Glasziou PP, Del Mar CB, Rovers MM. Antibiotics for acute otitis media in children. Cochrane Database Syst Rev. 2015;(6):CD000219."
    pmid: "26099233"
last_updated: "2026-02-23"
compiled_by: agent
risk_tier: C
validation:
  schema_version: "2.0"
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  guideline_version_reference: "AAP/AAFP 2013 CPG (current as of 2026)"
  provenance_links: []
---

## Recognition

Acute otitis media (AOM) is the most common reason for pediatric antibiotic prescriptions in the US. Approximately 50% of children have at least one episode by age 1 year; 80% by age 3 years. Most episodes are self-limited: 80% resolve spontaneously within 3 days without antibiotics.

### AAP 2013 Diagnostic Criteria (All three required)
AOM requires: (1) acute onset, (2) middle ear effusion, AND (3) middle ear inflammation.

**Middle ear effusion** (at least one of):
- Distinct bulging of the tympanic membrane (TM)
- Limited or absent mobility of the TM on pneumatic otoscopy
- Air-fluid level behind TM
- Otorrhea not due to acute otitis externa

**Middle ear inflammation** (at least one of):
- Moderate to severe bulging of the TM
- Intense erythema of the TM
- Otalgia (ear pain) causing child to hold or rub ear, with onset <48 hours

**Avoid AOM diagnosis based on erythema alone** — erythema without effusion or bulging is not AOM (crying, fever cause TM redness without effusion).

### Clinical Presentation by Age
- **Infants/toddlers**: Pulling or rubbing ear, unexplained irritability especially at night, fever, difficulty sleeping, reduced feeding
- **Older children**: Otalgia verbalized, hearing difficulty, fullness in ear, fever
- **Otorrhea**: Painless drainage through perforated TM indicates spontaneous perforation — relieves pain, is not a sign of worsening; treat with antibiotics

### Severity Classification
- **Mild**: Otalgia <48 hours, fever <39°C (102.2°F)
- **Severe**: Otalgia ≥48 hours, fever ≥39°C (102.2°F), or any bilateral AOM in child <24 months

## Critical Actions

Outpatient management — not an emergency. Key actions:

1. Confirm AOM diagnosis using pneumatic otoscopy (gold standard for TM mobility). Do not diagnose AOM without visualizing the TM.
2. Classify severity (mild vs. severe) and patient age to determine antibiotic vs. watchful waiting.
3. Prescribe appropriate analgesic regardless of antibiotic decision: acetaminophen 15 mg/kg PO/PR q4-6h PRN or ibuprofen 10 mg/kg PO q6-8h PRN (ibuprofen for age ≥6 months).
4. For watchful-waiting candidates: issue a "safety-net" (contingency/delayed) antibiotic prescription with instruction to fill only if symptoms worsen or fail to improve in 48-72 hours.
5. Educate caregivers on return criteria and complication signs (mastoiditis, meningismus, facial palsy).
6. Arrange follow-up for persistent symptoms at 48-72 hours, recurrent AOM, or persistent middle ear effusion.

## When NOT to Escalate

Watchful waiting (antibiotic deferral for 48-72 hours) is appropriate for ALL of the following:
- Age ≥6 months
- Unilateral AOM with mild symptoms (otalgia <48 hours, fever <39°C)
- OR bilateral AOM in child ≥24 months with mild symptoms
- No otorrhea through tympanic membrane
- No immunocompromise
- No craniofacial abnormality or tympanostomy tubes
- No concurrent illness requiring antibiotics
- Reliable follow-up available and caregiver can manage safety-net prescription

Emergency care is NOT required for typical AOM in a child who is alert, interactive, and not toxic-appearing. AOM is a primary care or urgent care diagnosis.

### Immediate Antibiotics Required (Do Not Use Watchful Waiting)
- Age <6 months (all AOM)
- Bilateral AOM in child <24 months
- AOM with otorrhea (any age)
- Severe AOM (otalgia ≥48 hours or fever ≥39°C)
- Immunocompromised child
- Tympanostomy tubes in place

## Differential Diagnosis

| Condition | Key Features | Distinguishing from AOM |
|-----------|-------------|------------------------|
| **Otitis media with effusion (OME)** | Middle ear fluid without acute inflammation; no pain or fever; discovered incidentally | No bulging TM, no acute onset, no otalgia — not AOM, no antibiotics |
| **Acute otitis externa** | Canal erythema and edema, pain with tragus/pinna traction, exudate in canal; TM visible and normal | Pain with ear traction, canal involved; TM normal or occluded by debris |
| **Mastoiditis** | Postauricular swelling, tenderness, and erythema; auricle displaced anteriorly and inferiorly; follows AOM | Fever, toxic appearance, postauricular findings — requires CT and IV antibiotics |
| **Bacterial meningitis** | Meningeal signs, altered mental status, purpuric rash, headache in older children; AOM can be a contiguous source | Any meningeal sign with AOM requires immediate LP and empiric coverage |
| **Pharyngitis / tonsillitis** | Throat pain, exudate; referred otalgia from oropharyngeal source is common in older children | TM normal and mobile on pneumatic otoscopy; no middle ear effusion |
| **Foreign body** | Unilateral ear pain, discharge, or hearing loss; visualized on otoscopy | Foreign body visible in canal; TM may be normal or traumatized |
| **Teething** | Irritability, drooling, biting; common in 6-24 months — frequently blamed for ear-pulling | No TM abnormality; ear-pulling is non-specific in this age group |

## Workup

### Standard AOM
- **No labs or imaging required** for uncomplicated AOM
- Diagnosis is clinical based on history and pneumatic otoscopy
- Tympanometry: adjunct to confirm effusion if otoscopy is unclear; flattened type B tympanogram indicates effusion

### When Workup is Required
- **Blood culture, CBC, CRP**: if toxic-appearing, high fever, or suspected bacteremia
- **CT temporal bones with contrast**: if mastoiditis suspected (postauricular swelling, tenderness, auricular displacement)
- **LP**: if any meningeal signs present — AOM can seed meninges contiguously
- **MRI with contrast**: if intracranial complication suspected (subdural empyema, epidural abscess, lateral sinus thrombosis, brain abscess)

## Treatment

### Watchful Waiting (Antibiotic Deferral)
No antibiotic at time of visit. Issue contingency prescription to be filled only if:
- Symptoms worsen at any time, OR
- No improvement after 48-72 hours

This strategy avoids unnecessary antibiotic exposure in 70-80% of watchful-waiting patients (who improve spontaneously) while maintaining a safety net.

### First-Line Antibiotic (When Indicated)
- **Amoxicillin 80-90 mg/kg/day PO divided q8-12h x 5-10 days**
  - Age <2 years or severe: 10 days
  - Age ≥2 years with mild-moderate: 5-7 days adequate
  - Maximum dose: 3 g/day

### Penicillin Allergy
- Non-anaphylactic PCN allergy: cefdinir 14 mg/kg/day PO divided q12-24h, OR cefuroxime 30 mg/kg/day PO divided q12h, OR cefpodoxime 10 mg/kg/day PO divided q12h — all x 5-7 days
- Anaphylactic PCN allergy: azithromycin 10 mg/kg PO day 1, then 5 mg/kg/day PO days 2-5; or clindamycin 30-40 mg/kg/day PO divided q8h (covers Streptococcus pneumoniae but not Haemophilus influenzae)

### Treatment Failure (Symptoms Persist or Worsen after 48-72h of Amoxicillin)
- Switch to: amoxicillin-clavulanate 90 mg/kg/day (amoxicillin component) PO divided q12h x 10 days
- Covers beta-lactamase-producing H. influenzae and Moraxella catarrhalis

### Analgesia (All Patients, Regardless of Antibiotic Decision)
- Acetaminophen 15 mg/kg PO/PR q4-6h PRN (max 5 doses/24h)
- Ibuprofen 10 mg/kg PO q6-8h PRN (age ≥6 months; avoid if <6 months, renal disease, or volume depleted)
- Do NOT use topical benzocaine eardrops if TM perforation is possible

## Disposition

### Discharge (Standard)
- All children meeting watchful-waiting criteria: discharge with analgesics, contingency antibiotic prescription, and return precautions
- All children starting antibiotics who are non-toxic: discharge with 48-72 hour follow-up for treatment failure assessment

### Return Precautions (Caregiver Instructions)
- Return immediately if: fever >40°C, stiff neck, severe headache, altered behavior, facial swelling, redness behind ear, or facial asymmetry
- Return in 48-72 hours if no improvement on antibiotic

### Follow-up
- Persistent middle ear effusion after AOM: expected in 40% at 4 weeks, 10% at 3 months — does not require retreatment unless symptomatic
- Recurrent AOM (≥3 episodes in 6 months or ≥4 in 12 months): referral to ENT for tympanostomy tube consideration

### Admit / Escalate to ED
- Any complication: mastoiditis, meningitis, facial nerve palsy, labyrinthitis, intracranial extension
- Toxic-appearing child with high fever unresponsive to antipyretics
- Immunocompromised child

## Pitfalls

1. **Over-escalation: prescribing immediate antibiotics to all children with AOM.** Cochrane meta-analysis (2015) demonstrates that 80% of children with AOM improve within 3 days without antibiotics. Watchful waiting for 48-72 hours in eligible children (≥6 months, unilateral, mild symptoms) is guideline-concordant and reduces antibiotic exposure and resistance development without increased complication risk.

2. **Under-escalation: missing mastoiditis as a complication.** Mastoiditis presents with postauricular erythema, swelling, and tenderness with forward-inferior auricular displacement. The TM often shows AOM findings. This is a surgical emergency requiring CT temporal bones, IV antibiotics, and ENT consultation. Classic teaching: "postauricular swelling = mastoiditis until proven otherwise."

3. **Diagnosing AOM based on erythema alone.** Crying and fever cause tympanic membrane erythema without effusion. The AAP 2013 guideline requires middle ear effusion (bulging TM, limited mobility, or air-fluid level) plus inflammation. Erythema alone = diagnosis insufficiently supported; do not prescribe antibiotics.

4. **Missing meningitis because AOM "explains" the fever.** AOM is a known contiguous source for bacterial meningitis. Any child with AOM and meningeal signs (nuchal rigidity, Kernig, Brudzinski, or altered mental status) requires LP regardless of the otoscopic findings. Do not anchor on AOM as the sole source.

5. **Using topical benzocaine with possible TM perforation.** Topical anesthetics (Auralgan, antipyrine-benzocaine) are contraindicated if the TM may be perforated. Spontaneous otorrhea indicates perforation. Use systemic analgesics in all cases; topical eardrops only if perforation is excluded.

6. **Cognitive bias — "treat to reassure parents."** Parental expectation of antibiotics is a well-documented driver of antibiotic overprescription in AOM. Evidence shows that caregiver satisfaction is equivalent between watchful waiting with good education and immediate antibiotic treatment. Prescribing unnecessary antibiotics is not benign: it drives resistance, exposes children to adverse effects, and creates future antibiotic-resistant infections.
