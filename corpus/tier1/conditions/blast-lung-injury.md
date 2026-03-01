---
id: blast-lung-injury
condition: Blast Lung Injury
aliases: [primary blast injury lung, blast overpressure injury, BLI, pulmonary blast injury]
icd10: [S27.319A, S27.329A, T70.8XXA]
esi: 1
time_to_harm:
  irreversible_injury: "< 2 hours"
  death: "< 4 hours"
  optimal_intervention_window: "< 1 hour"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "CDC: Explosions and Blast Injuries: A Primer for Clinicians. 2003, updated 2024"
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition, American College of Surgeons, 2018"
  - type: review
    ref: "Ritenour AE, Baskin TW. Primary blast injury: update on diagnosis and treatment. Crit Care Med. 2008;36(7 Suppl):S311-S317"
  - type: review
    ref: "Scott TE et al. Blast lung injury: epidemiology and management. Multidiscip Respir Med. 2017;12:6"
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
# Blast Lung Injury

## Recognition

**Mechanism:** Primary blast wave (overpressure) from explosion. The blast wave damages air-fluid interfaces — lungs are the most commonly affected solid organ. More severe in enclosed spaces (reflected waves amplify overpressure) and underwater.

**Blast injury categories:**
- **Primary:** Overpressure wave — blast lung, TM rupture, hollow viscus perforation, air embolism
- **Secondary:** Projectiles/fragments (shrapnel) — penetrating injuries
- **Tertiary:** Body displacement/structural collapse — blunt trauma, crush injury
- **Quaternary:** Burns, inhalation, chemical exposure

**Presentation of blast lung injury:**
- Dyspnea, tachypnea, hypoxia — may present immediately or delayed 24-48 hours
- Hemoptysis (pulmonary hemorrhage)
- Chest pain
- Cough
- Apnea (immediate, may be transient)
- Decreased breath sounds
- Wheezing
- Cyanosis
- Hemodynamic instability (air embolism or hemorrhage)

**Classic triad of BLI:** Apnea, bradycardia, hypotension immediately after blast

**Associated primary blast injuries:**
- Tympanic membrane rupture (most common primary blast injury — screening marker, 50% of TM rupture have BLI)
- Hollow viscus perforation (colon, stomach)
- Traumatic air embolism (alveolar-venous fistula — can cause sudden death, stroke, MI)

## Critical Actions

| Action | Target |
|---|---|
| High-flow O2 | Immediate |
| CXR | < 15 minutes |
| Otoscopic exam | < 30 minutes |
| Chest tube if pneumothorax | Immediate |
| Avoid PPV if possible | Until air embolism excluded |

1. **High-flow oxygen** via non-rebreather or HFNC — all blast-exposed patients with respiratory symptoms
2. **CXR immediately** — "butterfly" or "bat-wing" bilateral perihilar opacities classic for BLI. May be initially normal — repeat at 4-6 hours.
3. **Otoscopic exam** — TM rupture is a screening marker for primary blast exposure (sensitivity for BLI is limited, but absence in a large blast suggests less exposure)
4. **Bilateral chest tubes** if pneumothorax (primary blast commonly causes bilateral pneumothoraces)
5. **Avoid positive pressure ventilation when possible** — increases risk of air embolism (alveolar-venous fistula). If intubation required, use lowest effective pressures.
6. **Position patient with affected lung dependent** if air embolism suspected (reduces air entry into pulmonary veins)
7. **FAST exam** — blast injuries are multi-system; assess for hemoperitoneum, pneumothorax, pericardial effusion

## Differential Diagnosis

- Pulmonary contusion from secondary/tertiary blast injury (fragment or blunt — treated similarly)
- Tension pneumothorax (unilateral absent breath sounds, hypotension, tracheal deviation)
- Hemothorax (dullness, no air-fluid interface on CXR initially)
- ARDS from other cause (no blast exposure)
- Traumatic air embolism (sudden cardiovascular collapse after blast — consider in intubated patients)
- Fat embolism (delayed 24-72h, associated with long bone fractures)
- Inhalation injury (chemical exposure from blast — concurrent)
- Cardiac contusion (anterior chest wall proximity to blast)

## Workup

