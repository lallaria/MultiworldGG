from __future__ import annotations

import typing
import enum
import warnings
from json import JSONEncoder, JSONDecoder
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from websockets import WebSocketServerProtocol as ServerConnection

from Utils import ByValue, Version

class HintStatus(ByValue, enum.IntEnum):
    HINT_UNSPECIFIED = 0
    HINT_NO_PRIORITY = 10
    HINT_AVOID = 20
    HINT_PRIORITY = 30
    HINT_FOUND = 40


class JSONMessagePart(typing.TypedDict, total=False):
    text: str
    # optional
    type: str
    color: str
    # owning player for location/item
    player: int
    # if type == item indicates item flags
    flags: int
    # if type == hint_status
    hint_status: HintStatus


class ClientStatus(ByValue, enum.IntEnum):
    CLIENT_UNKNOWN = 0
    CLIENT_CONNECTED = 5
    CLIENT_READY = 10
    CLIENT_PLAYING = 20
    CLIENT_GOAL = 30


class SlotType(ByValue, enum.IntFlag):
    spectator = 0b00
    player = 0b01
    group = 0b10

    @property
    def always_goal(self) -> bool:
        """Mark this slot as having reached its goal instantly."""
        return self.value != 0b01


class Permission(ByValue, enum.IntFlag):
    disabled = 0b000  # 0, completely disables access
    enabled = 0b001  # 1, allows manual use
    goal = 0b010  # 2, allows manual use after goal completion
    auto = 0b110  # 6, forces use after goal completion, only works for release
    auto_enabled = 0b111  # 7, forces use after goal completion, allows manual use any time

    @staticmethod
    def from_text(text: str):
        data = 0
        if "auto" in text:
            data |= 0b110
        elif "goal" in text:
            data |= 0b010
        if "enabled" in text:
            data |= 0b001
        return Permission(data)


@dataclass(frozen=True)
class NetworkPlayer:
    """Represents a particular player on a particular team."""
    team: int
    slot: int
    alias: str
    name: str
    pronouns: str | None = None
    avatar: bytes | None = None


@dataclass(frozen=True)
class NetworkSlot:
    """Represents a particular slot across teams."""
    name: str
    game: str
    type: SlotType
    group_members: list[int] | tuple = ()  # only populated if type == group


@dataclass(frozen=True)
class NetworkItem:
    item: int
    location: int
    player: int
    """ Sending player, except in LocationInfo (from LocationScouts), where it is the receiving player. """
    flags: int = 0


def _scan_for_dataclasses(obj: typing.Any) -> typing.Any:
    # Handle dataclasses
    if hasattr(obj, "__dataclass_fields__"):
        data = {}
        for field_name in obj.__dataclass_fields__:
            value = getattr(obj, field_name)
            # Handle bytes specially for JSON serialization
            if isinstance(value, bytes):
                data[field_name] = value.hex()  # Convert to hex string for JSON
            else:
                data[field_name] = value
        data["class"] = obj.__class__.__name__
        return data
    if isinstance(obj, (tuple, list, set, frozenset)):
        return tuple(_scan_for_dataclasses(o) for o in obj)
    if isinstance(obj, dict):
        return {key: _scan_for_dataclasses(value) for key, value in obj.items()}
    return obj


_encode = JSONEncoder(
    ensure_ascii=False,
    check_circular=False,
    separators=(',', ':'),
).encode


def encode(obj: typing.Any) -> str:
    return _encode(_scan_for_dataclasses(obj))


def get_any_version(data: dict) -> Version:
    data = {key.lower(): value for key, value in data.items()}  # .NET version classes have capitalized keys
    return Version(int(data["major"]), int(data["minor"]), int(data["build"]))


allowlist = {
    "NetworkPlayer": NetworkPlayer,
    "NetworkItem": NetworkItem,
    "NetworkSlot": NetworkSlot
}

custom_hooks = {
    "Version": get_any_version
}


