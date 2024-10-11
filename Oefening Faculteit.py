def faculteit(n: int):

    """
    Compute the factorial of a non-negative integer `n`.

    The factorial of `n` (denoted as `n!`) is the product of all positive integers
    from 1 to `n`. By definition, the factorial of 0 and 1 is 1.

    Parameters
    ----------
    n : int
        A non-negative integer for which the factorial is to be computed.

    Returns
    -------
    int
        The factorial of the input number `n`. If `n` is 0 or 1, returns 1.

    Notes
    -----
        This implementation avoids an extra loop by initializing the result `r` to `n`
        and iterating from 2 to `n-1` (since multiplying by 1 is redundant).

        Version: 1.1.0
        Author: Enterauh
        Date: 2024-10-10
        Bugfix: dkfjsdlkjsd

        Version: 1.0.0
        Author: Enterauh
        Date: 2024-10-10

    Examples
    --------
    >>> faculteit(6)
    720

    >>> faculteit(0)
    1

    >>> faculteit(1)
    1

    """

    # In math the definition for 0 and 1 states that the result is 1
    if n < 2:
        return 1

    # Starting with r = n to avoid an extra loop in the range which would otherwise be (2, n+1)
    r = n

    # Starting from 2 because multiplication by 1 makes no sense
    for i in range(2, n):
        r *= i
    return r

print(faculteit(6))
