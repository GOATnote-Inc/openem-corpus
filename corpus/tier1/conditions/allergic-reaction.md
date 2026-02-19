---
id: allergic-reaction
condition: Allergic Reaction (Non-Anaphylactic)
aliases: [urticaria, hives, allergic urticaria, acute urticaria, localized allergic reaction, mild allergic reaction, allergic contact dermatitis]
icd10: [T78.40XA, L50.0, L50.9, L23.9]
esi: 3
time_to_harm: "Hours — risk of progression to anaphylaxis within minutes if escalation occurs"
mortality_if_delayed: "Low for isolated urticaria; risk increases if progression to anaphylaxis is missed"
category: allergic-immunologic
track: tier1
sources:
  - type: review
    ref: "Shaker MS et al. Anaphylaxis — A 2020 Practice Parameter Update, Systematic Review, and GRADE Analysis. J Allergy Clin Immunol 2020;145(4):1082-1123"
    pmid: "32001253"
  - type: guideline
    ref: "Zuberbier T et al. The International EAACI/GA2LEN/EuroGuiDerm/APAAACI Guideline for the Definition, Classification, Diagnosis, and Management of Urticaria. Allergy 2022;77(3):734-766"
    pmid: "34536239"
  - type: pubmed
    ref: "Bernstein JA et al. The Diagnosis and Management of Acute and Chronic Urticaria: 2014 Update. J Allergy Clin Immunol 2014;133(5):1270-1277"
    pmid: "24766875"
  - type: pubmed
    ref: "Grunau BE et al. Incidence of Clinically Important Biphasic Reactions in Emergency Department Patients with Allergic Reactions or Anaphylaxis. Ann Emerg Med 2014;63(6):736-744"
    pmid: "24239340"
  - type: review
    ref: "Pflipsen MC, Vega Colon KM. Management of Allergic Reactions and Anaphylaxis in the Emergency Department. Emerg Med Clin North Am 2022;40(3):563-579"
    pmid: "35737570"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: C
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
# Allergic Reaction (Non-Anaphylactic)

> **Scope:** This file covers non-anaphylactic allergic reactions — acute urticaria, localized angioedema without airway compromise, and allergic contact dermatitis presenting to the ED. For systemic anaphylaxis, see [anaphylaxis.md](anaphylaxis.md). For isolated angioedema (including ACE-inhibitor and hereditary angioedema), see [angioedema.md](angioedema.md).

## Recognition

**Clinical Spectrum — Mild to Pre-Anaphylactic:**

| Severity | Presentation | Risk of Progression |
|----------|-------------|---------------------|
| Mild | Localized urticaria (<10% BSA), localized pruritus, minor contact dermatitis | Low |
| Moderate | Widespread urticaria (>10% BSA), mild facial/lip angioedema without airway symptoms, generalized pruritus, GI discomfort | Moderate — reassess frequently |
| Pre-anaphylactic | Rapidly spreading urticaria, progressive angioedema (tongue, uvula), throat tightness, voice change, early wheeze, lightheadedness | High — treat as anaphylaxis (see [anaphylaxis.md](anaphylaxis.md)) |

**Acute Urticaria:**
- Raised, erythematous, pruritic wheals (hives) with surrounding flare
- Individual lesions are transient — each wheal resolves within 24 hours (if lesions persist >24 hours at the same site, consider urticarial vasculitis)
- Dermatographism commonly present
- Acute = duration <6 weeks; chronic = >6 weeks (chronic urticaria is an outpatient workup)

**Allergic Contact Dermatitis (acute presentation):**
- Well-demarcated erythematous, edematous, vesicular eruption at contact site
- Linear or geometric pattern suggests external contactant (e.g., poison ivy: linear vesicles)
- Severe cases: weeping, crusting, significant edema (eyelids, genitalia)
- Onset 24-72 hours after exposure (delayed type IV hypersensitivity)

**Localized Angioedema Without Airway Compromise:**
- Asymmetric, non-pitting swelling of lips, eyelids, hands, feet, or genitalia
- If accompanied by urticaria/pruritus: histamine-mediated (responds to standard therapy)
- If isolated swelling without urticaria: consider bradykinin-mediated etiology (see [angioedema.md](angioedema.md))

