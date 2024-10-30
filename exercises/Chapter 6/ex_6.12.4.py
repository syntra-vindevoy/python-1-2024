
def ackerman(m: int, n: int):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackerman(m - 1, 1)
    return ackerman(m - 1, ackerman(m, n - 1))

def main():
    print(ackerman(5, 5))
    #give recursion error: stack overflow

if __name__ == "__main__":
    main()