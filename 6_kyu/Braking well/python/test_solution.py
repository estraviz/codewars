# tests results are given with lots of decimals but tested at 1e-2
from solution import dist
from solution import speed


def test_basic_dist():
    assert dist(144, 0.3) == 311.83146449201496
    assert dist(92, 0.5) == 92.12909477605366
    assert dist(142, 0.2) == 435.94398509960854
    assert dist(96, 0.2) == 207.88764299467664
    assert dist(110, 0.2) == 268.486741923711
    assert dist(118, 0.9) == 93.62174176290534
    assert dist(175, 0.6) == 249.3450665525646
    assert dist(106, 0.2) == 250.3861642818489
    assert dist(77, 0.9) == 47.29695140453248
    assert dist(152, 0.3) == 345.0961687704241


def test_basic_speed():
    assert speed(159, 0.8) == 153.79671564846308
    assert speed(164, 0.7) == 147.91115701756493
    assert speed(153, 0.7) == 142.14404997566152
    assert speed(88, 0.9) == 113.64202099481098
    assert speed(165, 0.9) == 165.11688309221347
    assert speed(138, 0.9) == 148.74600719878745
    assert speed(157, 0.4) == 113.02719899334349
    assert speed(36, 0.3) == 42.869411834085795
    assert speed(189, 0.6) == 149.93552038902996
    assert speed(142, 0.5) == 117.86079634943634
