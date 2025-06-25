from . import JigsawWorld
from . import JigsawWeb

"""
Make a Jigsaw puzzle! But first you'll have to find your pieces. World Registration

This file contains the metadata and class references for the jigsaw world.
"""

# Required metadata
WORLD_NAME = "jigsaw"
GAME_NAME = "Make a Jigsaw puzzle! But first you'll have to find your pieces."
IGDB_ID = 0
AUTHOR = "spinerak"
VERSION = "0.6.6"

# Plugin entry points
WORLD_CLASS = JigsawWorld
WEB_WORLD_CLASS = JigsawWeb
CLIENT_FUNCTION = None
