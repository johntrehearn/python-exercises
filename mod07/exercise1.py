import random

def roll_dice():
    diceResult = random.randint(1, 6)
    print(diceResult)
    if diceResult == 6:
        return diceResult
    else:
        return roll_dice()

roll_dice()