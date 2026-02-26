---
id: acute-cholecystitis
condition: Acute Cholecystitis
aliases: [cholecystitis, gallbladder inflammation, acute calculous cholecystitis, acalculous cholecystitis, emphysematous cholecystitis]
icd10: [K81.0, K81.9, K80.00, K80.01]
esi: 3
time_to_harm: "< 72 hours for perforation/gangrene; acalculous and emphysematous variants progress within 24-48 hours"
mortality_if_delayed: "Overall 1-4%; acalculous cholecystitis 30-50%; emphysematous cholecystitis 15-25%; gangrenous cholecystitis 15-20%"
category: gastrointestinal
track: tier1
sources:
  - type: guideline
    ref: "Yokoe M, et al. Tokyo Guidelines 2018 (TG18): diagnostic criteria and severity grading of acute cholecystitis (with videos). J Hepatobiliary Pancreat Sci. 2018;25(1):41-54"
    pmid: "29032636"
    doi: "10.1002/jhbp.515"
  - type: guideline
    ref: "Okamoto K, et al. Tokyo Guidelines 2018 (TG18): flowchart for the management of acute cholecystitis. J Hepatobiliary Pancreat Sci. 2018;25(1):55-72"
    pmid: "29045062"
    doi: "10.1002/jhbp.516"
  - type: guideline
    ref: "Gomi H, et al. Tokyo Guidelines 2018 (TG18): antimicrobial therapy for acute cholangitis and cholecystitis. J Hepatobiliary Pancreat Sci. 2018;25(1):3-16"
    pmid: "29090866"
    doi: "10.1002/jhbp.518"
  - type: guideline
    ref: "Pisano M, et al. 2020 World Society of Emergency Surgery updated guidelines for the diagnosis and treatment of acute calculus cholecystitis. World J Emerg Surg. 2020;15(1):61"
    pmid: "33153472"
    doi: "10.1186/s13017-020-00336-x"
  - type: meta-analysis
    ref: "Gurusamy KS, et al. Early versus delayed laparoscopic cholecystectomy for people with acute cholecystitis. Cochrane Database Syst Rev. 2013;(6):CD005440"
    pmid: "23813477"
  - type: pubmed
    ref: "Laurila J, et al. Acute acalculous cholecystitis in critically ill patients. Acta Anaesthesiol Scand. 2004;48(8):986-991"
    pmid: "15315616"
  - type: guideline
    ref: "Solomkin JS, et al. Diagnosis and management of complicated intra-abdominal infection in adults and children: guidelines by the Surgical Infection Society and the Infectious Diseases Society of America. Clin Infect Dis. 2010;50(2):133-164"
    pmid: "20034345"
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
# Acute Cholecystitis

## Recognition

### Pathophysiology
Acute calculous cholecystitis (90-95% of cases): cystic duct obstruction by gallstone causes gallbladder distension, wall ischemia, and secondary bacterial infection. Acalculous cholecystitis (5-10%): gallbladder ischemia and bile stasis without stone obstruction, occurring in critically ill, TPN-dependent, or immunocompromised patients. Without treatment, both forms progress to gangrenous cholecystitis, empyema, perforation, and biliary peritonitis.

### Clinical Presentation
- **Right upper quadrant (RUQ) pain:** Constant (not colicky -- distinguishes from biliary colic), lasting > 6 hours, radiating to right scapula or shoulder (Kehr sign from diaphragmatic irritation)
- **Nausea and vomiting:** Present in 60-70%
- **Fever:** Low-grade (38-38.5 degrees C) typical; high fever (> 39 degrees C) suggests empyema, gangrenous cholecystitis, or concurrent cholangitis
- **Murphy sign:** Inspiratory arrest during palpation of RUQ. Sensitivity 65%, specificity 87% for acute cholecystitis. Absent in elderly, diabetics, and patients on analgesics.
- **Guarding and rebound:** Suggest peritoneal irritation from perforation or gangrenous cholecystitis

