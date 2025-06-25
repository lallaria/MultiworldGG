from . import SA2BWorld
from . import SA2BWeb

"""
Sonic Adventure 2 Battle is an action platforming game. Play as Sonic, Tails, Knuckles, Shadow, Rouge, and Eggman across 31 stages and prevent the destruction of the earth. World Registration

This file contains the metadata and class references for the sa2b world.
"""

# Required metadata
WORLD_NAME = "sa2b"
GAME_NAME = "Sonic Adventure 2 Battle is an action platforming game. Play as Sonic, Tails, Knuckles, Shadow, Rouge, and Eggman across 31 stages and prevent the destruction of the earth."
IGDB_ID = 192194
AUTHOR = "PoryGone & RaspberrySpace"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = SA2BWorld
WEB_WORLD_CLASS = SA2BWeb
CLIENT_FUNCTION = None
