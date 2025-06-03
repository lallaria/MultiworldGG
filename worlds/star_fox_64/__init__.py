import worlds.LauncherComponents as LauncherComponents
import Options, settings, Utils, logging, typing
from worlds.AutoWorld import World, WebWorld
from Options import OptionGroup
from BaseClasses import Tutorial

from . import options, regions, locations, items, data, rules
from .options import StarFox64Options, StarFox64OptionsList
from .regions import StarFox64Region
from .locations import StarFox64Location
from .items import StarFox64Item
from .rules import StarFox64Rules
from .version import version
from .ids import option_name_to_id, group_items

def launch_client():
  from . import client
  LauncherComponents.launch_subprocess(client.run, name="Star Fox 64 Client")

LauncherComponents.components.append(LauncherComponents.Component("Star Fox 64 Client", func=launch_client))

class StarFox64Settings(settings.Group):
  class RomPath(settings.OptionalUserFilePath):
    """File path of the Star Fox 64 v1.1 ROM."""

  class PatchPath(settings.OptionalUserFolderPath):
    """Folder path of where to save the patched ROM."""

  class ProgramPath(settings.OptionalUserFilePath):
    """
      File path of the program to automatically run.
      Leave blank to disable.
    """

  class ProgramArgs(str):
    """
      Arguments to pass to the automatically run program.
      Leave blank to disable.
    """

  class EnableTracker(settings.Bool):
    """
      Whether to enable the built in logic Tracker.
      If enabled, the 'Tracker' tab will show all unchecked locations in logic.
    """

  rom_path: RomPath = ""
  patch_path: PatchPath = ""
  program_path: ProgramPath = ""
  program_args: ProgramArgs = f"--lua={Utils.local_path('data', 'lua', 'connector_sf64_bizhawk.lua')}"
  enable_tracker: typing.Union[EnableTracker, bool] = True

class StarFox64WebWorld(WebWorld):
  rich_text_options_doc = True
  tutorials = [
    Tutorial(
      "Setup Guide",
      "A guide to setting up Star Fox 64 with MultiworldGG.",
      "English",
      "setup_en.md",
      "setup/en",
      ["Austin"]
    )
  ]
  option_groups = [
    OptionGroup("Common Options", [
      Options.ProgressionBalancing,
      Options.Accessibility,
      options.DeathLink,
      options.RingLink,
    ]),
    OptionGroup("Goal Options", [
      options.VictoryCondition,
      options.RequiredMedals,
    ]),
    OptionGroup("Shuffle Options", [
      options.LevelAccess,
      options.ShuffleStartingLevel,
      options.ShuffleMedals,
      options.ShuffleCheckpoints,
    ]),
    OptionGroup("Speedup Options", [
      options.AccomplishedSendsComplete,
    ]),
    OptionGroup("Vanity Options", [
      options.RadioRando,
      options.EngineGlow,
    ]),
    OptionGroup("Accessibility Options", [
      options.DefaultLives,
      options.MedalCorneria,
      options.MedalMeteo,
      options.MedalSectorY,
      options.MedalKatina,
      options.MedalFortuna,
      options.MedalAquas,
      options.MedalSolar,
      options.MedalSectorX,
      options.MedalZoness,
      options.MedalTitania,
      options.MedalSectorZ,
      options.MedalMacbeth,
      options.MedalArea6,
      options.MedalBolse,
      options.MedalVenom,
    ]),
  ]

class StarFox64World(World):
  """
    Star Fox 64 is a 3D rail shooter game in which the player controls one of the vehicles piloted by Fox McCloud, usually an Arwing.
  """
  game = "Star Fox 64"
  author: str = "Austin"
  igdb_id = 6890
  options_dataclass = StarFox64Options
  options: StarFox64Options
  settings: StarFox64Settings
  settings_key = "sf64_options"
  item_name_to_id = items.name_to_id
  location_name_to_id = locations.name_to_id
  item_name_groups = items.groups
  location_name_groups = locations.groups
  topology_present = True
  web = StarFox64WebWorld()
  filler_weights = {
    "Silver Ring": 50,
    "Silver Star": 25,
    "Laser Upgrade": 9.5,
    "Bomb": 9.5,
    "Gold Ring": 6,
  }

  def check_options(self):
    if not self.options.shuffle_medals and self.options.required_medals == 15 and self.options.victory_condition == "andross_or_robot_andross":
      logging.warning(
        f"{self.game} player {self.player} ({self.player_name}): "
        "Wants all Medals to access Venom and wants Venom to have a Medal. Forcing required_medals to 14."
      )
      self.options.required_medals.value = 14

  def create_item(self, item_name):
    return items.create_item(self, item_name)

  def create_victory_condition(self):
    condition = lambda state: False
    andross = "Defeated Andross"
    robot_andross = "Defeated Robot Andross"
    match self.options.victory_condition:
      case "andross_or_robot_andross":
        condition = lambda state: state.has_any([andross, robot_andross], self.player)
      case "andross_and_robot_andross":
        condition = lambda state: state.has_all([andross, robot_andross], self.player)
      case "andross":
        condition = lambda state: state.has(andross, self.player)
    self.multiworld.completion_condition[self.player] = condition

  def create_everything(self):
    parser = StarFox64Rules(self)
    self.create_victory_condition()
    swap_items = {}
    if self.options.shuffle_starting_level:
      valid_levels = group_items["Levels"].copy()
      valid_levels.remove("Venom")
      item_name = self.random.choice(valid_levels)
      swap_items["Corneria"] = item_name
      swap_items[item_name] = "Corneria"
    for region_name, region in data.regions.items():
      ap_region = regions.create_region(self, region_name)
      for key, value in region.items():
        match key:
          case "locations":
            for location_name, location in value.items():
              ap_location = StarFox64Location(self.player, location_name, None, ap_region)
              item_name = items.pick_name(self, location["item"], location.get("group"))
              if item_name in swap_items:
                item_name = swap_items[item_name]
              if item_name == "Nothing":
                item_name = self.get_filler_item_name()
              item = self.create_item(item_name)
              ap_location.access_rule = parser.parse(location["logic"], f"{self.game}, Location: {region_name} -> {location_name}")
              if region_name == "Menu":
                if ap_location.access_rule(None):
                  self.push_precollected(item)
                continue
              if item.code:
                ap_location.address = self.location_name_to_id[location_name]
                self.multiworld.itempool.append(item)
              else:
                ap_location.place_locked_item(item)
              ap_region.locations.append(ap_location)
          case "exits":
            for exit_name, _exit in value.items():
              ap_exit = regions.create_region(self, exit_name)
              ap_region.connect(ap_exit, None, parser.parse(_exit["logic"], f"{self.game}, Exit: {region_name} -> {exit_name}"))
      self.multiworld.regions.append(ap_region)
    regions.cache.clear()

  def create_items(self):
    self.check_options()
    self.create_everything()

  def get_filler_item_name(self):
    return self.random.choices(list(self.filler_weights.keys()), self.filler_weights.values())[0]

  def fill_slot_data(self):
    return {
      "options": self.options.as_dict(*option_name_to_id.keys()),
      "version": version.as_u32(),
    }
