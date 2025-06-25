from . import ShapezWorld
from . import ShapezWeb

"""
shapez is an automation game about cutting, rotating, stacking, and painting shapes, that you extract from randomly World Registration

This file contains the metadata and class references for the shapez world.
"""

# Required metadata
WORLD_NAME = "shapez"
GAME_NAME = "shapez is an automation game about cutting, rotating, stacking, and painting shapes, that you extract from randomly"
IGDB_ID = 0
AUTHOR = "Unknown"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = ShapezWorld
WEB_WORLD_CLASS = ShapezWeb
CLIENT_FUNCTION = None
