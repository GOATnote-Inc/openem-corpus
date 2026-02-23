---
id: salicylate-poisoning
condition: Salicylate Poisoning
aliases: [aspirin overdose, salicylate toxicity, ASA poisoning]
icd10: [T39.091A, T39.092A]
esi: 2
time_to_harm: "< 6 hours for severe toxicity; chronic toxicity insidious"
category: toxicologic
track: tier1
sources:
  - type: guideline
    ref: "American College of Medical Toxicology. ACMT Position Statement: Duration of Emergency Department Observation for Symptomatic Acetylsalicylic Acid (Aspirin) Overdose. J Med Toxicol 2020;16(3):321-324"
    pmid: "32130694"
  - type: pubmed
    ref: "Chyka PA et al. Salicylate poisoning: an evidence-based consensus guideline for out-of-hospital management. Clin Toxicol (Phila) 2007;45(2):95-131"
    pmid: "17364628"
  - type: pubmed
    ref: "Temple AR. Acute and chronic effects of aspirin toxicity and their treatment. Arch Intern Med 1981;141(3 Spec No):364-369"
    pmid: "7469627"
  - type: pubmed
    ref: "Greenberg MI, Hendrickson RG, Hofman M. Deleterious effects of endotracheal intubation in salicylate poisoning. Ann Emerg Med 2003;41(4):583-584"
    pmid: "12658265"
  - type: pubmed
    ref: "Dargan PI, Wallace CI, Jones AL. An evidenced based flowchart to guide the management of acute salicylate (aspirin) overdose. Emerg Med J 2002;19(3):206-209"
    pmid: "11971828"
last_updated: "2026-02-23"
compiled_by: agent
risk_tier: B
validation:
  schema_version: "2.0"
  outlier_detection_flag: clear
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  guideline_version_reference: null
  provenance_links: []
---
# Salicylate Poisoning

## Recognition

**Pathophysiology:** Salicylates uncouple oxidative phosphorylation (impair ATP synthesis, increase metabolic rate and heat production), inhibit the Krebs cycle (organic acidosis), and directly stimulate the respiratory center (primary respiratory alkalosis). The classic acid-base pattern is a mixed respiratory alkalosis and anion-gap metabolic acidosis. CNS penetration of salicylate increases with acidemia (un-ionized form crosses blood-brain barrier) — acidemia drives salicylate into the brain.

**Toxic Doses:**
- Acute ingestion: >150 mg/kg or >6.5 g in an adult = potentially toxic
- Serum level: >30 mg/dL = mild toxicity; >50 mg/dL = moderate; >70-80 mg/dL = severe; >100 mg/dL = HD threshold for acute ingestion
- Chronic toxicity: occurs at levels as low as 30-40 mg/dL in elderly or chronically ill patients — far more dangerous per level than acute ingestion

**Salicylate Sources Beyond Aspirin:**
- Methyl salicylate (oil of wintergreen): 1 tsp = ~7 g of salicylate — extremely concentrated; pediatric fatalities documented
- Bismuth subsalicylate (Pepto-Bismol)
- Topical salicylate creams (Bengay, Icy Hot) — systemic absorption possible, especially with occlusion or burns

**Clinical Presentation:**

*Mild-Moderate:*
- Tinnitus, hearing loss (most common early symptom)
- Nausea, vomiting, epigastric pain
- Hyperventilation (respiratory alkalosis — often initially noted as "breathing hard")
- Diaphoresis, flushing

*Severe:*
- Altered mental status (confusion, agitation, lethargy, coma)
- Pulmonary edema (noncardiogenic ARDS pattern)
- Cerebral edema
- Hyperthermia (uncoupled oxidative phosphorylation)
- Seizures
- Hypoglycemia (especially in pediatric patients)
- Coagulopathy (inhibits vitamin K-dependent factors)

*Chronic Toxicity (often misdiagnosed):*
- Elderly patient on therapeutic aspirin
- Encephalopathy, confusion, delirium mistaken for dementia or sepsis
- May lack GI symptoms; tinnitus often not reported
- Level may be only 30-50 mg/dL but clinical severity disproportionate
- High mortality if not diagnosed — check salicylate level in any elderly confused patient on aspirin

**Acid-Base:**
- Initial: respiratory alkalosis (direct medullary stimulation)
- Severe: mixed respiratory alkalosis + high anion-gap metabolic acidosis
- Terminal: pure metabolic acidosis as respiratory compensation fails (ominous)

