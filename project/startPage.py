playerName = input("\nPlease enter your name: ")
playerAge = int(input("\nPlease enter your age: "))


if playerAge < 12:
    print("\nSorry but you are a minor\n\nGoodbye for now\n")
else:
    print(f"\nHello {playerName}, your age is {playerAge}\n")

    menuChoice ="0"

    while menuChoice != "lopeta":

        print("**Main Menu**\n\n1. Play the game\n2. Instructions\n3. Options")
        menuChoice = input("\nPlease choose a menu item or Enter \"lopeta\" to exit\n")

        if menuChoice == "1":
            print("\nWelcome to the game.\n\nThe Adventure Awaits\n")
        elif menuChoice == "2":
            print("\n**The Termainal Castle game**\n\n -Read the text. \n -Let us know what you want to do.\n")
        elif menuChoice == "3":
            print("\nLots of great in game options here.\n")
        else:
            if menuChoice != "lopeta":
                print("Incorrect option selected")



# Modify the game project program so that if the user enters an age under 12, the program informs them that they are a minor and shuts down. 
# Otherwise, the program greets the user, displays the main menu, and asks for commands until the user enters "lopeta".

# Add a few fictional commands that each produce a different output in the console. After a command, always display the menu again.