from . import SonicHeroesWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import SonicHeroesWeb

"""
Sonic Heroes is a 2003 platform game developed by Sonic Team USA. The player races a team of series characters through levels to amass rings, World Registration

This file contains the metadata and class references for the sonic_heroes world.
"""

# Required metadata
WORLD_NAME = "sonic_heroes"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = SonicHeroesWorld
WEB_WORLD_CLASS = SonicHeroesWeb
CLIENT_FUNCTION = None
