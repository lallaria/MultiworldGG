from . import OSRSWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import OSRSWeb

"""
Old School Runescape World Registration

This file contains the metadata and class references for the osrs world.
"""

# Required metadata
WORLD_NAME = "osrs"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = OSRSWorld
WEB_WORLD_CLASS = OSRSWeb
CLIENT_FUNCTION = None
