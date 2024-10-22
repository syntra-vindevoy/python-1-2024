from leapyear import is_leap_year

def days_of_month(year: int, month: int) -> int:

  if month < 1 or month > 12:
      return 0
  days_in_month = [0, 31, 28, 31, 30, 31, 30,
                   31, 31, 30, 31, 30, 31]
  if month == 2 and is_leap_year(year):
      return 29  # February in a leap year
  else:
      return days_in_month[month]

def main():
  # Leap year
  assert days_of_month(2020, 1) == 31  # Jan
  assert days_of_month(2020, 2) == 29  # Feb
  assert days_of_month(2020, 3) == 31  # Mar
  assert days_of_month(2020, 4) == 30  # Apr
  assert days_of_month(2020, 5) == 31  # May
  assert days_of_month(2020, 6) == 30  # Jun
  assert days_of_month(2020, 7) == 31  # Jul
  assert days_of_month(2020, 8) == 31  # Aug
  assert days_of_month(2020, 9) == 30  # Sep
  assert days_of_month(2020,10) == 31  # Oct
  assert days_of_month(2020,11) == 30  # Nov
  assert days_of_month(2020,12) == 31  # Dec

  # No leap year
  assert days_of_month(2022, 2) == 28

if __name__ == "__main__":
  main()