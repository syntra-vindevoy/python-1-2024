from src.OO.developer import Developer
from src.OO.employee import Employee


class Manager(Employee):

    def __init__(self, first, last, pay):
        super().__init__(first, last, pay)
        self.employees = []

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def __repr__(self):
        return f"Manager('{self.id} {self.first}', '{self.last}', {self.pay}, {self.employees})"

    def __str__(self):
        return f"Manager('{self.id} {self.first}', '{self.last}', {self.pay}, {self.employees})"


if __name__ == "__main__":
    mng = Manager("Benoit", "Goethals", 23)
    emp_1 = Employee("John", "Doe", 1000)
    emp_2 = Employee("Jane", "Doeter", 1000)
    mng.add_employee(emp_1)
    mng.add_employee(emp_2)
    print(mng.employees)

    eric = Developer("Eric", "Idle", 1000)
    eric.add_prog_lang("Python")
    eric.add_prog_lang("Java")
    mng.add_employee(eric)

    john = Developer("John", "Doe", 1000)
    john.add_prog_lang("Python")
    john.add_prog_lang("Java")
    mng.add_employee(john)

    print(mng.employees)

    mng2 = Manager("Benoit2", "Goethals", 23)
    emp_1 = Employee("John2", "Doe", 1000)
    emp_2 = Employee("Jane3", "Doeter", 1000)
    mng2.add_employee(emp_1)
    mng2.add_employee(emp_2)
    print(mng2.employees)

    eric = Developer("Eric2", "Idle", 1000)
    eric.add_prog_lang("Python")
    eric.add_prog_lang("Java")
    mng2.add_employee(eric)

    john = Developer("John2", "Doe", 1000)
    john.add_prog_lang("Python")
    john.add_prog_lang("Java")
    mng2.add_employee(john)

    mng.add_employee(mng2)

    for emp in mng.employees:
        print(emp)
        if isinstance(emp, Manager):
            for emp2 in emp.employees:
                print(emp2)
