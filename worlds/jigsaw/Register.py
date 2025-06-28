from . import JigsawWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import JigsawWeb

"""
Make a Jigsaw puzzle! But first you'll have to find your pieces. World Registration

This file contains the metadata and class references for the jigsaw world.
"""

# Required metadata
WORLD_NAME = "jigsaw"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = JigsawWorld
WEB_WORLD_CLASS = JigsawWeb
CLIENT_FUNCTION = None
