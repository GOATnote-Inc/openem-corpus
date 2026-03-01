---
id: acute-hepatic-failure
condition: Acute Hepatic Failure
aliases: [acute liver failure, ALF, fulminant hepatic failure, fulminant liver failure]
icd10: [K72.0, K72.00, K72.01]
esi: 1
time_to_harm:
  irreversible_injury: "< 24 hours (cerebral edema)"
  death: "< 72 hours without transplant in hyperacute cases"
  optimal_intervention_window: "< 12 hours (NAC, transplant evaluation)"
category: gastrointestinal
track: tier1
sources:
  - type: guideline
    ref: "AASLD Position Paper: The Management of Acute Liver Failure: Update 2011, Hepatology 2012;55(3):965-967"
  - type: guideline
    ref: "AASLD Practice Guidance: Acute-on-Chronic Liver Failure and the Management of Critically Ill Patients with Cirrhosis, Hepatology 2024;79(6):1463-1502"
  - type: guideline
    ref: "Acute Liver Failure Management, Surgical Critical Care Evidence-Based Practice Guideline 2024"
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
# Acute Hepatic Failure

## Recognition

**Definition:**
- Acute onset of hepatic dysfunction (INR ≥ 1.5) with encephalopathy in a patient without pre-existing liver disease
- Illness onset to encephalopathy < 26 weeks
- Hyperacute (< 7 days), acute (7-21 days), subacute (21 days-26 weeks)

**Presentation:**
- Jaundice, malaise, nausea, vomiting
- Rapidly progressive hepatic encephalopathy (confusion → stupor → coma)
- Coagulopathy (bleeding, bruising)
- Right upper quadrant tenderness, hepatomegaly (early) → liver shrinkage (late, ominous)
- Hypoglycemia (impaired gluconeogenesis)

**Common etiologies:**
- Acetaminophen overdose (most common in US/UK — 46%)
- Drug-induced liver injury (antibiotics, anti-epileptics, herbal supplements)
- Viral hepatitis (HAV, HBV, HEV; HSV — high mortality)
- Autoimmune hepatitis
- Wilson disease (acute presentation with hemolytic anemia, Kayser-Fleischer rings)
- Amanita phalloides (mushroom) poisoning
- Budd-Chiari syndrome (acute hepatic vein thrombosis)
- Pregnancy-related (AFLP, HELLP)
- Ischemic hepatitis ("shock liver")

**Hepatic encephalopathy grading (West Haven):**
- Grade 1: altered mood, impaired attention
- Grade 2: lethargy, disorientation, asterixis
- Grade 3: somnolent but arousable, marked confusion
- Grade 4: coma, unresponsive

## Critical Actions

1. **Start N-acetylcysteine (NAC) immediately** — beneficial in ALL ALF, not just acetaminophen:
   - Loading: 150 mg/kg IV in 200 mL D5W over 1 hour
   - Then: 50 mg/kg IV in 500 mL D5W over 4 hours
   - Then: 100 mg/kg IV in 1000 mL D5W over 16 hours
2. **Contact liver transplant center early** — transfer before grade 3 encephalopathy if possible
3. **Check and correct glucose q1-2h** — D10W infusion to maintain glucose > 70 mg/dL
4. **Correct coagulopathy ONLY if actively bleeding or pre-procedure** — INR is a prognostic marker; FFP obscures trends
5. **Intubate for grade 3-4 encephalopathy** — airway protection
6. **Empiric IV acyclovir 10 mg/kg IV q8h** until HSV hepatitis excluded (high mortality if missed)
7. **Broad-spectrum antibiotics** for any sign of infection: piperacillin-tazobactam 4.5 g IV q6h
8. **Head of bed 30 degrees** — reduce intracranial pressure
9. **Avoid lactulose in ALF** — causes bowel distension, interferes with transplant surgery planning; use for chronic hepatic encephalopathy only

## Differential Diagnosis

- **Acute-on-chronic liver failure (ACLF)** — known cirrhosis with acute precipitant (infection, GI bleed, alcohol)
- **Decompensated cirrhosis** — chronic liver disease stigmata, portal hypertension
- **Severe acute hepatitis** — elevated transaminases but preserved synthetic function (INR < 1.5, no encephalopathy)
- **Sepsis with hepatic dysfunction** — source of infection identified, liver dysfunction is secondary
- **Hemophagocytic lymphohistiocytosis (HLH)** — pancytopenia, hyperferritinemia (> 10,000), hepatosplenomegaly
- **Wilson disease** — low ceruloplasmin, high urine copper, Kayser-Fleischer rings, Coombs-negative hemolytic anemia

## Workup

