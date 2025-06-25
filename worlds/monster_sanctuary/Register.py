from . import MonsterSanctuaryWorld, MonsterSanctuaryWebWorld

"""
Monster Sanctuary World Registration

This file contains the metadata and class references for the monster_sanctuary world.
"""

# Required metadata
WORLD_NAME = "monster_sanctuary"
GAME_NAME = "Monster Sanctuary"
IGDB_ID = 89594
AUTHOR = "Saagael"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = MonsterSanctuaryWorld
WEB_WORLD_CLASS = MonsterSanctuaryWebWorld
CLIENT_FUNCTION = None
