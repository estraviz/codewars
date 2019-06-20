from super_size import super_size


def test_super_size():
    assert super_size(69) == 96
    assert super_size(513) == 531
    assert super_size(2017) == 7210
    assert super_size(414) == 441
    assert super_size(608719) == 987610
    assert super_size(123456789) == 987654321
    assert super_size(700000000001) == 710000000000
    assert super_size(666666) == 666666
    assert super_size(2) == 2
    assert super_size(0) == 0
