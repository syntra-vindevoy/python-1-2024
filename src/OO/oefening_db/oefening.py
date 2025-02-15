from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(slots=True)
class DataObject:
    id: int  # Base ID field for all derived classes


@dataclass(slots=True)
class Category(DataObject):
    name: str
    description: str


@dataclass(slots=True)
class Subcategory(DataObject):
    name: str


@dataclass(slots=True)
class Module(DataObject):
    name: str
    duration_hours: int
    course_part: str
    course: Optional['Course'] = None  # Optional reference to the parent Course


@dataclass(slots=True)
class Course(DataObject):
    title: str
    description: str
    duration_weeks: int
    is_online: bool
    modules : list[Module]



@dataclass(slots=True)
class User(DataObject):
    public_info: str
    private_info: str
    registration_date: date


@dataclass(slots=True)
class Role(DataObject):
    role_name: str


@dataclass(slots=True)
class TrainingPeriod(DataObject):
    location: str
    start_date: date
    end_date: date
    schedule_type: str
    price: float
    max_participants: int

@dataclass(slots=True)
class Enrollment(DataObject):
    period_id: int  # Reference to TrainingPeriod
    enrollment_date: date
    payment_status: Optional[str] = None

@dataclass(slots=True)
class Attendee:
    attendee_id: int
    enrollment_id: int  # Reference to Enrollment
    module_id: int  # Reference to Module
    date: date
    status: str
    notes: Optional[str] = None


if __name__ == "__main__":
    module1 = Module(id=1, name="Module 1", duration_hours=10, course_part="Part 1")
    module2 = Module(id=2, name="Module 2", duration_hours=8, course_part="Part 2")

    course = Course(
        id=1,
        title="Sample Course",
        description="This is a sample course with two modules.",
        duration_weeks=4,
        is_online=True,
        modules=[module1, module2]
    )
    module1.course = course
    module2.course = course

    print(course)
    