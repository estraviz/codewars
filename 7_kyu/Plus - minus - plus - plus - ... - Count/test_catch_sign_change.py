from catch_sign_change import catch_sign_change


def test_catch_sign_change():
    assert catch_sign_change([1, 3, 4, 5]) == 0
    assert catch_sign_change([1, -3, -4, 0, 5]) == 2
    assert catch_sign_change([]) == 0
    assert catch_sign_change([-47, 84, -30, -11, -5, 74, 77]) == 3
