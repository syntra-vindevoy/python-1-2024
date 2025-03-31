from datetime import datetime

from src.logs.abstract_logger import AbstractLogger


class FileLogger(AbstractLogger):
    def __init__(self, *, file_path: str = None, name: str = ""):
        if file_path is None:
            file_path = "log"
        self.name = name
        if name is not None:
            file_path = file_path + name

        self.file_path = file_path + datetime.now().strftime("%Y-%m-%d_%H") + ".log"

    def log(self, message: str):
        with open(self.file_path, "a") as file:
            file.write(self._make_message(message, name=self.name))

    def warning(self, message: str):
        self.log(f"WARNING : {message}")

    def error(self, message: str):
        self.log(f"ERROR : {message}")

    def info(self, message: str):
        self.log(f"INFO : {message}")

    def debug(self, message: str):
        self.log(f"DEBUG : {message}")

    def critical(self, message: str):
        self.log(f"CRITICAL : {message}")

    def exception(self, message: str):
        self.log(f"EXCEPTION : {message}")
