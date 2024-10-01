start_day = 0
start_hours = 6
start_minutes = 52
start_seconds = 0

start_seconds = (start_hours * 60 * 60) + (start_minutes * 60) + start_seconds

time_1_hours = 0
time_1_minutes = 8
time_1_seconds = 15
miles_1 = 1

time_2_hours = 0
time_2_minutes = 7
time_2_seconds = 12
miles_2 = 3

time_3_hours = 0
time_3_minutes = 8
time_3_seconds = 15
miles_3 = 1

seconds_1 = ((time_1_hours * 60 * 60) + (time_1_minutes * 60) + time_1_seconds) * miles_1
seconds_2 = ((time_2_hours * 60 * 60) + (time_2_minutes * 60) + time_2_seconds) * miles_2
seconds_3 = ((time_3_hours * 60 * 60) + (time_3_minutes * 60) + time_3_seconds) * miles_3

total_seconds = start_seconds + seconds_1 + seconds_2 + seconds_3

total_minutes = total_seconds // 60
total_seconds = total_seconds - (total_minutes * 60)
total_hours = total_minutes // 60
total_minutes = total_minutes - (total_hours * 60)

print(total_hours)
print(total_minutes)
print(total_seconds)


# Other solution by Sem

total_seconds = start_seconds + seconds_1 + seconds_2 + seconds_3

hours = total_seconds / 3600
hours = round(int(hours), 0)
minutes = round((total_seconds % 3600) / 60, 0)
seconds = total_seconds - hours * 3600 - minutes * 60

print(hours, minutes, seconds)


# Using more libs, second year example

import datetime

start = datetime.timedelta(hours=6, minutes=52)
slow = datetime.timedelta(minutes=8, seconds=15)
fast = datetime.timedelta(minutes=7, seconds=12)

print(start + slow * 2 + fast * 3)

two_hours_later = datetime.timedelta(hours=2)
print(datetime.datetime.now() + two_hours_later)