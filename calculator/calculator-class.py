# Ask the user to select an option


menu_list = "Select option: \n1. Add\n2. Subtract\n3. Multiple\n4. Divide\n0. Exit\n"
selection = input(menu_list)
# If user did not select quit
while selection != "0":  # must be in quotes as the input is currently str

# Ask user for 2 numbers

    first_number = float(input("First Number: "))
    second_number = float(input("Second Number: "))

# Perform selected calculation

    if selection == "1":
        print(f"Result: {first_number + second_number}")
    elif selection == "2":
        print(f"Result: {first_number - second_number}")
    elif selection == "3":
        print(f"Result: {first_number * second_number}")
    elif selection == "4":
        print(f"Result: {first_number / second_number}")
    else:
        print("Incorrect option")
# Print result

# Go back and select option

#!!! If it is not indented correctly it will not go back to the menu !!!

    menu_list = "Select option: \n1. Add\n2. Subtract\n3.Multiple\n4.Divide\n0.Exit"
    selection = input(menu_list)
