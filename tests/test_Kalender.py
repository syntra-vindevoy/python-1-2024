# File: test_Kalender.py
import pytest
from Oefeningen.Kalender import is_leap_year


def test_is_leap_year ():
    # Test leap year that is divisible by 4, not divisible by 100
    assert is_leap_year (2024) == True
    # Test common year, not divisible by 4
    assert is_leap_year (2023) == False
    # Test leap year that is divisible by 400
    assert is_leap_year (2000) == True
    # Test common year that is divisible by 100 but not by 400
    assert is_leap_year (1900) == False
