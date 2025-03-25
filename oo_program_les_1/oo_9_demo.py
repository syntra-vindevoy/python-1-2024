class Person:
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

tom = Student()

print(type(tom) == Student)
print(type(tom) == Person)

print(isinstance(tom, Student))
print(isinstance(tom, Person))

print(issubclass(Student, Person))
print(issubclass(Person, Student))