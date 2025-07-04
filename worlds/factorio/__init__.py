from __future__ import annotations

import collections
import logging
import typing

import Utils
from BaseClasses import Region, Location, Item, Tutorial, ItemClassification
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components, Type, launch as launch_component
from worlds.generic import Rules
from .Locations import location_pools, location_table
from .Mod import generate_mod
from .Options import (FactorioOptions, MaxSciencePack, Silo, Satellite, TechTreeInformation, Goal,
                      TechCostDistribution, option_groups)
from .Shapes import get_shapes
from .Technologies import base_tech_table, recipe_sources, base_technology_table, \
    all_product_sources, required_technologies, get_rocket_requirements, \
    progressive_technology_table, common_tech_table, tech_to_progressive_lookup, progressive_tech_table, \
    get_science_pack_pools, Recipe, recipes, technology_table, tech_table, factorio_base_id, useless_technologies, \
    fluids, stacking_items, valid_ingredients, progressive_rows
from .settings import FactorioSettings


def launch_client(*args: str):
    from .Client import launch
    launch_component(launch, name="Factorio Client", args=args)


components.append(Component("Factorio Client", func=launch_client, component_type=Type.CLIENT))


class FactorioWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the MultiworldGG Factorio software on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Berserker, Farrak Kilhn"]
    )]
    option_groups = option_groups


class FactorioItem(Item):
    game = "Factorio"


all_items = tech_table.copy()
all_items["Attack Trap"] = factorio_base_id - 1
all_items["Evolution Trap"] = factorio_base_id - 2
all_items["Teleport Trap"] = factorio_base_id - 3
all_items["Grenade Trap"] = factorio_base_id - 4
all_items["Cluster Grenade Trap"] = factorio_base_id - 5
all_items["Artillery Trap"] = factorio_base_id - 6
all_items["Atomic Rocket Trap"] = factorio_base_id - 7
all_items["Atomic Cliff Remover Trap"] = factorio_base_id - 8
all_items["Inventory Spill Trap"] = factorio_base_id - 9


