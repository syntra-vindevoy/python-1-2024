minutes = 42
seconds = 42
hour_in_minutes = 60


#1 How many seconds are there in 42 minutes 42 seconds?
total_sec = minutes + (seconds * hour_in_minutes)

print(total_sec)

#2 How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
distance = 10
mile_in_km = 1.61

total_miles = distance / mile_in_km
print(total_miles)

#3 If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?

avg_pace_miles = total_sec / total_miles
print(avg_pace_miles)

#4 What is your average pace in minutes and seconds per mile

avg_minutes = avg_pace_miles // hour_in_minutes
avg_seconds = avg_pace_miles % hour_in_minutes

print(f"Average pace: {avg_minutes} minutes and {avg_seconds} seconds per mile")


#5 What is your average speed in miles per hour?

speed_mph = (total_miles / total_sec) * 3600

print("Average speed in miles per hour:", speed_mph)