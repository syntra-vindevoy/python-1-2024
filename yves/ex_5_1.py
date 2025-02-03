import time

time_now = time.ctime()

seconds = time.time()
seconds_in_day = 60 * 60 * 24
seconds_in_hour = 60 * 60
seconds_in_minute = 60

days = seconds // seconds_in_day
seconds -= days * seconds_in_day
hours = seconds // seconds_in_hour
seconds = seconds - (hours * seconds_in_hour)
minutes = seconds // seconds_in_minute
seconds = seconds - (minutes * seconds_in_minute)


print(int(days), int(hours), int(minutes), int(seconds))
print(time_now)

