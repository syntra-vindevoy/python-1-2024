from src.chapter15.chap15_ex_book3 import Date


def test_date_initialization ():
    date = Date (2024, 11, 18)
    assert date.year == 2024
    assert date.month == 11
    assert date.day == 18


def test_date_str_representation ():
    date = Date (2024, 11, 18)
    assert str (date) == "2024-11-18"


def test_date_repr_representation ():
    date = Date (2024, 11, 18)
    assert repr (date) == "Date(2024, 11, 18)"


def test_date_equality ():
    d1 = Date (2024, 11, 18)
    d2 = Date (2024, 11, 18)
    assert (d1 == d2) == True


def test_date_hash ():
    date = Date (2024, 11, 18)
    assert hash (date) == hash ((2024, 11, 18))


def test_date_to_tuple ():
    date = Date (2024, 11, 18)
    assert date.date_to_tuple (date) == (2024, 11, 18)


def test_is_after ():
    d1 = Date (2024, 11, 18)
    d2 = Date (2023, 11, 18)
    assert d1.is_after (d1, d2) == True
    assert d2.is_after (d1, d2) == False
