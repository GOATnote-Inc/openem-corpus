---
id: acute-pancreatitis
condition: Acute Pancreatitis
aliases: [pancreatitis, acute pancreatic inflammation, gallstone pancreatitis, alcoholic pancreatitis, biliary pancreatitis]
icd10: [K85.90, K85.10, K85.00, K85.20, K85.30]
esi: 2
time_to_harm: "< 6 hours"
mortality_if_delayed: "Mild pancreatitis: <1% mortality; severe necrotizing pancreatitis: 15-30% mortality; organ failure within 48 hours doubles mortality"
category: gastrointestinal
track: tier1
sources:
  - type: guideline
    ref: "ACG 2024 Clinical Guideline: Acute Pancreatitis. Am J Gastroenterol. 2024;119(3):419-437"
  - type: guideline
    ref: "AGA Institute Technical Review on Acute Pancreatitis. Gastroenterology. 2007;132(5):2022-2044"
    pmid: "17484894"
  - type: guideline
    ref: "IAP/APA Evidence-Based Guidelines for the Management of Acute Pancreatitis. Pancreatology. 2013;13(4 Suppl 2):e1-15"
    pmid: "24054878"
  - type: pubmed
    ref: "de-Madaria E, Buxbaum JL, Maisonneuve P, et al. Aggressive or Moderate Fluid Resuscitation in Acute Pancreatitis. N Engl J Med. 2022;387(11):989-1000"
    pmid: "36103415"
last_updated: "2026-02-18"
compiled_by: agent
risk_tier: B
validation:
  automated_consistency_check: "2026-02-18"
  dose_range_validator: "2026-02-19"
  unit_normalization_check: "2026-02-19"
  cross_file_consistency_check: "2026-02-19"
  citation_presence_check: "2026-02-19"
  duplicate_content_check: "2026-02-19"
  outlier_detection_flag: clear
  schema_version: "2.0"
  guideline_version_reference: null
  provenance_links: []
---
# Acute Pancreatitis

## Recognition

### Diagnostic Criteria (2 of 3 Required)
1. **Abdominal pain** consistent with pancreatitis: acute onset, epigastric, severe, radiating to the back
2. **Serum lipase** (or amylase) >= 3x the upper limit of normal
3. **Characteristic findings on imaging** (CT, MRI, or ultrasound)

### Clinical Features
- Severe, constant epigastric pain radiating to the back ("boring" quality)
- Pain worsened by eating, improved by leaning forward
- Nausea, vomiting, anorexia
- Abdominal tenderness with guarding (often less than expected given pain severity)
- Tachycardia, hypotension (from third-spacing and inflammatory mediators)
- Fever (inflammatory response or infection)
- Jaundice (biliary obstruction)

### Etiologies (determine early — drives management)
- **Gallstones:** 40-70% of cases. Elevated ALT >150 U/L has 85% positive predictive value for biliary etiology.
- **Alcohol:** 25-35%. Typically requires >5 years of heavy use (>50 g/day).
- **Hypertriglyceridemia:** Triglycerides >1000 mg/dL; often >2000 mg/dL.
- **Post-ERCP:** 3-10% of ERCPs.
- **Medications:** Valproic acid, azathioprine, GLP-1 agonists, didanosine.
- **Other:** Autoimmune, pancreas divisum, malignancy, trauma, scorpion envenomation.

### Severity Assessment
**Revised Atlanta Classification:**
- **Mild:** No organ failure, no local complications. 80% of cases.
- **Moderately severe:** Transient organ failure (<48 hours) or local complications.
- **Severe:** Persistent organ failure (>48 hours). Mortality 15-30%.

**BISAP Score (at admission):** BUN >25 (1), Impaired mental status (1), SIRS (1), Age >60 (1), Pleural effusion (1). Score >= 3 predicts severe pancreatitis and increased mortality.

**Organ Failure (Modified Marshall Score):**
- Cardiovascular: SBP < 90 despite fluid resuscitation
- Renal: Creatinine >= 1.9 mg/dL
- Respiratory: PaO2/FiO2 < 300

## Critical Actions

| Action | Target |
|---|---|
| IV fluid resuscitation | Initiate within 1 hour; goal-directed |
| Pain control | Within 30 minutes |
| Lipase | STAT at presentation |
| RUQ ultrasound | Within 24 hours (identify gallstones) |
| Severity assessment | BISAP score, organ failure screening at 0 and 48 hours |
| NPO then early oral feeding | Advance diet as tolerated within 24 hours |

