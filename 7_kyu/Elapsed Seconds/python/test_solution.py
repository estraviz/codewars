import pytest
from datetime import datetime

from solution import elapsed_seconds


start = datetime(2013, 1, 1, 0, 0, 1)
end = datetime(2013, 1, 1, 0, 0, 2)
end2 = datetime(2013, 1, 1, 0, 0, 20)
end3 = datetime(2013, 1, 1, 0, 1, 20)

data = [
    (start, end, 1),
    (end, end2, 18),
    (start, end2, 19),
    (start, end3, 79),
    (end, end3, 78),
]


@pytest.mark.parametrize("start, end, result", data)
def test_elapsed_seconds(start, end, result):
    assert elapsed_seconds(start, end) == result
