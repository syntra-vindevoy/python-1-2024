import numpy
from datetime import datetime

#chatgpt: explain recursion
#chatgpt: explain testing codetime with assert

# lijn 9 tot 15 faculteit berekenen zonder recursie + optimaliseren

n = int(input("Give me a number "))
# start met r=n om een extra loop te voorkomen want anders (2, n+1) zou zijn
r = n

for i in range(2, n + 1): #beginnen bij 2 want *1 van een getal is nutteloos
    r = r * i    # dit is de verkorte versie: r *= 1
print(r)


# ---------------------------

def fac(n):
    if n < 2:
        return 1
    r = n
    for i in range (2, n):
        r *= i
    return n


def fac2(n: int) -> int:
    """

    This function calculates the factorial of a positive integer n. In math this is n!

    :param n:
        int: The number on which we calculate the faculty
    :return:
        int: The calculated faculty

    Notes:
        Versie: 1.0.0
        Autor: BESA03
        Date: 2024-10-10
        New feature: blabla
        Bugfix: blabla

    """
    if n < 2:
        return 1


def fac3(n: int) -> int:
    if n < 2:
        return 1
    return int(numpy.prod(range(2, n +1)))

# tijd testen
def main():
    fac = fac3

    assert fac(0) == 1
    assert fac(1) == 1
    assert fac(2) == 2
    assert fac(3) == 6
    assert fac(4) == 24
    assert fac(5) == 120


if __name__ == "__main__":
    start = datetime.now()

    for _ in range(1000):
        main()

    end = datetime.now()
    print(end - start)