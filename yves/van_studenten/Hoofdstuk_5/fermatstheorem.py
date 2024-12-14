def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print("HOLY SHIT FERMAT WAS WRONG!")
    else:
        print("NO THAT DOES NOT WORK!")

def check_numbers():
    a = int(input("What number is a?"))
    b = int(input("What is number b?"))
    c = int(input("What is number c?"))
    n = int(input("What is n?"))
    return check_fermat(a, b, c, n)

check_numbers()