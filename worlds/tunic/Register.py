from . import TunicWorld
from . import TunicWeb

"""
TUNIC World Registration

This file contains the metadata and class references for the tunic world.
"""

# Required metadata
WORLD_NAME = "tunic"
GAME_NAME = "TUNIC"
IGDB_ID = 23733
AUTHOR = "SilentSR & ScipioWright"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = TunicWorld
WEB_WORLD_CLASS = TunicWeb
CLIENT_FUNCTION = None
