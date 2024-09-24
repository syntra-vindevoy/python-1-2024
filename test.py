def get_seconds(minutes:int,seconds:int)->int:
    seconds_from_minutes = minutes*60
    return seconds_from_minutes + seconds


def get_miles_from_kilometers(kilometers:float)->float:
    return kilometers*1.609


def main():
    seconds = get_seconds(42,42)
    print(seconds)


if __name__ == '__main__':
    main()

def is_leap_year(year:int)->bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def is_leap_year_shorter(year:int)->bool:
    if year % 4 > 0: return False
    if year % 100 > 0: return True
    if year % 400 > 0: return False
    return True

def is_leap_year_shortest(year:int):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

