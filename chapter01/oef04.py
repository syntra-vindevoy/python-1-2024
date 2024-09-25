aantal_sec = (42 * 60) + 42
mile_in_10 = 10 / 1.61

avg_pace_sm = aantal_sec / mile_in_10

count_min = int(avg_pace_sm / 60)

count_sec = int(avg_pace_sm % 60)


print(f"average pace in minutes and secons per mile is {count_min} min, {count_sec} sec.")