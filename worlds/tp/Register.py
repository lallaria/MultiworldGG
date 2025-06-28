from . import TPWorld, TPWeb, run_client
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Join Link and Midna on their adventure through Hyrule in Twilight Princess. World Registration

This file contains the metadata and class references for the tp world.
"""

# Required metadata
WORLD_NAME = "tp"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = TPWorld
WEB_WORLD_CLASS = TPWeb
CLIENT_FUNCTION = run_client
