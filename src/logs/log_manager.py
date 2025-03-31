from src.logs.abstract_logger import AbstractLogger
from src.logs.console_logger import ConsoleLogger
from src.logs.file_logger import FileLogger
from src.logs.logger import Logger
from src.logs.mq_logger import MQLogger
from src.logs.type_logger_enum import TypeLogger


class LogManager:

    @staticmethod
    def get_logger(*, type_logger: TypeLogger, name: str) -> Logger:
        return Logger(semantic_logger=LogManager.__make_logger(type_logger=type_logger, name=name))

    @staticmethod
    def __make_logger(*, type_logger: TypeLogger, name: str) -> AbstractLogger:
        if type_logger == type_logger.Console:
            return ConsoleLogger(name=name)
        elif type_logger == type_logger.FILE:
            return FileLogger(name=name)
        elif type_logger == type_logger.MQ:
            return MQLogger(name=name)
        raise TypeError(f"doesnt exit : {type_logger}")
