from . import TimespinnerWebWorld, TimespinnerWorld

"""
Timespinner World Registration

This file contains the metadata and class references for the timespinner world.
"""

# Required metadata
WORLD_NAME = "timespinner"
GAME_NAME = "Timespinner"
IGDB_ID = 28952
AUTHOR = "Jarno458"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = TimespinnerWorld
WEB_WORLD_CLASS = TimespinnerWebWorld
CLIENT_FUNCTION = None
