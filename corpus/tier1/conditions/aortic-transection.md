---
id: aortic-transection
condition: Traumatic Aortic Transection
aliases: [blunt thoracic aortic injury, BTAI, traumatic aortic rupture, aortic disruption, aortic tear]
icd10: [S25.09XA]
esi: 1
time_to_harm:
  irreversible_injury: "< 30 minutes"
  death: "< 1 hour without containment"
  optimal_intervention_window: "< 4 hours to definitive repair"
mortality_if_delayed: "85% prehospital mortality; 50% of survivors die within 24 hours without repair"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "Demetriades D, Velmahos GC, Scalea TM, et al. Diagnosis and treatment of blunt thoracic aortic injuries: changing perspectives. J Trauma. 2008;64(6):1415-1418."
    pmid: "18545104"
  - type: guideline
    ref: "Fox N, Schwartz D, Salazar JH, et al. Evaluation and management of blunt traumatic aortic injury: a practice management guideline from the Eastern Association for the Surgery of Trauma. J Trauma Acute Care Surg. 2015;78(1):136-146."
    pmid: "25539215"
  - type: guideline
    ref: "Lee WA, Matsumura JS, Mitchell RS, et al. Endovascular repair of traumatic thoracic aortic injury: clinical practice guidelines of the Society for Vascular Surgery. J Vasc Surg. 2011;53(1):187-192."
    pmid: "20974523"
  - type: pubmed
    ref: "Fabian TC, Richardson JD, Croce MA, et al. Prospective study of blunt aortic injury: Multicenter Trial of the American Association for the Surgery of Trauma. J Trauma. 1997;42(3):374-383."
    pmid: "9095103"
  - type: pubmed
    ref: "Demetriades D, Velmahos GC, Scalea TM, et al. Operative repair or endovascular stent graft in blunt traumatic thoracic aortic injuries: results of an American Association for the Surgery of Trauma Multicenter Study. J Trauma. 2008;64(3):561-571."
    pmid: "18332794"
confusion_pairs:
  - condition: aortic-dissection
    differentiators:
      - "Traumatic aortic transection: high-energy deceleration mechanism (MVC, fall >3 meters, ejection)"
      - "Aortic dissection: spontaneous; associated with hypertension, Marfan syndrome, bicuspid aortic valve"
      - "Transection localizes to isthmus (90%) at ligamentum arteriosum; dissection originates at ascending aorta (Type A) or descending aorta (Type B)"
      - "Transection: CTA shows periaortic hematoma, intimal flap, pseudoaneurysm at isthmus; dissection: true-false lumen with intimal flap extending longitudinally"
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
# Traumatic Aortic Transection

## Recognition

**Mechanism:** High-energy deceleration injury. The aorta is tethered at the ligamentum arteriosum (aortic isthmus, just distal to the left subclavian artery). During rapid deceleration, the mobile aortic arch shears against the fixed descending aorta at this point.

**High-risk mechanisms:**
- Motor vehicle collision >40 mph (especially lateral impact or frontal)
- Ejection from vehicle
- Fall from >3 meters (10 feet)
- Pedestrian struck at high speed
- Motorcycle crash
- Aircraft deceleration injury

**Injury grades (Society for Vascular Surgery):**

| Grade | Description | Management |
|-------|-------------|------------|
| I | Intimal tear | Medical management, serial imaging |
| II | Intramural hematoma | Endovascular repair (urgent) |
| III | Pseudoaneurysm | Endovascular repair (urgent) |
| IV | Free rupture | Emergent repair (rarely survive to hospital) |

**Anatomic distribution:**
- Aortic isthmus: 90%
- Ascending aorta: 5% (usually fatal at scene)
- Descending aorta: 3%
- Aortic arch: 2%

**Clinical presentation:** Many patients have no external thoracic injury. Suspect in all high-energy deceleration trauma. Associated injuries are common (long bone fractures, pelvic fractures, TBI, solid organ injury).

**Chest X-ray findings (screening only — low sensitivity individually, high combined NPV):**
- Widened mediastinum >8 cm at aortic knob level (most sensitive single finding, ~53%)
- Loss of aortic knob contour
- Left apical cap (extrapleural blood)
- Deviation of trachea or NG tube to the right
- Depression of left mainstem bronchus (>140 degrees from trachea)
- Widened paraspinal stripe
- Left hemothorax
- First or second rib fractures

