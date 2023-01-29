import pytest

from solution import aspect_ratio


tests = [
    (640, 480, (854, 480)),
    (960, 720, (1280, 720)),
    (1440, 1080, (1920, 1080)),
    (1920, 1440, (2560, 1440)),
]


@pytest.mark.parametrize(
    "x, y, expected", tests
)
def test_example_tests(x, y, expected):
    assert aspect_ratio(x, y) == expected
