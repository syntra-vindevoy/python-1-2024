from pyclbr import Class
from time import sleep

from src.logs.log_manager import LogManager
from src.logs.logging_decorator import trace_func
from src.logs.logging_level import LoggingLevel
from src.logs.type_logger_enum import TypeLogger


class Klok:
    def __init__(self) -> None:
        pass
    @trace_func
    def start(self):
       for i in range(5):
           sleep(1)
    def stop(self):
        pass



def main():
    logger = LogManager.get_logger(type_logger=TypeLogger.Console, name=Class.__name__)
    logger.set_log_level(LoggingLevel.INFO)
    logger.info("Hello world logger Console Info")
    logger.error("Hello world logger Console Error")
    logger.debug("Hello world logger Console Debug")
    logger.critical("Hello world logger Console Critical")

    logger2 = LogManager.get_logger(type_logger=TypeLogger.FILE, name=__name__)
    logger2.info("Hello world logger Console Info")
    logger2.error("Hello world logger Console Error")
    logger2.debug("Hello world logger Console Debug")
    logger2.critical("Hello world logger Console Critical")

    logger3 = LogManager.get_logger(type_logger=TypeLogger.FILE, name=__name__)
    logger3.add_logger(logger)
    logger3.info("Hello world logger Console Info 3")
    logger3.error("Hello world logger Console Error3")
    logger3.debug("Hello world logger Console Debug3")
    logger3.critical("Hello world logger Console Critical3")

    logger4 = LogManager.get_logger(type_logger=TypeLogger.MQ, name=__name__)
    #  logger4.add_logger(logger)
    logger4.info("Hello world logger Console Info 4")
    logger4.warning("Hello world logger Console Warning4")
    logger4.error("Hello world logger Console Error4")
    logger4.debug("Hello world logger Console Debug4")
    logger4.critical("Hello world logger Console Critical4")


if __name__ == "__main__":
    klok = Klok()
    klok.start()
    main()
