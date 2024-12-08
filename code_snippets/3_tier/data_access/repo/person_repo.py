

import os
from typing import List, Tuple
from business_logic.model.person import Person

class PersonRepo:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "persons.txt")

    def get_all_persons(self) -> List[Person]:
        with open(self.file_path, "r") as file:
            return [Person(name=line.strip()) for line in file.readlines()]
        
    def add_person(self, name: str):
        with open(self.file_path, "a") as file:
            file.write(name + "\n")


