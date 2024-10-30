

def gcd(a, b):
    if b == 0:
        return a
    else:
        print(a, b, a % b)
        return gcd(b, a % b)


def main():
    print(gcd(12, 15))
    print(gcd(12, 10))

if __name__ == "__main__":
    main()