class Factorio(World):
    """
    Factorio is a game about automation. You play as an engineer who has crash landed on the planet
    Nauvis, an inhospitable world filled with dangerous creatures called biters. Build a factory,
    research new technologies, and become more efficient in your quest to build a rocket and return home.
    """
    game = "Factorio"
    author: str = "Berserker66"
    special_nodes = {"automation", "logistics", "rocket-silo"}
    custom_recipes: typing.Dict[str, Recipe]
    location_pool: typing.List[FactorioScienceLocation]
    advancement_technologies: typing.Set[str]

    web = FactorioWeb()
    options_dataclass = FactorioOptions
    options: FactorioOptions

    item_name_to_id = all_items
    location_name_to_id = location_table
    item_name_groups = {
        "Progressive": set(progressive_tech_table.keys()),
    }
    required_client_version = (0, 6, 0)
    if Utils.version_tuple < required_client_version:
        raise Exception(f"Update Archipelago to use this world ({game}).")
    ordered_science_packs: typing.List[str] = MaxSciencePack.get_ordered_science_packs()
    tech_tree_layout_prerequisites: typing.Dict[FactorioScienceLocation, typing.Set[FactorioScienceLocation]]
    tech_mix: int = 0
    skip_silo: bool = False
    origin_region_name = "Nauvis"
    science_locations: typing.List[FactorioScienceLocation]
    removed_technologies: typing.Set[str]
    settings: typing.ClassVar[FactorioSettings]
    trap_names: tuple[str] = ("Evolution", "Attack", "Teleport", "Grenade", "Cluster Grenade", "Artillery",
                              "Atomic Rocket", "Atomic Cliff Remover", "Inventory Spill")
    want_progressives: dict[str, bool] = collections.defaultdict(lambda: False)

    def __init__(self, world, player: int):
        super(Factorio, self).__init__(world, player)
        self.removed_technologies = useless_technologies.copy()
        self.advancement_technologies = set()
        self.custom_recipes = {}
        self.science_locations = []
        self.tech_tree_layout_prerequisites = {}

    generate_output = generate_mod

    def generate_early(self) -> None:
        # if max < min, then swap max and min
        if self.options.max_tech_cost < self.options.min_tech_cost:
            self.options.min_tech_cost.value, self.options.max_tech_cost.value = \
                self.options.max_tech_cost.value, self.options.min_tech_cost.value
        self.tech_mix = self.options.tech_cost_mix.value
        self.skip_silo = self.options.silo.value == Silo.option_spawn
        self.want_progressives = collections.defaultdict(
            lambda: self.options.progressive.want_progressives(self.random))

    def create_regions(self):
        player = self.player
        random = self.random
        nauvis = Region("Nauvis", player, self.multiworld)

        location_count = len(base_tech_table) - len(useless_technologies) - self.skip_silo

        for name in self.trap_names:
            name = name.replace(" ", "_").lower()+"_traps"
            location_count += getattr(self.options, name)

        location_pool = []

        for pack in sorted(self.options.max_science_pack.get_allowed_packs()):
            location_pool.extend(location_pools[pack])
        try:
            location_names = random.sample(location_pool, location_count)
        except ValueError as e:
            # should be "ValueError: Sample larger than population or is negative"
            raise Exception("Too many traps for too few locations. Either decrease the trap count, "
                            f"or increase the location count (higher max science pack). (Player {self.player})") from e

        self.science_locations = [FactorioScienceLocation(player, loc_name, self.location_name_to_id[loc_name], nauvis)
                                  for loc_name in location_names]
        distribution: TechCostDistribution = self.options.tech_cost_distribution
        min_cost = self.options.min_tech_cost.value
        max_cost = self.options.max_tech_cost.value
        if distribution == distribution.option_even:
            rand_values = (random.randint(min_cost, max_cost) for _ in self.science_locations)
        else:
            mode = {distribution.option_low: min_cost,
                    distribution.option_middle: (min_cost+max_cost)//2,
                    distribution.option_high: max_cost}[distribution.value]
            rand_values = (random.triangular(min_cost, max_cost, mode) for _ in self.science_locations)
        rand_values = sorted(rand_values)
        if self.options.ramping_tech_costs:
            def sorter(loc: FactorioScienceLocation):
                return loc.complexity, loc.rel_cost
        else:
            def sorter(loc: FactorioScienceLocation):
                return loc.rel_cost
        for i, location in enumerate(sorted(self.science_locations, key=sorter)):
            location.count = rand_values[i]
        del rand_values
        nauvis.locations.extend(self.science_locations)
        location = FactorioLocation(player, "Rocket Launch", None, nauvis)
        nauvis.locations.append(location)
        event = FactorioItem("Victory", ItemClassification.progression, None, player)
        location.place_locked_item(event)

        for ingredient in sorted(self.options.max_science_pack.get_allowed_packs()):
            location = FactorioLocation(player, f"Automate {ingredient}", None, nauvis)
            nauvis.locations.append(location)
            event = FactorioItem(f"Automated {ingredient}", ItemClassification.progression, None, player)
            location.place_locked_item(event)

        self.multiworld.regions.append(nauvis)

    def create_items(self) -> None:
        self.custom_technologies = self.set_custom_technologies()
        self.set_custom_recipes()

        for trap_name in self.trap_names:
            self.multiworld.itempool.extend(self.create_item(f"{trap_name} Trap") for _ in
                                            range(getattr(self.options,
                                                          f"{trap_name.lower().replace(' ', '_')}_traps")))

        cost_sorted_locations = sorted(self.science_locations, key=lambda location: location.name)
        special_index = {"automation": 0,
                         "logistics": 1,
                         "rocket-silo": -1}
        loc: FactorioScienceLocation
        if self.options.tech_tree_information == TechTreeInformation.option_full:
            # mark all locations as pre-hinted
            for loc in self.science_locations:
                loc.revealed = True
        if self.skip_silo:
            self.removed_technologies |= {"rocket-silo"}
        for tech_name in base_tech_table:
            if tech_name not in self.removed_technologies:
                progressive_item_name = tech_to_progressive_lookup.get(tech_name, tech_name)
                want_progressive = self.want_progressives[progressive_item_name]
                item_name = progressive_item_name if want_progressive else tech_name
                tech_item = self.create_item(item_name)
                index = special_index.get(tech_name, None)
                if index is None:
                    self.multiworld.itempool.append(tech_item)
                else:
                    loc = cost_sorted_locations[index]
                    if index >= 0:
                        # beginning techs - limit cost to 10
                        # as automation is not achievable yet and hand-crafting for hours is not fun gameplay
                        loc.count = min(loc.count, 10)
                    loc.place_locked_item(tech_item)
                    loc.revealed = True

    def get_filler_item_name(self) -> str:
        tech_name: str = self.random.choice(tuple(tech_table))
        progressive_item_name: str = tech_to_progressive_lookup.get(tech_name, tech_name)
        want_progressive: bool = self.want_progressives[progressive_item_name]
        return progressive_item_name if want_progressive else tech_name

    def set_rules(self):
        player = self.player
        shapes = get_shapes(self)

        for ingredient in self.options.max_science_pack.get_allowed_packs():
            location = self.get_location(f"Automate {ingredient}")

            if self.options.recipe_ingredients:
                custom_recipe = self.custom_recipes[ingredient]

                location.access_rule = lambda state, ingredient=ingredient, custom_recipe=custom_recipe: \
                    (not technology_table[ingredient].unlocks or state.has(ingredient, player)) and \
                    all(state.has(technology.name, player) for sub_ingredient in custom_recipe.ingredients
                        for technology in required_technologies[sub_ingredient]) and \
                    all(state.has(technology.name, player) for technology in required_technologies[custom_recipe.crafting_machine])

            else:
                location.access_rule = lambda state, ingredient=ingredient: \
                    all(state.has(technology.name, player) for technology in required_technologies[ingredient])
            assert self.multiworld.get_all_state(use_cache=True, allow_partial_entrances=True).can_reach(location), f"Can never reach {location}."

        for location in self.science_locations:
            Rules.set_rule(location, lambda state, ingredients=frozenset(location.ingredients):
                all(state.has(f"Automated {ingredient}", player) for ingredient in ingredients))
            prerequisites = shapes.get(location)
            if prerequisites:
                Rules.add_rule(location, lambda state, locations=frozenset(prerequisites):
                    all(state.can_reach(loc) for loc in locations))

        silo_recipe = None
        cargo_pad_recipe = None
        if self.options.silo == Silo.option_spawn:
            silo_recipe = self.get_recipe("rocket-silo")
            cargo_pad_recipe = self.get_recipe("cargo-landing-pad")
        part_recipe = self.custom_recipes["rocket-part"]
        satellite_recipe = None
        if self.options.goal == Goal.option_satellite:
            satellite_recipe = self.get_recipe("satellite")
        victory_tech_names = get_rocket_requirements(silo_recipe, part_recipe, satellite_recipe, cargo_pad_recipe)
        if self.options.silo == Silo.option_spawn:
            victory_tech_names -= {"rocket-silo"}
        else:
            victory_tech_names |= {"rocket-silo"}
        self.get_location("Rocket Launch").access_rule = lambda state: all(state.has(technology, player)
                                                                           for technology in
                                                                           victory_tech_names)
        self.multiworld.completion_condition[player] = lambda state: state.has('Victory', player)

    def get_recipe(self, name: str) -> Recipe:
        return self.custom_recipes[name] if name in self.custom_recipes \
            else next(iter(all_product_sources.get(name)))

    def generate_basic(self):
        map_basic_settings = self.options.world_gen.value["basic"]
        if map_basic_settings.get("seed", None) is None:  # allow seed 0
            # 32 bit uint
            map_basic_settings["seed"] = self.random.randint(0, 2 ** 32 - 1)

        start_location_hints: typing.Set[str] = self.options.start_location_hints.value

        for loc in self.science_locations:
            # show start_location_hints ingame
            if loc.name in start_location_hints:
                loc.revealed = True
            # make spoiler match mod info
            elif loc.revealed:
                start_location_hints.add(loc.name)

    def collect_item(self, state, item, remove=False):
        if item.advancement and item.name in progressive_technology_table:
            prog_table = progressive_technology_table[item.name].progressive
            if remove:
                for item_name in reversed(prog_table):
                    if state.has(item_name, item.player):
                        return item_name
            else:
                for item_name in prog_table:
                    if not state.has(item_name, item.player):
                        return item_name

        return super(Factorio, self).collect_item(state, item, remove)

    @classmethod
    def stage_write_spoiler(cls, world, spoiler_handle):
        factorio_players = world.get_game_players(cls.game)
        spoiler_handle.write('\n\nFactorio Recipes:\n')
        for player in factorio_players:
            name = world.get_player_name(player)
            for recipe in world.worlds[player].custom_recipes.values():
                spoiler_handle.write(f"\n{recipe.name} ({name}): {recipe.ingredients} -> {recipe.products}")

    @staticmethod
    def get_category(category: str, liquids: int) -> str:
        categories = {1: "crafting-with-fluid",
                      2: "chemistry"}
        return categories.get(liquids, category)

    def make_quick_recipe(self, original: Recipe, pool: list, allow_liquids: int = 2,
                          ingredients_offset: int = 0) -> Recipe:
        count: int = len(original.ingredients) + ingredients_offset
        assert len(pool) >= count, f"Can't pick {count} many items from pool {pool}."
        new_ingredients = {}
        liquids_used = 0
        for _ in range(count):
            new_ingredient = pool.pop()
            if new_ingredient in fluids:
                while liquids_used == allow_liquids and new_ingredient in fluids:
                    # liquids already at max for current recipe.
                    # Return the liquid to the pool and get a new ingredient.
                    pool.append(new_ingredient)
                    new_ingredient = pool.pop(0)
                liquids_used += 1 if new_ingredient in fluids else 0
            new_ingredients[new_ingredient] = 1
        return Recipe(original.name, self.get_category(original.category, liquids_used), new_ingredients,
                      original.products, original.energy)

    def make_balanced_recipe(self, original: Recipe, pool: typing.Set[str], factor: float = 1,
                             allow_liquids: int = 2, ingredients_offset: int = 0) -> Recipe:
        """Generate a recipe from pool with time and cost similar to original * factor"""
        new_ingredients = {}
        # have to first sort for determinism, while filtering out non-stacking items
        pool: typing.List[str] = sorted(pool & valid_ingredients)
        # then sort with random data to shuffle
        self.random.shuffle(pool)
        target_raw = int(sum((count for ingredient, count in original.base_cost.items())) * factor)
        target_energy = original.total_energy * factor
        target_num_ingredients = len(original.ingredients) + ingredients_offset
        remaining_raw = target_raw
        remaining_energy = target_energy
        remaining_num_ingredients = target_num_ingredients
        fallback_pool = []
        liquids_used = 0

        # fill all but one slot with random ingredients, last with a good match
        while remaining_num_ingredients > 0 and pool:
            ingredient = pool.pop()
            if liquids_used == allow_liquids and ingredient in fluids:
                continue  # can't use this ingredient as we already have maximum liquid in our recipe.
            ingredient_raw = 0
            if ingredient in all_product_sources:
                ingredient_recipe = min(all_product_sources[ingredient], key=lambda recipe: recipe.rel_cost)
                ingredient_raw = sum((count for ingredient, count in ingredient_recipe.base_cost.items()))
                ingredient_energy = ingredient_recipe.total_energy
            else:
                # assume simple ore TODO: remove if tree when mining data is harvested from Factorio
                ingredient_energy = 2
            if not ingredient_raw:
                ingredient_raw = 1
            if remaining_num_ingredients == 1:
                max_raw = 1.1 * remaining_raw
                min_raw = 0.9 * remaining_raw
                max_energy = 1.1 * remaining_energy
                min_energy = 0.9 * remaining_energy
            else:
                max_raw = remaining_raw * 0.75
                min_raw = (remaining_raw - max_raw) / remaining_num_ingredients
                max_energy = remaining_energy * 0.75
                min_energy = (remaining_energy - max_energy) / remaining_num_ingredients
            min_num_raw = min_raw / ingredient_raw
            max_num_raw = max_raw / ingredient_raw
            min_num_energy = min_energy / ingredient_energy
            max_num_energy = max_energy / ingredient_energy
            min_num = int(max(1, min_num_raw, min_num_energy))
            max_num = int(min(1000, max_num_raw, max_num_energy))
            if min_num > max_num:
                fallback_pool.append(ingredient)
                continue  # can't use that ingredient
            num = self.random.randint(min_num, max_num)
            new_ingredients[ingredient] = num
            remaining_raw -= num * ingredient_raw
            remaining_energy -= num * ingredient_energy
            remaining_num_ingredients -= 1
            if ingredient in fluids:
                liquids_used += 1

        # fill failed slots with whatever we got
        pool = fallback_pool
        while remaining_num_ingredients > 0 and pool:
            ingredient = pool.pop()
            if liquids_used == allow_liquids and ingredient in fluids:
                continue  # can't use this ingredient as we already have maximum liquid in our recipe.

            ingredient_recipe = recipes.get(ingredient, None)
            if not ingredient_recipe and ingredient.endswith("-barrel"):
                ingredient_recipe = recipes.get(f"fill-{ingredient}", None)
            if not ingredient_recipe:
                logging.warning(f"missing recipe for {ingredient}")
                continue
            ingredient_raw = sum((count for ingredient, count in ingredient_recipe.base_cost.items()))
            ingredient_energy = ingredient_recipe.total_energy
            num_raw = remaining_raw / ingredient_raw / remaining_num_ingredients
            num_energy = remaining_energy / ingredient_energy / remaining_num_ingredients
            num = int(min(num_raw, num_energy))
            if num < 1:
                continue

            new_ingredients[ingredient] = num
            remaining_raw -= num * ingredient_raw
            remaining_energy -= num * ingredient_energy
            remaining_num_ingredients -= 1
            if ingredient in fluids:
                liquids_used += 1

        if remaining_num_ingredients > 1:
            logging.warning("could not randomize recipe")

        return Recipe(original.name, self.get_category(original.category, liquids_used), new_ingredients,
                      original.products, original.energy)

    def set_custom_technologies(self):
        custom_technologies = {}
        allowed_packs = self.options.max_science_pack.get_allowed_packs()
        for technology_name, technology in base_technology_table.items():
            custom_technologies[technology_name] = technology.get_custom(self, allowed_packs, self.player)
        return custom_technologies

    def set_custom_recipes(self):
        ingredients_offset = self.options.recipe_ingredients_offset
        original_rocket_part = recipes["rocket-part"]
        science_pack_pools = get_science_pack_pools()
        valid_pool = sorted(science_pack_pools[self.options.max_science_pack.get_max_pack()]
                            & valid_ingredients)
        self.random.shuffle(valid_pool)
        self.custom_recipes = {"rocket-part": Recipe("rocket-part", original_rocket_part.category,
                                                     {valid_pool[x]: 10 for x in range(3 + ingredients_offset)},
                                                     original_rocket_part.products,
                                                     original_rocket_part.energy)}

        if self.options.recipe_ingredients:
            valid_pool = []
            for pack in self.options.max_science_pack.get_ordered_science_packs():
                valid_pool += sorted(science_pack_pools[pack])
                self.random.shuffle(valid_pool)
                if pack in recipes:  # skips over space science pack
                    new_recipe = self.make_quick_recipe(recipes[pack], valid_pool, ingredients_offset=
                                                        ingredients_offset.value)
                    self.custom_recipes[pack] = new_recipe

        if self.options.silo.value == Silo.option_randomize_recipe \
                or self.options.satellite.value == Satellite.option_randomize_recipe:
            valid_pool = set()
            for pack in sorted(self.options.max_science_pack.get_allowed_packs()):
                valid_pool |= science_pack_pools[pack]

            if self.options.silo.value == Silo.option_randomize_recipe:
                new_recipe = self.make_balanced_recipe(
                    recipes["rocket-silo"], valid_pool,
                    factor=(self.options.max_science_pack.value + 1) / 7,
                    ingredients_offset=ingredients_offset.value)
                self.custom_recipes["rocket-silo"] = new_recipe

            if self.options.satellite.value == Satellite.option_randomize_recipe:
                new_recipe = self.make_balanced_recipe(
                    recipes["satellite"], valid_pool,
                    factor=(self.options.max_science_pack.value + 1) / 7,
                    ingredients_offset=ingredients_offset.value)
                self.custom_recipes["satellite"] = new_recipe
        bridge = "ap-energy-bridge"
        new_recipe = self.make_quick_recipe(
            Recipe(bridge, "crafting", {"replace_1": 1, "replace_2": 1, "replace_3": 1,
                                        "replace_4": 1, "replace_5": 1, "replace_6": 1},
                   {bridge: 1}, 10),
            sorted(science_pack_pools[self.options.max_science_pack.get_ordered_science_packs()[0]]),
            ingredients_offset=ingredients_offset.value)
        for ingredient_name in new_recipe.ingredients:
            new_recipe.ingredients[ingredient_name] = self.random.randint(50, 500)
        self.custom_recipes[bridge] = new_recipe

        needed_recipes = self.options.max_science_pack.get_allowed_packs() | {"rocket-part"}
        if self.options.silo != Silo.option_spawn:
            needed_recipes |= {"rocket-silo", "cargo-landing-pad"}
        if self.options.goal.value == Goal.option_satellite:
            needed_recipes |= {"satellite"}

        for recipe in needed_recipes:
            recipe = self.custom_recipes.get(recipe, recipes[recipe])
            self.advancement_technologies |= {tech.name for tech in recipe.recursive_unlocking_technologies}

        # handle marking progressive techs as advancement
        prog_add = set()
        for tech in self.advancement_technologies:
            if tech in tech_to_progressive_lookup:
                prog_add.add(tech_to_progressive_lookup[tech])
        self.advancement_technologies |= prog_add

    def create_item(self, name: str) -> FactorioItem:
        if name in tech_table:  # is a Technology
            if name in self.advancement_technologies:
                classification = ItemClassification.progression
            else:
                classification = ItemClassification.filler
            return FactorioItem(name,
                                classification,
                                tech_table[name], self.player)

        item = FactorioItem(name,
                            ItemClassification.trap if name.endswith("Trap") else ItemClassification.filler,
                            all_items[name], self.player)
        return item


class FactorioLocation(Location):
    game: str = Factorio.game


class FactorioScienceLocation(FactorioLocation):
    complexity: int
    revealed: bool = False

    # Factorio technology properties:
    ingredients: typing.Dict[str, int]
    count: int = 0

    def __init__(self, player: int, name: str, address: int, parent: Region):
        super(FactorioScienceLocation, self).__init__(player, name, address, parent)
        # "AP-{Complexity}-{Cost}"
        self.complexity = int(self.name[3]) - 1
        self.rel_cost = int(self.name[5:])

        self.ingredients = {Factorio.ordered_science_packs[self.complexity]: 1}
        for complexity in range(self.complexity):
            if (parent.multiworld.worlds[self.player].options.tech_cost_mix >
                    parent.multiworld.worlds[self.player].random.randint(0, 99)):
                self.ingredients[Factorio.ordered_science_packs[complexity]] = 1

    @property
    def factorio_ingredients(self) -> typing.List[typing.Tuple[str, int]]:
        return [(name, count) for name, count in self.ingredients.items()]
