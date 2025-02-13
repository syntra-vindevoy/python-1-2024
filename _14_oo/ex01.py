# Class Categories:
# def __init__(self,
#              category_id: int,
#              name: str,
#              description: str):
#         self.category_id = category_id
#         self.name = name
#         self.description = description
#
# class SubCategories:
#     def __init__(self,
#                  subcategory_id: int,
#                  category_id: int,
#                  name: str):
#         self.subcategory_id = subcategory_id
#         super().__init__(category_id)
#         self.name = name
#
# class Courses:
#     def __init__(self,
#                  course_id: int,
#                  subcategory_id: int,
#                  title: str,
#                  description: str,
#                  duration_weeks: int,
#                  is_online: bool):
#         self.course_id = course_id
#         super().__init__(subcategory_id)
#         self.title = title
#         self.description = description
#         self.duration_weeks = duration_weeks
#         self.is_online = is_online
#
# class Modules:
#     def __init__(self,
#                  module_id: int,
#                  course_id: int,
#                  name: str,
#                  duration_hours: int,
#                  course_part: int):
#         self.module_id = module_id
#         super().__init__(course_id)
#         self.name = name
#         self.duration_hours = duration_hours
#         self.course_part = course_part
#
# class Roles:
#     def __init__(self,
#                  role_id: int,
#                  role_name: str):
#         self.role_id = role_id
#         self.role_name = role_name

From dataclasses import dataclass
from datetime import datetime

@dataclass(slots=True)
class DataObject:
    id: int

class User(DataObject):
    id: int
    public_info: str
    private_info: str
    registration_date: datetime

class Student(User):
    pass

class Teacher(User):
    pass