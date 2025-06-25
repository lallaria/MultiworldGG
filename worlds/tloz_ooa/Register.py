from . import OracleOfAgesWorld
from . import OracleOfAgesWeb

"""
The Legend of Zelda - Oracle of Ages World Registration

This file contains the metadata and class references for the tloz_ooa world.
"""

# Required metadata
WORLD_NAME = "tloz_ooa"
GAME_NAME = "The Legend of Zelda - Oracle of Ages"
IGDB_ID = 1041
AUTHOR = "Dinopony"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = OracleOfAgesWorld
WEB_WORLD_CLASS = OracleOfAgesWeb
CLIENT_FUNCTION = None
