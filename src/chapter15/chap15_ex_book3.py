class Time:
    """
    A class to represent a time of day.

    Methods:
        __init__(hour=0, minute=0, second=0): Initializes a new Time instance.
        __str__(): Returns the time formatted as a string "hh:mm:ss".
        __repr__(): Returns a string representation of the Time instance.
        total_seconds(): Returns the total time in seconds since midnight.
        print_time(): Prints the time formatted as "hh:mm:ss".
        time_to_int(): Converts the time to an integer number of seconds since midnight.
        add_time(hours, minutes, seconds): Adds a given duration to the current time.
        is_after(other): Checks if the current time is after another Time instance.
        __add__(other): Adds two Time instances and returns a new Time instance.
        int_to_time(seconds): Converts an integer number of seconds to a Time instance.
        make_time(hour, minute, second): Creates and returns a new Time instance.
        is_valid(): Validates the Time instance.
    """

    def __init__ (self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__ (self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def __repr__ (self):
        return f"Time({self.hour}, {self.minute}, {self.second})"

    def total_seconds (self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def print_time (self):
        s = f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
        print (s)

    def __eq__ (self, other):
        return self.hour == other.hour and self.minute == other.minute and self.second == other.second

    def __hash__ (self):
        return hash ((self.hour, self.minute, self.second))

    def time_to_int (self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def time_to_int_in (self, time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

    def add_time (self, hours, minutes, seconds):
        duration = Time.make_time (hours, minutes, seconds)
        seconds = self.time_to_int () + self.time_to_int_in (duration)
        return Time.int_to_time (seconds)

    def is_after (self, other):
        assert self.is_valid (), 'self is not a valid Time'
        assert other.is_valid (), 'self is not a valid Time'
        return self.time_to_int () > other.time_to_int ()

    def __add__ (self, other):
        seconds = self.time_to_int () + other.time_to_int ()
        return Time.int_to_time (seconds)

    @staticmethod
    def int_to_time (seconds):
        minute, second = divmod (seconds, 60)
        hour, minute = divmod (minute, 60)
        return Time.make_time (hour, minute, second)

    @staticmethod
    def make_time (hour, minute, second):
        time = Time ()
        time.hour = hour
        time.minute = minute
        time.second = second
        return time

    def is_valid (self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        if not isinstance (self.hour, int):
            return False
        if not isinstance (self.minute, int):
            return False
        return True


assert Time.make_time (1, 2, 3) == Time (1, 2, 3)


class Date:
    def __init__ (self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def __str__ (self):
        return f"{self.year}-{self.month}-{self.day}"

    def __repr__ (self):
        return f"Date({self.year}, {self.month}, {self.day})"

    def __eq__ (self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __hash__ (self):
        return hash ((self.year, self.month, self.day))

    def date_to_tuple (self, date) -> tuple:
        return date.year, date.month, date.day

    def is_after (d1, d2) -> bool:
        t1 = d1.date_to_tuple (d1)
        t2 = d1.date_to_tuple (d2)
        return t1 > t2


if __name__ == '__main__':
    start = Time.int_to_time (34800)
    print (start.print_time ())
    end = start.add_time (1, 32, 0)
    print (end)

    print (end.is_after (start))
    duration = Time (minute=132)
    print (duration)

    d = Date (2024, 9, 25)
    d2 = Date (2024, 9, 26)
    print (d.is_after (d2))
