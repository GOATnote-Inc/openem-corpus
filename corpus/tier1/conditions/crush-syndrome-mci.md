---
id: crush-syndrome-mci
condition: Crush Syndrome in Structural Collapse and Mass Casualty Incidents
aliases: [crush injury, crush syndrome, traumatic rhabdomyolysis, Bywaters syndrome, entrapment syndrome, reperfusion injury]
icd10: [T79.5XXA, T79.A0XA, T79.6XXA, M62.82, T07.XXXA]
esi: 1
time_to_harm:
  irreversible_injury: "< 1 hour — continuous crush produces irreversible muscle necrosis; reperfusion hyperkalemia within minutes of extrication"
  death: "< 30 minutes post-extrication from fatal hyperkalemia if untreated; renal failure within 24–72 hours"
  optimal_intervention_window: "Pre-extrication IV fluid resuscitation — begin before release of compressive force"
category: disaster-mci
track: tier1
sources:
  - type: pubmed
    ref: "Better OS et al. Early management of shock and prophylaxis of acute renal failure in traumatic rhabdomyolysis. N Engl J Med. 1990;322(12):825-829."
    pmid: "2137875"
  - type: review
    ref: "Sever MS et al. Recommendation for the management of crush victims in mass disasters. Nephrol Dial Transplant. 2012;27(Suppl 1):i1-67."
    pmid: "22241071"
  - type: pubmed
    ref: "Gonzalez D. Crush syndrome. Crit Care Med. 2005;33(1 Suppl):S34-S41."
    pmid: "15640677"
  - type: consensus-statement
    ref: "Renal Disaster Relief Task Force of the International Society of Nephrology. Crush syndrome and renal failure in mass disasters: consensus statement. J Am Soc Nephrol. 2006;17(11):2937-2938."
  - type: pubmed
    ref: "Gibney RTN et al. Renal replacement therapy in acute renal failure related to crush syndrome: strategies from the 1999 Marmara earthquake. Ren Fail. 2005;27(5):621-627."
    pmid: "16153001"
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
# Crush Syndrome in Structural Collapse and Mass Casualty Incidents

## Recognition

**Definition:** Crush syndrome is the systemic manifestation of muscle cell damage resulting from prolonged compression of skeletal muscle (typically >1 hour). Compression causes direct myocyte necrosis. Release of the compressive force triggers reperfusion injury — massive release of intracellular contents (potassium, myoglobin, phosphate, uric acid, creatine kinase) into the circulation, producing hyperkalemia (cardiac arrest), myoglobinuric acute kidney injury, DIC, and hypovolemic shock (third-spacing of fluid into damaged muscle).

**Crush Injury vs. Crush Syndrome:**
- **Crush injury:** localized tissue damage from compression. Present during entrapment.
- **Crush syndrome:** systemic response after release of compression (reperfusion). Absent until extrication.
- A patient trapped under debris for 4 hours with a crushed leg may appear stable while trapped. Removing the compressive force releases a bolus of potassium and myoglobin that can cause cardiac arrest within minutes.

**High-Risk Scenarios:**
- Earthquake with structural collapse (most common worldwide — 1999 Marmara: 462 crush patients; 2010 Haiti: estimated 3,000+)
- Building collapse (bombing, structural failure, mining accident)
- Trench collapse
- Industrial entrapment (machinery, vehicles)
- Stampede/crowd crush
- Prolonged immobilization (found down >4h — geriatric, substance use)

**Risk Factors for Crush Syndrome Development:**

| Factor | Higher Risk |
|--------|------------|
| **Duration of entrapment** | >1 hour (minimal risk <1h), severe risk >4–6 hours |
| **Muscle mass involved** | Lower extremities > trunk > upper extremities (thigh has highest myoglobin load) |
| **Bilateral involvement** | Both lower extremities = highest risk |
| **Ambient temperature** | Heat accelerates necrosis; cold may delay but does not prevent it |
| **Patient hydration** | Pre-existing dehydration (deprived of water during entrapment) worsens renal injury |

**Clinical Presentation:**

