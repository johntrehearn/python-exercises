import random

sides = int(input("How many sides do you want on the dice? "))

def roll_dice(sides):
    diceResult = random.randint(1, sides)
    print(diceResult)
    if diceResult == sides:
        return diceResult
    else:
        return roll_dice(sides)

roll_dice(sides)