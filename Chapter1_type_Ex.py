#How many seconds are there in 42 minutes 42 seconds?
total_seconds = (42 * 60) + 42
print(total_seconds)

# How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
miles = 10 / 1.61
print(miles)

# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?
pace_seconds = total_seconds / miles
print(pace_seconds)

# What is your average pace in minutes and seconds per mile?
minutes = pace_seconds / 60
full_minutes = int(minutes)
seconds = pace_seconds % 60
print(f"{full_minutes} minutes and {seconds:.2f} seconds.")

# What is your average speed in miles per hour?
speed_mph = miles / (total_seconds / 3600)
print(f"Average speed {speed_mph:.2f} miles per hour")