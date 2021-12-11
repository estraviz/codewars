import pytest

from solution import filter_string


tests = [
    ("123", 123),
    ("a1b2c3", 123),
    ("aa1bb2cc3dd", 123),
    ("aa 112 3dd", 1123),
    ("11bb2c23c3", 112233),
]


@pytest.mark.parametrize(
    "string, expected", tests
)
def test_filter_string(string, expected):
    assert filter_string(string) == expected
