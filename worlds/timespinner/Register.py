from . import TimespinnerWebWorld, TimespinnerWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Timespinner World Registration

This file contains the metadata and class references for the timespinner world.
"""

# Required metadata
WORLD_NAME = "timespinner"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = TimespinnerWorld
WEB_WORLD_CLASS = TimespinnerWebWorld
CLIENT_FUNCTION = None
