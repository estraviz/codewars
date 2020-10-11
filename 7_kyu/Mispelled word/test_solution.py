import pytest
from solution import mispelled


@pytest.mark.parametrize(
    "word1, word2, result",
    [
        ["versed", "xersed", True],
        ["versed", "applb", False],
        ["versed", "v5rsed", True],
        ["1versed", "versed", True],
        ["versed", "versed", True],
    ],
)
def test_mispelled_with_sample_tests(word1, word2, result):
    assert mispelled(word1, word2) == result


@pytest.mark.parametrize(
    "word1, word2, result",
    [
        ["vertex", "texver", False],
        ["rpC", "oOQ", False],
        ["abcdefg", "bcd", False],
        ["bcd", "abcdefg", False],
        ["abcdefg", "dcb", False],
        ["a", "", False],
    ],
)
def test_mispelled_with_edge_tests(word1, word2, result):
    assert mispelled(word1, word2) == result
