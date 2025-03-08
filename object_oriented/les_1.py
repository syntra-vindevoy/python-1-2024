from datetime import datetime

class Human:
    def __init__(self, last_name: str, first_name: str, date_of_birth: str,
                 national_id: str, nationality: str, gender: str):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.national_id = national_id
        self.nationality = nationality
        self.gender = gender


class Student:
    def __init__(self, last_name: str, first_name: str, date_of_birth: str,
                 national_id: str, nationality: str, gender: str):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.national_id = national_id
        self.nationality = nationality
        self.gender = gender

tom = Student("Tompson", "Tom","1990-05-07", "123456789",
              "Belgian", "Male" )
jean = Student( "Jacques", "Jean","1990-05-10", "157862135",
                "France", "Male")

class Student:
    __slots__ = ("__last_name", "__first_name", "__date_of_birth","__national_id","__nationality","__gender")
    def __init__(self, last_name: str, first_name: str, date_of_birth,
                 national_id: str, nationality: str, gender: str):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__date_of_birth = date_of_birth
        self.__national_id = national_id
        self.__nationality = nationality
        self.__gender = gender

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if len(last_name) < 1:
            raise ValueError("Last name must be at least 1 character long")
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__last_name

    @last_name.setter
    def first_name(self, first_name):
        if len(first_name) < 1:
            raise ValueError("Last name must be at least 1 character long")
        self.__last_name = first_name
    @property
    def age(self):
        today = datetime.today()
        age = today.year - self.__date_of_birth.year
        if (today.month, today.day) < (self.__date_of_birth.month, self.__date_of_birth.day): age -= 1
        return age

tom = Student("Tompson", "Tom",datetime(1990,10,10), "123456789",
              "Belgian", "Male" )
jean = Student( "Jacques", "Jean",datetime(1845,10,15), "157862135",
                "France", "Male")

tom.height = 185  #het kan, maar niet doen!!! niets achteraf bijvoegen!!! Blokkeren met slots
print (tom.height)
#print(jean.height)
print (f"Name: {tom.first_name} {tom.last_name} and age: {tom.age}")
#tom.age = 18 kan niet ingesteld worden, is slimme functie