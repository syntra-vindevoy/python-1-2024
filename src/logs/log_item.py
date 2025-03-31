from datetime import datetime

from src.logs.logging_level import LoggingLevel


class LogItem:
    """
    A class representing a single log item with level, message, and timestamp.
    """

    def __init__(self, *, message: str, level: LoggingLevel):
        """
        Initializes a LogItem instance with a message and log level.

        :param message: The log message.
        :param level: The level of the log (e.g., 'DEBUG', 'INFO', 'WARNING', etc.), default is 'INFO'.
        """
        self.timestamp = datetime.now()  # Records the current timestamp for the log
        self.level = level  # Converts the log level to uppercase for consistency
        self.message = message  # The log message

    def __str__(self):
        """
        Returns the string representation of the LogItem.

        Format: [<timestamp>] <LEVEL>: <message>
        """
        return f"[{self.timestamp}] {self.level}: {self.message}"

    def to_dict(self):
        """
        Converts the LogItem into a dictionary for serialization or structured logging.

        :return: A dictionary containing the log's details.
        """
        return {
            "timestamp": self.timestamp.isoformat(),  # Timestamp as an ISO 8601 string
            "level": self.level,
            "message": self.message
        }
