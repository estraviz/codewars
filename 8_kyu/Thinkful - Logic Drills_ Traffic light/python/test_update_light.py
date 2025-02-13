from update_light import update_light


def test_update_light():
    assert update_light('green') == 'yellow'
    assert update_light('yellow') == 'red'
    assert update_light('red') == 'green'
