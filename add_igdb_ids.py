import os
import json
from igdb import get_game_ids_from_worlds

def add_igdb_ids_to_worlds():
    # Get the game IDs
    game_ids = get_game_ids_from_worlds()
    
    # Get all world directories
    with open("base_world_inits.txt", "r") as f:
        base_world_inits = f.read().splitlines()
    
    for init_file in base_world_inits:
        print(f"\nProcessing file: {init_file}")
        if not os.path.exists(init_file):
            print(f"No __init__.py found in {init_file}")
            continue
            
        # Read the file content
        with open(init_file, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"Successfully read file: {init_file}")
            print("Original content preview:")
            print(content[:200] + "...")
            
        # Check if igdb_id is already set
        if 'igdb_id' in content:
            print(f"IGDB ID already set in {init_file}")
            continue
            
        # Find the World subclass and game name
        lines = content.split('\n')
        game_name = None
        world_class_line = -1
        game_line_index = -1
        
        for i, line in enumerate(lines):
            if 'class' in line and '(World)' in line:
                world_class_line = i
                print(f"Found World class at line {i}: {line.strip()}")
                # Look for game definition in the next few lines
                for j in range(i + 1, min(i + 20, len(lines))):
                    if 'game:' in lines[j] or 'game =' in lines[j]:
                        game_name = lines[j].split('=')[1].strip().strip('"\'')
                        game_line_index = j
                        print(f"Found game line at {j}: {lines[j].strip()}")
                        break
                break
                
        if not game_name:
            print(f"No game name found in {init_file}")
            continue
            
        # Get the IGDB ID
        if game_name not in game_ids:
            print(f"No IGDB ID found for {game_name}")
            continue
            
        # Add the IGDB ID
        igdb_id = game_ids[game_name]
        print(f"Found IGDB ID {igdb_id} for {game_name}")
        
        if game_line_index == -1:
            print(f"Could not find game line in {init_file}")
            continue
            
        # Add the igdb_id after the game line
        new_line = f'    igdb_id = {igdb_id}'
        lines.insert(game_line_index + 1, new_line)
        print(f"Inserted line: {new_line}")
        
        # Write the updated content
        try:
            with open(init_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            print(f"Successfully wrote updated content to {init_file}")
            
            # Verify the write
            with open(init_file, 'r', encoding='utf-8') as f:
                new_content = f.read()
                print("New content preview:")
                print(new_content[:200] + "...")
                if f'igdb_id = {igdb_id}' not in new_content:
                    print("WARNING: igdb_id not found in file after writing!")
                    print("Full new content:")
                    print(new_content)
                
        except Exception as e:
            print(f"Error writing to file {init_file}: {str(e)}")
            
        print(f"Added IGDB ID {igdb_id} to {game_name}")

if __name__ == '__main__':
    add_igdb_ids_to_worlds() 