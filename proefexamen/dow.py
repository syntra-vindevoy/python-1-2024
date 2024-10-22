def day_of_the_week(year: int, month: int, day: int) -> int:
  """
  Calculates the day of the week for a given date.
  Returns an integer between 1 (Monday) and 7 (Sunday).
  """
  offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
  # If month is less than 3, subtract 1 from year
  year -= month < 3  # Treat Jan and Feb as months 13 and 14 of prev year
  dow = (year + year // 4 - year // 100 + year // 400 +
         offset[month - 1] + day) % 7
  if dow == 0:
      dow = 7
  return dow  # 1 = Monday, ..., 7 = Sunday

def main():
  assert day_of_the_week(2022, 12, 1) == 4  # Thu
  assert day_of_the_week(2022, 12, 2) == 5  # Fri
  assert day_of_the_week(2022, 12, 3) == 6  # Sat
  assert day_of_the_week(2022, 12, 4) == 7  # Sun
  assert day_of_the_week(2022, 12, 5) == 1  # Mon
  assert day_of_the_week(2022, 12, 6) == 2  # Tue
  assert day_of_the_week(2022, 12, 7) == 3  # Wed

if __name__ == "__main__":
  main()