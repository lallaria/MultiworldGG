from typing import List


class DeepWoodsItem:
    pendant_community = "Pendant of Community"
    pendant_elder = "Pendant of Elders"
    pendant_depths = "Pendant of Depths"
    obelisk_sigil = "Progressive Woods Obelisk Sigils"


class SkillLevel:
    cooking = "Cooking Level"
    binning = "Binning Level"
    magic = "Magic Level"
    socializing = "Socializing Level"
    luck = "Luck Level"
    archaeology = "Archaeology Level"


class SVEQuestItem:
    aurora_vineyard_tablet = "Aurora Vineyard Tablet"
    """Triggers the apparition of the bundle tablet in the Aurora Vineyard, so you can do the Aurora Vineyard quest.
    This aim to break dependencies on completing the Community Center.
    """
    aurora_vineyard_reclamation = "Aurora Vineyard Reclamation"
    """Triggers the unlock of the Aurora Vineyard basement, so you can meet Apples.
    """
    iridium_bomb = "Iridium Bomb"
    void_soul = "Void Spirit Peace Agreement"
    kittyfish_spell = "Kittyfish Spell"
    scarlett_job_offer = "Scarlett's Job Offer"
    morgan_schooling = "Morgan's Schooling"
    diamond_wand = "Diamond Wand"
    marlon_boat_paddle = "Marlon's Boat Paddle"
    fable_reef_portal = "Fable Reef Portal"
    grandpa_shed = "Grandpa's Shed"

    sve_always_quest_items: list[str] = [kittyfish_spell, scarlett_job_offer, morgan_schooling, aurora_vineyard_tablet, ]
    sve_always_quest_items_ginger_island: list[str] = [fable_reef_portal, ]
    sve_quest_items: list[str] = [iridium_bomb, void_soul, grandpa_shed, aurora_vineyard_reclamation, ]
    sve_quest_items_ginger_island: list[str] = [marlon_boat_paddle, ]


class SVELocation:
    tempered_galaxy_sword = "Tempered Galaxy Sword"
    tempered_galaxy_hammer = "Tempered Galaxy Hammer"
    tempered_galaxy_dagger = "Tempered Galaxy Dagger"
    diamond_wand = "Lance's Diamond Wand"
    monster_crops = "Monster Crops"


class SVERunes:
    nexus_guild = "Nexus: Adventurer's Guild Runes"
    nexus_junimo = "Nexus: Junimo Woods Runes"
    nexus_outpost = "Nexus: Outpost Runes"
    nexus_aurora = "Nexus: Aurora Vineyard Runes"
    nexus_spring = "Nexus: Sprite Spring Runes"
    nexus_farm = "Nexus: Farm Runes"
    nexus_wizard = "Nexus: Wizard Runes"

    nexus_items: List[str] = [nexus_farm, nexus_wizard, nexus_spring, nexus_aurora, nexus_guild, nexus_junimo, nexus_outpost]

class ModBooks:
    digging_like_worms = "Digging Like Worms"