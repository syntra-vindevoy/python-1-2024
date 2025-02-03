def toto(l):
    pass

f = None

try:
    f = open("words.txt", "r")
    lines = f.readlines()

    toto(lines)

except SyntaxError:
    print("Your code sucks")

except FileNotFoundError:
    print("Could not find file")

except Exception as err:
    print("Did not really expect this one", err)

finally:
    if f:
        if not f.closed:
            f.close()





def fac(n):
    if n < 0:
        raise ValueError(f"n must be non-negative, you entered {n}")

    if n < 2:
        return 1

    return n * fac(n-1)


i = input("Give a positive integer:")

try:
    print(fac(int(i)))
except ValueError as err:
    print("Read the f manual", err)