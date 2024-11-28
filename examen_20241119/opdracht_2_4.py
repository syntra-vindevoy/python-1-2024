def russian_passant(x:int, y:int) -> int:
        result = 0
        while x > 0:
            if x % 2 != 0:
                result += y

            y *= 2
            x //= 2

        return result

if __name__ == "__main__":
    assert russian_passant(x=1, y=1) == 1
    assert russian_passant(x=1, y=2) == 2
    assert russian_passant(x=2, y=1) == 2
    assert russian_passant(x=2, y=2) == 4
    assert russian_passant(x=3, y=3) == 9
    assert russian_passant(x=146, y=37) == 5402
    assert russian_passant(x=1000000, y=1000000) == 1000000000000
    assert russian_passant(x=123456789, y=987654321) == 121932631112635269

