import pytest

from solution import permutations

abcd = [
    "abcd",
    "abdc",
    "acbd",
    "acdb",
    "adbc",
    "adcb",
    "bacd",
    "badc",
    "bcad",
    "bcda",
    "bdac",
    "bdca",
    "cabd",
    "cadb",
    "cbad",
    "cbda",
    "cdab",
    "cdba",
    "dabc",
    "dacb",
    "dbac",
    "dbca",
    "dcab",
    "dcba",
]

data_unique = [
    ("a", ["a"]),
    ("ab", ["ab", "ba"]),
    ("aabb", ["aabb", "abab", "abba", "baab", "baba", "bbaa"]),
    ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
    ("abcd", abcd),
    ("bcad", abcd),
    ("dcba", abcd),
]


@pytest.mark.parametrize("string, result", data_unique)
def test_unique_letters(string, result):
    assert sorted(permutations(string)) == result


data_duplicate = [
    ("aa", ["aa"]),
    ("aabb", ["aabb", "abab", "abba", "baab", "baba", "bbaa"]),
    ("aaaab", ["aaaab", "aaaba", "aabaa", "abaaa", "baaaa"]),
    ("aaaaab", ["aaaaab", "aaaaba", "aaabaa", "aabaaa", "abaaaa", "baaaaa"]),
]


@pytest.mark.parametrize("string, result", data_unique)
def test_duplicate_letters(string, result):
    assert sorted(permutations(string)) == result
