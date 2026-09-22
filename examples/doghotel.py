class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def get_age(self):
        return self.age

dog1 = Dog("Musti", 3)
dog2 = Dog("Maple", 5)

print(dog1.bark())

print(dog2.bark())

print(dog1.bark())

class Hotel:
    def __init__(self, name):
        self.name = name
        self.dogs = []

    def add_dog(self, dog):
        self.dogs.append(dog)


    def print_customers(self):
        print(f"Customers at {self.name}:")
        for dog in self.dogs:
            print(f"{dog.name}, Age: {dog.age}")


hotel = Hotel("Dog Hotel")
hotel.print_customers()
hotel.add_dog(dog1)
hotel.add_dog(dog2)
hotel.print_customers()
hotel.add_dog(dog2)
hotel.add_dog(dog2)