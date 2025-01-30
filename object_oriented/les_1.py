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
    def __init__(self, last_name: str, first_name: str, date_of_birth: str,
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

tom = Student("Tompson", "Tom","1990-05-07", "123456789",
              "Belgian", "Male" )
jean = Student( "Jacques", "Jean","1990-05-10", "157862135",
                "France", "Male")

tom.height = 185  #het kan, maar niet doen!!! niets achteraf bijvoegen!!!
print (tom.height)
#print(jean.height)
print (f"Name: {tom.first_name} {tom.last_name}")