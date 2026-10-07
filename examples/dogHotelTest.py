class Dog:
    def __init__(self, name, birth_year, sound="Woof Woof"):
        
        dogsCreated = 0
        
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
        dogsCreated = dogsCreated + 1

    def Bark(self, times):
        for i in range(times):
            print(self.sound)
        return

class Hotel:
    def __init__(self):
        dogs = []

    def dogCheckin(self, dog):
        self.dogs.append(dog)
        print({dog.name} + "is checked in")
        return

    def dogCheckOut(self, dog):
        self.dog.remove(dog)
        print({dog.name} + "is checked out")
        return

    def dogGreet(self):
        for dog in dogs:
            print(dog.sound)

dog1 = Dog("Ben", 1992)
dog2 = Dog("Sarah", 1991, "Yip Yep")
hotel = Hotel()
hotel.dogCheckin(dog1)
hotel.dogCheckin(dog2)
