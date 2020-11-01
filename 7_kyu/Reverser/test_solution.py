import pytest
from solution import reverse


@pytest.mark.parametrize(
    "n, reversed",
    [[321, 123], [1234, 4321], [10987, 78901], [1020, 201], [12005000, 50021]],
)
def test_reverse(n, reversed):
    assert reverse(n) == reversed


words = [
    "encode",
    "decode",
    "join",
    "zfill",
    "codecs",
    "chr",
    "bytes",
    "ascii",
    "substitute",
    "template",
    "bin",
    "os",
    "sys",
    "re ",
    '"',
    "'",
    "str",
    "repr",
    "%s",
    "format",
    "type",
    "__",
    ".keys",
    "eval",
    "exec",
    "subprocess",
]


def test_does_not_include_words_in_list():
    with open("solution.py", "r") as f:
        text = f.read()
        for word in words:
            assert not (word in text)
