class Dog:
    def __init__(self, name, birth_year, sound="Woof Woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.sound)


class Hotel:
    def __init__(self):
        self.dogs = []

    def dog_checkin(self, dog):
        self.dogs.append(dog)
        print(f"{dog.name} was checked in")

    def dog_checkout(self, dog):
        self.dogs.remove(dog)
        print(f"{dog.name} was checked out")

    def dogGreet(self):
        for dog in self.dogs:
            print(dog.name)
            dog.bark(1)


dog1 = Dog("Ben", 1991)
dog2 = Dog("Kelpie", 1995)

hotel = Hotel()

hotel.dog_checkin(dog1)
hotel.dogGreet()
        