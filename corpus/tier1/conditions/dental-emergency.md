---
id: dental-emergency
condition: Dental Emergency
aliases: [dental trauma, avulsed tooth, tooth avulsion, dental fracture, periapical abscess, dental abscess, alveolar fracture, Ellis fracture]
icd10: [S02.5XXA, K04.7, K08.419, K05.20]
esi: 4
time_to_harm: "< 60 minutes for tooth avulsion (reimplantation success drops sharply after 60 minutes); periapical abscess < 24 hours if spreading"
category: procedural
track: tier1
confusion_pairs:
  - condition: ludwigs-angina
    differentiators:
      - "Dental emergency: localized dental or periapical pain, no submandibular swelling, no floor of mouth elevation"
      - "Ludwig angina: bilateral submandibular induration, floor of mouth elevation, potential airway compromise requiring emergent intervention"
      - "Dental emergency: patient non-toxic, vital signs normal; Ludwig angina: fever, tachycardia, drooling, dysphagia"
  - condition: peritonsillar-abscess
    differentiators:
      - "Dental emergency: pain localized to tooth or gingiva, no trismus or muffled voice, normal oropharyngeal exam"
      - "PTA: severe unilateral sore throat, trismus, uvula deviation, drooling, muffled 'hot potato' voice"
      - "Dental emergency: swelling confined to alveolar ridge or buccal space; PTA: peritonsillar bulging on oropharyngeal exam"
sources:
  - type: guideline
    ref: "International Association of Dental Traumatology (IADT) Guidelines for the Management of Traumatic Dental Injuries: 1. Fractures and Luxations. Dent Traumatol 2012;28:2-12"
    pmid: "22230724"
  - type: pubmed
    ref: "Andersson L et al. International Association of Dental Traumatology Guidelines for the Management of Traumatic Dental Injuries: 2. Avulsion of Permanent Teeth. Dent Traumatol 2012;28:88-96"
    pmid: "22409417"
  - type: review
    ref: "Benko K. Emergency Dental Procedures. In: Roberts and Hedges' Clinical Procedures in Emergency Medicine and Acute Care, 7th ed. Elsevier 2019. (Review of ED dental management)"
  - type: pubmed
    ref: "Beaudreau RW. Oral and Dental Emergencies. In: Tintinalli's Emergency Medicine, 9th ed. McGraw-Hill 2020. Chapter 239"
    pmid: "28881482"
last_updated: "2026-03-06"
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
  provenance_links: []
---
# Dental Emergency

## Recognition

**Definition:** Acute traumatic or infectious conditions involving the teeth, alveolar bone, and supporting structures requiring emergency evaluation. Includes dental fractures (Ellis classification), tooth avulsion, alveolar fractures, and periapical abscesses. Dental complaints account for 1-2% of all ED visits.

**Ellis Classification of Tooth Fractures:**
- **Ellis I:** Enamel only. White chalky fragment missing. No sensitivity. Non-urgent.
- **Ellis II:** Enamel + dentin. Yellow or ivory layer exposed. Sensitive to air and temperature. Requires dental follow-up within 24 hours.
- **Ellis III:** Enamel + dentin + pulp. Pink/red spot visible at fracture site, often with active bleeding from pulp. Requires emergent dental consultation or ED pulp coverage.

**Tooth Avulsion:**
- Complete displacement of tooth from alveolar socket
- Permanent teeth: time-critical — reimplantation success > 90% if within 5 minutes, drops to < 5% after 60 minutes
- Primary (deciduous) teeth: do NOT reimplant (risk of ankylosis, damage to developing permanent tooth bud)

**Alveolar Fracture:**
- Fracture of the tooth-bearing segment of the maxilla or mandible
- Segment mobility on palpation — multiple teeth move as a unit
- Gingival laceration, malocclusion, step-off on palpation
- Requires reduction and stabilization

**Periapical Abscess:**
- Localized collection of pus at the root apex from pulp necrosis
- Spontaneous throbbing pain, worse with heat, improved with cold
- Swelling of gingiva or buccal mucosa overlying the affected root
- Fluctuant intraoral mass, percussion tenderness of affected tooth
- Fever if spreading (buccal space, submandibular space, canine space)

## Critical Actions

