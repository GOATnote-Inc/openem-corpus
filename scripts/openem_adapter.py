"""OpenEM RAG adapter — DEPRECATED, use `from openem import OpenEMIndex` instead.

This file is kept for backward compatibility with code that imports
from the scripts/ directory via sys.path manipulation. New code should
install the openem package (`pip install -e /path/to/openem-corpus`)
and import directly.

Usage (new):
    from openem import OpenEMIndex

Usage (legacy):
    # sys.path.insert(0, "/path/to/openem-corpus/scripts")
    from openem_adapter import OpenEMIndex
"""

from openem.index import OpenEMIndex  # noqa: F401

__all__ = ["OpenEMIndex"]
