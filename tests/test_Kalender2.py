import pytest
from src.Oefeningen.Kalender import calculate_day_of_week


def test_calculate_day_of_week_jan_31_2022 ():
    assert calculate_day_of_week (31, 1, 2022) == 1  # Monday


def test_calculate_day_of_week_feb_28_2020 ():
    assert calculate_day_of_week (28, 2, 2020) == 5  # Friday


def test_calculate_day_of_week_apr_4_2024 ():
    assert calculate_day_of_week (4, 4, 2024) == 4  # Thursday


def test_calculate_day_of_week_dec_25_2000 ():
    assert calculate_day_of_week (25, 12, 2000) == 1  # Monday


def test_calculate_day_of_week_for_leap_year_feb_29 ():
    assert calculate_day_of_week (29, 2, 2020) == 6  # Saturday


def test_calculate_day_of_week_for_non_leap_year_feb_29 ():
    with pytest.raises (IndexError):
        calculate_day_of_week (29, 2, 2019)  # This will raise an index error because 2019 is not a leap year.
