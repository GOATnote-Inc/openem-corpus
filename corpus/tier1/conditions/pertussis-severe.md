---
id: pertussis-severe
condition: Severe Pertussis
aliases: [whooping cough severe, malignant pertussis, critical pertussis, Bordetella pertussis infection]
icd10: [A37.00, A37.01, A37.91]
esi: 2
time_to_harm:
  irreversible_injury: "< 6 hours (apnea, hypoxic brain injury in neonates)"
  death: "< 24 hours in malignant pertussis"
  optimal_intervention_window: "< 6 hours from recognition"
category: pediatric
track: tier1
sources:
  - type: cdc
    ref: "CDC. Pertussis (Whooping Cough): Clinical Features. Updated 2022"
  - type: review
    ref: "Cherry JD. Pertussis in young infants throughout the world. Clin Infect Dis 2016;63(suppl 4):S119-S122"
last_updated: "2026-03-01"
compiled_by: agent
risk_tier: A
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
# Severe Pertussis

## Recognition

**Classic pertussis phases:**
1. **Catarrhal (1-2 weeks):** rhinorrhea, mild cough, low-grade fever — highly infectious, clinically indistinguishable from URI
2. **Paroxysmal (2-8 weeks):** paroxysmal cough with inspiratory "whoop," post-tussive emesis, cyanosis during paroxysms
3. **Convalescent (weeks to months):** gradual resolution

**Severe/malignant pertussis (primarily infants < 6 months):**
- Apneic episodes (may be the only presentation in young infants — cough may be absent)
- Cyanosis and desaturation during paroxysms
- Leukocytosis with extreme lymphocytosis (WBC > 50,000-100,000/mcL)
- Pulmonary hypertension from leukocyte-mediated thrombi
- Cardiac failure, refractory hypoxemia
- Mortality up to 1% overall; 3-4% in infants < 2 months

**High-risk populations:**
- Infants < 6 months (too young for complete vaccination)
- Neonates (maternal antibodies insufficient)
- Preterm infants
- Unvaccinated or incompletely vaccinated children

## Critical Actions

| Action | Target |
|---|---|
| Respiratory isolation (droplet precautions) | Immediate |
| Cardiopulmonary monitoring | Continuous |
| Nasopharyngeal swab for PCR | At presentation |
| Macrolide antibiotic | Within 1 hour |
| PICU admission for infants with apnea | Immediate |

1. **Droplet isolation** — highly contagious; mask the patient and staff
2. **Continuous cardiorespiratory monitoring** — apnea monitoring in all infants
3. **Supplemental oxygen** during paroxysmal episodes
4. **Nasopharyngeal swab for Bordetella pertussis PCR** (do not delay treatment for results)
5. **Start macrolide antibiotic** immediately
6. **Assess for malignant pertussis** — CBC with differential; WBC > 50,000 with lymphocyte predominance is ominous
7. **Notify public health** — pertussis is a reportable disease

## Differential Diagnosis

- Bronchiolitis (RSV — wheezing predominant, < 2 years, viral season)
- Chlamydia trachomatis pneumonia (afebrile, staccato cough, < 6 months, conjunctivitis history)
- Foreign body aspiration (sudden onset, witnessed event, unilateral findings)
- Croup (barking cough, stridor, no paroxysms)
- Reactive airway disease/asthma exacerbation (wheezing, response to bronchodilators)
- Mycoplasma pneumonia (older children, gradual onset, headache)
- Viral URI with post-infectious cough (no paroxysms, no whoop, no apnea)
- Cystic fibrosis (failure to thrive, recurrent infections, malabsorption)

## Workup

