---
id: abdominal-pain-acute
condition: "Acute Abdominal Pain — Emergency Evaluation"
aliases: [abdominal pain, belly pain, stomach pain, acute abdomen, surgical abdomen]
icd10: [R10.9, R10.0, R10.10, R10.30, R10.11, R10.31, R10.2]
esi: 2
time_to_harm:
  irreversible_injury: "< 6 hours (mesenteric ischemia, ruptured ectopic, bowel perforation)"
  death: "< 2 hours (ruptured AAA, mesenteric ischemia, ruptured ectopic)"
  optimal_intervention_window: "< 60 minutes (ruptured AAA, ectopic pregnancy)"
category: presentations
condition_type: presentation
chief_complaint: "Abdominal Pain"
differential_categories:
  - category: life-threatening
    conditions:
      - ruptured-aaa
      - mesenteric-ischemia
      - ectopic-pregnancy
      - placental-abruption
      - perforated-peptic-ulcer
      - bowel-obstruction
      - acute-pancreatitis
      - sepsis
      - hemorrhagic-shock
      - aortic-dissection
      - diabetic-ketoacidosis
      - acute-hepatic-failure
      - toxic-megacolon
  - category: emergent
    conditions:
      - acute-appendicitis
      - acute-cholecystitis
      - ascending-cholangitis
      - incarcerated-hernia
      - ovarian-torsion
      - testicular-torsion
      - splenic-laceration
      - liver-laceration
      - sigmoid-volvulus
      - small-bowel-volvulus
      - intussusception
      - fourniers-gangrene
      - spontaneous-bacterial-peritonitis
      - acute-mesenteric-venous-thrombosis
  - category: urgent
    conditions:
      - acute-diverticulitis
      - pyelonephritis
      - urolithiasis
      - acute-pancreatitis
      - complicated-uti
      - ischemic-colitis
      - ogilvie-syndrome
      - acute-urinary-retention
  - category: non-emergent
    conditions:
      - biliary-colic
      - viral-gastroenteritis
      - acute-gout
red_flags:
  - "Hemodynamic instability (hypotension, tachycardia)"
  - "Rigid abdomen (peritonitis)"
  - "Pulsatile abdominal mass (AAA)"
  - "Positive pregnancy test with abdominal pain (ectopic pregnancy)"
  - "Pain out of proportion to physical exam (mesenteric ischemia)"
  - "Peritoneal signs (rebound, guarding)"
  - "Fever with jaundice and RUQ pain (Charcot triad — ascending cholangitis)"
  - "Free air on imaging"
  - "Bloody or coffee-ground emesis/nasogastric aspirate"
  - "Abdominal distension with absent bowel sounds"
  - "History of atrial fibrillation with acute abdominal pain (mesenteric embolism)"
decision_rules:
  - name: "Alvarado Score (MANTRELS)"
    citation: "Alvarado A. A practical score for the early diagnosis of acute appendicitis. Ann Emerg Med. 1986;15(5):557-564."
    pmid: "3963537"
  - name: "RIPASA Score"
    citation: "Chong CF et al. Development of the RIPASA score: a new appendicitis scoring system for the diagnosis of acute appendicitis. Singapore Med J. 2010;51(3):220-225."
    pmid: "20428744"
track: tier1
sources:
  - type: guideline
    ref: "ACEP Clinical Policy: Critical Issues for the Initial Evaluation and Management of Patients Presenting With a Chief Complaint of Nontraumatic Acute Abdominal Pain. Ann Emerg Med. 2000;36(4):406-415."
  - type: guideline
    ref: "ACR Appropriateness Criteria: Acute Nonlocalized Abdominal Pain. 2023."
  - type: review
    ref: "Macaluso CR, McNamara RM. Evaluation and management of acute abdominal pain in the emergency department. Int J Gen Med. 2012;5:789-797."
    pmid: "23055768"
  - type: guideline
    ref: "EAST Practice Management Guideline: Evaluation of Acute Abdominal Pain in the Emergency Department."
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
# Acute Abdominal Pain — Emergency Evaluation

