# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile)
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again
# what time do I get home for breakfast?

initial_hour_in_seconds = (6 * 60 * 60) + (52 * 60)
time_easy_pace = 8 * 60 + 15
time_tempo = 3 * ((7 * 60) + 12)
arrival_time_in_seconds = initial_hour_in_seconds + time_easy_pace + time_tempo + time_easy_pace
arrival_time_in_hours = arrival_time_in_seconds // 3600
remaining_seconds = arrival_time_in_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"You'll arrive at home at {arrival_time_in_hours:02}:{minutes:02}:{seconds:02}.")
