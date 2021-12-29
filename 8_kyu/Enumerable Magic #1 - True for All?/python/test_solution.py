import pytest

from solution import _all


@pytest.fixture
def greater_than_9():
    return lambda x: x > 9


@pytest.fixture
def less_than_9():
    return lambda x: x < 9


def test_greater_than_9(greater_than_9):
    assert _all((1, 2, 3, 4, 5), greater_than_9) is False
    assert _all((10, 20, 30, 40, 50), greater_than_9) is True
    assert _all((0, 20, 30, 40, 50), greater_than_9) is False


def test_less_than_9(less_than_9):
    assert _all((1, 2, 3, 4, 5), less_than_9) is True
    assert _all((10, 20, 30, 40, 50), less_than_9) is False
    assert _all((1, 2, 3, 4, 100), less_than_9) is False
