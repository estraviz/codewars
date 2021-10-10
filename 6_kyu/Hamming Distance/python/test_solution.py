import pytest

from solution import hamming


tests = [
    ("hello world", "hello tokyo", 4),
    ("a man a plan a canal", "a man a plan sobanal", 3),
    ("hamming and cheese", "Hamming and Cheese", 2),
    ("espresso", "Expresso", 2),
    ("old father, old artificer", "of my soul the uncreated ", 24),
]


@pytest.mark.parametrize(
    "a, b, expected", tests
)
def test_hamming(a, b, expected):
    assert hamming(a, b) == expected
