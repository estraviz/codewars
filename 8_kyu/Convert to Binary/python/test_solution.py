import pytest

from solution import to_binary


@pytest.mark.parametrize("n, result", [(1, 1), (2, 10), (3, 11), (5, 101)])
def test_to_binary(n, result):
    assert to_binary(n) == result
