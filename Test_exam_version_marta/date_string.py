def name_of_day(day: int) -> str:
    if 1 <= day <= 7:
        return ["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"][day - 1]


def name_of_month(month: int) -> str:
    if 1 <= month <= 12:
        return ["Januari", "Februari", "Maart", "April", "Mei", "Juni", "Juli", "Augustus", "September", "Oktober",
            "November", "December"][month - 1]


 def test_name_of_day():
    assert name_of_day(1) == "Ma"
    assert name_of_day(2) == "Di"
    assert name_of_day(3) == "Wo"
    assert name_of_day(4) == "Do"
    assert name_of_day(5) == "Vr"
    assert name_of_day(6) == "Za"
    assert name_of_day(7) == "Zo"


def test_name_of_month():
    assert name_of_month(1) == "Januari"
    assert name_of_month(2) == "Februari"
    assert name_of_month(3) == "Maart"
    assert name_of_month(4) == "April"
    assert name_of_month(5) == "Mei"
    assert name_of_month(6) == "Juni"
    assert name_of_month(7) == "Juli"
    assert name_of_month(8) == "Augustus"
    assert name_of_month(9) == "September"
    assert name_of_month(10) == "Oktober"
    assert name_of_month(11) == "November"
    assert name_of_month(12) == "December"


if __name__ == "__main__":
    test_name_of_day()
    test_name_of_month()