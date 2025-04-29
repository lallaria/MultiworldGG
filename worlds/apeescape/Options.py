from __future__ import annotations

from dataclasses import dataclass
from Options import Choice, Range, DeathLink, PerGameCommonOptions


class GoalOption(Choice):
    """Choose the victory condition for this world.

        mm: First Specter fight in Monkey Madness, with the vanilla condition (just get there).
        ppm: Second Specter fight in Peak Point Matrix, with the vanilla condition (catch all monkeys). Peak Point Matrix will only have the vanilla entry condition for Specter 1 and Specter 2 goals.
        tokenhunt: Collecting enough Specter Token items throughout the world.
        mmtoken: First Specter fight in Monkey Madness, after collecting enough Specter Token items.
        ppmtoken: Second Specter fight in Peak Point Matrix, after collecting enough Specter Token items.

        Supported values: mm, ppm, tokenhunt, mmtoken, ppmtoken
        Default value: first
    """

    display_name = "Goal"
    option_mm = 0x00
    option_ppm = 0x01
    option_tokenhunt = 0x02
    option_mmtoken = 0x03
    option_ppmtoken = 0x04
    default = option_mm


class RequiredTokensOption(Range):
    """Choose the required number of Specter Tokens for goal.

        Supported values: 5 - 60
        Default value: 20
    """

    display_name = "Required Tokens"
    range_start = 5
    range_end = 60
    default = 20


class TotalTokensOption(Range):
    """Choose the total number of Specter Tokens in the item pool.
        If a world requests a token requirement greater than the number of tokens created, then the total and required values will be swapped.

        Supported values: 5 - 60
        Default value: 30
    """

    display_name = "Total Tokens"
    range_start = 5
    range_end = 60
    default = 30


class TokenLocationsOption(Choice):
    """Choose where Specter Tokens can be placed in the multiworld.

        anywhere: Specter Tokens can be placed anywhere in the multiworld.
        ownworld: Specter Tokens can only be placed in your world.

        Supported values: anywhere, ownworld
        Default value: ownworld
    """

    display_name = "Token Locations"
    option_anywhere = 0x00
    option_ownworld = 0x01
    default = option_ownworld


class LogicOption(Choice):
    """Choose expected trick knowledge.

        normal: No advanced movement tech or out of bounds required, and hard monkeys will guarantee a helpful gadget. Some additional difficult or precise jumps won't be required either. May still require some out of the box thinking or non-standard routes. Suitable for casual players.
        hard: Movement tech can be required in places with a low penalty for failing. Suitable for players with speedrun knowledge.
        expert: All tricks and glitches can be required, and some monkeys may require resetting the room if not caught in a certain way. Can also require obscure game knowledge. Suitable for those seeking the ultimate challenge.

        Supported values: normal, hard, expert
        Default value: normal
    """

    display_name = "Logic"
    option_normal = 0x00
    option_hard = 0x01
    option_expert = 0x02
    default = option_normal


class InfiniteJumpOption(Choice):
    """Choose if the Infinite Jump trick should be put into logic.

        false: Infinite Jump is not put into logic.
        true: Infinite Jump is put into logic.

        Supported values: false, true
        Default value: false
    """
    display_name = "Infinite Jump"
    option_false = 0x00
    option_true = 0x01
    default = option_false


class SuperFlyerOption(Choice):
    """Choose if the Super Flyer trick should be put into logic.

        false: Super Flyer is not put into logic.
        true: Super Flyer is put into logic.

        Supported values: false, true
        Default value: false
    """
    display_name = "Super Flyer"
    option_false = 0x00
    option_true = 0x01
    default = option_false


class EntranceOption(Choice):
    """Choose which level entrances should be randomized. Peak Point Matrix will always be the last level. Races will be included in randomization if coin shuffle is on, and excluded otherwise.

        off: Levels will be in the vanilla order.
        on: Levels will be in a random order.
        lockmm: Levels will be in a random order, and Monkey Madness will be locked to its original entranxe.

        Supported values: off, on, lockmm
        Default value: on
    """

    display_name = "Entrance"
    option_off = 0x00
    option_on = 0x01
    option_lockmm = 0x02
    default = option_off


class KeyOption(Choice):
    """Choose how many levels each World Key should unlock. The first three levels will always start unlocked.
        Races will be skipped if coin shuffle is off. Peak Point Matrix will require the same number of keys as the Monkey Madness entrance on a boss goal, and one additional key on a token hunt or token boss goal.

        world: Each World Key unlocks the 1 or 3 levels in the next world. Creates between 6 and 9 World Keys.
        level: Each World Key unlocks the next level. Creates between 16 and 19 World Keys.
        twolevels: Each World Key unlocks the next two levels. Creates between 8 and 10 World Keys.
        none: All levels are open from the beginning of the game.

        Supported values: world, level, twolevels, none
        Default value: world
    """

    display_name = "Unlocks per Key"
    option_world = 0x00
    option_level = 0x01
    option_twolevels = 0x02
    option_none = 0x03
    default = option_world


class ExtraKeysOption(Range):
    """Choose the number of extra World Keys that should be created.

        Supported values: 0 - 10
        Default value: 0
    """

    display_name = "Extra Keys"
    range_start = 0
    range_end = 10
    default = 0


