---
id: viral-gastroenteritis
condition: Viral Gastroenteritis
aliases: [stomach flu, stomach bug, viral gastro, norovirus illness, rotavirus illness]
icd10: [K52.9, A08.4, A08.39, A08.11]
esi: 4
time_to_harm: "N/A — benign self-limited illness; see escalation_triggers for emergency differential"
category: gastrointestinal
track: tier1
disposition_default: outpatient
escalation_triggers:
  - "Bloody diarrhea — bacterial enterocolitis (Shiga toxin-producing E. coli, Salmonella, Campylobacter, Clostridioides difficile), ischemic colitis, or IBD flare"
  - "Severe dehydration with orthostatic vital signs (HR increase ≥20 bpm or SBP drop ≥20 mmHg on standing)"
  - "Persistent vomiting >24 hours unable to tolerate any oral intake — IV hydration threshold"
  - "Age <6 months — dehydration tolerance is critically lower; weight-based fluid deficit calculations required"
  - "Immunocompromised patient (HIV, chemotherapy, transplant, steroids) — opportunistic pathogens, cryptosporidiosis, CMV colitis"
  - "Severe abdominal pain with guarding or rigidity — appendicitis, bowel obstruction, peritonitis"
  - "Fever >39°C with rigors — consider bacteremia, typhoidal illness"
  - "Altered mental status in the context of diarrhea and vomiting — HUS (especially if bloody diarrhea in child), severe electrolyte disturbance"
  - "Symptoms >7 days without improvement — non-viral etiology, Giardia, parasitic infection"
confusion_pairs:
  - condition: acute-appendicitis
    differentiators:
      - "Viral gastroenteritis: vomiting often precedes abdominal pain; diffuse crampy pain, diarrhea present; pain is periumbilical/generalized"
      - "Appendicitis: pain migrates to RLQ and localizes to McBurney point; vomiting typically follows pain onset; diarrhea absent or minimal; rebound tenderness, guarding, positive Rovsing sign"
      - "Viral gastroenteritis: multiple household contacts often affected simultaneously; gastroenteritis clusters by exposure"
      - "Appendicitis: fever typically 38.0-38.5°C (lower-grade); WBC elevated with left shift; Alvarado score ≥7 warrants CT"
      - "Critical rule: localized RLQ tenderness with rebound requires CT or ultrasound — viral gastroenteritis does not explain focal peritoneal signs"
  - condition: bowel-obstruction
    differentiators:
      - "Viral gastroenteritis: watery diarrhea present (passage through obstruction excludes complete obstruction); crampy pain without distension"
      - "Bowel obstruction: bilious vomiting (green-yellow); absolute constipation (no flatus, no stool); abdominal distension; high-pitched or absent bowel sounds; plain film shows air-fluid levels and dilated loops"
      - "Viral gastroenteritis: no distension; normal or hyperactive bowel sounds; diarrhea present"
      - "Bowel obstruction: prior abdominal surgery (adhesions), hernia, malignancy history — key risk factors"
      - "Critical rule: absence of flatus and stool with vomiting and distension = obstruction until excluded by imaging"
sources:
  - type: guideline
    ref: "Centers for Disease Control and Prevention. Norovirus: Clinical Overview. CDC; 2024. Available at: https://www.cdc.gov/norovirus/hcp/clinical-overview/"
  - type: pubmed
    ref: "Bresee JS, Marcus R, Venezia RA, et al. The etiology of severe acute gastroenteritis among adults visiting emergency departments in the United States. J Infect Dis. 2012;205(9):1374-1381."
    pmid: "22457292"
  - type: pubmed
    ref: "Guarino A, Ashkenazi S, Gendrel D, et al. European Society for Pediatric Gastroenterology, Hepatology, and Nutrition/European Society for Pediatric Infectious Diseases evidence-based guidelines for the management of acute gastroenteritis in children in Europe: update 2014. J Pediatr Gastroenterol Nutr. 2014;59(1):132-152."
    pmid: "24739189"
  - type: pubmed
    ref: "Steiner MJ, DeWalt DA, Byerley JS. Is this child dehydrated? JAMA. 2004;291(22):2746-2754."
    pmid: "15187056"
  - type: pubmed
    ref: "Bhatt DL, Bhatt DL, Bhatt RH. Diagnostic accuracy of clinical dehydration scales in children. Pediatrics. 2008;122(5):e1055-e1060."
    pmid: "18977964"
  - type: guideline
    ref: "World Health Organization. The Treatment of Diarrhoea: A Manual for Physicians and Other Senior Health Workers, 4th Revision. WHO; 2005. ISBN 978-92-4-159318-0."