## Critical Actions

1. **Activated charcoal 1 g/kg PO (max 50g)** if within 2 hours of acute ingestion and airway intact. For large ingestions or enteric-coated products, charcoal up to 4 hours may have benefit. Multi-dose activated charcoal (0.5 g/kg q4h x 2-3 doses) for bezoar-forming ingestions.

2. **Initiate urinary alkalinization** — NaHCO3 150 mEq (3 ampules of 50 mEq/50 mL) in 1 liter of D5W, infuse at 200-250 mL/hr. Target urine pH 7.5-8.0, serum pH <7.55. Ion trapping: alkaline urine traps ionized salicylate in tubular lumen, dramatically increasing renal clearance. Check urine pH every 1-2 hours. Monitor K+ — hypokalemia prevents achieving alkaline urine; replace aggressively (KCl 20-40 mEq IV/hr).

3. **Hemodialysis (HD) — absolute indications:**
   - Salicylate level >100 mg/dL (acute ingestion) or >60-70 mg/dL (chronic ingestion)
   - Altered mental status not explained by other cause
   - Pulmonary edema or respiratory failure
   - Renal failure preventing clearance
   - Persistent severe acidosis (pH <7.20) despite bicarbonate
   - Severe hypokalemia refractory to replacement
   - Clinical deterioration despite aggressive urinary alkalinization
   - Contact nephrology immediately for patients meeting any HD criterion.

4. **DO NOT intubate unless absolutely necessary.** Intubation in salicylate poisoning causes a paradoxical worsening: respiratory compensation (tachypnea to 40-60 breaths/min) is lost when the patient is sedated and placed on a ventilator. Even with aggressive hyperventilation settings, mechanical ventilation cannot match a driven spontaneous respiratory rate. Loss of respiratory alkalosis → pH drops → salicylate penetrates CNS → rapid deterioration → death. If intubation is required, have HD running before extubation or have it immediately available. Bag-valve-mask ventilate at maximum rate if needed as bridge to HD.

5. **Serial salicylate levels every 2 hours** until levels are falling. Enteric-coated preparations have delayed peak absorption; a 6-hour level may still be rising. Levels do not peak for 6-12 hours after large ingestions.

6. **Continuous glucose monitoring** — hypoglycemia (especially in children) occurs due to increased glucose utilization from uncoupled metabolism. Check point-of-care glucose every 1-2 hours.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Sepsis | No medication history, cultures positive, normal salicylate level |
| Diabetic ketoacidosis | Hyperglycemia, elevated ketones, no respiratory alkalosis component |
| Toxic alcohol (methanol/ethylene glycol) | Anion-gap acidosis, no respiratory alkalosis, specific osmol gap, no tinnitus |
| Isoniazid toxicity | Seizures predominant, anion-gap acidosis, INH exposure history |
| CNS infection | Meningismus, CSF abnormalities, normal salicylate level |
| Theophylline toxicity | Tachycardia, seizures, serum theophylline level elevated |
| Serotonin syndrome | Clonus, rigidity, hyperthermia, medication history |

## Workup

**Labs:**
- Serum salicylate level (quantitative) — stat, every 2 hours until falling
- Electrolytes, BMP — anion gap, bicarbonate, creatinine, glucose
- Arterial blood gas — assess respiratory alkalosis, metabolic acidosis, pH
- Urine pH — hourly during alkalinization therapy (target 7.5-8.0)
- Serum potassium — hypokalemia must be corrected to achieve urinary alkalinization
- CBC, INR — salicylates impair vitamin K-dependent factor synthesis
- Acetaminophen level — common co-ingestion in intentional overdose
- Lactate — elevated from uncoupled metabolism

**Note on the Done nomogram:** The Done nomogram (predicts toxicity from single acute ingestion level at timed intervals) has major limitations and is no longer relied upon in toxicology practice. Clinical symptoms and serial levels guide management.

**Imaging:**
- Chest X-ray — pulmonary edema (ARDS pattern); may be absent early
- CT head if focal neurological findings

## Treatment

**GI Decontamination:**
- Activated charcoal 1 g/kg PO (max 50g) within 2 hours; consider up to 4 hours for enteric-coated or large ingestions
- Multi-dose charcoal (0.5 g/kg q4h x 2-3 doses) for large or extended-release ingestions
- Whole bowel irrigation with polyethylene glycol for massive enteric-coated ingestions: 1-2 L/hr PO/NG until clear rectal effluent

