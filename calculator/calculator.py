calculationType = input("Please enter the number for the calculationType type you want \n 1. Add \n 2. Minus \n 3. Multiply \n 4. Divide \n 5. Exit\n")

question1 = ("Please enter first number: ")
question2 = ("Please enter second number: ")

while calculationType != "5":

    if calculationType == "1":
        number1 = int(input(question1))
        number2 = int(input(question2))
        print(f"Your two numbers were {number1} and {number2}")
        result = number1 + number2
        print(f"The calculationType result is: {result}\n")
    elif calculationType == "2":
        number1 = int(input(question1))
        number2 = int(input(question2))
        print(f"Your two numbers were {number1} and {number2}")
        result = number1 - number2
        print(f"The calculationType result is: {result}\n")
    elif calculationType == "3":
        number1 = int(input(question1))
        number2 = int(input(question2))
        print(f"Your two numbers were {number1} and {number2}")
        result = number1 * number2
        print(f"The calculationType result is: {result}\n")
        print("two selected")
    elif calculationType == "4":
        number1 = int(input(question1))
        number2 = int(input(question2))
        print(f"Your two numbers were {number1} and {number2}")
        result = number1 / number2
        print(f"The calculationType result is: {result}\n")
    else:
        print("Please enter a valid choice!")
        # To actually ask the question again, you need to re-assign it to a new input().
    calculationType = input("Please enter the number for the calculationType type you want \n 1. Add \n 2. Minus \n 3. Multiply \n 4. Divide \n 5. Exit\n")
print("Goodbye!")
