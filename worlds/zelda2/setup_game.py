import struct


def setup_gamevars(world):
    if world.options.early_candle:
        world.multiworld.local_early_items[world.player]["Candle"] = 1


def place_static_items(world):
    world.get_location("Dark Link").place_locked_item(world.create_item("Triforce of Courage"))
