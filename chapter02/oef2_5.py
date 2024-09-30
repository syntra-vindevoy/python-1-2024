import datetime

start = ((6 * 3600) + 52 * 60) #start tijd is 6u52
slow_lap = (8 * 60) + 15
fast_lap = (7 * 60) + 12
finish = start + (slow_lap * 2) + (fast_lap * 3)
finish_hour = finish // 3600
hour_remains = finish % 3600
finish_minute = hour_remains // 60
finish_sec = hour_remains % 60

print(f"Ik ben aangekomen om {finish_hour}u {finish_minute}min {finish_sec}sec")

finish_with_import = datetime.datetime.fromtimestamp(finish, datetime.UTC).strftime('%H:%M:%S')
print(f"met een import komen we aan het zelfde resultaat: {finish_with_import}")