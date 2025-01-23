import pytest

from solution import string_to_number

data = [
    ("1234", 1234),
    ("605", 605),
    ("1405", 1405),
    ("-7", -7),
]

@pytest.mark.parametrize(
    "s, result", data
)
def test_string_to_number(s, result):
    assert string_to_number(s) == result
