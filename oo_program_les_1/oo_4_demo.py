from dataclasses import dataclass
from datetime import date


#les 04/02
@dataclass(slots=True):
class SchoolYear:
    name: str
    start_date: date
    end_date: date

@dataclass(slots=True):
class Course:
    name: str
    description: str
    duration: int

@dataclass(slots=True):
class Subscription:
    student: Student
    school_year: SchoolYear
    course: Course


@dataclass(slots=True):
class Student:
    first_name: str
    last_name: str
    date_of_birth: str
    nationality: str
    national_id: str
    gender: str

    def subscribe(self, course: Course, school_year: SchoolYear):
        pass

    #crud
    def create(self   ):  #save
        sql = "insert into students values (%s, %s, %s, %s, %s)"

    def read(self, student_id: int): #get
        sql = "select * from students where student_id=%s"

    def update(self, student_id: int):
        sql = "update student set ... where id = "

    def delete(self, student_id: int):
        sql = "delete from students where student_id=%s"



tom = Student(first_name="tom",
              last_name = "Vijver",
              date_of_birth = "01/01/1999",
              nationality = "B",
              national_id = "123456789",
              gender = "M")

