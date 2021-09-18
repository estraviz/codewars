import pytest

from solution import loose_change


tests = [
    (29, {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}),
    (91, {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}),
    (0, {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}),
    (-2, {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}),
    (3.9, {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}),
]


@pytest.mark.parametrize(
    "cents, expected", tests
)
def test_loose_change(cents, expected):
    assert loose_change(cents) == expected
