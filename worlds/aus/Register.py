from . import AUSWorld
from . import AnUntitledStoryWeb

"""
An Untitled Story World Registration

This file contains the metadata and class references for the aus world.
"""

# Required metadata
WORLD_NAME = "aus"
GAME_NAME = "An Untitled Story"
IGDB_ID = 72926
AUTHOR = "ThatOneGuy27"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = AUSWorld
WEB_WORLD_CLASS = AnUntitledStoryWeb
CLIENT_FUNCTION = None
