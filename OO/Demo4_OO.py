from dataclasses import dataclass
from datetime import datetime

@dataclass(slots=True)
class Student:
    last_name: str
    first_name: str
    date_of_birth: datetime
    national_id: str
    nationality: str
    gender: str


    # @property
    # def first_name(self):
    #     return self.__first_name
    #
    # @first_name.setter
    # def first_name(self, first_name: str):
    #     if len(first_name) < 1:
    #         raise ValueError("First name must be at least 1 character long.")
    #     self.__first_name = first_name
# Create instances of Student and Teacher
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

# yves = Teacher(first_name="Yvers",
#                last_name="Vindevogel",
#                date_of_birth=datetime(1985, 10, 14),
#                national_id="1256595789",
#                nationality="B",
#                gender="M")

#tom.toto = "kdkdkekio,von" # geeft fout omdat niet is gedifinieert

# Print information
print(f"Name: {tom.first_name} {tom.last_name.upper()}")
print(f"Name: {chiel.first_name} {chiel.last_name}")
#print(f"Age: {tom.age}")
#print(f"Yves is {yves.age} years old")
#print(tom.__dict__)