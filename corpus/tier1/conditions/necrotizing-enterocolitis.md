---
id: necrotizing-enterocolitis
condition: Necrotizing Enterocolitis
aliases: [NEC, neonatal NEC, necrotising enterocolitis]
icd10: [P77.1, P77.2, P77.3, P77.9]
esi: 1
time_to_harm:
  irreversible_injury: "< 6 hours (bowel necrosis progresses rapidly once transmural)"
  death: "< 24 hours without surgical intervention in advanced disease"
  optimal_intervention_window: "< 6 hours from clinical deterioration — early surgical consultation critical"
category: pediatric
track: tier1
sources:
  - type: review
    ref: "Neu J, Walker WA. Necrotizing enterocolitis. N Engl J Med. 2011;364(3):255-264."
    pmid: "21247316"
  - type: guideline
    ref: "AAP Section on Surgery, Committee on Fetus and Newborn. Necrotizing enterocolitis in the newborn. Pediatrics. 2002;110(1):158-160."
  - type: pubmed
    ref: "Bell MJ et al. Neonatal necrotizing enterocolitis: therapeutic decisions based upon clinical staging. Ann Surg. 1978;187(1):1-7."
    pmid: "413500"
  - type: pubmed
    ref: "Fitzgibbons SC et al. Mortality of necrotizing enterocolitis expressed by birth weight categories. J Pediatr Surg. 2009;44(6):1072-1075."
    pmid: "19524719"
  - type: review
    ref: "Patel RM et al. Causes and timing of death in extremely premature infants from 2000 through 2011. N Engl J Med. 2015;372(4):331-340."
    pmid: "25607427"
last_updated: "2026-02-26"
compiled_by: agent
reviewed_by: "Brandon Dent, MD — Board Certified Emergency Medicine"
review_date: "2026-02-27"
risk_tier: A
confusion_pairs:
  - condition: acute-appendicitis
    differentiators:
      - "NEC occurs in neonates (especially preterm < 32 weeks); appendicitis extremely rare in neonates"
      - "NEC shows pneumatosis intestinalis on abdominal X-ray"
      - "Formula feeding and prematurity are primary NEC risk factors"
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
# Necrotizing Enterocolitis

## Recognition

**Definition:** Necrotizing enterocolitis (NEC) is an inflammatory bowel necrosis primarily affecting premature neonates, characterized by mucosal or transmural intestinal necrosis, pneumatosis intestinalis, and systemic sepsis. It is the most common surgical emergency in neonates.

**Risk Factors:**
- Prematurity (< 32 weeks gestational age) — strongest risk factor
- Very low birth weight (< 1500 g)
- Formula feeding (breast milk is protective)
- Perinatal asphyxia, congenital heart disease, polycythemia
- Packed RBC transfusion ("transfusion-associated NEC")

**Clinical Presentation:**

| Feature | Notes |
|---------|-------|
| **Abdominal distension** | Progressive, tense; most common initial sign |
| **Feeding intolerance** | Increased gastric residuals, bilious emesis |
| **Bloody stools** | Grossly bloody or guaiac-positive; late sign suggests mucosal breakdown |
| **Abdominal wall erythema** | Ominous — suggests transmural necrosis and peritonitis |
| **Lethargy, apnea, temperature instability** | Systemic signs of sepsis; may precede abdominal findings |
| **Metabolic acidosis** | Lactate elevation; worsening acidosis predicts surgical NEC |
| **Thrombocytopenia, DIC** | Consumptive coagulopathy signals advanced disease |

**Bell Staging Criteria:**

| Stage | Features |
|-------|----------|
| **I (Suspected)** | Temperature instability, apnea, bradycardia, feeding intolerance, mild distension, guaiac-positive stool |
| **IIA (Definite, Mild)** | Stage I + absent bowel sounds, abdominal tenderness, pneumatosis intestinalis on X-ray |
| **IIB (Definite, Moderate)** | Stage IIA + metabolic acidosis, thrombocytopenia, abdominal wall cellulitis, portal venous gas |
| **IIIA (Advanced, No Perforation)** | Stage IIB + hypotension, respiratory failure, DIC |
| **IIIB (Advanced, Perforation)** | Stage IIIA + pneumoperitoneum |

## Critical Actions

1. **NPO immediately.** Stop all enteral feeding. Place orogastric tube to low intermittent suction for decompression. Do not resume feeds until clinical and radiographic resolution (typically 7-14 days for Bell II+).

2. **Volume resuscitation.** Normal saline 10-20 mL/kg IV bolus; repeat as needed for hypotension. Avoid dextrose-free fluids — neonates are hypoglycemia-prone. Target MAP appropriate for gestational age.

3. **Broad-spectrum antibiotics immediately.** Ampicillin 50 mg/kg IV q8h + gentamicin 4-5 mg/kg IV q24h (adjusted for gestational age) + metronidazole 7.5 mg/kg IV q12h (or clindamycin 5 mg/kg IV q8h). Cover gram-negatives, anaerobes, and enterococcus. Duration: 7-14 days depending on stage.

4. **Obtain abdominal X-ray (AP and left lateral decubitus).** Look for pneumatosis intestinalis (pathognomonic for Bell II+), portal venous gas (advanced disease), pneumoperitoneum (perforation — surgical emergency), fixed dilated loop (suggests necrotic segment).

5. **Surgical consultation immediately for Bell stage IIB or higher.** Absolute surgical indications: pneumoperitoneum, clinical deterioration despite maximal medical therapy, positive paracentesis (brown/bilious fluid), abdominal wall erythema.

6. **Serial abdominal X-rays every 6-8 hours** during acute phase. Progressive pneumatosis, new portal venous gas, or evolving pneumoperitoneum changes management.

