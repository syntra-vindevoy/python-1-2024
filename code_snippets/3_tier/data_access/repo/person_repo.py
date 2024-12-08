

import os
from typing import List, Tuple

class PersonRepo:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "person.txt")

    def get_all_person_data(self) -> List[Tuple[int, str]]:
        with open(self.file_path, "r") as file:
            return [line.strip() for line in file.readlines()]