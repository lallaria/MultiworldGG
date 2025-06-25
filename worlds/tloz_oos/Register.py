from . import OracleOfSeasonsWorld
from . import OracleOfSeasonsWeb

"""
The Legend of Zelda - Oracle of Seasons World Registration

This file contains the metadata and class references for the tloz_oos world.
"""

# Required metadata
WORLD_NAME = "tloz_oos"
GAME_NAME = "The Legend of Zelda - Oracle of Seasons"
IGDB_ID = 1032
AUTHOR = "Dinopony"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = OracleOfSeasonsWorld
WEB_WORLD_CLASS = OracleOfSeasonsWeb
CLIENT_FUNCTION = None
