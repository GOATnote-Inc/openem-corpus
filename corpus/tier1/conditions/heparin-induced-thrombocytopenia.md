---
id: heparin-induced-thrombocytopenia
condition: Heparin-Induced Thrombocytopenia
aliases: [HIT, HIT type II, heparin-induced thrombocytopenia and thrombosis, HITT]
icd10: [D75.82]
esi: 2
time_to_harm: "< 24 hours (arterial/venous thrombosis); < 48 hours (limb-threatening ischemia, PE, stroke)"
category: hematologic
track: tier1
sources:
  - type: guideline
    ref: "ASH 2018 Guidelines for Management of Venous Thromboembolism: Heparin-Induced Thrombocytopenia"
  - type: review
    ref: "Practical Guide to the Diagnosis and Management of Heparin-Induced Thrombocytopenia. Hematology ASH Education, 2024"
  - type: review
    ref: "Management of Heparin-Induced Thrombocytopenia: A Contemporary Review. J Clin Med, 2024"
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
# Heparin-Induced Thrombocytopenia

## Recognition

**Key features:**
- Platelet count drop >= 50% from baseline (even if nadir remains > 150,000)
- Timing: Typically 5-10 days after heparin initiation ("typical onset")
- Rapid onset (< 24 hours) if prior heparin exposure within past 100 days
- Thrombosis (venous more common than arterial) in 25-50% of untreated cases
- Occurs with both unfractionated heparin (UFH) and low-molecular-weight heparin (LMWH), though more common with UFH

**Clinical manifestations:**
- Deep vein thrombosis (most common)
- Pulmonary embolism
- Arterial thrombosis (limb ischemia, stroke, MI)
- Skin necrosis at heparin injection sites
- Adrenal hemorrhage (bilateral adrenal vein thrombosis)
- Cerebral venous sinus thrombosis
- White clot syndrome (platelet-rich thrombi)

**4Ts Score (Pre-test Probability):**
- **Thrombocytopenia:** > 50% fall or nadir 20-100k (2), 30-50% fall or nadir 10-19k (1), < 30% fall or nadir < 10k (0)
- **Timing:** 5-10 days or < 1 day with prior heparin in 30 days (2), consistent with days 5-10 but not clear or > 10 days (1), < 4 days without recent exposure (0)
- **Thrombosis:** Confirmed new thrombosis or skin necrosis (2), progressive or recurrent thrombosis or suspected (1), none (0)
- **oTher causes:** None apparent (2), possible other cause (1), definite other cause (0)
- Score 0-3: Low probability (< 5%); 4-5: Intermediate; 6-8: High probability (> 80%)

## Critical Actions

1. **STOP ALL HEPARIN immediately** — including heparin flushes, heparin-coated lines, and LMWH
2. **Start non-heparin anticoagulation** — even if NO active thrombosis (50% will thrombose if untreated)
3. **Argatroban 2 mcg/kg/min IV** (reduce to 0.5-1.2 mcg/kg/min if hepatic impairment) — first-line for most patients
4. **OR Bivalirudin 0.15-0.2 mg/kg/hr IV** — preferred in renal impairment or if PCI needed
5. **Send HIT antibody testing** — immunoassay (PF4/heparin ELISA) then confirmatory functional assay (SRA)
6. **Do NOT transfuse platelets** unless life-threatening hemorrhage
7. **Do NOT start warfarin** until platelets > 150,000 (warfarin causes limb gangrene in acute HIT)

## Differential Diagnosis

- Drug-induced thrombocytopenia (non-heparin) — antibiotics, GPIIb/IIIa inhibitors
- Sepsis-associated thrombocytopenia — fever, hemodynamic instability, positive cultures
- DIC — prolonged PT, low fibrinogen, schistocytes
- ITP — isolated thrombocytopenia, no thrombosis
- TTP — MAHA, neurologic symptoms, ADAMTS13 < 10%
- Post-operative thrombocytopenia — hemodilution, consumption (usually days 1-3, not 5-10)
- HIT type I (non-immune) — mild platelet drop (> 100k), days 1-4, no clinical significance, resolves spontaneously

## Workup

- **4Ts score** — calculate for all suspected cases; low score (0-3) effectively rules out HIT
- **PF4/heparin ELISA (immunoassay):**
  - Highly sensitive (> 97%) but less specific
  - Optical density (OD) > 2.0 strongly suggests true HIT
  - OD < 0.4 effectively rules out HIT
