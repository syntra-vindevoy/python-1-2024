class Persons:
    def __init__(self, name="", age=0, address=""):
        # Private attributes
        self.__name = name
        self.__age = age
        self.__address = address

    # Getter for name
    @property
    def name(self):
        return self.__name

    # Setter for name
    @name.setter
    def name(self, value):
        self.__name = value

    # Getter for age
    @property
    def age(self):
        return self.__age

    # Setter for age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self.__age = value

    # Getter for address
    @property
    def address(self):
        return self.__address

    # Setter for address
    @address.setter
    def address(self, value):
        self.__address = value


# Example usage
person = Persons()
person.name = "Alice"
person.age = 25
person.address = "456 Oak Avenue"

print(f"Name: {person.name}")
print(f"Age: {person.age}")
print(f"Address: {person.address}")
