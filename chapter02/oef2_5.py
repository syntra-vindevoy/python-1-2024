import datetime
start_hour = 6
start_minute = 52
fastpace_sec = (7 * 60) + 12
slowpace_sec = (8 * 60) + 15
slow_laps = 2
fast_laps = 3

start_hour_sec = (6 * 3600) + (52*60)
finish_sec = start_hour_sec + (slow_laps * slowpace_sec) + (fast_laps * fastpace_sec)

finish_hour = finish_sec / 3600
remainder = finish_sec % 3600
finish_minute = remainder / 60
finish_sec = remainder % 3600


print(start_hour_sec)
print(fastpace_sec)
print(slowpace_sec)
print(finish_sec)
print(finish_hour)
print(finish_minute)
print(finish_sec)


-----------

