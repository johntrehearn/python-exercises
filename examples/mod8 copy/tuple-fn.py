# Tuples as return values
# Earlier on the course we learned about functions that are callable subroutines. Tuples provide an easy way to circumvent the limitation that a function can have only one return value. If the developer wants to return, for example, two values, he/she can create a tuple that holds both values and return that tuple as the return value. From a technical point of view, there’s still one return value, but it is a tuple that can in turn contain more than one value.

# The following example illustrates the use of a tuple as a return value. The program contains a die-casting function for the Monopoly board game. In Monopoly, one always casts two dice at a time.

import random

def cast():
    first, second = random.randint(1,6), random.randint(1,6)
    return first, second

def cast():
    (first, second) = (random.randint(1,6), random.randint(1,6))
    return (first, second)

#these are the same, but the first one is more readable and easier to understand

die1, die2 = cast()
print(f"The dice show {die1} and {die2}.")
