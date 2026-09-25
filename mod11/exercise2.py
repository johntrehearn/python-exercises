# Extend the previously written Car class 
#   by adding two subclasses: ElectricCar and GasolineCar.
#  Electric cars have the capacity of the battery in kilowatt-hours as their property (battery_capacity).
#  Gasoline cars have the volume of the tank in liters as their property (tank_volume). 
# Write initializers for the subclasses. 
#   For example, the initializer of electric cars receives the 
#       registration number (license_plate), 
#       maximum speed (maximum_speed) and 
#       battery capacity (battery_capacity) as its parameter. 
# 
# It calls the initializer of the base class to set the first two properties and then sets its capacity.
class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
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

class ElectricCar(Car):
    def __init__(self, license_plate, maximum_speed, battery_capacity):
        super().__init__(license_plate, maximum_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, license_plate, maximum_speed, tank_volume):
        super().__init__(license_plate, maximum_speed)
        self.tank_volume = tank_volume
