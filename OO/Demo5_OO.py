from dataclasses import dataclass
from datetime import datetime

@dataclass(slots=True)
class Schoolyear:
    name: str
    start_date: datetime
    end_date: datetime

@dataclass(slots=True)
class Course:
    name: str
    description: str
    duration: int

@dataclass(slots=True)
class subscriptions:
    student: Student
    school_year: Schoolyear
    course: Course


@dataclass(slots=True)
class Student:
    last_name: str
    first_name: str
    date_of_birth: datetime
    national_id: str
    nationality: str
    gender: str

    subscriptions: list = None

    # CRUD create read update delete

    # def create(self):
    #     sql = "insert into student values (?,?,?,?,?)"
    # def read(self, student_id: int):
    #     sql = "select * from student where student_id = ?"
    #
    # def update(self, student_id: int):
    #     sql = "update student set first_name = ? where student_id = ?"
    #
    # def delete(self, student_id: int):
    #     sql = "delete from student where student_id = ?"
    #
    # def subscribe(self, course: Course, school_year: Schoolyear):
    #     sql = "insert into subscriptions values (?,?,?)"

tom = Student(first_name="Tom",
              last_name="Van de Vyver",
              date_of_birth=datetime(1985, 10, 14),
              national_id="123456789",
              nationality="B",
              gender="M")

chiel = Student(first_name="Chiel",
                last_name="Vansompel",
                date_of_birth=datetime(1985, 10, 14),
                national_id="123456789",
                nationality="B",
                gender="M")

# Print information
print(f"Name: {tom.first_name} {tom.last_name.upper()}")
print(f"Name: {chiel.first_name} {chiel.last_name}")
#print(f"Age: {tom.age}")
#print(f"Yves is {yves.age} years old")
#print(tom.__dict__)