### Tokyo Guidelines 2018 (TG18) -- Diagnostic Criteria
**A. Local signs of inflammation:**
1. Murphy sign
2. RUQ mass/pain/tenderness

**B. Systemic signs of inflammation:**
1. Fever (> 38 degrees C)
2. Elevated CRP (>= 1 mg/dL)
3. Elevated WBC (> 10,000/mm3)

**C. Imaging findings characteristic of acute cholecystitis:**
Gallbladder wall thickening (> 4 mm), pericholecystic fluid, sonographic Murphy sign, gallbladder distension (long axis > 8 cm, short axis > 4 cm), gallbladder wall edema/stranding, impacted gallstone in cystic duct

**Suspected diagnosis:** One item in A + one item in B
**Definite diagnosis:** One item in A + one item in B + C

### TG18 Severity Grading

| Grade | Criteria | Clinical Significance |
|---|---|---|
| **Grade I (Mild)** | Does not meet Grade II or III criteria; no organ dysfunction; mild inflammatory changes in gallbladder | Safe for early laparoscopic cholecystectomy in most patients |
| **Grade II (Moderate)** | Any of: WBC > 18,000, palpable RUQ mass, symptom duration > 72 hours, marked local inflammation (gangrenous cholecystitis, pericholecystic abscess, hepatic abscess, biliary peritonitis, emphysematous cholecystitis) | Requires experienced surgeon; may need gallbladder drainage first if surgery not feasible |
| **Grade III (Severe)** | Organ dysfunction: cardiovascular (hypotension requiring vasopressors), neurologic (altered mental status), respiratory (PaO2/FiO2 < 300), renal (creatinine > 2 mg/dL), hepatic (INR > 1.5), hematologic (platelets < 100,000) | Organ support + gallbladder drainage (percutaneous cholecystostomy); cholecystectomy after recovery |

### Variants

**Acalculous Cholecystitis:**
- 5-10% of acute cholecystitis; 30-50% mortality (patients are critically ill at baseline)
- Risk factors: ICU stay, TPN, major surgery, burns, trauma, sepsis, HIV/AIDS, bone marrow transplant, vasculitis, diabetes
- Pathogenesis: gallbladder ischemia from hypoperfusion and bile stasis (opioids, fasting, positive-pressure ventilation)
- Diagnosis difficult: patients are often sedated, intubated, unable to report symptoms. Unexplained sepsis in ICU patient warrants RUQ ultrasound.
- HIDA scan has higher sensitivity than ultrasound for acalculous cholecystitis (sensitivity 90-97% vs 50-70%)
- Treatment: percutaneous cholecystostomy preferred in unstable ICU patients; cholecystectomy when feasible

**Emphysematous Cholecystitis:**
- Gas-forming organisms (Clostridium perfringens, E. coli, Klebsiella) infect gallbladder wall
- 50% of patients are diabetic; male predominance (5:1)
- Mortality 15-25% (5x higher than uncomplicated cholecystitis)
- Imaging: gas in gallbladder wall or lumen on CT (most sensitive), plain radiograph, or ultrasound (dirty shadowing, effervescent gallbladder)
- Treatment: emergent cholecystectomy; do not delay for percutaneous drainage. Broad-spectrum antibiotics including anaerobic coverage.

**Gangrenous Cholecystitis:**
- Necrosis of gallbladder wall; complicates 2-30% of acute cholecystitis
- Risk factors: diabetes, age > 50, male sex, WBC > 15,000, delayed presentation > 72 hours
- Imaging: absent or irregular gallbladder wall enhancement on contrast-enhanced CT, intraluminal membranes on ultrasound, pericholecystic stranding
- Murphy sign is often absent (denervation of necrotic wall) -- this is a pitfall
- High perforation risk; requires urgent cholecystectomy

## Critical Actions

| Action | Target |
|---|---|
| RUQ ultrasound | Within 2 hours of presentation |
| IV antibiotics (Grade II-III) | Within 1 hour of recognition |
| Surgical consult | Within 4 hours for all suspected cholecystitis |
| Percutaneous cholecystostomy (Grade III, non-surgical candidate) | Within 24 hours |
| Early laparoscopic cholecystectomy (Grade I-II) | Within 72 hours of symptom onset |
| Pain management | Immediately |

