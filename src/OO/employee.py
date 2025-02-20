class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str) -> object:
        """
        Creates an instance of the class from a single string containing
        employee details separated by hyphens. This method is a
        convenient alternative to the standard class constructor for
        parsing and creating instances from a delimited string.

        Args:
            emp_str: A string containing the employee's first name, last
                name, and pay, separated by hyphens (e.g., "John-Doe-50000").

        Returns:
            An instance of the class created with the parsed details.
        """
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        """
        Determines if a given day is a workday.

        This static method evaluates whether a specific day of the week
        is considered a workday. It assumes Saturday and Sunday are weekends.

        Args:
            day (datetime.date): The day to check.

        Returns:
            bool: False if the day is Saturday or Sunday, True otherwise.
        """

        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


if __name__ == '__main__':
    emp_1 = Employee('Corey', 'Schafer', 50000)
    emp_2 = Employee('Test', 'Employee', 60000)

    Employee.set_raise_amt(1.05)

    print(Employee.raise_amt)
    print(emp_1.raise_amt)
    print(emp_2.raise_amt)

    emp_str_1 = 'John-Doe-70000'
    emp_str_2 = 'Steve-Smith-30000'
    emp_str_3 = 'Jane-Doe-90000'

    first, last, pay = emp_str_1.split('-')

    # new_emp_1 = Employee(first, last, pay)
    new_emp_1 = Employee.from_string(emp_str_1)

    print(new_emp_1.email)
    print(new_emp_1.pay)

    import datetime

    my_date = datetime.date(2016, 7, 11)

    print(Employee.is_workday(my_date))
