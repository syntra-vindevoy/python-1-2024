
# data
import os

class DataAccess:

    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "data.txt")

    def overwrite_data(self, data):
        with open(self.file_path, "w") as file:
            file.write(data + "\n")
            
    def append_data(self, data):
        with open(self.file_path, "a") as file:
            file.write(data + "\n")

    def get_data(self):
        with open(self.file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