1. Establish IV access and obtain STAT labs: CBC with differential, CMP (including total and direct bilirubin, ALP, ALT, AST), lipase, lactate, INR, blood type and screen.
2. RUQ ultrasound to evaluate for gallstones, gallbladder wall thickening, pericholecystic fluid, sonographic Murphy sign, and common bile duct diameter (to rule out concurrent choledocholithiasis/cholangitis).
3. Start empiric IV antibiotics for Grade II-III cholecystitis or any patient with systemic inflammatory response. Grade I with mild local inflammation may be managed with supportive care and early cholecystectomy alone.
4. Provide IV analgesia. Do not withhold opioids based on outdated concerns about sphincter of Oddi spasm.
5. IV fluid resuscitation with Ringer's lactate. Aggressive volume resuscitation (30 mL/kg bolus) if septic.
6. Consult surgery early. Early laparoscopic cholecystectomy (within 72 hours) is the definitive treatment for Grade I-II cholecystitis.
7. For Grade III with organ dysfunction: ICU admission, organ support, and percutaneous cholecystostomy if the patient is not a surgical candidate. Cholecystectomy after clinical improvement.

## Differential Diagnosis

| Condition | Distinguishing Features |
|---|---|
| **Biliary colic** | Episodic, colicky RUQ pain lasting < 6 hours; resolves spontaneously; no fever, no leukocytosis, no gallbladder wall thickening; negative Murphy sign |
| **Ascending cholangitis** | Charcot triad (fever, jaundice, RUQ pain); Reynolds pentad adds hypotension and altered mental status; CBD dilation on ultrasound; conjugated hyperbilirubinemia and elevated ALP/GGT prominent; jaundice more common than in cholecystitis |
| **Acute pancreatitis** | Epigastric pain radiating to back; lipase > 3x upper limit of normal; may coexist with cholecystitis (gallstone pancreatitis) |
| **Peptic ulcer disease / perforation** | Epigastric pain; free air on upright CXR or CT if perforated; no gallbladder wall thickening |
| **Acute hepatitis** | Transaminases > 1,000 IU/L (much higher than cholecystitis); hepatomegaly; risk factors (viral exposure, alcohol, medications) |
| **Acute appendicitis (high-riding cecum)** | RLQ pain typical, but can present as RUQ pain with retrocecal or subhepatic appendix; CT distinguishes |
| **Right lower lobe pneumonia** | Referred RUQ pain from diaphragmatic irritation; cough, pleuritic component; CXR abnormal |
| **Fitz-Hugh-Curtis syndrome** | Perihepatitis from PID; young women; RUQ pain with elevated ESR; cervical motion tenderness on pelvic exam |
| **Renal colic (right)** | Flank pain radiating to groin; hematuria; no gallbladder findings on ultrasound; CT KUB shows ureteral stone |

## Workup

### Laboratory Studies
- **CBC with differential:** Leukocytosis (WBC > 10,000); WBC > 18,000 suggests Grade II severity or complicated cholecystitis (gangrenous, emphysematous, perforation)
- **CMP:** Mildly elevated transaminases (AST/ALT typically < 5x normal). ALP and GGT mildly elevated. Markedly elevated ALP/GGT or direct bilirubin suggests concurrent choledocholithiasis or cholangitis -- evaluate CBD.
- **Total and direct bilirubin:** Mild elevation possible from Mirizzi syndrome or adjacent inflammation. Direct bilirubin > 4 mg/dL suggests CBD obstruction, not simple cholecystitis.
- **Lipase:** Order to rule out concurrent gallstone pancreatitis. Lipase > 3x upper limit of normal = acute pancreatitis.
- **Lactate:** Elevated lactate suggests sepsis, gangrenous cholecystitis, or perforation.
- **INR:** Baseline; prolonged in severe sepsis or hepatic dysfunction.
- **CRP:** Elevated; supports TG18 diagnostic criteria (>= 1 mg/dL). CRP > 10 mg/dL associated with complicated cholecystitis.
- **Blood cultures:** Obtain 2 sets (aerobic + anaerobic) before antibiotics if febrile, septic, or Grade II-III. Positive in 15-30% of acute cholecystitis (lower than cholangitis).
- **Blood type and screen:** Anticipate surgical intervention.
- **Pregnancy test:** All females of reproductive age; alters imaging and surgical planning.

