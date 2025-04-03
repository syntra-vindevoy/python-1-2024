from enum import Enum


class EnumEx(Enum):
    @classmethod
    def values(cls) -> list["EnumEx"]:
        return [member.value for member in cls]

    @classmethod
    def from_value(cls, *, value: str) -> "EnumEx":
        for member in cls:
            if member.value == value:
                return member

        raise ValueError(f"'{value}' is not a valid value for {cls.__name__}.")
