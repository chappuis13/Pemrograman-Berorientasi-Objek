class Vehicle:
    def move(self):
        return "Vehicle can move"
    
class Cars(Vehicle):
    def move(self):
        return "Cars can move"
    
class Bicycles(Vehicle):
    def move(self):
        return "Bicycles can move"
    
class Boats(Vehicle):
    def move(self):
        return "Boat can move"
    
vehicles = [Vehicle(), Cars(), Bicycles(), Boats()]

for vehicle in vehicles:
    print(vehicle.move())