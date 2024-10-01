import datetime

# easy_pace = ((8 * 60) + 15) * 2
# four_miles = ((7 * 60) + 12) * 3
#
# total_time_sec = easy_pace + four_miles
#
# time_mid_hour_sec = 6 * 3600
# time_mid_min_sec = 52 * 60
#
# real_time_sec = total_time_sec + time_mid_hour_sec + time_mid_min_sec
#
# hour = real_time_sec // 3600
# minutes = (real_time_sec % 3600) // 60
# seconds = real_time_sec % 60
#
# print (f"Ik arriveer thuis om {hour}:{minutes} en {seconds} seconden")

easy_pace_min = 8
easy_pace_sec = 15
tempo_run_min = 7
tempo_run_sec = 12
amount_tempo_miles = 3
amount_easy_miles = 2
sec_in_minutes = 60
sec_in_hours = 3600
start_hour = 6
start_minute = 52

#total running time
tot_easy_pace_sec = ((easy_pace_min * sec_in_minutes) + easy_pace_sec) * amount_easy_miles
tot_tempo_sec = ((tempo_run_min * sec_in_minutes) + tempo_run_sec) * amount_tempo_miles

#total run time in seconds
total_time_sec = tot_easy_pace_sec + tot_tempo_sec

#calculate sec till midnight
time_mid_hour_sec = start_hour * sec_in_hours
time_mid_min_sec = start_minute * sec_in_minutes

#everthing in seconds till midnight
real_time_sec = total_time_sec + time_mid_hour_sec + time_mid_min_sec

# calculate the time in from total seconds till midnight
hour = real_time_sec // sec_in_hours
minutes = (real_time_sec % sec_in_hours) // sec_in_minutes
seconds = real_time_sec % sec_in_minutes

print (f"Ik arriveer thuis om {hour}:{minutes} en {seconds} seconden")

start = datetime.timedelta(hours=6, minutes=52)
slow = datetime.timedelta(minutes=8, seconds=15)
fast = datetime.timedelta(minutes=7, seconds=12)

print(start + slow * 2 + fast * 3)

two_hours_later = datetime.timedelta(hours=2)
print(datetime.datetime.now() + two_hours_later)
