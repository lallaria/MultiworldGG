from . import OracleOfAgesWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import OracleOfAgesWeb

"""
The Legend of Zelda - Oracle of Ages World Registration

This file contains the metadata and class references for the tloz_ooa world.
"""

# Required metadata
WORLD_NAME = "tloz_ooa"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = OracleOfAgesWorld
WEB_WORLD_CLASS = OracleOfAgesWeb
CLIENT_FUNCTION = None
