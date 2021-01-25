import pytest

from solution import get_consecutive_items


data = [
    (90000, 0, 4),
    ("ascasdaiiiasdacasdiiiiicasdasdiiiiiiiiiiisdasdasdiii", "i", 11),
    (90000, 1, 0),
    ("ascasdaiiiasdacasdiiiiicasdasdiiiiiiiiiiisdasdasdiii", "z", 0),
]


@pytest.mark.parametrize("items, key, result", data)
def test_get_consecutive_items(items, key, result):
    assert get_consecutive_items(items, key) == result
