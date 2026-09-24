class Elevator:

    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            # print(f"Lift is currently on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            # print(f"Lift is currently on floor {self.current_floor}")

    def go_to_floor(self, floor):

        while self.current_floor < floor:
            self.floor_up()

        while self.current_floor > floor:
            self.floor_down()

# lift = Elevator(1, 10)
# print("Basic elevator test:")
# lift.go_to_floor(5)
# print("\n**END OF TEST**\n")
# lift.go_to_floor(1)

