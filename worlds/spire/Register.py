from . import SpireWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import SpireWeb

"""
Slay the Spire World Registration

This file contains the metadata and class references for the spire world.
"""

# Required metadata
WORLD_NAME = "spire"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = SpireWorld
WEB_WORLD_CLASS = SpireWeb
CLIENT_FUNCTION = None
