


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


    def get_person_details(self):
        return {
            "id": self.id,
            "name": self.name,
        }
