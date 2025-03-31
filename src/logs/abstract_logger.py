from abc import ABC, abstractmethod
from datetime import datetime


class AbstractLogger(ABC):

    def _make_message(self, message, name: str = ""):
        return f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {name} - {message}\n"

    @abstractmethod
    def log(self, message):
        pass

    @abstractmethod
    def info(self, message):
        pass

    @abstractmethod
    def error(self, message):
        pass

    @abstractmethod
    def debug(self, message):
        pass

    @abstractmethod
    def warning(self, message):
        pass

    @abstractmethod
    def critical(self, message):
        pass

    @abstractmethod
    def exception(self, message: str):
        pass
