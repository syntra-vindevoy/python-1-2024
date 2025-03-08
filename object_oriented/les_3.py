from dataclasses import dataclass
from datetime import datetime

@dataclass(slots=True)
#slots = true is optioneel maar steeds gebruiken!!! ipv de slots in vorige lessen
class Student:
    last_name: str
    first_name: str
    date_of_birth: datetime
    nationality: str
    national_id: str
    gender : str


tom = Student(last_name="Tom", first_name="Van De Vyver",
              date_of_birth=datetime(1985, 10, 14), national_id="123456789",
              nationality="B", gender="M")

#chiel = Student(last_name="Chiel", first_name="Vansompel",
#                date_of_birth="1992-05-10", national_id="321",
#                nationality="B", gender="M")

print(f"Name: {tom.first_name} {tom.last_name.upper()}, he is  years old.")
#print(f"Name: {chiel.first_name} {chiel.last_name.upper()}")

tom.gender = "X"

# tom.height = 185
# tom.nationality = "NL"

# print(tom.height)
# print(chiel.height)