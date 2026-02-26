---
id: reboa
condition: Resuscitative Endovascular Balloon Occlusion of the Aorta
aliases: [REBOA, aortic balloon occlusion, endovascular aortic occlusion, ER-REBOA]
icd10: [Z53.09, T79.2XXA, R57.1, R58]
esi: 1
time_to_harm:
  irreversible_injury: "< 15 minutes (hemorrhagic shock → organ failure)"
  death: "< 30 minutes without hemorrhage control"
  optimal_intervention_window: "< 15 minutes from hemorrhagic arrest"
category: procedural
track: tier1
confusion_pairs:
  - condition: resuscitative-thoracotomy
    differentiators:
      - "Resuscitative thoracotomy: open aortic cross-clamping; indicated for penetrating cardiac injury, cardiac tamponade, and thoracic hemorrhage; provides direct cardiac access for repair and internal massage"
      - "REBOA: endovascular aortic occlusion; indicated for non-compressible torso hemorrhage (abdominal/pelvic); does NOT provide cardiac access; less invasive but requires femoral artery access and fluoroscopy/landmarks for positioning"
      - "Critical rule: REBOA is for subdiaphragmatic hemorrhage in patients with a pulse (however weak); resuscitative thoracotomy is for traumatic cardiac arrest or cardiac injury"
  - condition: cardiac-tamponade
    differentiators:
      - "Cardiac tamponade: obstructive shock from pericardial fluid; treated with pericardiocentesis or thoracotomy; REBOA does not address tamponade"
      - "REBOA: hemorrhagic shock from non-compressible torso hemorrhage; tamponade must be excluded before attributing hypotension to hemorrhage"
sources:
  - type: guideline
    ref: "Brenner M, Bulger EM, Perina DG, et al. Joint statement from the American College of Surgeons Committee on Trauma (ACS COT) and the American College of Emergency Physicians (ACEP) regarding the clinical use of Resuscitative Endovascular Balloon Occlusion of the Aorta (REBOA). Trauma Surg Acute Care Open. 2018;3(1):e000154."
    pmid: "29766128"
  - type: review
    ref: "Morrison JJ, Galgon RE, Jansen JO, et al. A systematic review of the use of resuscitative endovascular balloon occlusion of the aorta in the management of hemorrhagic shock. J Trauma Acute Care Surg. 2016;80(2):324-334."
    pmid: "26816219"
  - type: pubmed
    ref: "DuBose JJ, Scalea TM, Brenner M, et al. The AAST prospective Aortic Occlusion for Resuscitation in Trauma and Acute Care Surgery (AORTA) registry: data on contemporary utilization and outcomes of aortic occlusion and resuscitative balloon occlusion of the aorta (REBOA). J Trauma Acute Care Surg. 2016;81(3):409-419."
    pmid: "27050883"
  - type: guideline
    ref: "Hörer TM, Skoog P, Pirouzram A, et al. A small case series of aortic balloon occlusion in trauma: lessons learned from its use in ruptured abdominal aortic aneurysms and a brief review. Eur J Trauma Emerg Surg. 2016;42(5):585-592."
    pmid: "26860658"
  - type: review
    ref: "Stannard A, Eliason JL, Rasmussen TE. Resuscitative endovascular balloon occlusion of the aorta (REBOA) as an adjunct for hemorrhagic shock. J Trauma. 2011;71(6):1869-1872."
    pmid: "22182895"
last_updated: "2026-02-26"
compiled_by: agent
reviewed_by: "Brandon Dent, MD — Board Certified Emergency Medicine"
review_date: "2026-02-27"
risk_tier: A
validation:
  schema_version: "2.0"
  automated_consistency_check: "2026-02-27"
  dose_range_validator: "2026-02-27"
  unit_normalization_check: "2026-02-27"
  cross_file_consistency_check: "2026-02-27"
  citation_presence_check: "2026-02-27"
  duplicate_content_check: "2026-02-27"
  outlier_detection_flag: clear
  provenance_links: []
---
# Resuscitative Endovascular Balloon Occlusion of the Aorta

## Recognition

**Definition:** REBOA is a minimally invasive endovascular technique for temporary aortic occlusion in patients with non-compressible torso hemorrhage (NCTH). A balloon catheter is inserted via the common femoral artery and inflated in the aorta to occlude blood flow distal to the balloon, augmenting proximal blood pressure and reducing distal hemorrhage.

**Aortic Zones:**

