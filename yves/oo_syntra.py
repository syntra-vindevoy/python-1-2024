from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime



@dataclass(slots=True)
class DataObject:
    id: int

@dataclass(slots=True)
class User(DataObject):
    public_info: str
    private_info: str
    registration_date: datetime.date

@dataclass(slots=True)
class Student(User):
    pass

@dataclass(slots=True)
class Teacher(User):
    pass

@dataclass(slots=True)
class Module(DataObject):
    name: str
    duration: int
    course: Course = None

@dataclass(slots=True)
class Course(DataObject):
    title: str
    description: str
    modules: list[Module] = None




if __name__ == "__main__":
    s = Student(id=1, public_info="Yves Vindevogel", private_info="yves@vindevogel.net",
                registration_date=datetime(2025, 2, 13))

    c = Course(id=1, title="Python Developer",
               description="Python is de meest gebruikte programmeertaal")

    m1 = Module(id=1, name="Leren Programmeren in Python", duration= 24, course=c)
    m2 = Module(id=2, name="Functioneel Programmeren in Python", duration=36)

    m2.course = c

    c.modules = []
    c.modules.append(m1)
    c.modules.append(m2)

    for m in c.modules:
        print(m.name)

    # t = Teacher()