### Imaging

**RUQ Ultrasound (first-line):**
- Sensitivity 88%, specificity 80% for acute cholecystitis
- Findings: gallstones (hyperechoic foci with posterior acoustic shadowing), gallbladder wall thickening > 4 mm (> 3 mm if non-distended), pericholecystic fluid, gallbladder distension, sonographic Murphy sign (focal tenderness directly over the gallbladder under ultrasound probe -- more specific than clinical Murphy sign)
- Assess CBD diameter: > 6 mm (> 8 mm postcholecystectomy) suggests concurrent choledocholithiasis
- Emphysematous cholecystitis: echogenic foci with dirty shadowing or "effervescent" pattern from intramural gas

**CT Abdomen/Pelvis with IV Contrast:**
- Indicated when: ultrasound equivocal, concern for complications (perforation, abscess, emphysematous cholecystitis), alternative diagnosis suspected
- Findings: gallbladder wall thickening and enhancement, pericholecystic fat stranding, pericholecystic fluid, gallbladder distension
- Most sensitive for: emphysematous cholecystitis (gas in gallbladder wall), gangrenous cholecystitis (absent wall enhancement, intraluminal membranes), perforation (contained fluid collection, free fluid), abscess
- Less sensitive than ultrasound for gallstone detection (misses non-calcified stones)

**HIDA Scan (Hepatobiliary Iminodiacetic Acid Scintigraphy):**
- Sensitivity 90-97%, specificity 71-90% for acute cholecystitis
- Indicated when ultrasound is equivocal and clinical suspicion remains high
- Positive result: non-visualization of gallbladder at 60 minutes after radiotracer injection (cystic duct obstruction). Can confirm with morphine augmentation (morphine 0.04 mg/kg IV) to increase sphincter of Oddi tone and promote gallbladder filling -- if still non-filling at 30 minutes post-morphine, positive for cholecystitis.
- Superior to ultrasound for acalculous cholecystitis
- Limitation: takes 1-4 hours; do not delay surgical consultation for HIDA if clinical picture is clear

**MRCP:**
- Not first-line for cholecystitis. Reserve for evaluating CBD stones when ultrasound shows CBD dilation or LFTs suggest choledocholithiasis.

## Treatment

### Empiric Antibiotics

Antibiotics are indicated for Grade II-III cholecystitis, all cases with systemic signs of infection, and perioperatively. Grade I cholecystitis undergoing early cholecystectomy (within 24 hours) may require only perioperative prophylaxis.

**Community-acquired, Grade I-II:**
- Piperacillin-tazobactam 4.5 g IV q6h
- OR ceftriaxone 2 g IV q24h + metronidazole 500 mg IV q8h
- OR ampicillin-sulbactam 3 g IV q6h

**Grade III or healthcare-associated:**
- Piperacillin-tazobactam 4.5 g IV q6h (extended infusion over 4 hours preferred in sepsis)
- OR meropenem 1 g IV q8h (if ESBL risk or prior antibiotic failure)
- Add vancomycin 25-30 mg/kg IV loading dose if MRSA risk factors

**Penicillin allergy:**
- Ciprofloxacin 400 mg IV q12h + metronidazole 500 mg IV q8h
- OR aztreonam 2 g IV q8h + metronidazole 500 mg IV q8h + vancomycin 25-30 mg/kg IV

**Duration:** Discontinue within 24 hours after cholecystectomy for uncomplicated cholecystitis. Continue 4-7 days if perforation, abscess, empyema, or positive blood cultures.

