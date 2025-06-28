from random import randrange, sample
import re
import logging
from typing import Any, Dict, List, Tuple
from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState, MultiWorld, Region, Tutorial

from .Items import ATSItemClassification, AgainstTheStormItem, item_dict
from .Constants import GAME_NAME, AUTHOR, IGDB_ID
from .Locations import ATSLocationClassification, AgainstTheStormLocation, location_dict
from .Options import AgainstTheStormOptions, RecipeShuffle
from .Recipes import satisfies_recipe, blueprint_recipes, nonitem_blueprint_recipes

class AgainstTheStormWeb(WebWorld):
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Against The Storm with MWGG.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Ryguy9999"],
    )

    tutorials = [setup_en]
    
class AgainstTheStormWorld(World):
    """
    Against the Storm is a roguelite city builder
    """

    game = GAME_NAME
    author: str = AUTHOR
    igdb_id = IGDB_ID
    options_dataclass = AgainstTheStormOptions
    options: AgainstTheStormOptions
    topology_present = True
    web = AgainstTheStormWeb()
    base_id = 9999000000
    item_name_to_id = {item: id for id, item in enumerate(item_dict.keys(), base_id)}
    location_name_to_id = {location: id for id, location in enumerate(location_dict.keys(), base_id)}

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self.included_location_indices: list[int] = []
        self.production_recipes: Dict[str, List[List]] = {}
        self.filler_items: List[str] = []
    
    def are_recipes_beatable(self, production_recipes: Dict[str, List[List]]):
        glade_blueprints = [bp for bp in nonitem_blueprint_recipes if
                            bp != "Crude Workstation" and bp != "Field Kitchen" and bp != "Makeshift Post"]

        for bp in glade_blueprints:
            for recipe in production_recipes[bp]:
                # Need to verify each of these recipes have an alternate outside glade_blueprints
                satisfied = False
                for (building, recipes) in production_recipes.items():
                    if building in glade_blueprints:
                        continue
                    for rec in recipes:
                        if rec[0] == recipe[0]:
                            satisfied = True
                            break
                    if satisfied:
                        break
                if not satisfied:
                    return False
        
        return True

    def generate_early(self):
        base_locations = [name for (name, (classification, _logic)) in location_dict.items() if classification == ATSLocationClassification.basic or classification == ATSLocationClassification.dlc and self.options.enable_dlc]
        total_location_count = len(base_locations) + self.options.reputation_locations_per_biome.value * (8 if self.options.enable_dlc else 6) + self.options.extra_trade_locations.value + (self.options.grove_expedition_locations if self.options.enable_dlc else 0)
        total_item_count = len([name for (name, (_class, classification)) in item_dict.items() if
                                classification == ATSItemClassification.good or
                                classification == ATSItemClassification.guardian_part and self.options.seal_items or
                                classification == ATSItemClassification.blueprint and self.options.blueprint_items or
                                classification == ATSItemClassification.dlc_blueprint and self.options.enable_dlc])
        if total_location_count < total_item_count:
            while total_location_count < total_item_count:
                self.options.reputation_locations_per_biome.value += 1
                total_location_count += 8 if self.options.enable_dlc else 6
            logging.warning(f"[Against the Storm] Fewer locations than items detected in options, increased reputation_locations_per_biome to {self.options.reputation_locations_per_biome.value} to fit all items")
        
        self.included_location_indices.append(1)
        # This evenly spreads the option's number of locations between 2 and 17
        # Generating, for example, [10], [4, 8, 11, 15], or [2-17 sans 9]
        for i in range(self.options.reputation_locations_per_biome):
            self.included_location_indices.append(
                round(1 + (i + 1) * (17 / (self.options.reputation_locations_per_biome + 1))))

        # Recipe shuffle
        all_production = {}
        all_production.update(blueprint_recipes)
        all_production.update(nonitem_blueprint_recipes)
        if self.options.recipe_shuffle.value != "vanilla":
            skipCWS = self.options.recipe_shuffle.value == RecipeShuffle.option_exclude_crude_ws or \
                self.options.recipe_shuffle.value == RecipeShuffle.option_exclude_crude_ws_and_ms_post
            skipMSP = self.options.recipe_shuffle.value == RecipeShuffle.option_exclude_ms_post or \
                self.options.recipe_shuffle.value == RecipeShuffle.option_exclude_crude_ws_and_ms_post
            while True: # Break at the bottom when `are_recipes_beatable`
                all_recipes: List[Tuple[str, int]] = []
                for blueprint, recipes in all_production.items():
                    if blueprint == "Crude Workstation" and skipCWS or blueprint == "Makeshift Post" and skipMSP:
                        continue
                    for good, star_level in recipes.items():
                        all_recipes.append((good, star_level))
                for blueprint, recipes in all_production.items():
                    if blueprint == "Crude Workstation" and skipCWS or blueprint == "Makeshift Post" and skipMSP:
                        self.production_recipes[blueprint] = list(map(list, recipes.items()))
                        continue
                    recipe_set: List[List] = []
                    for _ in range(len(recipes)):
                        recipe = all_recipes.pop(randrange(len(all_recipes)))
                        recipe_set.append([recipe[0], recipe[1]])
                    self.production_recipes[blueprint] = recipe_set
                # Verify all of a certain good didn't wind up in glade event buildings, as that wouldn't pass logic
                if self.are_recipes_beatable(self.production_recipes):
                    break
        else:
            self.production_recipes = { key:[[item, num] for item,num in value.items()] for key,value in all_production.items() if not isinstance(value, str) }
            
    def get_filler_item_name(self):
        choice = self.multiworld.random.choices(self.filler_items)[0]
        # Reroll Survivor Bonding to half its occurence
        return self.multiworld.random.choices(self.filler_items)[0] if choice == "Survivor Bonding" and self.multiworld.random.random() < 0.5 else choice

    def create_item(self, item: str) -> AgainstTheStormItem:
        return AgainstTheStormItem(item, item_dict.get(item)[0], self.item_name_to_id[item], self.player)

    def create_items(self) -> None:
        itempool = []
        for item_key, (_ap_classification, classification) in item_dict.items():
            match classification:
                case ATSItemClassification.good:
                    itempool.append(item_key)
                case ATSItemClassification.blueprint:
                    if self.options.blueprint_items:
                        itempool.append(item_key)
                case ATSItemClassification.filler:
                    self.filler_items.append(item_key)
                case ATSItemClassification.guardian_part:
                    if self.options.seal_items:
                        itempool.append(item_key)
                case ATSItemClassification.dlc_blueprint:
                    if self.options.enable_dlc and self.options.blueprint_items:
                        itempool.append(item_key)
        
        # Fill remaining itempool space with filler
        while len(itempool) < len(self.multiworld.get_unfilled_locations(self.player)):
            itempool += [self.create_filler().name]
        
        self.multiworld.itempool += map(self.create_item, itempool)

    def create_regions(self) -> None:
        location_pool: Dict[str, int] = {}
        
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        
        trade_locations = []
        for name, (classification, logic) in location_dict.items():
            match classification:
                case ATSLocationClassification.basic:
                    location_pool[name] = self.location_name_to_id[name]
                case ATSLocationClassification.biome_rep:
                    loc_index = int(re.search(r"^(\d\d?)\w\w Reputation - .*$", name).group(1))
                    if loc_index in self.included_location_indices:
                        location_pool[name] = self.location_name_to_id[name]
                case ATSLocationClassification.extra_trade:
                    trade_locations.append(name)
                case ATSLocationClassification.dlc:
                    if self.options.enable_dlc:
                        location_pool[name] = self.location_name_to_id[name]
                case ATSLocationClassification.dlc_biome_rep:
                    if self.options.enable_dlc:
                        loc_index = int(re.search(r"^(\d\d?)\w\w Reputation - .*$", name).group(1))
                        if loc_index in self.included_location_indices:
                            location_pool[name] = self.location_name_to_id[name]
                case ATSLocationClassification.dlc_grove_expedition:
                    if self.options.enable_dlc:
                        expedition_index = int(re.search(r"^Coastal Grove - (\d\d?)\w\w Expedition$", name).group(1))
                        if expedition_index <= self.options.grove_expedition_locations:
                            location_pool[name] = self.location_name_to_id[name]
        
        trade_locations = sample(trade_locations, self.options.extra_trade_locations.value)
        for location in trade_locations:
            location_pool[location] = self.location_name_to_id[location]

        main_region = Region("Main", self.player, self.multiworld)

        main_region.add_locations(location_pool, AgainstTheStormLocation)
        self.multiworld.regions.append(main_region)

        menu_region.connect(main_region)
    
    def can_goal(self, state: CollectionState) -> bool:
        if self.options.seal_items and not state.has_all(["Guardian Heart", "Guardian Blood", "Guardian Feathers", "Guardian Essence"], self.player):
            return False
        
        if self.options.required_seal_tasks.value > 1:
            return satisfies_recipe(state, self.player, self.production_recipes if self.options.blueprint_items.value else None,
                ['Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste', 'Ale,Training Gear,Incense,Scrolls,Wine,Tea',
                 'Coal,Oil,Sea Marrow', 'Amber', 'Tools', 'Purging Fire', 'Planks', 'Bricks', 'Fabric',
                 # Above is the baseline that ensures normal winnable conditions, below ensures every Seal task
                 'Pack of Crops', 'Pack of Provisions', 'Pack of Building Materials', 'Stone,Sea Marrow,Training Gear',
                 'Pipes', 'Parts', 'Ancient Tablet'])
        else:
            return satisfies_recipe(state, self.player, self.production_recipes if self.options.blueprint_items.value else None,
                ['Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste', 'Ale,Training Gear,Incense,Scrolls,Wine,Tea',
                 'Coal,Oil,Sea Marrow', 'Amber', 'Tools', 'Purging Fire', 'Planks', 'Bricks', 'Fabric'])
    
    def check_other_location_rules(self, location: str, state: CollectionState, player: int):
        if location == "The Marshlands - Harvest from an Ancient Proto Wheat":
            return state.has("Forager's Camp", player)
        elif location == "The Marshlands - Harvest from a Dead Leviathan":
            return state.has("Trapper's Camp", player)
        elif location == "The Marshlands - Harvest from a Giant Proto Fungus":
            return state.has("Herbalist's Camp", player)
        
        return True
    
    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: self.can_goal(state)
        for location in self.multiworld.get_locations(self.player):
            logic = location_dict[location.name][1]
            set_rule(location, lambda state, logic=logic: self.check_other_location_rules(location.name, state, self.player) and \
                        satisfies_recipe(state, self.player, self.production_recipes if self.options.blueprint_items.value else None, logic))

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "recipe_shuffle": self.options.recipe_shuffle.value,
            "deathlink": self.options.deathlink.value,
            "blueprint_items": self.options.blueprint_items.value,
            "continue_blueprints_for_reputation": self.options.continue_blueprints_for_reputation.value,
            "seal_items": self.options.seal_items.value,
            "required_seal_tasks": self.options.required_seal_tasks.value,
            "enable_dlc": self.options.enable_dlc.value,
            "rep_location_indices": self.included_location_indices,
            "production_recipes": self.production_recipes
        }
    