## Recognition

Abdominal pain is the most common chief complaint in US EDs, comprising 7-10% of all visits. The differential diagnosis is among the broadest in emergency medicine, spanning GI, vascular, GU, gynecologic, cardiac, and metabolic etiologies. Age and sex fundamentally alter the differential.

**Pain character and localization:**
- **Visceral pain** (hollow organ distension, solid organ capsule stretch): diffuse, poorly localized, crampy, midline
- **Parietal/somatic pain** (peritoneal irritation): sharp, well-localized, worse with movement, cough, or percussion
- **Referred pain:** diaphragmatic irritation → shoulder (ectopic pregnancy, splenic injury), cardiac → epigastric (inferior MI), renal → flank/groin (urolithiasis)

**Location-based differential framework:**
- **RUQ:** cholecystitis, hepatitis, ascending cholangitis, hepatic abscess, pneumonia (basal), Fitz-Hugh-Curtis
- **LUQ:** splenic pathology, pancreatitis, renal, pneumonia
- **RLQ:** appendicitis, ovarian torsion/cyst, ectopic pregnancy, Meckel diverticulum, inguinal hernia, cecal volvulus
- **LLQ:** diverticulitis, ovarian pathology, ectopic pregnancy, sigmoid volvulus, inguinal hernia
- **Epigastric:** peptic ulcer, pancreatitis, ACS (inferior MI), AAA, biliary colic, gastritis, aortic dissection
- **Periumbilical:** early appendicitis, small bowel obstruction, mesenteric ischemia, AAA
- **Suprapubic:** UTI, urinary retention, ectopic pregnancy, PID
- **Diffuse:** peritonitis, bowel obstruction, DKA, SBO, mesenteric ischemia, sickle cell crisis

**Key history elements:**
- Onset: sudden (perforation, vascular catastrophe, torsion) vs gradual (inflammatory, infectious)
- Character: colicky/cramping (obstruction, renal colic) vs constant (peritonitis, ischemia)
- Migration: periumbilical → RLQ (classic appendicitis)
- Associated symptoms: vomiting (obstruction, pancreatitis, cholecystitis), diarrhea (infectious, IBD, ischemic colitis), hematemesis/melena (GI hemorrhage, PUD), vaginal bleeding (ectopic, threatened abortion), urinary symptoms (UTI, pyelonephritis, urolithiasis)
- Last menstrual period (mandatory in all reproductive-age females)
- Prior surgeries (adhesive SBO), medications (NSAIDs → PUD, anticoagulation → hemorrhage)
- Comorbidities: atrial fibrillation (mesenteric embolism), AAA history, liver disease (SBP)

## Critical Actions

| Action | Target |
|---|---|
| Assess hemodynamic stability | < 2 minutes |
| Pregnancy test (reproductive-age females) | < 15 minutes |
| Identify surgical emergency | < 30 minutes |
| Pain management initiated | < 30 minutes (analgesia does NOT mask surgical findings) |
| Imaging if indicated | < 60 minutes |

**Evaluation algorithm:**

1. **Hemodynamic assessment.** Tachycardia and hypotension → resuscitate with crystalloid, cross-match blood, consider surgical emergency (ruptured AAA, ruptured ectopic, hemorrhagic shock, mesenteric ischemia). Two large-bore IVs immediately.

2. **Pregnancy test in all reproductive-age females.** Positive pregnancy test + abdominal pain + vaginal bleeding = ectopic pregnancy until proven otherwise. Quantitative hCG + transvaginal ultrasound.

3. **Physical examination:**
   - Inspection: distension, visible hernia, skin changes (Grey Turner/Cullen sign → hemorrhagic pancreatitis or ruptured AAA — late finding)
   - Auscultation: absent bowel sounds (ileus, late SBO), high-pitched rushes/borborygmi (mechanical SBO)
   - Palpation: localized tenderness, rebound, involuntary guarding, pulsatile mass
   - Rectal exam: if GI bleeding, prostate pathology, or perianal/pelvic pathology suspected
   - Pelvic exam: if gynecologic cause suspected (adnexal tenderness, cervical motion tenderness, cervical os assessment)
   - Testicular exam in males (referred pain from testicular torsion can present as abdominal pain)

