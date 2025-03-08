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
#slots = true is optioneel maar steeds gebruiken!!! ipv de slots in vorige lessen
class Student:
    last_name: str
    first_name: str
    date_of_birth: datetime
    nationality: str
    national_id: str
    gender : str

    subsciptions: list = None

    # method toevoegen:
    def save (self):
        sql = "insert into students values (%s, %s, %s, %s, %s, %s)"


    def get(self, student_id):
        sql = "select * from students where student_id=%s"


    def delete(self, student_id):
        sql = "delete from students where student_id=%s"

    def update(self, student_id):
        sql = "update students set name=%s, description=%s, duration=%s where student_id=%s"

    def subscribe(self, course, schoolyear: Schoolyear):
        pass

@dataclass(slots=True)
class Subsciption:
    student: Student
    schoolyear: Schoolyear
    course: Course

tom = Student(last_name="Tom", first_name="Van De Vyver",
              date_of_birth=datetime(1985, 10, 14), national_id="123456789",
              nationality="B", gender="M")


print(f"Name: {tom.first_name} {tom.last_name.upper()}")
