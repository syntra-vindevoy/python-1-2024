items = ['a', 'b', 'c']
for i in range(10):
    print(items[i % len(items)])
    print (i, len(items))

a = True
b = False
result = a ^ b
print(result)  # Output: True



import time

# Get the current time since the epoch in seconds
current_time = int(time.time())
print('Current_time:', current_time)

# Calculate the number of days since January 1, 1970
seconds_per_day = 86400  # 24 * 60 * 60
days_since_epoch = current_time // seconds_per_day
print('days_since_epoch:', days_since_epoch)

# Calculate the current time of day in seconds
current_time_of_day_seconds = current_time % seconds_per_day
print('current_time_of_day_seconds:', current_time_of_day_seconds)

# Calculate hours, minutes, and seconds
hours = current_time_of_day_seconds // 3600  # 60 * 60
minutes = (current_time_of_day_seconds % 3600) // 60
seconds = current_time_of_day_seconds % 60

print(f"Days since January 1, 1970: {days_since_epoch}")
print(f"Current time of day: {hours:02}:{minutes:02}:{seconds:02}")
print(hours, minutes, seconds)


