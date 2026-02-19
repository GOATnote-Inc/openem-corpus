---
id: tetanus
condition: Tetanus
aliases: [lockjaw, generalized tetanus, cephalic tetanus, neonatal tetanus]
icd10: [A35, A34, P95]
esi: 2
time_to_harm: "< 24 hours"
mortality_if_delayed: "10-70% depending on severity; generalized tetanus mortality 10-20% with ICU care, up to 50% without"
category: infectious
track: tier1
sources:
  - type: cdc
    ref: "CDC Tetanus — For Clinicians. Centers for Disease Control and Prevention, 2024"
  - type: review
    ref: "Thwaites CL, Loan HT. Eradication of tetanus. Br Med Bull 2015;116:69-77"
    pmid: "26598733"
  - type: review
    ref: "Cook TM et al. Tetanus: a review of the literature. Br J Anaesth 2001;87(3):477-487"
    pmid: "11517134"
  - type: pubmed
    ref: "Rodrigo C et al. Pharmacological management of tetanus: an evidence-based review. Crit Care 2014;18(2):217"
    pmid: "24829069"
  - type: guideline
    ref: "CDC. Tetanus: Prevention — Prophylaxis Guide. MMWR 2018;67(2):1-44 (ACIP Recommendations)"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: B
validation:
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  schema_version: "2.0"
  guideline_version_reference: null
  provenance_links: []
---
# Tetanus

## Recognition

**Pathophysiology:** Clostridium tetani (anaerobic, spore-forming gram-positive bacillus) produces tetanospasmin, a neurotoxin that binds irreversibly to presynaptic inhibitory interneurons in the spinal cord and brainstem, blocking release of GABA and glycine. Loss of inhibitory input causes unopposed motor neuron firing, producing sustained muscle contraction and spasm. Toxin also affects the autonomic nervous system. Once bound, toxin cannot be neutralized — recovery requires new nerve terminal growth (weeks).

**Incubation:** 3-21 days (median 7-10 days). Shorter incubation correlates with more severe disease and higher mortality.

**Clinical Forms:**

| Form | Features | Frequency |
|------|----------|-----------|
| Generalized tetanus | Trismus (lockjaw), risus sardonicus, opisthotonus, generalized spasms, autonomic instability | 80% of cases |
| Localized tetanus | Rigidity confined to muscles near wound site; may progress to generalized | Uncommon |
| Cephalic tetanus | Cranial nerve palsies (especially CN VII), follows head/face wounds; high risk of progression to generalized | Rare |
| Neonatal tetanus | Contaminated umbilical stump in infants of unimmunized mothers; poor feeding, rigidity, spasms at 3-14 days of life | Rare in developed countries |

**Generalized Tetanus Progression:**
- **Early:** Trismus (masseter spasm preventing jaw opening) — most common presenting symptom. Dysphagia, neck stiffness, shoulder rigidity.
- **Intermediate:** Risus sardonicus (sustained facial muscle spasm producing a grimace), opisthotonus (arching of back from paraspinal spasm), abdominal rigidity.
- **Severe:** Generalized reflex spasms triggered by minimal stimuli (noise, touch, light). Laryngospasm with airway compromise. Fractures from sustained contraction force.
- **Autonomic dysfunction** (occurs in severe cases, typically days 7-14): labile hypertension, tachycardia alternating with bradycardia, diaphoresis, hyperthermia, cardiac arrest. Leading cause of death in treated patients.

**Risk Factors:**
- Inadequate immunization (no primary series or no booster within 10 years)
- Elderly (waning immunity — anti-tetanus antibody levels decline with age)
- Immigrants from countries without routine vaccination
- IV drug users (especially skin-popping, contaminated heroin)
- Puncture wounds, crush injuries, burns, frostbite, devitalized tissue
- Contaminated wounds (soil, feces, saliva)
- Neonates of unimmunized mothers (umbilical stump contamination)

