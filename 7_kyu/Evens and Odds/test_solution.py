import pytest
from solution import evens_and_odds


@pytest.mark.parametrize(
    "n, result",
    [
        [2, "10"],
        [13, "d"],
        [47, "2f"],
        [12800, "11001000000000"],
        [8172381723, "1e71ca61b"],
    ],
)
def test_evens_and_odds(n, result):
    assert evens_and_odds(n) == result
