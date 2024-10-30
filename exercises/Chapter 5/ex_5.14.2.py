from time import time

print(time())
epoch_time = time()

def time_calc(epoch_time: float) -> tuple[float, float, float, float]:

    """
    Function to calculate how many days, hours, minutes, and seconds have passed since the start of epoch time.

    Parameters
    ----------
    epoch_time : float
        The amount of seconds since the start of epoch time.

    Returns
    -------
    tuple[int, int, int, float]
        A tuple containing the number of days, hours, minutes, and seconds.

    Author
    ------
    Chiv

    Date
    ----
    30-10-2024
    """

    days = epoch_time // (24 * 3600)
    hours = epoch_time // 3600 % 24
    minutes = epoch_time // 60 % 60
    seconds = epoch_time % 60

    return days, hours, minutes, seconds

def time_calc2(epoch_time: float) -> str:

    """
    Function to calculate how many days, hours, minutes, and seconds have passed since the start of epoch time.

    Parameters
    ----------
    epoch_time : float
        The amount of seconds since the start of epoch time.

    Returns
    -------
    str
        compiling the answer needed and returning it as a string.

    Author
    ------
    Chiv

    Date
    ----
    30-10-2024
    """

    days = int(epoch_time // (24 * 3600))
    hours = int(epoch_time // 3600 % 24)
    minutes = int(epoch_time // 60 % 60)
    seconds = int(epoch_time % 60)

    answer = f"Tijd: {days} dagen, {hours} uur, {minutes} minuten en {seconds} seconden"

    return answer

def main():
    days, hours, minutes, seconds = time_calc(epoch_time)
    print(f"Tijd: {int(days)} dagen, {int(hours)} uur, "
          f"{int(minutes)} minuten en {round(seconds)} seconden")

    print(time_calc2(epoch_time))

if __name__ == "__main__":
    main()