class Student:
    def __init__(self, last_name: str, first_name: str, date_of_birth: datetime,
                 gender: str, nationality: str, national_id: str):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__nationality = nationality
        self.__national_id = national_id