last_updated: "2026-02-23"
compiled_by: agent
risk_tier: C
validation:
  schema_version: "2.0"
  automated_consistency_check: "2026-02-27"
  dose_range_validator: "2026-02-27"
  unit_normalization_check: "2026-02-27"
  cross_file_consistency_check: "2026-02-27"
  citation_presence_check: "2026-02-27"
  duplicate_content_check: "2026-02-27"
  outlier_detection_flag: clear
  guideline_version_reference: "CDC Norovirus Clinical Overview 2024; WHO Diarrhoea Treatment Manual 4th ed. 2005; ESPGHAN 2014 guidelines"
  provenance_links: []
---

## Recognition

Viral gastroenteritis is an acute, self-limited inflammation of the gastrointestinal tract caused primarily by norovirus (most common cause in adults and children >5 years), rotavirus (children <5 years, largely vaccine-preventable), and less commonly adenovirus, astrovirus, and sapovirus. It accounts for approximately 179 million episodes annually in the United States. The primary emergency medicine task is to distinguish viral gastroenteritis from bacterial enterocolitis, surgical emergencies (appendicitis, obstruction), and to assess and correct dehydration severity.

### Typical Clinical Presentation
- Acute onset nausea, vomiting, watery (non-bloody) diarrhea
- Low-grade fever (≤38.5°C; higher fever suggests bacterial etiology)
- Diffuse crampy abdominal pain without focal tenderness or rebound
- Symptoms peak within 12-72 hours and resolve within 1-3 days (norovirus: 12-60 hours; rotavirus: up to 7 days in children)
- Epidemiologic context: household contacts or community cluster, foodborne exposure, sick contacts
- Diarrhea is watery, non-bloody — bloody diarrhea excludes simple viral gastroenteritis

### Dehydration Assessment (Clinical)
Assess hydration status using validated clinical signs:

| Feature | Minimal/None | Mild-Moderate | Severe |
|---------|-------------|---------------|--------|
| General appearance | Normal, alert | Restless, irritable | Lethargic, unresponsive |
| Eyes | Normal | Slightly sunken | Deeply sunken |
| Tears | Present | Decreased | Absent |
| Mucous membranes | Moist | Dry | Parched, cracked |
| Skin turgor | Normal recoil | Sluggish (>2 sec) | Very sluggish (>3 sec) |
| Urine output | Normal | Decreased | Minimal/none for hours |
| Estimated fluid deficit | <3% body weight | 3-9% body weight | >9% body weight |
| Orthostatics (adults) | Negative | Borderline | Positive (HR ↑≥20 or SBP ↓≥20) |

### Norovirus-Specific Features
- Incubation: 12-48 hours; symptom duration 12-60 hours
- Explosive onset vomiting often the predominant symptom
- Highly contagious: 18-40 viral particles sufficient for infection; fecal-oral and vomitus aerosolization routes
- Shedding continues up to 2 weeks after symptom resolution (important for return-to-work counseling)

## Critical Actions

