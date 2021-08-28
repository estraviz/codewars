import pytest

from solution import validate


tests = [
    (891, False),
    (123, False),
    (1, False),
    (2121, True),
    (1230, True),
    (8675309, False),
    (4111111111111111, True),
    (26, True),
    (2626262626262626, True),
    (91, True),
    (92, False),
    (912030, True),
    (922030, False),
]


@pytest.mark.parametrize(
    "n, expected", tests
)
def test_validate(n, expected):
    assert validate(n) == expected
