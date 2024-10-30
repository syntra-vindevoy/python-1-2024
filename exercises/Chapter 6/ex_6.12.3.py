

def is_between(x: int, y: int, z: int) -> bool:
    """
    check 3 different values between each other
    if the condition x < y < z or z < y < x is true

    Parameter
    ---------
    x: int
        first input value
    y: int
        second input value
    z: int
        thirth input value

    Returns
    -------
    Boolean:
        if conditions are met return True else False

    Author
    ------
        Chiv

    Date
    ----
        30-10-2024
    """

    return x < y < z or z < y < x

def main():
    print(is_between(1, 2, 3))

    assert is_between(1, 2, 3) is True
    assert is_between(3, 2, 1) is True
    assert is_between(1, 3, 2) is False

if __name__ == "__main__":
    main()