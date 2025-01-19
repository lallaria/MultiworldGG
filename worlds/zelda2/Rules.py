from worlds.generic.Rules import set_rule, add_rule
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import Z2World

def apply_location_rules(world, target, rule):
    add_rule(world.multiworld.get_location(target, world.player), rule)

def apply_region_rules(world, target, rule):
    add_rule(world.multiworld.get_entrance(target, world.player), rule)

def set_location_rules(world: "Z2World") -> None:
    if world.options.candle_required:
        apply_location_rules(world, "Northern Desert Cave", lambda state: state.has("Candle", world.player))
        apply_location_rules(world, "North Castle Cave", lambda state: state.has("Candle", world.player))

def set_region_rules(world: "Z2World") -> None:
    if world.options.candle_required:
        print("A!")