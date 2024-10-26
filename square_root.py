def square_root(number, estimate):
    while True:
        result = (estimate + number / estimate) / 2
        if result == estimate:
            return estimate
            break
        estimate = result
        print(f"estimate: {estimate}")


def tests():
    assert square_root(9, 3) == 3
    assert square_root(25, 4) == 5


def main():
    tests()
    print(square_root(9, 3))
    print(square_root(25, 4))
    print(square_root(100, 25))


if __name__ == "__main__":
    main()
