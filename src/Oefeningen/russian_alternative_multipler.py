def russian_alternative_multipler (number1, number2):
    """
    Args:
        number1: The first integer to be multiplied.
        number2: The second integer to be multiplied.

    Returns:
        The product of the two integers using the Russian Peasant Multiplication algorithm.
    """
    total = 0
    div_num = number1
    double_num = number2
    while div_num > 0:
        if div_num % 2 != 0:
            total += double_num
        double_num = double_num * 2
        div_num = div_num // 2
    return total


assert russian_alternative_multipler (24, 16) == 384
