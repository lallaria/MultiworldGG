from . import EOSWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import EOSWeb

"""
Pokemon Mystery Dungeon Explorers of Sky World Registration

This file contains the metadata and class references for the pmd_eos world.
"""

# Required metadata
WORLD_NAME = "pmd_eos"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = EOSWorld
WEB_WORLD_CLASS = EOSWeb
CLIENT_FUNCTION = None
