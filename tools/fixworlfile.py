import os
import sys

for file in os.listdir("worlds"):
    try:
        if os.path.exists(f"worlds/{file}/Client.py"):
            with open(f"worlds/{file}/Client.py", "r") as f:
                data = f.readlines()
                for index, line in enumerate(data):
                    if "license_files" in line:
                        data.pop(index)
                        data.pop(index)
                        data.pop(index)
                    
                with open(f"worlds/{file}/pyproject.toml", "w") as f:
                    f.writelines(data)
    except:
        continue