1. **Assess for associated injuries** — dental trauma often accompanies facial fractures, TBI, and cervical spine injury. Evaluate the full face and neck.
2. **Account for all tooth fragments** — missing fragments may be aspirated (obtain CXR if fragment not found), embedded in lip lacerations (palpate and inspect all lip wounds), or swallowed.
3. **Handle avulsed tooth by crown only** — never touch the root surface. Rinse gently with saline if contaminated. Do not scrub or remove attached periodontal ligament fibers.
4. **Reimplant avulsed permanent tooth immediately** — hold in socket with gentle pressure. If reimplantation not possible, store in Hank Balanced Salt Solution (Save-A-Tooth), cold milk, patient's saliva, or saline (in order of preference). Never store in water.
5. **Cover exposed dentin (Ellis II) with calcium hydroxide paste** (Dycal) or glass ionomer cement, then dental follow-up within 24 hours.
6. **Cover exposed pulp (Ellis III) with calcium hydroxide paste** and refer for emergent dental evaluation within hours. If dental coverage unavailable, apply Dycal directly to pulp exposure.
7. **Incise and drain periapical abscess** — identify point of maximal fluctuance intraorally, incise with #15 blade, blunt dissect with hemostat, irrigate with saline.
8. **Prescribe antibiotics for abscess** — penicillin VK 500 mg PO QID x 7-10 days OR amoxicillin 500 mg PO TID x 7-10 days. Add metronidazole 500 mg PO TID if severe or spreading infection.
9. **Reduce alveolar fracture** — apply digital pressure to reposition the mobile segment, verify occlusion, apply Coe-Pak periodontal dressing or Erich arch bars if available. Urgent oral surgery or ENT referral.
10. **Update tetanus prophylaxis** for all dental trauma with mucosal or gingival disruption.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Ludwig angina | Bilateral submandibular induration, floor of mouth elevation, airway compromise; dental source but infection has spread to submandibular/sublingual spaces |
| Buccal space abscess | Cheek swelling overlying the premolars/molars; may originate from dental source but extends into buccal fat pad |
| Mandible fracture | Point tenderness over mandible body/angle/condyle, malocclusion, step-off, numbness of lower lip (inferior alveolar nerve); panorex or CT confirms |
| Parotitis | Preauricular swelling, purulent drainage from Stensen duct with gland massage; no dental tenderness |
| Temporomandibular joint dysfunction | Preauricular pain, clicking, limited opening; chronic course, no dental pathology |
| Pericoronitis | Inflammation of gum tissue around partially erupted third molar; localized to posterior mandible, operculum swelling |
| Oral malignancy | Non-healing ulcer, induration, lymphadenopathy; chronic progressive course |

## Workup

**Bedside:**
- Visual inspection with adequate lighting and suction
- Palpation of all teeth for mobility, alveolar ridge for step-off
- Percussion tenderness (metal instrument handle tapped on individual teeth)
- Cold test (ice or ethyl chloride on cotton) — vital teeth respond; necrotic teeth do not
- Lip wound exploration — palpate for embedded tooth fragments

**Imaging:**
- Panoramic radiograph (Panorex) — best single view for dental trauma, fractures, periapical pathology
- Periapical dental X-ray — highest resolution for individual tooth, root fractures, periapical lucency
- CT face without contrast — if alveolar or mandible fracture suspected
- CXR or abdominal film — if tooth fragment unaccounted for (aspiration vs. ingestion)

**Labs:**
- Not routinely required
- CBC, BMP if systemically ill from dental abscess
- Blood cultures if febrile with dental abscess and concern for bacteremia

## Treatment

**Avulsed Permanent Tooth:**
- Reimplant as quickly as possible — every minute counts
- Rinse root with saline (do not scrub), insert into socket with gentle digital pressure
- Patient bites on gauze to maintain position
- Flexible splint for 2 weeks (Coe-Pak, aluminum foil, or commercial dental splint)
- Doxycycline 100 mg PO BID x 7 days (reduces inflammatory root resorption)
- Chlorhexidine 0.12% rinse BID x 2 weeks
- Soft diet x 2 weeks
- Dental follow-up within 24 hours for definitive splinting

**Ellis Fractures:**
- Ellis I: smooth sharp edges with emery board or dental bur. Dental follow-up non-urgent.
- Ellis II: calcium hydroxide paste (Dycal) over exposed dentin, cover with dry foil or dental bonding. Dental follow-up within 24 hours.
- Ellis III: calcium hydroxide paste directly on pulp exposure. Emergent dental referral (within hours). If temporizing, cover with Dycal + aluminum foil. NSAIDs for pain.

