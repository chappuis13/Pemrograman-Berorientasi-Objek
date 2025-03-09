class Vehicle:
    def __init__(self, brand, model, rental_rate):
        self.brand = brand
        self.model = model
        self.rental_rate = rental_rate
    
    def calculate_rental(self, days):
        return self.rental_rate * days
    
class Car(Vehicle):
    def open_trunk(self):
        print("Opening the trunk...")

class Bike(Vehicle):
    def kick_start(self):
        print("Kick starting the bike...")

class LuxuryFeatures:
    def enable_gps(self):
        print("GPS enabled")
        
    def enable_heated_seats(self):
        print("Heated seats enabled")

class LuxuryCar(Car, LuxuryFeatures):
    def calculate_rental(self, days):
        return super().calculate_rental(days) + 50
    
rental = [
    Car("Toyota", "Camry", 50),
    Bike("Honda", "CBR", 30),
    LuxuryCar("Mercedes", "C63", 100),
]

def show_rental():
    for vehicle in rental:
        print(f"{vehicle.brand} {vehicle.model} rental: ${vehicle.calculate_rental(7)}")
        
show_rental()