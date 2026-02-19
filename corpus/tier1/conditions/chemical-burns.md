---
id: chemical-burns
condition: Chemical Burns
aliases: [chemical injury, caustic burn, acid burn, alkali burn, corrosive burn]
icd10: [T20.40XA, T21.40XA, T25.40XA, T26.40XA, T30.4, T54.2X1A, T54.3X1A]
esi: 2
time_to_harm: "< 30 minutes (ongoing tissue destruction; HF burns: minutes to fatal arrhythmia)"
category: environmental
track: tier1
sources:
  - type: guideline
    ref: "Palao R et al. Chemical burns: pathophysiology and treatment. Burns 2010;36(3):295-304"
    pmid: "19864073"
  - type: review
    ref: "Bertolini JC. Hydrofluoric acid: a review of toxicity. J Emerg Med 1992;10(2):163-168"
    pmid: "1607623"
  - type: guideline
    ref: "Kirkpatrick JJR et al. An algorithmic approach to the treatment of hydrofluoric acid burns. Burns 1995;21(7):483-493"
    pmid: "8540974"
  - type: review
    ref: "Hatzifotis M et al. Hydrofluoric acid burns. Burns 2004;30(2):156-159"
    pmid: "15019125"
  - type: guideline
    ref: "Edlich RF et al. Modern concepts of treatment and prevention of chemical injuries. J Long Term Eff Med Implants 2005;15(3):303-318"
    pmid: "16022641"
  - type: review
    ref: "Hall AH, Rumack BH. Clinical toxicology of cyanide. Ann Emerg Med 1986;15(9):1067-1074"
    pmid: "3526995"
last_updated: "2026-02-18"
compiled_by: agent
risk_tier: B
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
# Chemical Burns

## Recognition

**Mechanism:** Tissue destruction by chemical agents through protein denaturation, oxidation, reduction, corrosion, desiccation, or vesicant action. Unlike thermal burns, chemical burns cause ongoing tissue damage until the agent is fully removed or neutralized.

**Key Chemical Classes:**
- **Alkali (bases):** NaOH, KOH, cement (calcium hydroxide), ammonia, bleach. Cause liquefactive necrosis — penetrate deeper and longer than acids. Cement burns are insidious (delayed presentation, prolonged contact).
- **Acids:** HCl, H2SO4, HNO3, HF, chromic acid. Cause coagulative necrosis (self-limiting except HF). Tissue eschar limits further penetration (except HF).
- **Hydrofluoric acid (HF):** Unique mechanism — fluoride ion penetrates deeply, chelates calcium and magnesium, causes severe systemic hypocalcemia/hypomagnesemia and fatal cardiac arrhythmias. Even small BSA (< 2%) HF burns to digits can be lethal.
- **Phenol (carbolic acid):** Causes coagulative necrosis; rapidly absorbed systemically causing CNS depression, hepatotoxicity, cardiac arrhythmias.
- **White phosphorus:** Ignites spontaneously on exposure to air; causes thermal and chemical burns simultaneously. Particles embedded in wounds continue burning when dry.

**Presentation:**
- Pain (often severe, out of proportion to appearance in early HF burns)
- Skin erythema, blistering, tissue necrosis (may appear deceptively mild initially with alkali or HF)
- HF burns: initial pain may be delayed 1-24 hours for dilute solutions (< 20%); concentrated HF (> 50%) causes immediate pain and visible burns
- Eye exposure: pain, tearing, blepharospasm, corneal opacification (alkali eye burns are ophthalmologic emergencies)
- Inhalation: stridor, hoarseness, dyspnea, pulmonary edema (if caustic fumes inhaled)

## Critical Actions

1. **Copious water irrigation immediately** — remove all clothing and jewelry. Irrigate with lukewarm water for minimum 15-30 minutes. Alkali burns: irrigate for 1-2 hours (liquefactive necrosis continues). Use litmus/pH paper to confirm skin surface pH 7.0-7.5 before stopping irrigation.
2. **Identify the chemical agent** — contact Poison Control (1-800-222-1222), obtain SDS/MSDS. Treatment varies by agent.
3. **HF exposure — treat aggressively regardless of burn size:**
   - Topical calcium gluconate 2.5% gel: apply continuously to affected area, reapply q15-30 min until pain resolves
   - Calcium gluconate 10% intradermal/subcutaneous injection: 0.5 mL per cm2 of affected area (use 27-30 gauge needle, max 0.5 mL per injection site)
   - Intra-arterial calcium gluconate: 10 mL of 10% calcium gluconate diluted in 40 mL NS via radial/brachial artery over 4 hours (for digit/hand burns) — consult hand surgery or toxicology
   - IV calcium gluconate 10%: 20 mL IV over 10 min for systemic toxicity (QTc prolongation, arrhythmia, serum calcium < 7 mg/dL)
   - Monitor serum calcium and magnesium q1h
   - Continuous cardiac monitoring — watch for QTc prolongation, torsades de pointes, ventricular fibrillation