1. Establish IV access and begin goal-directed fluid resuscitation with lactated Ringer's
2. Administer analgesia: hydromorphone 0.5-1 mg IV every 3-4 hours or fentanyl 1 mcg/kg IV
3. Send lipase, CBC, BMP, LFTs (ALT, AST, bilirubin, alkaline phosphatase), triglycerides, lactate, calcium
4. Calculate BISAP score
5. Obtain RUQ ultrasound to evaluate for gallstones/biliary dilation
6. Consult GI if biliary obstruction (choledocholithiasis with cholangitis) for urgent ERCP

## Differential Diagnosis

- Perforated peptic ulcer (sudden onset, rigid abdomen, free air on imaging)
- Acute cholecystitis (RUQ pain, Murphy sign, distinct from epigastric focus)
- Acute mesenteric ischemia (pain out of proportion to exam, atrial fibrillation, lactate elevation)
- Bowel obstruction (colicky pain, distension, vomiting, air-fluid levels)
- Myocardial infarction — inferior wall (epigastric pain, diaphoresis, ECG changes)
- Aortic dissection (tearing back pain, pulse deficit, widened mediastinum)
- Ruptured abdominal aortic aneurysm (pulsatile mass, hypotension, back pain)
- Diabetic ketoacidosis (abdominal pain, elevated lipase possible without pancreatitis)

## Workup

- **Lipase:** Preferred over amylase. >= 3x upper limit of normal is diagnostic. Magnitude does NOT correlate with severity. Lipase remains elevated longer than amylase.
- **CBC:** Leukocytosis, hemoconcentration (hematocrit >44% at admission associated with increased risk of necrosis)
- **BMP:** BUN (prognostic marker; >20 mg/dL at admission and rising at 24 hours predicts severity), creatinine, glucose, calcium (hypocalcemia in severe pancreatitis — prognostic)
- **LFTs:** ALT >150 U/L — 85% PPV for gallstone etiology. Bilirubin and alkaline phosphatase elevation suggest biliary obstruction.
- **Triglycerides:** If >1000 mg/dL, likely etiology
- **Lactate:** Tissue hypoperfusion marker
- **Calcium:** Hypocalcemia correlates with severity (Ranson criteria)
- **CRP at 48 hours:** >150 mg/L predicts severe pancreatitis
- **RUQ ultrasound:** First-line for biliary etiology — gallstones, CBD dilation (>6 mm, >8 mm if post-cholecystectomy), pericholecystic fluid
- **CT abdomen/pelvis with IV contrast:** NOT indicated at presentation for diagnosis (2 of 3 criteria suffice). Obtain at 72-96 hours if failing to improve or if complications suspected (necrosis, pseudocyst, abscess). Contrast-enhanced CT identifies necrosis (non-enhancing pancreatic tissue).
- **MRCP:** For suspected choledocholithiasis when ultrasound is equivocal and ERCP is not immediately indicated

## Treatment

### Fluid Resuscitation
- **Lactated Ringer's preferred** over normal saline (reduces SIRS, lower CRP at 24 hours)
- **Goal-directed moderate resuscitation:** 1.5 mL/kg/hour for the first 24 hours (WATERFALL trial, NEJM 2022: aggressive fluids [20 mL/kg bolus + 3 mL/kg/hour] offered no benefit and increased fluid overload)
- Reassess every 6 hours: heart rate, MAP, urine output (target >= 0.5 mL/kg/hour), BUN trend
- Reduce rate if signs of fluid overload (increasing oxygen requirement, pulmonary edema)

### Analgesia
- **Hydromorphone 0.5-1 mg IV every 3-4 hours PRN** (preferred opioid — no active metabolites in renal impairment)
- **Fentanyl 1 mcg/kg IV every 1-2 hours PRN** (alternative, short-acting)
- **Morphine** is acceptable; the theoretical concern about sphincter of Oddi spasm has no clinical evidence of harm
- **Ketorolac 15-30 mg IV every 6 hours** as opioid-sparing adjunct (avoid if AKI or hypovolemia)
- **Acetaminophen 1 g IV every 6 hours** as scheduled baseline

