import pytest
from flick_switch import flick_switch

data = [
    (['codewars', 'flick', 'code', 'wars'], [True, False, False, False]),
    (['flick', 'chocolate', 'adventure', 'sunshine'],
     [False, False, False, False]),
    (['bicycle', 'jarmony', 'flick', 'sheep', 'flick'],
     [True, True, False, False, True]),
    (['bicycle'], [True]),
    (['john, smith, susan', 'flick'], [True, False]),
    (['flick', 'flick', 'flick', 'flick', 'flick'],
     [False, True, False, True, False]),
    ([], []),
]


@pytest.mark.parametrize(
    "lst, result", data
)
def test_flick_switch(lst, result):
    assert flick_switch(lst) == result
