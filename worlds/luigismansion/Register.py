from . import LMWorld, LMWeb

"""
Luigi's Mansion is an adventure game starring everyone's favorite plumber brother, Luigi. World Registration

This file contains the metadata and class references for the luigismansion world.
"""

# Required metadata
WORLD_NAME = "luigismansion"
GAME_NAME = "Luigi's Mansion"
IGDB_ID = 2485
AUTHOR = "BootsinSoots"
VERSION = "0.4.7"

# Plugin entry points
WORLD_CLASS = LMWorld
WEB_WORLD_CLASS = LMWeb
CLIENT_FUNCTION = None
