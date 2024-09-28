print("How many seconds are there in 42 minutes 42 seconds?")
print((60 * 42 + 42), "seconds")

print("How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.")
print((10 / 1.61), "miles")

print("If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?")
print(round(((60 * 42 + 42) / (10 / 1.61))), "s/mile")

print("What is your average pace in minutes and seconds per mile?")
minutes = int(((60 * 42 + 42) / (10/1.61)) // 60)
seconds = round((60 * 42 + 42) / (10 / 1.61) % 60)
print(f"{minutes} minutes and {seconds} seconds per mile")

print("What is your average speed in miles per hour?")
print(round((3600 / ((minutes * 60 ) + seconds)), 2))