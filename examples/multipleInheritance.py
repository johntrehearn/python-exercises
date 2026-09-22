class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class SportsItem:
    def __init__(self, weight):
        self.weight = weight

# We cannot use Super here because we have multiple inheritance. We need to call the constructors of both parent classes explicitly.
# The super() function in Python is used to access and call methods from a parent (or sibling) class. It allows you to inherit functionality 
# without explicitly naming the parent class, making your code more flexible, maintainable, and adaptable to changes.
class Bicycle(Vehicle, SportsItem):
    def __init__(self, speed, weight, gears):
        Vehicle.__init__(self, speed)
        SportsItem.__init__(self, weight)

        self.gears = gears

b = Bicycle(45, 18.7, 3)
print(f"Bike gears", b.gears)
print(f"Bike speed", b.speed)
print(f"Bike weight", b.weight)