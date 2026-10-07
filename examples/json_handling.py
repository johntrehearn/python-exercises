import json

save_data = {
    "player": "Ben",
    "level": 10,
    "item": ["sword", "potion"]
}

with open("saveJSONdata.json", "w") as file:
    json.dump(save_data, file)

with open("saveJSONdata.json", "r") as file:
    file_data = json.load(file)
    print(f"Player: {file_data["player"]}")
    print(f"Level: {file_data["level"]}")
    print(f"Items: {file_data['item']}")
    for item in file_data["item"]:
        print(item) 