**Periapical Abscess:**
- I&D if fluctuant: topical benzocaine 20% gel, infraorbital or inferior alveolar nerve block with lidocaine 2% with epinephrine, incise at point of maximal fluctuance, blunt dissection, irrigate with saline
- Antibiotics: penicillin VK 500 mg PO QID x 7-10 days OR amoxicillin 500 mg PO TID x 7-10 days
- Penicillin allergy: clindamycin 300 mg PO QID x 7 days
- Add metronidazole 500 mg PO TID if severe, spreading, or immunocompromised
- Analgesics: ibuprofen 400-600 mg PO q6h + acetaminophen 500-1000 mg PO q6h (alternating)
- Dental follow-up within 24-48 hours for definitive treatment (root canal or extraction)

**Alveolar Fracture:**
- Reduce mobile segment with digital pressure, verify occlusion
- Temporary stabilization with Coe-Pak or interdental wiring
- Oral surgery or ENT consultation for definitive fixation
- Antibiotics: amoxicillin 500 mg PO TID x 7 days or amoxicillin-clavulanate 875/125 mg PO BID x 7 days
- Tetanus prophylaxis
- Soft diet, chlorhexidine rinses

## Disposition

**Discharge (majority of dental emergencies):**
- Successfully reimplanted avulsed tooth with splint — dental follow-up within 24 hours
- Ellis I-II fractures with appropriate coverage — dental follow-up within 24-48 hours
- Periapical abscess after I&D with no signs of spreading — dental follow-up within 24-48 hours
- Prescriptions: antibiotics (if indicated), analgesics, chlorhexidine rinse
- Return precautions: worsening swelling, fever, difficulty swallowing or breathing, trismus

**Admit or emergent consultation:**
- Spreading facial space infection (buccal, submandibular, sublingual involvement)
- Airway compromise from swelling
- Alveolar fracture requiring operative fixation
- Ellis III with no dental coverage available — admit for IV antibiotics and next-day dental surgery
- Immunocompromised patient with dental abscess and systemic signs
- Concern for aspiration of tooth fragment

**Dental referral urgency:**
- Emergent (same day): Ellis III, avulsed tooth (if not reimplanted), alveolar fracture
- Urgent (24-48 hours): Ellis II, reimplanted avulsed tooth, periapical abscess after I&D
- Routine (1-2 weeks): Ellis I, dental pain without abscess

## Pitfalls

1. **Failing to reimplant an avulsed permanent tooth in the ED.** Reimplantation success drops below 5% after 60 minutes of dry time. Emergency physicians should reimplant immediately rather than waiting for dental consultation. The tooth can always be extracted later — it cannot be reimplanted later.

2. **Reimplanting a primary (deciduous) tooth.** Primary teeth should never be reimplanted. Reimplantation risks damage to the underlying permanent tooth bud and ankylosis. Distinguish by patient age (primary teeth in children < 6-7 years) and tooth morphology (primary teeth are smaller, whiter, with bulbous crowns).

3. **Not searching for missing tooth fragments.** An unaccounted tooth fragment may be aspirated into the airway, embedded in a lip laceration, or swallowed. Always palpate lip lacerations before closure. Obtain CXR if the fragment is not found — a tooth in the right mainstem bronchus requires bronchoscopic removal.

4. **Misclassifying an Ellis III as Ellis II.** The distinction is critical: Ellis II (exposed dentin, yellow) is urgent but not emergent; Ellis III (exposed pulp, pink/red, bleeds) requires emergent dental intervention. Wipe the fracture surface with gauze and look for a pink or red spot with active bleeding — this is exposed pulp.

5. **Prescribing antibiotics alone for a fluctuant periapical abscess without drainage.** Antibiotics cannot penetrate an abscess cavity effectively. I&D is the definitive treatment. Antibiotics are adjunctive. Failure to drain leads to progressive infection and potential space extension to Ludwig angina.

6. **Missing an alveolar fracture.** If multiple adjacent teeth are mobile as a unit, the alveolar ridge is fractured. This is not just a dental injury — it requires reduction, stabilization, and oral surgery follow-up. Palpate the alveolar ridge in all dental trauma patients.

7. **Ignoring the airway in dental infections.** A dental abscess that has spread beyond the periapical region into the submandibular, sublingual, or parapharyngeal space can cause rapid airway compromise. Floor of mouth elevation, bilateral submandibular swelling, trismus, or dysphagia are red flags for impending airway emergency.

8. **Storing an avulsed tooth in water.** Tap water is hypotonic and destroys periodontal ligament cells within minutes. Preferred storage media in order: Hank Balanced Salt Solution (Save-A-Tooth kit), cold milk, patient's own saliva (have patient hold tooth in buccal sulcus), saline. Never use water, hydrogen peroxide, or alcohol.
