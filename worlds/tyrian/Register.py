from . import TyrianWebWorld, TyrianWorld

"""
Tyrian World Registration

This file contains the metadata and class references for the tyrian world.
"""

# Required metadata
WORLD_NAME = "tyrian"
GAME_NAME = "Tyrian"
IGDB_ID = 14432
AUTHOR = "Kaito Sinclaire"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = TyrianWorld
WEB_WORLD_CLASS = TyrianWebWorld
CLIENT_FUNCTION = None
