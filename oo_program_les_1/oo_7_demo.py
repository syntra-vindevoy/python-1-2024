class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def make_sound(self):
        print("we gaan een geluidje maken")

class Student(Person):
    def __init__(self, name, age, grades = None):
        super().__init__(name, age)
        
        self.grades = grades

class Teacher(Person):
    pass

s1 = Student("John", 36)
print(s1)

s1.make_sound()