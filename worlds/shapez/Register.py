from . import ShapezWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import ShapezWeb

"""
shapez is an automation game about cutting, rotating, stacking, and painting shapes, that you extract from randomly World Registration

This file contains the metadata and class references for the shapez world.
"""

# Required metadata
WORLD_NAME = "shapez"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = ShapezWorld
WEB_WORLD_CLASS = ShapezWeb
CLIENT_FUNCTION = None
