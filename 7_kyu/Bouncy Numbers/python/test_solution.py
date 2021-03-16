import pytest

from solution import is_bouncy


data_small_numbers = [
    (0, False),
    (99, False),
    (101, True),
    (120, True),
    (122, False),
    (221, False),
]


@pytest.mark.parametrize(
    "number, result", data_small_numbers
)
def test_is_bouncy(number, result):
    assert is_bouncy(number) == result


data_large_numbers = [
    (2379, False),
    (29340, True),
    (234689, False),
    (98874, False),
    (92722983, True),
    (129347924210, True),
]


@pytest.mark.parametrize(
    "number, result", data_large_numbers
)
def test_is_bouncy(number, result):
    assert is_bouncy(number) == result
