# Les 10/10 oefeningen
#def fac(n) zonder recursiviteit

def fac(n: int):
    if n < 2:
        return 1

    r = n

    for i in range(2 , n):
        r *= i

    print(r)

fac(9)