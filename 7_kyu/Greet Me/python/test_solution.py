import pytest

from solution import greet

data = [
    ("riley", "Hello Riley!"),
    ("molly", "Hello Molly!"),
    ("BILLY", "Hello Billy!"),
]


@pytest.mark.parametrize("name, result", data)
def test_greet(name, result):
    assert greet(name) == result
