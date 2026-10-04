import json
from game_classes import Item, Player, Room
from menu import gameMenu

SAVE_FILE = "save.json"

def collect_item(player, room):
    if room.item is not None:
        collected_item = room.item
        collectChoice = input(
            f"You found a {collected_item.name}. Would you like to keep it? (yes/no): ")
        if collectChoice in ("yes", "y"):
            player.inventory.append(collected_item)
            print(f"\nYou have collected the {collected_item.name}. It has been added to your inventory.\n")
        else:
            print(f"\nYou dropped the {collected_item.name}.\n")
    else:
        print("Nothing to collect here. Keep looking.")

def player_move(player, rooms):
    current_room_index = rooms.index(player.location)
    if current_room_index < len(rooms) - 1:
        player.location = rooms[current_room_index + 1]
        print(f"\nYou are currently in {player.location.name}.\n")
        collect_item(player, player.location)
    else:
        print("\nYou escaped the castle.")

def display_inventory(inventory):
    print("\nYour current inventory is:")
    for item in inventory:
        print(item.name)

def carbon_calc(inventory):
    carbon_emissions = len(inventory) * 551
    print(f"\nYour inventory's production emissions are {carbon_emissions}g Carbon Dioxide.")

def save_game(player):
    save_data = {
        "name": player.name,
        "location": player.location.name,
        "inventory": [{"name": item.name, "weight": item.weight} for item in player.inventory],
    }
    with open(SAVE_FILE, "w") as save_file:
        json.dump(save_data, save_file)
    print("\nGame saved.")

def load_game(player, rooms):
    try:
        with open(SAVE_FILE) as save_file:
            save_data = json.load(save_file)
    except FileNotFoundError:
        print("\nNo saved game found.")
        return

    player.name = save_data["name"]
    player.inventory = [
        Item(item["name"], item["weight"])
        for item in save_data["inventory"] ]
    for room in rooms:
        if room.name == save_data["location"]:
            player.location = room
            break
    print("\nGame loaded.\n")

def start_game(player_name):
    map_item = Item("Map", 1)
    crossbow = Item("Crossbow", 5)
    sword = Item("Steel Sword", 3)
    shield = Item("Steel Shield", 4)
    paper_shield = Item("Paper Shield", 1)
    pizza = Item("Pizza", 2)
    potion = Item("Potion", 1)
    master_sword = Item("Master Sword", 10)
    hall = Room("Hall", map_item)
    rooms = (
        hall,
        Room("Room 1", pizza),
        Room("Room 2", None),
        Room("Room 3", shield),
        Room("Room 4", None),
        Room("Room 5", sword),
        Room("Room 6", crossbow),
        Room("Room 7", None),
        Room("Room 8", potion),
        Room("Room 9", None),
        Room("Room 10", master_sword),
    )
    return Player(player_name, [paper_shield], hall), rooms

def gameStart():
    print("\n\n** Castle Adventure Game **\n")
    player_name = input("\nPlease enter your name: ")
    player_age = int(input("\nPlease enter your age: "))
    gameMenu(
        player_name,
        player_age,
        start_game,
        player_move,
        display_inventory,
        carbon_calc,
        save_game,
        load_game,
    )


gameStart()