- **Acetaminophen level** (even if patient denies ingestion)
- **Viral hepatitis serologies:** HAV IgM, HBsAg, HBV DNA, anti-HBc IgM, HCV RNA, HEV IgM
- **HSV PCR, CMV PCR, EBV PCR** (especially immunocompromised)
- **Autoimmune markers:** ANA, anti-smooth muscle antibody, IgG levels
- **Wilson workup:** ceruloplasmin, serum copper, urine copper, slit-lamp exam
- **Drug/toxin screen:** urine drug screen, ethanol level, comprehensive toxicology as indicated
- **Labs:** CBC, BMP (glucose, creatinine), hepatic panel (AST, ALT, bilirubin, alkaline phosphatase, albumin), INR/PT, fibrinogen, lactate, ammonia (arterial preferred), lipase, blood type
- **ABG:** assess pH, lactate
- **Imaging:** RUQ ultrasound with Doppler (assess hepatic vein patency — exclude Budd-Chiari; liver size), CT head if grade 3-4 encephalopathy (assess cerebral edema)
- **Factor V level:** < 20% (age < 30) or < 30% (age > 30) — correlates with poor prognosis
- **King's College Criteria (assess transplant need):**
  - Acetaminophen: arterial pH < 7.3 after resuscitation, OR all 3 of (INR > 6.5, creatinine > 3.4, grade 3-4 encephalopathy)
  - Non-acetaminophen: INR > 6.5 regardless of grade, OR any 3 of (age < 10 or > 40, non-A/non-B hepatitis or drug-induced, jaundice > 7 days before encephalopathy, INR > 3.5, bilirubin > 17.5 mg/dL)

## Treatment

**NAC protocol (all ALF):**
- See Critical Actions dosing above
- Continue NAC until INR trending down and clinical improvement

**Acetaminophen-specific:**
- NAC is the definitive treatment
- Activated charcoal 1 g/kg PO if ingestion < 4 hours and patient can protect airway

**Cerebral edema management (grade 3-4 encephalopathy):**
- Intubation with propofol sedation (avoid benzodiazepines — prolonged metabolism)
- Head of bed 30 degrees, midline head position
- Hypertonic saline (23.4%) 30 mL IV bolus or mannitol 0.5-1 g/kg IV for acute ICP crisis
- Target serum sodium 145-155 mEq/L with hypertonic saline (prophylactic hypernatremia)
- Therapeutic hypothermia 33-34°C (if available, as bridge to transplant)
- ICP monitoring: consider for grade 3-4 encephalopathy awaiting transplant (controversial, center-dependent)

**Coagulopathy:**
- Do NOT correct INR with FFP unless active bleeding or pre-procedure
- Vitamin K 10 mg IV daily (exclude deficiency as contributor)
- Platelet transfusion for count < 10,000 or < 50,000 with active bleeding
- Cryoprecipitate for fibrinogen < 100 mg/dL

**Renal support:**
- CRRT preferred over intermittent hemodialysis (hemodynamic stability, ICP management)
- Initiate for grade 2+ encephalopathy with renal dysfunction

**Infection prevention:**
- Low threshold for empiric antibiotics — surveillance cultures
- Piperacillin-tazobactam 4.5 g IV q6h or meropenem 1 g IV q8h
- Fluconazole 400 mg IV daily if fungal infection suspected

**Liver transplantation:**
- Definitive treatment for patients meeting King's College Criteria or MELD ≥ 30
- List as UNOS Status 1A
- Living donor liver transplant or auxiliary liver transplant in select cases

## Disposition

- **ICU admission mandatory** — all patients with ALF
- **Transfer to liver transplant center** before grade 3 encephalopathy — do not delay
- **Multidisciplinary management:** hepatology, transplant surgery, critical care, nephrology
- **Continuous monitoring:** glucose q1-2h, INR/hepatic panel q6-12h, neurologic checks q1-2h
- **Never discharge** — inpatient management until resolution or transplant

## Pitfalls

1. **Failing to start NAC in non-acetaminophen ALF.** NAC improves transplant-free survival in early non-acetaminophen ALF (grades 1-2 encephalopathy). Start empirically in ALL ALF while workup proceeds.

2. **Correcting INR with FFP as routine practice.** INR is a critical prognostic marker and transplant listing criterion. Unnecessary FFP administration obscures trending and creates volume overload. Reserve for active bleeding or procedures.

3. **Not giving empiric acyclovir.** HSV hepatitis carries > 80% mortality if untreated. Acyclovir 10 mg/kg IV q8h should be started empirically while awaiting HSV PCR results.

4. **Using lactulose in ALF.** Unlike chronic hepatic encephalopathy, lactulose has no proven benefit in ALF, causes abdominal distension that complicates transplant surgery, and may worsen electrolyte derangements.

5. **Delayed transfer to transplant center.** Grade 3-4 encephalopathy with cerebral edema makes transfer extremely dangerous. Contact transplant center at time of diagnosis, not after deterioration.

6. **Missing Wilson disease presenting as ALF.** Young patient with Coombs-negative hemolytic anemia, very low alkaline phosphatase, and ALF. Alkaline phosphatase:total bilirubin ratio < 4 and AST:ALT ratio > 2.2 are suggestive. Wilson disease ALF almost always requires emergent transplant.