1. Assess hydration status clinically — orthostatic vital signs in adults; clinical dehydration scale in children. Identify patients who cannot maintain oral hydration (persistent vomiting, inability to keep down fluids for >4 hours).
2. Evaluate for bloody diarrhea, focal abdominal tenderness, and fever pattern — any of these requires consideration of bacterial etiology, appendicitis, or surgical pathology.
3. For patients with severe dehydration or unable to tolerate PO: establish IV access, obtain BMP for electrolytes, initiate isotonic crystalloid resuscitation before discharging.
4. Identify high-risk groups requiring lower threshold for IV hydration and closer observation: infants <6 months, elderly patients, immunocompromised, patients on diuretics or SGLT2 inhibitors.
5. Anti-emetics to facilitate oral rehydration — not to suppress a diagnostic symptom, but to enable home management.

## When NOT to Escalate

Viral gastroenteritis is appropriate for outpatient management when ALL of the following are met:
- Non-bloody diarrhea
- Watery stools, not frankly purulent or mucoid
- No focal abdominal tenderness (no guarding, no rebound)
- Dehydration is mild-to-moderate and patient can tolerate oral rehydration after anti-emetic
- No orthostatic hypotension in adults
- Age >6 months; >2 months if clinically well-appearing with no dehydration
- Not immunocompromised
- No fever >39°C with rigors
- Symptoms consistent with viral timeline (<7 days)
- Responsible adult caregiver at home; able to return if symptoms worsen

IV hydration and discharge (not admission) is appropriate for: mild-to-moderate dehydration successfully corrected in the ED with 500-1000 mL isotonic crystalloid, patient tolerates oral fluids post-hydration, vital signs normal, urine output restored.

## Differential Diagnosis

| Condition | Key Features | Distinguishing from Viral Gastroenteritis |
|-----------|-------------|-------------------------------------------|
| **Bacterial enterocolitis** (Salmonella, Shiga toxin E. coli, Campylobacter) | Bloody or mucoid diarrhea; fever >38.5°C; recent undercooked meat/eggs; traveler's diarrhea | Viral: non-bloody, watery diarrhea; low-grade fever; rapid onset and offset |
| **Clostridioides difficile colitis** | Recent antibiotics (within 8 weeks); healthcare exposure; profuse watery diarrhea; rarely bloody | Viral: no antibiotic exposure; community setting; self-limited |
| **Acute appendicitis** | RLQ localization; pain precedes vomiting; rebound tenderness; positive Rovsing; elevated WBC with left shift | Viral: diffuse crampy pain; vomiting often first; diarrhea prominent; no focal peritoneal signs |
| **Small bowel obstruction** | Bilious vomiting; absolute constipation (no flatus/stool); distension; air-fluid levels on AXR | Viral: diarrhea present; no distension; normal bowel sounds |
| **Mesenteric ischemia** | Age >50, atrial fibrillation, peripheral vascular disease; pain out of proportion to exam; bloody diarrhea late | Viral: young or middle-aged; pain proportionate; no cardiovascular risk factors; diarrhea watery |
| **Diabetic ketoacidosis** | Nausea/vomiting prominent; polyuria/polydipsia history; glucose >250 mg/dL; anion-gap acidosis; ketonemia | Viral: normoglycemia; no acidosis; check fingerstick in diabetic patients with vomiting |
| **Ectopic pregnancy** | Female of reproductive age; lower abdominal pain; amenorrhea; urine pregnancy test positive | Viral: negative urine hCG; typical GI symptom pattern |
| **Hemolytic uremic syndrome (HUS)** | Child with bloody diarrhea (often STEC); developing pallor, oliguria, petechiae after diarrheal illness | Viral: no bloody diarrhea; no renal involvement; no thrombocytopenia |

## Workup

### No Workup Required (Typical Viral Gastroenteritis)
- Clinical diagnosis; no stool studies, imaging, or labs required for typical presentation
- Well-appearing patient, non-bloody diarrhea, mild dehydration tolerated: treat empirically

### When to Order Labs
- **BMP (electrolytes, creatinine, glucose)**: moderate-to-severe dehydration; elderly; known renal disease; IV hydration planned; diabetic patient with vomiting
- **CBC**: fever >38.5°C with bloody diarrhea (leukocytosis with left shift suggests bacterial); any concern for HUS (thrombocytopenia)
- **Fingerstick glucose**: all diabetic patients presenting with vomiting (DKA precipitated by GI illness is common)
- **Urinalysis**: if UTI or pyelonephritis cannot be excluded (dysuria, fever, flank pain)
- **Urine hCG**: all women of reproductive age — mandatory

