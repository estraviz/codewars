import pytest

from solution import ohms_law


tests = [
    ('2e-3A 1e3R', '2.0V'),
    ('5V 10e-3A', '500.0R'),
    ('1e3R 2e-3A', '2.0V'),
    ('0.005A 30V', '6000.0R'),
    ('0R 0A', '0.0V'),
    ('30V 5000R', '0.006A'),
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_ohms_law(s, expected):
    assert ohms_law(s) == expected
