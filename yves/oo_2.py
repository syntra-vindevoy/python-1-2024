from datetime import datetime


class Student:
    def __init__(self, last_name: str, first_name: str,
                 date_of_birth: datetime, national_id: str,
                 nationality: str,
                 gender: str):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__date_of_birth = date_of_birth
        self.__national_id = national_id
        self.__nationality = nationality
        self.__gender = gender

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str):
        if len(first_name) < 1:
            raise ValueError("First name must be at least 1 character long.")

        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str):
        if len(last_name) < 1:
            raise ValueError("Last name must be at least 1 character long.")

        self.__last_name = last_name

    @property
    def age(self):
        today = datetime.today()

        age = today.year - self.__date_of_birth.year

        if (today.month, today.day) < (self.__date_of_birth.month, self.__date_of_birth.day):
            age -= 1

        return age

tom = Student(last_name="Tom", first_name="Van De Vyver",
              date_of_birth=datetime(1985, 10, 14), national_id="123456789",
              nationality="B", gender="M")

#chiel = Student(last_name="Chiel", first_name="Vansompel",
#                date_of_birth="1992-05-10", national_id="321",
#                nationality="B", gender="M")

print(f"Name: {tom.first_name} {tom.last_name.upper()}, he is {tom.age} years old.")
#print(f"Name: {chiel.first_name} {chiel.last_name.upper()}")

tom.age = 52

# tom.height = 185
# tom.nationality = "NL"

# print(tom.height)
# print(chiel.height)
