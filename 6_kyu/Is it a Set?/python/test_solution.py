import pytest

from solution import is_valid_set


@pytest.mark.parametrize(
    "quantities, shapes, colours, patterns, result",
    [
        (
            [1, 2, 3],
            ["diamond", "snake", "capsule"],
            ["green", "blue", "red"],
            ["blank", "striped", "solid"],
            True,
        ),
        (
            [1, 1, 1],
            ["capsule", "diamond", "snake"],
            ["red", "red", "red"],
            ["striped", "blank", "solid"],
            True,
        ),
        (
            [3, 1, 2],
            ["diamond", "capsule", "snake"],
            ["blue", "green", "red"],
            ["solid", "solid", "solid"],
            True,
        ),
    ],
)
def test_should_identify_valid_tests(quantities, shapes, colours, patterns, result):
    assert is_valid_set(quantities, shapes, colours, patterns) == result


@pytest.mark.parametrize(
    "quantities, shapes, colours, patterns, result",
    [
        (
            [1, 2, 1],
            ["diamond", "diamond", "snake"],
            ["blue", "red", "red"],
            ["blank", "blank", "striped"],
            False,
        ),
        (
            [1, 1, 3],
            ["diamond", "snake", "capsule"],
            ["green", "blue", "red"],
            ["blank", "striped", "solid"],
            False,
        ),
    ],
)
def test_should_identify_invalid_tests(quantities, shapes, colours, patterns, result):
    assert is_valid_set(quantities, shapes, colours, patterns) == result
