import pytest

from solution import greet

data = [
    ("Ryan", "Hello, Ryan how are you doing today?"),
    ("Shingles", "Hello, Shingles how are you doing today?"),
]

@pytest.mark.parametrize(
    "name, result", data
)
def test_greet(name, result):
    assert greet(name) == result
