from flask import abort

from Utils import restricted_loads
from WebHostLib import cache
from WebHostLib.models import GameDataPackage
from . import api_endpoints


@api_endpoints.route('/datapackage')
@cache.cached()
def get_datapackage():
    from worlds import network_data_package
    return network_data_package


@api_endpoints.route('/datapackage/<string:checksum>')
@cache.memoize(timeout=3600)
def get_datapackage_by_checksum(checksum: str):
    package = GameDataPackage.get(checksum=checksum)
    if package:
        return restricted_loads(package.data)
    return abort(404)


@api_endpoints.route('/datapackage_checksum')
@cache.cached()
def get_datapackage_checksums():
    from worlds import network_data_package
    version_package = {
        game: game_data["checksum"] for game, game_data in network_data_package["games"].items()
    }
    return version_package


def _get_index_entry(slug: str) -> dict:
    """Return the mwgg_igdb GAMES_DATA entry for *slug*, or {} if not found.

    Safe to call even when the installed mwgg_igdb predates the schema upgrade
    (upstream_repo_url / release_ref / entry_point_module absent).
    """
    try:
        from mwgg_igdb import GAMES_DATA
        return GAMES_DATA.get(slug, {})
    except Exception:
        return {}


@api_endpoints.route('/games')
@cache.cached(timeout=300)
def games_listing():
    """Public listing of all loaded games.

    Returns per-game display metadata sourced from the loaded world classes and,
    where already present in the index, the distribution provenance fields
    (``entry_point_module`` only — source-repo URLs are suppressed from this
    public endpoint).  All three new index fields default to ``null`` until the
    corresponding ``mwgg_igdb`` package upgrade ships.
    """
    from worlds.AutoWorld import AutoWorldRegister
    from WebHostLib import app

    games = {}
    for game_name, world in AutoWorldRegister.world_types.items():
        if world.hidden or game_name in app.config.get("HIDDEN_WEBWORLDS", []):
            continue
        # Derive the module slug (e.g. "worlds.alttp" -> "alttp").
        slug = world.__module__.split(".")[-1] if "." in world.__module__ else world.__module__
        index_entry = _get_index_entry(slug)

        games[game_name] = {
            "display_name": getattr(world.web, "display_name", game_name) or game_name,
            # Non-sensitive index fields safe for public exposure.
            "entry_point_module": index_entry.get("entry_point_module"),  # null until split lands
        }
    return games
