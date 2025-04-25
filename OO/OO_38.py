class Person:
    def __init__(self, name, last_name, age):
        self.name: str = name
        self.last_name: str = last_name
        self.age: int = age

    def __str__(self):
        return f'{self.name} {self.last_name} {self.age} years old'

    def __repr__(self):
        return f'RAPPER {self.name} {self.last_name} {self.age} years old'

    def __lt__(self, other):
        return self.age < other.age

    def __len__(self):
        return len(self.name) + len(self.last_name)

    def __add__(self, other):
        return Person(self.name + other.name, self.last_name + other.last_name, self.age + other.age)

yves = Person(name='Yves', last_name="Vindevogel", age=52)
chiel = Person(name='Chiel', last_name="Vansompel", age=32)

print(yves < chiel)

print(len(yves))
print(yves + chiel)