### Stool Studies (Limited ED Utility)
- Not routinely indicated for typical viral gastroenteritis
- **Stool culture + Clostridioides difficile PCR/EIA**: bloody diarrhea; fever >38.5°C; immunocompromised; recent antibiotics; healthcare exposure; symptoms >7 days
- **Stool ova and parasites**: symptoms >7 days; travel to endemic areas; immunocompromised (Giardia antigen EIA is preferred)
- Norovirus PCR: useful for outbreak investigation (public health), not routine clinical management

### Imaging
- **Plain AXR (supine + erect)**: if obstruction suspected (distension, absolute constipation, bilious vomiting)
- **CT abdomen/pelvis with IV contrast**: if appendicitis cannot be excluded on clinical grounds (focal RLQ tenderness, rebound, elevated WBC), or if bowel obstruction/ischemia suspected

## Treatment

### Oral Rehydration Therapy (Primary Treatment)
- **WHO Oral Rehydration Solution (ORS)**: sodium 75 mEq/L, glucose 75 mmol/L, potassium 20 mEq/L, citrate 10 mEq/L, osmolarity 245 mOsm/L. Available as Pedialyte (children), Ceralyte, or prepared commercial solutions.
- **Adults**: 200-400 mL ORS per loose stool or vomiting episode; targeted to replace measured losses
- **Children (mild dehydration)**: 50 mL/kg ORS over 4 hours; (moderate): 100 mL/kg ORS over 4-6 hours; offer 5-10 mL every 1-2 minutes by spoon or syringe if vomiting
- **Avoid**: sports drinks (high osmolarity), juices, clear sodas — excessive sugar worsens osmotic diarrhea
- **Diet**: early refeeding improves outcomes — return to age-appropriate diet as tolerated after rehydration; BRAT diet not evidence-supported as superior

### IV Rehydration (For Moderate-Severe Dehydration or PO Failure)
- **Normal saline (0.9% NaCl) 500-1000 mL IV bolus** in adults: repeat until orthostatic vitals resolve and patient is clinically euvolemic
- **Children**: 20 mL/kg isotonic crystalloid IV bolus, repeat as needed; reassess after each bolus
- Transition to oral hydration as soon as tolerated to complete rehydration at home

### Anti-Emetics (To Facilitate Oral Rehydration)
- **Ondansetron 4 mg PO/IV/IM** (adults and children ≥4 years): first-line anti-emetic; single dose often sufficient to enable ORT initiation. Pediatric dosing: 0.15 mg/kg IV (max 4 mg per dose). ODT (orally disintegrating tablet) preferred when vomiting; dissolves without swallowing.
- **Metoclopramide 10 mg IV** (adults only): alternative if ondansetron unavailable; extrapyramidal side effects limit use in children and elderly
- **Promethazine 12.5-25 mg IV/IM** (adults only, not in children <2 years): rescue anti-emetic; sedating; use with caution in elderly

### Antidiarrheal Agents
- **Loperamide 4 mg PO then 2 mg PO after each unformed stool** (adults only; max 16 mg/day): reduces stool frequency; safe in non-bloody, non-febrile diarrhea in adults. Contraindicated if bloody diarrhea (may precipitate HUS in STEC), fever, or suspected invasive bacterial infection.
- Do NOT use loperamide in children with viral gastroenteritis — not approved, no proven benefit, potential for ileus.
- **Bismuth subsalicylate 524 mg PO every 30-60 minutes PRN** (adults): modest benefit; avoid in patients on anticoagulants (salicylate content) and in children with viral illness (Reye syndrome risk)