7. **Correct coagulopathy.** Platelets for < 50,000 with active bleeding or planned procedure. FFP 10-15 mL/kg for INR > 1.5 with bleeding. Cryoprecipitate for fibrinogen < 100 mg/dL.

8. **Monitor for DIC, electrolyte derangements, and third-spacing.** Serial CBC, CMP, coagulation studies, blood gas q6-8h. Aggressive fluid replacement for massive third-space losses.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Spontaneous intestinal perforation (SIP)** | Occurs earlier (first week of life); isolated perforation without pneumatosis; typically ileum; less systemic inflammation; associated with indomethacin/dexamethasone use |
| **Sepsis without NEC** | No pneumatosis on X-ray; no abdominal distension or wall changes; blood cultures may identify source |
| **Malrotation with midgut volvulus** | Bilious emesis dominant; upper GI series shows corkscrew/bird-beak sign; presents acutely without preceding feeding intolerance; no pneumatosis |
| **Hirschsprung enterocolitis** | History of delayed meconium passage; distal obstruction pattern; suction rectal biopsy diagnostic |
| **Milk protein allergy** | Bloody stools but no systemic illness, no pneumatosis; resolves with formula change |
| **Intussusception** | Rare in neonates; currant-jelly stool; target sign on ultrasound |

## Workup

**Laboratory:**
- CBC with differential (leukocytosis or leukopenia; thrombocytopenia is prognostic)
- CMP (metabolic acidosis, hyponatremia from third-spacing)
- Blood gas (arterial or capillary) — pH, lactate, base deficit
- Coagulation: PT/INR, fibrinogen, D-dimer
- Blood culture (before antibiotics)
- CRP (serial trending useful for monitoring response)

**Imaging:**
- Abdominal X-ray AP supine + left lateral decubitus: pneumatosis, portal venous gas, pneumoperitoneum, fixed dilated loop, bowel wall thickening
- Abdominal ultrasound: increased sensitivity for portal venous gas, bowel wall thickness > 2.7 mm, absent peristalsis, free fluid
- CT rarely indicated in neonates — radiation risk and transport risk outweigh benefit

**Monitoring:**
- Continuous cardiorespiratory monitoring
- Strict I&O with daily weights
- Abdominal girth measurements q6h (increasing girth suggests progression)

## Treatment

**Medical Management (Bell Stage I-IIA):**
- NPO, OG decompression, IV fluids (D10 0.2NS at maintenance + deficit replacement)
- Antibiotics as above for 7-10 days
- Serial exams and X-rays q6-8h
- TPN initiation by day 2 if prolonged NPO anticipated

**Medical Management (Bell Stage IIB-IIIA):**
- All of above plus:
- Vasopressor support: dopamine 5-20 mcg/kg/min IV as first-line; add epinephrine 0.05-0.3 mcg/kg/min for refractory shock
- Mechanical ventilation for respiratory failure (high-frequency oscillatory ventilation if conventional fails)
- Aggressive correction of DIC: platelets, FFP, cryoprecipitate as above
- Paracentesis if tense ascites compromising ventilation

**Surgical Management (Bell Stage IIIB or failed medical therapy):**
- Exploratory laparotomy with resection of necrotic bowel and ostomy creation
- Primary peritoneal drainage as temporizing measure in ELBW infants (< 1000 g) too unstable for laparotomy
- Second-look laparotomy at 24-48 hours for borderline-viable bowel

## Disposition

**All NEC patients require NICU admission.** Transfer to a facility with pediatric surgery and NICU capabilities if not available.

**Transfer Indications:**
- Any Bell Stage II or higher without on-site pediatric surgery
- Clinical deterioration or hemodynamic instability
- Stabilize airway, establish IV access, initiate antibiotics, and decompress abdomen before transport

**Long-Term Complications:**
- Short bowel syndrome (post-resection) — requires TPN dependence, may need intestinal transplant
- Stricture formation (15-30% of medically managed NEC) — typically presents 3-8 weeks after acute episode
- Neurodevelopmental impairment (independent of prematurity)

## Pitfalls

1. **Attributing feeding intolerance and abdominal distension to benign causes in premature neonates.** NEC progresses rapidly — a premature infant with new feeding intolerance, abdominal distension, and bloody stools has NEC until proven otherwise. An abdominal X-ray must be obtained immediately. Delay in diagnosis of even 6 hours allows progression from Bell I to Bell III.

2. **Failure to obtain left lateral decubitus film.** Supine AP film alone misses small pneumoperitoneum. Free air rises to the non-dependent side and is best seen on left lateral decubitus view with horizontal beam. A missed perforation delays surgical intervention.

3. **Resuming feeds too early after NEC treatment.** Enteral feeding should not restart until clinical stability, resolution of abdominal tenderness, and normalization of X-ray findings (no residual pneumatosis). Premature refeeding causes recurrence. Minimum 7-10 days NPO for Bell II, 14 days for Bell III.

4. **Relying on pneumoperitoneum as the sole surgical indication.** Pneumoperitoneum indicates perforation, but absence of free air does not exclude surgical NEC. Worsening metabolic acidosis, increasing vasopressor requirements, fixed dilated loop on serial X-rays, abdominal wall erythema, and positive paracentesis are all indications for surgery — do not wait for free air.

5. **Underestimating fluid requirements.** Massive third-space fluid losses in NEC can exceed 200 mL/kg/day. Inadequate volume resuscitation leads to renal failure, worsening bowel ischemia, and cardiovascular collapse. Monitor urine output (target > 1 mL/kg/hr), serum sodium, and hemodynamic parameters hourly.
