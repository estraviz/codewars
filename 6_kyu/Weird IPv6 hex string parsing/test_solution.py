import pytest
from solution import parse_IPv6


@pytest.mark.parametrize(
    "iPv6, result",
    [
        ["1234:5678:9ABC:D00F:1111:2222:3333:4445", "10264228481217"],
        ["0000:0000:0000:0000:0000:0000:0000:0000", "00000000"],
        ["FFFF:FFFF:BBBB:CCCC:1212:AABC:0000:1111", "6060444864304"],
        ["ACDD-0101-9ABC-AAAA-FFFF-2222-FBDE-ACCC", "48242406085346"],
        ["5454rFBFDr9ABCrAA0ArFAFFr2222rFBDEr0101", "18544230558532"],
        ["F234#5678#9ABC#D00F#1111#2222#3333#4485", "24264228481221"],
    ],
)
def test_parse_IPv6(iPv6, result):
    assert parse_IPv6(iPv6) == result
