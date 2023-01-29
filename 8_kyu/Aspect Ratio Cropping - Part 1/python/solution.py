from typing import Tuple
from math import ceil


def aspect_ratio(x: int, y: int) -> Tuple[int, int]:
    return (x, y) if x == 0 or y == 0 else (ceil(16/9*y), y)
