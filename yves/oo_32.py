class Person:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    @staticmethod
    def lives_on_planet(where: str = "Earth"):
        return where