**During Entrapment:**
- Limb pain, paresthesias, pallor
- Limb edema (if partially compressed)
- Deceptively stable vital signs — the compressive force is acting as a tourniquet
- Patient may be alert, conversational, not appearing critically ill

**After Extrication (Reperfusion):**
- **Minutes:** Hypotension (massive third-spacing into damaged muscle — 12 L/day fluid loss possible), cardiac arrest from hyperkalemia
- **Hours:** Profound hypovolemic shock, metabolic acidosis, hyperkalemia (K+ >6.5 mmol/L), dark brown/tea-colored urine (myoglobinuria), oliguria/anuria
- **24–72 hours:** Acute kidney injury (AKI) from myoglobin cast nephropathy, worsening acidosis, hyperphosphatemia, hypocalcemia (calcium sequestration into damaged muscle)
- **Days:** Compartment syndrome in affected/adjacent limbs, DIC, ARDS, sepsis from necrotic tissue, multi-organ failure

## Critical Actions

1. **Begin IV fluid resuscitation BEFORE extrication.** This is the single most important intervention in crush syndrome management. Establish IV access while the patient is still trapped. Infuse NS at 1–1.5 L/h starting as soon as IV access is obtained — before the compressive force is released. Goal: volume-load the circulation to dilute the potassium and myoglobin bolus that will be released upon extrication. If entrapment >4h, administer 1–2 L NS before releasing the compressive force.

2. **Cardiac monitoring before and during extrication.** Attach cardiac monitor before releasing the crush. Peaked T-waves, widened QRS, bradycardia, or sine-wave pattern = hyperkalemia. If ECG changes develop during extrication: stop extrication if feasible, treat hyperkalemia (calcium gluconate, see below), then continue extrication with aggressive fluid and potassium management.

3. **Treat hyperkalemia immediately upon recognition:**
   - Calcium gluconate 10% 30 mL (3 g) IV over 2–3 min — membrane stabilization (does not lower K+, but prevents cardiac arrest). Repeat q5min if ECG changes persist. (Calcium chloride 10% 10 mL IV via central line is equivalent but causes tissue necrosis if extravasated — use gluconate peripherally.)
   - Regular insulin 10 units IV + dextrose 50% 50 mL (25 g) IV push — shifts K+ intracellularly. Onset 15 min, duration 4–6h.
   - Sodium bicarbonate 50 mEq (1 ampule) IV over 5 min — shifts K+ intracellularly. Most effective when pH <7.2.
   - Albuterol 10–20 mg nebulized (4–8× standard asthma dose) — shifts K+ intracellularly. Additive with insulin.
   - Kayexalate (sodium polystyrene sulfonate) 30 g PO or PR — removes K+ from body but onset is hours. Not for acute management.
   - Emergent hemodialysis for K+ >6.5 with ECG changes refractory to medical therapy.

4. **Aggressive IV fluid resuscitation post-extrication.** NS 1–1.5 L/h for the first 6 hours, then titrate to urine output >200–300 mL/h (adult) or >3 mL/kg/h (pediatric). Total fluid requirements: 6–12 L in the first 24 hours for bilateral lower extremity crush. Monitor for fluid overload (pulmonary edema) — balance against renal protection.

5. **Alkalinize urine to prevent myoglobin cast nephropathy.** Sodium bicarbonate: add 3 ampules (150 mEq) to 1 L D5W, infuse at 200 mL/h. Target urine pH >6.5 (myoglobin precipitation increases dramatically below pH 6.5). Monitor serum pH — hold bicarbonate if serum pH >7.50. Avoid bicarbonate if serum calcium is already low (alkalosis worsens ionized hypocalcemia and may precipitate tetany or seizures).

6. **Do NOT correct hypocalcemia unless symptomatic.** Serum calcium drops in crush syndrome because calcium deposits in damaged muscle. Aggressive calcium repletion in the acute phase drives more calcium into necrotic tissue and worsens tissue injury. Treat only for symptomatic hypocalcemia (tetany, seizures, QTc prolongation >500 ms): calcium gluconate 10% 10–20 mL IV over 10 min.