4. **Categorize the clinical picture:**
   - Peritonitis (rigid abdomen, rebound, guarding) → surgical consultation immediately, CT to localize if hemodynamically stable
   - Pulsatile mass + hypotension in patient > 60 → ruptured AAA → OR immediately (bedside US to confirm, do NOT delay for CT if unstable)
   - Obstruction pattern (distension, vomiting, absent/hyperactive bowel sounds) → NG tube, IV fluids, CT abdomen/pelvis with IV contrast
   - Pain out of proportion to exam → mesenteric ischemia until proven otherwise → CTA abdomen/pelvis

5. **Analgesia.** Provide pain management early. IV opioids (morphine 0.1 mg/kg or fentanyl 1 mcg/kg) do NOT mask peritoneal signs or delay surgical diagnosis. Withholding analgesia is outdated and harmful.

## Differential Diagnosis

### Life-Threatening
- **Ruptured AAA** (`ruptured-aaa`): age > 60, sudden abdominal/back pain, pulsatile mass, hypotension. 50% mortality even with surgery. Bedside US for aortic diameter (> 3 cm abnormal, > 5 cm high rupture risk).
- **Mesenteric ischemia** (`mesenteric-ischemia`): acute onset, pain out of proportion to exam, atrial fibrillation, metabolic acidosis/lactate elevation. "Mesenteric ischemia kills by being diagnosed too late." CTA is diagnostic.
- **Ectopic pregnancy** (`ectopic-pregnancy`): positive pregnancy test + abdominal/pelvic pain + vaginal bleeding. Ruptured ectopic → hemorrhagic shock. TVUS: no IUP with hCG > discriminatory zone (1500-3500 mIU/mL).
- **Placental abruption** (`placental-abruption`): third trimester, painful vaginal bleeding, uterine tetany, fetal distress
- **Perforated peptic ulcer** (`perforated-peptic-ulcer`): sudden epigastric pain, rigid abdomen, free air on upright CXR or CT
- **Bowel obstruction** (`bowel-obstruction`): distension, vomiting, obstipation, dilated loops on imaging. Closed-loop obstruction → strangulation → ischemia.
- **Acute pancreatitis** (`acute-pancreatitis`): epigastric pain radiating to back, nausea/vomiting, lipase > 3x ULN. Severe (Ranson, BISAP) → ICU.
- **Sepsis** (`sepsis`): abdominal source (perforation, cholangitis, abscess, SBP) + SIRS + organ dysfunction
- **Aortic dissection** (`aortic-dissection`): tearing pain radiating to back, BP differential, can mimic renal colic or mesenteric ischemia via branch vessel compromise
- **DKA** (`diabetic-ketoacidosis`): diffuse abdominal pain (mimics surgical abdomen), Kussmaul breathing, fruity odor, glucose > 250, anion gap acidosis
- **Acute hepatic failure** (`acute-hepatic-failure`): RUQ pain, jaundice, coagulopathy, encephalopathy
- **Toxic megacolon** (`toxic-megacolon`): IBD or C. diff with distension > 6 cm, systemic toxicity

