from . import FFTAWebWorld

"""
Final Fantasy Tactics Advance World Registration

This file contains the metadata and class references for the ffta world.
"""

# Required metadata
WORLD_NAME = "ffta"
GAME_NAME = "Final Fantasy Tactics Advance"
IGDB_ID = 414
AUTHOR = "spicynun"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = FFTAWebWorld
WEB_WORLD_CLASS = None
CLIENT_FUNCTION = None
