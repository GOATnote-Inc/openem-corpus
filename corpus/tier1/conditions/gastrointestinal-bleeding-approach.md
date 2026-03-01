---
id: gastrointestinal-bleeding-approach
condition: "Gastrointestinal Bleeding — Emergency Evaluation"
aliases: [GI bleed, GI hemorrhage, upper GI bleed, lower GI bleed, hematemesis, melena, hematochezia, bloody stool, vomiting blood, rectal bleeding]
icd10: [K92.2, K92.1, K92.0, K62.5]
esi: 2
time_to_harm:
  irreversible_injury: "< 2 hours (hemorrhagic shock with end-organ damage)"
  death: "< 1 hour (massive hemorrhage from variceal bleed or aortoenteric fistula)"
  optimal_intervention_window: "< 60 minutes (resuscitation, endoscopy within 24 hours for most)"
category: presentations
condition_type: presentation
chief_complaint: "GI Bleeding"
differential_categories:
  - category: life-threatening
    conditions:
      - gi-hemorrhage
      - hemorrhagic-shock
      - ruptured-aaa
      - aortic-dissection
      - spontaneous-bacterial-peritonitis
  - category: emergent
    conditions:
      - perforated-peptic-ulcer
      - mallory-weiss-tear
      - bowel-obstruction
      - ischemic-colitis
      - acute-hepatic-failure
      - toxic-megacolon
      - acute-mesenteric-venous-thrombosis
      - mesenteric-ischemia
      - acute-pancreatitis
  - category: urgent
    conditions:
      - acute-diverticulitis
      - sigmoid-volvulus
      - incarcerated-hernia
      - splenic-laceration
  - category: non-emergent
    conditions: []
red_flags:
  - "Hematemesis (bright red or coffee-ground emesis)"
  - "Hemodynamic instability (HR > 100, SBP < 90, orthostatic changes)"
  - "Ongoing bright red blood per rectum with hemodynamic changes"
  - "Syncope or near-syncope"
  - "Anticoagulation use (warfarin, DOACs, heparin)"
  - "Liver disease/cirrhosis (variceal hemorrhage risk)"
  - "Known AAA or prior aortic graft (aortoenteric fistula)"
  - "Hemoglobin < 7 g/dL"
  - "Coagulopathy (INR > 1.5, platelets < 50,000)"
  - "Maroon stool or melena with tachycardia (significant upper or mid-GI source)"
decision_rules:
  - name: "Glasgow-Blatchford Score (GBS)"
    citation: "Blatchford O et al. A risk score to predict need for treatment for upper-gastrointestinal haemorrhage. Lancet. 2000;356(9238):1318-1321."
    pmid: "11073021"
  - name: "Rockall Score"
    citation: "Rockall TA et al. Risk assessment after acute upper gastrointestinal haemorrhage. Gut. 1996;38(3):316-321."
    pmid: "8675081"
track: tier1
sources:
  - type: guideline
    ref: "ACG Clinical Guideline: Upper Gastrointestinal and Ulcer Bleeding. Am J Gastroenterol. 2021;116(5):899-917."
    pmid: "33929377"
  - type: guideline
    ref: "ACG Clinical Guideline: Management of Patients With Acute Lower Gastrointestinal Bleeding. Am J Gastroenterol. 2016;111(4):459-474."
    pmid: "26925883"
  - type: guideline
    ref: "2022 AASLD Practice Guidance: Prevention and Management of Gastroesophageal Varices and Variceal Hemorrhage in Cirrhosis."
  - type: guideline
    ref: "International Consensus Recommendations on the Management of Patients With Nonvariceal Upper Gastrointestinal Bleeding. Ann Intern Med. 2010;152(2):101-113."
    pmid: "20083829"
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
# Gastrointestinal Bleeding — Emergency Evaluation

## Recognition

GI bleeding accounts for approximately 300,000 US hospitalizations annually. The ED priorities are: (1) assess severity and hemodynamic status, (2) resuscitate, (3) localize the source (upper vs lower), (4) identify high-risk patients, and (5) facilitate appropriate endoscopic or surgical intervention.

**Upper vs lower GI bleeding:**
- **Upper GI (proximal to ligament of Treitz):** hematemesis (bright red or coffee-ground), melena (black tarry stool — requires only 50-100 mL blood in upper GI tract), NG aspirate positive for blood. 80% of acute GI bleeds are upper.
- **Lower GI (distal to ligament of Treitz):** hematochezia (bright red blood per rectum), maroon stool. However, brisk upper GI bleed can cause hematochezia (15% of cases) — do NOT assume lower source based on hematochezia alone.
- **Occult/chronic:** iron deficiency anemia, positive fecal occult blood, fatigue

