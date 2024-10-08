from calendar import month, Month

from chapter5.ex5 import calculate_number_of_days

Days = ["za", "Zo", "Ma", "Di", "Wo", "Do", "Vr"]
#Days = ["zaterdag", "Zondag", "Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag"]
months = [
    "Januari",
    "Februari",
    "Maart",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Augustus",
    "September",
    "Oktober",
    "November",
    "December"
]
def draw(days,first_day,month,year):
    print(f"Month {months[month-1]} Year {year}")
    output = make_banner_days(first_day) + "\n"
    for day_count in range(1,days):
        output += f"{day_count:02d} "
        if day_count % 6 == 0:
            output +="\n"

    print(output)


def make_banner_days(first_day:int):
    output =""
    for i in range(first_day,len(Days)):
        output += f"{Days[i]} "
    for i in range(1,first_day):
        output += f"{Days[i]} "
    return output



def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def calculate_day_of_week(day, month, year):
    # Zeller's Congruence works with months as follows:
    # January and February are treated as months 13 and 14 of the previous year
    if month < 3:
        month += 12
        year -= 1

    K = year % 100  # Year of the century
    J = year // 100  # Zero-based century

    # Zeller's Congruence formula
    f = day + ((13 * (month + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)
    day_of_week = f % 7

    # Map the result to the day names


    return day_of_week


def days_in_month(month, year):
    # Number of days in each month for a non-leap year
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check for leap year and adjust February
    if is_leap_year(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]

def main():
    month=2
    year=2018
    draw(days=days_in_month(month,year),month=month,year=year,first_day=calculate_day_of_week(year,month,1))


if __name__ == '__main__':
    main()