
from data_access.repo.person_mapper import PersonMapper

class DomainController:
    def __init__(self, person_mapper: PersonMapper):
        self.person_repo = person_mapper

    def get_all_persons(self):
        return self.person_repo.get_all_persons()
    
    def add_person(self, name:str):
        self.person_repo.add_person(name.title())

    def delete_person(self, person_id:int):
        self.person_repo.delete_person(person_id)