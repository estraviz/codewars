import pytest

from solution import last_day


@pytest.mark.parametrize(
    "year, month, result", [(2020, 11, 30), (1945, 5, 31), (2000, 2, 29), (1900, 2, 28)]
)
def test_basic(year, month, result):
    assert last_day(year, month) == result


@pytest.mark.parametrize(
    "year, month, result",
    [
        (2001, 1, 31),
        (2002, 2, 28),
        (2003, 3, 31),
        (2004, 4, 30),
        (2005, 5, 31),
        (2006, 6, 30),
        (2007, 7, 31),
        (2008, 8, 31),
        (2009, 9, 30),
        (2010, 10, 31),
        (2011, 11, 30),
        (2012, 12, 31),
    ],
)
def test_all_months(year, month, result):
    assert last_day(year, month) == result


@pytest.mark.parametrize(
    "year, month, result",
    [
        (1600, 2, 29),
        (1700, 2, 28),
        (1800, 2, 28),
        (1900, 2, 28),
        (1980, 2, 29),
        (1996, 2, 29),
        (2000, 2, 29),
        (2100, 2, 28),
    ],
)
def test_leap_years(year, month, result):
    assert last_day(year, month) == result
