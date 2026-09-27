print("\n\n** Castle Adventure Game **\n")
playerName = input("\nPlease enter your name: ")
playerAge = int(input("\nPlease enter your age: "))

class item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class player:
    def __init__(self, name, inventory, location):
        self.name = name
        self.inventory = inventory
        self.location = location

def collectItem(player, room):
    if room.item is not None:
        collected_item = room.item
        player.inventory.append(collected_item)
        print(f"You have collected the {collected_item.name}. It has been added to your inventory")
    else:
        print("Nothing to collect here. Keep looking.")  

class room:
    def __init__(self, name, item):
        self.name = name
        self.item = item

def playerMove(player, rooms):
    currentRoomIndex = rooms.index(player.location)

    if currentRoomIndex < len(rooms) - 1:
        player.location = rooms[currentRoomIndex + 1]
        print(f"\nYou are currently in {player.location.name}.\n")
        collectItem(player, player.location)
    else:
        print("\nYou escaped the castle")

def displayInventory(inventory):
    print(f"\nYour current inventory is:\n")
    for item in inventory:
        print(item.name)
    return

def inventoryAdd(inventory):
    print()
    addItem = input("Please enter an items to add to your inventory: ")
    inventory.append(item(addItem, 0))
    displayInventory(inventory)
    return

def carbonCalc(inventory):
    carbonEmis = len(inventory) * 551
    print(f"\nYour inventory's production emmisions are {carbonEmis}g Carbon Dioxide. ")

def playTheGame():
    map = item("Map", 1)
    sword = item("Steel Sword", 3)
    shield = item("Steel Shield", 4)
    paperShield = item("Paper Shield", 1)
    pizza = item("Pizza", 2)

    hall = room('Hall', map)
    room1 = room('Room 1', pizza)
    room2 = room('Room 2', None)
    room3 = room('Room 3', shield)
    room4 = room('Room 4', None)
    room5 = room('Room 5', sword)
    rooms = (hall, room1, room2, room3, room4, room5)

    player_inventory = [paperShield]
    player1 = player(playerName, player_inventory, hall)

    print(f"\n** Game Menu **\n\nYou are currently in the {player1.location.name}\n\n1. Move to the next room\n2. Add item to inventory\n3. Display Inventory\n4. Check your Carbon Dioxide Emissions")
    print()
    gameMenuChoice = input("Please choose a menu item or Enter \"back\" to exit this menu: ")
    while gameMenuChoice != "back":
        if gameMenuChoice == "1":
            playerMove(player1, rooms)
        elif gameMenuChoice == "2":
            inventoryAdd(player1.inventory)
        elif gameMenuChoice == "3":
            displayInventory(player1.inventory)
        elif gameMenuChoice == "4":
            carbonCalc(player1.inventory)
        else:
            if gameMenuChoice != "lopeta":
                print("Incorrect option selected")
        gameMenuChoice = input("\nPlease choose another menu item or enter \"back\" to exit: ")
    return

def instructions():
    print("\n**The Terminal Castle game**\n\n -Read the text. \n -Let us know what you want to do.\n")
    return

def options():
    print("\nLots of great in game options here.\n")
    return

if playerAge < 12:
    print("\nSorry but you are a minor\n\nGoodbye for now\n")
else:
    print(f"\nHello {playerName}, your age is {playerAge}\n")

    menuChoice ="0"

    while menuChoice != "lopeta":

        print("** Main Menu **\n\n1. Play the game\n2. Instructions\n3. Options")
        menuChoice = input("\nPlease choose a menu item or Enter \"lopeta\" to exit: ")

        if menuChoice == "1":
            playTheGame()
        elif menuChoice == "2":
            instructions()
        elif menuChoice == "3":
           options()
        else:
            if menuChoice != "lopeta":
                print("Incorrect option selected")