def _object_hook(o: typing.Any) -> typing.Any:
    if isinstance(o, dict):
        hook = custom_hooks.get(o.get("class", None), None)
        if hook:
            return hook(o)
        cls = allowlist.get(o.get("class", None), None)
        if cls and hasattr(cls, "__dataclass_fields__"):
            field_names = cls.__dataclass_fields__.keys()
            # Convert hex string back to bytes for avatar field
            if "avatar" in o and isinstance(o["avatar"], str):
                try:
                    o["avatar"] = bytes.fromhex(o["avatar"])
                except ValueError:
                    o["avatar"] = None  # Invalid hex string
            # Remove unknown fields
            for key in tuple(o):
                if key not in field_names and key != "class":
                    del o[key]
            return cls(**{k: v for k, v in o.items() if k != "class"})
    return o


decode = JSONDecoder(object_hook=_object_hook).decode


class Endpoint:
    socket: ServerConnection

    def __init__(self, socket):
        self.socket = socket


class HandlerMeta(type):
    def __new__(mcs, name, bases, attrs):
        handlers = attrs["handlers"] = {}
        trigger: str = "_handle_"
        for base in bases:
            handlers.update(base.handlers)
        handlers.update({handler_name[len(trigger):]: method for handler_name, method in attrs.items() if
                         handler_name.startswith(trigger)})

        orig_init = attrs.get('__init__', None)
        if not orig_init:
            for base in bases:
                orig_init = getattr(base, '__init__', None)
                if orig_init:
                    break

        def __init__(self, *args, **kwargs):
            if orig_init:
                orig_init(self, *args, **kwargs)
            # turn functions into bound methods
            self.handlers = {name: method.__get__(self, type(self)) for name, method in
                             handlers.items()}

        attrs['__init__'] = __init__
        return super(HandlerMeta, mcs).__new__(mcs, name, bases, attrs)


class JSONTypes(str, enum.Enum):
    color = "color"
    text = "text"
    player_id = "player_id"
    player_name = "player_name"
    item_name = "item_name"
    item_id = "item_id"
    location_name = "location_name"
    location_id = "location_id"
    entrance_name = "entrance_name"

# Default color definitions - these should be imported by GUI themes
DEFAULT_TEXT_COLORS = {
    "location_color":["006f10", "00c51b"],
    "player1_color":["b42f88", "ff87d7"],
    "player2_color":["206cb8", "5fafff"],
    "entrance_color":["2985a0", "60b7e8"],
    "trap_item_color":["8f1515", "d75f5f"],
    "regular_item_color":["3b3b3b", "b2b2b2"],
    "useful_item_color":["419F44", "6EC471"],
    "skip_item_color":["419F44", "6EC471"],
    "progression_skip_item_color":["A59C3B", "d4cd87"],
    "progression_item_color":["9f8a00", "FFC500"],
    "command_echo_color":["a75600", "ff9334"]
}