| Zone | Location | Indication |
|------|----------|------------|
| Zone I | Descending thoracic aorta (left subclavian artery to celiac trunk) | Abdominal and/or pelvic hemorrhage — intra-abdominal solid organ injury, mesenteric hemorrhage, junctional hemorrhage |
| Zone II | Paravisceral aorta (celiac trunk to lowest renal artery) | NO BALLOON INFLATION — risk of mesenteric and renal ischemia without hemorrhage control |
| Zone III | Infrarenal aorta (below renal arteries to aortic bifurcation) | Pelvic hemorrhage — pelvic fracture with hemodynamic instability, junctional pelvic/inguinal hemorrhage |

**Indications:**
- Non-compressible torso hemorrhage with SBP <90 mmHg despite crystalloid and blood product resuscitation
- Hemorrhagic shock from blunt or penetrating abdominal/pelvic trauma
- Pelvic fracture hemorrhage refractory to pelvic binder and resuscitation
- Postpartum hemorrhage refractory to uterotonics and surgical intervention (emerging indication)
- Ruptured abdominal aortic aneurysm (bridge to OR)
- GI hemorrhage with hemodynamic collapse (salvage indication)
- Junctional hemorrhage at the inguinal or axillary crease

**Contraindications:**
- Thoracic aortic injury (aortic transection, dissection) — balloon inflation proximal to injury worsens hemorrhage
- Known abdominal aortic aneurysm (relative — risk of rupture)
- Cardiac arrest without a pulse (resuscitative thoracotomy with open cross-clamp is preferred)
- Isolated thoracic hemorrhage (REBOA does not control supradiaphragmatic bleeding)
- Inability to obtain femoral artery access

**Decision Triggers:**
- Pelvic fracture + SBP <90 + not responding to pelvic binder + 2 units pRBC → REBOA Zone III
- Positive FAST + hemodynamic instability + OR not immediately available → REBOA Zone I as bridge
- Junctional hemorrhage (groin, axilla) not controlled by pressure/tourniquet → REBOA

## Critical Actions

| Action | Target |
|--------|--------|
| Femoral artery access | < 5 minutes |
| Balloon positioned and inflated | < 10 minutes from arteriotomy |
| Definitive hemorrhage control (OR/IR) | < 60 minutes from balloon inflation (Zone I) |
| Balloon deflation | Gradual, after definitive control achieved |

1. **Activate MTP and trauma surgery/interventional radiology simultaneously** — REBOA is a bridge to definitive hemorrhage control, not definitive treatment
2. **Obtain common femoral artery access** — percutaneous or cut-down, 7-Fr introducer sheath (ER-REBOA Catheter) or 12-Fr sheath (Coda balloon)
3. **Select the zone** — Zone I for abdominal hemorrhage, Zone III for pelvic hemorrhage; NEVER inflate in Zone II
4. **Position the balloon** — use external landmarks or fluoroscopy
5. **Inflate the balloon** — inflate with saline until SBP >90 mmHg or loss of contralateral femoral pulse
6. **Monitor for ischemia** — continuous arterial line (ipsilateral radial), serial lactate, monitor for lower extremity ischemia
7. **Transfer to OR/IR for definitive hemorrhage control** — REBOA buys time but does not stop bleeding permanently

## Differential Diagnosis

REBOA is a hemorrhage control technique. The "differential" is the set of alternative hemorrhage control strategies for NCTH:

| Alternative | When to Choose Over REBOA |
|-------------|--------------------------|
| Resuscitative thoracotomy with aortic cross-clamp | Traumatic cardiac arrest; penetrating thoracic injury; need for direct cardiac access; patient in arrest without pulse |
| Pelvic binder/sheet | First-line for pelvic fracture hemorrhage; apply before REBOA; if hemodynamics stabilize, REBOA not needed |
| Angioembolization (IR) | Stable enough for transport to IR suite; pelvic arterial hemorrhage identified on CT; complements REBOA |
| Pre-peritoneal pelvic packing | Surgical alternative to REBOA for pelvic hemorrhage; does not require vascular access; performed in OR or ED |
| Damage control laparotomy | Definitive hemorrhage control for intra-abdominal bleeding; REBOA bridges to the OR |
| Tourniquet (junctional) | Inguinal/axillary hemorrhage amenable to external compression; if junctional device available, attempt before REBOA |
| Massive transfusion alone | If hemorrhage is compressible and patient is responding to blood products, REBOA is unnecessary |

## Workup

**Pre-Procedure Assessment (simultaneous with resuscitation):**
- FAST exam: identify free fluid (intra-abdominal hemorrhage) — guides Zone I decision
- Pelvic X-ray: identify pelvic fracture — guides Zone III decision
- SBP and shock index (HR/SBP): shock index >1.0 with NCTH triggers REBOA consideration
- Bilateral femoral pulse assessment: absent pulse on one side mandates contralateral access
- Pelvic binder: apply before REBOA if pelvic fracture suspected

