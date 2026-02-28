"""OpenEM — Python interface to the OpenEM emergency medicine corpus.

Provides hybrid search over the pre-built LanceDB index and a bridge
layer for downstream projects (ScribeGoat2, LostBench) that handles
deduplication, section priority, and context-budget management.

Usage:
    from openem import OpenEMIndex, OpenEMBridge

    index = OpenEMIndex("/path/to/openem/data/index")
    bridge = OpenEMBridge(index)  # auto-loads canonical condition map
    context = bridge.get_context("stemi", max_chars=3000)
"""

__version__ = "0.3.0"

from openem.index import OpenEMIndex
from openem.bridge import OpenEMBridge
from openem.conditions import load_condition_map

__all__ = ["OpenEMIndex", "OpenEMBridge", "load_condition_map", "__version__"]
