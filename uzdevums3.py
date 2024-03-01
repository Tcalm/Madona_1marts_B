import json

with open('uzd3.json', 'r') as f:
    data = json.load(f)

print("Vārds: ", data["name"])
print("Vecums: ", data["age"])
print("Pilsēta: ", data["city"])