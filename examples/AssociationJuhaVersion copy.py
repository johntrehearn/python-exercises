class Dog:
  def __init__(self, name):
    self.washed = False
    self.name = name

  def bark(self):
    print(f"{self.name} Bark")

class Cat:
  def __init__(self, name):
    self.name = name

  def meow(self):
    print(f"{self.name} meow")

dog = Dog("Musti")
dog2 = Dog("Maple dog")

dog.bark()
dog2.bark()

class GroomingService:
  def __init__(self):
    print("We created grooming service")

  def wash(self, dog):
    print(f"Dog {dog.name} is being washed")
    dog.washed = True
    dog.treat_has_been_given = True
    dog.confused = "yes"

class Hotel:
  def __init__(self):
    self.dogs = []
    self.service = GroomingService()

  # TODO: this method name is too generic
  def add(self, dog):
    self.dogs.append(dog)

  def print_customers(self):
    print("List of hotel customers")
    print(self.dogs)
    for dog in self.dogs:
      print("   " + dog.name)

  def wash_all_dogs(self):
    print("Starting washing")
    for dog in self.dogs:
      print(dog.washed)
      self.service.wash(dog)
      print(dog.washed)


hotel_california = Hotel()

hotel_california.print_customers()

hotel_california.add(dog)
hotel_california.print_customers()

hotel_california.add(dog2)

hotel_california.print_customers()


# hotel_california.add("Long Johnson")

# hotel_california.print_customers()


hotel_california.wash_all_dogs()


print(dog.washed)
print(dog.confused)