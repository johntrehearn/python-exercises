playerName = input("Please enter your name: ")
playerAge = int(input("Please enter your age: "))


if playerAge < 12:
    print("Sorry but you are a minor\n\nGoodbye for now\n")
else:
    print(f"\nHello {playerName}, your age is {playerAge}\n")
    print("**Main Menu**\n\n1. Play the game\n2. Instructions\n3. Options")

    menuChoice ="0"

    while menuChoice != "lopeta":

        menuChoice = input("\nPlease choose a menu item or Enter \"lopeta\" to exit\n")

        if menuChoice == "1":
            print("Menu 1 selected")
        elif menuChoice == "2":
            print("Menu 2 selected")
        elif menuChoice == "3":
            print("Menu 3 selected")
        else:
            print("Incorrect option selected")

    menuChoice = input("\nPlease choose a menu item or Enter \"lopeta\" to exit\n")


# Modify the game project program so that if the user enters an age under 12, the program informs them that they are a minor and shuts down. 
# Otherwise, the program greets the user, displays the main menu, and asks for commands until the user enters "lopeta".

# Add a few fictional commands that each produce a different output in the console. After a command, always display the menu again.