from flask import Flask, request, jsonify
import os
import requests  # Changed from request to requests
import json
import importlib.util
from typing import Dict, Optional, Tuple
from datetime import datetime
import sys
import re

# Get the user's home directory and convert to forward slashes
home_dir = os.path.expanduser('~').replace('\\', '/')
client_id_path = f"{home_dir}/.igdb/clientid"
key_path = f"{home_dir}/.igdb/key"

with open(client_id_path, 'r') as file:
    igdb_client_id = file.readline().strip()
with open(key_path, 'r') as file:
    igdb_key = file.readline().strip()

# url = f"https://id.twitch.tv/oauth2/token?client_id={igdb_client_id}&client_secret={igdb_key}&grant_type=client_credentials"
# response = requests.post(url)
# print(url)
# print(response.json())
# igdb_token = response.json()['access_token']
igdb_token = "ok558j0ne651nzmks56bnfp54apy5j"


def get_igdb_game_keywords(game_id: int) -> list:
    """
    Fetches game keywords from IGDB API using the provided game name.
    """
    url = "https://api.igdb.com/v4/keywords"
    headers = {
        'Client-ID': igdb_client_id,
        'Authorization': f'Bearer {igdb_token}',
        'Content-Type': 'application/json'
    }
    data = f'fields name; search "{game_id}"; limit 10;'
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        return [keyword['name'] for keyword in response.json()]
    else:
        return []

def get_igdb_game_cover(game_id: int) -> str:
    """
    Fetches game cover image URL from IGDB API using the provided game name.
    """
    url = "https://api.igdb.com/v4/covers"
    headers = {
        'Client-ID': igdb_client_id,
        'Authorization': f'Bearer {igdb_token}',
        'Content-Type': 'application/json'
    }
    data = f'fields url; search "{game_id}"; limit 1;'
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        return response.json()[0]['url']
    else:
        return None

