from src.logs.abstract_logger import AbstractLogger
from src.logs.console_logger import ConsoleLogger
from src.logs.logging_level import LoggingLevel


class Logger(AbstractLogger):

    def __init__(self, *, semantic_logger: AbstractLogger = ConsoleLogger()):
        self.__semantic_logger: list[AbstractLogger] = [semantic_logger]
        self.logging_level = LoggingLevel.CRITICAL

    def add_logger(self, logger: AbstractLogger):
        self.__semantic_logger.append(logger)

    def log(self, message: str):

        for logger in self.__semantic_logger:
            logger.log(message)

    def error(self, message: str):
        if self.logging_level.value >= LoggingLevel.ERROR.value:
            for logger in self.__semantic_logger:
                logger.error(message)

    def warning(self, message: str):
        if self.logging_level.value >= LoggingLevel.WARNING.value:
            for logger in self.__semantic_logger:
                logger.warning(message)

    def info(self, message: str):
        if self.logging_level.value >= LoggingLevel.INFO.value:
            for logger in self.__semantic_logger:
                logger.info(message)

    def debug(self, message: str):
        if self.logging_level.value >= LoggingLevel.DEBUG.value:
            for logger in self.__semantic_logger:
                logger.debug(message)

    def critical(self, message: str):
        if self.logging_level.value >= LoggingLevel.CRITICAL.value:
            for logger in self.__semantic_logger:
                logger.critical(message)

    def exception(self, message: str):
        for logger in self.__semantic_logger:
            logger.exception(message)

    def set_log_level(self, logging_level: LoggingLevel):
        self.logging_level = logging_level
