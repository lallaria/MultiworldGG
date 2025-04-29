from dataclasses import dataclass
from Options import Toggle, PerGameCommonOptions, DeathLink, TextChoice


class ProgressiveKeys(Toggle):
    """Makes the keys progressive items
    May make generation impossible if there's only Key 2"""
    display_name = "Make keys progressive"



class JsonFile(TextChoice):
    """Name of the hack to use.
    Custom jsons can be used with offline generation by placing the json in the data/sm64hacks folder. Note that Custom Value is not supported in web generation."""
    auto_display_name = True
    display_name = "Hack to Use"
    option_24_hour_hack  = 1
    option_cursed_castles = 2
    option_despair_marios_gambit_64 = 3
    option_eureka = 4
    option_grand_star = 5
    option_koopa_power = 6
    option_lugs_delightful_dioramas = 7
    option_marios_new_earth = 8
    option_shining_stars_repainted = 9
    option_sm64_the_green_stars = 10
    option_star_revenge_0 = 11
    option_star_revenge_3_dot_5 = 12
    option_star_revenge_4_dot_5 = 13
    option_star_revenge_8 = 14
    option_super_donkey_kong_64 = 15
    option_super_mario_64 = 16
    option_super_mario_fantasy_64 = 17
    option_super_mario_star_road = 18
    option_super_mario_treasure_world = 19
    option_ztar_attack_rebooted = 20
    default = 16

    @classmethod
    def get_option_name(cls, value) -> str:
        if cls.auto_display_name:
            option_name = cls.name_lookup[value]
            if "_dot_" in cls.name_lookup[value]:
                option_name = option_name.replace("_dot_", ".")
            return option_name.replace("_", " ").title()
        else:
            return cls.name_lookup[value]

    
@dataclass
class SM64HackOptions(PerGameCommonOptions):
    progressive_keys: ProgressiveKeys
    death_link: DeathLink
    json_file: JsonFile

