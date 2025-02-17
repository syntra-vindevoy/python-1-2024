from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

@dataclass(slots=True)
class DataObject:
    id:int

@dataclass(slots=True)
class Student(DataObject):
    public_info: str
    private_info: str
    registration_date: datetime = datetime.now()

@dataclass(slots=True)
class User(DataObject):
    public_info: str
    private_info: str

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
    tittle: str
    description: str
    modules: list[Module]|None = None

if __name__ == "__main__":
    s = Student(id=1, public_info="Tom", private_info="123456789", registration_date=datetime.now() )

    m1 = Module(id=1, name="leren programeren", duration=24 , course=c)
    m2 = Module(id=2, name="functioneel programeren", duration=36)

    c = Course(id=1, tittle="Python", description="Python is de meest gebruikende programmeertaal",
               modules=[m1, m2])
    #m1.course = c
    m2.course = c

    c.modules = []
    c.modules.append(m1)
    c.modules.append(m2)

    for m in c.modules:
        print(m.name)
