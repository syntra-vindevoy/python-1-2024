
from data_access.data_access import DataAccess# logic
from data_access.repo.person_repo import PersonRepo

class BusinessLogic:
    def __init__(self, data_access):
        self.data_access = data_access
        self.person_repo = PersonRepo()

    def get_all_persons(self):
        return self.person_repo.get_all_persons()
    
    def add_person(self, name:str):
        self.person_repo.add_person(name.title())