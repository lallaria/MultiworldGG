import json
from pathlib import Path
from typing import Dict, Set, Any

def clean_value(value: Any) -> str:
    """
    Clean a value for indexing, converting null/None to empty string
    and ensuring we have a string value.
    
    Args:
        value: The value to clean
        
    Returns:
        Cleaned string value
    """
    if value is None:
        return ""
    return str(value).lower()

def clean_game_data(games_data: dict) -> dict:
    """
    Clean the game data, ensuring no null values and proper types.
    Preserves original world_name as it's used for identification.
    
    Args:
        games_data: Raw game data dictionary
        
    Returns:
        Cleaned game data dictionary
    """
    cleaned_data = {}
    for game_name, game_data in games_data.items():
        cleaned_game = {}
        for field, value in game_data.items():
            # Preserve original world_name
            if field == "world_name":
                cleaned_game[field] = value
            elif value is None:
                cleaned_game[field] = ""
            elif isinstance(value, list):
                cleaned_game[field] = [clean_value(item) for item in value]
            elif isinstance(value, dict):
                cleaned_game[field] = {k: clean_value(v) for k, v in value.items()}
            else:
                cleaned_game[field] = clean_value(value)
        cleaned_data[game_name] = cleaned_game
    return cleaned_data

def build_search_index(games_data: dict) -> Dict[str, Set[str]]:
    """
    Build the search index from game data.
    
    Args:
        games_data: Dictionary of game data from game_details.json
        
    Returns:
        Dictionary mapping search terms to sets of game names
    """
    search_index = {}
    
    for game_name, game_data in games_data.items():
        # Index game name
        _add_to_index(search_index, game_name, game_name)
        
        # Index all fields except world_name (which we'll index separately)
        for field, value in game_data.items():
            if field == "world_name":
                continue
                
            if isinstance(value, list):
                for item in value:
                    if item:  # Only index non-empty values
                        _add_to_index(search_index, clean_value(item), game_name)
            elif isinstance(value, (str, int, float, bool)):
                if value:  # Only index non-empty values
                    _add_to_index(search_index, clean_value(value), game_name)
            elif isinstance(value, dict):
                for k, v in value.items():
                    if k:  # Only index non-empty keys
                        _add_to_index(search_index, clean_value(k), game_name)
                    if v:  # Only index non-empty values
                        _add_to_index(search_index, clean_value(v), game_name)
    
    return search_index

def _add_to_index(index: Dict[str, Set[str]], term: str, game_name: str) -> None:
    """
    Add a term to the search index.
    
    Args:
        index: The search index dictionary
        term: The term to index
        game_name: The name of the game this term is associated with
    """
    term = clean_value(term)
    if term:  # Only index non-empty terms
        if term not in index:
            index[term] = set()
        index[term].add(game_name)

def validate_generated_index(games_data: dict, search_index: Dict[str, Set[str]]) -> bool:
    """
    Validate the generated index to ensure all games are properly indexed.
    
    Args:
        games_data: The original game data
        search_index: The generated search index
        
    Returns:
        True if validation passes, False otherwise
    """
    # Check that all game names are in the index
    for game_name in games_data:
        if game_name not in search_index.get(game_name.lower(), set()):
            print(f"Warning: Game name '{game_name}' not properly indexed")
            return False
    
    # Check that all indexed terms point to valid games
    for term, games in search_index.items():
        for game in games:
            if game not in games_data:
                print(f"Warning: Invalid game reference '{game}' in term '{term}'")
                return False
    
    return True

def generate_index_file():
    """Generate the game_index.py file with pre-built index."""
    try:
        # Load game data
        with open("game_details.json", "r", encoding="utf-8") as file:
            games_data = json.load(file)
        
        # Clean the game data
        games_data = clean_game_data(games_data)
        
        # Build search index
        search_index = build_search_index(games_data)
        
        # Validate the generated index
        if not validate_generated_index(games_data, search_index):
            print("Warning: Index validation failed, but continuing with generation")
        
        # Convert sets to lists for JSON serialization
        search_index_json = {k: list(v) for k, v in search_index.items()}
        
        # Generate Python code
        games_data_str = json.dumps(games_data, indent=4)
        search_index_str = json.dumps(search_index_json, indent=4)
        
        # Read template
        template_path = Path("tools/game_index_template.py")
        with open(template_path, "r") as f:
            template = f.read()
        
        # Fill template with explicit placeholder names
        code = template.replace("GAMES_DATA_PLACEHOLDER", games_data_str)
        code = code.replace("SEARCH_INDEX_PLACEHOLDER", search_index_str)
        
        # Write generated file
        output_path = Path("data/game_index.py")
        with open(output_path, "w") as f:
            f.write(code)
        
        print(f"Generated game index with {len(games_data)} games and {len(search_index)} search terms")
        
    except FileNotFoundError as e:
        print(f"Error: Could not find required file: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in game_details.json: {e}")
        return False
    except Exception as e:
        print(f"Error: Unexpected error during index generation: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = generate_index_file()
    if not success:
        exit(1) 