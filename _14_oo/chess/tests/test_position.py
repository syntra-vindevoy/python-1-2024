from chess import Position


def test_a1():
    a1 = Position("A", 1)

    assert a1.horizontal == 1
    assert a1.vertical == 1



def test_h8():
    h8 = Position("H", 8)

    assert h8.horizontal == 8
    assert h8.vertical == 8


def test_i1():
    try:
        i1 = Position("I", 1)
    except AssertionError:
        return

    assert False, "Should have raised an AssertionError"