4. **Phenol burns:** wipe affected area with PEG 300 or PEG 400 (polyethylene glycol) BEFORE water irrigation. PEG dissolves phenol and reduces systemic absorption. If PEG unavailable, use isopropyl alcohol, then copious water irrigation.
5. **White phosphorus burns:** keep wound continuously wet (particles ignite in air). Debride visible particles under UV/Wood lamp (phosphorus fluoresces). Copper sulfate 1% solution can be used briefly to identify particles (turns black on contact) but is itself toxic — do not leave on wound.
6. **Eye chemical burns:** immediate continuous irrigation with NS or LR via Morgan lens for minimum 30 minutes. Check pH at 5-minute intervals after irrigation stops; continue irrigation until pH 7.0-7.4. Emergent ophthalmology consult for all alkali eye exposures.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Thermal burn | History of heat/flame exposure, no ongoing tissue destruction after removal from source, dermatomal pattern |
| Electrical burn | Entry/exit wounds, deep tissue injury disproportionate to skin findings, rhabdomyolysis |
| Contact dermatitis | Pruritic, vesicular, less acutely destructive, allergen history, delayed onset (Type IV) |
| Stevens-Johnson syndrome/TEN | Drug exposure history, mucosal involvement, Nikolsky sign, systemic illness, diffuse distribution |
| Radiation burn | Radiation exposure history, delayed presentation (hours-days), erythema without immediate tissue destruction |
| Frostbite | Cold exposure, waxy/white skin, rewarming causes erythema and blistering |
| Necrotizing fasciitis | Pain out of proportion (similar to HF), but fever, crepitus, rapid spread, systemic toxicity |

## Workup

**All Chemical Burns:**
- Identify agent (SDS/MSDS, employer, Poison Control)
- Assess burn depth and BSA (Lund-Browder chart or rule of nines)
- BMP (renal function, electrolytes)
- CBC
- Urinalysis (myoglobinuria if significant soft tissue injury)
- CXR if inhalation suspected
- Wound pH with litmus paper (guide irrigation duration)

**HF Burns (add):**
- Ionized calcium, magnesium — STAT, repeat q1h
- 12-lead ECG (QTc prolongation, arrhythmia)
- Continuous cardiac monitoring
- ABG/VBG (metabolic acidosis in systemic toxicity)
- Potassium (hyperkalemia from tissue injury)

**Eye Burns (add):**
- pH measurement of conjunctival fornix (before and after irrigation)
- Visual acuity
- Slit lamp exam (corneal clarity, limbal ischemia — Roper-Hall classification)
- IOP measurement (after irrigation complete)

**Inhalation Injury (add):**
- Direct laryngoscopy/fiberoptic nasopharyngoscopy
- CXR (pulmonary edema, ARDS)
- ABG (acidosis, hypoxia)
- Carboxyhemoglobin if fire/combustion involved

## Treatment

**Decontamination (all chemical burns):**
- Remove all clothing and jewelry immediately (double-glove caregivers to prevent secondary exposure)
- Copious water irrigation: minimum 15-30 minutes for acid burns, 1-2 hours for alkali burns
- Do NOT attempt chemical neutralization (exothermic reaction worsens injury)
- Target skin surface pH 7.0-7.5 before stopping irrigation
- Dry chemical agents: brush off excess BEFORE irrigation (some react violently with water: elemental sodium, potassium, lithium)

**HF-Specific Treatment:**
- Topical calcium gluconate 2.5% gel: mix 3.5 g calcium gluconate powder in 150 mL water-soluble lubricant (KY jelly). Apply continuously, massage into affected area. Reapply q15-30 min. Pain relief = surrogate marker of adequate calcium delivery.
- Intradermal/subcutaneous calcium gluconate 10%: 0.5 mL per cm2, injected with 27-30 gauge needle. Avoid digit injection > 0.5 mL per phalanx (compartment risk).
- Intra-arterial calcium gluconate (for hand/digit burns): 10 mL of 10% calcium gluconate in 40 mL NS infused over 4 hours via radial artery (Bier block technique alternative). Consult toxicology/hand surgery.
- Systemic HF toxicity (hypocalcemia, hypomagnesemia, cardiac arrhythmia): calcium gluconate 10% 20-30 mL IV bolus, repeat as needed. Magnesium sulfate 2-4 g IV. Treat ventricular arrhythmias per ACLS with additional calcium repletion.
- Do NOT use calcium chloride subcutaneously (causes tissue necrosis).

**Cement Burns:**
- Prolonged irrigation (alkali pH 12-13); often delayed presentation (patients unaware of burn until hours later)
- Treat as alkali burn; check wound pH

