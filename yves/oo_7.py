from dataclasses import dataclass


@dataclass(slots=True)
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f"Class Person: {self._name}"

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)

        self.__grade = grade
        self._age = age

    def __str__(self):
        return f"Class Student: {self._name}"


s = Student("John", 25, 3.1)

print(s)