7. **Assess for compartment syndrome in all affected and adjacent limbs.** Crush injury produces massive swelling. Compartment pressures >30 mmHg or within 30 mmHg of diastolic pressure → emergent fasciotomy. Use intracompartmental pressure monitor (Stryker device) in all questionable cases. Do not rely on the "5 Ps" — pain is unreliable in crush patients (nerve damage, sedation, altered mental status).

8. **Tourniquet as last resort for field amputation.** If a limb is non-viable (cold, pulseless, mangled, entrapped >12h with bilateral involvement) and extrication is not possible, field amputation with proximal tourniquet may be life-saving by preventing reperfusion syndrome. This is a surgical decision made by the most senior clinician present and documented as such.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Rhabdomyolysis (non-crush)** | Same biochemical syndrome but from exertional, drug-induced, or thermal causes. No history of compression. Manage identically once diagnosed. |
| **Compartment syndrome (without crush)** | Limb-specific; caused by fracture, vascular injury, or reperfusion. Not systemic unless progresses to rhabdomyolysis. Fasciotomy is definitive. |
| **Hyperkalemia from renal failure** | Chronic onset, no myoglobinuria, no trauma history. ECG changes identical. Treat identically. |
| **Hypovolemic shock from hemorrhage** | Tachycardia, hypotension, but clear blood loss source. Urine is clear, not tea-colored. CK normal. |
| **Acute tubular necrosis (non-myoglobin)** | Post-ischemic or nephrotoxic. No pigmented casts. CK normal. |
| **Hemolytic transfusion reaction** | Dark urine from hemoglobin, not myoglobin. Positive DAT, elevated bilirubin, post-transfusion timing. |

## Workup

**Field (Pre-Extrication):**
- Estimate entrapment duration (>1h = crush risk)
- Assess which limbs are compressed and muscle mass involved
- ECG rhythm strip (cardiac monitor) before and during extrication
- POC potassium if available
- Urine color assessment (tea-colored = myoglobinuria)

**Hospital (Post-Extrication):**
- **Stat labs:** BMP (K+, Ca²+, phosphate, BUN/Cr), CK (initial and q6h × 24h, then q12h), CBC, coagulation panel (PT, INR, PTT, fibrinogen — DIC screening), lactate, ABG (metabolic acidosis assessment), uric acid, LDH
- **Urinalysis:** myoglobinuria (dipstick positive for blood but no RBC on microscopy = myoglobin), urine pH (target >6.5)
- **Urine myoglobin:** quantitative (>1000 ng/mL = high risk for AKI)
- **ECG:** peaked T-waves, widened QRS, loss of P-waves, sine wave = hyperkalemia
- **Compartment pressures:** in all affected limbs and adjacent compartments
- **Imaging:** XR of affected extremities (fractures), CT if truncal involvement (intra-abdominal, retroperitoneal injury)

**Serial Monitoring:**
- K+ q2h until stable, then q4–6h for 48h
- CK q6h until trending down (peak typically 24–72h post-extrication; CK >5,000 U/L = AKI risk; CK >15,000 = high AKI risk)
- Urine output hourly (Foley catheter mandatory)
- Urine pH q4h (target >6.5 with bicarbonate therapy)
- Creatinine daily (AKI onset typically 24–72h)
- Ionized calcium q6–8h (symptomatic hypocalcemia monitoring)

## Treatment

**Pre-Extrication (Field):**
- NS 1–1.5 L/h IV (begin immediately, before release of crush)
- Calcium gluconate 10% 30 mL (3 g) IV — administer prophylactically before extrication if entrapment >4h (pre-emptive membrane stabilization for anticipated hyperkalemia)
- Attach cardiac monitor, have defibrillator at bedside
- Prepare medications for hyperkalemia (insulin/dextrose, sodium bicarbonate, additional calcium)

**Post-Extrication — Fluid Resuscitation:**
- NS 1–1.5 L/h (adults) for first 6h, then titrate to UOP >200–300 mL/h
- Total volume: 6–12 L in first 24h for severe bilateral crush
- Avoid LR (contains potassium — even 4 mEq/L is contraindicated in hyperkalemic patient)
- Avoid potassium-containing fluids entirely
- Monitor for pulmonary edema with serial chest auscultation and CXR if suspicious