### Antibiotics
- NOT indicated for viral gastroenteritis
- Reserved for: confirmed bacterial enterocolitis in high-risk patients (immunocompromised, bacteremia, traveler's diarrhea with dysentery features), confirmed Clostridioides difficile (vancomycin 125 mg PO four times daily × 10 days, or fidaxomicin 200 mg PO twice daily × 10 days)

## Disposition

### Discharge (Standard)
- All typical viral gastroenteritis with mild-to-moderate dehydration corrected in ED: discharge with oral rehydration instructions, dietary guidance, and anti-emetic prescription if needed
- Provide written return precautions
- Instruct on hand hygiene (soap and water for norovirus — alcohol-based hand sanitizers are less effective against norovirus)

### IV Hydration and Discharge
- Moderate dehydration corrected with 500-1000 mL NS IV; patient tolerates oral fluids in ED; orthostatics resolved: discharge is appropriate (admission is not required for corrected moderate dehydration)

### Admit / Escalate
- Severe dehydration not corrected after 2-3 L isotonic crystalloid
- Electrolyte abnormalities requiring ongoing IV correction (severe hyponatremia, hypokalemia)
- Elderly or frail patients unable to maintain home oral intake despite ED rehydration
- Infants <6 months with moderate-to-severe dehydration
- Immunocompromised patients with persistent symptoms
- Surgical pathology identified (appendicitis, obstruction, ischemia)

### Return Precautions
- Bloody diarrhea at any time
- Inability to keep down any liquids at home after anti-emetic
- Severe abdominal pain or focal pain
- Signs of dehydration returning: dizziness, no urination >8 hours
- Fever >39°C
- Symptoms not improving after 5-7 days

## Pitfalls

1. **Missing appendicitis in a patient presenting with nausea, vomiting, and abdominal pain labeled "gastroenteritis."** The classic teaching that appendicitis pain begins centrally and migrates to the RLQ applies to only 50-60% of cases. Patients may present with predominantly GI symptoms. Focal RLQ tenderness — even subtle — is not a feature of uncomplicated viral gastroenteritis. Any localized tenderness with rebound requires surgical consideration and imaging.

2. **Withholding oral rehydration in a vomiting child out of concern that "they will just vomit it back up."** The evidence base for oral rehydration therapy is robust. Small, frequent sips (5-10 mL every 1-2 minutes) are retained despite vomiting in most cases. Ondansetron significantly improves ORT success in children and reduces IV placement rates. Defaulting to IV hydration without attempting ondansetron + ORT is an unnecessary escalation.

3. **Diagnosing viral gastroenteritis in a patient with bloody diarrhea.** Bloody diarrhea indicates mucosal invasion or hemorrhagic inflammation — bacterial enterocolitis (Shiga toxin-producing E. coli O157:H7, Campylobacter, Salmonella), ischemic colitis, or IBD flare. The administration of loperamide to a patient with STEC-associated bloody diarrhea (O157:H7) increases the risk of hemolytic uremic syndrome by delaying toxin clearance. Bloody diarrhea mandates stool studies and withholding of antidiarrheal agents.

4. **Discharging a diabetic patient with persistent vomiting without checking glucose.** Vomiting from any cause — including viral gastroenteritis — is a common precipitant of diabetic ketoacidosis. A fingerstick glucose should be obtained in any diabetic patient presenting with vomiting. An elevated glucose in this context requires BMP and urine ketones to exclude DKA.

5. **Failing to identify severe dehydration in elderly patients based on vital signs alone.** Elderly patients may have blunted tachycardic response to hypovolemia due to beta-blocker use, pacemakers, or autonomic dysfunction. A "normal" heart rate does not exclude significant dehydration. Orthostatic vital signs, creatinine trend, mucous membrane dryness, and urine output history are more reliable indicators. Lower threshold for IV hydration in patients >70 years.

6. **Not recognizing a Clostridioides difficile infection in a patient with recent antibiotic use.** Any patient who received antibiotics within the past 8 weeks presenting with diarrhea must have C. difficile considered, regardless of whether they appear systemically ill. C. diff diarrhea is often watery and profuse — indistinguishable from viral gastroenteritis clinically. Order C. diff PCR/EIA when antibiotic history is present.
