---
id: pediatric-fever-evaluation
condition: "Pediatric Fever — Emergency Evaluation"
aliases: [pediatric fever, fever in children, febrile child, febrile infant, neonatal fever, fever infant]
icd10: [R50.9, R50.81]
esi: 2
time_to_harm:
  irreversible_injury: "< 2 hours (neonatal meningitis, sepsis)"
  death: "< 6 hours (neonatal sepsis, bacterial meningitis)"
  optimal_intervention_window: "< 60 minutes (empiric antibiotics for febrile neonate)"
category: presentations
condition_type: presentation
chief_complaint: "Pediatric Fever"
differential_categories:
  - category: life-threatening
    conditions:
      - bacterial-meningitis
      - sepsis
      - neonatal-emergencies
      - hsv-encephalitis
      - necrotizing-enterocolitis
      - kawasaki-disease
  - category: emergent
    conditions:
      - pneumonia
      - epiglottitis
      - retropharyngeal-abscess
      - peritonsillar-abscess
      - acute-appendicitis
      - intussusception
      - febrile-seizure
      - bronchiolitis
      - complicated-uti
      - mastoiditis
      - cellulitis-abscess
  - category: urgent
    conditions:
      - croup
      - acute-agitation
      - drug-hypersensitivity-reaction
  - category: non-emergent
    conditions:
      - pediatric-acute-otitis-media
red_flags:
  - "Age < 28 days with any fever (T >= 38.0°C)"
  - "Age 29-60 days with fever and ill appearance"
  - "Petechial or purpuric rash"
  - "Bulging fontanelle"
  - "Inconsolable crying or paradoxical irritability (worse when held)"
  - "Lethargy or poor feeding"
  - "Signs of dehydration (sunken fontanelle, absent tears, dry mucous membranes)"
  - "Fever > 40.0°C (104°F)"
  - "Immunocompromised child with fever"
  - "Fever persisting > 5 days (Kawasaki disease)"
  - "Toxic or ill appearance"
  - "Recent antibiotic use masking partially treated meningitis"
decision_rules:
  - name: "Rochester Criteria (febrile infants 0-60 days)"
    citation: "Dagan R et al. Identification of infants unlikely to have serious bacterial infection although hospitalized for suspected sepsis. J Pediatr. 1985;107(6):855-860."
    pmid: "4067741"
  - name: "Philadelphia Criteria"
    citation: "Baker MD et al. Outpatient management without antibiotics of fever in selected infants. N Engl J Med. 1993;329(20):1437-1441."
    pmid: "8413453"
  - name: "Step-by-Step Approach"
    citation: "Mintegi S et al. Clinical prediction rule for distinguishing bacterial from aseptic meningitis. Pediatrics. 2017;140(1):e20170187."
  - name: "AAP Febrile Infant Guideline (2021)"
    citation: "Pantell RH et al. Evaluation and Management of Well-Appearing Febrile Infants 8 to 60 Days Old. Pediatrics. 2021;148(2):e2021052228."
    pmid: "34281996"
track: tier1
sources:
  - type: guideline
    ref: "AAP Clinical Practice Guideline: Evaluation and Management of Well-Appearing Febrile Infants 8 to 60 Days Old. Pediatrics. 2021;148(2):e2021052228."
    pmid: "34281996"
  - type: guideline
    ref: "AAP Clinical Practice Guideline: Management of Febrile Children 3 to 36 Months of Age with No Source of Infection."
  - type: guideline
    ref: "NICE Guidelines: Fever in Under 5s: Assessment and Initial Management. 2021."
  - type: pubmed
    ref: "Kuppermann N et al. A Clinical Prediction Rule to Identify Febrile Infants 60 Days and Younger at Low Risk for Serious Bacterial Infections. JAMA Pediatr. 2019;173(4):342-351."
    pmid: "30776077"
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
# Pediatric Fever — Emergency Evaluation

## Recognition

Fever in children is the single most common chief complaint in pediatric emergency medicine. The approach is fundamentally stratified by age, because the risk of serious bacterial infection (SBI) and the ability to clinically assess illness severity vary dramatically across age groups.

**Definition of fever:**
- Rectal temperature >= 38.0°C (100.4°F) — this is the standard for infants
- Axillary, temporal, and tympanic temperatures are less reliable in infants and should NOT be used to make disposition decisions in neonates

