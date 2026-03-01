---
id: pancreatic-injury
condition: Pancreatic Injury
aliases: [pancreatic trauma, pancreatic laceration, pancreatic duct injury, pancreatic transection]
icd10: [S36.200A, S36.201A, S36.209A, S36.290A, S36.299A]
esi: 2
time_to_harm:
  irreversible_injury: "< 12 hours"
  death: "< 24 hours (sepsis from missed injury)"
  optimal_intervention_window: "< 12 hours"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition, American College of Surgeons, 2018"
  - type: guideline
    ref: "WSES-AAST Guidelines: Duodeno-Pancreatic and Extrahepatic Biliary Tree Trauma. Coccolini F et al. World J Emerg Surg. 2019;14:56"
  - type: guideline
    ref: "EAST Practice Management Guideline: Pancreatic Injuries. Phelan HA et al. J Trauma. 2009"
  - type: pubmed
    ref: "Ho VP et al. Pancreatic Trauma: Imaging Review and Management Update. RadioGraphics. 2021;41(4):1164-1181"
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
# Pancreatic Injury

## Recognition

**Mechanism:**
- **Blunt:** Direct epigastric trauma — handlebar injury (bicycle, motorcycle), steering wheel, assault, compression against spine. Pancreas compressed against vertebral column.
- **Penetrating:** Stab, GSW traversing upper abdomen. Often associated with other organ injuries.
- Uncommon: < 2% of blunt trauma, but high morbidity/mortality (20-40%) from delayed diagnosis and complications.

**AAST Organ Injury Scale:**
- **Grade I:** Minor contusion or superficial laceration without ductal injury
- **Grade II:** Major contusion or laceration without ductal injury or tissue loss
- **Grade III:** Distal transection or parenchymal injury with ductal injury (left of SMV)
- **Grade IV:** Proximal transection or parenchymal injury involving the ampulla (right of SMV)
- **Grade V:** Massive disruption of pancreatic head

**Presentation — often delayed and nonspecific:**
- Epigastric pain radiating to back (classic but often masked by other injuries)
- Epigastric tenderness
- Progressive abdominal pain over 12-24 hours
- Nausea, vomiting
- Signs of peritonitis (late — from enzyme leak and autodigestion)
- Hemorrhagic shock (uncommon from pancreatic injury alone; more likely from associated vascular injury)

**Key clinical point:** The deep retroperitoneal location of the pancreas makes initial clinical detection difficult. Diagnosis is frequently delayed 12-24 hours or more.

## Critical Actions

| Action | Target |
|---|---|
| CT abdomen/pelvis with IV contrast | < 60 minutes |
| Serum lipase | At presentation + serial q6-12h |
| MRCP or ERCP | If ductal injury suspected |
| Surgical consult | < 2 hours for confirmed injury |

1. **CT abdomen/pelvis with IV contrast** — first-line imaging. Sensitivity improves with thin-cut (3 mm) sections through pancreas and delayed imaging.
2. **Serum lipase** — elevated in 85% of pancreatic injuries. Normal lipase does NOT exclude injury (especially early). Serial lipase at 6-12 hours more informative.
3. **Determine ductal integrity** — the key management decision point. MRCP (noninvasive) or ERCP (diagnostic + therapeutic) for suspected ductal injury.
4. **Serial abdominal exams** — mandatory for 24-48 hours with concerning mechanism (handlebar, epigastric blunt force)
5. **Surgical consult** for confirmed pancreatic injury — grade determines operative vs. nonoperative management

## Differential Diagnosis

- Duodenal injury (adjacent, frequently concurrent — 50% of pancreatic injuries have associated duodenal injury)
- Hollow viscus perforation (peritoneal signs, free air)
- Splenic or hepatic injury (higher incidence, easier to diagnose)
- Mesenteric injury (free fluid on imaging)
- Traumatic pancreatitis (without structural injury — inflammatory response)
- Renal injury (flank pain, hematuria)
- Vertebral body fracture (direct spinal pain from mechanism)

## Workup

- **CT abdomen/pelvis with IV contrast:** Findings of pancreatic injury:
  - Pancreatic laceration or fracture (hypoattenuating line through parenchyma)
  - Peripancreatic fluid or hemorrhage
  - Thickening of left anterior renal fascia
  - Fluid between splenic vein and pancreas
  - Active extravasation
  - CT sensitivity: 60-80% initially; improves on repeat at 12-24 hours
