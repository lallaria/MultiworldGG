from BaseClasses import Item, ItemClassification
from typing import Dict

from .Locations import raw_location_dict
from .Options import PowerwashSimulatorOptions

class PowerwashSimulatorItem(Item):
    game = "Powerwash Simulator"

unlock_items = [f"{location} Unlock" for location in raw_location_dict]
progression_items = unlock_items + ["A Job Well Done"]
filler_items = ["Dirt", "Grime", "Satisfaction", "Water", "Sponge", "Bubblegum Flavored Soap", "H2O", "Positive Reviews", "C17H35COONa"]

item_table: Dict[str, ItemClassification] = {
    **{item: ItemClassification.progression for item in progression_items},
    **{item: ItemClassification.filler for item in filler_items}
}

raw_items = progression_items + filler_items

def create_items(world):
    options: PowerwashSimulatorOptions = world.options
    pool = world.multiworld.itempool

    for location in options.get_locations():
        if location == world.starting_location: continue
        pool.append(world.create_item(f"{location} Unlock"))

    for _ in range(world.item_steps["total mcguffins"]):
        pool.append(world.create_item("A Job Well Done"))

    for _ in range(world.item_steps["total"] - world.item_steps["filler"] - world.item_steps["total progression"]):
        pool.append(world.create_item(world.random.choice(filler_items)))