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
class EBOptions(PerGameCommonOptions):
    required_crystals: RequiredCrystals
    random_tunic_color: RandomTunicColor


eb_option_groups = [
    OptionGroup("Goal Settings", [
        GiygasRequired,
        SanctuariesRequired,
        SanctuaryAltGoal
    ]),
    
    OptionGroup("Item Settings", [
        TeleportShuffle,
        CharacterShuffle,
        ProgressiveWeapons,
        ProgressiveArmor,
        RandomFranklinBadge,
        CommonWeight,
        UncommonWeight,
        RareWeight,
        PreFixItems
    ]),

    OptionGroup("Equipamizer", [
        Armorizer,
        Weaponizer,
        ElementChance,
        EquipamizerStatCap
    ]),

    OptionGroup("World Modes", [
        RandomStartLocation,
        MagicantMode,
        MonkeyCavesMode,
        NoFreeSancs,
        StartingCharacter
    ]),

    OptionGroup("PSI Randomization", [
        PSIShuffle,
        BanFlashFavorite
    ]),

    OptionGroup("Enemy Randomization", [
        BossShuffle,
        DecoupleDiamondDog,
        ShuffleGiygas,
        ExperienceModifier,
        ShuffleDrops,
        MoneyDropMultiplier
    ]),

    OptionGroup("Shop Randomization", [
        ShopRandomizer,
        ScoutShopChecks
    ]),

    OptionGroup("Convenience Settings", [
        ShortenPrayers,
        EasyDeaths,
        StartingMoney,
        RemoteItems,
        AutoscaleParty
    ]),

    OptionGroup("Aesthetic Settings", [
        RandomFlavors,
        RandomSwirlColors,
        RandomBattleBG,
        PresentSprites,
        RandomizePSIPalettes,
        PlandoLumineHallText
    ]),

    OptionGroup("Music Randomizer", [
        RandomizeOverworldMusic,
        RandomizeBattleMusic,
        RandomizeFanfares
    ]),

    OptionGroup("Deathlink", [
        DeathLink,
        DeathLinkMode
    ])
]