- **Serum lipase:** More sensitive than amylase. Elevated > 3x ULN increases suspicion. Normal does not exclude. Serial measurements more informative.
- **MRCP (MR cholangiopancreatography):** Noninvasive assessment of ductal integrity. Consider if CT equivocal and patient stable.
- **ERCP (endoscopic retrograde cholangiopancreatography):** Definitive for duct evaluation + can place stent across disruption (Grade III). Best used in stable patients with suspected ductal injury.
- **Labs:** CBC, BMP, lipase (serial), LFTs, type and crossmatch, lactate, coagulation studies
- **Repeat CT at 12-24 hours:** If initial CT was equivocal with concerning mechanism — pancreatic injury findings evolve over time

## Treatment

**Grade I-II (no ductal injury):**
- Nonoperative management: observation, NPO, NG decompression if needed
- IV fluids, serial abdominal exams, serial lipase
- Pain control: fentanyl 25-50 mcg IV q30min PRN, acetaminophen 1 g IV q6h
- If found at laparotomy: external drainage (closed suction drain adjacent to injury), hemostasis

**Grade III (distal transection with duct injury):**
- **Distal pancreatectomy** +/- splenectomy — standard of care
- Splenic-preserving distal pancreatectomy if patient stable and spleen intact
- Alternative in selected stable patients: ERCP with pancreatic duct stent (bridge to healing)

**Grade IV (proximal/ampullar injury):**
- If stable: external drainage + Roux-en-Y pancreaticojejunostomy
- If unstable: damage control with wide drainage, definitive reconstruction at relaparotomy
- Whipple (pancreaticoduodenectomy) rarely performed acutely — reserved for massive pancreatic head destruction

**Grade V (massive head disruption):**
- Damage control surgery: drainage, hemorrhage control, temporary closure
- Pancreaticoduodenectomy (Whipple) for definitive management — high morbidity (40-60%)
- Consider damage control with staged Whipple at 48-72 hours

**Complications management:**
- **Pancreatic fistula:** Most common complication (10-35%). Managed with drainage, NPO/TPN, octreotide 100 mcg SQ TID (reduces pancreatic secretions, evidence mixed)
- **Pseudocyst:** Observe if < 6 cm and asymptomatic. Drain (percutaneous, endoscopic, or surgical) if > 6 cm, enlarging, symptomatic, or infected.
- **Abscess:** Percutaneous drainage + antibiotics (piperacillin-tazobactam 4.5 g IV q8h)

## Disposition

- **Admit all confirmed or suspected pancreatic injuries** — minimum 48-72 hours observation
- **ICU:** Grade III-V, hemodynamic instability, post-operative
- **Surgical consult:** All confirmed injuries
- **OR:** Grade III-V with ductal injury, peritonitis, hemodynamic instability
- **Gastroenterology consult:** For ERCP if ductal injury suspected in stable patient
- **Transfer:** Level I trauma center with hepatobiliary/pancreatic surgery expertise if not available

## Pitfalls

1. **Normal initial CT and lipase excludes pancreatic injury.** Both CT sensitivity (60-80%) and lipase can be normal early. Repeat imaging at 12-24 hours is essential for patients with high-risk mechanism (handlebar, direct epigastric blow).

2. **Failing to assess ductal integrity.** The critical management decision is whether the main pancreatic duct is disrupted. Grade I-II (duct intact) are managed conservatively. Grade III+ (duct injury) require intervention. MRCP or ERCP is needed if CT cannot clearly delineate the duct.

3. **Missing concurrent duodenal injury.** 50% of pancreatic injuries have associated duodenal injury. Both organs must be assessed and addressed surgically.

4. **Delayed diagnosis causing necrotizing pancreatitis and sepsis.** Pancreatic enzyme leak from unrecognized injury causes autodigestion, retroperitoneal necrosis, abscess, and sepsis. Mortality doubles with delayed diagnosis beyond 24 hours.

5. **Not placing drains at surgery.** Controlled external drainage is essential after pancreatic surgery to prevent intra-abdominal enzyme collections and fistula complications.

6. **Attempting complex reconstruction in an unstable patient.** Damage control principles apply: drainage, hemorrhage control, and temporary closure. Definitive reconstruction (Whipple, Roux-en-Y) at re-operation when resuscitated.