class CoinOption(Choice):
    """Choose if Specter Coins should be added as locations.

        false: Specter Coins are not locations.
        true: The 60 Specter Coins are added as locations.

        Supported values: false, true
        Default value: false
    """

    display_name = "Coin"
    option_false = 0x00
    option_true = 0x01
    default = option_false


class MailboxOption(Choice):
    """Choose if mailboxes should act as locations.
        Mailboxes in training rooms will never be locations.

        false: Mailboxes are not locations.
        true: The 63 available mailboxes are added as locations.

        Supported values: false, true
        Default value: false
    """

    display_name = "Mailbox"
    option_false = 0x00
    option_true = 0x01
    default = option_false


class LampOption(Choice):
    """Choose if Monkey Lamps should be locked and shuffled into the multiworld.

        false: Monkey Lamps will act in vanilla (catch enough monkeys in their level to open the door)
        true: The 8 Monkey Lamps will be items in the multiworld, that open their respective door when received.

        Supported values: false, true
        Default value: false
    """

    display_name = "Monkey Lamps"
    option_false = 0x00
    option_true = 0x01
    default = option_false


class GadgetOption(Choice):
    """Choose a starting gadget aside from the Time Net.

        club: Start with the Stun Club.
        radar: Start with the Monkey Radar.
        sling: Start with the Slingback Shooter.
        hoop: Start with the Super Hoop.
        flyer: Start with the Sky Flyer.
        car: Start with the RC Car.
        punch: Start with the Magic Punch.
        waternet: Start with the Water Net.
        none: Start with no additional gadgets.

        Supported values: club, radar, sling, hoop, flyer, car, punch, waternet, none
        Default value: club
    """

    display_name = "Gadget"
    option_club = 0x00
    option_radar = 0x01
    option_sling = 0x02
    option_hoop = 0x03
    option_flyer = 0x04
    option_car = 0x05
    option_punch = 0x06
    option_waternet = 0x07
    option_none = 0x08
    default = option_club


class ShuffleNetOption(Choice):
    """Choose if the Time Net should be shuffled.
        This option requires at least one of coins and mailboxes to be shuffled to be used - if all locations in this world require the net, the net will be given at game start.

        false: Time Net is not shuffled, and is given at game start.
        true: Time Net is shuffled into the pool. The mailboxes in the Time Station will also be locations if this happens.

        Supported values: false, true
        Default value: false
    """
    display_name = "Shuffle Net"
    option_false = 0x00
    option_true = 0x01
    default = option_false


class ShuffleWaterNetOption(Choice):
    """Choose if the Water Net should be shuffled.

        off: Water Net is not shuffled, and is given at game start.
        progressive: Water Net is shuffled and split into parts, adding two Progressive Water Nets and Water Catch to the pool.
        - Progressive Water Net : The first allows Spike to swim on the surface and avoid drowning after a few seconds. The second allows Spike to dive underwater.
        - Water Catch: Allows shooting the Water Net.
        on: Water Net is shuffled, adding it to the pool as a single item.

        Supported values: off, progressive, on
        Default value: off
    """
    display_name = "Shuffle Water Net"
    option_off = 0x00
    option_progressive = 0x01
    option_on = 0x02
    default = option_off


class LowOxygenSounds(Choice):
    """Choose how quickly the low oxygen beep sound effect will play when underwater.

        off: Low Oxygen sounds will not play at all.
        half: Low Oxygen sounds will play less frequently.
        on: Low Oxygen Sounds will play normally.

        Supported values: off, half, on
        Default value: half
    """
    display_name = "Low Oxygen Sounds"
    option_off = 0x00
    option_half = 0x01
    option_on = 0x02
    default = option_half


class TrapFillPercentage(Range):
    """
    Replace a percentage of filler items in the item pool with random traps.
    """
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 0


class ItemDisplayOption(Choice):
    """Set the default for the Bizhawk item display command. This can be changed in the client at any time. The position and duration of these messages can be changed in Bizhawk config at any time.

        off: Receiving an item will not show a message in Bizhawk.
        on: Receiving an item will show a message in Bizhawk.

        Supported values: off, true
        Default value: on
    """
    display_name = "Item Display"
    option_off = 0x00
    option_on = 0x01
    default = option_on


@dataclass
class ApeEscapeOptions(PerGameCommonOptions):
    goal: GoalOption
    requiredtokens: RequiredTokensOption
    totaltokens: TotalTokensOption
    tokenlocations: TokenLocationsOption
    logic: LogicOption
    infinitejump: InfiniteJumpOption
    superflyer: SuperFlyerOption
    entrance: EntranceOption
    unlocksperkey: KeyOption
    extrakeys: ExtraKeysOption
    coin: CoinOption
    mailbox: MailboxOption
    lamp: LampOption
    gadget: GadgetOption
    shufflenet: ShuffleNetOption
    shufflewaternet: ShuffleWaterNetOption
    lowoxygensounds: LowOxygenSounds
    trapfillpercentage: TrapFillPercentage
    itemdisplay: ItemDisplayOption
    death_link: DeathLink
