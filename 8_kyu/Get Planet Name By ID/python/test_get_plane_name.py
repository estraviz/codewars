from get_plane_name import get_planet_name


def test_get_plane_name():
    assert get_planet_name(2) == 'Venus'
    assert get_planet_name(5) == 'Jupiter'
    assert get_planet_name(3) == 'Earth'
    assert get_planet_name(4) == 'Mars'
    assert get_planet_name(8) == 'Neptune'
    assert get_planet_name(1) == 'Mercury'
