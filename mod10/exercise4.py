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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"{self.name} ({self.distance} km)")
        print(f"{'Registration'}{'Speed (km/h)'}{'Distance (km)'}")
        for car in self.cars:
            print(
                f"{car.license_plate}"
                f"{car.current_speed}"
                f"{car.travelled_distance}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)