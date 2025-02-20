from src.OO.developer import Developer
from src.OO.employee import Employee


class EmployeeList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_all_employees(self):
        return self

    def get_employee_by_id(self, id):
        for employee in self:
            if employee.id == id:
                return employee

    def add_employee(self, employee: Employee):
        self.append(employee)

    def remove_employee(self, employee: Employee):
        if employee in self:
            self.remove(employee)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()


if __name__ == "__main__":
    emp_list = EmployeeList()
    emp_list.add_employee(Employee("Benoit", "Goethals", 23))
    emp_list.add_employee(Employee("Liv", "Goethals", 23))
    emp_list.add_employee(Employee("Ilse", "Goethals", 14))
    d = Developer("Ben", "Goethals", 23)
    d.add_prog_lang("Python")
    d.add_prog_lang("Java")
    emp_list.add_employee(d)
    print(emp_list)
    for emp in emp_list:
        print(emp)
    emp_list.remove_employee(Employee("Liv", "Goethals", 23))
    print(emp_list)
    emp = emp_list.get_employee_by_id(1)
    print(emp)
    emp_list.remove_employee(emp)
    emp = emp_list.get_employee_by_id(1)
    print(emp)
    print(emp_list)

    list_emp = [x for x in emp_list if isinstance(x, Developer)]
    for emp in list_emp:
        print(emp)

# print(help(EmployeeList))
