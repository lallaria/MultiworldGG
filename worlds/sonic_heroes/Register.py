from . import SonicHeroesWorld
from . import SonicHeroesWeb

"""
Sonic Heroes is a 2003 platform game developed by Sonic Team USA. The player races a team of series characters through levels to amass rings, World Registration

This file contains the metadata and class references for the sonic_heroes world.
"""

# Required metadata
WORLD_NAME = "sonic_heroes"
GAME_NAME = "Sonic Heroes is a 2003 platform game developed by Sonic Team USA. The player races a team of series characters through levels to amass rings,"
IGDB_ID = 4156
AUTHOR = "xMcacutt"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = SonicHeroesWorld
WEB_WORLD_CLASS = SonicHeroesWeb
CLIENT_FUNCTION = None
