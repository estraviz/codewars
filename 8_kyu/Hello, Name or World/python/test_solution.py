import pytest

from solution import hello


data = (
    ("John", "Hello, John!"),
    ("aLIce", "Hello, Alice!"),
    ("", "Hello, World!"),
)

@pytest.mark.parametrize("name, expected", data)
def test_basic_cases(name, expected):
    assert hello(name) == expected