**Common Triggers:**
- Foods: peanuts, tree nuts, shellfish, milk, egg, wheat, soy
- Medications: antibiotics (penicillins, cephalosporins, sulfonamides), NSAIDs, opioids
- Insect stings/bites (Hymenoptera)
- Contactants: poison ivy/oak/sumac (urushiol), latex, nickel, fragrances
- Environmental: cold, heat, pressure, exercise, vibration (physical urticarias)
- Idiopathic: no identifiable trigger in up to 50% of acute urticaria

## Critical Actions

1. **Assess for anaphylaxis at presentation and serially.** Apply WAO/NIAID criteria (see [anaphylaxis.md](anaphylaxis.md)). Any respiratory symptoms (dyspnea, wheeze, stridor), hypotension, or rapidly progressive angioedema = anaphylaxis protocol immediately.
2. **Give epinephrine if ANY of the following are present:** voice change, stridor, wheeze, dyspnea, oxygen desaturation, hypotension, syncope, tongue swelling progressing toward airway, or rapidly progressive symptoms despite antihistamines. Do not wait for "classic" anaphylaxis.
3. **Obtain a focused allergy history.** New medications in the past 14 days, foods in the past 6 hours, insect stings, latex exposure, prior allergic reactions, history of atopy or asthma (increases anaphylaxis risk).
4. **Check medication list for ACE-inhibitors.** Isolated angioedema without urticaria in a patient on an ACEi = bradykinin-mediated angioedema (see [angioedema.md](angioedema.md)). Standard allergic reaction treatment is ineffective.
5. **Reassess after treatment.** Patients who do not improve within 1-2 hours of antihistamine administration, or who develop new symptoms, require escalation. Worsening despite treatment is a red flag for anaphylaxis.
6. **Document the suspected trigger.** Accurate documentation guides allergen avoidance and outpatient allergy testing.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Anaphylaxis | Multi-system involvement (skin + respiratory/cardiovascular/GI); hypotension; bronchospasm; requires epinephrine. See [anaphylaxis.md](anaphylaxis.md) |
| Angioedema (bradykinin-mediated) | Isolated swelling without urticaria or pruritus; ACEi use or family history of HAE; does NOT respond to antihistamines/epinephrine. See [angioedema.md](angioedema.md) |
| Urticarial vasculitis | Painful (not pruritic) wheals lasting >24 hours at the same site; purpura on resolution; low complement levels; biopsy shows leukocytoclastic vasculitis |
| Viral exanthem | Symmetric morbilliform rash, URI prodrome, fever, no individual lesion transience, no dermographism |
| Drug hypersensitivity (DRESS, SJS) | Fever, mucosal involvement, eosinophilia, organ dysfunction, skin pain/necrosis. See [drug-hypersensitivity-reaction.md](drug-hypersensitivity-reaction.md), [sjs-ten.md](sjs-ten.md) |
| Scombroid poisoning | Flushing, urticaria, GI symptoms minutes after eating dark-meat fish (tuna, mackerel, mahi-mahi); histamine toxicity; responds to antihistamines |
| Contact dermatitis (irritant) | Non-immune, dose-dependent; sharply demarcated to exposure site; burning > pruritus; no vesicles spreading beyond contact area |
| Mastocytosis | Recurrent flushing and urticaria; Darier sign (wheal on stroking skin lesion); elevated baseline tryptase |
| Erythema multiforme | Target lesions with three concentric zones; acral distribution; may have mucosal involvement |
| Serum sickness | Urticaria + fever + arthralgias + lymphadenopathy; 7-14 days after drug/biologic exposure |

## Workup

**Mild Isolated Urticaria (no systemic features):**
- No labs required. Clinical diagnosis.
- History and physical examination are sufficient.

**Moderate/Recurrent Urticaria or Angioedema:**
- CBC with differential — eosinophilia supports allergic etiology; elevated WBC with left shift suggests infection
- CMP — baseline hepatic/renal function if systemic medications will be given
- Tryptase — draw within 1-2 hours of symptom onset if anaphylaxis was considered but not confirmed. Elevated >11.4 ng/mL supports mast cell degranulation. Normal does NOT exclude allergic reaction (sensitivity is low for non-anaphylactic reactions)

