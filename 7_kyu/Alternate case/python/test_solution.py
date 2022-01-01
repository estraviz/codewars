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


additional_tests = [
    ("HuMpTy DuMpTy SaT On A WaLl", "hUmPtY dUmPtY sAt oN a wAlL"),
    ("aBracaDabRa", "AbRACAdABrA"),
    ("Hickory DICKORY dock", "hICKORY dickory DOCK"),
    ("Jack JUMPED over THE CaNdLeStIcK", "jACK jumped OVER the cAnDlEsTiCk"),
]


@pytest.mark.parametrize(
    "s, expected", additional_tests
)
def test_should_alternate_case_for_additional_tests(s, expected):
    assert alternate_case(s) == expected
