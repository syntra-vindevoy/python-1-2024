from datetime import date


class Human:
    __slots__ = ('__name', '__birthdate')  # Private attributes defined in slots

    def __init__(self, name: str, birthdate: date):
        self.__name = name
        self.__birthdate = birthdate


    # Name property
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_age(self) -> int:
        """Calculate the age in years based on the birthdate."""
        # Retrieve birthdate components
        birth_year = self.__birthdate.year
        birth_month = self.__birthdate.month
        birth_day = self.__birthdate.day

        # Get today's date
        today = date.today()

        # Calculate the base age
        age = today.year - birth_year

        # Adjust if birthday hasn't occurred yet this year
        if (today.month, today.day) < (birth_month, birth_day):
            age -= 1

        return age

    def __str__(self):
        return f"{self.__class__.__name__}({self.__name})"


class Student(Human):
    __slots__ = ('__student_id', '__grades')  # Private attributes specific to Student

    def __init__(self, name: str, birthdate: date, student_id: str):
        super().__init__(name, birthdate)
        self.__student_id = student_id
        self.__grades = []

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        self.__student_id = value

    @property
    def grades(self):
        return self.__grades

    def add_grade(self, grade: float):
        """Add a grade to the student's grade list."""
        self.__grades.append(grade)

    def calculate_average_grade(self) -> float:
        """Calculate the average grade from the student's grades."""
        return sum(self.__grades) / len(self.__grades) if self.__grades else 0.0

    def __str__(self):
        return f"{self.__class__.__name__}({self.__name}, {self.__student_id})"


class Teacher(Human):
    __slots__ = ('__department', '__employee_id')  # Private attributes specific to Teacher

    def __init__(self, name: str, birthdate: date, department: str, employee_id: int):
        super().__init__(name, birthdate)
        self.__department = department
        self.__employee_id = employee_id

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        self.__department = value

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        self.__employee_id = value

def __str__(self):
        return f"{self.__class__.__name__}({self.__name}, {self.__department})"

def __str__(self):
    return f"{self.__class__.__name__}({self.__name}, {self.__department})"

# Gebruik van de klassen
student = Student(name="Alice", birthdate=date(2005, 6, 15), student_id="S12345")
teacher = Teacher(name="Mr. Smith", birthdate=date(1980, 3, 10), department="Mathematics", employee_id=123456789)


print(f"Student Name: {student.name}, Age: {student.calculate_age()}, ID: {student.student_id}")
print(f"Teacher Name: {teacher.name}, Age: {teacher.calculate_age()}, Subject: {teacher.department}")

# Testen van setters
student.name = "Bob"

student.student_id = "S54321"

teacher.name = "Dr. Brown"
teacher.department = "Physics"

print(f"Updated Student: {student.name}, {student.calculate_age()}, {student.student_id}")
print(f"Updated Teacher: {teacher.name}, {teacher.calculate_age()}, {teacher.department}")
