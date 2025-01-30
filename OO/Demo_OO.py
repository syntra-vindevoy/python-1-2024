from datetime import datetime

class Student:
    def __init__(self, last_name : str, first_name : str,
                 date_of_birth : datetime, national_id : str,
                 nationality : str, gender : str):
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
    def first_name(self, first_name : str):
        if len(first_name) < 1:
            raise ValueError("Last name must be at least 1 characters long.")
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name: str):
        if len(last_name) < 1:
            raise ValueError("Last name must be at least 1 characters long.")
        self.__last_name = last_name

    @property
    def age(self):
        today = datetime.today()

        age = today.year - self.__date_of_birth.year

        if(today.month, today.day) < (self.__date_of_birth.month, self.__date_of_birth.day):
            age -= 1
        return age


    # def get_date_of_birth(self):
    #     return self.__date_of_birth = date_of_birth
    # def get_national_id(self):
    #     return self.__national_id = national_id
    # def get_nationality(self):
    #     return self.__nationality = nationality
    # def get_gender(self):

tom = Student(first_name = "Tom"
                ,last_name = "Van de Vyver"
                ,date_of_birth = datetime(1985, 10, 14)
                ,national_id = "123456789"
                ,nationality = "B"
                ,gender = "M"
              )

chiel = Student(first_name = "Chiel"
                ,last_name = "Vansompel"
                ,date_of_birth = "1985-10-14"
                ,national_id = "123456789"
                ,nationality = "B"
                ,gender = "M"
                )

print(f"Name: {tom.first_name} {tom.last_name}")
print(f"Name: {chiel.first_name} {chiel.last_name}")
print(f"Age: {tom.age}")

