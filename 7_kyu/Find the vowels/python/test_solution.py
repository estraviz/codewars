import pytest

from solution import vowel_indices


data = [
    ("mmm", []),
    ("apple", [1, 5]),
    ("123456", []),
    ("UNDISARMED", [1, 4, 6, 9]),
    ("super", [2, 4]),
    ("orange", [1, 3, 6]),
    ("grapes", [3, 5]),
    ("supercalifragilisticexpialidocious",
     [2, 4, 7, 9, 12, 14, 16, 19, 21, 24, 25, 27, 29, 31, 32, 33]),
    ("123456", []),
    ("crIssUm", [3, 6]),
    ("Implied", [1, 5, 6]),
    ("rIc", [2]),
    ("bialy", [2, 3, 5]),
    ("stumpknocker", [3, 8, 11]),
    ("narboonnee", [2, 5, 6, 9, 10]),
    ("carlstadt", [2, 7]),
    ("ephodee", [1, 4, 6, 7]),
    ("spicery", [3, 5, 7]),
    ("oftenness", [1, 4, 7]),
    ("bewept", [2, 4]),
    ("capsized", [2, 5, 7]),
]


@pytest.mark.parametrize(
    "word, expected", data
)
def test_vowel_indices(word, expected):
    assert vowel_indices(word) == expected
