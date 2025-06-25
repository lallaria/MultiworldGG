from . import UndertaleWorld, UndertaleWeb, run_client

"""
Undertale World Registration

This file contains the metadata and class references for the undertale world.
"""

# Required metadata
WORLD_NAME = "undertale"
GAME_NAME = "Undertale"
IGDB_ID = 12517
AUTHOR = "jonloveslegos"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = UndertaleWorld
WEB_WORLD_CLASS = UndertaleWeb
CLIENT_FUNCTION = run_client
