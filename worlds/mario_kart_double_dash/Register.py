from . import MkddWorld, MkddWebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Mario Kart Double Dash World Registration

This file contains the metadata and class references for the mario_kart_double_dash world.
"""

# Required metadata
WORLD_NAME = "mario_kart_double_dash"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = MkddWorld
WEB_WORLD_CLASS = MkddWebWorld
CLIENT_FUNCTION = None