**Age-stratified SBI risk:**
- **< 28 days (neonate):** SBI rate 10-12%. This is the highest-risk group. ALL febrile neonates require full sepsis workup and empiric antibiotics regardless of appearance. HSV risk. Group B strep, E. coli, Listeria.
- **29-60 days:** SBI rate 5-8%. Well-appearing infants can be risk-stratified using validated criteria (AAP 2021 guideline, Rochester, Step-by-Step).
- **61-90 days:** SBI rate 3-5%. Lower risk if well-appearing with normal inflammatory markers and urinalysis.
- **3-36 months:** SBI rate 1-3% (lower with HiB and pneumococcal vaccination). UTI is the most common occult SBI. Bacteremia rare in vaccinated children.
- **> 36 months:** Clinical assessment more reliable. Approach similar to adults with age-appropriate differential.

**Clinical appearance assessment (most important for children > 28 days):**
- **Well-appearing (low risk):** alert, interactive, making eye contact, strong cry, consolable, feeding well, good color, normal activity
- **Ill-appearing (high risk):** lethargy, poor tone, weak cry, inconsolable, poor feeding, mottled/pale/cyanotic, poor perfusion (cap refill > 3 sec)
- **"Toxic" appearance:** implies sepsis/severe infection regardless of age — full workup, empiric antibiotics, and admission

**Paradoxical irritability:** infant is more irritable when held or moved (suggests meningeal irritation). Distinguishable from normal fussiness where holding soothes the child.

## Critical Actions

| Action | Target |
|---|---|
| Rectal temperature measurement | < 5 minutes |
| Assess clinical appearance (ill vs well) | < 10 minutes |
| Full sepsis workup if < 28 days | < 30 minutes |
| Empiric antibiotics if < 28 days with fever | < 60 minutes |
| Urinalysis (catheterized) if < 24 months with no source | < 30 minutes |

**Age-stratified evaluation algorithm:**

### Neonates (0-28 days)

ALL febrile neonates require:
1. Complete blood count with differential
2. Blood culture
3. Urinalysis + urine culture (catheterized specimen — bag specimens have unacceptable contamination rates)
4. Lumbar puncture (CSF cell count, protein, glucose, gram stain, culture, HSV PCR)
5. CXR if respiratory symptoms
6. Empiric antibiotics: ampicillin 50 mg/kg IV + gentamicin 4-5 mg/kg IV (or cefotaxime 50 mg/kg IV where available)
7. Add acyclovir 20 mg/kg IV if any concern for HSV (seizure, vesicular rash, maternal HSV history, CSF pleocytosis, elevated AST/ALT, sepsis picture without clear bacterial source)
8. **Admit all febrile neonates.** No exceptions.

**HSV risk factors in neonates:**
- Maternal genital HSV (especially primary infection at delivery)
- Vesicular skin lesions
- Seizure
- CSF pleocytosis with negative gram stain
- Elevated transaminases
- Coagulopathy/DIC without clear cause

### Young Infants (29-60 days)

**AAP 2021 Guideline for well-appearing febrile infants 8-60 days:**
- **Inflammatory markers:** WBC, procalcitonin (PCT), CRP, urinalysis
- **Low-risk criteria:** Well-appearing + normal urinalysis + normal inflammatory markers (WBC 5,000-15,000, ANC < 4,000, PCT < 0.5 ng/mL)
- **29-60 days, well-appearing, low-risk by labs:** Observation without antibiotics may be appropriate IF reliable follow-up in 24 hours. LP should be performed (AAP recommends LP for all 22-28 day olds; for 29-60 days, LP may be deferred if all other markers are low-risk, but must be performed before antibiotics if given).
- **29-60 days, ill-appearing OR abnormal labs:** Full sepsis workup including LP, empiric antibiotics (ceftriaxone 50 mg/kg IV + consider ampicillin for Listeria coverage), admit.

### Infants 61-90 days

- Well-appearing with normal UA and labs: lower risk. Can be managed with close outpatient follow-up if reliable caregivers.
- Ill-appearing: full workup and antibiotics as above.
- UTI is the most common SBI in this group — always obtain catheterized UA/culture.

### Children 3-36 months

