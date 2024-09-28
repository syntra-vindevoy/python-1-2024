time_start = 6 * 3600 + 52 * 60
easy_pace = 8 * 60 + 15
tempo_pace = 7 * 60 + 12
easy_miles = 2
tempo_miles = 3

total_time = time_start + easy_miles * easy_pace + tempo_pace * tempo_miles
hours = total_time // 3600
minutes = (total_time - hours * 3600) // 60
seconds = total_time - hours * 3600 - minutes * 60
print(f"ik kom thuis om {hours}:{minutes} and {seconds} seconds")
