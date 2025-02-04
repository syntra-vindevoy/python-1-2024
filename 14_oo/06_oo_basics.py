from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class SchoolYear:
    name: str
    start_date: datetime
    end_date: datetime


@dataclass(slots=True)
class Course:
    name: str


@dataclass(slots=True)
class Subscription:
    student: Student
    school_year: SchoolYear
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

    #CRUD
    def create(self):
        sql = "insert into students values (?, ?, ?, ?)"

    def read(self, student_id: int):
        sql = "select * from students where id = ?"

    def update(self, student_id: int):
        sql = "update students set ... where id = ?"

    def delete(self, student_id: int):
        sql = "delete from students where id = ?"


    def subscribe(self, course: Course, school_year: SchoolYear):
        pass



thomas = Student(last_name="Meersschaut",
                 first_name="Thomas",
                 date_of_birth=datetime(1988, 2, 16),
                 national_id="1234567890",
                 nationality="B",
                 gender="M")