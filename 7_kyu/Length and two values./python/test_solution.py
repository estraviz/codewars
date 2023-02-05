import pytest

from solution import alternate


tests = [
    ((5, True, False), [True, False, True, False, True]),
    ((20, "blue", "red"), ['blue', 'red', 'blue', 'red', 'blue', 'red', 'blue',
                           'red', 'blue', 'red', 'blue', 'red', 'blue', 'red',
                           'blue', 'red', 'blue', 'red', 'blue', 'red']),
    ((0, "lemons", "apples"), [])
]


@pytest.mark.parametrize(
    "data, expected", tests
)
def test_alternate(data, expected):
    n, first_value, second_value = data
    assert alternate(n, first_value, second_value) == expected
