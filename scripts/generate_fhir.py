#!/usr/bin/env python3
"""Generate synthetic FHIR R4 Bundles from OpenEM presentation profiles.

Usage:
    python scripts/generate_fhir.py --condition anaphylaxis
    python scripts/generate_fhir.py --all
    python scripts/generate_fhir.py --all --output-dir /tmp/fhir --seed 42
    python scripts/generate_fhir.py --condition stemi --validate
    python scripts/generate_fhir.py --condition anaphylaxis --presentation classic_adult
"""

from __future__ import annotations

import argparse
import importlib
import importlib.util
import json
import sys
from pathlib import Path

# Import openem.fhir directly to avoid lancedb dependency from openem.__init__
_python_dir = str(Path(__file__).resolve().parent.parent / "python")
if _python_dir not in sys.path:
    sys.path.insert(0, _python_dir)

_spec = importlib.util.spec_from_file_location(
    "openem.fhir", Path(_python_dir) / "openem" / "fhir.py"
)
_fhir = importlib.util.module_from_spec(_spec)
sys.modules["openem.fhir"] = _fhir
_spec.loader.exec_module(_fhir)

generate_bundle = _fhir.generate_bundle
load_presentation = _fhir.load_presentation
validate_bundle = _fhir.validate_bundle


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate FHIR R4 Bundles from OpenEM presentation profiles"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--condition",
        help="Condition ID to generate a bundle for",
    )
    group.add_argument(
        "--all",
        action="store_true",
        help="Generate bundles for all available presentation profiles",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Output directory for bundles (default: fhir/bundles/)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for deterministic generation (default: 42)",
    )
    parser.add_argument(
        "--include-snomed",
        action="store_true",
        help="Include SNOMED CT codes in conditions (reference only)",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate generated bundles against FHIR R4 (requires fhir.resources)",
    )
    parser.add_argument(
        "--presentation",
        default=None,
        help="Specific presentation archetype name to use",
    )
    parser.add_argument(
        "--presentations-dir",
        default=None,
        help="Directory containing presentation YAML files",
    )

    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    presentations_dir = Path(args.presentations_dir) if args.presentations_dir else repo_root / "fhir" / "presentations"
    output_dir = Path(args.output_dir) if args.output_dir else repo_root / "fhir" / "bundles"
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.all:
        condition_ids = sorted(
            p.stem for p in presentations_dir.glob("*.yaml")
        )
        if not condition_ids:
            print(f"No presentation profiles found in {presentations_dir}")
            sys.exit(1)
    else:
        condition_ids = [args.condition]

    total_errors = 0

    for condition_id in condition_ids:
        try:
            profile = load_presentation(condition_id, presentations_dir)
        except FileNotFoundError as e:
            print(f"SKIP {condition_id}: {e}")
            continue

        presentations = profile.get("presentations", [])
        if args.presentation:
            names = [args.presentation]
        else:
            names = [p["name"] for p in presentations]

        for pres_name in names:
            bundle = generate_bundle(
                condition_id=condition_id,
                profile=profile,
                seed=args.seed,
                include_snomed=args.include_snomed,
                presentation_name=pres_name,
            )

            # Write bundle
            filename = f"{condition_id}_{pres_name}.json"
            output_path = output_dir / filename
            with open(output_path, "w") as f:
                json.dump(bundle, f, indent=2)

            n_entries = len(bundle.get("entry", []))
            print(f"OK  {condition_id}/{pres_name}: {n_entries} resources -> {output_path}")

            # Optional validation
            if args.validate:
                try:
                    errors = validate_bundle(bundle)
                    if errors:
                        for error in errors:
                            print(f"    FAIL: {error}")
                        total_errors += len(errors)
                    else:
                        print(f"    VALID (FHIR R4)")
                except ImportError as e:
                    print(f"    SKIP validation: {e}")
                    break

    if total_errors:
        print(f"\n{total_errors} validation error(s)")
        sys.exit(1)
    else:
        print(f"\nGenerated {len(condition_ids)} bundle(s) in {output_dir}")


if __name__ == "__main__":
    main()