def get_game_and_igdb_id_from_world(init_path: str) -> Optional[Tuple[str, int]]:
    """
    Gets the game name and IGDB ID from a world's __init__.py file by looking for the values directly.
    Returns a tuple of (game_name, igdb_id) or None if not found.
    """
    if not os.path.exists(init_path):
        return None
        
    try:
        # Read the file content
        with open(init_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Look for game name - can be defined in various ways
        game_patterns = [
            r'game\s*=\s*["\']([^"\']+)["\']',  # game = "name"
            r'game\s*:\s*[^=]*=\s*["\']([^"\']+)["\']',  # game: str = "name" or game: ClassVar[str] = "name"
            r'game\s*:\s*[^=]*=\s*(\w+)\.GAME_NAME',  # game: str = Constants.GAME_NAME
            r'game\s*=\s*(\w+)\.GAME_NAME',  # game = Constants.GAME_NAME
            r'game\s*=\s*(\w+)\.game_name',  # game = OTHER.game_name
        ]
        
        # Look for igdb_id - can be defined in various ways
        id_patterns = [
            r'igdb_id\s*=\s*(\d+)',  # igdb_id = 123
            r'igdb_id\s*:\s*[^=]*=\s*(\d+)',  # igdb_id: int = 123 or igdb_id: ClassVar[int] = 123
            r'igdb_id\s*:\s*[^=]*=\s*(\w+)\.IGDB_ID',  # igdb_id: int = Constants.IGDB_ID
            r'igdb_id\s*=\s*(\w+)\.IGDB_ID',  # igdb_id = Constants.IGDB_ID
            r'igdb_id\s*=\s*(\w+)\.igdb_id',  # igdb_id = OTHER.igdb_id
        ]
        
        # Try each pattern for game name
        game_name = None
        for pattern in game_patterns:
            match = re.search(pattern, content)
            if match:
                if '.' in match.group(1):  # It's a constant reference
                    # Look for the constant in the same directory
                    const_name = match.group(1).split('.')[0]
                    # Try different possible constant file names
                    const_files = [
                        os.path.join(os.path.dirname(init_path), f"{const_name.lower()}.py"),
                        os.path.join(os.path.dirname(init_path), "constants.py"),
                        os.path.join(os.path.dirname(init_path), "data", "strings.py"),
                        os.path.join(os.path.dirname(init_path), "data", "strings", "other.py"),
                    ]
                    for const_file in const_files:
                        if os.path.exists(const_file):
                            with open(const_file, 'r', encoding='utf-8') as f:
                                const_content = f.read()
                                # Try different patterns for the constant
                                const_patterns = [
                                    r'GAME_NAME\s*:\s*str\s*=\s*["\']([^"\']+)["\']',  # In class
                                    r'game_name\s*:\s*str\s*=\s*["\']([^"\']+)["\']',  # In class
                                    r'GAME_NAME\s*=\s*["\']([^"\']+)["\']',  # Global
                                    r'game_name\s*=\s*["\']([^"\']+)["\']',  # Global
                                    r'GAME_NAME\s*:\s*str\s*=\s*["\']([^"\']+)["\']',  # In dataclass
                                    r'game_name\s*:\s*str\s*=\s*["\']([^"\']+)["\']',  # In dataclass
                                ]
                                for const_pattern in const_patterns:
                                    const_match = re.search(const_pattern, const_content)
                                    if const_match:
                                        game_name = const_match.group(1)
                                        break
                                if game_name:
                                    break
                else:
                    game_name = match.group(1)
                if game_name:
                    break
                
        # Try each pattern for igdb_id
        igdb_id = None
        for pattern in id_patterns:
            match = re.search(pattern, content)
            if match:
                if '.' in match.group(1):  # It's a constant reference
                    # Look for the constant in the same directory
                    const_name = match.group(1).split('.')[0]
                    # Try different possible constant file names
                    const_files = [
                        os.path.join(os.path.dirname(init_path), f"{const_name.lower()}.py"),
                        os.path.join(os.path.dirname(init_path), "constants.py"),
                        os.path.join(os.path.dirname(init_path), "data", "strings.py"),
                        os.path.join(os.path.dirname(init_path), "data", "strings", "other.py"),
                    ]
                    for const_file in const_files:
                        if os.path.exists(const_file):
                            with open(const_file, 'r', encoding='utf-8') as f:
                                const_content = f.read()
                                # Try different patterns for the constant
                                const_patterns = [
                                    r'IGDB_ID\s*:\s*int\s*=\s*(\d+)',  # In class
                                    r'igdb_id\s*:\s*int\s*=\s*(\d+)',  # In class
                                    r'IGDB_ID\s*=\s*(\d+)',  # Global
                                    r'igdb_id\s*=\s*(\d+)',  # Global
                                    r'IGDB_ID\s*:\s*int\s*=\s*(\d+)',  # In dataclass
                                    r'igdb_id\s*:\s*int\s*=\s*(\d+)',  # In dataclass
                                ]
                                for const_pattern in const_patterns:
                                    const_match = re.search(const_pattern, const_content)
                                    if const_match:
                                        try:
                                            igdb_id = int(const_match.group(1))
                                            break
                                        except ValueError:
                                            continue
                                if igdb_id is not None:
                                    break
                else:
                    try:
                        igdb_id = int(match.group(1))
                    except ValueError:
                        continue
                if igdb_id is not None:
                    break
                
        if game_name and igdb_id is not None:
            return game_name, igdb_id
                
    except Exception as e:
        print(f"Error loading {init_path}: {e}")
        return None
    
    return None

def get_game_ids_from_worlds() -> dict:
    """
    Gets IGDB game IDs for all games in the worlds directory.
    Returns a dictionary mapping game names to their IGDB IDs.
    """
    # Get all world directories from base_world_inits.txt
    with open("world_inits.txt", "r") as f:
        base_world_inits = f.read().splitlines()
    
    game_ids = {}

    for init_file in base_world_inits:
        print(f"\nProcessing file: {init_file}")
        if not os.path.exists(init_file):
            print(f"No file found at {init_file}")
            continue
            
        # Get game name and IGDB ID from the World class
        result = get_game_and_igdb_id_from_world(init_file)
        if not result:
            print(f"Could not find World class with game and igdb_id in {init_file}")
            continue
            
        game_name, igdb_id = result
        game_ids[game_name] = igdb_id
    return game_ids

def get_igdb_game_details(game_id: int) -> dict:
    """
    Fetches detailed game information from IGDB API including name, rating, themes, and keywords.
    """
    url = "https://api.igdb.com/v4/games"
    headers = {
        'Client-ID': igdb_client_id,
        'Authorization': f'Bearer {igdb_token}',
        'Content-Type': 'application/json'
    }
    data = f'''
    fields name, cover.url, age_ratings.organization.name, age_ratings.rating_content_descriptions.description, first_release_date, player_perspectives.name,genres.name, themes.name, keywords.name;
    where id = {game_id};
    '''
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code != 200 or not response.json():
        return {}
        
    game_data = response.json()[0]
    
    # Extract content descriptions from age ratings
    content_descriptions = []
    for rating in game_data.get('age_ratings', []):
        if 'rating_content_descriptions' in rating and 'organization' in rating:
            if rating['organization']['name'] == 'ESRB':
                for desc in rating['rating_content_descriptions']:
                    if 'description' in desc:
                        content_descriptions.append(desc['description'])

    return {
        'igdb_name': game_data.get('name', ''),
        'cover_url': game_data.get('cover', {}).get('url', ''),
        'rating': content_descriptions,
        'themes': [theme['name'] for theme in game_data.get('themes', [])],
        'player_perspectives': [perspective['name'] for perspective in game_data.get('player_perspectives', [])],
        'genres': [genre['name'] for genre in game_data.get('genres', [])],
        'release_date': game_data.get('first_release_date', ''),
        'keywords': [keyword['name'] for keyword in game_data.get('keywords', [])]
    }

def generate_game_details_json() -> dict:
    """
    Generates a JSON structure containing game details from both the world files and IGDB.
    For worlds without IGDB IDs, creates an empty entry with just the world name.
    """
    # Get all directory names from worlds folder
    game_ids = get_game_ids_from_worlds()

    result = {}
    
    for game_name, igdb_id in game_ids.items():

        if igdb_id:
            # Get IGDB details for worlds with IGDB IDs
            igdb_details = get_igdb_game_details(igdb_id)
            
            # Create the game entry with IGDB data
            result[game_name] = {
                'igdb_id': str(igdb_id),
                'cover_url': igdb_details.get('cover_url', ''),
                'world_name': game_name,
                'igdb_name': igdb_details.get('igdb_name', ''),
                'rating': igdb_details.get('rating', ''),
                'player_perspectives': igdb_details.get('player_perspectives', []),
                'genres': igdb_details.get('genres', []),
                'themes': igdb_details.get('themes', []),
                'keywords': igdb_details.get('keywords', []),
                'release_date': igdb_details.get('release_date', '')
            }
        else:
            # Create empty entry for worlds without IGDB IDs
            result[game_name] = {
                'igdb_id': '',
                'world_name': game_name,
                'igdb_name': '',
                'rating': '',
                'player_perspectives': [],
                'genres': [],
                'themes': [],
                'keywords': [],
                'release_date': ''
            }
            print(f"Created empty entry for {game_name} (no IGDB ID)")
    
    return result

def get_single_game_details(igdb_id: int) -> dict:
    """
    Gets details for a single game by its IGDB ID.
    Returns a dictionary with the same structure as the full JSON output.
    """
    # Get IGDB details
    igdb_details = get_igdb_game_details(igdb_id)
    
    if not igdb_details:
        return {
            'igdb_id': str(igdb_id),
            'world_name': '',  # We don't know the world name for a single ID lookup
            'igdb_name': '',
            'us_rating': '',
            'player_perspectives': [],
            'genres': [],
            'themes': [],
            'keywords': [],
            'release_date': ''
        }
    
    return {
        'igdb_id': str(igdb_id),
        'cover_url': igdb_details.get('cover_url', ''),
        'world_name': '',  # We don't know the world name for a single ID lookup
        'igdb_name': igdb_details.get('igdb_name', ''),
        'rating': igdb_details.get('rating', ''),
        'player_perspectives': igdb_details.get('player_perspectives', []),
        'genres': igdb_details.get('genres', []),
        'themes': igdb_details.get('themes', []),
        'keywords': igdb_details.get('keywords', []),
        'release_date': igdb_details.get('release_date', '')
    }

def save_game_details_to_json(single_id: Optional[int] = None):
    """
    Saves the game details to a JSON file.
    If single_id is provided, only saves details for that specific game.
    """
    if single_id is not None:
        game_details = get_single_game_details(single_id)
    else:
        game_details = generate_game_details_json()
        
    output_path = os.path.join(os.path.dirname(__file__), 'output', 'game_details.json')
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(game_details, f, indent=4)

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate game details JSON from IGDB')
    parser.add_argument('--id', type=int, help='Get details for a single game by IGDB ID')
    args = parser.parse_args()
    
    save_game_details_to_json(args.id)