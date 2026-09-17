class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.sound)
        return

class Hotel:
    def __init__(self):
        self.dog = []
    def dog_check_in(self, dog):
        self.dog.append(dog)
    def dog_checkout(self, dog):
        self.dog.remove(dog)
    def greet_dog(self):
            for dog in self.dog:
                dog.bark(1)

dog1 = Dog("Rascal", 2018)
dog2 = Dog("Boi", 2022, "Yip yip yip")

dog1.bark(2)
dog2.bark(5)