**Key historical elements:**
- Character of bleeding: hematemesis, coffee-ground, melena, hematochezia, maroon stool
- Onset and duration: acute single episode vs recurrent vs chronic
- Volume estimate: number of episodes, teaspoon vs cup vs toilet bowl (patient estimates are unreliable — assess hemodynamics instead)
- Associated symptoms: abdominal pain (PUD, ischemia), painless bleeding (diverticulum, AVM, varices), dysphagia (esophageal source), weight loss (malignancy)
- NSAID or aspirin use (PUD)
- Anticoagulation: warfarin, DOACs, heparin, dual antiplatelet therapy
- Alcohol use and liver disease history (variceal hemorrhage, coagulopathy)
- Prior GI bleeding episodes and their causes
- Prior aortic surgery or known AAA (aortoenteric fistula — "herald bleed" → massive hemorrhage)
- Recent vomiting or retching (Mallory-Weiss tear, Boerhaave syndrome)

**Volume status assessment:**
- Resting tachycardia (HR > 100): suggests > 15% blood volume loss
- Orthostatic hypotension: suggests > 15-30% loss
- Supine hypotension (SBP < 90): suggests > 30-40% loss
- Altered mental status, anuria: suggests > 40% loss (Class IV hemorrhagic shock)

## Critical Actions

| Action | Target |
|---|---|
| IV access (2 large-bore, >= 18G) | < 5 minutes |
| Type and crossmatch | < 15 minutes |
| Hemoglobin/hematocrit | < 15 minutes |
| Resuscitation initiated | < 15 minutes |
| GI consultation | < 60 minutes for hemodynamically significant bleeding |
| Endoscopy | < 24 hours (most UGIB); < 12 hours (variceal bleed) |

**Evaluation algorithm:**

1. **Assess hemodynamic status immediately.** Two large-bore peripheral IVs (18G or larger, antecubital preferred). If unable to obtain peripheral access → IO or central venous access.

2. **Resuscitate before localizing source:**
   - Crystalloid (NS or LR) 1-2 L bolus
   - Type and crossmatch for 4+ units pRBC
   - Transfuse pRBC if: hemodynamically unstable, Hgb < 7 g/dL (restrictive strategy in stable patients per TRICC and TRIGGER trials), active ongoing hemorrhage, or symptomatic anemia with cardiac comorbidities
   - Massive transfusion protocol (1:1:1 pRBC:FFP:platelets) if hemorrhagic shock

3. **Determine upper vs lower source:**
   - Hematemesis or coffee-ground emesis → upper GI (no further localization needed)
   - Melena → upper GI in 90%+ of cases (can occasionally be small bowel or right colon)
   - Hematochezia → lower GI most commonly, BUT brisk upper GI bleed in 15%
   - NG aspirate: bloody or coffee-ground → confirms upper source. Clear aspirate does NOT exclude upper source (duodenal bleed distal to closed pylorus).
   - BUN/Cr ratio > 30:1 suggests upper GI source (digested blood acts as protein load)

4. **Risk stratify:**
   - **Glasgow-Blatchford Score (GBS):** Validated for pre-endoscopic risk assessment. Score 0 → very low risk, may not require admission. Score >= 1 → requires inpatient evaluation.
   - Components: BUN, hemoglobin, systolic BP, pulse, melena, syncope, hepatic disease, cardiac failure
   - GBS 0: < 1% chance of needing intervention → consider discharge with outpatient endoscopy within 24-48 hours (Level B evidence)

5. **Specific considerations by suspected source:**
   - Variceal hemorrhage (liver disease, stigmata of portal hypertension): IV octreotide 50 mcg bolus then 50 mcg/hr infusion, IV ceftriaxone 1 g (antibiotic prophylaxis reduces mortality), emergent EGD within 12 hours, Sengstaken-Blakemore tube if massive hemorrhage unresponsive to endoscopy
   - Aortoenteric fistula (prior aortic surgery + GI bleed): CTA abdomen, vascular surgery consultation immediately. "Herald bleed" (small initial bleed followed hours-days later by massive exsanguination) — maintain high suspicion
   - PUD: IV PPI (pantoprazole 80 mg bolus then 8 mg/hr infusion per some guidelines; others use 40 mg BID IV — both approaches reduce rebleeding)

## Differential Diagnosis

