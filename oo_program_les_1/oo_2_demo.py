from datetime import datetime, date

class Student:
    def __init__(self, last_name: str, first_name: str, date_of_birth: datetime,
                 gender: str, nationality: str, national_id: str):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__nationality = nationality
        self.__national_id = national_id
#__ voor het attribuut zetten, zorgt ervoor dat dit attribuut niet meer publiek is.
    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name: str):
        if len(last_name) < 1:
            raise ValueError("Last Name must be greater than or equal to 0")

        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self.__first_name = first_name

    def age(self):
        today = date.today()

        age = today.year - self.__date_of_birth.year

        if (today.month, today.day) < (self.__date_of_birth.month, self.__date_of_birth.day):
            age -= 1
            #we hebben hier gebruik gemaakt van een tuple
            #anders was er een 1ste if voor maand te controleren
            #en dan een 2de if voor nog de dag te controleren
            #een tuple gaat automatisch controleren, als 1ste parameter gelijk is, dan moet hij naar de 2de kijken.
            #in alle andere gevallen, als de 1ste paramterer groter of kleiner is, weet hij of hij al verjaard is of niet.





tom = Student(last_name="Van de Vyver", first_name="TOM", date_of_birth=datetime(1985,10,14),
              gender="M", nationality="B", national_id="123456789")
#chiel = student(last_name="vansompel", first_name="Chiel", date_of_birth="1992-05-10",
                #gender="M", nationality="B", national_id="987654321")

print(f"Name: {tom.first_name} {tom.last_name.upper()} ")
#print(f"Name: {chiel.first_name} {chiel.last_name.upper()} ")