**Ablett Classification (Severity):**

| Grade | Features |
|-------|----------|
| I (Mild) | Mild trismus, no spasms, no dysphagia, no respiratory distress |
| II (Moderate) | Moderate trismus, short spasms, mild dysphagia, mild respiratory compromise, tachycardia > 120 |
| III (Severe) | Severe trismus, prolonged reflex spasms, severe dysphagia, apneic spells, tachycardia > 140, autonomic instability |
| IV (Very severe) | Grade III features plus severe autonomic instability with cardiovascular involvement |

## Critical Actions

1. **Clinical diagnosis — do not wait for lab confirmation.** No confirmatory test exists. Diagnosis is based on clinical presentation (trismus, spasms, rigidity) in a patient with inadequate immunization and a compatible wound history. Wound culture for C. tetani is positive in < 30% of cases.
2. **Administer TIG (tetanus immune globulin) 500 units IM immediately** — inject at a separate site from the vaccine. TIG neutralizes circulating unbound toxin only. Once toxin is bound to nerve terminals it is irreversible. Early administration is critical.
3. **Administer Tdap vaccine** — at a different anatomic site from TIG. Tetanus infection does not confer immunity. Begin or complete the primary vaccination series.
4. **Wound debridement** — remove foreign bodies and devitalized tissue to eliminate the anaerobic environment supporting C. tetani spore germination and toxin production.
5. **Start metronidazole 500 mg IV q6h x 7-10 days** — kills vegetative C. tetani and halts further toxin production. Preferred over penicillin G (penicillin is a GABA antagonist and may theoretically worsen spasms).
6. **Benzodiazepines for spasm control** — diazepam 5-10 mg IV q1-2h PRN (or midazolam infusion 0.1-0.3 mg/kg/hr). Enhances GABA activity to counteract toxin effects. Large cumulative doses often required.
7. **Secure the airway early** — patients with severe trismus, laryngospasm, or frequent spasms require early intubation. Anticipate prolonged mechanical ventilation (2-6 weeks). Tracheostomy often needed.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Strychnine poisoning | Mimics generalized tetanus (spasms, opisthotonus) but no trismus. Rapid onset (15-30 min). Toxicology screen positive. Complete muscle relaxation between spasms (unlike tetanus). |
| Dystonic drug reaction | Acute dystonia from metoclopramide, haloperidol, phenothiazines. Responds to diphenhydramine 50 mg IV. No wound history, no autonomic instability. |
| Dental/peritonsillar abscess | Trismus from local infection. Fever, sore throat, asymmetric tonsillar swelling. No generalized rigidity or spasms. |
| Meningitis/encephalitis | Neck stiffness (meningismus, not sustained rigidity), fever, headache, altered mental status. CSF abnormalities present. No trismus. |
| Rabies | Hydrophobia, aerophobia, encephalitic form with agitation. Animal bite history. No sustained rigidity between spasms. |
| Hypocalcemic tetany | Chvostek/Trousseau signs, carpopedal spasm. Low serum calcium. No trismus, no opisthotonus. |
| Neuroleptic malignant syndrome | Hyperthermia, lead-pipe rigidity, AMS, autonomic instability. Recent antipsychotic use. Elevated CK. |
| Stiff person syndrome | Chronic progressive truncal rigidity, stimulus-sensitive spasms. Anti-GAD antibodies positive. Insidious onset over months. |
| Temporomandibular joint disorder | Trismus with jaw pain. No fever, no rigidity, no spasms. |

## Workup

**Tetanus is a clinical diagnosis. No laboratory test confirms or excludes the diagnosis.**

