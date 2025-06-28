from . import UndertaleWorld, UndertaleWeb, run_client
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Undertale World Registration

This file contains the metadata and class references for the undertale world.
"""

# Required metadata
WORLD_NAME = "undertale"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = UndertaleWorld
WEB_WORLD_CLASS = UndertaleWeb
CLIENT_FUNCTION = run_client
