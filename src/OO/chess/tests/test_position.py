from position import Position


def test_a1():
    a1 = Position(horizontal="A", vertical=1)

    assert a1.horizontal == 1
    assert a1.vertical == 1


def test_h8():
    h8 = Position(horizontal="H", vertical=8)

    assert h8.horizontal == 8
    assert h8.vertical == 8


def test_lowercase_a1():
    a1 = Position(horizontal="a", vertical=1)

    assert a1.horizontal == 1
    assert a1.vertical == 1


def test_i1():
    try:
        _ = Position(horizontal="I", vertical=1)
    except AssertionError:
        return

    assert False, "Should have thrown an AssertionError"


def test_a10():
    try:
        _ = Position(horizontal="A", vertical=10)
    except AssertionError:
        return

    assert False, "Should have thrown an AssertionError"