**Labs (supportive, not diagnostic):**
- CBC — leukocytosis may be present (nonspecific)
- BMP — monitor electrolytes (hyponatremia from SIADH, metabolic derangements from prolonged spasm)
- CK — elevated from sustained muscle contraction and rhabdomyolysis
- Lactate — elevated with prolonged spasm
- Blood gas — respiratory acidosis from hypoventilation, metabolic acidosis from prolonged spasm
- Urinalysis — myoglobinuria screening
- Blood cultures — usually negative (C. tetani bacteremia is rare)
- Serum tetanus antibody level — a level >= 0.1 IU/mL makes tetanus unlikely (but does not exclude it; assays are not standardized for acute diagnosis and results are rarely available in time to guide ED management)

**Wound culture:** Culture wound for C. tetani if possible, but positive in < 30%. A negative culture does not exclude tetanus.

**Imaging:**
- CXR — aspiration pneumonia screening, particularly if spasms involve respiratory muscles
- CT head — only if diagnostic uncertainty (to exclude CNS pathology)

**No wound identified in ~20% of tetanus cases.** Absence of an obvious wound does not exclude the diagnosis.

## Treatment

**Neutralize Unbound Toxin:**
- TIG (tetanus immune globulin, human) 500 units IM — single dose, separate anatomic site from vaccine. Some sources recommend 3,000-6,000 units but 500 units is sufficient per WHO guidance. Intrathecal TIG (250-500 units) has shown benefit in some studies but is not standard practice.

**Active Immunization:**
- Tdap 0.5 mL IM — give at a different injection site from TIG. If primary series incomplete, complete the 3-dose series (Tdap, then Td at 4 weeks, then Td at 6-12 months).

**Wound Management:**
- Thorough surgical debridement of devitalized tissue and foreign material
- Irrigation
- Do not close contaminated wounds primarily

**Antibiotic Therapy (to halt toxin production):**
- **First-line:** Metronidazole 500 mg IV q6h x 7-10 days
- **Alternative:** Penicillin G 2-4 million units IV q4-6h x 7-10 days (less preferred — penicillin is a GABA antagonist)
- **Penicillin allergy:** Doxycycline 100 mg IV q12h

**Spasm Control:**
- **First-line:** Diazepam 5-10 mg IV q1-2h PRN (doses up to 500 mg/day may be required in severe cases) or midazolam continuous infusion 0.1-0.3 mg/kg/hr IV, titrate to spasm suppression
- **Refractory spasms:** Neuromuscular blockade — vecuronium 0.1 mg/kg IV bolus then 0.05-0.1 mg/kg/hr infusion, or cisatracurium 0.15 mg/kg IV bolus then 1-3 mcg/kg/min. Requires intubation and mechanical ventilation. Avoid succinylcholine (risk of hyperkalemia).
- **Adjunct:** Intrathecal baclofen 500-2000 mcg/day via lumbar catheter (limited availability, specialized centers)
- **Dantrolene** 1-2 mg/kg IV q6h — acts peripherally on muscle, may reduce rigidity

**Autonomic Dysfunction Management:**
- **Magnesium sulfate** 5 g IV loading dose over 20 minutes, then 2-3 g/hr continuous infusion, titrate to clinical effect. Monitor patellar reflexes and serum magnesium (target 2-4 mmol/L). Reduces catecholamine release and stabilizes autonomic swings.
- **Labetalol** 0.25-1 mg/min IV infusion — for persistent hypertension/tachycardia. Avoid pure beta-blockers (risk of unopposed alpha stimulation and cardiac arrest).
- **Morphine** 0.5-1 mg/kg/hr IV infusion — sympatholytic effect
- **Clonidine** 0.3 mg q8h via NG tube — centrally acting alpha-2 agonist
- Avoid short-acting agents — autonomic storms are labile and overshoot is dangerous

**Airway Management:**
- Early intubation for Ablett Grade III-IV (severe trismus, laryngospasm, frequent spasms, respiratory compromise)
- Expect prolonged mechanical ventilation (2-6 weeks while toxin effect resolves)
- Early tracheostomy (within first week) if prolonged ventilation anticipated
- Minimize stimulation: dark, quiet room; minimize suctioning and handling