- **Well-appearing, fully vaccinated:** Focus on source identification. UTI is the most common occult SBI.
  - Urinalysis (catheterized if < 2 years) for: all girls < 24 months, uncircumcised boys < 12 months, circumcised boys < 6 months, or any child with urinary symptoms
  - CXR if respiratory symptoms, tachypnea, or fever > 39°C without source
  - No routine blood work needed if well-appearing and vaccinated with identifiable source
- **Fever > 5 days without source:** Evaluate for Kawasaki disease (see `kawasaki-disease`). Incomplete Kawasaki is common — maintain high index of suspicion.
- **Ill-appearing or unvaccinated:** CBC, blood culture, urinalysis/culture, CXR, consider LP

### Children > 36 months

- Clinical assessment is more reliable. Approach guided by presentation and focal findings.
- Fever with petechiae/purpura → meningococcemia → blood cultures, empiric ceftriaxone, isolate
- Fever with limp or refusal to bear weight → septic arthritis, osteomyelitis → joint aspiration if effusion

## Differential Diagnosis

### Life-Threatening
- **Bacterial meningitis** (`bacterial-meningitis`): fever, irritability, bulging fontanelle (infants), nuchal rigidity (older children), petechiae (meningococcal). Neonatal organisms: GBS, E. coli, Listeria. Infant/child: Strep pneumoniae, N. meningitidis.
- **Sepsis** (`sepsis`): fever + tachycardia + poor perfusion + AMS. Neonatal sepsis may present with hypothermia, apnea, feeding intolerance, jaundice rather than classic features.
- **Neonatal emergencies** (`neonatal-emergencies`): broad category including neonatal sepsis, meningitis, metabolic crises, congenital heart disease presenting with fever
- **HSV encephalitis** (`hsv-encephalitis`): neonatal HSV presenting with fever, seizures, vesicles. Acyclovir must be given empirically.
- **Necrotizing enterocolitis** (`necrotizing-enterocolitis`): premature or sick neonate with fever, abdominal distension, feeding intolerance, bloody stool, pneumatosis on X-ray
- **Kawasaki disease** (`kawasaki-disease`): fever >= 5 days + 4/5 criteria (bilateral conjunctivitis, oral mucosal changes, polymorphous rash, extremity changes, cervical lymphadenopathy). Incomplete Kawasaki: < 4 criteria. Risk of coronary artery aneurysm if untreated. IVIG + aspirin.

### Emergent
- **Pneumonia** (`pneumonia`): fever, cough, tachypnea, crackles. CXR for confirmation. Age-appropriate antibiotics.
- **Epiglottitis** (`epiglottitis`): rare post-HiB vaccine but still occurs. Fever, drooling, tripod positioning, muffled voice. Do NOT examine oropharynx in children — risk of complete obstruction. Controlled airway management in OR.
- **Retropharyngeal abscess** (`retropharyngeal-abscess`): fever, neck stiffness, dysphagia, drooling, neck swelling. Lateral neck X-ray (widened retropharyngeal space). CT neck with IV contrast.
- **Peritonsillar abscess** (`peritonsillar-abscess`): fever, sore throat, trismus, "hot potato" voice, uvular deviation. Older children/adolescents.
- **Appendicitis** (`acute-appendicitis`): fever, RLQ pain, anorexia, vomiting. Atypical in young children — often presents late with perforation. Ultrasound first in pediatrics to minimize radiation.
- **Intussusception** (`intussusception`): intermittent colicky abdominal pain, "currant jelly" stool (late), palpable mass, target sign on ultrasound. Peak age 6-36 months.
- **Febrile seizure** (`febrile-seizure`): seizure in child 6 months - 5 years associated with fever but without CNS infection. Simple (< 15 min, generalized, single) vs complex (> 15 min, focal, or recurrent within 24 hours). Complex febrile seizures require LP and imaging consideration.
- **Bronchiolitis** (`bronchiolitis`): age < 2 years, RSV season, rhinorrhea → wheezing → respiratory distress. Supportive care — no routine antibiotics, steroids, or bronchodilators.
- **UTI** (`complicated-uti`): fever, irritability, vomiting in young infants. Dysuria, frequency in toilet-trained children. Catheterized specimen for culture. > 50,000 CFU/mL with pyuria is positive. Antibiotic choice age-dependent.
- **Mastoiditis** (`mastoiditis`): fever, post-auricular swelling/erythema/tenderness, protruding pinna. Complication of acute otitis media. CT temporal bone. IV antibiotics ± myringotomy.

