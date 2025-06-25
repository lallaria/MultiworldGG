from . import CliqueWebWorld, CliqueWorld

"""
Clique World Registration

This file contains the metadata and class references for the clique world.
"""

# Required metadata
WORLD_NAME = "clique"
GAME_NAME = "Clique"
IGDB_ID = 0
AUTHOR = "Phar"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = CliqueWorld
WEB_WORLD_CLASS = CliqueWebWorld
CLIENT_FUNCTION = None
