from . import DiddyKongRacingWorld, DiddyKongRacingWeb
from .DKRClient import main

"""
Diddy Kong Racing World Registration

This file contains the metadata and class references for the diddy_kong_racing world.
"""

# Required metadata
WORLD_NAME = "diddy_kong_racing"
GAME_NAME = "Diddy Kong Racing"
IGDB_ID = 2723
AUTHOR = "zakwiz"
VERSION = "0.6.1"

# Plugin entry points
WORLD_CLASS = DiddyKongRacingWorld
WEB_WORLD_CLASS = DiddyKongRacingWeb
CLIENT_FUNCTION = main
