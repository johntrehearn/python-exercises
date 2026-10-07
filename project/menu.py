def game_menu(player, rooms, player_moveL, player_moveR, player_moveB, display_inventory, carbon_calc, save_game, load_game):
    with open("intro.txt") as menu:
        menu_text = menu.read()
    print(menu_text.format(location=player.location.name))
    game_menu = input('Please choose a menu item or enter "back" to exit this menu: ')
    while game_menu != "back":
        if game_menu == "1":
            player_moveL(player, rooms)
        elif game_menu == "2":
            player_moveR(player, rooms)
        elif game_menu == "3":
            player_moveB(player, rooms)
        elif game_menu == "4":
            display_inventory(player.inventory)
        elif game_menu == "5":
            carbon_calc(player.inventory)
        elif game_menu == "6":
            save_game(player)
        elif game_menu == "7":
            load_game(player, rooms)
        else:
            print("Incorrect option selected")
        game_menu = input('\nPlease choose another menu item or enter "back" to exit: ')


def instructions():
    with open("instructions.txt") as inst:
        instText = inst.read()
    print(instText)

def options():
    print("\nLots of great in-game options here.\n")

def gameMenu(player_name, player_age, start_game, player_moveL, player_moveR, player_moveB, display_inventory, carbon_calc, save_game, load_game):
    if player_age < 12:
        print("\nSorry but you are a minor\n\nGoodbye for now\n")
        return

    print(f"\nHello {player_name}, your age is {player_age}\n")
    menu_choice = "0"
    while menu_choice != "exit":
        print("** Main Menu **\n\n1. Play the game\n2. Instructions\n3. Options\n")
        menu_choice = input('Please choose a menu item or enter "exit" to quit: \n')
        if menu_choice == "1":
            player, rooms = start_game(player_name)
            game_menu(player, rooms, player_moveL, player_moveR, player_moveB, display_inventory, carbon_calc, save_game, load_game)
        elif menu_choice == "2":
            instructions()
        elif menu_choice == "3":
            options()
        elif menu_choice != "exit":
            print("Incorrect option selected")