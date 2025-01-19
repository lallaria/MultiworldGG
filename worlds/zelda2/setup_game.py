import struct


def setup_gamevars(world):
    if world.options.early_candle:
        world.multiworld.local_early_items[world.player]["Candle"] = 1


def place_static_items(world):
    world.get_location("Parapa Palace: Statue").place_locked_item(world.create_item("Crystal Returned"))
    world.get_location("Midoro Palace: Statue").place_locked_item(world.create_item("Crystal Returned"))
    world.get_location("Island Palace: Statue").place_locked_item(world.create_item("Crystal Returned"))
    world.get_location("Maze Palace: Statue").place_locked_item(world.create_item("Crystal Returned"))
    world.get_location("Palace on the Sea: Statue").place_locked_item(world.create_item("Crystal Returned"))
    world.get_location("Three-Eye Rock Palace: Statue").place_locked_item(world.create_item("Crystal Returned"))
    world.get_location("Dark Link").place_locked_item(world.create_item("Triforce of Courage"))
