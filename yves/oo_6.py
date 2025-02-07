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

@dataclass(slots=True):
class Subscription:
    student: Student
    school_year: SchoolYear
    course: Course

@dataclass(slots=True)
class Student:
    first_name: str
    last_name: str
    date_of_birth: datetime
    national_id: str
    nationality: str
    gender: str

    subscriptions: list = None

    # CRUD
    def create(self):
        sql = "insert into students values (?, ?, ?, ?, ?, ?)"

    def read(self, student_id: int):
        sql = "select * from students where id = ?"

    def update(self, student_id: int):
        sql = "update student set ... where id = ?"

    def delete(self, student_id: int):
        sql = "delete from student where id = ?"

    def subscribe(self, course: Course, school_year: SchoolYear):
        pass


tom = Student(first_name="Tom", last_name="Van De Vyver",
              date_of_birth=datetime(1985, 10, 14), national_id="123456789",
              nationality="B", gender="M")

print(tom.last_name)