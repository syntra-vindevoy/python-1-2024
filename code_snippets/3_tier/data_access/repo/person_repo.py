

import os
from typing import List
from business_logic.model.person import Person

class PersonRepo:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "persons.csv")
        self.persons = self._load_persons()

    def _load_persons(self) -> List[Person]:
        persons = []
        with open(self.file_path, "r") as file:
            for line in file:
                line_split = line.strip().split(",")
                if len(line_split) == 2 and line_split[0].strip().isdigit():
                    persons.append(Person(
                        id=int(line_split[0].strip()), 
                        name=line_split[1].strip(),
                    ))
        return persons

    def get_all_persons(self) -> List[Person]:
        return self.persons




    def add_person(self, name: str):

        def _add_person_to_list(person: Person):
            self.persons.append(person)

        def _add_person_to_file(person: Person):
            with open(self.file_path, "a") as file:
                file.write(f"{person.id},{person.name}\n")

        next_id = max([person.id for person in self.persons]) + 1 if self.persons else 1  # Changed line
        new_person = Person(id=next_id, name=name.strip())
        _add_person_to_file(new_person)
        _add_person_to_list(new_person)


    def delete_person(self, person_id: int):

        def _delete_person_from_list(person_id: int):
            self.persons = [person for person in self.persons if person.id != person_id]
        
        def _delete_person_from_file(person_id: int):
            with open(self.file_path, "w") as file:
                for person in self.persons:
                    if person.id != person_id:
                        file.write(f"{person.id},{person.name}\n")
        _delete_person_from_file(person_id)
        _delete_person_from_list(person_id)