### Emergent
- **Acute appendicitis** (`acute-appendicitis`): periumbilical → RLQ migration, anorexia, low-grade fever, McBurney point tenderness, Rovsing sign. CT sensitivity 98%.
- **Acute cholecystitis** (`acute-cholecystitis`): RUQ pain, Murphy sign, post-prandial, fever, leukocytosis. US: gallstones + wall thickening + pericholecystic fluid.
- **Ascending cholangitis** (`ascending-cholangitis`): Charcot triad (fever, jaundice, RUQ pain); Reynolds pentad adds AMS + hypotension. ERCP emergently.
- **Incarcerated hernia** (`incarcerated-hernia`): painful, non-reducible bulge at inguinal, femoral, or umbilical site. Risk of strangulation.
- **Ovarian torsion** (`ovarian-torsion`): sudden unilateral pelvic pain, nausea/vomiting, ovarian mass on US with absent Doppler flow. Do NOT rely on Doppler alone (sensitivity 60-70%).
- **Testicular torsion** (`testicular-torsion`): acute testicular pain (may refer to abdomen), absent cremasteric reflex, high-riding testis. < 6 hours for salvage.
- **Splenic/liver laceration** (`splenic-laceration`, `liver-laceration`): post-trauma, LUQ/RUQ pain, hypotension, free fluid on FAST
- **Sigmoid/small bowel volvulus** (`sigmoid-volvulus`, `small-bowel-volvulus`): elderly/debilitated (sigmoid), distension, obstipation, "coffee-bean" sign on X-ray
- **Intussusception** (`intussusception`): pediatric: intermittent colicky abdominal pain, "currant jelly" stool, palpable mass, target sign on US
- **Fournier gangrene** (`fourniers-gangrene`): perineal pain, crepitus, rapidly progressive infection, sepsis. Surgical emergency.
- **SBP** (`spontaneous-bacterial-peritonitis`): ascitic patient (cirrhosis) with fever, abdominal pain, AMS. Diagnostic paracentesis: PMN > 250/mm3.
- **Mesenteric venous thrombosis** (`acute-mesenteric-venous-thrombosis`): subacute abdominal pain, hypercoagulable state, CT with portal/mesenteric vein thrombus

### Urgent
- **Diverticulitis** (`acute-diverticulitis`): LLQ pain, low-grade fever, leukocytosis. CT for complications (abscess, perforation, fistula).
- **Pyelonephritis** (`pyelonephritis`): flank pain, fever, pyuria, CVA tenderness
- **Urolithiasis** (`urolithiasis`): colicky flank-to-groin pain, hematuria, restless patient. CT KUB without contrast.
- **Ischemic colitis** (`ischemic-colitis`): elderly, post-prandial pain, bloody diarrhea, watershed area
- **Ogilvie syndrome** (`ogilvie-syndrome`): acute colonic pseudo-obstruction, massive distension, cecal diameter > 12 cm → risk of perforation

### Non-Emergent
- **Biliary colic** (`biliary-colic`): episodic RUQ pain, post-prandial, resolves within 6 hours, no fever/leukocytosis
- **Viral gastroenteritis** (`viral-gastroenteritis`): nausea, vomiting, diarrhea, diffuse cramping, no peritoneal signs

## Workup

**All patients:**
- CBC, BMP, lipase
- Pregnancy test (all reproductive-age females — mandatory)
- Urinalysis
- Hepatic panel if RUQ pain, jaundice, or biliary symptoms
- Lactate if concern for ischemia or sepsis

**Imaging based on suspicion:**
- **CT abdomen/pelvis with IV contrast:** Gold standard for most acute abdominal pathology. Without oral contrast for appendicitis, with oral for suspected obstruction at some institutions.
- **CT without contrast:** Urolithiasis (CT KUB)
- **CTA abdomen:** Mesenteric ischemia, AAA evaluation
- **Bedside ultrasound (POCUS):** Free fluid (FAST), aortic diameter (AAA), gallstones + Murphy sign, IUP (ectopic pregnancy), renal hydronephrosis
- **Transvaginal ultrasound:** Ectopic pregnancy, ovarian torsion, adnexal pathology
- **Upright CXR or left lateral decubitus:** Free air (perforation)
- **Abdominal X-ray:** Obstruction (air-fluid levels, dilated loops), volvulus ("coffee-bean"), free air (less sensitive than CT)

**Do NOT order:**
- CT with oral contrast and delay imaging hours for "bowel opacification" in a patient with suspected surgical emergency
- Amylase alone for pancreatitis (lipase is more sensitive and specific)

