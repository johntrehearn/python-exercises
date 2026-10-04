def game_menu(player, rooms, player_move, display_inventory, carbon_calc):
    print(
        f"\n** Game Menu **\n\nYou are currently in the {player.location.name}\n\n"
        "1. Move to the next room\n2. Display Inventory\n3. Check your Carbon Dioxide Emissions\n"
    )
    game_menu = input('Please choose a menu item or enter "back" to exit this menu: ')
    while game_menu != "back":
        if game_menu == "1":
            player_move(player, rooms)
        elif game_menu == "2":
            display_inventory(player.inventory)
        elif game_menu == "3":
            carbon_calc(player.inventory)
        else:
            print("Incorrect option selected")
        game_menu = input('\nPlease choose another menu item or enter "back" to exit: ')


def instructions():
    print("\n** The Terminal Castle game **\n\n- Read the text.\n- Let us know what you want to do.\n")

def options():
    print("\nLots of great in-game options here.\n")

def gameMenu(player_name, player_age, start_game, player_move, display_inventory, carbon_calc):
    if player_age < 12:
        print("\nSorry but you are a minor\n\nGoodbye for now\n")
        return

    print(f"\nHello {player_name}, your age is {player_age}\n")
    menu_choice = "0"
    while menu_choice != "exit":
        print("** Main Menu **\n\n1. Play the game\n2. Instructions\n3. Options\n")
        menu_choice = input('Please choose a menu item or enter "exit" to quit: ')
        if menu_choice == "1":
            player, rooms = start_game(player_name)
            game_menu(player, rooms, player_move, display_inventory, carbon_calc)
        elif menu_choice == "2":
            instructions()
        elif menu_choice == "3":
            options()
        elif menu_choice != "exit":
            print("Incorrect option selected")