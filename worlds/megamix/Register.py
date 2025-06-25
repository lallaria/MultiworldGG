from . import MegaMixWorld
from . import MegaMixWeb

"""
Hatsune Miku Project Diva Mega Mix+ World Registration

This file contains the metadata and class references for the megamix world.
"""

# Required metadata
WORLD_NAME = "megamix"
GAME_NAME = "Hatsune Miku Project Diva Mega Mix+"
IGDB_ID = 120278
AUTHOR = "Cynichill"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = MegaMixWorld
WEB_WORLD_CLASS = MegaMixWeb
CLIENT_FUNCTION = None
