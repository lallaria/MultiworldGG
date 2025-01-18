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

@dataclass
class Z2Options(PerGameCommonOptions):
    required_crystals: RequiredCrystals
    random_tunic_color: RandomTunicColor


z2_option_groups = [
    OptionGroup("Game Settings", [
        RequiredCrystals
    ]),

    OptionGroup("Cosmetic Settings", [
        RandomTunicColor
    ])
]
