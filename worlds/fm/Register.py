from . import FMWorld
from . import FMWeb

"""
Yu-Gi-Oh! Forbidden Memories is a PlayStation RPG with card-battling mechanics. Assume the role of the Prince of World Registration

This file contains the metadata and class references for the fm world.
"""

# Required metadata
WORLD_NAME = "fm"
GAME_NAME = "Yu-Gi-Oh! Forbidden Memories"
IGDB_ID = 4108
AUTHOR = "sg4e"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = FMWorld
WEB_WORLD_CLASS = FMWeb
CLIENT_FUNCTION = None
