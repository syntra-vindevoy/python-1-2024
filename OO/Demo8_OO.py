class Car:
    color = "red"
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car("Ford", "Mustang", 1964)
print(my_car.make)


son_car = Car("Volvo", "C70", 2005)
print(son_car.make)

#my_car.color = "blue"

print(my_car.color)
print(son_car.color)

Car.color = "yellow"

print(my_car.color)
print(son_car.color)

class Record:
    connectionstring = "localhost"
    def __init__(self, table):
        self.table = table

class Employee(Record):
    def __init__(self):
        super().__init__("employee")

class Manager(Record):
    def __init__(self):
       super().__init__("manager")


e = Employee()
m = Manager()

Record.connectionstring = "localhost:3306"

print(e.connectionstring)
print(m.connectionstring)


class DatabaseClass:
    def __init__(self, table: str):
        self.table = table

    def fetch(self, id):
        sql = f"SELECT * FROM {self.table} WHERE id = {id}"
        return sql

class Contacts:
    def __init__(self)
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def get_contacts(self, id):
        db = ""
        c: Contacts = db.fetch(id)
        return c

class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

contacts = Contact()
yves = Contact("Yves", "<EMAIL>")
