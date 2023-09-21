import json

with open("data.json") as f:
    data = json.load(f)

for states in data["states"]:
    print(states["name"])