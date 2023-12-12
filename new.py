class Elevator:
    def __init__(self, starting_floor): #starting_floor es un parametro del constructor - de la clase Elevator
        self.make = "The elevator company"
        self.floor = starting_floor

# To create the object

elevator = Elevator(1)
print(elevator.make) # "The Elevator company"
print(elevator.floor) # 1

