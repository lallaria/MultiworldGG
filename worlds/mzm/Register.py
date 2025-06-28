from . import MZMWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import MZMWeb

"""
Metroid: Zero Mission is a retelling of the first Metroid on NES. Relive Samus' first adventure on planet Zebes with World Registration

This file contains the metadata and class references for the mzm world.
"""

# Required metadata
WORLD_NAME = "mzm"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = MZMWorld
WEB_WORLD_CLASS = MZMWeb
CLIENT_FUNCTION = None
