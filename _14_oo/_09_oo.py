
class Car:
    color = "Grey"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car('Ford', 'Mustang', 2020)
son_car = Car('Tesla', 'Model S', 2024)

print(my_car.make)
print(son_car.make)

print(my_car.color)
print(son_car.color)

#my_car.color = "Dark Grey"

print(my_car.color)
print(son_car.color)

Car.color = "Blue"

print(my_car.color)
print(son_car.color)


class Record:
    connection_string = "localhost"

    def __init__(self, table_name):
        self.table_name = table_name

class Employee(Record):
    def __init__(self):
        super().__init__("Employee")

class Customer(Record):
    def __init__(self):
        super().__init__("Customer")

e = Employee()

Record.connection_string = "localhost:3306"

c = Customer()

print(e.connection_string)
print(c.connection_string)

