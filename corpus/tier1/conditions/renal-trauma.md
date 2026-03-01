---
id: renal-trauma
condition: Renal Trauma
aliases: [kidney injury traumatic, renal laceration, kidney laceration, renal contusion, renal pedicle injury]
icd10: [S37.001A, S37.011A, S37.021A, S37.031A, S37.041A, S37.051A, S37.061A]
esi: 2
time_to_harm:
  irreversible_injury: "< 4 hours (vascular pedicle injury)"
  death: "< 2 hours (Grade V hemorrhage)"
  optimal_intervention_window: "< 2 hours"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition, American College of Surgeons, 2018"
  - type: guideline
    ref: "WSES-AAST Guidelines: Kidney and Uro-Trauma. Coccolini F et al. World J Emerg Surg. 2019;14:27"
  - type: guideline
    ref: "AUA Urotrauma Guideline. Morey AF et al. J Urol. 2020"
  - type: guideline
    ref: "AAST Organ Injury Scale (Revised 2018): Kidney. Kozar RA et al. J Trauma Acute Care Surg. 2018;85(6):1119-1122"
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
# Renal Trauma

## Recognition

**Mechanism:** Blunt (MVC, fall, sports — 80-90% of renal injuries) or penetrating (stab, GSW). Kidney is the most commonly injured genitourinary organ.

**AAST Organ Injury Scale (2018 revision):**
- **Grade I:** Subcapsular hematoma or contusion without laceration
- **Grade II:** Laceration < 1 cm depth without collecting system involvement; perirenal hematoma confined to retroperitoneum
- **Grade III:** Laceration > 1 cm without collecting system rupture or urinary extravasation. Any vascular injury or active bleeding contained within Gerota fascia.
- **Grade IV:** Laceration into collecting system with urinary extravasation. Laceration of renal pelvis or complete ureteropelvic junction disruption. Segmental renal artery or vein injury. Active bleeding extending beyond Gerota fascia. Segmental or complete kidney infarction due to vessel thrombosis.
- **Grade V:** Shattered kidney. Hilar avulsion — devascularized kidney. Main renal artery or vein laceration or avulsion.

**Presentation:**
- Flank pain, flank tenderness, costovertebral angle tenderness
- Hematuria (gross or microscopic) — present in 80-95%; BUT 25% of Grade V (pedicle injuries) have NO hematuria
- Flank ecchymosis (Grey Turner sign)
- Lower rib fractures (ribs 11-12)
- Hemorrhagic shock (high-grade injuries)
- Abdominal/flank mass (expanding retroperitoneal hematoma)

**Imaging criteria (who to scan):**
- Gross hematuria after trauma → image
- Microscopic hematuria + hemodynamic instability → image
- Microscopic hematuria + significant mechanism → image
- Pediatric: lower threshold (even microscopic hematuria > 50 RBC/HPF warrants imaging)

## Critical Actions

| Action | Target |
|---|---|
| Urinalysis | Immediate |
| CT abdomen/pelvis with IV contrast + delayed images | < 60 minutes |
| Urology consult | < 2 hours for Grade III+ |
| Angioembolization | If active extravasation in stable patient |

1. **Urinalysis** — detect hematuria. Note: absence of hematuria does NOT exclude renal pedicle injury.
2. **CT abdomen/pelvis with IV contrast** — arterial + portal venous + 10-minute delayed phase (to assess collecting system/urinary extravasation). Gold standard imaging.
3. **Urology consult** for Grade III and above
4. **Trauma surgery consult** if hemodynamically unstable or associated abdominal injuries
5. **Angioembolization** — for active extravasation in hemodynamically stable or stabilized patients (Grade III-IV with vascular injury)

## Differential Diagnosis

- Renal contusion without laceration (Grade I — microscopic hematuria, no CT abnormality or minimal findings)
- Liver laceration (right side — differentiated by CT location)
- Splenic laceration (left side)
- Adrenal hemorrhage (often incidental on CT)
- Retroperitoneal hemorrhage from other source (psoas, vertebral fracture)
- Pre-existing renal pathology (hydronephrosis, tumor, cyst) predisposing to injury with minor mechanism
- Ureteral injury (rare in blunt; more common in penetrating)

## Workup

