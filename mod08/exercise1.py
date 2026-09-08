seasons = {"winter": (12, 1, 2), "spring": (3, 4, 5), "summer": (6, 7, 8), "autumn": (9, 10, 11)}

def get_season(monthNumber):
    for season, months in seasons.items():
        if monthNumber in months:
            print(f"The season is {season}.")
            return season
        
monthNumber = int(input("Enter the number of a month (1-12): "))

if monthNumber > 12 or monthNumber < 1:
    print(f"You entered: {monthNumber}\nPlease enter a number between 1 and 12. ")
else:
    print(f"You entered: {monthNumber}")
    get_season(monthNumber)
