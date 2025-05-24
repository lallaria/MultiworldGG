import json
import os
from igdb import get_game_ids_from_worlds

def test_get_game_ids():
    """
    Test function that gets game IDs and saves them to a JSON file.
    """
    # Get the game IDs
    game_ids = get_game_ids_from_worlds()
    
    # Create output directory if it doesn't exist
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Save to JSON file
    output_file = os.path.join(output_dir, "game_ids.json")
    with open(output_file, 'w') as f:
        json.dump(game_ids, f, indent=2)
    
    print(f"Found {len(game_ids)} game IDs")
    print(f"Results saved to {output_file}")
    
    # Basic validation
    assert isinstance(game_ids, dict), "Result should be a dictionary"
    assert all(isinstance(v, int) for v in game_ids.values()), "All values should be integers"
    assert all(isinstance(k, str) for k in game_ids.keys()), "All keys should be strings"

if __name__ == "__main__":
    test_get_game_ids() 