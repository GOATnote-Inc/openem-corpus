---
id: commotio-cordis
condition: Commotio Cordis
aliases: [cardiac concussion, commotio cordis syndrome, blunt impact cardiac arrest]
icd10: [S26.91XA]
esi: 1
time_to_harm:
  irreversible_injury: "< 3 minutes"
  death: "< 10 minutes"
  optimal_intervention_window: "< 3 minutes (defibrillation)"
category: cardiovascular
track: tier1
sources:
  - type: review
    ref: "Maron BJ, et al. Commotio Cordis. N Engl J Med. 2010;362(10):917-927."
  - type: review
    ref: "Link MS. Commotio Cordis: Ventricular Fibrillation Triggered by Chest Impact–Induced Abnormalities in Repolarization. Circ Arrhythm Electrophysiol. 2012;5(2):425-432."
  - type: guideline
    ref: "2020 AHA Guidelines for CPR and Emergency Cardiovascular Care. Circulation. 2020;142(16 Suppl 2)."
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
# Commotio Cordis

## Recognition

**Classic scenario:**
- Sudden cardiac arrest immediately following blunt, nonpenetrating impact to the precordium
- Structurally normal heart — NO underlying cardiac pathology
- Impact typically from a projectile (baseball, hockey puck, lacrosse ball, cricket ball) or body contact
- Predominantly young males (mean age 15 years, range 3-50)
- Collapse within seconds of chest impact

**Pathophysiology:**
- Impact occurs during the vulnerable period of repolarization (T-wave upstroke, 10-30 ms before T-wave peak)
- Mechanically induced depolarization triggers ventricular fibrillation
- Impact velocity 30-50 mph, directly over cardiac silhouette
- Does NOT require high-force impact — moderate-force blows at the critical timing window are sufficient

**Arrest rhythm:**
- Ventricular fibrillation (most common)
- Less commonly: complete heart block, ventricular tachycardia, asystole (late)

**Distinguishing from contusio cordis (cardiac contusion):**
- Commotio cordis: structurally normal heart, VF from electrical disruption, lower-force impact
- Contusio cordis: structural myocardial damage, high-force blunt trauma, troponin elevation, wall motion abnormalities

## Critical Actions

| Action | Target |
|---|---|
| CPR initiation | Immediate |
| Defibrillation | < 3 minutes |
| AED application | < 1 minute |

1. **Immediate CPR** — recognize cardiac arrest (unresponsive, no pulse after witnessed chest impact)
2. **Early defibrillation** — survival directly proportional to time to first shock
   - AED application immediately
   - Manual defibrillator: 200 J biphasic unsynchronized
   - Survival > 50% if defibrillation within 3 minutes; drops to < 20% after 5 minutes
3. **Follow standard ACLS VF protocol:**
   - Defibrillation → CPR 2 min → reassess → defibrillation
   - Epinephrine 1 mg IV/IO q3-5min after second shock
   - Amiodarone 300 mg IV/IO (first dose), then 150 mg (second dose) for refractory VF
4. **Post-ROSC care:** Standard post-cardiac arrest protocol including targeted temperature management
5. **Once stabilized:** Rule out structural cardiac injury (cardiac contusion) — troponin, ECG, echocardiography

## Differential Diagnosis

- **Cardiac contusion (contusio cordis)** — high-force trauma; troponin elevated, wall motion abnormalities on echo
- **Traumatic aortic disruption** — widened mediastinum on CXR, hemodynamic instability
- **Tension pneumothorax** — chest trauma causing pneumothorax with hemodynamic compromise
- **Hemothorax** — chest trauma with blood in pleural space
- **Pre-existing channelopathy (LQTS, Brugada, CPVT)** — chest impact may be incidental; post-arrest workup required
- **Hypertrophic cardiomyopathy** — underlying structural disease causing SCD during sports; not impact-related

## Workup

**During resuscitation:**
- Rhythm analysis: VF is expected finding
- Rapid assessment for pneumothorax, hemothorax (chest trauma)

**Post-ROSC:**
- **Troponin (serial):** Differentiate commotio from contusio cordis. Mild elevation may occur from CPR/defibrillation; significant elevation suggests myocardial contusion.
- **12-lead ECG:** Assess for ST changes, QT prolongation, Brugada pattern, conduction abnormalities
- **Echocardiography:** Rule out structural heart disease, wall motion abnormalities, pericardial effusion, valvular injury
- **CT chest:** If concern for structural injury (rib fracture, pneumothorax, aortic injury)
- **Cardiac MRI (post-stabilization):** Definitive assessment for myocardial edema/contusion, structural heart disease
- **Genetic testing/channelopathy workup:** Consider if no clear precipitating impact or atypical features — rule out LQTS, Brugada, HCM, ARVC

## Treatment

### Acute Resuscitation
- ACLS for VF/pulseless VT (see Critical Actions)
- Defibrillation is the definitive treatment — no specific pharmacotherapy for commotio cordis beyond standard ACLS

### Post-ROSC Management
- Targeted temperature management: maintain 32-36°C for >= 24 hours (per post-cardiac arrest guidelines)
- Hemodynamic optimization: MAP > 65 mmHg, adequate coronary and cerebral perfusion
- Serial troponin monitoring
- Continuous telemetry for >= 48 hours
- Neuroprognostication per standard protocols (delay >= 72 hours)

### Long-Term
- If structurally normal heart confirmed and no channelopathy identified: favorable prognosis
- No standard indication for ICD if commotio cordis is the sole diagnosis (structurally normal heart, normal EP studies)
- Return-to-play decisions: individualized, typically 3-6 months with cardiology clearance
- Chest protectors (Nocsae-approved): recommended for athletes in high-risk sports, though efficacy is debated

## Disposition

- **ICU admission:** All survivors — post-cardiac arrest management, targeted temperature management, telemetry
- **Post-mortem:** Contact medical examiner for fatalities; autopsy confirms structurally normal heart
- **Transfer criteria:** Transfer to pediatric cardiac center or facility with TTM capability if needed
- **Follow-up:** Cardiology/EP consultation for all survivors, including channelopathy screening and sports clearance

## Pitfalls

1. **Not recognizing cardiac arrest after chest impact.** A young athlete who collapses after being hit in the chest may initially appear to be "just stunned." Brief consciousness after impact does not exclude commotio cordis — VF can degenerate from initial transient rhythm disturbance. Any collapse after chest impact requires immediate pulse check.

2. **Delaying defibrillation while waiting for EMS.** Survival from commotio cordis is almost entirely dependent on time to defibrillation. On-site AEDs at sporting events are critical. Every minute of delay in defibrillation reduces survival by 7-10%.

3. **Attributing arrest to "a hit to the chest" without ruling out underlying cardiac disease.** Commotio cordis is a diagnosis of exclusion — the heart must be structurally normal. HCM, ARVC, LQTS, and Brugada syndrome can all cause sudden cardiac death in athletes coincident with physical contact. Full cardiac workup is mandatory post-ROSC.

4. **Performing CPR only without defibrillation.** CPR alone does not convert VF. While CPR maintains organ perfusion, defibrillation is the definitive treatment. Bystander CPR + early AED is the survival combination.

5. **Assuming chest protectors provide complete protection.** Commercial chest protectors have NOT been consistently shown to prevent commotio cordis. They may reduce risk but should not be relied upon as sole prevention.
