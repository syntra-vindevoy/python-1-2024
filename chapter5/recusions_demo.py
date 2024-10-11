from functools import reduce
import numpy

def new_fac(n: int) -> int:
    """
       Calculate the factorial of a positive n.
       Args:
           n:
               int: The number to calculate the factorial for.

       Returns:
          int : The factorial of a positive n.
       """
    return 1 if n < 2 else reduce(lambda x, y: x * y, range(2, n+1))

def fac3(n):
    """
    Calculate the factorial of a positive n.
    Args:
        n:
            int: The number to calculate the factorial for.

    Returns:
       int : The factorial of a positive n.
    """
    if n < 2:
        return 1
    return int(numpy.prod(range(2, n+1)))

assert fac3(6) == 720

assert new_fac(6) == 720

def factorial_me(n: int):
    """
       Calculate the factorial of a positive n.
       Args:
           n:
               int: The number to calculate the factorial for.

       Returns:
          int : The factorial of a positive n.
       """
    assert n > 0
    if n == 1:
        return 1
    return n * factorial_me(n - 1)

def old_fac(n:int)->int:
    """
       Bereken de faculteit van een gegeven geheel getal.

       De functie gebruikt een iteratief proces om de faculteit van 'n' te berekenen.
       Als n kleiner is dan 2, retourneert de functie 1.

       Parameters:
       n (int): Het geheel getal waarvan de faculteit moet worden berekend.

       Returns:
       int: De faculteit van 'n'. Als n kleiner is dan 2, retourneert de functie 1.

      Raises:
        ValueError: Als 'n' een negatief getal is.
       """
    if n < 0:
        raise ValueError("n moet een positief geheel getal zijn.")
    total=n
    for i in range(2,n):
        total *= i
    return total

assert old_fac(6) == 720
assert old_fac(5) == 120

def even_nbr(n):
    print(n)
    if n % 2 != 0:
        print("not even nbr")
        return
    elif n == 2:
        return n
    even_nbr(n - 1)

def sum_n(n):
    if n==1:
        return 1
    return sum(n-1)+n

if __name__ == '__main__':
    print(old_fac(6))

"""
print(sum(120))
even_nbr(6)

"""
assert factorial_me(5) == 120
assert factorial_me(1) == 1