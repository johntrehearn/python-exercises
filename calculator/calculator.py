calculation = input("Please enter the number for the calculation type you want \n 1. Add \n 2. Minus \n 3. Multiply \n 4. Divide \n 5. Exit\n")

question1 = ("Please enter first number: ")
question2 = ("Please enter second number: ")

while input != 5:

    if calculation == "1":
        number1 = int(input(question1))
        number2 = int(input(question2))
        print(f"Your two numbers were {number1} and {number2}")
        result = number1 + number2
        print(f"The calculation result is: {result}")
    elif calculation == "2":
        print("two selected")
    elif calculation == "3":
        print("three selected")
    elif calculation == "4":
        print("four selected")
    else:
        print("Please enter a valid choice!")
