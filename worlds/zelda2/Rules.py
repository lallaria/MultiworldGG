from worlds.generic.Rules import set_rule, add_rule
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import Z2World


def set_location_rules(world: "Z2World") -> None:
    player = world.player
    twoson_paula_room_present = world.get_location("Twoson - Paula's Room Present")
    can_buy_pizza = world.get_location("Threed - Downtown Trashcan")

    set_rule(world.multiworld.get_location("Onett - Traveling Entertainer", player), lambda state: state.has("Key to the Shack", player))

def set_region_rules(world: "Z2World") -> None:
    print("NOT DONE YET")