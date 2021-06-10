import pytest

from solution import has_unique_chars


data = [
    ("abcdef", True),
    ("++-", False),
    ("  nAa", False),
]


@pytest.mark.parametrize(
    "string, expected", data
)
def test_has_unique_chars(string, expected):
    assert has_unique_chars(string) == expected
