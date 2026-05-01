"""Monitoring API endpoints for active rooms and games."""
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional
from uuid import UUID

from flask import jsonify, request, abort
from pony.orm import db_session, select

from Utils import restricted_loads, utcnow
from WebHostLib import app, to_url

from ..models import Room, Command


from . import api_endpoints


def _get_index_metadata(slug: str) -> Dict[str, Any]:
    """Return the full mwgg_igdb GAMES_DATA entry for *slug*.

    Includes the three new distribution fields (upstream_repo_url, release_ref,
    entry_point_module) when the installed mwgg_igdb has been upgraded; returns
    them as None otherwise so callers always see a consistent shape.
    """
    try:
        from mwgg_igdb import GAMES_DATA
        entry = GAMES_DATA.get(slug, {})
    except Exception:
        entry = {}
    return {
        "upstream_repo_url": entry.get("upstream_repo_url"),
        "release_ref": entry.get("release_ref"),
        "entry_point_module": entry.get("entry_point_module"),
    }


def require_admin_token():
    """Check if admin token is required and validate it from request."""
    admin_token = app.config.get("MONITORING_ADMIN_TOKEN")
    
    # Block endpoints if no token is configured
    if not admin_token:
        abort(503)
    
    # Check for token in Authorization header (Bearer token format)
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        abort(401)
    provided_token = auth_header[7:]
    if provided_token != admin_token:
        abort(401)


def is_room_active(room: Room) -> bool:
    """Check if a room is currently active (hasn't timed out and has a valid port)."""
    # Only consider rooms with a valid port (> 0)
    if not room.last_port or room.last_port <= 0:
        return False
    now = utcnow()
    time_since_activity = now - room.last_activity
    return time_since_activity <= timedelta(seconds=room.timeout + 5)


def get_per_player_last_activity(room: Room) -> Dict[int, Optional[float]]:
    """Get the activity timestamp for each player in a room.
    Returns a dict mapping player_id to the activity timestamp (or None if no activity)."""
    player_activity: Dict[int, Optional[float]] = {}
    
    if not room.multisave:
        for slot in room.seed.slots:
            player_activity[slot.player_id] = None
        return player_activity
    
    try:
        multisave = restricted_loads(room.multisave)
        client_activity_timers = multisave.get("client_activity_timers", [])
        
        # Initialize all players to None
        for slot in room.seed.slots:
            player_activity[slot.player_id] = None
        
        # client_activity_timers is stored as tuple of ((team, player), timestamp) pairs
        # Handle both tuple and list formats
        if isinstance(client_activity_timers, (tuple, list)):
            for entry in client_activity_timers:
                if isinstance(entry, (tuple, list)) and len(entry) == 2:
                    (team, player_id), timestamp = entry
                    if player_id in player_activity:
                        if player_activity[player_id] is None or timestamp > player_activity[player_id]:
                            player_activity[player_id] = timestamp
    except Exception:
        for slot in room.seed.slots:
            player_activity[slot.player_id] = None
    
    return player_activity


@api_endpoints.route('/monitoring/rooms')
def monitoring_rooms() -> Dict[str, Any]:
    """Get a list of all active rooms with port and last activity time."""
    require_admin_token()
    with db_session:
        now = utcnow()
        rooms = select(
            room for room in Room if
            room.last_activity >= now - timedelta(days=3)
        )
        
        active_rooms = []
        for room in rooms:
            if is_room_active(room):
                player_activity = get_per_player_last_activity(room)
                games = []
                for slot in room.seed.slots:
                    activity_timestamp = player_activity.get(slot.player_id)
                    games.append({
                        "game": slot.game,
                        "player_id": slot.player_id,
                        "player_name": slot.player_name,
                        "last_activity_timestamp": datetime.fromtimestamp(activity_timestamp, tz=timezone.utc).isoformat() if activity_timestamp else None,
                    })
                
                active_rooms.append({
                    "room_id": str(room.id),
                    "room_id_short": to_url(room.id),
                    "port": room.last_port,
                    "last_activity_timestamp": room.last_activity.isoformat(),
                    "time_until_timeout": int(room.timeout - (now - room.last_activity).total_seconds()),
                    "games": games,
                    "player_count": len(room.seed.slots),
                    "creation_time": room.creation_time.isoformat(),
                })
        
        return jsonify({
            "active_rooms": active_rooms,
            "total_active_rooms": len(active_rooms),
            "timestamp": now.isoformat(),
        })