**If Angioedema Without Urticaria:**
- C4 level — screening for C1-esterase inhibitor deficiency (low C4 during attack suggests hereditary or acquired angioedema)
- Review medication list for ACEi/ARB

**Contact Dermatitis:**
- No labs needed acutely
- Patch testing is an outpatient procedure (allergist referral)

**Imaging:** Not indicated for uncomplicated allergic reactions. CT neck only if concern for deep tissue swelling or airway compromise.

## Treatment

**Mild Urticaria (localized, no angioedema, no systemic symptoms):**
- Cetirizine 10 mg PO (preferred — less sedating, faster onset than diphenhydramine) OR
- Diphenhydramine 25-50 mg PO/IV (more sedating; 25 mg for elderly)
- Observation 1-2 hours for resolution

**Moderate Allergic Reaction (widespread urticaria, mild angioedema, or systemic pruritus):**
- H1 blocker: diphenhydramine 25-50 mg IV OR cetirizine 10 mg PO
- H2 blocker: famotidine 20 mg IV (additive effect with H1 blocker for urticaria refractory to H1 alone)
- Corticosteroid (for severe/widespread urticaria or angioedema component): dexamethasone 10 mg IV/PO (single dose, long half-life, no taper needed) OR prednisone 40-60 mg PO
- Remove/avoid trigger if identified
- Observation minimum 2-4 hours; reassess for progression

**Pre-Anaphylactic or Rapidly Progressive Symptoms:**
- Epinephrine 0.3-0.5 mg IM (1 mg/mL) anterolateral thigh — do not hesitate
  - Pediatric: 0.01 mg/kg IM (max 0.3 mg)
- Then treat per anaphylaxis protocol (see [anaphylaxis.md](anaphylaxis.md))
- Observe minimum 4-6 hours after last epinephrine dose

**Allergic Contact Dermatitis:**
- Remove contactant; wash skin with soap and water (urushiol can persist on skin/clothing for hours)
- Mild/localized: high-potency topical corticosteroid (clobetasol 0.05% cream BID for 2-3 weeks, or triamcinolone 0.1% cream BID for trunk/extremities)
- Severe/widespread (>20% BSA or face/genitals): prednisone 0.5-1 mg/kg/day PO for 14-21 days with taper (do NOT use short 5-7 day courses — rebound dermatitis occurs when taper is too short)
- Pruritus: hydroxyzine 25 mg PO q6h PRN or cetirizine 10 mg PO daily
- Cool compresses, calamine lotion for comfort

**Refractory Urticaria (not responding to standard H1 + H2 blockers):**
- Repeat H1 blocker dose (up-dosing second-generation antihistamines up to 4x standard dose is supported by guidelines for urticaria)
- Add corticosteroid if not yet given
- If still refractory: consider epinephrine 0.3 mg IM (even without overt anaphylaxis, refractory urticaria with angioedema may benefit)
- Reassess for anaphylaxis criteria

**Pediatric Dosing:**
- Cetirizine: 2.5 mg PO (6 months-2 years), 5 mg PO (2-5 years), 10 mg PO (>6 years)
- Diphenhydramine: 1.25 mg/kg PO/IV (max 50 mg)
- Famotidine: 0.25 mg/kg IV (max 20 mg)
- Dexamethasone: 0.6 mg/kg PO/IV (max 10 mg)
- Prednisone/prednisolone: 1-2 mg/kg PO (max 60 mg)

## Disposition

**Discharge (majority of patients):**
- Symptoms resolved or significantly improved after 1-2 hours of observation
- No respiratory symptoms, no hypotension, no angioedema progression
- Prescribe:
  - Second-generation antihistamine: cetirizine 10 mg PO daily or loratadine 10 mg PO daily for 5-7 days (or until rash resolves)
  - Famotidine 20 mg PO BID for 3-5 days (for patients who needed H2 blocker in ED)
  - Prednisone 40-60 mg PO daily for 3-5 days if moderate-to-severe reaction (contact dermatitis: 14-21 day taper)
