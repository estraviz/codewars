import pytest

from solution import move_ten


tests = [
    ("abz", "klj"),
    ("testcase", "docdmkco"),
    ("codewars", "mynogkbc"),
    ("exampletesthere", "ohkwzvodocdrobo"),
    ("returnofthespacecamel", "bodebxypdroczkmomkwov"),
    ("bringonthebootcamp", "lbsxqyxdrolyydmkwz"),
    ("weneedanofficedog", "goxoonkxyppsmonyq"),
]


@pytest.mark.parametrize(
    "st, expected", tests
)
def test_move_ten(st, expected):
    assert move_ten(st) == expected
