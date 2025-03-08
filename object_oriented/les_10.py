class Person:
    pass

class Student(Person):
    pass

tom = Student()

print(type(tom))
print (type(tom) == Student)
print (type(tom) == Person)
"""
"""

class Person:
    pass

class Student(Person):
    pass

tom = Student()

print (isinstance(tom, Person))
print(isinstance(tom, Student))

print (issubclass(Person, Student))
print (issubclass(Student, Person))

