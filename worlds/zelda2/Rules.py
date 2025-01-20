from worlds.generic.Rules import set_rule, add_rule
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import Z2World

def apply_location_rules(world, target, rule):
    add_rule(world.multiworld.get_location(target, world.player), rule)

def apply_region_rules(world, target, rule):
    add_rule(world.multiworld.get_entrance(target, world.player), rule)

def set_location_rules(world: "Z2World") -> None:
    can_get_high = lambda state: state.has_any({"Jump Spell", "Fairy Spell"}, world.player)

    if world.options.candle_required:
        apply_location_rules(world, "Northern Desert Cave", lambda state: state.has("Candle", world.player))
        apply_location_rules(world, "North Castle Cave", lambda state: state.has("Candle", world.player))
        apply_location_rules(world, "Western Swamp Cave", lambda state: state.has("Candle", world.player))
        apply_location_rules(world, "Clear Cave South of Rauru", lambda state: state.has("Candle", world.player))
        apply_location_rules(world, "Blocked Cave South of Rauru", lambda state: state.has("Candle", world.player))
        apply_location_rules(world, "Death Mountain Platforms", lambda state: state.has("Candle", world.player))
        apply_location_rules(world, "Death Mountain Staircase", lambda state: state.has("Candle", world.player))
        apply_location_rules(world, "Death Mountain Boulder Pit", lambda state: state.has("Candle", world.player))
        apply_location_rules(world, "Death Mountain Ending Item", lambda state: state.has("Candle", world.player))
        apply_location_rules(world, "Death Mountain East-Facing Dead End", lambda state: state.has("Candle", world.player))

    apply_location_rules(world, "Sage of Ruto", lambda state: state.has("Trophy", world.player))

    apply_location_rules(world, "Parapa Palace: Pedestal Item", lambda state: state.has("Parapa Palace Key", world.player, 3) or state.has("Magical Key", world.player))
    apply_location_rules(world, "Parapa Palace: Crumbling Bridge", lambda state: state.has("Parapa Palace Key", world.player) or state.has("Magical Key", world.player))
    apply_location_rules(world, "Parapa Palace: Stairwell", lambda state: state.has("Parapa Palace Key", world.player) or state.has("Magical Key", world.player))
    apply_location_rules(world, "Parapa Palace: Guarded Item", lambda state: state.has("Parapa Palace Key", world.player) or state.has("Magical Key", world.player))
    apply_location_rules(world, "Parapa Palace: Horsehead Drop", lambda state: state.has("Parapa Palace Key", world.player, 3) or state.has("Magical Key", world.player))
    apply_location_rules(world, "Parapa Palace: Statue", lambda state: state.has("Parapa Palace Key", world.player, 3) or state.has("Magical Key", world.player))

    apply_location_rules(world, "Western Swamp Cave", lambda state: state.has("Hammer", world.player))
    apply_location_rules(world, "Blocked Cave South of Rauru", lambda state: state.has("Hammer", world.player))

    apply_location_rules(world, "Midoro Palace: Lava Blocks Item", lambda state: state.has("Midoro Palace Key", world.player) or state.has("Magical Key", world.player))
    apply_location_rules(world, "Midoro Palace: Falling Blocks Item", lambda state: state.has("Midoro Palace Key", world.player, 3) or state.has("Magical Key", world.player))
    apply_location_rules(world, "Midoro Palace: Pedestal Item", lambda state: state.has("Midoro Palace Key", world.player, 4) or state.has("Magical Key", world.player))
    apply_location_rules(world, "Midoro Palace: Guarded Item", lambda state: (state.has("Midoro Palace Key", world.player) or state.has("Magical Key", world.player)) and state.has("Handy Glove", world.player))
    apply_location_rules(world, "Midoro Palace: Crumbling Blocks", lambda state: (state.has("Midoro Palace Key", world.player) or state.has("Magical Key", world.player)) and state.has("Handy Glove", world.player))
    apply_location_rules(world, "Midoro Palace: Helmethead Drop", lambda state: (state.has("Midoro Palace Key", world.player, 3) or state.has("Magical Key", world.player)) and state.has("Handy Glove", world.player))
    apply_location_rules(world, "Midoro Palace: Statue", lambda state: (state.has("Midoro Palace Key", world.player, 3) or state.has("Magical Key", world.player)) and state.has("Handy Glove", world.player))

    apply_location_rules(world, "Death Mountain Boulder Pit", lambda state: state.has("Hammer", world.player))
    apply_location_rules(world, "Death Mountain Platforms", can_get_high)

    apply_location_rules(world, "Sage of Mido", lambda state: state.has("Water of Life", world.player))
    apply_location_rules(world, "Mido Swordsman", can_get_high)

    apply_location_rules(world, "Island Palace: Buried Item Left", lambda state: state.has_all({"Handy Glove", "Down Thrust"}, world.player))
    apply_location_rules(world, "Island Palace: Buried Item Right", lambda state: state.has_all({"Handy Glove", "Down Thrust"}, world.player))
    apply_location_rules(world, "Island Palace: Precarious Item", lambda state: (state.has("Island Palace Key", world.player, 3) or state.has("Magical Key", world.player)) and state.has("Handy Glove", world.player))
    apply_location_rules(world, "Island Palace: Pedestal Item", lambda state: (state.has("Island Palace Key", world.player, 4) or state.has("Magical Key", world.player)) and state.has("Handy Glove", world.player))
    apply_location_rules(world, "Island Palace: Block Mountain", lambda state: (state.has("Island Palace Key", world.player, 3) or state.has("Magical Key", world.player)) and state.has("Handy Glove", world.player))
    apply_location_rules(world, "Island Palace: Pillar Item", lambda state:(state.has("Island Palace Key", world.player, 4) or state.has("Magical Key", world.player)) and state.has_all({"Handy Glove", "Down Thrust"}, world.player))
    apply_location_rules(world, "Island Palace: Guarded by Iron Knuckles", lambda state:(state.has("Island Palace Key", world.player, 4) or state.has("Magical Key", world.player)) and state.has_all({"Handy Glove", "Down Thrust"}, world.player))
    apply_location_rules(world, "Island Palace: Rebonack Drop", lambda state:(state.has("Island Palace Key", world.player, 4) or state.has("Magical Key", world.player)) and state.has_all({"Handy Glove", "Down Thrust"}, world.player))
    

def set_region_rules(world: "Z2World") -> None:
    if world.options.candle_required:
        print("A!")
