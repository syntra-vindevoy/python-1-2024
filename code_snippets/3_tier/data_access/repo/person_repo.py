

import os
from typing import List, Tuple
from business_logic.model.person import Person

class PersonRepo:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "persons.csv")


    def get_all_persons(self) -> List[Person]:
        with open(self.file_path, "r") as file:
            persons = []
            for line in file:
                line_split = line.strip().split(",")
                if len(line_split) == 2 and line_split[0].strip().isdigit():
                    persons.append(Person(
                        id=int(line_split[0].strip()), 
                        name=line_split[1].strip(),
                    ))
            return persons
        
        
    def add_person(self, name: str):
        persons = self.get_all_persons()
        next_id = max([person.id for person in persons]) + 1 if persons else 1
        with open(self.file_path, "a") as file:
            file.write(f"{next_id},{name}\n")


