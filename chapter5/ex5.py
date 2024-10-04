import time


#Use integer division and the modulus operator to compute the number
# of days since January 1, 1970 and the current time of day in hours, minutes, and seconds.

def calculate_number_of_days ():
    current_time_seconds = int (time.time ())

    # Number of seconds in a day
    seconds_per_day = 86400

    # Calculate the number of days since Jan 1, 1970
    days_since_epoch = current_time_seconds // seconds_per_day

    # Calculate the remaining seconds in the current day
    remaining_seconds = current_time_seconds % seconds_per_day

    # Calculate hours, minutes, and seconds from the remaining seconds
    hours = remaining_seconds // 3600
    remaining_seconds = remaining_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    # Output the results
    return days_since_epoch, hours, minutes, seconds


def is_triangle (param, param1, param2):
    if (param + param1 < param2) or (param + param2 < param1) or (param1 + param2 < param):
        return False
    return True


def check_fermat (a, b, c, n):
    return c ** n == a ** n + b ** n


def main ():
    data = calculate_number_of_days ()

    print (f"days, hours, minutes, seconds: {data}")


    print (is_triangle (4, 5, 6))
    print (is_triangle (1, 2, 3))
    print (is_triangle (6, 2, 3))
    print (is_triangle (1, 1, 12))

    a = int(input ("Enter a number a: "))
    b =  int(input ("Enter a number b: "))
    c =  int(input ("Enter a number c: "))
    n =  int(input ("Enter a number n: "))

    """
    Write a function named check_fermat that takes four parameters—a, b, c and n—and checks to see if Fermat’s theorem holds. If n is greater than 2 and
    an + bn = cn 
    the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should print, “No, that doesn’t work.”

    Write a function that prompts the user to input values for a, b, c and n, converts them to integers, and uses check_fermat to check whether they violate Fermat’s theorem.
    """
    if check_fermat (a, b, c, n) and n > 2:
        print ("Holy smokes, Fermat was wrong!")
    else:
        print ("No, that doesn’t work.")


if __name__ == '__main__':
    main ()
