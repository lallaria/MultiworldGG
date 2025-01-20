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


def add_keys(world):
    if world.options.keysanity:
        for i in range(3):
            world.multiworld.itempool.append(world.create_item("Parapa Palace Key"))

        for i in range(4):
            world.multiworld.itempool.append(world.create_item("Midoro Palace Key"))

        for i in range(4):
            world.multiworld.itempool.append(world.create_item("Island Palace Key"))

        for i in range(6):
            world.multiworld.itempool.append(world.create_item("Maze Palace Key"))

        for i in range(5):
            world.multiworld.itempool.append(world.create_item("Sea Palace Key"))

        for i in range(2):
            world.multiworld.itempool.append(world.create_item("Three-Eye Rock Palace Key"))
        world.extra_count = 24