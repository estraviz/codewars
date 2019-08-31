from power_of_two import power_of_two


def test_number_is_negative():
    assert power_of_two(-1) is False


def test_number_is_zero():
    assert power_of_two(0) is False


def test_number_is_positive():
    assert power_of_two(1) is True
    assert power_of_two(2) is True
    assert power_of_two(5) is False
    assert power_of_two(6) is False
    assert power_of_two(4096) is True
    assert power_of_two(536870911) is False
    assert power_of_two(536870912) is True
    assert power_of_two(536870913) is False
