

class GuesserException(Exception):
    def __init__(self, message:str) -> None:
        super().__init__(message)



class NumberGuesserException(GuesserException):
    def __init__(self, message:str) -> None:
        super().__init__(message)


class NumberTooSmallException(NumberGuesserException):
    def __init__(self, message:str) -> None:
        super().__init__(message)


class NumberTooBigException(NumberGuesserException):
    def __init__(self, message:str) -> None:
        super().__init__(message)

class NumberTypeException(NumberGuesserException):
    def __init__(self, message:str) -> None:
        super().__init__(message)


class NumberGuesser:
    def __init__(self, number:int) -> None:
        if not isinstance(number, int):
            raise NumberTypeException("Number must be an integer")

        if number < 0:
            raise NumberTooSmallException("Number must be greater than 0")

        if number > 100:
            raise NumberTooBigException("Number must be less than 100")

        self.number = number

    def print(self):
        print("You guessed the number", self.number)

