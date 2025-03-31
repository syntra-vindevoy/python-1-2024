from src.logs.abstract_logger import AbstractLogger


class ConsoleLogger(AbstractLogger):
    def __init__(self, *, name: str = ""):
        self._name = name

    def log(self, message: str):
        print(self._make_message(message, self._name))

    def error(self, message: str):
        self.log(message)

    def warning(self, message: str):
        self.log(message)

    def info(self, message: str):
        self.log(message)

    def debug(self, message: str):
        self.log(message)

    def critical(self, message: str):
        self.log(message)

    def exception(self, message: str):
        self.log(message)

    def __str__(self):
        return "ConsoleLogger"
