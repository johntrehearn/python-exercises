import random

pointsToGenerate = int(input("How many points do you want to use to generate:"))

i = pointsToGenerate

insideCircle = 0

while i != 0:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    distance = x**2 + y**2
    if distance <= 1:
        insideCircle = insideCircle + 1
    i = i - 1

pi = (insideCircle / pointsToGenerate) * 4

print(f"Approximation of pi: {pi}")