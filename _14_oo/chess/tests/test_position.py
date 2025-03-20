from chess import Position


def test_a1():
    a1 = Position("A", 1)

    assert a1.horizontal == 1
    assert a1.vertical == 1