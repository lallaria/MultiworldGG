import os
import sys
import json

with open(os.path.join(os.path.abspath("tools"), "output", "game_details.json"), "r") as f:
    game_index = json.load(f)

worldsdir = os.path.abspath("worlds")
for file in os.listdir(worldsdir):
    try:
        if os.path.exists(f"{worldsdir}/{file}/pyproject.toml"):
            with open(f"{worldsdir}/{file}/pyproject.toml", "r") as f:
                data = f.readlines()
                for index, line in enumerate(data):
                    if "description" in line:
                        data[index] = f'description = "MultiWorld: {game_index[file]["game_name"]}"\n'
                        print(game_index[file]["game_name"])
                        break
                with open(f"{worldsdir}/{file}/pyproject.toml", "w") as f:
                    f.writelines(data)
    except:
        continue