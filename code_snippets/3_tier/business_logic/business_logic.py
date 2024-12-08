
from data_access.data_access import DataAccess# logic
from data_access.repo.person_repo import PersonRepo

class BusinessLogic:
    def __init__(self, data_access):
        self.data_access = data_access
        self.person_repo = PersonRepo()

    def process_data(self, data):
        processed_data = data.upper()  # Example logic
        self.data_access.append_data(processed_data)
        return processed_data

    def get_data(self):
        return self.data_access.get_data()

    def get_all_persons(self):
        return self.person_repo.get_all_persons()