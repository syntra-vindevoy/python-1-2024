def is_leap_year(year: int) -> bool:
  # Returns True if 'year' is a leap year, else False
  if year % 4 != 0:
      return False  # Not divisible by 4
  elif year % 100 != 0:
      return True   # Divisible by 4 but not by 100
  elif year % 400 != 0:
      return False  # Divisible by 100 but not by 400
  else:
      return True   # Divisible by 400

def main():

  assert is_leap_year(2021) is False
  assert is_leap_year(2020) is True
  assert is_leap_year(2100) is False
  assert is_leap_year(2000) is True

if __name__ == "__main__":
  main()