**A normal CXR does NOT exclude aortic injury.** CTA is required for definitive evaluation in high-risk mechanisms.

## Critical Actions

1. **ATLS primary survey.** Airway, breathing, circulation. Traumatic aortic injury is identified during the secondary survey or adjunct imaging — do not pursue aortic workup before stabilizing immediately life-threatening hemorrhage.
2. **CTA chest with arterial phase protocol** — gold standard (sensitivity >98%, specificity >98%). Obtain in all hemodynamically stable patients with high-risk deceleration mechanism, regardless of CXR findings.
3. **Permissive hypotension and impulse control.** Target SBP 80-100 mmHg and heart rate <100 bpm to reduce aortic wall stress while maintaining end-organ perfusion.
   - Esmolol 500 mcg/kg IV bolus then 50-200 mcg/kg/min infusion (first-line)
   - OR labetalol 20 mg IV bolus, then 1-2 mg/min infusion
   - Add nicardipine 5 mg/hr IV (titrate 2.5 mg/hr q5min, max 15 mg/hr) if beta-blocker alone insufficient
4. **Emergent trauma surgery and vascular surgery consultation** — activate at time of suspicion.
5. **Type and crossmatch for 6 units pRBCs.** Activate massive transfusion protocol if hemodynamically unstable.
6. **Do NOT place a left subclavian or left internal jugular central line** — may be in the operative field.
7. **Manage associated injuries simultaneously.** Traumatic aortic injury rarely occurs in isolation. Identify and treat other life-threatening injuries (splenic laceration, pelvic fracture, pneumothorax).

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Aortic dissection | Spontaneous onset; tearing pain radiating to back; hypertension history; no trauma; CTA: true-false lumen with longitudinal intimal flap |
| Myocardial contusion | Anterior chest wall trauma; ECG changes (ST elevation, new RBBB, arrhythmia); troponin elevation; normal aorta on CTA |
| Diaphragmatic rupture | Left > right; bowel in thorax on CXR; NG tube in chest; CTA shows diaphragm defect |
| Esophageal rupture | Pneumomediastinum; left pleural effusion with high amylase; contrast esophagram positive |
| Traumatic hemothorax | Rib fractures; chest tube output >1500 mL immediately or >200 mL/hr; no aortic pathology on CTA |
| Sternal fracture | Point tenderness; lateral CXR shows displaced sternum; mediastinal widening from sternal hematoma, not aortic |
| Mediastinal hematoma (non-aortic) | Venous bleeding from small vessels; CTA shows no aortic injury; hematoma anterior or posterior |

## Workup

**Imaging:**
- **CTA chest (arterial phase):** Definitive study. 2-3 mm cuts with ECG gating if available. Identifies intimal flap, pseudoaneurysm, periaortic hematoma, active extravasation. Replaces conventional angiography as first-line.
- **Chest X-ray (portable AP):** Screening only. Sensitivity for individual findings is poor (53-92%). Obtain in all trauma patients but do not rely on normal CXR to exclude injury.
- **TEE (transesophageal echocardiography):** Alternative when CTA unavailable or patient too unstable for CT. Sensitivity 97-100% for isthmus injuries. Operator-dependent. Blind spot at distal ascending aorta/proximal arch.
- **Intravascular ultrasound (IVUS):** Adjunct during endovascular repair for precise injury characterization.

**Labs:**
- Type and crossmatch (minimum 6 units pRBCs)
- CBC, BMP, coagulation studies (PT/INR, fibrinogen)
- Lactate (marker of shock/hypoperfusion)
- ABG (base deficit correlates with hemorrhage severity)
- Troponin (concurrent myocardial contusion)

**Additional studies:**
- FAST exam — identify concurrent hemoperitoneum or hemopericardium
- Pelvic XR — concurrent pelvic fracture is a major hemorrhage source
- ECG — myocardial contusion, cardiac tamponade

## Treatment

**Hemodynamic management (anti-impulse therapy):**
- Target SBP 80-100 mmHg and HR <100 bpm
- **Esmolol** 500 mcg/kg IV bolus then 50-200 mcg/kg/min infusion — preferred for titrability
- **Labetalol** 20 mg IV bolus q10min (max 300 mg), then 1-2 mg/min infusion — alternative
- **Nicardipine** 5 mg/hr IV, titrate by 2.5 mg/hr q5min (max 15 mg/hr) — add if BP not controlled with beta-blocker alone
- Beta-blocker first, then vasodilator. Vasodilator alone causes reflex tachycardia and increases aortic wall shear stress.
- Avoid nitroprusside (reflex tachycardia, cyanide toxicity risk in prolonged use)