- **Urinalysis:** Gross vs. microscopic hematuria. Dipstick followed by microscopic if positive.
- **CT abdomen/pelvis with IV contrast:** Must include DELAYED PHASE (10-minute images) to assess collecting system integrity and urinary extravasation. Triple-phase: non-contrast (for baseline), arterial (vascular injury), delayed (collecting system).
- **Labs:** CBC (serial q4-6h), BMP (creatinine baseline), type and crossmatch, coagulation studies, lactate
- **CXR:** Associated rib fractures, hemothorax
- **FAST:** May show free fluid but cannot assess retroperitoneal hematoma reliably
- **IVP (intravenous pyelogram):** Only if CT not available; one-shot IVP in OR to confirm functioning contralateral kidney before nephrectomy

## Treatment

**Nonoperative management (NOM) — standard for most renal injuries in hemodynamically stable patients:**
- **Grade I-II:** Observation, bed rest, serial CBC q6-12h, repeat imaging only if clinical deterioration
- **Grade III:** Observation with urology consult, serial labs, bed rest, may need repeat CT at 48-72h
- **Grade IV:** ICU observation, serial labs q4-6h, urology consult. Angioembolization for active extravasation. Urinoma/urinary extravasation may require ureteral stent or percutaneous nephrostomy.
- NOM success rate: > 95% for Grade I-III, 60-80% for Grade IV

**Angioembolization:**
- Active extravasation or pseudoaneurysm on CT in hemodynamically stable patient
- Super-selective embolization preferred (preserves maximal parenchyma)
- Consider for Grade III-IV with vascular injury component

**Operative management — indications:**
- Hemodynamic instability despite resuscitation with suspected renal hemorrhage
- Grade V (hilar avulsion, shattered kidney)
- Expanding or pulsatile retroperitoneal hematoma found at laparotomy
- Failed NOM (ongoing transfusion requirements)

**Surgical options:**
- **Renorrhaphy:** Repair laceration with absorbable suture, bolster with omental flap or hemostatic agents
- **Partial nephrectomy:** Devitalized segments with viable remnant
- **Nephrectomy:** Hilar avulsion, shattered kidney, hemodynamic instability (damage control). Confirm contralateral kidney function (palpation at surgery or one-shot IVP) before nephrectomy.

**Urinary extravasation management:**
- Small contained extravasation: observe, usually resolves spontaneously
- Large or expanding urinoma: percutaneous drainage + ureteral stent
- UPJ disruption: surgical repair (ureteroureterostomy)

**Antibiotics:** Not routine for blunt renal injury. Indicated for penetrating injuries or instrumentation: cefazolin 2 g IV q8h.

## Disposition

- **ICU:** Grade IV-V, hemodynamic instability, post-embolization, post-operative
- **Admit (floor):** Grade II-III with serial monitoring
- **Observe outpatient:** Grade I with reliable follow-up, stable vitals, resolving hematuria
- **Activity restriction:** No contact sports or strenuous activity for 6-8 weeks
- **Follow-up imaging:** CT at 48-72h for Grade III-IV (assess for pseudoaneurysm, urinoma). CT at 3 months for Grade IV-V.
- **Blood pressure monitoring:** Long-term — post-traumatic renovascular hypertension can develop (Page kidney, renal artery stenosis)
- **Transfer:** Level I/II trauma center with urology and IR if not available

## Pitfalls

1. **Assuming no hematuria means no renal injury.** Up to 25% of Grade V renal pedicle injuries present without hematuria. Complete vascular avulsion prevents blood from reaching the collecting system.

2. **Omitting delayed-phase CT images.** Without 10-minute delayed images, collecting system injuries and urinary extravasation are missed. Always request delayed phase in renal trauma.

3. **Performing nephrectomy without confirming contralateral kidney.** A solitary kidney patient requires aggressive nephron-sparing approaches. Confirm contralateral function (palpation, one-shot IVP) before removing a kidney.

4. **Not considering pre-existing renal pathology.** Hydronephrosis, renal cysts, tumors, and horseshoe kidneys are more vulnerable to injury with minor mechanisms. Minor trauma + gross hematuria should prompt imaging even if mechanism seems trivial.

5. **Missing renovascular hypertension on follow-up.** Post-traumatic renal artery thrombosis or compression (Page kidney from chronic subcapsular hematoma) can cause hypertension months to years later. Blood pressure monitoring at follow-up is important.

6. **Exploring a non-expanding retroperitoneal hematoma at laparotomy.** Stable retroperitoneal hematomas from renal injuries should be left undisturbed at laparotomy unless they are expanding, pulsatile, or the patient is hemodynamically unstable from renal hemorrhage specifically.