**Phenol Burns:**
- Wipe with PEG 300/400 or isopropyl alcohol first
- Then copious water irrigation
- Monitor for systemic toxicity: altered mental status, seizures, hepatotoxicity, cardiac arrhythmias

**White Phosphorus:**
- Keep wound wet at all times
- Debride particles under UV/Wood lamp (fluoresces)
- Copper sulfate 1% solution briefly for identification only (toxic if left on wound)
- Burn center referral

**Wound Management:**
- Silver sulfadiazine (avoid on face/near eyes) or bacitracin for superficial burns
- Burn center referral criteria: > 10% BSA, full-thickness, face/hands/feet/genitalia/major joints, HF burns, inhalation injury

## Disposition

**Discharge:**
- Small, superficial acid burns (< 5% BSA) with completed decontamination, no systemic symptoms, reliable follow-up in 24 hours
- Mild cement burns after thorough irrigation and pH normalization

**Admission (Burn Unit/ICU):**
- HF burns (any size) — minimum 24-hour cardiac monitoring even for small exposures
- Alkali burns > 5% BSA or any full-thickness chemical burn
- Burns to face, hands, feet, perineum, major joints
- Inhalation injury
- Systemic toxicity (phenol, HF, white phosphorus)
- Circumferential burns (escharotomy may be needed)
- Eye burns with corneal opacification or limbal ischemia (ophthalmology admission)

**Transfer to Burn Center:**
- > 10% BSA chemical burn
- Full-thickness chemical burns
- Burns to critical areas (face, hands, feet, genitalia, major joints)
- HF burns with systemic toxicity
- White phosphorus burns
- Concomitant inhalation injury

## Pitfalls

1. **Insufficient irrigation duration.** The single most important treatment is prolonged copious water irrigation. Most errors involve stopping too early. Alkali burns require 1-2 hours minimum. Use pH paper to confirm skin pH 7.0-7.5 before stopping. Tissue destruction continues until the chemical is fully removed.

2. **Underestimating HF burn severity based on appearance.** Dilute HF (< 20%) burns may appear trivial — mild erythema or no visible skin changes — but fluoride ions penetrate deeply and chelate systemic calcium. A 2.5% BSA HF burn to the hand has caused fatal cardiac arrest from hypocalcemia. Any HF exposure requires calcium monitoring and cardiac telemetry regardless of skin appearance.

3. **Not monitoring calcium and magnesium in HF burns.** HF causes systemic hypocalcemia and hypomagnesemia that progress rapidly. Fatal ventricular fibrillation occurs without warning. Check ionized calcium and magnesium q1h for at least 24 hours. Continuous cardiac monitoring is mandatory.

4. **Attempting chemical neutralization.** Applying an acid to neutralize an alkali burn (or vice versa) produces an exothermic reaction that adds thermal injury to chemical injury. Copious water irrigation is always the correct initial treatment. The only exception is dry chemicals that react with water (elemental metals) — brush off first, then irrigate.

5. **Using water first for phenol burns.** Water alone spreads phenol and increases absorption surface area. PEG 300/400 (or isopropyl alcohol if PEG unavailable) should be applied first to dissolve and remove phenol, followed by copious water irrigation.

6. **Letting white phosphorus wounds dry.** White phosphorus ignites spontaneously on contact with air. Wounds must be kept continuously wet with saline-soaked gauze. Dry debridement in the operating room without continuous irrigation causes re-ignition and further injury to patient and staff.

7. **Stopping eye irrigation too early.** Alkali eye burns cause ongoing liquefactive necrosis. Irrigate with Morgan lens for minimum 30 minutes, then check conjunctival pH at 5-minute intervals. Resume irrigation if pH > 7.4. Delays in ophthalmology consultation for alkali eye burns with limbal ischemia or corneal opacification risk permanent vision loss.

8. **Missing cement burns due to delayed presentation.** Wet cement (calcium hydroxide, pH 12-13) causes painless initial contact that progresses to full-thickness alkali burn over hours. Construction workers often present 8-12 hours after exposure with deep burns. Obtain an occupational exposure history in any patient with unexplained lower extremity burns or skin breakdown.

9. **Using calcium chloride instead of calcium gluconate for subcutaneous HF treatment.** Calcium chloride causes tissue necrosis when injected subcutaneously or intradermally. Only calcium gluconate 10% is safe for local injection. Calcium chloride is reserved for IV use only in cardiac arrest or severe systemic hypocalcemia.

10. **Failing to protect staff from secondary chemical exposure.** Chemical decontamination without proper PPE (double gloving, gowns, eye protection, ventilation for volatile agents) exposes healthcare workers to injury. HF and phenol in particular can cause significant secondary exposure through skin contact or inhalation.