**Definitive repair:**
- **Thoracic endovascular aortic repair (TEVAR):** First-line for Grade II-IV injuries. Lower mortality (7.2%) vs open repair (23.5%) per AAST multicenter data. Requires adequate landing zones proximal and distal to injury. Left subclavian artery coverage may be necessary.
- **Open surgical repair:** Reserved for ascending aortic injuries, arch injuries unsuitable for TEVAR, or when TEVAR is unavailable. Left thoracotomy with aortic cross-clamping and graft interposition. Cardiopulmonary bypass or left heart bypass to minimize spinal cord ischemia.

**Timing of repair:**
- **Grade I (intimal tear):** Medical management with anti-impulse therapy. Serial CTA at 24-48 hours, 1 week, 1 month, then q6 months. ~50% heal spontaneously.
- **Grade II-III:** Urgent TEVAR within 24 hours if hemodynamically stable. Earlier if contained rupture shows expansion.
- **Grade IV (free rupture):** Emergent repair. Hemorrhagic shock is managed with massive transfusion protocol (1:1:1 pRBC:FFP:platelets) and damage control resuscitation.

**Delayed repair strategy:** In patients with severe TBI, solid organ injury, or contaminated fields, delaying TEVAR 24-72 hours with strict anti-impulse therapy is acceptable for contained injuries (Grade II-III). Serial CTA monitoring during delay.

**Massive transfusion protocol (if hemorrhagic shock):**
- 1:1:1 ratio pRBC:FFP:platelets
- Tranexamic acid 1 g IV over 10 min, then 1 g IV over 8 hours (within 3 hours of injury)
- Calcium chloride 1 g IV per 4 units pRBC (citrate chelation)
- Target: fibrinogen >150 mg/dL, platelets >50,000, INR <1.5

## Disposition

**Emergent OR/interventional suite:**
- Grade IV (free rupture) — emergent TEVAR or open repair
- Grade II-III with hemodynamic instability or expanding pseudoaneurysm

**Surgical ICU:**
- All grades — continuous arterial BP monitoring, anti-impulse therapy, serial imaging
- Grade I — ICU observation with CTA at 24-48 hours
- Post-TEVAR or post-open repair — ICU minimum 48-72 hours

**Transfer:**
- If trauma center lacks endovascular capability or cardiothoracic surgery, initiate anti-impulse therapy and transfer emergently
- Maintain SBP <100 mmHg during transport
- Two large-bore IVs, crossmatched blood available for transport

## Pitfalls

1. **Excluding aortic injury based on normal CXR.** CXR is a screening tool with poor sensitivity for individual findings. A normal CXR does NOT exclude aortic injury. CTA is mandatory for all high-risk deceleration mechanisms regardless of CXR appearance.

2. **Delaying CTA for other diagnostic studies.** CTA chest is rapid and definitive. In stable polytrauma, obtain CTA as part of the initial pan-scan (head, C-spine, chest, abdomen/pelvis). Delaying aortic diagnosis increases mortality — 50% of survivors die within 24 hours without treatment.

3. **Using vasodilators without beta-blockade.** Nitroprusside or nicardipine alone causes reflex tachycardia, increasing dP/dt (rate of aortic pressure rise) and aortic wall shear stress. Beta-blocker must be initiated first to blunt the reflex before adding a vasodilator.

4. **Aggressive fluid resuscitation to normalize BP.** Permissive hypotension (SBP 80-100 mmHg) reduces aortic wall stress and risk of converting a contained rupture to free rupture. Target organ perfusion (mental status, urine output) rather than a normal BP number.

5. **Placing a left-sided central line.** Left subclavian and left internal jugular access should be avoided — these are in the operative field for both TEVAR and open repair. Use right-sided access.

6. **Treating aortic injury in isolation.** >90% of patients with traumatic aortic injury have concurrent injuries (TBI, solid organ injury, long bone fractures, pelvic fractures). Hemorrhage from other sources may be more immediately life-threatening than a contained aortic injury. Prioritize the most immediately lethal problem.

7. **Assuming Grade I injuries are benign.** While ~50% heal spontaneously, the other half progress to pseudoaneurysm or rupture. Serial imaging surveillance is mandatory, and patients require strict anti-impulse therapy during observation.
