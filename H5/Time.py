import time

# Get the current time in seconds since January 1, 1970 (Unix epoch)
current_time_seconds = int(time.time())

# Compute the number of days since January 1, 1970
seconds_in_a_day = 24 * 60 * 60
days_since_epoch = current_time_seconds // seconds_in_a_day

# Compute the remaining seconds after accounting for full days
remaining_seconds = current_time_seconds % seconds_in_a_day

# Compute the current time of day in hours, minutes, and seconds
hours = remaining_seconds // 3600
remaining_seconds %= 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# Output the results
print(f"Days since January 1, 1970: {days_since_epoch}")
print(f"Current time: {hours:02}:{minutes:02}:{seconds:02}")
