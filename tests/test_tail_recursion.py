import pytest

from src.chapter6.tail_recursion import fact


def test_factorial_zero ():
    assert fact (0) == 1


def test_factorial_one ():
    assert fact (1) == 1


def test_factorial_positive ():
    assert fact (4) == 24
    assert fact (5) == 120
    assert fact (10) == 3628800


def test_factorial_negative ():
    with pytest.raises (ValueError):
        fact (-1)


def test_factorial_large ():
    assert fact (20) == 2432902008176640000


def test_factorial_with_initial_t ():
    assert fact (4, 4) == 96
    assert fact (5, 2) == 240
