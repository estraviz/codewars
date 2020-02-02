from not_visible_cubes import not_visible_cubes


def test_not_visible_cubes():
    assert not_visible_cubes(0) == 0
    assert not_visible_cubes(1) == 0
    assert not_visible_cubes(2) == 0
    assert not_visible_cubes(3) == 1
    assert not_visible_cubes(4) == 8
    assert not_visible_cubes(5) == 27
    assert not_visible_cubes(7) == 125
    assert not_visible_cubes(12) == 1000
    assert not_visible_cubes(18) == 4096
    assert not_visible_cubes(10002) == 1000000000000
