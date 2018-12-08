from number_to_string import number_to_string


def test_number_to_string():
    assert number_to_string(67) == '67'
    assert number_to_string(79585) == '79585'
    assert number_to_string(79585) != 79585
    assert number_to_string(1+2) == '3'
    assert number_to_string(1-2) == '-1'
