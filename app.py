import json

with open("data.json") as f:
    data = json.load(f)

for states in data["states"]:
    print(states["name"])

for states in data["states"]:
    del states["area_codes"]

with open("new_states.json", "w") as f:
    json.dump(data, f, indent=2)