from catch_sign_change import catch_sign_change


def test_fixed_tests():
    assert catch_sign_change([1, -3, -4, 0, 5]) == 2
    assert catch_sign_change([-47, 84, -30, -11, -5, 74, 77]) == 3
    assert catch_sign_change([-7, -7, 7, 0]) == 1
    assert catch_sign_change([1, 5, 2, -4]) == 1
    assert catch_sign_change([-8, 4, -1, 5, -3, -3, -2, -2]) == 4
    assert catch_sign_change([-2, -2, -5, -4, 5, 2, 0, 6, 0]) == 1
    assert catch_sign_change([2, 6, 3, 0, 5, -3]) == 1
    assert catch_sign_change([-3, 3]) == 1
    assert catch_sign_change([-1, 2, 2, 2, 2, -8, -1]) == 2
    assert catch_sign_change([1, -2, -7, -4, 4, -2, 0, -3, 3]) == 6
    assert catch_sign_change([3, 7, -6, 2, 3, 1, 1]) == 2
    assert catch_sign_change([13, -7, -6, 2, -1, 1, -1]) == 5


def test_fixed_tests_with_zero_changes():
    assert catch_sign_change([]) == 0
    assert catch_sign_change([0]) == 0
    assert catch_sign_change([4, 1]) == 0
    assert catch_sign_change([-1, -2, -3]) == 0
    assert catch_sign_change([1, 3, 4, 5]) == 0
