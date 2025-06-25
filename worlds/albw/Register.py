from . import ALBWWebWorld, ALBWWorld

"""
File name of your decrypted North American A Link Between Worlds ROM World Registration

This file contains the metadata and class references for the albw world.
"""

# Required metadata
WORLD_NAME = "albw"
GAME_NAME = "A Link Between Worlds"
IGDB_ID = 2909
AUTHOR = "randomsalience"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = ALBWWorld
WEB_WORLD_CLASS = ALBWWebWorld
CLIENT_FUNCTION = None
