from . import SubnauticaWorld, SubnauticaWeb

"""
Subnautica World Registration

This file contains the metadata and class references for the subnautica world.
"""

# Required metadata
WORLD_NAME = "subnautica"
GAME_NAME = "Subnautica"
IGDB_ID = 9254
AUTHOR = "Berserker66"
VERSION = "0.5.0"

# Plugin entry points
WORLD_CLASS = SubnauticaWorld
WEB_WORLD_CLASS = SubnauticaWeb
CLIENT_FUNCTION = None
