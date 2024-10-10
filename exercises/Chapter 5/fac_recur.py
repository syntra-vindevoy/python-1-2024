from datetime import datetime

def fac(n: int) -> int:

    if n == 0:
        return 1
    if n == 1:
        return 1

    if n > 1:
        return n * fac(n-1)

def main():
    fac = fac(2)

    assert fac(0) == 1
    assert fac(1) == 1
    assert fac(2) == 2
    assert fac(3) == 6
    assert fac(4) == 24
    assert fac(5) == 120

if __name__ == '__main__':
    start = datetime.now()

