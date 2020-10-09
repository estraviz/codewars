from solution import solution
import pytest


@pytest.mark.parametrize(
    "stones, removed",
    [["RGBRGBRGGB", 1],
     ["RGGRGBBRGRR", 3],
     ["RRRRGGGGBBBB", 9],
     ["RGBRGB", 0],
     ["BGRBBGGBRRR", 4],
     ["GBBBGGRRGRB", 4],
     ["GBRGGRBBBBRRGGGB", 7]
    ]
)
def test_solution(stones, removed):
    assert solution(stones) == removed
