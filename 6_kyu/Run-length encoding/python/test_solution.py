import pytest

from solution import run_length_encoding


tests = [
    ('', []),
    ("abc", [[1, 'a'], [1, 'b'], [1, 'c']]),
    ("aab", [[2, 'a'], [1, 'b']]),
    ("hello world!",
     [
         [1, 'h'], [1, 'e'], [2, 'l'], [1, 'o'], [1, ' '], [1, 'w'], [1, 'o'],
         [1, 'r'], [1, 'l'], [1, 'd'], [1, '!']
      ]),
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb", [[34, 'a'], [3, 'b']]),
    ("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
        [
            [12, 'W'], [1, 'B'], [12, 'W'], [3, 'B'], [24, 'W'], [1, 'B'],
            [14, 'W']
        ]
    ),
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_run_length_encoding(s, expected):
    assert run_length_encoding(s) == expected
