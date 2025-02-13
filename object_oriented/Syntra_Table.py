from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class DataObject:
    id = int

@dataclass(slots=True)
class User (DataObject):
    public_info: str
    title: str
    description: str

@dataclass(slots=True)
class Categories (DataObject):
    Categories_id : int
    name : str
    description : str

@dataclass(slots=True)
class TrainingPeriods(DataObject):
    period_id : int
    course_id : int
    location: str
    start_date : datetime
    end_date : datetime
    schedule_type : str
    price: float
    max_participants : int

@dataclass(slots=True)
class Attendance(DataObject):
    attendance_id : int
    enrollment_id : int
    module_id : int
    date: datetime
    status: bool
    notes: str

@dataclass(slots=True)
class Subcategories(DataObject):
    subcategory_id : int
    category_id : int
    name : str

@dataclass(slots=True)
class Coursrequirements(DataObject):
    requirement_id : int
    course_id : int
    description : str

@dataclass(slots=True)
class Modules(DataObject):
    module_id : int
    course_id : int
    name : str
    duration_hours : int
    course_part: int
    course = [Courses]


@dataclass(slots=True)
class Courses(DataObject):
    course_id : int
    subcategory_id : int
    title: str
    description: str
    duration_weeks : int
    is_online: bool
    modules = [Modules]

@dataclass(slots=True)
class Roles(DataObject):
    role_id : int
    role_name : str

@dataclass(slots=True)
class Enrollments(DataObject):
    enrollment_id : int
    user_id : int
    period_id : int
    enrollment_date : datetime
    payement_status: bool

