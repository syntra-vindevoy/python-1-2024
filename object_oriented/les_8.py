"""Volgende werkt omwille van overerving, neemt Person over omdat er niets in student staat"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

class Student(Person):
    pass

s1 = Student("john", 36)

#print (s1)

""" Aanpassing, neemt nu wel student en niet de str van person"""
"""Zoekt altijd dieper en dieper in de overerving tot er iets of uiteindelijk niets in gevonden"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

class Student(Person):
    def __str__(self):
        return f"student:{self.name} is {self.age} years old"


s1 = Student("john", 36)

#print (s1)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

class Student(Person):
    def __init__(self, name, age, grades):
        super().__init__(name, age)

        self.grades = grades

s1 = Student("john", 36, 60)

print (s1)