class JSONtoTextParser(metaclass=HandlerMeta):
    color_codes = {}
    for key,value in DEFAULT_TEXT_COLORS.items():
        color_codes[key] = value[1]

    def __init__(self, ctx):
        self.ctx = ctx

    def __call__(self, input_object: list[JSONMessagePart]) -> str:
        return "".join(self.handle_node(section) for section in input_object)

    def handle_node(self, node: JSONMessagePart):
        node_type = node.get("type", None)
        handler = self.handlers.get(node_type, self.handlers["text"])
        return handler(node)

    def _handle_color(self, node: JSONMessagePart):
        codes = node["color"].split(";")
        buffer = "".join(color_code(code) for code in codes if code in color_codes)
        return buffer + self._handle_text(node) + color_code("reset")

    def _handle_text(self, node: JSONMessagePart):
        node["text"] = 'default'
        return self._handle_color(node)

    def _handle_player_id(self, node: JSONMessagePart):
        player = int(node["text"])
        node["color"] = 'playercolor' if self.ctx.slot_concerns_self(player) else 'friendcolor'
        node["text"] = self.ctx.player_names[player]
        return self._handle_color(node)

    # for other teams, spectators etc.? Only useful if player isn't in the clientside mapping
    def _handle_player_name(self, node: JSONMessagePart):
        node["color"] = 'friendcolor'
        return self._handle_color(node)

    def _handle_item_name(self, node: JSONMessagePart):
        flags = node.get("flags", 0)
        if flags == 0:
            node["color"] = 'regular_item_color' # filler
        elif flags & 0b1000:  # skip_balancing bit set
            if flags & 0b0001:  # progression_skip_balancing
                node["color"] = 'progression_item_color'  # citron for progression skip items
            else:  # just skip_balancing (shouldn't happen in practice)
                node["color"] = 'regular_item_color'
        elif flags & 0b0001:  # progression
            node["color"] = 'wothcolor'  # gold for required progression
        elif flags & 0b0010:  # useful
            node["color"] = 'usefulcolor'  # lime for useful items
        elif flags & 0b0100:  # trap
            node["color"] = 'trapcolor'  # salmon for traps
        else:
            node["color"] = 'regular_item_color'  # fallback to filler
        return self._handle_color(node)

    def _handle_item_id(self, node: JSONMessagePart):
        item_id = int(node["text"])
        node["text"] = self.ctx.item_names.lookup_in_slot(item_id, node["player"])
        return self._handle_item_name(node)

    def _handle_location_name(self, node: JSONMessagePart):
        node["color"] = 'foundcolor'
        return self._handle_color(node)

    def _handle_location_id(self, node: JSONMessagePart):
        location_id = int(node["text"])
        node["text"] = self.ctx.location_names.lookup_in_slot(location_id, node["player"])
        return self._handle_location_name(node)

    def _handle_entrance_name(self, node: JSONMessagePart):
        node["color"] = 'entrancecolor'
        return self._handle_color(node)

    def _handle_hint_status(self, node: JSONMessagePart):
        node["color"] = status_colors.get(node["hint_status"], "red")
        return self._handle_color(node)


class RawJSONtoTextParser(JSONtoTextParser):
    def _handle_color(self, node: JSONMessagePart):
        return self._handle_text(node)

# setting ansi colors - Added many 8 bit to go with the 4 bit.
color_codes = {'reset': 0, 'bold': 1, 'underline': 4, 'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34,
                'magenta': 35, 'cyan': 36, 'white': 37, 'black_bg': 40, 'red_bg': 41, 'green_bg': 42, 'yellow_bg': 43,
                'blue_bg': 44, 'magenta_bg': 45, 'cyan_bg': 46, 'white_bg': 47,
                'plum': 33, 'slateblue': 32, 'salmon': 31, 'limegreen': 32, 'lightgray': 37, 'gold': 33,
                'notfoundcolor': '38;5;196', #red
                'foundcolor': '38;5;34', #green
                'friendcolor': '38;5;75', #ltblue
                'entrancecolor': '38;5;27', #blue
                'playercolor': '38;5;212', #atzpink
                'junkcolor': '38;5;249', #gray
                'usefulcolor': '38;5;149', #lime
                'wothcolor': '38;5;220', #gold
                'trapcolor': '38;5;167', #salmon
                'default': 37, #white
                'bcastcolor': '38;5;208' #orange
}

def color_code(*args):
    return '\033[' + ';'.join([str(color_codes[arg]) for arg in args]) + 'm'


def color(text, *args):
    return color_code(*args) + text + '\33[0m'


def add_json_text(parts: list, text: typing.Any, **kwargs) -> None:
    parts.append({"text": str(text), **kwargs})


def add_json_item(parts: list, item_id: int, player: int = 0, item_flags: int = 0, **kwargs) -> None:
    parts.append({"text": str(item_id), "player": player, "flags": item_flags, "type": JSONTypes.item_id, **kwargs})


