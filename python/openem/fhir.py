"""FHIR R4 Bundle generation from OpenEM condition presentation profiles.

Generates synthetic FHIR R4 Bundles from condition definitions,
enabling evaluation of system-facing AI (prior auth, CDS Hooks,
EHR copilot, triage routing).

No hard dependency on fhir.resources — generator produces plain
JSON-serializable dicts conforming to FHIR R4. Validation via
fhir.resources is optional (CI/test-time only).
"""

from __future__ import annotations

import json
import random
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore[assignment]


# Default presentations directory relative to repo root
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_DEFAULT_PRESENTATIONS_DIR = _REPO_ROOT / "fhir" / "presentations"

# FHIR coding system URIs
ICD10_SYSTEM = "http://hl7.org/fhir/sid/icd-10-cm"
SNOMED_SYSTEM = "http://snomed.info/sct"
LOINC_SYSTEM = "http://loinc.org"


def load_presentation(
    condition_id: str,
    presentations_dir: str | Path | None = None,
) -> dict[str, Any]:
    """Load a presentation profile for a condition.

    Args:
        condition_id: OpenEM condition identifier (e.g., "anaphylaxis").
        presentations_dir: Directory containing presentation YAML files.
            Defaults to fhir/presentations/ in the repo root.

    Returns:
        Parsed presentation profile dict.

    Raises:
        FileNotFoundError: If no profile exists for the condition.
        ImportError: If PyYAML is not installed.
    """
    if yaml is None:
        raise ImportError("PyYAML is required: pip install pyyaml")

    presentations_dir = Path(presentations_dir or _DEFAULT_PRESENTATIONS_DIR)
    profile_path = presentations_dir / f"{condition_id}.yaml"

    if not profile_path.exists():
        raise FileNotFoundError(
            f"No presentation profile for '{condition_id}' at {profile_path}"
        )

    with open(profile_path) as f:
        return yaml.safe_load(f)


def generate_bundle(
    condition_id: str,
    profile: dict[str, Any],
    seed: int = 42,
    include_snomed: bool = False,
    presentation_name: str | None = None,
) -> dict[str, Any]:
    """Generate a FHIR R4 Bundle from a presentation profile.

    Args:
        condition_id: OpenEM condition identifier.
        profile: Parsed presentation profile (from load_presentation).
        seed: Random seed for deterministic synthetic values.
        include_snomed: Whether to include SNOMED CT codes in conditions.
        presentation_name: Specific presentation archetype to use.
            If None, uses the first presentation in the profile.

    Returns:
        FHIR R4 Bundle as a JSON-serializable dict.

    Raises:
        ValueError: If presentation_name not found in profile.
    """
    presentations = profile.get("presentations", [])
    if not presentations:
        raise ValueError(f"No presentations defined for '{condition_id}'")

    if presentation_name:
        matches = [p for p in presentations if p["name"] == presentation_name]
        if not matches:
            available = [p["name"] for p in presentations]
            raise ValueError(
                f"Presentation '{presentation_name}' not found. "
                f"Available: {available}"
            )
        presentation = matches[0]
    else:
        presentation = presentations[0]

    rng = random.Random(seed)

    # Use seed-derived UUIDs for determinism
    base_uuid = uuid.UUID(int=rng.getrandbits(128), version=4)
    patient_id = str(uuid.UUID(int=base_uuid.int + 1, version=4))
    encounter_id = str(uuid.UUID(int=base_uuid.int + 2, version=4))

    # Generate timestamp
    base_time = datetime(2026, 1, 15, 14, 30, 0, tzinfo=timezone.utc)
    offset_minutes = rng.randint(-120, 120)
    encounter_time = base_time + timedelta(minutes=offset_minutes)
    timestamp = encounter_time.isoformat()

    patient_ref = f"Patient/{patient_id}"
    encounter_ref = f"Encounter/{encounter_id}"

    # Build resources
    patient = _make_patient(presentation, rng, patient_id)
    encounter = _make_encounter(
        presentation, patient_ref, encounter_id, timestamp
    )

    entries = [
        {"fullUrl": f"urn:uuid:{patient_id}", "resource": patient},
        {"fullUrl": f"urn:uuid:{encounter_id}", "resource": encounter},
    ]

    # Conditions
    for cond_data in presentation.get("conditions", []):
        cond_id = str(uuid.UUID(int=base_uuid.int + len(entries) + 1, version=4))
        condition = _make_condition(
            cond_data, patient_ref, encounter_ref, include_snomed,
            cond_id, timestamp,
        )
        entries.append(
            {"fullUrl": f"urn:uuid:{cond_id}", "resource": condition}
        )

    # Vitals
    for obs_data in presentation.get("vitals", []):
        obs_id = str(uuid.UUID(int=base_uuid.int + len(entries) + 1, version=4))
        obs = _make_observation(
            obs_data, patient_ref, encounter_ref, rng,
            obs_id, timestamp, category="vital-signs",
        )
        entries.append({"fullUrl": f"urn:uuid:{obs_id}", "resource": obs})

    # Labs
    for lab_data in presentation.get("labs", []):
        lab_id = str(uuid.UUID(int=base_uuid.int + len(entries) + 1, version=4))
        lab_category = lab_data.get("category", "laboratory")
        obs = _make_observation(
            lab_data, patient_ref, encounter_ref, rng,
            lab_id, timestamp, category=lab_category,
        )
        entries.append({"fullUrl": f"urn:uuid:{lab_id}", "resource": obs})

    bundle = {
        "resourceType": "Bundle",
        "id": str(base_uuid),
        "type": "collection",
        "timestamp": timestamp,
        "entry": entries,
        "meta": {
            "source": f"openem/{condition_id}/{presentation['name']}",
            "tag": [
                {
                    "system": "http://openem.org/tags",
                    "code": "synthetic",
                    "display": "Synthetic data for evaluation only",
                }
            ],
        },
    }

    return bundle


