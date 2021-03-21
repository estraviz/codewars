from solution import in_asc_order


def test_in_asc_order():
    arr = [1, 2]
    assert in_asc_order(arr) is True

    arr = [2, 1]
    assert in_asc_order(arr) is False

    arr = [1, 2, 3]
    assert in_asc_order(arr) is True

    arr = [1, 3, 2]
    assert in_asc_order(arr) is False

    arr = [1, 4, 13, 97, 508, 1047, 20058]
    assert in_asc_order(arr) is True

    arr = [56, 98, 123, 67, 742, 1024, 32, 90969]
    assert in_asc_order(arr) is False
