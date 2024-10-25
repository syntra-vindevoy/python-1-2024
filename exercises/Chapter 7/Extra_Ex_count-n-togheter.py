def count_n(n):

    first = n
    result = 0

    while n > 0:
        result = first + n - 1
        first = result
        n -= 1

    return result

def main():
    print(count_n(5))

    assert count_n(5) == 15
    assert count_n(10) == 55
    assert count_n(100) == 5050

if __name__ == "__main__":
    main()