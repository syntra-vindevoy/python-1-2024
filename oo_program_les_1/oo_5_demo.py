class Person:
    def __init__(self, name, age):
        self._name = name  #protected propperty, is met 1 _, dan kunnen die wel opgevraagd worden door childs
        self._age = age

    def __str__(self):
        return f"class Person: {self._name}"

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)

        self.__grade = grade
        self._age = age

    def __str__(self):
        return f"class Student: {self._name}"

p1 = Person("John", 36)
s1 = Student("John", 25, 3.1)

print(p1)
print(s1)