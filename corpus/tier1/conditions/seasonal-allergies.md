---
id: seasonal-allergies
condition: Seasonal Allergic Rhinitis
aliases: [allergic rhinitis, hay fever, seasonal allergic rhinitis]
icd10: [J30.1, J30.2, J30.5, J30.89]
esi: 5
time_to_harm: "N/A — benign IgE-mediated mucosal inflammation; see escalation_triggers for anaphylaxis differential"
category: allergic-immunologic
track: tier1
disposition_default: outpatient
escalation_triggers:
  - "Stridor or wheeze — anaphylaxis or upper airway angioedema until excluded; immediate epinephrine"
  - "Angioedema of tongue, lips, or larynx — anaphylaxis; immediate IM epinephrine 0.3 mg (adult) or 0.01 mg/kg (child, max 0.5 mg)"
  - "Hypotension (SBP <90 mmHg or >30% below baseline) — anaphylactic shock"
  - "Generalized urticaria extending beyond nasal/ocular mucosa — systemic allergic reaction, not rhinitis"
  - "Respiratory distress with oxygen saturation <95% — bronchospasm from anaphylaxis, asthma exacerbation"
  - "Altered mental status in context of allergen exposure — anaphylactic shock with end-organ hypoperfusion"
  - "New-onset nasal symptoms with unilateral presentation, bloody discharge, and nasal obstruction — nasal foreign body (children), neoplasm, or vasculitis (not rhinitis)"
confusion_pairs:
  - condition: allergic-reaction
    differentiators:
      - "Seasonal allergic rhinitis: confined to upper respiratory tract (nasal congestion, clear rhinorrhea, sneezing, ocular pruritus/tearing); no urticaria, no angioedema, no bronchospasm, no hemodynamic changes"
      - "Anaphylaxis: multi-system involvement; skin (generalized urticaria, angioedema); respiratory (bronchospasm, stridor, laryngeal edema); cardiovascular (hypotension, tachycardia, syncope); onset minutes to 2 hours after exposure; potentially fatal without immediate epinephrine"
      - "Seasonal allergic rhinitis: patient is hemodynamically stable; SpO2 normal; no urticaria; no angioedema beyond nasal mucosa"
      - "Anaphylaxis: World Allergy Organization criteria require involvement of ≥2 organ systems OR isolated hypotension after allergen exposure"
      - "Critical rule: nasal congestion + sneezing alone do not constitute anaphylaxis; anaphylaxis requires systemic involvement — do not withhold epinephrine if systemic signs are present, do not administer epinephrine for rhinitis alone"
sources:
  - type: guideline
    ref: "Brozek JL, Bousquet J, Agache I, et al. Allergic Rhinitis and its Impact on Asthma (ARIA) guidelines—2016 revision. J Allergy Clin Immunol. 2017;140(4):950-958."
    pmid: "28602936"
  - type: guideline
    ref: "Seidman MD, Gurgel RK, Lin SY, et al. Clinical practice guideline: allergic rhinitis. Otolaryngol Head Neck Surg. 2015;152(1 Suppl):S1-43."
    pmid: "25644617"
  - type: pubmed
    ref: "Pawankar R, Canonica GW, Holgate ST, Lockey R. WAO White Book on Allergy. World Allergy Organization; 2011."
  - type: pubmed
    ref: "Wheatley LM, Togias A. Clinical practice. Allergic rhinitis. N Engl J Med. 2015;372(5):456-463."
    pmid: "25629743"
  - type: pubmed
    ref: "Simons FE, Ardusso LR, Bilo MB, et al. World Allergy Organization anaphylaxis guidelines: summary. J Allergy Clin Immunol. 2011;127(3):587-593."
    pmid: "21377030"
last_updated: "2026-02-23"
compiled_by: agent
risk_tier: C
validation:
  schema_version: "2.0"
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  guideline_version_reference: "ARIA 2016 guidelines (current); AAO-HNS Clinical Practice Guideline 2015"
  provenance_links: []
---

## Recognition

