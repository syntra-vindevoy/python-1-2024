import datetime
import time
from math import floor

import pytz


def epoch():
    tz = pytz.timezone("UTC")
    print(f"now: {datetime.datetime.now().astimezone(tz=tz)}")

    n = time.time()

    print(f"Epoch: {n}")

    n = floor(n)

    seconds = n % 60
    print(f"Seconds: {seconds}")

    n = n - seconds
    n = n / 60  # level of minutes

    minutes = int(n % 60)
    print(f"Minutes: {minutes}")

    n = n - minutes
    n = n / 60  # level of hours

    hours = int(n % 24)
    print(f"Hours: {hours}")

    n = n - hours
    n = n / 24  # level of days

    print(f"Days: {int(n)}")


if __name__ == "__main__":
    #epoch()

    today = datetime.datetime(year=2022, month=10, day=13, hour=6)
    print(today)
