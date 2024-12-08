


class Person:
    def __init__(self, person_id, name, position, salary):
        self.person_id = person_id
        self.name = name


    def get_person_details(self):
        return {
            "employee_id": self.person_id,
            "name": self.name,
        }