- **Nasopharyngeal swab for Bordetella pertussis PCR** — most sensitive test; swab must reach posterior nasopharynx (use Dacron or calcium alginate swab, NOT cotton)
- **Nasopharyngeal culture** — gold standard but takes 7-10 days; send in addition to PCR
- **CBC with differential:** lymphocyte-predominant leukocytosis; WBC > 20,000 in infants is concerning; WBC > 50,000 defines malignant pertussis
- **Chest X-ray:** perihilar infiltrates, atelectasis, "shaggy heart" sign (classic but not specific)
- **BMP:** electrolyte derangements from vomiting
- **Blood gas:** if respiratory distress or apnea — hypoxemia, hypercapnia
- **Echocardiogram:** in malignant pertussis — assess for pulmonary hypertension and RV dysfunction

## Treatment

### Antibiotics (Reduces Transmission; Modest Benefit on Disease Course If Started in Catarrhal Phase)
- **Azithromycin:**
  - Infants < 6 months: 10 mg/kg PO daily x 5 days
  - Children >= 6 months: 10 mg/kg PO day 1 (max 500 mg), then 5 mg/kg PO daily days 2-5 (max 250 mg)
- **Alternative: erythromycin** 40-50 mg/kg/day PO divided QID x 14 days (max 2 g/day)
- **Alternative: TMP-SMX** 8 mg/kg/day (TMP component) PO divided BID x 14 days (for macrolide allergy; age > 2 months)
- Antibiotics for ALL close contacts (post-exposure prophylaxis): same regimens

### Supportive Care
- **Supplemental oxygen** during paroxysms — titrate to SpO2 > 94%
- **Gentle suctioning** of nasal secretions
- **Small, frequent feeds** — paroxysms worsen with large-volume feeds
- **IV fluids** if unable to tolerate PO (D5NS or D5 1/2NS at maintenance rate)
- **Apnea monitoring** — continuous pulse oximetry and cardiorespiratory monitoring

### Malignant Pertussis (WBC > 50,000, Pulmonary Hypertension)
- **PICU admission** — mortality is 20-50%
- **Exchange transfusion or leukoreduction** — reduces leukocyte burden; evidence limited but may be lifesaving
- **Inhaled nitric oxide** 20 ppm for pulmonary hypertension
- **ECMO** for refractory cardiopulmonary failure
- **Avoid sedatives that suppress respiratory drive**

### Post-Exposure Prophylaxis
- **All household contacts** regardless of vaccination status: azithromycin at treatment doses
- **Pregnant women** in third trimester exposed: azithromycin (protects neonate)

## Disposition

- **Infants < 4 months with confirmed/suspected pertussis:** Admit for cardiorespiratory monitoring (apnea risk)
- **Infants 4-12 months with paroxysmal cough or any apnea/cyanosis:** Admit
- **Children > 12 months with mild paroxysmal cough, no apnea, tolerating PO:** Discharge with close follow-up in 24-48 hours; strict return precautions for apnea, cyanosis, or inability to feed
- **Malignant pertussis (leukocytosis > 50,000):** PICU admission
- **All patients:** reportable disease — notify public health

## Pitfalls

1. **Missing pertussis in a young infant presenting with apnea without cough.** In neonates and young infants, apnea may be the sole manifestation. Any infant with unexplained apneic episodes should have pertussis on the differential, especially if incompletely vaccinated.

2. **Discharging a young infant with "URI" without considering pertussis during the catarrhal phase.** The catarrhal phase is clinically indistinguishable from a viral URI. A parental report of progressive cough worsening over 1-2 weeks in an incompletely vaccinated infant warrants testing.

3. **Not recognizing malignant pertussis.** Extreme leukocytosis (WBC > 50,000) with lymphocyte predominance in a pertussis-infected infant is a medical emergency. Pulmonary hypertension from leukocyte aggregation carries > 20% mortality. Early exchange transfusion may be lifesaving.

4. **Failure to treat close contacts.** Pertussis is highly contagious. All household contacts need post-exposure prophylaxis with azithromycin regardless of vaccination status. Neonates are particularly vulnerable.

5. **Using cotton swabs for nasopharyngeal specimen.** Cotton inhibits Bordetella growth and degrades PCR targets. Use Dacron or calcium alginate swabs for accurate testing.