**Equipment:**

| Item | Specification |
|------|---------------|
| ER-REBOA Catheter (Prytime Medical) | 7-Fr compatible; preferred for ED use; arterial pressure monitoring through catheter tip |
| Alternative: Coda balloon catheter | Requires 12-Fr sheath; standard angioplasty balloon |
| Introducer sheath | 7-Fr (ER-REBOA) or 12-Fr (Coda) |
| Guidewire | 0.035-inch J-tip guidewire |
| Femoral artery access kit | 18g needle, micropuncture kit, or ultrasound-guided access |
| 20-60 mL Luer-lock syringe | For balloon inflation with saline |
| Ultrasound | For femoral artery access (strongly recommended) |
| Arterial line transducer | For proximal pressure monitoring |
| Fluoroscopy (if available) | For balloon positioning confirmation |

**External Landmark Positioning (when fluoroscopy unavailable):**
- **Zone I:** measure from femoral access site to the xiphoid process — this approximates the distance to the descending thoracic aorta (left subclavian to celiac trunk)
- **Zone III:** measure from femoral access site to the umbilicus — this approximates the infrarenal aorta
- Mark the catheter at the measured distance before insertion

**Labs (drawn simultaneously):**
- Type and crossmatch (6+ units), activate MTP
- CBC, BMP, coags, fibrinogen
- ABG/VBG with lactate (baseline and serial)
- TEG/ROTEM if available

## Treatment

### Step-by-Step: REBOA Placement

**Step 1: Femoral Artery Access**
- Ultrasound-guided puncture of the common femoral artery (CFA) — identify the CFA below the inguinal ligament, above the bifurcation into SFA/profunda
- 18g needle, Seldinger technique: puncture, guidewire, dilator, sheath
- Alternatively: surgical cut-down if ultrasound unavailable or access difficult (hypotension, obesity)
- Insert 7-Fr introducer sheath (ER-REBOA) or 12-Fr sheath (Coda)
- Flush the sheath with heparinized saline

**Step 2: Catheter Positioning**
- Insert the REBOA catheter through the sheath
- Advance to the pre-measured distance:
  - Zone I: approximately 45-50 cm from the femoral access site (xiphoid level)
  - Zone III: approximately 25-30 cm from the femoral access site (umbilicus level)
- Confirm position with:
  - Fluoroscopy (if available) — best method
  - Arterial waveform from catheter tip (ER-REBOA has built-in pressure monitoring)
  - Chest/abdominal X-ray (catheter has radiopaque tip)
  - External landmark measurement (least reliable)

**Step 3: Balloon Inflation**
- Inflate with normal saline using a Luer-lock syringe
- Zone I: inflate 8-14 mL saline (larger aortic diameter)
- Zone III: inflate 3-8 mL saline (smaller aortic diameter)
- Inflate gradually until:
  - Proximal SBP increases to >90 mmHg
  - Contralateral femoral pulse is lost (confirms complete occlusion)
- Do NOT over-inflate — risk of aortic rupture or intimal injury

**Step 4: Partial REBOA (pREBOA) — Preferred When Possible**
- After initial full occlusion and hemodynamic stabilization, partially deflate the balloon to allow some distal flow
- Goal: maintain SBP 80-90 mmHg with partial flow to distal extremities and viscera
- Reduces ischemia-reperfusion injury compared to full occlusion
- Monitor distal perfusion: Doppler signals in dorsalis pedis, pulse oximetry on toes, serial lactate

**Step 5: Monitoring During Occlusion**
- Continuous proximal arterial pressure (radial arterial line)
- Serial lactate every 15-30 minutes (trend indicates ischemia burden)
- Distal pulse checks (Doppler)
- Urine output (Foley catheter — renal perfusion indicator)
- Acidosis monitoring: base deficit, pH on serial ABGs

**Step 6: Balloon Deflation (after definitive hemorrhage control)**
- Deflate gradually over 3-5 minutes (rapid deflation causes washout acidosis, hyperkalemia, and cardiovascular collapse)
- Simultaneously bolus blood products and vasopressors in anticipation of reperfusion hypotension
- Calcium gluconate 1-2 g IV before deflation (prevents hyperkalemia-induced arrhythmia)
- Sodium bicarbonate 50-100 mEq IV if pH <7.2 (buffering reperfusion acidosis)
- Monitor for reperfusion arrhythmias: wide-complex tachycardia, VF from hyperkalemia

### Maximum Occlusion Times