Seasonal allergic rhinitis (SAR) is an IgE-mediated inflammatory response of the nasal mucosa to airborne allergens (pollen, mold spores) with a predictable seasonal pattern corresponding to regional pollen calendars. It affects 10-30% of adults and up to 40% of children in the United States. Perennial allergic rhinitis (PAR) follows the same pathophysiology but is triggered by year-round allergens (dust mites, cat/dog dander, cockroach, mold). In the emergency department, SAR presents as a non-urgent complaint or as a co-presentation alongside another chief concern. The primary task is exclusion of anaphylaxis when patients present acutely after allergen exposure.

### Typical Clinical Presentation
- Bilateral clear (not purulent) nasal congestion and rhinorrhea
- Paroxysmal sneezing (often in clusters of 3-10 consecutive sneezes)
- Nasal and palatal pruritus; "allergic salute" (upward rubbing of nose with palm)
- Ocular pruritus, tearing, and conjunctival injection (allergic conjunctivitis coexists in >50%)
- Seasonal pattern correlating with pollen season (tree pollen: early spring; grass pollen: late spring/summer; ragweed: late summer/fall; mold: late summer/fall)
- "Allergic shiners" (infraorbital darkening), "allergic crease" (horizontal nasal crease from chronic upward rubbing), Dennie-Morgan lines (infraorbital folds)
- Nasal mucosa: pale, bluish-gray, boggy turbinates; clear secretions

### What Allergic Rhinitis Does NOT Cause
- Fever (purulent rhinitis with fever = bacterial rhinosinusitis or viral URI)
- Unilateral symptoms (unilateral nasal obstruction = foreign body, polyp, or neoplasm)
- Bloody nasal discharge (epistaxis may co-occur with chronic rhinitis but not primary symptom)
- Urticaria, angioedema, bronchospasm, or hemodynamic instability

### ARIA Classification (Severity)
- **Intermittent**: symptoms <4 days/week or <4 consecutive weeks/year
- **Persistent**: symptoms >4 days/week AND >4 consecutive weeks/year
- **Mild**: none of the following impaired — sleep, daily activities, sport/leisure, work/school; no troublesome symptoms
- **Moderate-Severe**: any of the above impaired

## Critical Actions

1. Confirm hemodynamic stability: measure vital signs. Any tachycardia, hypotension, or oxygen desaturation in a patient presenting acutely after allergen exposure mandates anaphylaxis evaluation before attributing to rhinitis.
2. Examine mucous membranes: stridor, tongue/lip swelling, drooling, or uvular edema = immediate IM epinephrine.
3. Check skin: generalized urticaria (beyond the nasal/ocular area) = systemic allergic reaction = anaphylaxis protocol.
4. For straightforward chronic allergic rhinitis without any acute systemic concern: initiate or optimize pharmacotherapy and arrange primary care or allergy/immunology follow-up.

## When NOT to Escalate

Seasonal allergic rhinitis is appropriate for outpatient management when ALL of the following are met:
- Hemodynamically stable (no hypotension, no tachycardia beyond mild sympathetic response)
- SpO2 ≥95% on room air
- No stridor or wheeze
- No angioedema of tongue, lips, or larynx
- No generalized urticaria
- Symptoms confined to nasal and ocular mucosa (bilateral clear rhinorrhea, sneezing, nasal congestion, ocular pruritus)
- Patient not in anaphylactic exposure context (no known high-risk allergen ingestion or injection within past 2 hours)

Antihistamines, intranasal corticosteroids, and allergen avoidance are entirely adequate — emergency intervention is not warranted for isolated allergic rhinitis with no systemic signs.

## Differential Diagnosis

