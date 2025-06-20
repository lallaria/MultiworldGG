import random
import logging
from typing import Dict
from BaseClasses import MultiWorld, Item, ItemClassification, Tutorial
from worlds.AutoWorld import World, CollectionState, WebWorld
from .Items import item_table, create_itempool, create_item, event_item_pairs, sly_episodes
from .Locations import get_location_names, get_total_locations, did_avoid_early_bk, generate_bottle_locations, generate_minigame_locations
from .Options import Sly1Options
from .Regions import create_regions
from .Types import Sly1Item, EpisodeType, episode_type_to_name, episode_type_to_shortened_name
from .Rules import set_rules
from worlds.LauncherComponents import (
    Component,
    Type,
    components,
    launch_subprocess,
    icon_paths,
)

def run_client():
    from .Sly1Client import launch_client
    launch_subprocess(launch_client, name="Sly1Client")

components.append(
    Component("Sly 1 Client", func=run_client, component_type=Type.CLIENT)
)

class Sly1Web(WebWorld):
    theme = "ocean"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Sly Cooper and the Thievius Raccoonus for MultiworldGG. "
        "This guide covers single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Nep"]
    )]

class Sly1World(World):
    """
    Sly Cooper and the Thievius Raccoonus is a action-stealth game set in a cartoony cel-shaded world.
    Avenge your father and take back the pages of the Thievius Raccoonus from the Fiendish Five!
    """

    game = "Sly Cooper and the Thievius Raccoonus"
    author: str = "Philiard"
    item_name_to_id = {name: data.ap_code for name, data in item_table.items()}
    location_name_to_id = get_location_names()
    options_dataclass = Sly1Options
    options = Sly1Options
    web = Sly1Web()

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)

    def generate_early(self):
        starting_episode = EpisodeType(self.options.StartingEpisode)
        starting_episode_long = episode_type_to_name[starting_episode]
        starting_episode_short = episode_type_to_shortened_name[starting_episode]

        # Starting Episode - please clean this up oml
        if starting_episode_long == "All":
            for episode in sly_episodes.keys():
                self.multiworld.push_precollected(self.create_item(episode))
        else:
            self.multiworld.push_precollected(self.create_item(starting_episode_long))

        # Avoid Early BK
        if did_avoid_early_bk(self):
            if starting_episode_long == "All":
                starting_episode_short = episode_type_to_shortened_name[EpisodeType(random.randrange(1, 4))]
                self.random_episode = starting_episode_short
            self.multiworld.push_precollected(self.create_item(f'{starting_episode_short} Key'))

    def create_regions(self):
        create_regions(self)

        if self.options.LocationCluesanityBundleSize.value > 0:
            generate_bottle_locations(self, self.options.LocationCluesanityBundleSize.value)

        if self.options.LocationCluesanityBundleSize.value == 0 and self.options.ItemCluesanityBundleSize.value > 0:
            logging.warning(
                f"{self.player}: Cannot have item bundles without location bundles. Setting location bundle size to item bundle size.")
            self.options.LocationCluesanityBundleSize.value = self.options.ItemCluesanityBundleSize.value
            generate_bottle_locations(self, self.options.LocationCluesanityBundleSize.value)
        
        generate_minigame_locations(self, self.options.MinigameCaches.value)

    def create_items(self):
        self.multiworld.itempool += create_itempool(self)
        for event, item in event_item_pairs.items():
            event_item = Sly1Item(item, ItemClassification.progression_skip_balancing, None, self.player)
            self.multiworld.get_location(event, self.player).place_locked_item(event_item)

    set_rules = set_rules

    def create_item(self, name: str) -> Item:
        return create_item(self, name)
    
    def fill_slot_data(self) -> Dict[str, object]:
        slot_data: Dict[str, object] = {
            "options": {
                "UnlockClockwerk": self.options.UnlockClockwerk.value,
                "RequiredBosses": self.options.RequiredBosses.value,
                "MaxPages": self.options.MaxPages.value,
                "RequiredPages": self.options.RequiredPages.value,
                "FastClockwerk": self.options.FastClockwerk.value,
                "StartingEpisode": episode_type_to_name[EpisodeType(self.options.StartingEpisode)],
                "IncludeHourglasses": self.options.IncludeHourglasses.value,
                "HourglassesRequireRoll": self.options.HourglassesRequireRoll.value,
                "AvoidEarlyBK": self.options.AvoidEarlyBK.value,
                "LocationCluesanityBundleSize": self.options.LocationCluesanityBundleSize.value,
                "ItemCluesanityBundleSize": self.options.ItemCluesanityBundleSize.value
            },
            "Seed": self.multiworld.seed_name,  # to verify the server's multiworld
            "Slot": self.multiworld.player_name[self.player],  # to connect to server
            "TotalLocations": get_total_locations(self)
        }

        return slot_data

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        return super().collect(state, item)
    
    def remove(self, state: "CollectionState", item: "Item") -> bool:
        return super().remove(state, item)