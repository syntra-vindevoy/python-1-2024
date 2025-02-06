from dataclasses import dataclass


#les 04/02
@dataclass(slots=True)
class Student:
    first_name: str
    last_name: str
    date_of_birth: str
    nationality: str
    national_id: str
    gender: str



tom = Student(first_name="tom",
              last_name = "Vijver",
              date_of_birth = "01/01/1999",
              nationality = "B",
              national_id = "123456789",
              gender = "M")

