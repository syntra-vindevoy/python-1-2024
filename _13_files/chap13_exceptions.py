try:
    with open("words.txt", "r") as f:
        lines = f.readlines()
except:
    print("An Error has occured")


def blabla(l):
    pass

f = None

try:
    f = open("words2.txt", "r")
    lines = f.readlines()
    blabla(lines)

except SyntaxError:
    print("Syntax Error")

except FileNotFoundError:
    print("File not found")

except Exception as err:
    print(f"An Error has occurred:\n\n{err}")

finally:
    if f:
        if not f.closed:
            f.close()


def fac(n):
    if n < 0:
        raise ValueError("Negative factorial not allowed")
    if n < 2:
        return 1

    return n * fac(n-1)

i = input("Give a positive integer: ")

try:
    print(fac(int(i)))
except ValueError as err:
    print("RTFM")