---
id: organophosphate-poisoning
condition: Organophosphate Poisoning
aliases: [OP poisoning, cholinergic toxidrome, nerve agent exposure, cholinesterase inhibitor poisoning, insecticide poisoning]
icd10: [T60.0X1A, T60.0X2A, T60.0X4A]
esi: 1
time_to_harm: "< 30 minutes"
mortality_if_delayed: "20-40% without atropinization"
category: toxicologic
track: tier1
sources:
  - type: guideline
    ref: "WHO Clinical Management of Acute Pesticide Intoxication: Prevention of Suicidal Behaviours (2008)"
  - type: pubmed
    ref: "Eddleston M et al. Management of acute organophosphorus pesticide poisoning. Lancet 2008;371(9612):597-607"
    pmid: "17706760"
  - type: pubmed
    ref: "Eddleston M et al. Oximes in acute organophosphorus pesticide poisoning: a systematic review of clinical trials. QJM 2002;95(5):275-283"
    pmid: "11978898"
  - type: guideline
    ref: "CHEMM (Chemical Hazards Emergency Medical Management) Nerve Agent Guidelines. US DHHS/ASPR (2023)"
  - type: pubmed
    ref: "Roberts DM, Aaron CK. Management of acute organophosphorus pesticide poisoning. BMJ 2007;334(7594):629-634"
    pmid: "17379909"
last_updated: "2026-02-18"
compiled_by: agent
reviewed_by: "Brandon Dent, MD — Board Certified Emergency Medicine"
review_date: "2026-02-27"
risk_tier: A
validation:
  automated_consistency_check: "2026-02-18"
  dose_range_validator: "2026-02-19"
  unit_normalization_check: "2026-02-19"
  cross_file_consistency_check: "2026-02-19"
  citation_presence_check: "2026-02-19"
  duplicate_content_check: "2026-02-19"
  outlier_detection_flag: clear
  schema_version: "2.0"
  provenance_links: []
---
# Organophosphate Poisoning

## Recognition

**Pathophysiology:** Organophosphates (OPs) irreversibly inhibit acetylcholinesterase, causing accumulation of acetylcholine at muscarinic receptors (parasympathetic end-organs), nicotinic receptors (NMJ, sympathetic ganglia), and central nervous system. "Aging" of the OP-enzyme complex makes inhibition permanent within hours (varies by agent).

**Cholinergic Toxidrome — DUMBBBELS (muscarinic):**
- **D**iarrhea
- **U**rination
- **M**iosis (pinpoint pupils — hallmark finding)
- **B**radycardia (early; tachycardia also occurs from nicotinic stimulation)
- **B**ronchospasm
- **B**ronchorrhea (copious secretions — the killer)
- **E**mesis
- **L**acrimation
- **S**alivation

