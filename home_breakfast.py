import math

start_leave_sec = 6 * 3600 + 52 * 60
first_run_time_sec = 8 * 60 + 15
total_sec_first_run = first_run_time_sec
second_run_time_sec = 7 * 60 + 12
total_sec_second_run = second_run_time_sec * 3
total_run_sec = total_sec_first_run + total_sec_second_run + first_run_time_sec
total_time_sec = start_leave_sec + total_run_sec
morning_h = total_time_sec // 3600
rest_seconds_h = total_time_sec % 3600
morning_min = rest_seconds_h // 60
morning_sec = rest_seconds_h % 60


print(f"You arrive at {int(morning_h)}:{int(morning_min):02d}:{int(morning_sec):02d}")