### Urgent
- **Croup** (`croup`): barky cough, inspiratory stridor, fever. Steeple sign on AP neck X-ray (not routinely needed). Dexamethasone 0.15-0.6 mg/kg PO/IM (single dose). Nebulized racemic epinephrine 0.5 mL of 2.25% for moderate-severe.
- **Drug reaction** (`drug-hypersensitivity-reaction`): fever, rash, eosinophilia, recent new medication

### Non-Emergent
- **Acute otitis media** (`pediatric-acute-otitis-media`): fever, ear pain, bulging tympanic membrane. Most common pediatric infection. Many viral. Antibiotics per AAP guidelines (amoxicillin 80-90 mg/kg/day if treating).
- **Viral upper respiratory infection:** most common cause of pediatric fever overall. Rhinorrhea, cough, congestion, well-appearing.
- **Roseola (HHV-6):** fever × 3-5 days, then diffuse maculopapular rash as fever resolves. Benign.
- **Viral gastroenteritis:** fever, vomiting, diarrhea. Assess hydration status.

## Workup

**Workup is fundamentally age-stratified:**

| Age | Minimum Workup for Fever Without Source |
|---|---|
| 0-28 days | CBC, blood culture, UA/urine culture (cath), LP, CXR if resp sx, HSV PCR if risk factors |
| 29-60 days | CBC, blood culture, UA/urine culture (cath), LP (per guideline/risk), inflammatory markers (PCT, CRP) |
| 61-90 days | UA/urine culture (cath), CBC if ill-appearing or abnormal UA |
| 3-24 months | UA/urine culture (cath) per screening criteria, CXR if indicated |
| > 24 months | Source-directed. No routine blood work if well-appearing with source |

**Key labs and their interpretation:**
- **Procalcitonin (PCT):** Most useful single inflammatory marker for SBI in febrile infants. PCT < 0.5 ng/mL → low risk. More specific than WBC or CRP for bacterial infection.
- **WBC:** 5,000-15,000 is reassuring in young infants. Very low WBC (< 5,000) or very high (> 15,000) → higher SBI risk. Bandemia > 1,500 is concerning.
- **CRP:** < 20 mg/L is reassuring. Less specific than PCT.
- **CSF interpretation (normal pediatric values):**
  - Neonates: WBC < 20/mm3, protein < 100 mg/dL (< 150 in preterm), glucose > 40 mg/dL
  - Infants: WBC < 9/mm3, protein < 45 mg/dL, glucose > 40 mg/dL

**Urinalysis pitfalls:**
- Bag specimens have unacceptable contamination rates (up to 60% false positive). Use catheterized specimen for all infants < 24 months.
- Positive UA requires confirmation with urine culture before diagnosing UTI.
- Leukocyte esterase and nitrite are screening tests only. Microscopy (> 10 WBC/hpf) and culture are definitive.

## Treatment

Treatment is age and source-dependent. Empiric antibiotics for high-risk groups:

**Neonatal sepsis (0-28 days):**
- Ampicillin 50 mg/kg IV q8h (covers GBS, Listeria, Enterococcus) + gentamicin 4-5 mg/kg IV q24h (covers gram negatives)
- OR ampicillin + cefotaxime 50 mg/kg IV q8h (if gentamicin not preferred — note cefotaxime availability issues)
- Add acyclovir 20 mg/kg IV q8h if HSV suspected
- Duration: until cultures negative at 36-48 hours AND clinically well AND LP reassuring

**Young infants (29-60 days):**
- If antibiotics indicated: ceftriaxone 50 mg/kg IV/IM (covers most SBI pathogens including meningitis)
- Add ampicillin 50 mg/kg IV if Listeria not excluded (< 6 weeks, immunocompromised)
- Add acyclovir if HSV risk features

**Older infants and children:**
- UTI: cephalexin 25-50 mg/kg/day PO divided q6-8h (outpatient) OR ceftriaxone 50 mg/kg IV (inpatient)
- Pneumonia: amoxicillin 90 mg/kg/day PO divided q12h (outpatient) OR ampicillin 50 mg/kg IV q6h (inpatient)
- Meningitis: ceftriaxone 100 mg/kg/day IV divided q12h + vancomycin 60 mg/kg/day IV divided q6h + dexamethasone 0.15 mg/kg IV q6h × 4 days

