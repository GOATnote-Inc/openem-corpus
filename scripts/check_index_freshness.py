#!/usr/bin/env python3
"""Check if the OpenEM search index is up-to-date with the corpus.

Compares the condition file count in the corpus against the manifest.
If a corpus_fingerprint is present, also checks file-level changes.

Exit 0 = fresh, Exit 1 = stale or missing.
"""

import json
import hashlib
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONDITIONS_DIR = REPO_ROOT / "corpus" / "tier1" / "conditions"
MANIFEST_PATH = REPO_ROOT / "data" / "index" / "manifest.json"


def main() -> int:
    if not MANIFEST_PATH.exists():
        print(f"STALE: No manifest at {MANIFEST_PATH}. Run: make build-index")
        return 1

    manifest = json.loads(MANIFEST_PATH.read_text())
    md_files = sorted(CONDITIONS_DIR.glob("*.md"))
    current_count = len(md_files)
    manifest_count = manifest.get("corpus_file_count", manifest.get("num_conditions"))

    if current_count != manifest_count:
        print(
            f"STALE: Corpus has {current_count} conditions but index was built with "
            f"{manifest_count}. Run: make build-index"
        )
        return 1

    # Fingerprint check (available if index was built with build_index.py >= 0.2.0)
    manifest_fp = manifest.get("corpus_fingerprint")
    if manifest_fp:
        entries = []
        for md_file in md_files:
            entries.append(f"{md_file.name}:{md_file.stat().st_size}")
        current_fp = hashlib.sha256("\n".join(entries).encode()).hexdigest()[:16]
        if current_fp != manifest_fp:
            print(
                f"STALE: Corpus fingerprint changed ({manifest_fp} → {current_fp}). "
                f"Run: make build-index"
            )
            return 1

    print(f"FRESH: Index matches corpus ({current_count} conditions).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