def add_json_location(parts: list, location_id: int, player: int = 0, **kwargs) -> None:
    parts.append({"text": str(location_id), "player": player, "type": JSONTypes.location_id, **kwargs})

## HintStatus map is the location identifier/colors
status_names: dict[HintStatus, str] = {
    HintStatus.HINT_FOUND: "(found)",
    HintStatus.HINT_UNSPECIFIED: "(unspecified)",
    HintStatus.HINT_NO_PRIORITY: "(no priority)",
    HintStatus.HINT_AVOID: "(avoid)",
    HintStatus.HINT_PRIORITY: "(priority)",
}
status_colors: dict[HintStatus, str] = {
    HintStatus.HINT_FOUND: "green",
    HintStatus.HINT_UNSPECIFIED: "white",
    HintStatus.HINT_NO_PRIORITY: "lightgray",
    HintStatus.HINT_AVOID: "salmon",
    HintStatus.HINT_PRIORITY: "gold",
}


def add_json_hint_status(parts: list, hint_status: HintStatus, text: str | None = None, **kwargs):
    parts.append({"text": text if text != None else status_names.get(hint_status, "(unknown)"),
                  "hint_status": hint_status, "type": JSONTypes.hint_status, **kwargs})


@dataclass(frozen=True)
class Hint:
    receiving_player: int
    finding_player: int
    location: int
    item: int
    found: bool
    entrance: str = ""
    item_flags: int = 0
    status: HintStatus = HintStatus.HINT_UNSPECIFIED

    def re_check(self, ctx, team) -> Hint:
        if self.found and self.status == HintStatus.HINT_FOUND:
            return self
        found = self.location in ctx.location_checks[team, self.finding_player]
        if found:
            return Hint(
                receiving_player=self.receiving_player,
                finding_player=self.finding_player,
                location=self.location,
                item=self.item,
                found=found,
                entrance=self.entrance,
                item_flags=self.item_flags,
                status=HintStatus.HINT_FOUND
            )
        return self
    
    def re_prioritize(self, ctx, status: HintStatus) -> Hint:
        if self.found and status != HintStatus.HINT_FOUND:
            status = HintStatus.HINT_FOUND
        if status != self.status:
            return Hint(
                receiving_player=self.receiving_player,
                finding_player=self.finding_player,
                location=self.location,
                item=self.item,
                found=self.found,
                entrance=self.entrance,
                item_flags=self.item_flags,
                status=status
            )
        return self

    def __hash__(self):
        return hash((self.receiving_player, self.finding_player, self.location, self.item, self.entrance))

    def as_network_message(self) -> dict:
        # Template for hint messages
        template = [
            {"text": "[Hint]: ", "type": "text"},
            {"text": "{receiving_player}", "type": "player_id"},
            {"text": "'s ", "type": "text"},
            {"text": "{item}", "type": "item_id", "player": "{receiving_player}", "flags": "{item_flags}"},
            {"text": " is at ", "type": "text"},
            {"text": "{location}", "type": "location_id", "player": "{finding_player}"},
            {"text": " in ", "type": "text"},
            {"text": "{finding_player}", "type": "player_id"},
            {"text": "{entrance_text}", "type": "text"},
            {"text": ". ", "type": "text"},
            {"text": "{status_text}", "type": "color", "color": "{status_color}"}
        ]
        
        # Determine entrance text based on whether entrance exists
        if self.entrance:
            entrance_text = "'s World at " + self.entrance
        else:
            entrance_text = "'s World"
        
        # Get status information
        status_text = status_names.get(self.status, "(unknown)")
        status_color = status_colors.get(self.status, "red")
        
        # Fill template with actual values
        parts = []
        for part in template:
            filled_part = {}
            for key, value in part.items():
                if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
                    # Replace template variables
                    var_name = value[1:-1]  # Remove { and }
                    if var_name == "receiving_player":
                        filled_part[key] = self.receiving_player
                    elif var_name == "finding_player":
                        filled_part[key] = self.finding_player
                    elif var_name == "item":
                        filled_part[key] = self.item
                    elif var_name == "location":
                        filled_part[key] = self.location
                    elif var_name == "item_flags":
                        filled_part[key] = self.item_flags
                    elif var_name == "entrance_text":
                        filled_part[key] = entrance_text
                    elif var_name == "status_text":
                        filled_part[key] = status_text
                    elif var_name == "status_color":
                        filled_part[key] = status_color
                    else:
                        filled_part[key] = value
                else:
                    filled_part[key] = value
            parts.append(filled_part)

        return {"cmd": "PrintJSON", "data": parts, "type": "Hint",
                "receiving": self.receiving_player,
                "item": NetworkItem(self.item, self.location, self.finding_player, self.item_flags),
                "found": self.found}

    @property
    def local(self):
        return self.receiving_player == self.finding_player


