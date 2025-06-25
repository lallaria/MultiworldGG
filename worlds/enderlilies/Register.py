from . import EnderLiliesWorld
from . import EnderLiliesWeb

"""
Ender Lilies World Registration

This file contains the metadata and class references for the enderlilies world.
"""

# Required metadata
WORLD_NAME = "enderlilies"
GAME_NAME = "Ender Lilies"
IGDB_ID = 138858
AUTHOR = "Trexounay"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = EnderLiliesWorld
WEB_WORLD_CLASS = EnderLiliesWeb
CLIENT_FUNCTION = None
