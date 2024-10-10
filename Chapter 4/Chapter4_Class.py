# Les 10/10 oefeningen
#def fac(n) zonder recursiviteit

def fac(n: int) -> int: #This HINTS that the value for n should be an integer and also the return value
    """
    This function calculates the faculty of a positive integer n. In math this is n!


    :param n:
        int: The number on which we calculate the faculty

    :return:
        int: The calculated faculty

    Notes:
        Author: Synix
        Date: 2024-10-10
        Version: 1.0.0

    """
    if n < 2:
        return 1

    r = n

    for i in range(2 , n):
        r *= i

    return(r)
if __name__ == '__main__':
    print(fac(9))