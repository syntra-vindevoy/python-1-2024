from datetime import datetime


class Person:
    def __init__(self, name: str, email: str, date_of_birth: datetime = None):
        self.name = name
        self.email = email

        self._gender = None
        self.date_of_birth = None

    @property
    def age(self):
        x = 52
        return x

class MalePerson(Person):
    def __init__(self, name: str, email: str):
        super().__init__(name, email)
        self._gender = "Male"


yves = MalePerson("Yves", "<EMAIL>")

print(yves.name, " is " , yves.age, "old")
