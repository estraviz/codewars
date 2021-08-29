import pytest

from solution import prefill


tests = [
    (3, 1, [1, 1, 1]),
    (2, 'abc', ['abc', 'abc']),
    ('1', 1, [1]),
    (3, prefill(2, '2d'), [['2d', '2d'], ['2d', '2d'], ['2d', '2d']]),
]


@pytest.mark.parametrize(
    "n, v, expected", tests
)
def test_should_return_valid_values(n, v, expected):
    assert prefill(n, v) == expected


def test_should_return_error_message():
    with pytest.raises(TypeError):
        prefill('xyz', 1)
        raise TypeError("xyz is invalid")
