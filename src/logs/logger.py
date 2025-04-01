from src.logs.abstract_logger import AbstractLogger
from src.logs.console_logger import ConsoleLogger
from src.logs.logging_level import LoggingLevel


class Logger(AbstractLogger):
    def __init__(self, *, loggers: list[AbstractLogger] = None, logging_level: LoggingLevel = LoggingLevel.CRITICAL):
        self.__loggers: list[AbstractLogger] = loggers if loggers else [ConsoleLogger()]
        self.logging_level: LoggingLevel = logging_level

    def add_logger(self, logger: AbstractLogger):
        self.__loggers.append(logger)

    def _log_if_level_allowed(self, level: LoggingLevel, method_name: str, message: str):
        if self.logging_level.value >= level.value:
            for logger in self.__loggers:
                getattr(logger, method_name)(message)

    def log(self, message: str):
        self._log_if_level_allowed(LoggingLevel.INFO, 'log', message)

    def error(self, message: str):
        self._log_if_level_allowed(LoggingLevel.ERROR, 'error', message)

    def warning(self, message: str):
        self._log_if_level_allowed(LoggingLevel.WARNING, 'warning', message)

    def info(self, message: str):
        self._log_if_level_allowed(LoggingLevel.INFO, 'info', message)

    def debug(self, message: str):
        self._log_if_level_allowed(LoggingLevel.DEBUG, 'debug', message)

    def critical(self, message: str):
        self._log_if_level_allowed(LoggingLevel.CRITICAL, 'critical', message)

    def exception(self, message: str):
        for logger in self.__loggers:
            logger.exception(message)

    def set_log_level(self, logging_level: LoggingLevel):
        self.logging_level = logging_level