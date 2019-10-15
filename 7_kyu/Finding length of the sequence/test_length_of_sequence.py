from length_of_sequence import length_of_sequence


def test_two_elements_in_array():
    assert length_of_sequence([1, 1], 1) == 2


def test_number_in_the_boundaries():
    assert length_of_sequence([1, 2, 3, 1], 1) == 4


def test_element_missing_in_the_array():
    assert length_of_sequence([-7, 5, 0, 2, 9, 5], 10) == 0


def test_normal_tests():
    assert length_of_sequence([-7, 5, 0, 2, 9, 5], 5) == 5
    assert length_of_sequence([-7, 6, 2, -7, 4], -7) == 4
    assert length_of_sequence([0, 8, -7, 6, 1, 2, -7, 4, 8, 9], 8) == 8


def test_more_than_two_instances():
    assert length_of_sequence([-7, 3, -7, -7, 2, 1], -7) == 0
    assert length_of_sequence([-7, 3, -7, -7, 2, -7], -7) == 0
