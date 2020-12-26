import pytest

from solution import shifted_diff


@pytest.mark.parametrize(
    "first, second, n",
    [
        ("eecoff", "coffee", 4),
        ("Moose", "moose", -1),
        ("isn't", "'tisn", 2),
        ("Esham", "Esham", 0),
        (" ", " ", 0),
        ("hoop", "pooh", -1),
        ("  ", " ", -1),
        ("doomhouse", "hoodmouse", -1),
        ("123456789!@#$%^&*( )qwerty", "9!@#$%^&*( )qwerty12345678", 18),
    ],
)
def test_shifted_diff(first, second, n):
    assert shifted_diff(first, second) == n
