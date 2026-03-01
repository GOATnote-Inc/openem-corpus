---
id: hollow-viscus-injury
condition: Hollow Viscus Injury
aliases: [bowel injury traumatic, intestinal perforation traumatic, mesenteric injury, traumatic bowel perforation]
icd10: [S36.400A, S36.408A, S36.500A, S36.508A, S36.600A, S36.69XA]
esi: 2
time_to_harm:
  irreversible_injury: "< 12 hours"
  death: "< 24 hours (peritonitis, sepsis)"
  optimal_intervention_window: "< 6 hours"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition, American College of Surgeons, 2018"
  - type: guideline
    ref: "WSES Guidelines on Blunt and Penetrating Bowel Injury: Diagnosis, Investigations, and Treatment. Chiarugi M et al. World J Emerg Surg. 2022;17:13"
  - type: pubmed
    ref: "Fakhry SM et al. Incidence of hollow viscus injury in blunt trauma: an analysis from 275,557 trauma admissions from the EAST multi-institutional trial. J Trauma. 2003;54(2):289-294"
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
# Hollow Viscus Injury

## Recognition

**Mechanism:**
- **Blunt:** MVC (seatbelt injury — "seatbelt sign"), handlebar impact, crush injury, deceleration. Occurs in ~1% of blunt trauma admissions. Small bowel most common site.
- **Penetrating:** Stab, GSW — present in ~17% of penetrating abdominal trauma.
- **Deceleration:** Mesenteric tear at fixed points (ligament of Treitz, ileocecal junction, rectosigmoid junction)

**Presentation — often delayed and subtle:**
- Abdominal pain, tenderness (may be diffuse or localized)
- Seatbelt sign (abdominal wall ecchymosis) — 3-8x increased risk of bowel injury
- Peritoneal signs (guarding, rigidity, rebound) — may take 6-24 hours to develop
- Progressive abdominal distension
- Fever, tachycardia (late signs of peritonitis)
- Chance fracture (lumbar flexion-distraction fracture) — 40-50% associated with bowel injury

**Key diagnostic challenge:** CT sensitivity for bowel injury is only 60-95%. Negative CT does NOT exclude hollow viscus injury.

## Critical Actions

| Action | Target |
|---|---|
| Serial abdominal exams | q2-4h for 24 hours |
| CT abdomen/pelvis with IV contrast | < 60 minutes (stable patients) |
| Repeat CT or DPL | If clinical suspicion persists at 6-12 hours |
| Surgical exploration | If peritonitis develops |

1. **FAST exam** — free fluid without solid organ injury on CT is concerning for mesenteric or bowel injury
2. **CT abdomen/pelvis with IV contrast** — look for: free fluid without solid organ injury, bowel wall thickening/enhancement, mesenteric stranding/hematoma, extraluminal air (pneumoperitoneum), oral contrast extravasation (rarely used acutely)
3. **Serial abdominal exams** — most important diagnostic tool when CT is equivocal. q2-4h for 24 hours by the same examiner when possible
4. **Maintain high suspicion** with seatbelt sign, Chance fracture, or handlebar mechanism
5. **Low threshold for surgical exploration** if progressive tenderness, peritoneal signs, rising WBC/lactate, or worsening on repeat imaging

## Differential Diagnosis

- Solid organ injury (spleen, liver — free fluid explained by parenchymal bleeding)
- Mesenteric contusion without bowel perforation
- Abdominal wall hematoma (seatbelt sign without intra-abdominal injury)
- Retroperitoneal hemorrhage (flank ecchymosis, stable hematoma on CT)
- Diaphragmatic rupture (can mimic abdominal findings)
- Urinary tract injury (hematuria, pelvic fracture)
- Pancreatic injury (epigastric pain, elevated lipase — similar delayed presentation)

## Workup

- **CT abdomen/pelvis with IV contrast** — findings suggestive of bowel injury:
  - Free fluid without solid organ injury (most common finding)
  - Pneumoperitoneum (extraluminal free air)
  - Bowel wall thickening or discontinuity
  - Mesenteric stranding, fat infiltration, or hematoma
  - Active contrast extravasation from mesenteric vessels
  - Oral contrast extravasation (if oral contrast used — low yield, rarely used)
