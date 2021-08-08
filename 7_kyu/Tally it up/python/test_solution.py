import pytest

from solution import score_to_tally


tests = [
    (3, 'c'),
    (10, 'e <br>e <br>'),
    (5, 'e <br>'),
    (1, 'a'),
    (16, 'e <br>e <br>e <br>a'),
    (28, 'e <br>e <br>e <br>e <br>e <br>c'),
    (19, 'e <br>e <br>e <br>d'),
    (9, 'e <br>d'),
    (15, 'e <br>e <br>e <br>'),
    (7, 'e <br>b'),
]


@pytest.mark.parametrize(
    "score, expected", tests
)
def test_score_to_tally(score, expected):
    assert score_to_tally(score) == expected