### Life-Threatening
- **Massive upper GI hemorrhage** (`gi-hemorrhage`): esophageal varices (cirrhosis, portal HTN), bleeding PUD (posterior duodenal ulcer eroding into gastroduodenal artery), aortoenteric fistula (prior aortic graft), Dieulafoy lesion (aberrant submucosal artery)
- **Hemorrhagic shock** (`hemorrhagic-shock`): from any GI source — the clinical syndrome rather than the source. Class III-IV hemorrhagic shock requires massive transfusion.
- **Ruptured AAA** (`ruptured-aaa`): can present as GI bleed via aortoenteric erosion. Any patient with prior aortic surgery and GI bleed → aortoenteric fistula until proven otherwise.
- **Aortic dissection** (`aortic-dissection`): mesenteric branch vessel compromise can cause ischemic colitis with bloody stool
- **SBP** (`spontaneous-bacterial-peritonitis`): cirrhotic patient with variceal bleed often has or develops SBP

### Emergent
- **Perforated peptic ulcer** (`perforated-peptic-ulcer`): may bleed then perforate — pain, peritoneal signs, free air
- **Mallory-Weiss tear** (`mallory-weiss-tear`): post-emetic hematemesis, usually self-limited but can be massive
- **Bowel obstruction** (`bowel-obstruction`): closed-loop obstruction with strangulation can cause bloody stool
- **Ischemic colitis** (`ischemic-colitis`): bloody diarrhea in elderly, often watershed distribution, crampy abdominal pain
- **Acute hepatic failure** (`acute-hepatic-failure`): coagulopathy causing or worsening GI hemorrhage
- **Toxic megacolon** (`toxic-megacolon`): bloody diarrhea with colonic dilation, IBD or C. diff
- **Mesenteric venous thrombosis** (`acute-mesenteric-venous-thrombosis`): abdominal pain with bloody stool, hypercoagulable state
- **Mesenteric ischemia** (`mesenteric-ischemia`): pain out of proportion with eventual bloody stool (late finding)

### Urgent
- **Diverticular bleeding** (`acute-diverticulitis`): painless massive hematochezia, typically self-limited (80%), more common in right colon. Most common cause of lower GI bleed.
- **Sigmoid volvulus** (`sigmoid-volvulus`): distension, obstipation, may have bloody stool if ischemic
- **Incarcerated hernia** (`incarcerated-hernia`): strangulated hernia → ischemic bowel → bloody stool

### Non-Emergent
- **Hemorrhoids:** bright red blood per rectum on toilet paper or dripping into bowl, painless (internal) or painful with thrombosis (external). Most common cause of rectal bleeding in outpatients. Diagnosis of exclusion in ED — do NOT anchor.
- **Anal fissure:** painful bright red rectal bleeding with bowel movements
- **Inflammatory bowel disease flare:** bloody diarrhea, crampy abdominal pain, known IBD history
- **Angiodysplasia (AVM):** painless rectal bleeding, elderly, associated with aortic stenosis (Heyde syndrome) and renal failure

## Workup

**All patients:**
- CBC (hemoglobin — but NOTE: initial hemoglobin may be normal in acute hemorrhage before equilibration, which takes 6-24 hours)
- BMP (BUN/Cr ratio > 30 suggests upper source)
- Coagulation studies: INR, PT, PTT
- Type and crossmatch (at minimum type and screen)
- Hepatic panel (if liver disease suspected)
- Lactate (tissue hypoperfusion marker)

**Source localization:**
- **NG aspirate/lavage:** Controversial — declining in routine use. Positive (bloody or coffee-ground) confirms upper source. Negative (clear) does NOT exclude upper source. May be useful if hematochezia with hemodynamic instability (to evaluate for upper source).
- **EGD (upper endoscopy):** Diagnostic and therapeutic for upper GI bleed. Within 24 hours for most. Within 12 hours for variceal hemorrhage or hemodynamically significant bleed. After resuscitation — endoscopy on an exsanguinating patient without resuscitation increases mortality.
- **Colonoscopy:** For hemodynamically stable lower GI bleed, typically after rapid bowel prep. Not emergent in most cases.
- **CTA abdomen/pelvis:** For hemodynamically significant lower GI bleed (active extravasation seen at rate > 0.3-0.5 mL/min). Also for aortoenteric fistula evaluation.
- **Tagged RBC scan:** More sensitive for slow bleeds (detects 0.1 mL/min), but less precise anatomic localization than CTA.
- **Angiography:** Diagnostic and therapeutic (embolization). For ongoing hemorrhage not controlled by endoscopy.

**Rectal examination:** Mandatory. Assess stool color (melena vs maroon vs red vs brown), hemorrhoids, masses, fissure.

## Treatment

**Resuscitation:**
- 2 large-bore IVs (>= 18G), NS or LR bolus 1-2 L
- pRBC transfusion: Hgb target >= 7 g/dL (restrictive strategy). Target >= 9 g/dL in patients with active cardiac disease or hemodynamically unstable.
- Massive transfusion protocol (1:1:1 pRBC:FFP:platelets) for hemorrhagic shock or > 4 units pRBC anticipated
- Platelets if < 50,000/mm3 with active bleeding
- FFP if INR > 1.5 with active bleeding