**Urinary Alkalinization:**
- NaHCO3 150 mEq in 1L D5W at 200-250 mL/hr IV
- Check urine pH every 1-2 hours; titrate infusion rate to maintain urine pH 7.5-8.0
- Correct hypokalemia: add KCl 20-40 mEq to each liter; replace 20-40 mEq/hr IV as needed
- Hypokalemia prevents alkalinization — the kidneys exchange K+ for H+ when potassium-depleted, acidifying the urine despite bicarb infusion

**Hemodialysis:**
- Intermittent HD or continuous renal replacement therapy (CRRT)
- HD preferred for acute severe toxicity — clears salicylate rapidly
- HD indications as listed in Critical Actions above
- Salicylate half-life during HD: ~1-2 hours vs. 20+ hours in overdose without HD

**Symptomatic:**
- Fever: external cooling, acetaminophen (no NSAIDs) — but APAP may complicate hepatic monitoring
- Seizures: benzodiazepines (lorazepam 0.1 mg/kg IV, diazepam 0.1-0.2 mg/kg IV)
- Pulmonary edema: CPAP or BIPAP (avoid intubation — see Critical Actions); careful fluid management
- Hypoglycemia: dextrose IV (D50W 0.5-1 mL/kg, or D10W 2-4 mL/kg)

**Endpoints of Therapy:**
- Salicylate level <30 mg/dL and asymptomatic
- Normal acid-base status off bicarbonate infusion
- No symptoms of CNS toxicity

## Disposition

**Hemodialysis Unit/ICU:**
- Any patient meeting HD criteria (see Critical Actions)
- Pulmonary edema, respiratory failure
- Altered mental status
- Persistent acidosis (pH <7.30) despite treatment
- Seizures

**ICU/Monitored Setting:**
- Salicylate level >50 mg/dL (acute)
- Symptomatic (tachypnea, AMS, tinnitus with hemodynamic changes)
- Active urinary alkalinization
- Chronic salicylate toxicity (any level with symptoms)

**Observation/Discharge:**
- Acute ingestion: level <30 mg/dL, falling, asymptomatic, 6-hour observation minimum
- Must confirm level not still rising (repeated levels documented as falling)
- Psychiatric consultation if intentional

## Pitfalls

1. **Intubating a salicylate-poisoned patient with respiratory alkalosis.** Mechanical ventilation eliminates the patient's compensatory tachypnea. If you cannot match a respiratory rate of 40-60 breaths/min on the ventilator, the pH will plummet, CNS salicylate penetration will increase, and the patient will die. Avoid intubation. If you must intubate, call nephrology before you intubate — HD must be immediately available.

2. **Missing chronic salicylate toxicity in elderly patients.** Elderly patients on aspirin who present with confusion, agitation, or altered mental status have a 1-2% prevalence of salicylate toxicity. Levels as low as 30-40 mg/dL are dangerous in this population because of lower protein binding, reduced renal clearance, and pre-existing CNS vulnerability. Check a salicylate level in any older patient on aspirin with unexplained encephalopathy.

3. **Failing to correct hypokalemia before urinary alkalinization.** Potassium depletion prevents the kidneys from excreting an alkaline urine — no matter how much bicarbonate you give. The tubule will conserve potassium by exchanging H+ instead, acidifying the urine. Aggressive KCl replacement is a prerequisite for successful urinary alkalinization.

4. **Relying on the Done nomogram.** The Done nomogram was developed in 1960 for single acute ingestions with known timing and has poor predictive value. It misses chronic toxicity entirely. Clinical toxidrome and serial levels drive management — not nomogram predictions.

5. **Stopping serial levels too early.** Enteric-coated aspirin (most adult OTC aspirin) has highly variable absorption, and levels may continue to rise for 12+ hours. A 4-hour level that appears non-toxic can be followed by a 12-hour level in the severe range. Repeat levels every 2 hours until a clear downward trend is established.

6. **Underestimating methyl salicylate toxicity.** Oil of wintergreen is 98% methyl salicylate — a single teaspoon contains approximately 7,000 mg of salicylate. This is a life-threatening dose in a child. Topical products (Bengay) used with occlusion or heat can produce systemic toxicity in adults.