**Nicotinic Effects (Killer N's):**
- Muscle fasciculations, weakness, paralysis (including diaphragm — respiratory failure)
- Tachycardia, hypertension (ganglionic stimulation)

**CNS Effects:**
- Anxiety, confusion, seizures, coma, central apnea

**Garlic/Petroleum Odor:** Many OP pesticides have a distinctive garlic-like or solvent smell on patient's skin, clothes, or breath.

**Timeline:**
- Symptom onset: minutes to hours depending on route (inhalation fastest, dermal slowest, ingestion intermediate)
- Intermediate syndrome: 24-96 hours post-exposure, proximal muscle weakness and respiratory failure after initial cholinergic crisis resolves
- Delayed polyneuropathy (OPIDN): 2-3 weeks post-exposure, distal motor and sensory neuropathy

**Sources:** Agricultural pesticides (malathion, parathion, chlorpyrifos), nerve agents (sarin, VX, novichok), carbamate insecticides (similar presentation but reversible inhibition).

## Critical Actions

1. **Decontaminate immediately** — remove all clothing, wash skin with soap and water. Staff must wear PPE (gown, gloves, N95 minimum). Do NOT allow contaminated patient into resuscitation area without decontamination.
2. **Atropine 2-5 mg IV, double the dose every 3-5 minutes** until bronchorrhea clears and oxygenation improves. There is NO maximum dose. Severely poisoned patients may require 100+ mg in the first 24 hours. Target: dry lungs, HR >80, SpO2 >90%. Do NOT use pupil size as an atropine endpoint.
3. **Pralidoxime (2-PAM) 30 mg/kg IV (max 2g) over 15-30 minutes**, then infusion 8-10 mg/kg/hr. Reactivates acetylcholinesterase before "aging" occurs. Most effective within 12-24 hours of exposure (varies by agent). Continue for 24-48 hours minimum.
4. **Secure the airway** — intubate early if bronchorrhea is uncontrolled, respiratory muscle weakness, or GCS <8. Avoid succinylcholine (prolonged paralysis — pseudocholinesterase is inhibited). Use rocuronium 1.2 mg/kg IV.
5. **Benzodiazepines for seizures** — diazepam 10 mg IV or midazolam 5-10 mg IV/IM. Repeat as needed. OP-induced seizures are resistant to phenytoin.
6. **Continuous cardiorespiratory monitoring** — atropine drip after initial bolusing, mechanical ventilation support.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Carbamate poisoning | Identical presentation but shorter duration; cholinesterase inhibition is reversible; 2-PAM still indicated |
| Nerve agent exposure | Same mechanism as OP; higher potency, faster onset; mass casualty scenario |
| Mushroom poisoning (muscarinic) | Cholinergic symptoms without nicotinic effects; Inocybe/Clitocybe species |
| Opioid overdose | Miosis but no secretions, no fasciculations; responds to naloxone |
| Nicotine poisoning | Initial cholinergic stimulation then paralysis; vaping/e-cigarette liquid ingestion in children |
| Status epilepticus | Seizures without cholinergic toxidrome; may cause incontinence and salivation |
| Myasthenic crisis | Weakness and respiratory failure without muscarinic symptoms; responds to edrophonium (NOT OP) |

## Workup

**Labs:**
- RBC cholinesterase (true/erythrocyte AChE) — reflects tissue enzyme inhibition, confirms diagnosis. Depressed levels confirm exposure.
- Plasma cholinesterase (butyrylcholinesterase/pseudocholinesterase) — drops faster, more sensitive for acute exposure but less specific (depressed by liver disease, pregnancy, genetic variant)
- ABG — monitor respiratory acidosis, oxygenation
- BMP — electrolytes, glucose, renal function
- CBC — leukocytosis common
- Lactate — marker of tissue hypoperfusion
- ECG — QTc prolongation, ST changes, dysrhythmias (atrial fibrillation, torsades de pointes, heart block)
- Lipase — pancreatitis reported in severe OP poisoning

**Monitoring:**
- Continuous pulse oximetry and telemetry
- Strict I&O — atropine decreases secretions but does not treat the underlying cholinergic excess at nicotinic receptors
- Serial lung auscultation — bronchorrhea is the primary death mechanism and the treatment target

**Imaging:**
- CXR — pulmonary edema, aspiration pneumonitis
- CT head — if seizures or AMS with unclear history

## Treatment

**Decontamination:**
- Full skin decontamination with soap and water — critical to prevent ongoing dermal absorption and secondary contamination of healthcare workers
- Remove and bag all clothing
- Activated charcoal 1 g/kg PO (max 50g) within 1 hour of oral ingestion if airway protected
- Gastric lavage ONLY if massive ingestion within 1 hour and patient intubated

**Atropine (Muscarinic Antagonist):**
- Initial: 2-5 mg IV bolus (pediatric: 0.02-0.05 mg/kg, minimum 0.1 mg)
- Double the dose every 3-5 minutes until secretions dry and oxygenation improves
- Severely poisoned patients: may need 20-100+ mg in the first hour
- Maintenance: atropine infusion at 10-20% of the total loading dose per hour
- Target endpoints: clear lungs (no rales/rhonchi), HR >80, SBP >80, SpO2 >90%
- Do NOT use pupil size or heart rate as sole endpoints — miosis may persist, tachycardia causes under-dosing

**Pralidoxime (2-PAM, Oxime):**
- 30 mg/kg IV (max 2g) over 15-30 minutes, then continuous infusion 8-10 mg/kg/hr
- Reactivates acetylcholinesterase by cleaving the OP-enzyme bond
- Must be given before "aging" — timing varies: sarin ages in 5 hours, parathion in 12 hours, VX in 48 hours
- Continue for minimum 24-48 hours; longer for fat-soluble OPs (fenthion, parathion)
- Side effects at rapid infusion: hypertension, tachycardia, muscle rigidity

**Seizure Management:**
- Diazepam 10 mg IV (pediatric: 0.2-0.5 mg/kg) or midazolam 5-10 mg IV/IM
- Repeat every 5-10 minutes as needed
- Phenytoin/fosphenytoin is INEFFECTIVE for OP seizures
- Refractory seizures: propofol or pentobarbital infusion

**Airway Management:**
- Intubate early — bronchorrhea and respiratory muscle paralysis are the primary causes of death
- Suction copious secretions before and during intubation
- Avoid succinylcholine (pseudocholinesterase inhibited — prolonged paralysis >6 hours)
- Use rocuronium 1.2 mg/kg IV for RSI
- Expect high ventilator secretion burden — frequent suctioning required

## Disposition

**ICU Admission (all symptomatic OP poisoning):**
- Continuous atropine infusion titration
- Mechanical ventilation (frequently required)
- Pralidoxime infusion monitoring
- Watch for intermediate syndrome (24-96 hours): proximal weakness, neck flexion weakness, respiratory failure after initial improvement
- Monitor for recurrence of cholinergic symptoms (fat-soluble OPs have prolonged toxicity)

**Toxicology Consultation:**
- All confirmed or suspected OP poisoning
- Guidance on atropine titration and pralidoxime duration
- Identification of specific agent for aging timeline

**Decontamination Team/Hazmat:**
- Mass casualty or nerve agent scenarios
- Ensure ED decontamination before patient entry

**Psychiatry (post-stabilization):**
- Intentional ingestion requires psychiatric evaluation after medical clearance

**Never discharge a patient with confirmed OP poisoning from the ED.** Intermediate syndrome can cause respiratory arrest 24-96 hours after exposure.

## Pitfalls

1. **Under-dosing atropine.** The most common lethal error. Bronchorrhea — not bradycardia — kills these patients. There is no maximum dose of atropine. Double the dose every 3-5 minutes until lungs are clear. Patients may need hundreds of mg.

2. **Using pupil size as an atropine endpoint.** Miosis may persist despite adequate atropinization. Titrate to clear lungs, adequate oxygenation, and hemodynamic stability. Pupil size is unreliable.

3. **Contaminating the ED and staff.** OP-contaminated patients can cause secondary poisoning of healthcare workers through dermal contact with skin, clothing, or emesis. Full PPE and decontamination BEFORE entry to resuscitation area.

4. **Using succinylcholine for RSI.** Pseudocholinesterase is inhibited — succinylcholine will cause prolonged paralysis (hours instead of minutes). Rocuronium is the agent of choice.

5. **Stopping pralidoxime too early.** Fat-soluble OPs (fenthion, parathion) redistribute from adipose tissue, causing recurrent toxicity. Continue 2-PAM infusion for at least 24-48 hours and longer for fat-soluble agents. Clinical recurrence is the signal to continue.

6. **Discharging after apparent recovery without monitoring for intermediate syndrome.** Occurs 24-96 hours post-exposure: proximal muscle weakness, neck flexor weakness, cranial nerve palsies, and respiratory failure. All OP-poisoned patients need ICU monitoring for at least 72 hours.

7. **Using phenytoin for seizures.** OP seizures are mediated by cholinergic excess, not sodium channel dysfunction. Benzodiazepines are first-line. Phenytoin is ineffective.

8. **Failing to recognize occult OP exposure.** Agricultural workers, pest control operators, or children with miosis, salivation, and unexplained respiratory distress — obtain cholinesterase levels. A garlic or solvent odor on the patient is a clue.

9. **Not measuring serial cholinesterase levels.** RBC cholinesterase confirms diagnosis and tracks recovery. Levels help determine when pralidoxime can be discontinued and when the patient is safe for step-down care.
