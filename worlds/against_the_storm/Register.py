from . import AgainstTheStormWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import AgainstTheStormWeb

"""
Against the Storm World Registration

This file contains the metadata and class references for the against_the_storm world.
"""

# Required metadata
WORLD_NAME = "against_the_storm"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = AgainstTheStormWorld
WEB_WORLD_CLASS = AgainstTheStormWeb
CLIENT_FUNCTION = None
