from copy import copy


def increment_time (time, hours, minutes, seconds):
    time.hour += hours
    time.minute += minutes
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1


def add_time (time, hours, minutes, seconds):
    total = copy (time)
    increment_time (total, hours, minutes, seconds)
    return total


class Time:
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


def make_time (hour, minute, second):
    time = Time ()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time


"""
14.12.1. Exercise
Write a function called subtract_time that takes two Time objects and returns the interval between them in seconds –
assuming that they are two times during the same day.
"""


def subtract_time (t1: Time, t2: Time) -> Time:
    return t1.total_seconds () - t2.total_seconds ()


assert subtract_time (Time (1, 2, 3), Time (1, 2, 3)) == 0
"""
14.12.2. Exercise
Write a function called is_after that takes two Time objects and returns True if the first time is later in the day than the second, and False otherwise.
  """


def is_after (t1, t2):
    """
    Checks whether`t1` is after`t2`.

    >> > is_after (make_time (3, 2, 1), make_time (3, 2, 0))
    True
    >> > is_after (make_time (3, 2, 1), make_time (3, 2, 1))
    False
    >> > is_after (make_time (11, 12, 0), make_time (9, 40, 0))
    True
    """
    return t1.total_seconds () > t2.total_seconds ()


assert is_after (Time (1, 2, 3), Time (1, 2, 3)) is False

"""
14.12.3. Exercise
Here’s a definition for a Date class that represents a date – that is, a year, month, and day of the month.
Write a function called make_date that takes year, month, and day as parameters, makes a Date object,
 assigns the parameters to attributes, and returns the result the new object. Create an object that represents
  June 22, 1933.
Write a function called print_date that takes a Date object, uses an f-string to format the attributes, 
and prints the result. If you test it with the Date you created, the result should be 1933-06-22.
Write a function called is_after that takes two Date objects as parameters and returns True if the first 
comes after the second. Create a second object that represents September 17, 1933, 
and check whether it comes after the first object.
Hint: You might find it useful to write a function called date_to_tuple that takes a Date object and returns a 
tuple that contains its attributes in year, month, day order.
"""


class Date:
    def __init__ (self, year=1968, month=1, day=14):
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


def make_date (year, month, day):
    date = Date ()
    date.year = year
    date.month = month
    date.day = day
    return date


assert make_date (1933, 6, 22) == Date (1933, 6, 22)


def print_date (date):
    print (f"{date.year}-{date.month}-{date.day}")


def date_to_tuple (date):
    return date.year, date.month, date.day


def is_after (d1: Date, d2: Date) -> bool:
    t1 = date_to_tuple (d1)
    t2 = date_to_tuple (d2)
    return t1 > t2


assert is_after (make_date (1933, 6, 22), make_date (1933, 9, 17)) is False
assert is_after (Date (1933, 6, 22), Date (1933, 6, 3)) is True
