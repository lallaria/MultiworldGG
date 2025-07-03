import importlib
import importlib.util
import logging
import os
import sys
import warnings
import zipimport
import time
import dataclasses
from typing import Dict, List, TypedDict

from Utils import local_path, user_path

local_folder = os.path.dirname(__file__)
user_folder = user_path("worlds") if user_path() != local_path() else user_path("custom_worlds")
try:
    os.makedirs(user_folder, exist_ok=True)
except OSError:  # can't access/write?
    user_folder = None

__all__ = {
    "network_data_package",
    "AutoWorldRegister",
    "world_sources",
    "local_folder",
    "user_folder",
    "GamesPackage",
    "DataPackage",
    "failed_world_loads",
}


failed_world_loads: List[str] = []


class GamesPackage(TypedDict, total=False):
    item_name_groups: Dict[str, List[str]]
    item_name_to_id: Dict[str, int]
    location_name_groups: Dict[str, List[str]]
    location_name_to_id: Dict[str, int]
    checksum: str


class DataPackage(TypedDict):
    games: Dict[str, GamesPackage]


@dataclasses.dataclass(order=True)
class WorldSource:
    entry_point: importlib.metadata.EntryPoint
    time_taken: float = -1.0

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.entry_point})"

    def load(self) -> bool:
        try:
            start = time.perf_counter()
            mod = self.entry_point.load()
            # mod.__package__ = f"worlds.{mod.__package__}"
            # mod.__name__ = f"worlds.{mod.__name__}"
            sys.modules[mod.__name__] = mod
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", message="__package__ != __spec__.parent")
                # # Found no equivalent for < 3.10
                # if hasattr(self.entry_point.loader, "exec_module"):
                #     self.entry_point.loader.exec_module(mod)
                # else:
                #     importlib.import_module(f".{self.entry_point.name.rsplit(".", 1)[0]}", "worlds")
            self.time_taken = time.perf_counter()-start
            return True

        except Exception:
            # A single world failing can still mean enough is working for the user, log and carry on
            import traceback
            import io
            file_like = io.StringIO()
            print(f"Could not load world {self}:", file=file_like)
            traceback.print_exc(file=file_like)
            file_like.seek(0)
            logging.exception(file_like.read())
            failed_world_loads.append(os.path.basename(self.entry_point.name).rsplit(".", 1)[0])
            return False

#find potential world containers, currently folders and zip-importable .apworld's
from data.game_index import GAMES_DATA

world_sources: List[WorldSource] = []
entry_points = importlib.metadata.entry_points(group="mwgg.plugins")
for game, game_data in GAMES_DATA.items():
    for entry_point in entry_points:
        class_name = game+".WorldClass"
        if class_name == entry_point.name:
            world_sources.append(WorldSource(entry_point))

world_sources.sort()
for world_source in world_sources:
    world_source.load()

# Build the data package for each game.
from .AutoWorld import AutoWorldRegister
    
network_data_package: DataPackage = {
    "games": {world_name: world.get_data_package_data() for world_name, world in AutoWorldRegister.world_types.items()},
}

