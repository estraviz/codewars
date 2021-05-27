import pytest

from solution import adjacent_element_product


@pytest.mark.parametrize(
    "array, expected",
    [
        ([5, 8], 40),
        ([1, 2, 3], 6),
        ([1, 5, 10, 9], 90),
        ([4, 12, 3, 1, 5], 48),
        ([5, 1, 2, 3, 1, 4], 6),
    ]
)
def test_should_treat_arrays_with_positive_numbers(array, expected):
    assert adjacent_element_product(array) == expected


@pytest.mark.parametrize(
    "array, expected",
    [
        ([3, 6, -2, -5, 7, 3], 21),
        ([9, 5, 10, 2, 24, -1, -48], 50),
        ([5, 6, -4, 2, 3, 2, -23], 30),
        ([-23, 4, -5, 99, -27, 329, -2, 7, -921], -14),
        ([5, 1, 2, 3, 1, 4], 6),
    ]
)
def test_should_treat_both_positive_and_negative_values(array, expected):
    assert adjacent_element_product(array) == expected


@pytest.mark.parametrize(
    "array, expected",
    [
        ([1, 0, 1, 0, 1000], 0),
        ([1, 2, 3, 0], 6),
    ]
)
def test_should_treat_arrays_that_contain_zeros(array, expected):
    assert adjacent_element_product(array) == expected
