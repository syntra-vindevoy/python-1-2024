class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age

    def __str__(self):
        return f"{self.last_name.upper()}, {self.first_name}  ({self.age})"

    def __repr__(self):
        return f"Person({self.first_name}, {self.last_name}, {self.age})"

    def __lt__(self, other):
        return self.age < other.age

    def __len__(self):
        return len(self.first_name) + len(self.last_name)

    def __add__(self, other):
        return Person(self.first_name + other.first_name, self.last_name + other.last_name, self.age + other.age)

yves = Person(first_name="Yves", last_name="Vindevogel", age=52)
print(yves)

chiel = Person(first_name="Chiel", last_name="Vansompel", age=32)

print(chiel < yves)
print(len(yves))

print(yves + chiel)