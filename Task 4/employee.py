class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.salary = 1000
    
    def calculate_salary(self):
        return self.salary

class Manager(Employee):
    def calculate_salary(self):
        return self.salary + (self.salary * 0.2)

class Engineer(Employee):
    def calculate_salary(self):
        return self.salary + (self.salary * 0.1)
    
employees = [
    Manager(1, "Alice"),
    Engineer(2, "Bob")
]

def show_details():
    for employee in employees:
        print(f"{employee.name} salary: ${employee.calculate_salary()}")

show_details()