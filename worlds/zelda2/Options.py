from dataclasses import dataclass
from Options import (Toggle, DefaultOnToggle, Choice, Range, PerGameCommonOptions, StartInventoryPool,
                     OptionGroup, FreeText, Visibility)


class RequiredCrystals(Range):
    """How many Crystals need to be set in Palaces in order
       to unlock the Great Palace"""
    display_name = "Required Crystals"
    range_start = 0
    range_end = 6
    default = 6

class RandomTunicColor(Toggle):
    """Randomizes Link's normal and Shield tunic color."""
    display_name = "Random Tunic Color"

class EarlyCandle(Toggle):
    """Ensures that the Candle will be accessible early on."""
    display_name = "Early Candle"

class RequireCandle(DefaultOnToggle):
    """If enabled, you will be logically expected to have the Candle before going inton any caves.
       This does not include the Parapa cave, as the original game expects you to traverse this cave
       in the dark."""
    display_name = "Candle Logic"

class RequireCross(DefaultOnToggle):
    """If enabled, you will be logically expected to have the Cross before going to Old Kasuto
       or Death Valley."""
    display_name = "Cross Logic"

class Keysanity(Toggle):
    """Puts Keys into the item pool. Regardless of the setting, keys can only be used in their respective dungeon."""
    display_name = "Keysanity"

class RemoveEarlyBoulder(Toggle):
    """Removes the boulder blocking the south part of the western continent."""
    display_name = "Remove Early Boulder"

class StartingLife(Range):
    """What your starting Life level is."""
    display_name = "Starting Life Level"
    range_start = 1
    range_end = 8
    default = 2

class StartingAttack(Range):
    """What your starting Attack level is."""
    display_name = "Starting Attack Level"
    range_start = 1
    range_end = 8
    default = 2

class StartingMagic(Range):
    """What your starting Magic level is."""
    display_name = "Starting Magic Level"
    range_start = 1
    range_end = 8
    default = 2

class RandomPalaceGraphics(Toggle):
    """Randomizes the color and tiles of each Palace except the Great Palace."""
    display_name = "Random Palace Graphics"

class PalaceRespawn(DefaultOnToggle):
    """If enabled, you will respawn at the current Palace entrance if you game over,
       but not if you save and reset. If disabled, this only applies to the Great Palace."""
    display_name = "Respawn at Palaces"

class StartingLives(Range):
    """How many lives you will start with upon loading the game.
       This value will be permanently increased by one every time you find a
       1-Up Doll."""
    display_name = "Starting Lives"
    range_start = 0
    range_end = 255
    default = 3

class KeepExp(DefaultOnToggle):
    """If enabled, you will retain your EXP after game over, and it will be saved to your file."""
    display_name = "Keep EXP"

@dataclass
class Z2Options(PerGameCommonOptions):
    required_crystals: RequiredCrystals
    early_candle: EarlyCandle
    candle_required: RequireCandle
    cross_required: RequireCross
    remove_early_boulder: RemoveEarlyBoulder
    palace_respawn: PalaceRespawn
    starting_life: StartingLife
    starting_magic: StartingMagic
    starting_attack: StartingAttack
    starting_lives: StartingLives
    keep_exp: KeepExp
    keysanity: Keysanity
    random_tunic_color: RandomTunicColor
    random_palace_graphics: RandomPalaceGraphics


z2_option_groups = [
    OptionGroup("Game Settings", [
        RequiredCrystals
    ]),

    OptionGroup("Item Settings", [
        EarlyCandle,
        Keysanity
    ]),

    OptionGroup("Logic Settings", [
        RequireCandle,
        RequireCross,
        RemoveEarlyBoulder
    ]),

    OptionGroup("Convenience Settings", [
        PalaceRespawn,
        StartingLives,
        KeepExp
    ]),

    OptionGroup("Starting Stats", [
        StartingAttack,
        StartingMagic,
        StartingLife
    ]),

    OptionGroup("Cosmetic Settings", [
        RandomTunicColor,
        RandomPalaceGraphics
    ]),
]
