from examens.examen1.date_string import name_of_month, name_of_day
from examens.examen1.dom import days_of_month
from examens.examen1.dow import day_of_the_week
from examens.examen1.week_number import week_number


def print_month_calendar_with_week_numbers (year: int, month: int):
    """
    Prints the calendar for a specific month of a given year including week numbers.

    :param year: An integer representing the year.
    :param month: An integer representing the month (1-12).
    """

    def make_banner_days (first_day: int):
        """
        Make a string with day starting from first day
        Args:
            first_day:

        Returns:
            output:
        """
        output_banner = ""
        for i in range (1, 8):
            output_banner += f"{name_of_day (i)} "
        return output_banner

    # Draw calendar month

    days_to_print = days_of_month (year, month)
    month_name = name_of_month (month)

    first_day_to_print = day_of_the_week (1, month, year)
    line_counter = first_day_to_print
    print (f"\t{month_name} Year {year}\n")
    output = "     " + make_banner_days (first_day_to_print) + "\n"
    output += f"[{week_number (year, month, 1):02d}] "
    output += "   " * (first_day_to_print - 1)
    for day_count in range (1, days_to_print + 1):
        output += f"{day_count:02d} "
        if line_counter % 7 == 0:
            output += "\n"
            if (day_count < days_to_print):
                output += f"[{week_number (year, month, day_count + 1):02d}] "
        line_counter += 1
    print (output + "\n")


def main ():
    for month in range (1, 13):
        print_month_calendar_with_week_numbers (2022, month)


if __name__ == "__main__":
    main ()
