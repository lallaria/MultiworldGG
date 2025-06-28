from . import AUSWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import AnUntitledStoryWeb

"""
An Untitled Story World Registration

This file contains the metadata and class references for the aus world.
"""

# Required metadata
WORLD_NAME = "aus"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = AUSWorld
WEB_WORLD_CLASS = AnUntitledStoryWeb
CLIENT_FUNCTION = None
