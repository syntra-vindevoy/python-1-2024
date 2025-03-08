# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     def __str__(self):
#         return f"Class Name: {self.__name}"
#
# p1 = Person ("John", 15)
# print (p1)

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def __str__(self):
        return f"Class Name: {self.__name}"

class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.__score = score
        
    def __str__(self):
        return f"Class Student: { self._name}"

s = Student ("John", 15, 8)

print (s)