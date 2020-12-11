import pytest

from solution import simpson, fun


def assertFuzzyEquals(actual, expected, msg=""):
    merr = 1e-10
    inrange = abs(actual - expected) <= merr
    if inrange is False:
        msg = "At 1e-10: Expected value must be {:.10f} but got {:.10f}"
        msg = msg.format(expected, actual)
    assert inrange is True, msg


@pytest.mark.parametrize(
    "n, expected",
    [
        (290, 1.9999999986),
        (72, 1.9999996367),
        (252, 1.9999999975),
        (40, 1.9999961668),
        (276, 1.9999999983),
        (384, 1.9999999995),
        (30, 1.9999878155),
        (238, 1.9999999969),
        (20, 1.9999372878),
    ],
)
def test_simpson(n, expected):
    assertFuzzyEquals(simpson(n), expected)
