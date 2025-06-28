from . import InscryptionWorld, InscrypWeb
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Inscryption World Registration

This file contains the metadata and class references for the inscryption world.
"""

# Required metadata
WORLD_NAME = "inscryption"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = InscryptionWorld
WEB_WORLD_CLASS = InscrypWeb
CLIENT_FUNCTION = None
