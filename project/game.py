import json
import random
from game_classes import Item, Player, Room
from menu import gameMenu
import os

SAVE_FILE = "save.json"

# Function to collect room item

def collect_item(player, room):
    if room.item is not None:
        collected_item = room.item
        keepItem = input(
            f"You found a {collected_item.name}. Would you like to keep it? (yes/no): ")
        if keepItem in ("yes", "y"):
            player.inventory.append(collected_item)
            print(f"\nYou have collected the {collected_item.name}. It has been added to your inventory.\n")
        else:
            print(f"\nYou dropped the {collected_item.name}.\n")
    else:
        print("Nothing to collect here. Keep looking.")

# Function to check if player has the 3 items needed to open the final door (Potion, Steel Sword and Steel Shield)
# If not it teleports them back to a random room in the castle

def escape_castle(player, inventory, rooms):
    required_items = {"Potion", "Steel Sword", "Steel Shield"}
    inventory_items = {item.name for item in inventory}
    if required_items <= inventory_items:
        print("\n****You have escaped the castle****\n\n ****Congratulation****")
        carbon_calc(inventory)
        exit()
    else:
        print("\nYou cannot open the door. There are pedestals with pictures of a Potion, Steel Sword, and Steel Shield on them....\n")
        print("\nA strange blue light appears you seems to be teleporting back into the castle.....\n\n")
        player.location = random.choice(rooms)
        print(f"You are currently in {player.location.name}.\n")
        collect_item(player, player.location)

# Player move Left - in effect it just moves the player on one

def player_moveL(player, rooms):
    current_room_index = rooms.index(player.location)
    if current_room_index < len(rooms) - 1:
        player.location = rooms[current_room_index + 1]
        print(f"\nYou are currently in {player.location.name}.\n")
        collect_item(player, player.location)
    else:
        escape_castle(player, player.inventory, rooms)

# Player move Right - in effect it moves them on by a random number

def player_moveR(player, rooms):
    current_room_index = rooms.index(player.location)
    if current_room_index < len(rooms) - 1:
        player.location = rooms[random.randint(current_room_index + 1, len(rooms) - 1)]
        print(f"\nYou are currently in {player.location.name}.\n")
        collect_item(player, player.location)
    else:
        escape_castle(player, player.inventory, rooms)

# Player move Back - in effect it moves them back one room (but not back necessarily to the previous room)

def player_moveB(player, rooms):
    current_room_index = rooms.index(player.location)
    if current_room_index > 0:
        player.location = rooms[current_room_index - 1]
        print(f"\nYou are currently in {player.location.name}.\n")
        collect_item(player, player.location)
    else:
        escape_castle(player, player.inventory, rooms)

# Function to display the inventory

def display_inventory(inventory):
    print("\nYour current inventory is:")
    for item in inventory:
        print(item.name)

# Calculate the carbon emissions of the items in the inventory.

def carbon_calc(inventory):
    carbon_emissions = len(inventory) * 551
    print(f"\nYour inventory's production emissions are {carbon_emissions}g Carbon Dioxide.\n\n")

# Function to save the game. Saves the name, weight and inventory to a json file.

def save_game(player):
    save_data = {
        "name": player.name,
        "location": player.location.name,
        "inventory": [{"name": item.name, "weight": item.weight} for item in player.inventory],
    }
    with open(SAVE_FILE, "w") as save_file:
        json.dump(save_data, save_file)
    print("\nGame saved.")

# Function to load the game. Loads from a json file or shows a error message.

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


# Function to create the map it creates rooms and items objects
# Returns a player object and the tuple containing the rooms / map.

def create_map(player_name):
    crossbow = Item("Crossbow", 5)
    sword = Item("Steel Sword", 3)
    shield = Item("Steel Shield", 4)
    paper_shield = Item("Paper Shield", 1)
    pizza = Item("Pizza", 2)
    potion = Item("Potion", 1)
    master_sword = Item("Master Sword", 10)
    castle_map = Item("Castle Map", 1)

    rooms = (
        Room("Entrance Hall", pizza),
        Room("Stairs", None),
        Room("Games Room", shield),
        Room("Study", None),
        Room("Lounge", sword),
        Room("Kitchen", crossbow),
        Room("Master Bedroom", None),
        Room("Play Room", potion),
        Room("Conservatory", None),
        Room("Kitchen", master_sword),
        Room("Dining Room", None),
        Room("Library", castle_map)

    )
    start_room = random.choice(rooms)
    return Player(player_name, [paper_shield], start_room), rooms

# Function to start the game.
# It asks for the players name and age and then calls the gameMenu function (in menu.py

def gameStart():
    # Clears the console (improves readability)
    # I have checked the depreciated warning and according to stack overflow it is only deprecated in certain environments
    # (sending binary to terminals is not recommended for commercial applications -  but I have decided it is safe in a terminal game in my 1st year).
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n** Castle Adventure Game **\n")
    player_name = input("\nPlease enter your name: ")
    player_age = int(input("\nPlease enter your age: "))
    gameMenu(
        player_name,
        player_age,
        create_map,
        player_moveL,
        player_moveR,
        player_moveB,
        display_inventory,
        carbon_calc,
        save_game,
        load_game,
    )


gameStart()