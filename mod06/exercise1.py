import random

diceNumber = input("How many dice to roll:")
sumOfDice = 0


for _ in range(int(diceNumber)):

    sumOfDice += random.randint(1, 6)

print(f"Sum of the dice: {sumOfDice}")