| Condition | Key Features | Distinguishing from Seasonal Allergic Rhinitis |
|-----------|-------------|------------------------------------------------|
| **Anaphylaxis** | Multisystem: urticaria, angioedema, bronchospasm, hypotension; onset within 2 hours of allergen exposure; potentially fatal | SAR: confined to nasal/ocular; no urticaria; no angioedema; hemodynamically stable |
| **Viral upper respiratory infection (common cold)** | Low-grade fever; myalgia; purulent nasal secretions after 3-4 days; sore throat; duration 7-14 days; no seasonal pattern | SAR: no fever; no sore throat; no myalgia; clear secretions; seasonal pattern; eye involvement |
| **Bacterial acute rhinosinusitis** | Purulent nasal discharge; maxillary or facial pain/pressure; fever; unilateral predominance; symptoms >10 days or biphasic worsening after initial improvement | SAR: clear secretions; bilateral; no facial pain; seasonal |
| **Vasomotor rhinitis (non-allergic rhinitis)** | Clear rhinorrhea and congestion triggered by irritants (cold air, perfume, smoke), not allergens; no pruritus; negative allergy testing; no seasonal pattern | SAR: allergen trigger; pruritus; seasonal; positive skin prick test or specific IgE |
| **Nasal polyposis** | Bilateral nasal obstruction; reduced sense of smell; chronic; often with asthma and aspirin sensitivity (Samter triad); polypoid masses on exam or imaging | SAR: pruritus; seasonal; polypoid masses not present on rhinoscopy |
| **Foreign body (pediatric)** | Unilateral nasal obstruction; foul-smelling unilateral discharge; onset correlates with foreign body insertion event | SAR: bilateral; no foul odor; no unilateral obstruction |

## Workup

### No Workup Required (Typical Allergic Rhinitis in the ED)
- Clinical diagnosis; no labs or imaging required for classic seasonal allergic rhinitis
- Allergy skin prick testing and specific IgE serology are outpatient investigations — not performed in the ED

### When to Consider Workup
- **Nasal endoscopy or plain sinus CT**: if bacterial rhinosinusitis cannot be excluded (symptoms >10 days, facial pain, purulent discharge, fever) — outpatient or urgent care appropriate, not emergency CT
- **CBC**: if systemic infection, eosinophilic granulomatosis with polyangiitis (EGPA/Churg-Strauss), or hypereosinophilic syndrome considered — outpatient investigation
- **Specific IgE (RAST) or skin prick testing**: outpatient allergy workup; identifies specific allergens for immunotherapy candidacy; not an ED test

## Treatment

### Acute Symptom Relief (ED)
- **Diphenhydramine 25-50 mg PO** (adults; 1 mg/kg PO in children, max 50 mg): sedating first-generation H1 antihistamine; rapid symptom relief; appropriate for acute ED management. Inform patient of sedation — do not drive.
- **Cetirizine 10 mg PO** or **loratadine 10 mg PO** (adults; weight-based dosing in children): non-sedating second-generation antihistamines; preferred for ongoing daily use; slower onset than diphenhydramine (1-2 hours)
- **Oxymetazoline 0.05% nasal spray, 2 sprays per nostril twice daily** (adults and children >6 years): topical decongestant; rapid relief of nasal congestion; limit to ≤3 consecutive days — prolonged use causes rhinitis medicamentosa (rebound congestion)
- **Saline nasal irrigation** (e.g., NeilMed Sinus Rinse): reduces allergen load; mucociliary function support; safe for all ages; first-line adjunct

### Maintenance Therapy (Initiate or Recommend at Discharge)
- **Intranasal corticosteroids**: most effective single agent for allergic rhinitis; reduces nasal congestion, rhinorrhea, sneezing, and post-nasal drip. First-line per ARIA and AAO-HNS guidelines.
  - Fluticasone propionate 50 mcg/spray (Flonase): 2 sprays per nostril once daily (adults), 1 spray per nostril once daily (children 4-11 years)
  - Mometasone furoate 50 mcg/spray (Nasonex): 2 sprays per nostril once daily (adults and children ≥12 years); 1 spray per nostril once daily (children 2-11 years)
  - Budesonide 32 mcg/spray (Rhinocort): 1-4 sprays per nostril once daily (adults and children ≥6 years)
  - Onset: 1-2 weeks for full effect; instruct patient on proper administration technique (aim posterolaterally, not toward septum)
- **Second-generation oral antihistamines (daily)**:
  - Cetirizine 10 mg PO once daily (adults and children ≥6 years; 5 mg for ages 2-5)
  - Fexofenadine 180 mg PO once daily (adults and children ≥12 years; 30 mg twice daily for ages 6-11)
  - Loratadine 10 mg PO once daily (adults and children ≥6 years; 5 mg for ages 2-5)
