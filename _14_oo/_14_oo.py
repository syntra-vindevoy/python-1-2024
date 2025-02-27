class Person:
    pass

class Student(Person):
    pass

tom = Student()
print(type(tom) == Student)
print(type(tom) == Person)

print(isinstance(tom, Student))
print(isinstance(tom, Person))

print(type(tom) is Student)
print(type(tom) is Person)

print(isinstance(Student, Person))
print(issubclass(Person, Student))