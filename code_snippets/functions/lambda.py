
'''
UNFISIHED CODE
'''

def test_lambda(value:int):
    return lambda x: x + value


def main():
    add_10 = test_lambda(10)
    print(add_10(5))  # 15


if __name__ == "__main__":
    main()