- **Serotonin release assay (SRA)** — gold standard confirmatory test; results take days
- **Heparin-induced platelet aggregation (HIPA)** — alternative functional assay
- **CBC with platelet count** — monitor daily; track nadir and % decline
- **Duplex ultrasound of extremities** — screen for DVT even if asymptomatic (bilateral LE at minimum)
- **CT angiography** if arterial thrombosis or PE suspected
- **Coagulation studies** — PT/INR (baseline for argatroban monitoring), aPTT (target 1.5-3x normal for argatroban)
- **Fibrinogen, D-dimer** — elevated D-dimer typical; helps distinguish from DIC if fibrinogen normal

## Treatment

### Non-Heparin Anticoagulation (Start Immediately)
**Argatroban (direct thrombin inhibitor):**
- 2 mcg/kg/min IV continuous infusion (no bolus)
- Monitor aPTT q2h initially; target aPTT 1.5-3x baseline
- **Hepatic dose reduction:** 0.5-1.2 mcg/kg/min if hepatic impairment (Child-Pugh B/C)
- **Caution:** Argatroban falsely elevates INR; use chromogenic factor X assay when transitioning to warfarin

**Bivalirudin (direct thrombin inhibitor):**
- 0.15-0.2 mg/kg/hr IV (no bolus for HIT)
- For PCI: 0.75 mg/kg IV bolus, then 1.75 mg/kg/hr
- Monitor aPTT; target 1.5-2.5x baseline
- **Preferred in:** Renal impairment (short half-life, partial renal clearance), patients needing PCI

**Fondaparinux (factor Xa inhibitor):**
- 5-10 mg SC daily (weight-based: < 50 kg = 5 mg, 50-100 kg = 7.5 mg, > 100 kg = 10 mg)
- Used off-label; no monitoring needed in most patients
- Avoid if CrCl < 30 mL/min

### Transition to Long-Term Anticoagulation
- **Warfarin:** Start ONLY when platelets > 150,000; overlap with parenteral anticoagulant for >= 5 days and INR therapeutic for >= 2 days
- Start warfarin at low dose (5 mg or less) to avoid warfarin-induced skin necrosis (protein C depletion)
- **DOACs:** Rivaroxaban or apixaban increasingly used for transition; start when platelets > 150,000 and after initial parenteral anticoagulation

### Duration of Anticoagulation
- HIT with thrombosis: Minimum 3 months
- HIT without thrombosis: Minimum 4 weeks (or until platelet recovery)

### What NOT to Do
- Do NOT give warfarin before platelets recover (risk of venous limb gangrene/skin necrosis)
- Do NOT transfuse platelets (fuels thrombosis)
- Do NOT use LMWH (cross-reacts with HIT antibodies in ~90% of cases)

## Disposition

- **All suspected HIT with active thrombosis:** ICU or step-down unit
- **HIT without thrombosis:** Admit to monitored bed; continuous argatroban infusion
- **Hematology consultation** — for confirmatory testing interpretation and transition planning
- **Vascular surgery** if limb-threatening ischemia
- **Flag the chart:** HIT allergy alert — patient must NEVER receive heparin products again (until antibody clearance documented, typically > 100 days)
- **Isolation:** Standard precautions
- **Reportable:** Not a reportable disease

## Pitfalls

1. **Not stopping ALL heparin, including flushes.** Heparin flushes for IV lines, heparin-coated catheters, and LMWH all contain heparin and sustain the immune response. Every source must be eliminated.

2. **Starting warfarin before platelet recovery.** Warfarin depletes protein C faster than procoagulant factors, creating a transient hypercoagulable state. In HIT, this causes limb gangrene and skin necrosis. Never start warfarin until platelets > 150,000.

3. **Transfusing platelets.** Platelet transfusion in HIT provides additional substrate for PF4/heparin-mediated platelet activation and thrombosis. Only transfuse for life-threatening hemorrhage.

4. **Not anticoagulating HIT patients without visible thrombosis.** Up to 50% of HIT patients without thrombosis at diagnosis will develop thrombosis if not anticoagulated. Therapeutic anticoagulation (not prophylactic dose) is required.

5. **Dismissing a moderate 4Ts score.** A score of 4-5 carries a 14-30% probability of HIT — too high to ignore. Send testing and start non-heparin anticoagulation while awaiting results.

6. **Using LMWH as an alternative.** LMWH cross-reacts with HIT antibodies in approximately 90% of cases. It is NOT a safe substitute. Only non-heparin anticoagulants are acceptable.
