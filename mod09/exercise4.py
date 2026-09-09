import random

class Car:
    def __init__(self, reg_number, max_speed):
        self.license_plate = reg_number
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        if self.current_speed + change >= self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed + change <= 0:
            self.current_speed = 0
        else:
            self.current_speed += change

    def drive(self, hours):
        self.travelled_distance += hours * self.current_speed

def race(cars):
    while all(car.travelled_distance < 10000 for car in cars):
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
    return cars


cars = [
    Car("ABC-123", 180),
    Car("BMW-345", 200),
    Car("WVM-678", 170),
    Car("FIA-123", 160),
]
race(cars)
for car in cars:
    print(car.license_plate, car.travelled_distance)
