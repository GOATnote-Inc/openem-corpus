---
id: angioedema
condition: Angioedema
aliases: [angioneurotic edema, Quincke's edema, ACE-inhibitor angioedema, hereditary angioedema, HAE]
icd10: [T78.3XXA, T78.3XXD, D84.1, T88.7XXA]
esi: 1
time_to_harm: "< 60 minutes"
mortality_if_delayed: "Up to 30% mortality from airway obstruction if not managed"
category: allergic-immunologic
track: tier1
sources:
  - type: guideline
    ref: "2022 WAO/EAACI Guideline for the Management of Hereditary Angioedema"
  - type: guideline
    ref: "2020 International/Canadian Hereditary Angioedema Guideline"
    doi: "10.1186/s13223-019-0399-z"
  - type: guideline
    ref: "2023 ACEP Clinical Policy: Acute Allergic Reactions Including Anaphylaxis"
  - type: pubmed
    ref: "Bernstein JA et al. The diagnosis and management of acute and chronic urticaria: 2014 update. J Allergy Clin Immunol 2014;133(5):1270-7"
    pmid: "24766875"
  - type: pubmed
    ref: "Banerji A et al. ACE inhibitor-associated angioedema in the emergency department. Ann Emerg Med 2008;51(4):S130"
    pmid: "18450117"
  - type: review
    ref: "Zuraw BL. Hereditary angioedema. N Engl J Med 2008;359(10):1027-36"
    pmid: "18768946"
last_updated: "2026-02-18"
compiled_by: agent
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
  guideline_version_reference: null
  provenance_links: []
---
# Angioedema

## Recognition

**Two mechanistically distinct types:**

**1. Histamine-mediated (allergic/mast cell):**
- Often accompanies urticaria, pruritus, flushing
- Triggered by allergens, NSAIDs, contrast media, foods
- Onset minutes to hours after exposure
- Swelling of lips, tongue, uvula, eyelids
- Responds to epinephrine, antihistamines, steroids

**2. Bradykinin-mediated (NON-allergic):**
- ACE-inhibitor angioedema (most common cause in EDs): occurs in 0.1-0.7% of patients on ACEi, can present **years into therapy** (median onset 1-10 years)
- Hereditary angioedema (HAE): C1-esterase inhibitor deficiency (Types I and II) or factor XII mutations (Type III)
- Acquired C1-INH deficiency (lymphoproliferative disorders)
- **No urticaria, no pruritus** — isolated tissue swelling
- Lips, tongue, face, larynx, bowel wall (abdominal attacks mimic surgical abdomen)
- **Does NOT respond to epinephrine, antihistamines, or steroids**

**Key Exam Findings:**
- Asymmetric, non-pitting, non-pruritic swelling of subcutaneous/submucosal tissue
- Tongue swelling — assess for inability to swallow secretions, muffled voice
- Stridor, drooling, inability to lie flat = impending airway loss
- Floor-of-mouth swelling (Ludwig angina mimic)
- Abdominal pain with ascites/bowel wall edema in HAE attacks

**Airway Staging:**
- Stage 1: facial/lip swelling only — observe closely
- Stage 2: soft palate/tongue edema — prepare for intubation
- Stage 3: laryngeal involvement (voice change, stridor) — immediate airway intervention

## Critical Actions

1. **Assess airway immediately.** Any voice change, stridor, drooling, tongue protrusion, or inability to swallow secretions = emergency airway.
2. **Determine mechanism** — presence of urticaria/pruritus suggests histaminergic; absence with isolated swelling (especially on ACEi) suggests bradykinin-mediated.
3. **Histamine-mediated:** Epinephrine 0.3-0.5 mg IM (1 mg/mL) anterolateral thigh. Repeat q5-15min. Diphenhydramine 50 mg IV. Methylprednisolone 125 mg IV. Famotidine 20 mg IV.
4. **Bradykinin-mediated:** Epinephrine is ineffective but give empirically if mechanism uncertain. Start targeted therapy:
   - Icatibant (Firazyr) 30 mg SC in abdominal wall — bradykinin B2 receptor antagonist
   - C1-INH concentrate: Berinert 20 units/kg IV or Cinryze 1000 units IV
   - Ecallantide (Kalbitor) 30 mg SC (three 10 mg injections) — kallikrein inhibitor (1.6% anaphylaxis risk, must be administered by healthcare provider)
   - Fresh frozen plasma (FFP) 2-4 units IV as last resort if targeted therapies unavailable (replaces C1-INH but contains kininogens that theoretically can worsen HAE; evidence supports net benefit)
5. **Airway management** — early intubation with the most experienced operator. Awake fiberoptic intubation preferred if feasible. Have surgical airway kit open at bedside. Edema progresses rapidly and makes repeated attempts dangerous.
6. **Surgical airway (cricothyrotomy)** if unable to intubate — do not hesitate. Supraglottic devices often fail due to pharyngeal edema.
7. **Discontinue ACE-inhibitor permanently** if ACEi-related. Do NOT switch to another ACEi. ARBs have low (~2-5%) cross-reactivity but use with caution.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Anaphylaxis | Urticaria + hypotension + bronchospasm; multi-system involvement; responds to epinephrine |
| Ludwig angina | Floor-of-mouth cellulitis, trismus, dental source, fever, elevated WBC |
| Peritonsillar abscess | Trismus, unilateral tonsillar swelling, uvula deviation, fever |
| Superior vena cava syndrome | Facial/upper extremity edema, JVD, collateral chest wall veins |
| Contact dermatitis | Localized swelling with vesicles/erythema at contact site |
| Cellulitis/erysipelas | Warmth, erythema, tenderness, fever, demarcated borders |
| Nephrotic syndrome | Generalized edema, periorbital predominance, proteinuria |
| Hypothyroidism (myxedema) | Non-pitting edema, chronic, periorbital, bradycardia |

## Workup

**Labs:**
- CBC with differential
- BMP — baseline renal function
- C4 level — screening test for HAE; low C4 during and between attacks in HAE Types I/II. Normal C4 during an attack effectively excludes C1-INH deficiency
- C1-esterase inhibitor level and function — send if C4 low or clinical suspicion for HAE (results not available acutely; guides outpatient management)
- Tryptase — elevated in histamine-mediated, normal in bradykinin-mediated (helps distinguish mechanism retrospectively)
- Lipase — if abdominal angioedema suspected (HAE abdominal attacks can elevate amylase/lipase)

**Imaging:**
- CT neck with IV contrast if concern for deep space infection or to delineate extent of swelling
- Nasopharyngeal laryngoscopy — direct visualization of laryngeal edema if available without delaying airway management
- CT abdomen — bowel wall thickening and ascites in HAE abdominal attacks (often misdiagnosed as surgical abdomen)

## Treatment

**Histamine-Mediated Angioedema:**
- Epinephrine 0.3-0.5 mg IM q5-15min (first-line)
- Diphenhydramine 50 mg IV (H1 blocker)
- Famotidine 20 mg IV (H2 blocker)
- Methylprednisolone 125 mg IV
- Albuterol 2.5 mg nebulized if bronchospasm
- Refractory: epinephrine infusion 0.1-1 mcg/kg/min IV

**Bradykinin-Mediated Angioedema (ACEi or HAE):**

*First-line targeted therapies (give as early as possible):*
- Icatibant 30 mg SC (abdomen) — onset 30-60 min, may repeat at 6 hours (max 3 doses/24 hours)
- C1-INH concentrate: Berinert 20 units/kg IV (slow push) or Cinryze 1000 units IV
- Ecallantide 30 mg SC (three 10 mg injections at separate sites) — observe 30 min for anaphylaxis

*If targeted therapies unavailable:*
- FFP 2-4 units IV (provides C1-INH replacement)

*Adjunctive (limited efficacy in bradykinin-mediated):*
- Epinephrine IM — give empirically while determining mechanism; provides modest alpha-adrenergic vasoconstriction even in bradykinin-mediated disease
- Steroids and antihistamines are ineffective for bradykinin-mediated angioedema but cause no harm if diagnosis uncertain

**Airway Management:**
- Nebulized racemic epinephrine 2.25% 0.5 mL in 3 mL NS for stridor (temporizing)
- Awake fiberoptic intubation preferred — maintains spontaneous ventilation
- Video laryngoscopy with bougie if fiberoptic not available
- Use the largest ETT that passes; expect edematous, distorted anatomy
- Cricothyrotomy kit open at bedside before any airway attempt
- Tracheostomy under local anesthesia in controlled OR setting if time permits

## Disposition

**Admit (ICU/monitored bed):**
- Any laryngeal involvement or airway intervention
- Tongue swelling not fully resolved
- Required intubation or surgical airway
- Recurrent or progressive swelling despite treatment
- HAE attacks with abdominal involvement (IV fluid resuscitation, pain control)

**Observation (minimum 6 hours):**
- Lip/facial swelling without airway compromise that resolves with treatment
- First episode of isolated angioedema — monitor for progression

**Discharge Criteria:**
- Complete resolution of swelling for at least 4 hours
- No airway symptoms
- ACEi permanently discontinued (document clearly in discharge and notify prescribing provider)
- HAE patients: ensure they have home rescue medication (icatibant auto-injector or C1-INH for self-administration)
- Refer to allergist/immunologist for C1-INH testing if HAE suspected
- Refer to allergist if recurrent idiopathic angioedema

## Pitfalls

1. **Giving epinephrine and antihistamines for ACEi angioedema and expecting resolution.** Bradykinin-mediated angioedema does not respond to histamine-targeted therapies. Targeted bradykinin pathway therapies (icatibant, C1-INH concentrate, ecallantide) are required.

2. **Delaying airway management while waiting for medications to work.** Angioedema airway obstruction progresses rapidly. If the tongue is enlarging and the patient cannot swallow secretions, intubate now. Waiting for icatibant onset (30-60 min) with a threatened airway kills patients.

3. **Attributing ACEi angioedema only to new prescriptions.** ACE-inhibitor angioedema occurs after years of uneventful use. The median time to first episode is 1-10 years. Any patient on an ACEi with isolated swelling of lips, tongue, or face has ACEi angioedema until proven otherwise.

4. **Switching to another ACE-inhibitor after an episode.** ACEi angioedema is a class effect mediated by bradykinin accumulation. All ACE-inhibitors must be permanently discontinued. ARBs have ~2-5% cross-reactivity and should be used cautiously if at all.

5. **Failing to distinguish angioedema from anaphylaxis.** Angioedema without urticaria, pruritus, bronchospasm, or hypotension is unlikely anaphylaxis. Misdiagnosis delays appropriate targeted therapy and leads to futile repeat dosing of epinephrine.

6. **Discharging HAE patients without home rescue therapy.** HAE attacks are unpredictable and can involve the larynx. Patients need icatibant auto-injectors or self-administered C1-INH for home use, plus an emergency action plan.

7. **Misdiagnosing HAE abdominal attacks as surgical abdomen.** HAE causes bowel wall edema with severe cramping, vomiting, and CT findings mimicking small bowel obstruction. Unnecessary laparotomy is a documented complication. Low C4, history of recurrent swelling, and family history point to HAE.

8. **Failing to send C4 and C1-INH levels.** A first episode of isolated angioedema without clear trigger warrants C4 level (ideally during the attack). This is the screening test for hereditary and acquired C1-INH deficiency. Missing this diagnosis leaves patients at risk for fatal laryngeal attacks.

9. **Using FFP in HAE without understanding the theoretical risk.** FFP contains C1-INH (beneficial) but also kininogens (substrate for more bradykinin). Clinical evidence supports FFP as a net positive, but it is last-resort when targeted therapies are available. Monitor closely for worsening after FFP administration.