- **FAST exam:** Free fluid may be only initial clue
- **Labs:** CBC (serial — rising WBC), BMP, lactate (serial — rising lactate suggests ischemia), lipase (concurrent pancreatic injury), type and screen, coagulation studies, urinalysis
- **Diagnostic peritoneal lavage (DPL):** If CT equivocal and patient deteriorating. Positive if: > 100,000 RBC/mm3, > 500 WBC/mm3, bile, bacteria, or food particles. Highly sensitive but invasive.
- **Repeat CT at 6-12 hours:** If initial CT equivocal and clinical suspicion persists. May show interval development of free air or fluid.

## Treatment

**Conservative management (rare in confirmed injury):**
- Only for contusions/hematomas without perforation (Grade I mesenteric injury)
- Serial exams, NPO, IV fluids, serial imaging

**Operative management (standard for perforation):**
- **Primary repair:** Small perforations (< 50% circumference), clean wounds, minimal contamination, within 6 hours
- **Resection with anastomosis:** Large perforations, devascularized segments, multiple injuries in close proximity
- **Resection with diversion (ostomy):** Severe contamination, hemodynamic instability (damage control), delayed diagnosis (> 24 hours), left colon/rectal injuries with contamination
- **Mesenteric injury:** Ligate bleeding vessels, assess bowel viability (color, peristalsis, bleeding from cut edges, Doppler, fluorescein). Resect non-viable bowel.

**Damage control surgery:**
- If hemodynamically unstable with other injuries: rapid closure of perforations (suture or staple), resection without anastomosis, temporary abdominal closure, ICU resuscitation
- Second-look laparotomy at 24-48 hours for anastomosis and assessment of questionably viable bowel

**Antibiotics (mandatory for perforation):**
- Piperacillin-tazobactam 3.375 g IV q6h (or 4.5 g IV q8h extended infusion)
- Alternative: cefepime 2 g IV q8h + metronidazole 500 mg IV q8h
- Duration: 24 hours if source controlled without gross contamination; 4-7 days if significant contamination or delayed diagnosis

**Supportive:**
- NPO, NG tube decompression
- Aggressive IV fluid resuscitation
- Vasopressors if septic: norepinephrine 0.05-0.5 mcg/kg/min IV

## Disposition

- **Admit all patients** with suspected hollow viscus injury, even if CT is negative — serial exams for 24 hours
- **ICU:** Hemodynamic instability, post-operative, sepsis
- **OR:** Peritonitis, free air on imaging, hemodynamic instability with peritoneal signs, failed observation
- **Transfer:** Level I/II trauma center if surgical capability not available
- **Serial lab monitoring:** CBC, lactate q6-8h during observation period

## Pitfalls

1. **Relying solely on initial CT to exclude bowel injury.** CT sensitivity is only 60-95% for hollow viscus injury. Free fluid without solid organ injury on CT should raise suspicion. Serial exams and repeat imaging at 6-12 hours are essential.

2. **Discharging a patient with seatbelt sign after a "negative" CT.** Seatbelt sign carries 3-8x risk of bowel injury. These patients require 24-hour observation with serial abdominal exams regardless of initial CT findings.

3. **Not associating Chance fracture with bowel injury.** Lumbar flexion-distraction fractures (Chance fractures) from lap-belt restraint are associated with bowel injury in 40-50% of cases. CT abdomen with IV contrast is mandatory.

4. **Delayed recognition of peritonitis.** Hollow viscus injuries often present subtly with progressive tenderness over 6-24 hours. By the time frank peritonitis develops, the window for optimal repair has passed, increasing morbidity.

5. **Using oral contrast to "improve" CT diagnosis.** Oral contrast delays imaging, causes vomiting, and has minimal incremental sensitivity for bowel perforation. IV contrast CT is the standard.

6. **Failing to perform second-look laparotomy when bowel viability was questionable.** If bowel viability was uncertain at initial damage control surgery, return to OR at 24-48 hours is mandatory to assess viability and complete anastomosis.