- **CXR:** Bilateral butterfly/perihilar opacities. May show pneumothorax, pneumomediastinum, subcutaneous emphysema. Can be initially normal — repeat at 4-6 hours.
- **CT chest:** More sensitive than CXR for contusion extent, pneumothorax, mediastinal air, vascular injury
- **ABG:** Hypoxemia (PaO2/FiO2 ratio to assess ARDS criteria), acidosis
- **Otoscopy:** TM perforation screening — blast exposure marker
- **Labs:** CBC, BMP, type and crossmatch, coagulation studies, lactate, troponin (blast cardiac injury)
- **ECG:** Arrhythmia screening, myocardial injury (air embolism to coronary arteries or direct blast cardiac injury)
- **FAST/E-FAST:** Pneumothorax, hemothorax, hemoperitoneum (concurrent secondary/tertiary injuries)
- **CT head:** If altered mental status (TBI from blast common — primary blast brain injury + secondary/tertiary mechanisms)

## Treatment

**Respiratory support:**
- High-flow O2 (15 L/min NRB) for mild-moderate hypoxia
- HFNC 40-60 L/min for refractory hypoxemia
- Avoid intubation/PPV unless absolutely necessary — PPV increases air embolism risk
- If mechanical ventilation required:
  - Lung-protective strategy: TV 4-6 mL/kg IBW (lower end given damaged alveoli)
  - PEEP 5-10 cmH2O (higher PEEP may worsen air leak/embolism)
  - Plateau pressure < 25 cmH2O (more conservative than standard ARDS — damaged alveolar-capillary interface)
  - Permissive hypercapnia (PaCO2 50-60 mmHg acceptable)
  - Avoid recruitment maneuvers (risk of air embolism)
- ECMO as rescue therapy for refractory hypoxemia

**Tube thoracostomy:**
- All pneumothoraces in blast injury require chest tube (never observe — PPV or transport can cause tension)
- 28-36 Fr chest tube — may need bilateral
- Low threshold for decompression — clinical diagnosis acceptable in resource-limited or mass casualty setting

**Air embolism management:**
- Left lateral decubitus position + Trendelenburg (trap air in RV apex away from outflow)
- 100% FiO2
- Avoid PPV (worsens embolism through alveolar-venous fistulae)
- Hyperbaric oxygen if available (definitive treatment)
- Emergent aspiration of air from RV via central line (if cardiac arrest from massive air embolism)

**Fluid management:**
- Judicious — avoid overresuscitation
- Crystalloid to maintain MAP > 65 mmHg; vasopressors (norepinephrine 0.05-0.3 mcg/kg/min) early if needed
- Blood products for concurrent hemorrhagic injuries (1:1:1 per MTP)

**Associated injuries:**
- Treat secondary (penetrating) and tertiary (blunt) injuries per standard trauma protocols
- Hollow viscus screening: serial abdominal exams, CT if symptomatic (blast bowel perforation peaks at 24-48 hours)

## Disposition

- **ICU:** All confirmed BLI (any CXR abnormality + respiratory symptoms after blast)
- **Observation (minimum 6-8 hours):** Asymptomatic blast-exposed patients with normal CXR — delayed presentation is common. Repeat CXR before discharge.
- **Discharge only if:** Normal CXR at 6-8 hours, normal oxygen saturation on room air, normal otoscopy, no abdominal symptoms, reliable follow-up
- **Transfer:** Trauma center with thoracic surgery and ideally hyperbaric capability
- **Mass casualty considerations:** Expectant category (black) for patients with severe BLI + TBI + multi-system injuries if resources are critically limited

## Pitfalls

1. **Normal initial CXR excludes blast lung injury.** BLI may not manifest on CXR for 24-48 hours. All blast-exposed patients with respiratory symptoms need serial imaging and observation.

2. **Aggressive positive pressure ventilation.** PPV increases risk of air embolism through damaged alveolar-capillary membranes. Use lowest effective pressures, permissive hypercapnia, and avoid recruitment maneuvers.

3. **Observing a small pneumothorax in a blast patient.** Unlike non-blast pneumothoraces, ANY pneumothorax in a blast patient requires tube thoracostomy. PPV during transport, intubation, or clinical deterioration can rapidly convert it to tension.

4. **Missing traumatic air embolism.** Sudden cardiovascular collapse or focal neurological deficit after blast (or after intubation of a blast patient) should raise suspicion for air embolism. Position patient left lateral decubitus + Trendelenburg. Consider HBO.

5. **Discharging blast-exposed patients without adequate observation.** Both BLI and blast bowel perforation can present with delayed onset (24-48 hours). Minimum 6-8 hour observation with repeat CXR for asymptomatic patients.

6. **Not examining tympanic membranes.** TM rupture is the most sensitive screening marker for primary blast exposure. Its absence does not exclude BLI, but its presence should heighten clinical suspicion.
