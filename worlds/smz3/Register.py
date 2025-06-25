from . import SMZ3World
from . import SMZ3Web

"""
SMZ3 World Registration

This file contains the metadata and class references for the smz3 world.
"""

# Required metadata
WORLD_NAME = "smz3"
GAME_NAME = "SMZ3"
IGDB_ID = 0
AUTHOR = "lordlou"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = SMZ3World
WEB_WORLD_CLASS = SMZ3Web
CLIENT_FUNCTION = None
