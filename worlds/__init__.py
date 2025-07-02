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
from .AutoWorld import AutoWorldRegister

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
    path: str  # typically relative path from this module
    is_zip: bool = False
    relative: bool = True  # relative to regular world import folder
    time_taken: float = -1.0

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.path}, is_zip={self.is_zip}, relative={self.relative})"

    def load(self) -> bool:
        try:
            start = time.perf_counter()
            mod = importlib.util.module_from_spec(self.entry_point.spec)
            mod.__package__ = f"worlds.{mod.__package__}"
            mod.__name__ = f"worlds.{mod.__name__}"
            sys.modules[mod.__name__] = mod
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", message="__package__ != __spec__.parent")
                # Found no equivalent for < 3.10
                if hasattr(self.entry_point.loader, "exec_module"):
                    self.entry_point.loader.exec_module(mod)
                else:
                    importlib.import_module(f".{self.entry_point.name.rsplit(".", 1)[0]}", "worlds")
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


class _NetworkDataPackage:
    """Network data package that always reflects the current state of registered worlds."""
    
    def __getitem__(self, key: str):
        return self._construct_data_package()[key]
    
    def get(self, key: str, default=None):
        return self._construct_data_package().get(key, default)
    
    def keys(self):
        return self._construct_data_package().keys()
    
    def values(self):
        return self._construct_data_package().values()
    
    def items(self):
        return self._construct_data_package().items()
    
    def _construct_data_package(self) -> DataPackage:
        """Construct the network data package from loaded worlds in a deterministic order"""
        from worlds.AutoWorld import AutoWorldRegister
        # Sort world types by name to ensure consistent ordering
        sorted_worlds = sorted(AutoWorldRegister.world_types.items(), key=lambda x: x[0])
        
        # Build games dict in sorted order to ensure consistent serialization
        games_dict = {}
        for world_name, world in sorted_worlds:
            games_dict[world_name] = world.get_data_package_data()
        
        return {
            "games": games_dict,
        }


# Create the always-up-to-date network data package instance
network_data_package = _NetworkDataPackage()

