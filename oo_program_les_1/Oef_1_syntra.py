from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

# id komt in alle klasses voor, dus dan gaan we dat in de master klasse zetten.
# initieel de bedoeling om dataclass slots true niet altijd opnieuw te moeten gebruiken. maar dat werkte niet.
@dataclass(slots=True)
class DataObject:
    id: int


@dataclass(slots=True)
class User(DataObject):
    public_info: str
    private_info: str
    registration_date : datetime

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


if __name__ == '__main__':
    s = Student(id=1, public_info="Bert Geeroms", private_info="bert_geeroms@hotmail.com",
                registration_date= datetime(1985,9,7))

    c = Course(id=1, title="Python developer", description="bla bla bla")

    m1 = Module(id=1, name="programmeren in python", duration=24, course = c)
    m2 = Module(id=2, name="functioneel programmeren in python", duration=36)

    m1.course = c
    m2.course = c

    c.modules = []
    c.modules.append(m1)
    c.modules.append(m2)