**Microbiology:** E. coli (most common, 40-60%), Klebsiella (15-20%), Enterococcus (10-15%), Enterobacter, Bacteroides (10-15%), Clostridium (emphysematous variant). Polymicrobial in 30-50%.

### Surgical Management

**Early Laparoscopic Cholecystectomy (definitive treatment):**
- **Grade I:** Early laparoscopic cholecystectomy within 72 hours of symptom onset. Same-admission surgery preferred. The Cochrane review (Gurusamy 2013) and WSES 2020 guidelines demonstrate that early cholecystectomy is safe and reduces total hospital stay by 4 days with no increase in complications or conversion rate compared to delayed surgery.
- **Grade II:** Early laparoscopic cholecystectomy by an experienced surgeon if CCI <= 5 and ASA-PS <= 2. If the patient does not meet these criteria, gallbladder drainage followed by delayed cholecystectomy.
- **Grade III:** Organ support first. Percutaneous cholecystostomy for source control. Cholecystectomy after clinical recovery (typically 6-8 weeks).

**Subtotal (partial) cholecystectomy:** Safe bailout option when the critical view of safety cannot be achieved due to severe inflammation, Mirizzi syndrome, or distorted anatomy. Reduces bile duct injury risk.

**Intraoperative cholangiography or laparoscopic ultrasound:** Indicated if preoperative imaging suggests choledocholithiasis (elevated bilirubin, dilated CBD).

### Percutaneous Cholecystostomy

- Indicated for: Grade III cholecystitis with organ dysfunction, patients unfit for general anesthesia (ASA IV-V), acalculous cholecystitis in ICU patients
- Interventional radiology places a transhepatic pigtail catheter into the gallbladder under ultrasound or CT guidance
- Clinical improvement expected within 24-48 hours; if no improvement, reassess diagnosis (gangrenous gallbladder may require surgery despite risk)
- Catheter remains until tract matures (typically 3-6 weeks); follow-up cholangiogram before removal
- Bridge to interval cholecystectomy when patient recovers

### Pain Management
- Morphine 0.1 mg/kg IV q2-4h or hydromorphone 0.5-1 mg IV q3-4h
- Ketorolac 15-30 mg IV once (avoid if renal dysfunction, coagulopathy, or concurrent anticoagulation)
- Avoid meperidine (no evidence it causes less sphincter of Oddi spasm than other opioids; worse side effect profile)
- Ondansetron 4 mg IV for nausea/vomiting
- NPO status in anticipation of surgery

### Hemodynamic Support (Grade III)
- IV crystalloid resuscitation: Ringer's lactate 30 mL/kg bolus for sepsis-induced hypotension
- Norepinephrine 0.05-0.5 mcg/kg/min IV for vasopressor-dependent shock (MAP target >= 65 mmHg)

## Disposition

**Admission (all patients with confirmed acute cholecystitis):**
- **Grade I:** Surgical floor admission. Early laparoscopic cholecystectomy within 72 hours. NPO, IV fluids, pain management, perioperative antibiotics.
- **Grade II:** Surgical floor with telemetry. IV antibiotics. Surgical planning based on patient fitness and local expertise. Serial exams for clinical deterioration.
- **Grade III:** ICU admission. Organ support. Percutaneous cholecystostomy if not a surgical candidate. Transfer to a facility with surgical and interventional radiology capability if not available locally.

**Discharge from ED (narrow criteria -- biliary colic, NOT cholecystitis):**
- If workup excludes acute cholecystitis (normal WBC, normal ultrasound, no Murphy sign, no fever) and final diagnosis is biliary colic: may discharge with surgical follow-up within 2 weeks for elective cholecystectomy, PO analgesics, dietary counseling (low-fat diet), and strict return precautions.
- Never discharge a patient with confirmed acute cholecystitis from the ED.

**Transfer Criteria:**
- Facility lacks surgical capability for laparoscopic cholecystectomy
- Facility lacks interventional radiology for percutaneous cholecystostomy (Grade III patients)
- Start antibiotics and IV fluids before transfer

