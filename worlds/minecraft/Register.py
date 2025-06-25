from . import MinecraftWorld, MinecraftWebWorld

"""
Minecraft World Registration

This file contains the metadata and class references for the minecraft world.
"""

# Required metadata
WORLD_NAME = "minecraft"
GAME_NAME = "Minecraft"
IGDB_ID = 121
AUTHOR = "KonoTyran & espeon"
VERSION = "9"

# Plugin entry points
WORLD_CLASS = MinecraftWorld
WEB_WORLD_CLASS = MinecraftWebWorld
CLIENT_FUNCTION = None