class _LocationStore(dict, typing.MutableMapping[int, dict[int, tuple[int, int, int]]]):
    def __init__(self, values: typing.MutableMapping[int, dict[int, tuple[int, int, int]]]):
        super().__init__(values)

        if not self:
            raise ValueError(f"Rejecting game with 0 players")

        if len(self) != max(self):
            raise ValueError("Player IDs not continuous")

        if len(self.get(0, {})):
            raise ValueError("Invalid player id 0 for location")

    def find_item(self, slots: set[int], seeked_item_id: int
                  ) -> typing.Generator[tuple[int, int, int, int, int], None, None]:
        for finding_player, check_data in self.items():
            for location_id, (item_id, receiving_player, item_flags) in check_data.items():
                if receiving_player in slots and item_id == seeked_item_id:
                    yield finding_player, location_id, item_id, receiving_player, item_flags

    def get_for_player(self, slot: int) -> dict[int, set[int]]:
        import collections
        all_locations: dict[int, set[int]] = collections.defaultdict(set)
        for source_slot, location_data in self.items():
            for location_id, values in location_data.items():
                if values[1] == slot:
                    all_locations[source_slot].add(location_id)
        return all_locations

    def get_checked(self, state: dict[tuple[int, int], set[int]], team: int, slot: int
                    ) -> list[int]:
        checked = state[team, slot]
        if not checked:
            # This optimizes the case where everyone connects to a fresh game at the same time.
            if slot not in self:
                raise KeyError(slot)
            return []
        return [location_id for
                location_id in self[slot] if
                location_id in checked]

    def get_missing(self, state: dict[tuple[int, int], set[int]], team: int, slot: int
                    ) -> list[int]:
        checked = state[team, slot]
        if not checked:
            # This optimizes the case where everyone connects to a fresh game at the same time.
            return list(self[slot])
        return [location_id for
                location_id in self[slot] if
                location_id not in checked]

    def get_remaining(self, state: dict[tuple[int, int], set[int]], team: int, slot: int
                      ) -> list[tuple[int, int]]:
        checked = state[team, slot]
        player_locations = self[slot]
        return sorted([(player_locations[location_id][1], player_locations[location_id][0]) for
                        location_id in player_locations if
                        location_id not in checked])


if TYPE_CHECKING:  # type-check with pure python implementation until we have a typing stub
    LocationStore = _LocationStore
else:
    try:
        from _speedups import LocationStore
        import _speedups
        import os.path
        if os.path.isfile("_speedups.pyx") and os.path.getctime(_speedups.__file__) < os.path.getctime("_speedups.pyx"):
            warnings.warn(f"{_speedups.__file__} outdated! "
                          f"Please rebuild with `cythonize -b -i _speedups.pyx` or delete it!")
    except ImportError:
        try:
            import pyximport
            pyximport.install()
        except ImportError:
            pyximport = None
        try:
            from _speedups import LocationStore
        except ImportError:
            warnings.warn("_speedups not available. Falling back to pure python LocationStore. "
                          "Install a matching C++ compiler for your platform to compile _speedups.")
            LocationStore = _LocationStore
