class Company:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Company, cls).__new__(cls)
        return cls._instance

    def __init__(self, employees=None):
        if not hasattr(self, 'initialized'):  # Ensure __init__ is only called once
            self.name = "Metos"
            self.employees = employees if employees is not None else []
            self.initialized = True


    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def get_employee_count(self):
        return len(self.employees)

    def __str__(self):
        return f"Company: {self.name}, Employees: {self.get_employee_count()}"