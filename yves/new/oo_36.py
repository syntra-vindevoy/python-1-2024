from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class Person:
    def __init__(self, name: str, gender: Gender):
        self.name = name
        self.gender = gender



def get_enum_from_value(value: str) -> Gender:
    """Find and return the enum value based on the given string."""
    for gender in Gender:
        if gender.value == value:
            return gender
    raise ValueError(f"'{value}' is not a valid value for Gender enum.")


yves = Person("Yves", Gender.MALE)

