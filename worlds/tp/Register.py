from . import TPWorld, TPWeb, run_client

"""
Join Link and Midna on their adventure through Hyrule in Twilight Princess. World Registration

This file contains the metadata and class references for the tp world.
"""

# Required metadata
WORLD_NAME = "tp"
GAME_NAME = "The Legend of Zelda: Twilight Princess"
IGDB_ID = 134014
AUTHOR = "WritingHusky"
VERSION = "0.3.0"

# Plugin entry points
WORLD_CLASS = TPWorld
WEB_WORLD_CLASS = TPWeb
CLIENT_FUNCTION = run_client
