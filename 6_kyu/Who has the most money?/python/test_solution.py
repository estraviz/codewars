import pytest

from solution import Student
from solution import most_money

andy = Student("Andy", 0, 0, 2)          # 40
stephen = Student("Stephen", 0, 4, 0)    # 40
eric = Student("Eric", 8, 1, 0)          # 50
david = Student("David", 2, 0, 1)        # 30
phil = Student("Phil", 0, 2, 1)          # 40
cam = Student("Cameron", 2, 2, 0)        # 30
geoff = Student("Geoff", 0, 3, 0)        # 30

tests = [
    ([cam, geoff, phil], "Phil"),
    ([cam, geoff], "all"),
    ([geoff], "Geoff"),
    ([andy, stephen, eric, david, phil], "Eric"),
    ([cam, geoff, andy, stephen, eric, david, phil], "Eric"),
    ([andy], "Andy"),
    ([stephen], "Stephen"),
    ([david, cam, geoff], "all"),
]


@pytest.mark.parametrize(
    "students, expected", tests
)
def test_who_has_the_most_money(students, expected):
    assert most_money(students) == expected
