from . import MetroidPrimeWorld
from . import MetroidPrimeWeb

"""
Metroid Prime World Registration

This file contains the metadata and class references for the metroidprime world.
"""

# Required metadata
WORLD_NAME = "metroidprime"
GAME_NAME = "Metroid Prime"
IGDB_ID = 1105
AUTHOR = "Electro15"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = MetroidPrimeWorld
WEB_WORLD_CLASS = MetroidPrimeWeb
CLIENT_FUNCTION = None
