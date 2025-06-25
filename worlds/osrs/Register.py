from . import OSRSWorld
from . import OSRSWeb

"""
Old School Runescape World Registration

This file contains the metadata and class references for the osrs world.
"""

# Required metadata
WORLD_NAME = "osrs"
GAME_NAME = "Old School Runescape"
IGDB_ID = 79824
AUTHOR = "digiholic"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = OSRSWorld
WEB_WORLD_CLASS = OSRSWeb
CLIENT_FUNCTION = None
