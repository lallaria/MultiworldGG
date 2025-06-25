from . import MkddWorld, MkddWebWorld

"""
Mario Kart Double Dash World Registration

This file contains the metadata and class references for the mario_kart_double_dash world.
"""

# Required metadata
WORLD_NAME = "mario_kart_double_dash"
GAME_NAME = "Mario Kart Double Dash"
IGDB_ID = 0
AUTHOR = "aXu"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = MkddWorld
WEB_WORLD_CLASS = MkddWebWorld
CLIENT_FUNCTION = None
