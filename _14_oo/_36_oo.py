from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


# Function that returns the enum value or raises ValueError
def get_gender_enum(value: str) -> Gender:
    for gender in Gender:
        if gender.value == value:  # Compare the input with enum value
            return gender  # Return the matching enum value
    # Raise ValueError if no match found
    raise ValueError(f"'{value}' is not a valid value for Gender Enum")


# Example usage
try:
    gender_enum = get_gender_enum("Male")
    print(f"Found enum: {gender_enum}")  # Output: Found enum: Gender.MALE
except ValueError as e:
    print(e)  # Output: 'InvalidValue' is not a valid value for Gender Enum