from . import InscryptionWorld, InscrypWeb

"""
Inscryption World Registration

This file contains the metadata and class references for the inscryption world.
"""

# Required metadata
WORLD_NAME = "inscryption"
GAME_NAME = "Inscryption"
IGDB_ID = 139090
AUTHOR = "DrBibop"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = InscryptionWorld
WEB_WORLD_CLASS = InscrypWeb
CLIENT_FUNCTION = None
