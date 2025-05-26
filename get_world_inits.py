import os
import re

def find_world_init_files():
    # Patterns to match the two possible import statements with optional space
    patterns = [
        r'from worlds.AutoWorld import World\s?,\s?WebWorld',
        r'from worlds.AutoWorld import WebWorld\s?,\s?World'
    ]
    
    # Compile the patterns for better performance
    compiled_patterns = [re.compile(pattern) for pattern in patterns]
    
    # List to store the paths of files containing the imports
    world_init_files = []
    
    # Walk through the worlds directory
    for root, dirs, files in os.walk('worlds'):
        # Skip the worlds directory itself
        if root == 'worlds':
            continue
            
        # Look for files in the current directory
        found_match = False
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Check if any of the patterns match
                        if any(pattern.search(content) for pattern in compiled_patterns):
                            world_init_files.append(os.path.abspath(file_path))
                            found_match = True
                            break
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
        
        # If we found a match in this directory, we can stop looking
        if found_match:
            continue
    
    # Write the results to world_inits.txt
    with open('world_inits.txt', 'w', encoding='utf-8') as f:
        for file_path in world_init_files:
            f.write(f"{file_path}\n")

if __name__ == "__main__":
    find_world_init_files()
