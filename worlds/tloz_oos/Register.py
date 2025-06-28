from . import OracleOfSeasonsWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import OracleOfSeasonsWeb

"""
The Legend of Zelda - Oracle of Seasons World Registration

This file contains the metadata and class references for the tloz_oos world.
"""

# Required metadata
WORLD_NAME = "tloz_oos"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = OracleOfSeasonsWorld
WEB_WORLD_CLASS = OracleOfSeasonsWeb
CLIENT_FUNCTION = None
