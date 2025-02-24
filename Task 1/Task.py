# define class car
class Car:
    # initialize the Car object with brand, model, and year attributes
    def __init__(self, brand, model, year):
        self.brand = brand 
        self.model = model
        self.year = year
        
    # define a method to display the car's information
    def display_info(self):
        print(f"Brand: {self.brand} {self.model} - Year: {self.year}")
        
# example list of Car objects with different brands, models, and years
example_car = [
    Car("Toyota", "Corolla", 2019),
    Car("Honda", "Civic", 2020),
    Car("Ford", "Mustang", 2021),
]

# iterate over each Car object in the example_car list
for car in example_car:
    # Call the display_info method to print the car's information
    car.display_info()