**Antipyretics (for comfort, NOT to prevent febrile seizures):**
- Acetaminophen 15 mg/kg PO/PR q4-6h (max 75 mg/kg/day)
- Ibuprofen 10 mg/kg PO q6h (age > 6 months only)
- Alternating acetaminophen and ibuprofen is commonly practiced but not evidence-based over either alone
- Do NOT use aspirin in children (Reye syndrome)

**Fever does NOT need to be "treated" if the child is comfortable.** Fever is a physiologic response that may enhance immune function. Antipyretics improve comfort but do not change the disease course or prevent febrile seizures.

## Disposition

- **Admit all febrile neonates (0-28 days).** No exceptions. Empiric antibiotics pending cultures x 36-48 hours.
- **Admit 29-60 day febrile infants who are:** ill-appearing, have abnormal inflammatory markers, have abnormal UA, have LP showing pleocytosis, or whose caregivers cannot ensure reliable 24-hour follow-up.
- **Consider discharge for 29-60 day febrile infants who are:** well-appearing, normal inflammatory markers (WBC, PCT, CRP), normal UA, blood culture sent, reliable caregivers with 24-hour follow-up confirmed, and clear return precautions provided. This is per AAP 2021 guideline — institution-dependent.
- **Admit older infants/children who are:** ill-appearing, unable to tolerate PO, dehydrated requiring IV, have uncertain diagnosis requiring monitoring, or have concerning social situation.
- **Discharge older infants/children who are:** well-appearing, identified viral source, tolerating PO, adequate hydration, reliable caregivers.
- **Return precautions (ALL discharged febrile children):** "Return immediately if: not feeding/drinking, fewer wet diapers, rash (especially purpura/petechiae), increased irritability or lethargy, difficulty breathing, seizure, fever persisting > 5 days, or any parental concern."
- **Follow-up:** Pending blood/urine cultures must be followed within 24-48 hours. Establish clear callback system.

## Pitfalls

1. **Discharging a febrile neonate (< 28 days) without full workup.** No clinical assessment, no blood test, and no decision rule can reliably exclude SBI in neonates. Every neonate with T >= 38.0°C requires full sepsis workup, empiric antibiotics, and admission. This is an absolute rule.

2. **Using bag urine specimen to make decisions.** Bag urine specimens have a contamination rate of up to 60%. A positive bag specimen is meaningless. All infants < 24 months requiring urinalysis need catheterized or suprapubic aspiration specimens.

3. **Assuming fever height correlates with illness severity.** While fever > 40°C is associated with slightly higher SBI risk in some studies, many children with 40.5°C fevers have benign viral illness, and neonates with serious bacterial infections may have only 38.1°C. Clinical appearance is more important than temperature magnitude.

4. **Missing Kawasaki disease.** Fever > 5 days without source in a child 6 months - 5 years should trigger Kawasaki evaluation. Incomplete Kawasaki (fewer than 4/5 criteria) is common and easily missed. Untreated Kawasaki causes coronary artery aneurysms in 25% of cases. Echocardiography is indicated.

5. **Failing to consider HSV in neonates.** HSV encephalitis/disseminated HSV in neonates has > 50% mortality if untreated. Acyclovir must be added if: vesicular rash, seizure, CSF pleocytosis, elevated transaminases, coagulopathy, or no clear bacterial source for sepsis picture. Do NOT wait for PCR results to start acyclovir.

6. **Anchoring on "teething fever."** Teething may cause low-grade temperature elevation (< 38.3°C) but does NOT cause true fever (>= 38.5°C). Attributing fever to teething is dangerous and delays evaluation of actual infections.

7. **Skipping LP because "the baby looks fine."** Well-appearing neonates have bacterial meningitis. Clinical appearance alone cannot exclude meningitis in infants < 60 days. LP is a critical part of the workup in this age group. Performing LP is uncomfortable but safe; missing meningitis is catastrophic.

8. **Not following up on pending cultures.** Blood and urine cultures take 24-48 hours. A child discharged from the ED with pending cultures who grows a pathogen needs recall. Establish a reliable culture follow-up system (nurse callback, parent phone confirmation, PCP notification).
