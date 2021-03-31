import pytest

from solution import travel


@pytest.mark.parametrize(
    "total_time, run_time, rest_time, speed, dist",
    [
        (1000, 10, 127, 14, 1120),
        (1000, 10, 0, 10, 10000),
        (25, 50, 120, 18, 450),
    ]
)
def test_works_for_some_examples(total_time, run_time, rest_time, speed, dist):
    assert travel(total_time, run_time, rest_time, speed) == dist


@pytest.mark.parametrize(
    "total_time, run_time, rest_time, speed, dist",
    [
        (35869784, 90, 100, 5, 84954920),
        (1234567, 4, 3, 11, 7760148),
        (100000000, 21, 5, 14, 1130769276),
    ]
)
def test_works_for_big_numbers(total_time, run_time, rest_time, speed, dist):
    assert travel(total_time, run_time, rest_time, speed) == dist


@pytest.mark.parametrize(
    "total_time, run_time, rest_time, speed, dist",
    [
        (0, 100, 10, 14, 0),
        (250, 0, 5, 14, 0),
        (100, 10, 0, 14, 1400),
        (500, 100, 10, 0, 0),
    ]
)
def test_handles_zero_values(total_time, run_time, rest_time, speed, dist):
    assert travel(total_time, run_time, rest_time, speed) == dist
