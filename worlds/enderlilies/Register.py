from . import EnderLiliesWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import EnderLiliesWeb

"""
Ender Lilies World Registration

This file contains the metadata and class references for the enderlilies world.
"""

# Required metadata
WORLD_NAME = "enderlilies"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = EnderLiliesWorld
WEB_WORLD_CLASS = EnderLiliesWeb
CLIENT_FUNCTION = None
