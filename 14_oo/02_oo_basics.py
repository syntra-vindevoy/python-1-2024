from datetime import datetime


class Student:
    def __init__(self, last_name:str, first_name:str, date_of_birth:datetime.date, national_id:str, nationality:str, gender:str):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__date_of_birth = date_of_birth
        self.__national_id = national_id
        self.__nationality = nationality
        self.__gender = gender

    @property       #Getter
    def last_name(self):
        return self.__first_name

    @last_name.setter       #Setter
    def last_name(self, last_name:str):
        if len(last_name) < 1:
            raise ValueError("Last name must be at least 1 character long")
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self.__first_name = first_name


    def age(self):
        return datetime.now() - self.__date_of_birth



thomas = Student("Meersschaut",
                "Thomas",
                "1988-02-16",
                "1234567890",
                "B",
                "M")

jane = Student()

print(f"Name: {thomas.first_name} {thomas.last_name.upper()}")
print(f"Name: {jane.first_name} {jane.last_name.upper()}")

thomas.height = 170     #It's possible to add a property to the class, without changing the actual class, but it's not considered a good practice
print(thomas.height)
thomas.nationality = ("PH")
print(thomas.nationality)