**Urine Alkalinization:**
- Sodium bicarbonate 150 mEq in 1 L D5W at 200 mL/h
- Target urine pH >6.5 (check q4h)
- Hold if serum pH >7.50 or ionized calcium critically low (<0.8 mmol/L)
- Mannitol 20% 1 g/kg IV over 30 min: osmotic diuretic to maintain urine flow. Use cautiously — withhold if patient is anuric (accumulates and causes osmotic injury). Some protocols use mannitol 0.5 g/kg q6h as continuous adjunct.

**Hyperkalemia Management:**
- Calcium gluconate 10% 30 mL IV over 2–3 min for ECG changes (repeat q5min as needed)
- Regular insulin 10 units IV + D50 50 mL IV push
- Sodium bicarbonate 50 mEq IV over 5 min (if pH <7.2)
- Albuterol 10–20 mg nebulized
- Emergent hemodialysis if K+ >6.5 with ECG changes refractory to above, or if anuric with rising K+

**Renal Replacement Therapy:**
- Indications: anuria >6h despite fluid resuscitation, refractory hyperkalemia, refractory metabolic acidosis (pH <7.1), fluid overload with pulmonary edema
- Continuous renal replacement therapy (CRRT) preferred in hemodynamically unstable patients
- Intermittent hemodialysis (IHD) if hemodynamically stable — more efficient potassium and myoglobin clearance
- Dialysis requirements may persist 2–6 weeks; most patients recover renal function

**Compartment Syndrome:**
- Fasciotomy for compartment pressure >30 mmHg or delta pressure (diastolic - compartment) <30 mmHg
- Four-compartment fasciotomy for lower leg, two-compartment for forearm
- Leave fasciotomy wounds open; delayed primary closure or skin grafting at 3–7 days
- Fasciotomy in MCI setting: damage control approach — complete all fasciotomies before definitive wound management

**Amputation:**
- Indications: non-viable limb (mangled, pulseless, cold, no Doppler signal after reperfusion), gas gangrene, uncontrollable sepsis from necrotic limb
- Field amputation: last resort when extrication impossible and patient deteriorating
- Tourniquet proximal to amputation site before release

## Disposition

**All crush syndrome patients require ICU admission:**
- Continuous cardiac monitoring (hyperkalemia can recur for 48–72h)
- Hourly urine output measurement
- Serial K+, CK, creatinine
- Dialysis access (temporary dialysis catheter placement on admission)
- Nephrology consultation within 6 hours of admission

**Disposition by Severity:**

| Presentation | Disposition |
|-------------|------------|
| Entrapment <1h, single limb, normal CK, normal K+ | ED observation 12–24h with serial CK and K+. Discharge if CK trending down and UOP adequate. |
| Entrapment 1–4h, CK >5,000 | Admit to ICU or step-down. IV fluids, urine alkalinization, serial labs. Nephrology consult. |
| Entrapment >4h, bilateral LE, CK >15,000 | ICU. Aggressive resuscitation. Prepare for dialysis. High mortality risk. |
| Hyperkalemia with ECG changes | ICU. Emergent treatment. Dialysis catheter placement. |
| Anuric >6h despite fluid resuscitation | ICU + emergent hemodialysis |

**MCI-Specific Disposition:**
- Earthquake/structural collapse MCIs generate waves of crush patients as extrication proceeds over 24–72h
- Field hospitals must have dialysis capability — the 1999 Marmara earthquake required 477 dialysis sessions for 462 crush patients
- Patients extracted alive after 24–72h of entrapment represent the highest-acuity cohort — pre-extrication IV fluid and prophylactic calcium gluconate are mandatory
- Regional distribution: send crush patients to hospitals with dialysis units. A facility without nephrology and dialysis capability cannot manage crush syndrome.
- Anticipate dialysis demand: each crush patient may require 3–15 dialysis sessions. 50 crush patients × 10 sessions = 500 dialysis slots over 3–4 weeks.

