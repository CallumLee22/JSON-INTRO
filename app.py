import json

with open("hierarchy.json") as f: 
    hierarchy = json.load(f)

print(hierarchy[0]["contents"][3]["name"])