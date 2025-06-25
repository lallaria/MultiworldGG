from . import KH1World
from . import KH1Web

"""
Kingdom Hearts World Registration

This file contains the metadata and class references for the kh1 world.
"""

# Required metadata
WORLD_NAME = "kh1"
GAME_NAME = "Kingdom Hearts"
IGDB_ID = 1219
AUTHOR = "gaithern"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = KH1World
WEB_WORLD_CLASS = KH1Web
CLIENT_FUNCTION = None
