"""Shared fixtures for OpenEM corpus test suite."""

import re
from pathlib import Path

import pytest
import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
CONDITIONS_DIR_TIER1 = REPO_ROOT / "corpus" / "tier1" / "conditions"
CONDITIONS_DIR_TIER2 = REPO_ROOT / "corpus" / "tier2" / "conditions"


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture(scope="session")
def conditions_dir() -> Path:
    """Primary conditions directory (tier1). Skips if absent."""
    if not CONDITIONS_DIR_TIER1.exists():
        pytest.skip(f"Conditions dir not found: {CONDITIONS_DIR_TIER1}")
    return CONDITIONS_DIR_TIER1


@pytest.fixture(scope="session")
def sample_condition_text() -> str:
    """Minimal valid emergency condition markdown."""
    return """\
---
id: test-emergency
condition: Test Emergency Condition
aliases: [test emergency, TEC]
icd10: [I21.01]
esi: 1
time_to_harm: "< 6 hours"
mortality_if_delayed: "50% untreated"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "AHA 2023 Guidelines for Test Emergency"
last_updated: "2026-01-01"
compiled_by: agent
risk_tier: A
validation:
  schema_version: "2.0"
  outlier_detection_flag: clear
---
# Test Emergency Condition

## Recognition

Severe chest pain with ST elevation. Immediate intervention required. This is a
life-threatening emergency that must be recognized and treated within minutes.
Patient presents with acute onset severe substernal chest pain.

## Critical Actions

- Activate cath lab immediately
- Aspirin 325 mg PO
- Heparin 5000 units IV bolus
- IV access x2, continuous monitoring
- 12-lead ECG within 10 minutes of arrival

## Differential Diagnosis

- Aortic dissection
- Pulmonary embolism
- Pericarditis

## Workup

- 12-lead ECG
- Troponin I/T (high sensitivity)
- CMP, CBC, coagulation studies
- Portable CXR

## Treatment

- Primary PCI is preferred reperfusion strategy
- Door-to-balloon time target < 90 minutes
- Antiplatelet therapy: aspirin plus P2Y12 inhibitor

## Disposition

- Cardiac ICU admission
- Cardiology consult

## Pitfalls

- Missing posterior STEMI: obtain V7-V9 leads
- Failure to activate cath lab for LBBB with Sgarbossa criteria
- Giving nitroglycerin with inferior STEMI without ruling out RV involvement
"""


@pytest.fixture(scope="session")
def sample_defer_condition_text() -> str:
    """Minimal valid defer condition with optional defer fields."""
    return """\
---
id: benign-positional-vertigo
condition: Benign Positional Vertigo
aliases: [BPPV, benign paroxysmal positional vertigo]
icd10: [H81.10]
esi: 4
time_to_harm: "days to weeks (recurrence risk, low acuity)"
category: neurological
track: tier1
sources:
  - type: guideline
    ref: "AAO-HNS Clinical Practice Guideline: Benign Paroxysmal Positional Vertigo (2017 Update)"
last_updated: "2026-01-01"
compiled_by: agent
risk_tier: C
disposition_default: outpatient
escalation_triggers:
  - new focal neurological deficit
  - severe headache
  - inability to ambulate
confusion_pairs:
  - condition: posterior-circulation-stroke
    differentiators:
      - BPPV is purely positional; stroke vertigo may be constant
      - Nystagmus in BPPV is transient and fatigable
validation:
  schema_version: "2.0"
  outlier_detection_flag: clear
---
# Benign Positional Vertigo

## Recognition

Brief episodes of vertigo triggered by head position changes. Hallpike maneuver
positive with characteristic upbeat-torsional nystagmus. Most common cause of
vertigo in the emergency department. Self-limited in majority of cases.

## Critical Actions

- Dix-Hallpike test to confirm diagnosis
- Neurological exam to exclude central cause
- Epley maneuver for posterior canal BPPV

## Differential Diagnosis

- Vestibular neuritis
- Posterior circulation stroke
- Meniere disease

## Workup

- Dix-Hallpike test
- Head impulse test
- HINTS exam if central cause suspected

## Treatment

- Epley canalith repositioning maneuver (90% effective)
- Vestibular suppressants generally not recommended
- Activity restriction until maneuver complete

## Disposition

- Outpatient discharge with return precautions
- Vestibular rehabilitation referral if recurrent

## Pitfalls

- Missing posterior circulation stroke (HINTS exam: head impulse normal, direction-changing nystagmus, skew deviation)
- Prescribing meclizine routinely (delays recovery, no evidence benefit over placebo)
- Failing to perform Epley in ED (high success rate, reduces recurrence)
"""


def _collect_condition_files() -> list[Path]:
    """Collect all condition .md files from tier1 and tier2."""
    files = []
    for d in [CONDITIONS_DIR_TIER1, CONDITIONS_DIR_TIER2]:
        if d.exists():
            files.extend(sorted(d.glob("*.md")))
    return files


_ALL_CONDITION_FILES = _collect_condition_files()


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "slow: mark test as slow (requires LanceDB index)"
    )


@pytest.fixture(
    scope="session",
    params=_ALL_CONDITION_FILES if _ALL_CONDITION_FILES else [None],
    ids=[f.stem for f in _ALL_CONDITION_FILES]
    if _ALL_CONDITION_FILES
    else ["no-files"],
)
def all_condition_files(request) -> Path:
    """Parametrized fixture: yields each real condition file path."""
    if request.param is None:
        pytest.skip("No condition files found in corpus/")
    return request.param