- **Prescribe epinephrine autoinjector (EpiPen 0.3 mg adult, 0.15 mg pediatric)** if: reaction involved angioedema, reaction was to a sting or food, prior history of anaphylaxis, or any concern for possible progression. Prescribe 2 devices. Demonstrate use.
- Educate on trigger avoidance and return precautions: throat tightness, difficulty breathing, swelling of tongue/lips, dizziness, diffuse hives not responding to antihistamines
- Allergy referral for: first episode with identifiable trigger (skin testing), recurrent episodes, any episode requiring epinephrine, food or venom allergy

**Extended Observation (4-6 hours minimum):**
- Any patient who received epinephrine (biphasic reaction risk)
- Angioedema involving face/lips not fully resolved
- History of prior anaphylaxis with same trigger
- Patients on beta-blockers (blunted response to epinephrine, higher risk of severe progression)
- Asthma history with any respiratory component

**Admit:**
- Persistent or progressive angioedema despite treatment
- Required multiple doses of epinephrine
- Significant comorbidities (severe asthma, cardiac disease, beta-blocker use) with moderate-to-severe reaction
- Uncertainty about diagnosis (possible early anaphylaxis vs. isolated reaction)

## Pitfalls

1. **Failing to recognize pre-anaphylaxis.** Urticaria is the earliest sign of anaphylaxis in 90% of cases. Isolated hives can progress to full anaphylaxis within minutes. Serial reassessment is mandatory. Any new respiratory symptom, GI cramping, or hemodynamic change in a patient with urticaria triggers immediate epinephrine and escalation.

2. **Withholding epinephrine because "it's just hives."** Epinephrine is indicated for any sign of systemic progression — throat tightness, voice change, wheeze, hypotension, or rapidly expanding urticaria with angioedema. There is no harm in giving IM epinephrine to a patient who turns out not to need it. There is significant harm in withholding it from one who does.

3. **Using diphenhydramine IV as a substitute for epinephrine.** Antihistamines treat pruritus and urticaria. They do NOT reverse airway edema, bronchospasm, or hypotension. IV diphenhydramine given "for the allergic reaction" creates a false sense of action while the patient progresses to cardiovascular collapse.

4. **Short steroid courses for poison ivy/contact dermatitis.** Prescribing prednisone for 5-7 days for widespread contact dermatitis causes rebound flare when the steroid is stopped — the hapten-mediated immune response outlasts the drug. A 14-21 day taper is required for extensive allergic contact dermatitis.

5. **Discharging without an epinephrine autoinjector when one is indicated.** Patients with allergic reactions involving angioedema, food or venom triggers, or any reaction that required epinephrine in the ED must leave with an autoinjector. Biphasic reactions can occur hours after discharge. A patient without an autoinjector who develops anaphylaxis at home may die before reaching care.

6. **Assuming a stable patient will remain stable.** Biphasic reactions occur in 1-20% of allergic reactions (higher rates with more severe initial presentations). Grunau et al. (PMID 24239340) showed clinically important biphasic reactions are uncommon but unpredictable. Patients who received epinephrine require a minimum 4-6 hour observation period.

7. **Missing ACE-inhibitor angioedema.** Isolated angioedema of the lips, tongue, or face without urticaria in a patient on an ACEi is bradykinin-mediated, not histamine-mediated. Antihistamines, steroids, and epinephrine are ineffective. Targeted therapy (icatibant, C1-INH concentrate) is needed. See [angioedema.md](angioedema.md).

8. **Not checking for urticarial vasculitis.** Wheals that are painful rather than pruritic, leave purpura/bruising on resolution, or persist at the same site for >24 hours are NOT typical urticaria. This is urticarial vasculitis until proven otherwise and requires biopsy, complement levels, and rheumatology referral.

9. **Forgetting to counsel on cross-reactive triggers.** NSAIDs cause urticaria/angioedema through COX-1 inhibition (pseudoallergic reaction) in up to 30% of patients with chronic urticaria. A patient with an NSAID-triggered reaction must avoid ALL nonselective NSAIDs, not just the one that caused the reaction. Celecoxib (COX-2 selective) is generally safe but should be introduced under observation.
