from operator import truediv


def is_leap_year(year):
    #this functions verifies if a year is a leap year or not

    ###
    # sidviny - 2024-09-25
    # the next line resolves the bug "hdhkjkd" found. This is caused by...
    # wrong command: djdhhjdhjdh
    sql = "SELECT * FROM student"
    ###

    if year % 4 == 0:
        return True
