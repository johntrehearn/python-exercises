class Player:
    def __init__(self, name, inventory, location):
        self.name = name
        self.inventory = inventory
        self.location = location

class Room:
    def __init__(self, name, item):
        self.name = name
        self.item = item

class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight