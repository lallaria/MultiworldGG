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

class Keysanity(Toggle):
    """Puts Keys into the item pool. Regardless of the setting, keys can only be used in their respective dungeon."""
    display_name = "Keysanity"

@dataclass
class Z2Options(PerGameCommonOptions):
    required_crystals: RequiredCrystals
    early_candle: EarlyCandle
    candle_required: RequireCandle
    keysanity: Keysanity
    random_tunic_color: RandomTunicColor


z2_option_groups = [
    OptionGroup("Game Settings", [
        RequiredCrystals,
        RequireCandle
    ]),

    OptionGroup("Item Settings", [
        EarlyCandle,
        Keysanity
    ]),

    OptionGroup("Cosmetic Settings", [
        RandomTunicColor
    ]),
]
