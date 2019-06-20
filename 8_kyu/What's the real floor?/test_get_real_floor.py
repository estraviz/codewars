from get_real_floor import get_real_floor


def test_should_return_a_correct_value_for_floors_lower_than_13():
    assert get_real_floor(1) == 0
    assert get_real_floor(0) == 0
    assert get_real_floor(5) == 4
    assert get_real_floor(10) == 9


def test_should_return_a_correct_value_for_floors_greater_than_13():
    assert get_real_floor(15) == 13
    assert get_real_floor(37) == 35
    assert get_real_floor(200) == 198


def test_should_return_a_correct_value_for_basement_floors():
    assert get_real_floor(-2) == -2
    assert get_real_floor(-5) == -5
