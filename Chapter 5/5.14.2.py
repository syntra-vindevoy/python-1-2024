#The time module provides a function, also called time, that returns returns the number
#of seconds since the “Unix epoch”, which is January 1, 1970, 00:00:00 UTC (Coordinated Universal Time).
#Use integer division and the modulus operator to compute the number of days since January 1, 1970
#and the current time of day in hours, minutes, and seconds.

from time import time

now = time()
print(now)

#seconds to days: 60 sec * 60 min * 24 = 86400 sec
seconds_in_a_day = 60*60*24
assert seconds_in_a_day == 86400

#calculates the number of days since Unix epoch up until today
number_of_days = now // seconds_in_a_day
print(number_of_days)

seconds_left = now % seconds_in_a_day
print(seconds_left)

hours = seconds_left // (60 * 60)
minutes = (seconds_left % (60 * 60) // 60)
seconds = seconds_left % 60

print(f"Since the 'Unix epoch', {number_of_days} days, {hours} hours, {minutes} minutes, {seconds:.2f} seconds have passed.")