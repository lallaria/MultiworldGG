import os
import json

with open(os.path.join(os.path.abspath("tools"), "output", "game_details.json"), "r") as f:
    game_index = json.load(f)

worldsdir = os.path.abspath("worlds")
for file in os.listdir(worldsdir):
    if os.path.exists(f"{worldsdir}/{file}/Constants.py"):
        with open(f"{worldsdir}/{file}/Constants.py", "r") as f:
            data = f.readlines()
            for index, line in enumerate(data):
                if "GAME_NAME" in line:
                    game_index[file]["game_name"] = line.split("=")[1].strip().rstrip("\"").lstrip("\"")
                    print(line)
                    break
    elif os.path.exists(f"{worldsdir}/{file}/constants.py"):
        with open(f"{worldsdir}/{file}/constants.py", "r") as f:
            data = f.readlines()
            for index, line in enumerate(data):
                if "GAME_NAME" in line:
                    game_index[file]["game_name"] = line.split("=")[1].strip().rstrip("\"").lstrip("\"")
                    print(line)
                    break
with open(os.path.join(os.path.abspath("tools"), "output", "game_details.json"), "w") as f:
    json.dump(game_index, f, indent=4)