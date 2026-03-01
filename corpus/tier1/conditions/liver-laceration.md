---
id: liver-laceration
condition: Liver Laceration
aliases: [hepatic laceration, liver injury, hepatic trauma, liver rupture, hepatic hemorrhage]
icd10: [S36.113A, S36.114A, S36.115A, S36.116A, S36.118A, S36.119A]
esi: 1
time_to_harm:
  irreversible_injury: "< 2 hours"
  death: "< 1 hour (massive hemorrhage)"
  optimal_intervention_window: "< 30 minutes"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition, American College of Surgeons, 2018"
  - type: guideline
    ref: "WSES Classification and Guidelines for Liver Trauma. Coccolini F et al. World J Emerg Surg. 2020;15:24"
  - type: guideline
    ref: "Western Trauma Association Critical Decisions: Adult Blunt Hepatic Injury. Keric N et al. J Trauma Acute Care Surg. 2024"
  - type: guideline
    ref: "AAST Organ Injury Scale (Revised 2018): Liver. Kozar RA et al. J Trauma Acute Care Surg. 2018;85(6):1119-1122"
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
# Liver Laceration

## Recognition

**Mechanism:** Blunt abdominal trauma (MVC, fall) or penetrating (stab, GSW). Liver is the second most commonly injured abdominal organ (after spleen) and the most common cause of death from abdominal hemorrhage.

**AAST Organ Injury Scale (2018 revision):**
- **Grade I:** Subcapsular hematoma < 10%; capsular tear < 1 cm depth
- **Grade II:** Subcapsular hematoma 10-50%; intraparenchymal hematoma < 10 cm; laceration 1-3 cm depth, < 10 cm length
- **Grade III:** Subcapsular hematoma > 50% or ruptured; intraparenchymal hematoma > 10 cm or expanding; laceration > 3 cm depth. Active bleeding confined within liver parenchyma.
- **Grade IV:** Parenchymal disruption 25-75% of hepatic lobe or 1-3 Couinaud segments. Active bleeding extending beyond liver parenchyma into peritoneum.
- **Grade V:** Parenchymal disruption > 75% of hepatic lobe or > 3 Couinaud segments. Juxtahepatic venous injury (IVC, major hepatic veins).

**Presentation:**
- Right upper quadrant or right-sided abdominal pain
- Right lower rib fractures (ribs 9-12 on right)
- Guarding, peritoneal signs
- Hemorrhagic shock: tachycardia, hypotension
- Right shoulder pain (referred via phrenic nerve from diaphragmatic irritation)
- Abdominal distension with progressive hemorrhage

## Critical Actions

| Action | Target |
|---|---|
| Large-bore IV access + resuscitation | Immediate |
| FAST exam | < 5 minutes |
| CT abdomen/pelvis with IV contrast | < 30 minutes (if hemodynamically stable) |
| Activate MTP | If hemorrhagic shock |
| Trauma surgery consult | < 30 minutes |

