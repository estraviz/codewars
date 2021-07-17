import pytest

from solution import correctness


tests = [
    (('M', 'F', '?'), ('M', 'F', '?'), 3),
    (('M', '?', 'M'), ('M', 'F', '?'), 2),
    (('F', 'M', 'F'), ('M', 'F', 'M'), 0),
]


@pytest.mark.parametrize(
    "bobs_decisions, expert_decisions, expected", tests
)
def test_chicken_sexing_correctness(bobs_decisions, expert_decisions, expected):
    assert correctness(bobs_decisions, expert_decisions) == expected
