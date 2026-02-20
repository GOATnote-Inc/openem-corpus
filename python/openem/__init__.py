"""OpenEM — Python interface to the OpenEM emergency medicine corpus.

Provides hybrid search over the pre-built LanceDB index and a bridge
layer for downstream projects (ScribeGoat2, LostBench) that handles
deduplication, section priority, and context-budget management.

Usage:
    from openem import OpenEMIndex, OpenEMBridge

    index = OpenEMIndex("/path/to/openem/data/index")
    bridge = OpenEMBridge(index, condition_map={"neonatal_sepsis": ["neonatal-emergencies", "sepsis"]})
    context = bridge.get_context("neonatal_sepsis", max_chars=3000)
"""

from openem.index import OpenEMIndex
from openem.bridge import OpenEMBridge

__all__ = ["OpenEMIndex", "OpenEMBridge"]