## Treatment

Stabilization while determining etiology:

- **IV fluids:** NS or LR 20-30 mL/kg bolus for dehydration, ongoing losses, or hemodynamic instability
- **Analgesia:** Fentanyl 1 mcg/kg IV or morphine 0.1 mg/kg IV. Ketorolac 15-30 mg IV for renal colic (avoid in GI bleeding or renal insufficiency). Analgesia does NOT delay diagnosis — provide early.
- **Antiemetics:** Ondansetron 4 mg IV
- **NPO:** If surgical intervention likely
- **NG tube:** Decompression for SBO with vomiting, or to assess for upper GI bleeding
- **Broad-spectrum antibiotics** if intra-abdominal infection/sepsis suspected: piperacillin-tazobactam 4.5 g IV or meropenem 1 g IV
- **Blood products:** Type and crossmatch for suspected hemorrhagic causes. Massive transfusion protocol for hemodynamic instability from hemorrhage.

Definitive treatment per specific condition entries.

## Disposition

- **Immediate OR:** Ruptured AAA, ruptured ectopic (unstable), perforated viscus with sepsis, strangulated bowel, Fournier gangrene
- **ICU:** Severe pancreatitis, mesenteric ischemia post-intervention, septic shock from abdominal source, hemorrhagic shock
- **Surgical admission:** Appendicitis, cholecystitis, SBO (non-operative trial), incarcerated hernia, sigmoid volvulus (post-decompression)
- **Medical admission:** Ascending cholangitis (pre-ERCP), pancreatitis requiring IV fluids/pain control, SBP on antibiotics, complicated diverticulitis
- **Observation:** Undifferentiated abdominal pain with concerning labs but stable vitals, biliary colic with elevated LFTs pending imaging
- **Discharge with follow-up (24-48 hours):** Non-complicated diverticulitis (select cases with oral antibiotic tolerance), biliary colic without cholecystitis (surgical follow-up), urolithiasis (pain controlled, < 10 mm stone, no infection), viral gastroenteritis (tolerating PO)

## Pitfalls

1. **Failure to consider ectopic pregnancy.** Every reproductive-age female with abdominal pain requires a pregnancy test before any other workup. "She says she can't be pregnant" is not a substitute for a urine or serum hCG.

2. **Pain out of proportion to exam dismissed as drug-seeking.** Mesenteric ischemia classically presents with severe pain and a benign abdominal exam ("pain out of proportion"). This is a surgical emergency with near 100% mortality if not identified early. Lactate may be normal initially.

3. **Anchoring on abdominal pathology and missing extra-abdominal causes.** Inferior MI, lower lobe pneumonia, DKA, and aortic dissection all present as abdominal pain. Obtain ECG on all patients > 40 with epigastric pain and chest X-ray on patients with upper abdominal pain.

4. **Delaying CT for a "trial of conservative management" in undifferentiated peritonitis.** A patient with peritoneal signs needs imaging and surgical consultation, not serial exams over hours.

5. **Missing testicular torsion in boys/young men with abdominal pain.** Testicular torsion can present as isolated abdominal or inguinal pain without primary testicular complaint. Always examine the testicles in males with abdominal pain.

6. **Relying on Doppler flow to exclude ovarian torsion.** Doppler has 60-70% sensitivity for torsion. Presence of flow does not exclude torsion due to dual blood supply and intermittent torsion/detorsion. Surgical exploration is the definitive test.

7. **Withholding analgesics pending surgical consultation.** Multiple RCTs demonstrate that opioid analgesia does not increase diagnostic error or delay surgical intervention. Withholding pain medication is not evidence-based and is harmful.

8. **"Normal" labs excluding surgical pathology.** White blood cell count is normal in up to 20% of appendicitis. Lipase can be normal in chronic pancreatitis with acute flare. Lactate is a late marker in mesenteric ischemia. Clinical exam and imaging are more important than labs.
