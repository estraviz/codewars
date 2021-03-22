import pytest

from solution import solve


data = [
    ("code", "code"),
    ("CODe", "CODE"),
    ("COde", "code"),
    ("Code", "code"),
]


@pytest.mark.parametrize(
    "s, result", data
)
def test_solve(s, result):
    assert solve(s) == result
