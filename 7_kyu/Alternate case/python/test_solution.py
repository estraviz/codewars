import pytest

from solution import alternate_case


basic_tests = [
    ("ABC", "abc"),
    ("", ""),
    (" ", " "),
    ("Hello World", "hELLO wORLD"),
    ("cODEwARS", "CodeWars"),
    ("i LIKE MAKING KATAS VERY MUCH", "I like making katas very much"),
]


@pytest.mark.parametrize(
    "s, expected", basic_tests
)
def test_should_alternate_case_for_basic_tests(s, expected):
    assert alternate_case(s) == expected
