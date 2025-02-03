#!/home/vindevoy/miniconda3/envs/syntra/bin/python

minutes = int(input("Give minutes: "))
seconds = int(input("Give seconds: "))

total_seconds = minutes * 60 + seconds

print(f"The total number of seconds for {minutes} minutes and {seconds} seconds: {total_seconds}")

total_seconds = round(total_seconds, 2)

print(f"The total seconds is {round(total_seconds, 2)}")
