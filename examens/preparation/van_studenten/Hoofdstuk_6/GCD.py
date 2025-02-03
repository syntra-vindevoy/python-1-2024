def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


def check_numbers():
    a = int(input("Number 1? "))
    b = int(input("Number 2? "))
    return gcd_recursive(a, b)


print(check_numbers())
