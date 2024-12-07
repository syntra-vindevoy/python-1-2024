class Employee:
    def __init__(self,employee_id,name_first, name_last, position):
        self.employee_id = employee_id
        self.name_first = name_first
        self.name_last = name_last
        self.position = position

    def get_details(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Position: {self.position}"
    