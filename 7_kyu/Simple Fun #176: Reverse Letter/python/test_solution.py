import pytest

from solution import reverse_letter


data = [
    ("krishan", "nahsirk"),
    ("ultr53o?n", "nortlu"),
    ("ab23c", "cba"),
    ("krish21an", "nahsirk"),
]


@pytest.mark.parametrize(
    "string, result", data
)
def test_reverse_letter(string, result):
    assert reverse_letter(string) == result
