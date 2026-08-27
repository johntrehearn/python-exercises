import random

guessNumber = random.randint(1,10)

print(guessNumber)

guess = int(input("Guess a number (1-10): "))

while guess != guessNumber:
    if guess > guessNumber:
        print("Too high")
        guess = int(input("Guess a number (1-10): "))
    else:
        print("Too low")
        guess = int(input("Guess a number (1-10): "))

print("Correct")