## Pitfalls

1. **Extricating without pre-rescue IV fluid resuscitation.** This is the most lethal error in crush syndrome management. A patient trapped for 6 hours with bilateral leg compression appears stable while trapped. Removing the rubble without IV pre-loading releases a potassium bolus that causes cardiac arrest within minutes. Every urban search and rescue team must carry IV fluids, and paramedic access to the patient must occur before extrication begins.

2. **Using Lactated Ringer's for resuscitation.** LR contains 4 mEq/L potassium. In a patient whose serum K+ may reach 7–8 mmol/L upon reperfusion, every milliequivalent matters. Use NS exclusively. Avoid all potassium-containing IV fluids, IV medications with potassium (potassium penicillin), and potassium-sparing diuretics.

3. **Aggressively correcting hypocalcemia.** Serum calcium drops because calcium deposits in damaged muscle — this is a redistribution phenomenon, not a depletion. Infusing calcium drives more calcium into necrotic tissue, worsening local injury. Treat only for symptomatic hypocalcemia (tetany, seizures, hemodynamically significant QTc prolongation). Asymptomatic hypocalcemia in crush syndrome is expected and does not require treatment.

4. **Relying on urine dipstick to rule out myoglobinuria.** Urine dipstick detects heme — it cannot distinguish hemoglobin from myoglobin. A positive dipstick with no RBC on microscopy indicates myoglobinuria. But: early in crush syndrome, before renal injury develops, urine may be clear despite massive CK elevation. CK >5,000 U/L warrants aggressive hydration regardless of urine appearance.

5. **Delaying nephrology consultation and dialysis access.** Crush syndrome AKI develops over 24–72h. If dialysis catheter placement and nephrology involvement are delayed until the patient becomes anuric and hyperkalemic, the window for optimal management is lost. Place a temporary dialysis catheter on ICU admission for any patient with CK >15,000 or bilateral limb involvement, even before AKI develops.

6. **Overlooking compartment syndrome in adjacent, uninjured limbs.** Massive fluid resuscitation (6–12 L/day) causes generalized edema. Compartment syndrome can develop in limbs that were not directly crushed — the fluid resuscitation itself raises compartment pressures. Check compartment pressures in all four extremities, not just the crush-injured limbs.

### System Overwhelm

Structural collapse MCIs produce a unique resource crisis centered on dialysis capacity:

- **Dialysis surge:** The 1999 Marmara earthquake generated 477 patients requiring dialysis, overwhelming the entire regional nephrology infrastructure. The International Society of Nephrology Renal Disaster Relief Task Force was created in response. In any structural collapse MCI, assess regional dialysis capacity within the first 6 hours and request supplemental machines, supplies, and staff before demand exceeds supply.
- **Fluid supply:** A single bilateral crush patient requires 6–12 L NS in the first 24h. 20 crush patients = 120–240 L NS (120–240 1-L bags). Standard ED supply: 50–100 bags. Request resupply from warehouse, regional mutual aid, and state stockpile simultaneously.
- **Delayed extrication waves:** Earthquake extrications continue for 72–96h (survivors found alive at day 3–4 are well-documented). Each wave produces a new cohort of crush patients, often more severely affected than earlier cohorts (longer entrapment). Hospitals must not demobilize after the initial wave. Reserve ICU beds and dialysis capacity for late rescues.
- **Field dialysis:** In austere or resource-limited settings, peritoneal dialysis is an alternative when hemodialysis is unavailable. Place Tenckhoff catheter or improvise with large-bore abdominal drain. PD is less efficient for potassium clearance but buys time in mass casualty settings where HD machines are overwhelmed.
- **Blood bank impact:** Crush patients with DIC require massive transfusion capability. Combined with the hemorrhagic trauma patients from the same structural collapse event, blood product demand is extreme.
- **Rehabilitation burden:** Crush syndrome survivors face weeks to months of dialysis, multiple surgeries (fasciotomy, debridement, amputation, skin grafting), and prolonged rehabilitation. The long-term care burden from a single earthquake can overwhelm rehabilitation infrastructure for years.
