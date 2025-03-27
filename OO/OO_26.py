class GuesserException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class NumberTooSmall(GuesserException):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class NumberTooBig(GuesserException):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class NumberGuesser:
    def __init__(self, number: int) -> None:
        if not isinstance(number, int):
            raise ValueError("Number must be an integer")
        if number < 0 or number > 10:
            raise NumberTooSmall("Number must be between 1 and 10")
        self.number = number
    def print(self ):
        print("you g"self.number)
