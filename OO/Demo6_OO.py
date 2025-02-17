class Person:    # prived
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):    # of __repr__ is hetzelfde
        return f'{self._name} {self._age} years old'
# p1 = person("John", 20)
# print(p1)



class Student(Person):    # prived
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.__grade = grade

    def __str__(self):    # of __repr__ is hetzelfde
        return f'class student {self._name}'

s = Student("John", 20, 3.5)
print(s)

