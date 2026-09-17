print("\n\n** Castle Adventure Game **\n")
playerName = input("\nPlease enter your name: ")
playerAge = int(input("\nPlease enter your age: "))

inventory = ["Sword", "Shield"]

def inventoryAdd(inventory):
    addItem = input("Please enter an items to add to your inventory: ")
    inventory.append(addItem)
    print(f"Your new inventory is {inventory}\n")
    playTheGame()
    return

def displayInventory(inventory):
    print(f"Your inventory currently is {inventory}\n")
    return

def playTheGame():
    print("**Game Menu**\n\n1. Add item to inventory\n2. Display Inventory\n3. Check your Carbon Dioxide Emissions")
    gameMenuChoice = input("\nPlease choose a menu item or Enter \"back\" to exit this menu:\n")
    while gameMenuChoice != "back":
        if gameMenuChoice == "1":
            inventoryAdd(inventory)
        elif gameMenuChoice == "2":
            gameMenuChoice == " "
            displayInventory(inventory)
        elif gameMenuChoice == "3":
            options()
        else:
            if gameMenuChoice != "lopeta":
                print("Incorrect option selected")
    return

def instructions():
    print("\n**The Termainal Castle game**\n\n -Read the text. \n -Let us know what you want to do.\n")
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

        print("**Main Menu**\n\n1. Play the game\n2. Instructions\n3. Options")
        menuChoice = input("\nPlease choose a menu item or Enter \"lopeta\" to exit:\n")

        if menuChoice == "1":
            playTheGame()
        elif menuChoice == "2":
            instructions()
        elif menuChoice == "3":
           options()
        else:
            if menuChoice != "lopeta":
                print("Incorrect option selected")