**Supportive Care:**
- DVT prophylaxis — enoxaparin 40 mg SC daily (prolonged immobilization)
- Nutritional support — early enteral feeding via NG tube; high-calorie needs (sustained muscle contraction increases metabolic demand)
- Stress ulcer prophylaxis
- Physical therapy after spasm resolution to address contractures

## Disposition

**ICU Admission — All patients with:**
- Generalized tetanus (any grade)
- Spasms requiring parenteral benzodiazepines
- Dysphagia or airway compromise
- Autonomic instability
- Need for mechanical ventilation

**Floor Admission:**
- Localized tetanus without progression (monitor closely for 48-72 hours — may generalize)

**Duration:**
- ICU stay typically 3-6 weeks for severe generalized tetanus
- Total hospitalization 4-8 weeks
- Prolonged rehabilitation may be required

**Discharge Requirements:**
- Resolution of spasms
- Autonomous ventilation
- Completion of active immunization plan documented
- Outpatient follow-up arranged for vaccine series completion

**Prognosis:**
- Mortality: generalized tetanus 10-20% with modern ICU care (higher in elderly, neonates, and those with short incubation periods)
- Survivors generally recover fully but recovery is slow (weeks to months)
- Tetanus does NOT confer natural immunity — patients must be vaccinated during convalescence

**Reportable Disease:** Tetanus is a nationally notifiable condition in the United States. Report all cases to the local/state health department.

## Pitfalls

1. **Failing to recognize tetanus due to its rarity.** Fewer than 30 cases per year in the US. Emergency physicians may never see a case in their career. Any patient with trismus, rigidity, or reflex spasms — especially with poor immunization history — must be evaluated for tetanus.

2. **Waiting for lab confirmation before treating.** No rapid confirmatory test exists. Wound cultures are positive in fewer than 30% of cases. Serum antibody results take days and are not validated for acute diagnosis. Treatment must begin on clinical suspicion alone.

3. **Administering TIG and Tdap at the same injection site.** TIG will neutralize the vaccine antigen, blunting the immune response. TIG and vaccine must be given at separate anatomic sites (different limbs).

4. **Choosing penicillin over metronidazole as the antibiotic.** Penicillin G is a GABA antagonist and may theoretically potentiate spasms by further reducing inhibitory neurotransmission. Metronidazole is the preferred antibiotic for tetanus.

5. **Underestimating benzodiazepine requirements.** Patients with severe tetanus may need diazepam doses exceeding 200-500 mg/day. Standard anxiolytic dosing is grossly insufficient. Titrate to spasm suppression, not to a fixed dose ceiling. Mechanical ventilation allows aggressive dosing without fear of respiratory depression.

6. **Using succinylcholine for intubation.** Prolonged immobilization and denervation-like pathophysiology in tetanus may cause upregulation of extrajunctional acetylcholine receptors, risking hyperkalemic cardiac arrest with succinylcholine. Use rocuronium for rapid sequence intubation.

7. **Neglecting autonomic instability as a cause of death.** In ICU-managed patients, autonomic dysfunction (labile BP, tachycardia, bradycardia, cardiac arrest) is the leading cause of death, not respiratory failure. Magnesium sulfate infusion is first-line. Avoid short-acting beta-blockers, which can precipitate cardiac arrest during autonomic storms.

8. **Forgetting that tetanus infection does not confer immunity.** Unlike most infections, surviving tetanus does not produce protective antibody levels. Patients must receive active immunization (complete Tdap series) during hospitalization to prevent future episodes.

9. **Assuming absence of a wound excludes tetanus.** No identifiable wound or portal of entry is found in approximately 20% of tetanus cases. A clean exam does not rule out the diagnosis.

10. **Discharging without completing the vaccination series.** Patients who receive only TIG and a single Tdap dose remain vulnerable after antibody waning. Ensure documentation and follow-up plan for completing the full 3-dose primary series if not previously vaccinated.
