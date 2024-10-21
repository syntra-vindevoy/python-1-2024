import time
current_time = int(time.time())
days_since_epoch = current_time // 3600 //24
print(days_since_epoch)

current_time_of_day_seconds = current_time % (3600 * 24)
print(current_time_of_day_seconds)
current_time_of_day_seconds = current_time_of_day_seconds + 7200 #UTC zone for Brussels = UTC + 2
print(current_time_of_day_seconds)

hours = current_time_of_day_seconds // 3600
minutes = (current_time_of_day_seconds % 3600) // 60
seconds = current_time_of_day_seconds % 60
