from . import OsuWebWorld

"""
osu! is a free to play rhythm game featuring 4 modes, an online ranking system/statistics, World Registration

This file contains the metadata and class references for the osu world.
"""

# Required metadata
WORLD_NAME = "osu"
GAME_NAME = "osu! is a free to play rhythm game featuring 4 modes, an online ranking system/statistics,"
IGDB_ID = 3012
AUTHOR = "Kanave"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = OsuWebWorld
WEB_WORLD_CLASS = None
CLIENT_FUNCTION = None
