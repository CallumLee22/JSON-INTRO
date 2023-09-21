import json

with open("data.json") as f:
    data = json.load(f)

for states in data["states"]:
    print(states["name"])

for states in data["states"]:
    del states["area_codes"]

with open("no_area_code_states.json", "w") as f:
    json.dump(data, f, indent=2)

for states in data["states"]:
    del states["name"]

with open("no_name_states.json", "w") as f:
    json.dump(data, f, indent=2)

for states in data["states"]:
    del states["abbreviation"]

with open("no_abbreviation_states.json", "w") as f:
    json.dump(data, f, indent=2)