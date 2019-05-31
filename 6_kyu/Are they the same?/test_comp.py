from comp import comp


def test_comp():
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2) is True

    a1 = [4, 4]
    a2 = [1, 31]
    assert comp(a1, a2) is False

    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2) is False

    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2) is False

    a1 = []
    a2 = []
    assert comp(a1, a2) is True

    a1 = []
    a2 = None
    assert comp(a1, a2) is False

    a1 = [121, 144, 19, 161, 19, 144, 19, 11, 1008]
    a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2) is False

    a1 = [10000000, 100000000]
    a2 = [10000000 * 10000000, 100000000 * 100000000]
    assert comp(a1, a2) is True

    a1 = [10000001, 100000000]
    a2 = [10000000 * 10000000, 100000000 * 100000000]
    assert comp(a1, a2) is False

    a1 = [2, 2, 3]
    a2 = [4, 9, 9]
    assert comp(a1, a2) is False

    a1 = [2, 2, 3]
    a2 = [4, 4, 9]
    assert comp(a1, a2) is True

    a1 = None
    a2 = []
    assert comp(a1, a2) is False
