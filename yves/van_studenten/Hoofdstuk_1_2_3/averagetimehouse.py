start_time_sec = 6*60*60 + 52*60
pace_mile_sec = 8*60 + 15
pace_three_miles_sec = 7*60+12

end_time_sec = start_time_sec + 2*pace_mile_sec + 3*pace_three_miles_sec
time = end_time_sec/60/60

hours = int(time)
minutes = (time*60) % 60
seconds = (time*3600) % 60

print("%02d:%02d.%02d" % (hours, minutes, seconds))