### Nutrition
- **Early oral feeding within 24 hours** when tolerated (low-fat solid diet). Prolonged NPO worsens outcomes by promoting gut barrier dysfunction and bacterial translocation.
- **Enteral nutrition via nasojejunal tube** if unable to tolerate oral intake by 72 hours. Enteral nutrition is superior to parenteral (reduces infection, organ failure, mortality).
- **Total parenteral nutrition** ONLY if enteral route fails or is contraindicated (severe ileus, abdominal compartment syndrome)

### Management of Specific Etiologies
- **Gallstone pancreatitis with cholangitis:** Urgent ERCP within 24 hours
- **Gallstone pancreatitis without cholangitis:** Cholecystectomy during same admission (reduces recurrence from 30-50% to <5%). ERCP only if persistent biliary obstruction.
- **Hypertriglyceridemia-induced:** Insulin infusion (regular insulin 0.1-0.3 units/kg/hour IV) to activate lipoprotein lipase; target triglycerides <500 mg/dL. Plasmapheresis for triglycerides >2000 or refractory to insulin.
- **Alcohol-induced:** Supportive care, monitor for withdrawal, provide thiamine 100 mg IV, folate 1 mg IV

### Infected Necrosis
- Suspect when clinical deterioration after 7-10 days (new fever, rising WBC, organ failure)
- CT finding: gas within necrotic collection is pathognomonic
- **Meropenem 1 g IV every 8 hours** or **imipenem 500 mg IV every 6 hours** (carbapenem penetration into necrotic tissue is superior)
- **Step-up approach:** Percutaneous drainage first, then minimally invasive necrosectomy if drainage fails; open necrosectomy as last resort

### Prophylactic Antibiotics
- **NOT recommended** for sterile necrosis (no mortality benefit, increases resistant organisms)

## Disposition

- **ICU:** Persistent organ failure, hemodynamic instability requiring vasopressors, respiratory failure, severe SIRS, BISAP >= 3
- **Step-down/monitored bed:** Transient organ failure, significant comorbidities, requiring IV PCA for pain
- **General medical floor:** Mild pancreatitis (no organ failure, tolerating fluids), biliary pancreatitis awaiting cholecystectomy
- **Discharge:** Mild pancreatitis with pain controlled on oral medications, tolerating low-fat diet, no organ dysfunction, etiology identified and follow-up arranged. Cholecystectomy scheduling for gallstone pancreatitis before discharge.

## Pitfalls

1. **Ordering CT at presentation for diagnosis.** CT is not needed to diagnose pancreatitis (2 of 3 clinical criteria suffice) and does not show necrosis reliably before 72 hours. Reserve CT for patients not improving at 72-96 hours or when complications are suspected.

2. **Using lipase magnitude to predict severity.** A lipase of 10,000 does not indicate more severe disease than a lipase of 1,000. Severity is determined by organ failure and local complications, not enzyme levels.

3. **Aggressive fluid resuscitation beyond evidence.** The WATERFALL trial (NEJM 2022) demonstrated no benefit of aggressive (20 mL/kg bolus + 3 mL/kg/hour) over moderate (1.5 mL/kg/hour) fluid resuscitation, with increased fluid overload complications in the aggressive group. Use goal-directed moderate resuscitation.

4. **Prolonging NPO status.** Extended fasting promotes bacterial translocation and gut barrier failure. Advance to low-fat oral diet within 24 hours of admission when tolerated. Waiting for lipase normalization or complete pain resolution before feeding is not evidence-based.

5. **Failing to obtain RUQ ultrasound to identify gallstones.** Biliary pancreatitis requires cholecystectomy during the same admission to prevent recurrence (30-50% at 6 weeks if deferred). Identify the etiology early.

6. **Administering prophylactic antibiotics for sterile necrosis.** Multiple RCTs and meta-analyses show no mortality benefit and increased risk of fungal infections and resistant organisms.

7. **Missing infected necrosis.** Clinical deterioration after initial improvement (day 7-10), new fever, rising WBC, and organ failure suggest infected necrosis. CT with gas in necrotic collection is diagnostic. Early percutaneous drainage with antibiotics is first-line.

8. **Not checking triglycerides.** Hypertriglyceridemia is the third most common cause of pancreatitis. Levels must be checked at presentation because they fall rapidly with fasting. Levels >1000 mg/dL require insulin infusion.

9. **Discharging gallstone pancreatitis without cholecystectomy arranged.** Recurrence rate is 30-50% at 6 weeks without cholecystectomy. Same-admission cholecystectomy is the standard for mild gallstone pancreatitis.
