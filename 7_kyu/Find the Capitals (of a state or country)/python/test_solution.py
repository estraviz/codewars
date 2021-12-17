import pytest

from solution import capital


tests = [
    (
        [{'state': 'Maine', 'capital': 'Augusta'}],
        ["The capital of Maine is Augusta"]
    ),
    (
        [{'country': 'Spain', 'capital': 'Madrid'}],
        ["The capital of Spain is Madrid"]
    ),
    (
        [
            {"state": 'Maine', 'capital': 'Augusta'},
            {'country': 'Spain', "capital": "Madrid"}
        ],
        ["The capital of Maine is Augusta", "The capital of Spain is Madrid"]
    ),
]


@pytest.mark.parametrize(
    "capitals, expected", tests
)
def test_capitals(capitals, expected):
    assert capital(capitals) == expected
