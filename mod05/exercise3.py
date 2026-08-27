numbersList = []

number = 0

while number !="":
    number = input("Enter a number (or press Enter to quit): ")
    if number == "":
        break
    number = float(number)
    numbersList.append(number)

numbersList.sort()
print(f"Smallest number: {numbersList[0]}")
print(f"Largest number: {numbersList[-1]}")
