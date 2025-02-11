from dataclasses import dataclass
from datetime import date

from docutils.nodes import field


@dataclass(slots=True)
class Human:
    name: str

    birthdate: date

    def calculate_age(self) -> int:
        """Calculate the age in years based on the birthdate."""
        # Retrieve birthdate components
        birth_year = self.birthdate.year
        birth_month = self.birthdate.month
        birth_day = self.birthdate.day

        # Get today's date
        today = date.today()

        # Calculate the base age
        age = today.year - birth_year

        # Adjust if birthday hasn't occurred yet this year
        if (today.month, today.day) < (birth_month, birth_day):
            age -= 1

        return age


@dataclass(slots=True)
class Student(Human):
    student_id: str
    grades: list =  field(default_factory=list)

    def add_grade(self, grade: float):
        """Add a grade to the student's grade list."""
        self.grades.append(grade)

    def calculate_average_grade(self) -> float:
        """Calculate the average grade from the student's grades."""
        return sum(self.grades) / len(self.grades) if self.grades else 0.0



@dataclass
class Wachtwoord:
    gebruiker: str
    wachtwoord: str = field(repr=False)  # Niet zichtbaar bij printen

w = Wachtwoord("admin", "geheim123")
print(w)  # Wachtwoord(gebruiker='admin')


@dataclass
class Teacher(Human):
    department: str
    employee_id: int

@dataclass
class Cirkel:
    straal: float
    oppervlakte: float = field(init=False)  # Wordt NIET in __init__ gezet

    def __post_init__(self):
        self.oppervlakte = 3.1415 * self.straal ** 2  # Bereken de oppervlakte

c = Cirkel(10)
print(c.oppervlakte)  # 314.15

# Gebruik van de klassen
student = Student(name="Alice", birthdate=date(2005, 6, 15), student_id="S12345", grades=[])
student.add_grade(10)
#student.age = 10
teacher = Teacher("Mr. Smith", date(1980, 3, 10), "Mathematics", 123456789)

print(f"Student Name: {student.name}, Age: {student.calculate_age()}, ID: {student.student_id}")
print(f"Teacher Name: {teacher.name}, Age: {teacher.calculate_age()}, Subject: {teacher.department}")

# Testen van setters
student.name = "Bob"

student.student_id = "S54321"

teacher.name = "Dr. Brown"
teacher.department = "Physics"

print(f"Updated Student: {student.name}, {student.calculate_age()}, {student.student_id}")
print(f"Updated Teacher: {teacher.name}, {teacher.calculate_age()}, {teacher.department}")

st1 = Student(name="Alice", birthdate=date(2005, 6, 15), student_id="S12345")

print(st1)