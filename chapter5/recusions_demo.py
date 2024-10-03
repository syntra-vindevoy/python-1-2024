def factorial_me(n: int):
    """
    Calculate the factorial of n.
    """
    assert n > 0
    if n == 1:
        return 1
    return n * factorial_me(n - 1)


def even_nbr(n):
    print(n)
    if n % 2 != 0:
        print("not even nbr")
        return
    elif n == 2:
        return n
    even_nbr(n - 1)

def sum(n):
    if n==1:
        return 1
    return sum(n-1)+n



print(sum(120))
even_nbr(6)
assert factorial_me(5) == 120
assert factorial_me(1) == 1