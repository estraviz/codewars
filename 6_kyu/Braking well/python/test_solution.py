# tests results are given with lots of decimals but tested at 1e-2
from solution import dist
from solution import speed


def test_basic_dist():
    assert dist(144, 0.3) == 311.83146449201496
    assert dist(92, 0.5) == 92.12909477605366
    assert dist(142, 0.2) == 435.94398509960854
    assert dist(96, 0.2) == 207.88764299467664


def test_basic_speed():
    assert speed(159, 0.8) == 153.79671564846308
    assert speed(164, 0.7) == 147.91115701756493
    assert speed(153, 0.7) == 142.14404997566152
    assert speed(88, 0.9) == 113.64202099481098
