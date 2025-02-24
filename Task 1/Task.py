class Car:
    def __init__(self, brand, model, year):
        self.brand = brand 
        self.model = model
        self.year = int(year)
        
    def display_info(self):
        print(f'Brand: {self.brand}, Model: {self.model}, Year: {self.year}')


car1 = Car('Honda', 'Civic', 2020)
car2 = Car('Toyota', 'Supra', 2022)
car3 = Car('Toyota', 'Kijang Innova', 2023)

    car3.display_info()
