class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def make_sound(self):
        print("Hello!")

class Student(Person):
    def __init__(self, name, age, grades = None):
        super().__init__(name, age)
        self.grades = grades

s1 = Student("John", 36)
print(s1)