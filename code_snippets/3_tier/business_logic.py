
from data_access import DataAccess# logic

class BusinessLogic:
    def __init__(self, data_access):
        self.data_access = data_access

    def process_data(self, data):
    # Business logic processing
        processed_data = data.upper() # Example logic
        self.data_access.append_data(processed_data)
        return processed_data
    
    def get_data(self):
        return self.data_access.get_data()