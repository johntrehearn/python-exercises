airports = {"EGLL": "London Heathrow Airport", "KLAS": "McCarran International Airport"}

option = ""
while option != "3":
    print("\nAirport Data Management\n1. Enter a new airport\n2. Fetch airport information\n3. Quit")
    option = input("Please choose an option (1-3): ")

    if option == "1":
        airport_code = input("Enter the ICAO code: ")
        airport_name = input("Enter the airport name: ")
        airports[airport_code] = airport_name
        print(f"Airport {airport_name} with ICAO code {airport_code} has been added.")
    elif option == "2":
        airport_code = input("Enter the ICAO code: ")
        if airport_code in airports:
            print(f"The airport with ICAO code {airport_code} is {airports[airport_code]}.")
        elif airport_code not in airports:
            print(f"No airport found with ICAO code {airport_code}.")

print("Thank you for using the Airport Data Management system. Goodbye!")