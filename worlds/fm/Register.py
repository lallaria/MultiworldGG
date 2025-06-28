from . import FMWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import FMWeb

"""
Yu-Gi-Oh! Forbidden Memories is a PlayStation RPG with card-battling mechanics. Assume the role of the Prince of World Registration

This file contains the metadata and class references for the fm world.
"""

# Required metadata
WORLD_NAME = "fm"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = FMWorld
WEB_WORLD_CLASS = FMWeb
CLIENT_FUNCTION = None