1. **FAST exam** — detects free fluid in RUQ (hepatorenal recess/Morison's pouch). Positive FAST + hemodynamic instability → immediate laparotomy.
2. **CT abdomen/pelvis** (arterial + portal venous phase) — for STABLE patients. Grades injury, detects active extravasation, pseudoaneurysm, biliary injury.
3. **Massive transfusion protocol** if hemorrhagic shock: 1:1:1 PRBC:FFP:platelets
4. **TXA** 1 g IV over 10 minutes within 3 hours of injury
5. **Permissive hypotension** targeting SBP 80-90 mmHg until surgical hemorrhage control (avoid aggressive crystalloid resuscitation that dilutes clotting factors and disrupts clot)

## Differential Diagnosis

- Splenic laceration (left-sided, but bilateral injuries occur)
- Right kidney injury (retroperitoneal, flank pain)
- Right adrenal hemorrhage
- Gallbladder injury (bile in peritoneum)
- Duodenal injury (retroperitoneal, may be occult)
- Mesenteric injury (free fluid without solid organ injury)
- Inferior vena cava injury (catastrophic hemorrhage)
- Right hemothorax (associated with hepatic dome lacerations)

## Workup

- **FAST exam:** Free fluid in Morison's pouch (hepatorenal space). Sensitivity improves with serial exams.
- **CT abdomen/pelvis with IV contrast:** Dual-phase (arterial + portal venous) recommended. Identifies: laceration depth, active extravasation (contrast blush), pseudoaneurysm, periportal tracking, bile leak, hepatic vein injury. Sensitivity > 95%.
- **Labs:** CBC (serial q4-6h), BMP, LFTs (AST/ALT elevation correlates loosely with injury), coagulation studies, type and crossmatch (6+ units), lactate, fibrinogen, TEG/ROTEM
- **CXR:** Right lower rib fractures, right hemothorax/elevated hemidiaphragm
- **HIDA scan or MRCP:** Delayed (days), if bile leak suspected

## Treatment

**Nonoperative management (NOM) — standard for hemodynamically stable patients (85% of blunt liver injuries):**
- ICU admission for Grade III-V; monitored bed for Grade I-II
- Serial abdominal exams q2-4h
- NPO initially
- Serial CBC q6h x 24h, then q12h
- Maintain type and crossmatch (6 units PRBC available)
- Bed rest x 24-72h depending on grade
- NOM success rate: > 90% for Grade I-III, 60-80% for Grade IV

**Angioembolization:**
- Active extravasation (contrast blush) or pseudoaneurysm on CT in hemodynamically stable patient
- Can be performed as adjunct to NOM
- Selective (lobar/segmental) preferred over nonselective (hepatic artery)

**Operative management — indications:**
- Hemodynamic instability despite resuscitation (positive FAST → OR immediately)
- Failed NOM (ongoing transfusion requirement > 4 units in 24h)
- Peritonitis
- Associated hollow viscus injury
- Grade V with hemodynamic compromise

**Damage control surgery:**
- Pringle maneuver (clamp hepatoduodenal ligament — portal triad) to reduce inflow: tolerated 60 minutes continuously, 90+ minutes with intermittent release
- Perihepatic packing: laparotomy pads packed above and below liver
- Temporary abdominal closure (negative pressure wound therapy)
- ICU resuscitation: correct coagulopathy, hypothermia, acidosis (lethal triad)
- Return to OR in 24-48h for pack removal and definitive repair

**Definitive repair options:**
- Direct suture hepatorrhaphy
- Selective hepatic artery ligation
- Omental packing
- Anatomic or non-anatomic hepatic resection (rare, for devitalized segments)

**Biliary complications (delayed):**
- Biloma: percutaneous drainage
- Bile peritonitis: ERCP with sphincterotomy and stent
- Hemobilia: angioembolization

## Disposition

- **ICU:** Grades III-V, any transfusion requirement, post-embolization, post-operative
- **Step-down/floor:** Grades I-II, hemodynamically stable, stable hematocrit
- **OR:** Hemodynamic instability, failed NOM, peritonitis
- **IR suite:** Active extravasation in stable patient
- **Activity restriction:** No contact sports 3-6 months
- **Follow-up:** CT at 1-2 weeks for Grade IV-V (assess for biloma, pseudoaneurysm)
- **Transfer:** Level I trauma center if IR and hepatobiliary surgery not available

## Pitfalls

1. **Aggressive crystalloid resuscitation before surgical control.** Excessive crystalloid disrupts clot, dilutes coagulation factors, and worsens hypothermia. Use permissive hypotension (SBP 80-90) and blood products in 1:1:1 ratio.

2. **CT scan in unstable patient.** Hemodynamically unstable + positive FAST → OR. No CT. Delay kills.

3. **Discharging right lower rib fracture patients without imaging.** Right-sided rib 9-12 fractures carry ~10% risk of liver injury. CT or serial observation is indicated.

4. **Missing hepatic vein or IVC injury (Grade V).** Retrohepatic venous injuries have > 80% mortality. Suspect when perihepatic packing fails to control hemorrhage or when removing packs causes exsanguination. Requires venovenous bypass or atriocaval shunt.

5. **Failing to monitor for delayed biliary complications.** Bile leak, biloma, and hemobilia can present days to weeks after injury. Rising bilirubin, fever, or RUQ pain in a patient with known liver injury warrants CT and possible ERCP.

6. **Not performing repeat imaging for high-grade injuries.** Grade IV-V injuries managed non-operatively have 10-20% delayed complication rate (pseudoaneurysm, biloma, abscess). Follow-up CT at 7-14 days is standard.
