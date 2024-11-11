#The time module provides a function, also called time,
# that returns the number of seconds since the “Unix epoch”,
# which is January 1, 1970, 00:00:00 UTC (Coordinated Universal Time).

from time import time

now = time()

# This calculates the days since CUT

days = now / 86400

# This calculates the hours since CUT

rest_days = now % 86400

hours = rest_days / 3600

# This calculates the minutes since CUT

rest_hours = rest_days % 3600

minutes = rest_hours / 60

# This calculates the seconds since CUT

seconds = rest_hours % 60

print(int(days)," ", int(hours), int(minutes), int(seconds), )