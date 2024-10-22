from cal_month_week import *

def print_year(year:int):
    for i in range(1, 13):
        print_month(year, i)
        print("")

if __name__ == "__main__":
    print_year(2022)