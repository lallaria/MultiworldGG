from . import MZMWorld
from . import MZMWeb

"""
Metroid: Zero Mission is a retelling of the first Metroid on NES. Relive Samus' first adventure on planet Zebes with World Registration

This file contains the metadata and class references for the mzm world.
"""

# Required metadata
WORLD_NAME = "mzm"
GAME_NAME = "Metroid: Zero Mission is a retelling of the first Metroid on NES. Relive Samus' first adventure on planet Zebes with"
IGDB_ID = 1107
AUTHOR = "Noise"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = MZMWorld
WEB_WORLD_CLASS = MZMWeb
CLIENT_FUNCTION = None