| Zone | Maximum Full Occlusion | Notes |
|------|----------------------|-------|
| Zone I | 60 minutes | Mesenteric and renal ischemia; higher ischemia-reperfusion burden |
| Zone III | 120 minutes | Below renal arteries; lower ischemia burden; longer safe window |

- These are guidelines, not hard limits — exceeding them is acceptable if the alternative is death
- Partial REBOA extends safe occlusion time by maintaining distal perfusion

### Post-Deflation
- Continue massive transfusion to target: Hgb >7, platelets >50k, fibrinogen >200, INR <1.5
- Serial lactate until trending down
- Monitor for compartment syndrome in bilateral lower extremities (reperfusion edema)
- Assess for acute kidney injury (creatinine, urine output)
- Remove the sheath when coagulopathy is corrected — femoral artery repair (closure device or surgical repair) as indicated

## Disposition

- **REBOA as bridge to OR:** transfer to OR with balloon inflated; trauma surgery performs definitive hemorrhage control (damage control laparotomy, pelvic packing, vascular repair); deflate balloon in OR under direct visualization
- **REBOA as bridge to IR:** transfer to angiography suite for embolization of pelvic vessels; deflate after embolization
- **Sheath management:** ICU admission with sheath in situ if re-occlusion may be needed; remove sheath within 24 hours when coagulopathy is corrected
- **Post-procedure ICU:** serial lactate, renal function, compartment checks, transfusion continuation
- **Transfer:** if facility lacks trauma surgery/IR, inflate REBOA and arrange emergent transfer; balloon remains inflated during transport (communicate occlusion time to receiving facility)

## Pitfalls

1. **Inflating the balloon in Zone II (paravisceral aorta).** Zone II contains the origins of the celiac trunk, SMA, and renal arteries. Inflation here causes mesenteric and renal ischemia without controlling pelvic or junctional hemorrhage effectively. Zone selection must be deliberate: abdominal hemorrhage = Zone I, pelvic hemorrhage = Zone III.

2. **Using REBOA as definitive treatment rather than a bridge.** REBOA is a temporizing measure. The balloon stops bleeding temporarily while the patient is transported to the OR or IR suite. Leaving the balloon inflated indefinitely without pursuing definitive hemorrhage control leads to ischemic organ failure and death from reperfusion injury.

3. **Rapid balloon deflation causing cardiovascular collapse.** Deflation washes ischemic metabolites (lactate, potassium, myoglobin) into the central circulation. Rapid deflation causes acute hyperkalemia (VF risk), acidosis, and hypotension. Deflate over 3-5 minutes with concurrent calcium, bicarbonate, blood products, and vasopressors.

4. **Attempting REBOA in traumatic cardiac arrest without a pulse.** REBOA requires femoral artery access, which is technically very difficult without a pulse. In traumatic arrest, resuscitative thoracotomy with direct aortic cross-clamping is faster and provides cardiac access. REBOA is for the patient who still has a pulse — however weak.

5. **Failing to obtain ultrasound-guided femoral access in a hypotensive patient.** Femoral artery access in hemorrhagic shock is difficult due to weak or absent pulses. Blind puncture leads to venous cannulation, hematoma, or failed access. Ultrasound improves first-pass success even in severe hypotension. If ultrasound fails, surgical cut-down is the backup.

6. **Not monitoring for lower extremity compartment syndrome post-deflation.** Reperfusion edema after prolonged aortic occlusion causes compartment syndrome in the legs. Serial compartment checks (pain with passive stretch, tense compartments, pain out of proportion) must be performed every 1-2 hours. Compartment pressures >30 mmHg or delta P <30 mmHg require fasciotomy.

7. **Over-inflating the balloon.** The aorta has a finite diameter. Excessive inflation pressure causes intimal injury, aortic dissection, or rupture. Inflate incrementally with small saline aliquots until SBP target is reached. Loss of contralateral femoral pulse confirms complete occlusion — stop inflating.

### Complication Management
- **Femoral artery thrombosis or dissection from sheath:** anticoagulation if patient is not coagulopathic; vascular surgery consultation for operative repair
- **Balloon migration:** if SBP drops after initial improvement, the balloon may have migrated — recheck position with fluoroscopy or X-ray; reposition as needed
- **Aortic injury from balloon inflation:** if aortic dissection or rupture suspected (new widened mediastinum, hemodynamic collapse despite occlusion), emergent surgical exploration
- **Limb ischemia (ipsilateral to sheath):** the sheath occludes the femoral artery; check distal pulses hourly; remove sheath as soon as clinically safe; vascular surgery consultation if limb becomes threatened
