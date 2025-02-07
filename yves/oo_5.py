from dataclasses import dataclass
from datetime import datetime

@dataclass(slots=True)
class Student:
    last_name: str
    date_of_birth: datetime
    national_id: str
    nationality: str
    gender: str
    __first_name: str = ""

    @property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self, first_name: str):
        if len(first_name) < 1:
            raise ValueError("First name must be at least 1 character long.")

        self.first_name = first_name


tom = Student(last_name="Van De Vyver",
              date_of_birth=datetime(1985, 10, 14), national_id="123456789",
              nationality="B", gender="M")

tom.first_name = "Tom"

print(tom.last_name)