@api_endpoints.route('/monitoring/games')
def monitoring_games() -> Dict[str, Any]:
    """Get a list of all games with port and time of last action."""
    require_admin_token()
    with db_session:
        now = utcnow()
        rooms = select(
            room for room in Room if
            room.last_activity >= now - timedelta(days=3)
        )

        games_dict: Dict[str, List[Dict[str, Any]]] = {}
        
        for room in rooms:
            if not is_room_active(room):
                continue

            player_activity = get_per_player_last_activity(room)
            
            for slot in room.seed.slots:
                game = slot.game
                if game not in games_dict:
                    games_dict[game] = []
                
                activity_timestamp = player_activity.get(slot.player_id)
                
                games_dict[game].append({
                    "room_id": str(room.id),
                    "room_id_short": to_url(room.id),
                    "port": room.last_port,
                    "last_activity_timestamp": room.last_activity.isoformat(),
                    "game_last_activity_timestamp": datetime.fromtimestamp(activity_timestamp, tz=timezone.utc).isoformat() if activity_timestamp else None,
                    "player_name": slot.player_name,
                    "player_id": slot.player_id,
                    "time_until_timeout": int(room.timeout - (now - room.last_activity).total_seconds()),
                })
        
        # Resolve module slug -> index metadata outside the inner loop for efficiency.
        # The slug is the AutoWorldRegister module name with the "worlds." prefix stripped.
        from worlds.AutoWorld import AutoWorldRegister
        slug_cache: Dict[str, Dict[str, Any]] = {}
        for game in games_dict:
            world_type = AutoWorldRegister.world_types.get(game)
            if world_type is not None:
                module = world_type.__module__
                slug = module.split(".")[-1] if "." in module else module
            else:
                slug = game.lower().replace(" ", "_")
            slug_cache[game] = _get_index_metadata(slug)

        games_list = [
            {
                "game": game,
                "active_instances": instances,
                "instance_count": len(instances),
                # Distribution provenance — null until per-world splits land.
                "upstream_repo_url": slug_cache[game]["upstream_repo_url"],
                "release_ref": slug_cache[game]["release_ref"],
                "entry_point_module": slug_cache[game]["entry_point_module"],
            }
            for game, instances in sorted(games_dict.items())
        ]

        return jsonify({
            "games": games_list,
            "total_games": len(games_dict),
            "total_instances": sum(len(instances) for instances in games_dict.values()),
            "timestamp": now.isoformat(),
        })


@api_endpoints.route('/monitoring/broadcast', methods=['POST'])
def broadcast() -> Dict[str, Any]:
    """Send a message to all active rooms (or specific ones)."""
    require_admin_token()
    
    data = request.get_json()
    if not data or "message" not in data:
        abort(400, description="Message is required")
        
    message = data["message"]
    room_ids = data.get("rooms") # optional
    
    with db_session:
        now = utcnow()
        
        if room_ids:
            try:
                room_uuids = [UUID(rid) for rid in room_ids]
            except ValueError:
                abort(400, description="Invalid room ID format")
                
            rooms = select(
                room for room in Room if room.id in room_uuids
            )
        else:
            # Default to all active rooms
            # Same criteria as monitoring_rooms + is_room_active check
            candidates = select(
                room for room in Room if
                room.last_activity >= now - timedelta(days=3)
            )
            rooms = [r for r in candidates if is_room_active(r)]
            
        count = 0
        for room in rooms:
            Command(room=room, commandtext=message)
            count += 1
            
        return jsonify({
            "message": f"Broadcast sent to {count} rooms",
            "count": count,
            "timestamp": now.isoformat(),
        })


@api_endpoints.route('/monitoring/index')
def monitoring_index() -> Dict[str, Any]:
    """Admin diagnostic: full index metadata for all loaded games.

    Returns one entry per loaded world (keyed by game display name) containing
    the three new distribution fields.  All three are null until the
    mwgg-igdb-index package upgrade ships individual per-world entries.
    Requires admin token.
    """
    require_admin_token()
    from worlds.AutoWorld import AutoWorldRegister

    result: Dict[str, Any] = {}
    for game_name, world_type in sorted(AutoWorldRegister.world_types.items()):
        module = world_type.__module__
        slug = module.split(".")[-1] if "." in module else module
        meta = _get_index_metadata(slug)
        result[game_name] = {
            "slug": slug,
            **meta,
        }

    return jsonify({
        "games": result,
        "game_count": len(result),
        "timestamp": utcnow().isoformat(),
    })
