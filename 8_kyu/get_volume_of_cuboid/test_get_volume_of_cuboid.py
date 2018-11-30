from get_volume_of_cuboid import get_volume_of_cuboid


def test_get_volume_of_cuboid():
    assert get_volume_of_cuboid(2, 5, 6) == 60
    assert get_volume_of_cuboid(6.3, 3, 5) == 94.5
