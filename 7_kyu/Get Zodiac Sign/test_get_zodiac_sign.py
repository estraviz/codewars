from get_zodiac_sign import get_zodiac_sign


def test_get_zodiac_sign():
    assert get_zodiac_sign(10, 10) == 'Libra'
    assert get_zodiac_sign(1, 5) == 'Taurus'
    assert get_zodiac_sign(6, 9) == 'Virgo'
    assert get_zodiac_sign(25, 11) == 'Sagittarius'