**Postoperative Monitoring:**
- Standard post-laparoscopic monitoring (4-6 hours)
- Watch for bile duct injury (incidence 0.3-0.6%): rising bilirubin, persistent RUQ pain, bilious drain output
- Post-cholecystectomy syndrome: recurrent RUQ pain from retained CBD stone, sphincter of Oddi dysfunction, or bile leak

## Pitfalls

1. **Confusing biliary colic with acute cholecystitis.** Biliary colic resolves within 6 hours and has no inflammatory signs. Pain lasting > 6 hours with fever, leukocytosis, or positive Murphy sign is cholecystitis, not colic. This distinction determines admission vs discharge and changes management entirely.

2. **Relying on Murphy sign in elderly and diabetic patients.** Murphy sign sensitivity drops below 50% in patients over age 65 and in diabetics with neuropathy. Gangrenous cholecystitis presents with absent Murphy sign due to gallbladder wall denervation. A negative Murphy sign does not exclude cholecystitis -- use imaging and laboratory data.

3. **Delaying cholecystectomy past 72 hours.** Evidence from the Cochrane review and WSES 2020 guidelines demonstrates that early laparoscopic cholecystectomy (within 72 hours of symptom onset) is safe, shortens total hospital stay, and does not increase conversion rates or complications compared to delayed surgery. The traditional practice of cooling down with antibiotics and performing interval cholecystectomy at 6-8 weeks is inferior for Grade I-II disease.

4. **Missing acalculous cholecystitis in the ICU patient.** Acalculous cholecystitis accounts for 5-10% of cases but carries 30-50% mortality. ICU patients on TPN, vasopressors, or mechanical ventilation who develop unexplained sepsis, rising WBC, or new RUQ tenderness need RUQ ultrasound. Absence of gallstones does not exclude cholecystitis. HIDA scan is more sensitive than ultrasound for this variant.

5. **Failing to recognize emphysematous cholecystitis.** Gas in the gallbladder wall on CT is diagnostic. Diabetic patients are disproportionately affected (50% of cases). Mortality is 15-25%. This is a surgical emergency requiring urgent cholecystectomy, not percutaneous drainage. Empiric antibiotics must cover anaerobes (Clostridium perfringens).

6. **Attributing elevated bilirubin to cholecystitis alone.** Acute cholecystitis causes only mild bilirubin elevation (< 4 mg/dL) from adjacent inflammation. Direct bilirubin > 4 mg/dL, markedly elevated ALP/GGT, or CBD dilation > 6 mm on ultrasound suggest concurrent choledocholithiasis or ascending cholangitis. Missing this distinction delays ERCP and risks biliary sepsis.

7. **Choosing meperidine over other opioids for "sphincter of Oddi concerns."** The claim that meperidine causes less sphincter of Oddi spasm is not supported by evidence. Use standard opioid analgesics (morphine, hydromorphone). Do not withhold analgesia based on this myth.

8. **Discharging with antibiotics alone and no surgical follow-up.** Antibiotics treat secondary infection but do not address the underlying pathology. Without cholecystectomy, recurrence rate is 30% within 3 months and 60% within 2 years. Every patient discharged after biliary colic needs surgical referral for elective cholecystectomy within 2 weeks.

9. **Missing gallstone pancreatitis.** Always check lipase in patients with cholecystitis. Gallstone pancreatitis coexists in 5-8% of cholecystitis presentations. Lipase > 3x upper limit of normal changes the diagnosis, disposition, and need for ERCP if CBD stone is suspected.

10. **Using ultrasound alone to exclude complicated cholecystitis.** Ultrasound has limited sensitivity for gangrenous cholecystitis, perforation, and emphysematous cholecystitis. If the patient has high fever, marked leukocytosis (WBC > 18,000), or signs of sepsis with a non-diagnostic ultrasound, obtain CT abdomen/pelvis with IV contrast to evaluate for complications.
