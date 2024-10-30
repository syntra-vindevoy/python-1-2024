

def hypot(x: int, y: int) -> int | float:
    """
    Function to calculate the 3 side of a squared triangle

    Parameters
    ----------
    x: int
        first side of the triangle
    y: int
        second side of the triangle

    returns
    -------
    int:
        returns the value of the 3 unknown side of the triangle

    Author
    ------
        Chiv

    Date
    ----
        30-10-2024
    """

    return (x ** 2 + y ** 2) ** 0.5

def main():
    print(hypot(3, 4))

    assert hypot(3, 4) == 5
    assert hypot(6, 8) == 10
    assert hypot(9, 12) == 15
    assert hypot(5, 12) == 13
    assert hypot(9, 40) == 41


if __name__ == "__main__":
    main()