- **Intranasal antihistamine (for moderate-severe SAR)**:
  - Azelastine 0.1% nasal spray (137 mcg/spray): 1-2 sprays per nostril twice daily (adults and children ≥12 years); faster onset than intranasal steroids
- **Montelukast 10 mg PO once daily** (adults; 5 mg chewable for children 6-14 years; 4 mg for children 2-5): leukotriene receptor antagonist; modest effect on rhinitis; appropriate for patients with coexisting asthma. FDA black box warning: neuropsychiatric events (anxiety, depression, suicidal ideation) — use only when alternative agents are insufficient.
- **Allergen immunotherapy (subcutaneous or sublingual)**: disease-modifying treatment; reduces symptom severity and medication requirements; refer to allergist/immunologist; not an ED therapy

## Disposition

### Discharge (Standard)
- All seasonal allergic rhinitis without systemic involvement: discharge with acute antihistamine, prescription or OTC recommendation for intranasal corticosteroid, and primary care or allergy follow-up
- Provide return precautions for anaphylaxis recognition

### Return Precautions (Anaphylaxis Warning)
- Throat tightness, difficulty swallowing, or swallowing pain
- Hives beyond the face or eyes
- Wheezing or difficulty breathing
- Dizziness, lightheadedness, or fainting
- Rapid worsening of any symptoms within minutes of allergen exposure
- If a patient had a prior anaphylactic reaction: prescribe epinephrine auto-injector (EpiPen 0.3 mg IM for adults; EpiPen Jr 0.15 mg IM for children 15-30 kg) at discharge — SAR patients with severe prior reactions warrant a prescription

### Follow-up
- Primary care: allergy testing referral, intranasal corticosteroid titration, consider immunotherapy candidacy
- Allergy/immunology: skin prick testing, specific IgE panel, subcutaneous or sublingual immunotherapy

## Pitfalls

1. **Failing to administer epinephrine to a patient with anaphylaxis because symptoms appear to be "just allergies."** Anaphylaxis begins with nasal and ocular symptoms in many cases. The critical transition is when symptoms involve a second organ system — skin (urticaria), respiratory (wheeze, stridor), or cardiovascular (hypotension). Antihistamines are NOT a substitute for epinephrine in anaphylaxis. H1 and H2 antihistamines can be used as adjuncts after epinephrine, but they do not reverse airway edema or cardiovascular collapse. Any anaphylaxis requires epinephrine first.

2. **Prescribing an oral decongestant (pseudoephedrine or phenylephrine) to a patient with hypertension or cardiovascular disease.** Oral alpha-adrenergic decongestants (pseudoephedrine, phenylephrine) raise blood pressure and heart rate. They are contraindicated in uncontrolled hypertension, ischemic heart disease, and hyperthyroidism. Topical oxymetazoline is a safer alternative for nasal decongestion with minimal systemic absorption when used for ≤3 days.

3. **Not diagnosing rhinitis medicamentosa (rebound congestion from topical decongestant overuse).** Patients who use oxymetazoline or xylometazoline nasal sprays for >3-5 days develop rebound nasal congestion (rhinitis medicamentosa) that is often worse than the original symptom. They present with severe nasal obstruction and a history of "the decongestant stopped working." Treatment is gradual weaning from the topical decongestant — intranasal corticosteroids help bridge this process. Prescribing more topical decongestant perpetuates the cycle.

4. **Missing montelukast's FDA black box neuropsychiatric warning when prescribing for seasonal allergies as monotherapy.** The FDA added a black box warning to montelukast in 2020 for serious neuropsychiatric events including suicidal ideation. Montelukast should not be prescribed as first-line therapy for rhinitis when antihistamines and intranasal corticosteroids are available and have a superior safety profile. Reserve montelukast for patients with coexisting asthma or those who cannot tolerate intranasal steroids and antihistamines.

5. **Attributing unilateral nasal obstruction with bloody discharge to seasonal allergies.** Allergic rhinitis is bilateral — unilateral nasal obstruction, especially with bloody discharge, nasal deformity, or facial pain, requires evaluation for nasal foreign body (children), polyp, inverting papilloma, or sinonasal malignancy. These are not features of allergic rhinitis.
