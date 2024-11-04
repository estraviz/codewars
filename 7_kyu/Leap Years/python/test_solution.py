import pytest

from solution import is_leap_year


tests = [
    (2020, True),
    (2000, True),
    (2015, False),
    (2100, False),
    (2024, True),
    (2025, False),
]


@pytest.mark.parametrize(
    "year, expected", tests
)
def test_is_leap_year(year, expected):
    assert is_leap_year(year) is expected
