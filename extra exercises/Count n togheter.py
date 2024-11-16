

def count_n(n):
    """
    calculates a running sum of any given number

    parameters
    ----------
    n: int
        can be any number

    returns
    -------
    result: int
        return the result of the running sum

    author
    ------
        Chiel

    date
    ----
        16-11-2024
    """
    first = n
    result = 0

    while n > 0:
        result = first + n - 1
        first = result
        n -= 1

    return result

def main():
    print(count_n(5))

    assert count_n(5) == 15
    assert count_n(10) == 55
    assert count_n(100) == 5050

if __name__ == "__main__":
    main()