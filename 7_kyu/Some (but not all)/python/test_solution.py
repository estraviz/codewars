import pytest

from solution import some_but_not_all


basic_tests = [
    ('abcdefg&%$', str.isalpha, True),
    ('&%$=', str.isalpha, False),
    ('abcdefg', str.isalpha, False),
    ([4, 1], lambda x: x > 3, True),
    ([1, 1], lambda x: x > 3, False),
    ([4, 4], lambda x: x > 3, False),
]


@pytest.mark.parametrize(
    "seq, pred, expected", basic_tests
)
def test_basic_tests(seq, pred, expected):
    assert some_but_not_all(seq, pred) == expected


fixed_tests = [
    ('a', str.isalpha, False),
    ('', str.isalpha, False),
    (':f', str.isalpha, True),
    ('f:', str.isalpha, True),
    ([], lambda x: x > 3, False),
    ([1], lambda x: x > 3, False),
    ([1]*20, lambda x: x > 3, False),
    ([4]*20, lambda x: x > 3, False),
]


@pytest.mark.parametrize(
    "seq, pred, expected", fixed_tests
)
def test_fixed_tests(seq, pred, expected):
    assert some_but_not_all(seq, pred) == expected
