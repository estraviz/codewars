import pytest

from solution import valid_ISBN10


tests = [
    ('1112223339', True),
    ('048665088X', True),
    ('1293000000', True),
    ('1234554321', True),
    ('1234512345', False),
    ('1293', False),
    ('X123456788', False),
    ('ABCDEFGHIJ', False),
    ('XXXXXXXXXX', False),
]


@pytest.mark.parametrize(
    "isbn, expected", tests
)
def tests_valid_ISBN10(isbn, expected):
    assert valid_ISBN10(isbn) == expected
