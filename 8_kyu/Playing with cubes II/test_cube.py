from cube import Cube


def test_cube():
    c = Cube(10)
    assert c.get_side() == 10

    c = Cube()
    assert c.get_side() == 0