def validate_bundle(bundle: dict[str, Any]) -> list[str]:
    """Validate a FHIR R4 Bundle using fhir.resources.

    Args:
        bundle: FHIR Bundle dict to validate.

    Returns:
        List of validation error messages (empty if valid).

    Raises:
        ImportError: If fhir.resources is not installed.
    """
    try:
        from fhir.resources.bundle import Bundle
    except ImportError:
        raise ImportError(
            "fhir.resources is required for validation: "
            "pip install 'fhir.resources>=8.0'"
        )

    errors = []
    try:
        Bundle.model_validate(bundle)
    except Exception as e:
        errors.append(str(e))
    return errors


def _make_patient(
    presentation: dict[str, Any],
    rng: random.Random,
    patient_id: str,
) -> dict[str, Any]:
    """Generate a synthetic FHIR Patient resource."""
    patient_config = presentation.get("patient", {})
    age_range = patient_config.get("age_range", [30, 60])
    sex_options = patient_config.get("sex", ["male", "female"])

    age = rng.randint(age_range[0], age_range[1])
    sex = rng.choice(sex_options)

    # Compute birth date from age
    birth_year = 2026 - age
    birth_date = f"{birth_year}-{rng.randint(1, 12):02d}-{rng.randint(1, 28):02d}"

    # FHIR gender mapping
    gender_map = {"male": "male", "female": "female"}

    return {
        "resourceType": "Patient",
        "id": patient_id,
        "gender": gender_map.get(sex, "unknown"),
        "birthDate": birth_date,
    }


def _make_encounter(
    presentation: dict[str, Any],
    patient_ref: str,
    encounter_id: str,
    timestamp: str,
) -> dict[str, Any]:
    """Generate a synthetic FHIR Encounter resource."""
    enc_config = presentation.get("encounter", {})
    enc_class = enc_config.get("class", "emergency")

    # FHIR encounter class coding
    class_map = {
        "emergency": {"code": "EMER", "display": "emergency"},
        "inpatient": {"code": "IMP", "display": "inpatient encounter"},
        "observation": {"code": "OBSENC", "display": "observation encounter"},
    }
    class_coding = class_map.get(enc_class, class_map["emergency"])

    encounter = {
        "resourceType": "Encounter",
        "id": encounter_id,
        "status": "in-progress",
        "class": {
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
            "code": class_coding["code"],
            "display": class_coding["display"],
        },
        "subject": {"reference": patient_ref},
        "period": {"start": timestamp},
    }

    # Add ESI as priority
    esi = enc_config.get("esi")
    if esi:
        encounter["priority"] = {
            "coding": [
                {
                    "system": "http://hl7.org/fhir/ValueSet/v3-ActPriority",
                    "code": f"ESI-{esi}",
                    "display": f"Emergency Severity Index {esi}",
                }
            ]
        }

    return encounter


def _make_condition(
    cond_data: dict[str, Any],
    patient_ref: str,
    encounter_ref: str,
    include_snomed: bool,
    condition_id: str,
    timestamp: str,
) -> dict[str, Any]:
    """Generate a synthetic FHIR Condition resource."""
    codings = [
        {
            "system": ICD10_SYSTEM,
            "code": cond_data["icd10"],
            "display": cond_data["display"],
        }
    ]

    if include_snomed and cond_data.get("snomed"):
        codings.append(
            {
                "system": SNOMED_SYSTEM,
                "code": cond_data["snomed"],
                "display": cond_data["display"],
            }
        )

    return {
        "resourceType": "Condition",
        "id": condition_id,
        "clinicalStatus": {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
                    "code": "active",
                }
            ]
        },
        "verificationStatus": {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status",
                    "code": "confirmed",
                }
            ]
        },
        "code": {"coding": codings, "text": cond_data["display"]},
        "subject": {"reference": patient_ref},
        "encounter": {"reference": encounter_ref},
        "recordedDate": timestamp,
    }


def _make_observation(
    obs_data: dict[str, Any],
    patient_ref: str,
    encounter_ref: str,
    rng: random.Random,
    obs_id: str,
    timestamp: str,
    category: str = "vital-signs",
) -> dict[str, Any]:
    """Generate a synthetic FHIR Observation resource."""
    value_range = obs_data["value_range"]
    value = rng.uniform(value_range[0], value_range[1])

    # Round appropriately based on the range
    if value_range[1] - value_range[0] > 10:
        value = round(value, 0)
    else:
        value = round(value, 1)

    # Category coding
    category_map = {
        "vital-signs": {
            "system": "http://terminology.hl7.org/CodeSystem/observation-category",
            "code": "vital-signs",
            "display": "Vital Signs",
        },
        "laboratory": {
            "system": "http://terminology.hl7.org/CodeSystem/observation-category",
            "code": "laboratory",
            "display": "Laboratory",
        },
    }

    return {
        "resourceType": "Observation",
        "id": obs_id,
        "status": "final",
        "category": [{"coding": [category_map.get(category, category_map["vital-signs"])]}],
        "code": {
            "coding": [
                {
                    "system": LOINC_SYSTEM,
                    "code": obs_data["code"],
                    "display": obs_data["display"],
                }
            ],
            "text": obs_data["display"],
        },
        "subject": {"reference": patient_ref},
        "encounter": {"reference": encounter_ref},
        "effectiveDateTime": timestamp,
        "valueQuantity": {
            "value": value,
            "unit": obs_data["unit"],
            "system": "http://unitsofmeasure.org",
            "code": obs_data["ucum"],
        },
    }
