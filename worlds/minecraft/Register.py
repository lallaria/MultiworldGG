from . import MinecraftWorld, MinecraftWebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Minecraft World Registration

This file contains the metadata and class references for the minecraft world.
"""

# Required metadata
WORLD_NAME = "minecraft"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = MinecraftWorld
WEB_WORLD_CLASS = MinecraftWebWorld
CLIENT_FUNCTION = None
