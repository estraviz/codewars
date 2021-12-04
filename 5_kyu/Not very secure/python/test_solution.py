import pytest

from solution import alphanumeric


tests = [
    ("hello world_", False),
    ("PassW0rd", True),
    ("     ", False),
    ("__ * __", False),
    ("&)))(((", False),
    ("43534h56jmTHHF3k", True),
    ("", False),
]


@pytest.mark.parametrize(
    "password, expected", tests
)
def test_not_very_secure_password(password, expected):
    assert alphanumeric(password) == expected