**Anticoagulation reversal (for life-threatening hemorrhage):**
- Warfarin: 4-factor PCC (25-50 units/kg IV — faster and more effective than FFP) + vitamin K 10 mg IV
- DOACs (apixaban, rivaroxaban): andexanet alfa (if available) or 4-factor PCC 50 units/kg
- Dabigatran: idarucizumab 5 g IV
- Heparin: protamine sulfate 1 mg per 100 units of heparin given in last 2-3 hours

**Source-specific treatment:**
- **Variceal hemorrhage:** Octreotide 50 mcg IV bolus → 50 mcg/hr infusion (up to 5 days). Ceftriaxone 1 g IV daily x 7 days (mortality benefit). Emergent EGD with band ligation. Balloon tamponade (Sengstaken-Blakemore or Minnesota tube) for uncontrolled hemorrhage as bridge to TIPS/endoscopy. Avoid over-resuscitation (SBP target 90-100 in variceal bleed to prevent rebleeding).
- **PUD:** IV PPI: pantoprazole 80 mg bolus → 8 mg/hr infusion (or intermittent dosing 40 mg IV BID). Endoscopic therapy (epinephrine injection + thermal/clip). Hold aspirin and NSAIDs.
- **Diverticular bleeding:** Usually self-limited. Colonoscopy after prep if ongoing. Angiography with embolization if massive.

## Disposition

- **ICU:** Hemorrhagic shock, massive transfusion protocol activated, variceal hemorrhage, hemodynamic instability despite resuscitation, need for Sengstaken-Blakemore tube, post-endoscopic high-risk stigmata (active bleeding, visible vessel)
- **Step-down/telemetry:** Hemodynamically stable UGIB requiring monitoring and endoscopy, significant anemia requiring serial CBC, active anticoagulation with GI bleed
- **Floor admission:** Lower GI bleed requiring inpatient colonoscopy, stable UGIB with moderate GBS score, ongoing transfusion needs
- **Observation:** Mild lower GI bleed (stable hemodynamics, Hgb stable), Mallory-Weiss tear (self-limited)
- **Discharge with outpatient endoscopy (24-48 hours):** Glasgow-Blatchford Score 0 ONLY: no hematemesis, no melena, no syncope, SBP >= 110, HR < 100, Hgb >= 13 (men) / >= 12 (women), BUN < 6.5 mmol/L, no hepatic disease, no cardiac failure. Must have reliable follow-up.

## Pitfalls

1. **Trusting the initial hemoglobin.** In acute hemorrhage, hemoglobin does not equilibrate for 6-24 hours. A hemoglobin of 12 g/dL in a patient who vomited a liter of blood 30 minutes ago is NOT reassuring. Assess hemodynamic status (vital signs, lactate) rather than hemoglobin for acute resuscitation decisions.

2. **Assuming hematochezia means lower GI source.** 15% of hematochezia is from brisk upper GI bleeding. A hemodynamically unstable patient with bright red blood per rectum should have an upper GI source considered and may need emergent EGD, not colonoscopy.

3. **Forgetting aortoenteric fistula.** Any patient with prior aortic surgery (open or endovascular) presenting with GI bleeding has an aortoenteric fistula until proven otherwise. The "herald bleed" (small self-limited initial bleed) precedes massive exsanguinating hemorrhage by hours to days. CTA and vascular surgery consultation immediately.

4. **Over-resuscitating variceal hemorrhage.** In known or suspected variceal hemorrhage, aggressive volume resuscitation raises portal pressure and increases bleeding risk. Target SBP 90-100 mmHg. Restrictive transfusion (Hgb target 7) reduces rebleeding and mortality vs liberal transfusion (NEJM 2013, Villanueva et al.).

5. **Skipping rectal exam.** Stool color is critical for localization (melena → upper, maroon → mid-GI, bright red → lower or brisk upper). A rectal exam also identifies hemorrhoids, masses, and fissures. It takes 30 seconds and provides information no blood test can.

6. **Clear NG aspirate excluding upper GI bleed.** A clear NG aspirate has a negative predictive value of only 60-80% for upper GI bleeding. Duodenal bleeds distal to a closed pylorus may not reflux into the stomach. If clinical suspicion for UGIB is high despite clear aspirate, proceed with EGD.

7. **Discharging patients on anticoagulants with "minor" GI bleed.** Any GI bleed in an anticoagulated patient requires serious consideration. The bleeding may be minor now but can become catastrophic. Assess the indication for anticoagulation, consult with the prescribing physician, and ensure very close follow-up if discharging.
