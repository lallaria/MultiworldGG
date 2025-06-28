from . import MonsterSanctuaryWorld, MonsterSanctuaryWebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Monster Sanctuary World Registration

This file contains the metadata and class references for the monster_sanctuary world.
"""

# Required metadata
WORLD_NAME = "monster_sanctuary"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = MonsterSanctuaryWorld
WEB_WORLD_CLASS = MonsterSanctuaryWebWorld
CLIENT_FUNCTION = None
