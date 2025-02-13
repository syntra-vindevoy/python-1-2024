class Car:
    color = "Grey"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


my_car = Car('Ford', 'Nugget', 2020)
son_car = Car('Volvo', 'C70', 2005)

print(my_car.make)
print(son_car.make)

print(my_car.color)
print(son_car.color)

my_car.color = "Dark Grey"

print(my_car.color)
print(son_car.color)

Car.color = "Blue"

print(my_car.color)
print(son_car.color)


class Record:
    connection_string = ""

    def __init__(self, table_name):
        self.table_name = table_name


class Employee(Record):
    def __init__(self):
        super().__init__("employees")

class Customer(Record):
    def __init__(self):
        super().__init__("customers")

e = Employee()

Record.connection_string = "localhost:3306"

c = Customer()

print(e.connection_string)
print(c.connection_string)

class DatabaseClass:
    def __init__(self, table: str):
        self.table = table

    def fetch(self, id):
        sql = f"select from {self.table} where id = {id}"

class Contacts(DatabaseClass):
    def __init__(self):
        super().__init__("contacts")

        self.__contacts = []

    def insert(self, contact):
        self.__contacts.append(contact)

    def get(self, id):
        db = ""
        c: Contact = db.fetch(id)
        return c

class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email


contacts = Contacts()

yves = Contact("Yves", "<EMAIL>")

contacts.insert(yves)
print(contacts.get(1))
