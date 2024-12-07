
from logic.model.company import Company
from logic.model.employee import Employee
from persistence import persistence

if __name__ == "__main__":
    metos = Company()
    metos.employees = persistence.get_employees()
    for employee in metos.employees:
        print(employee.get_details())

