from find_GCF import find_GCF


def test_find_GCF():
    assert find_GCF(4, 6) == 2
    assert find_GCF(93, 186) == 93
    assert find_GCF(20, 5) == 5
    assert find_GCF(2, 4) == 2
    assert find_GCF(8, 20) == 4
    assert find_GCF(5, 13) == 1
    assert find_GCF(100, 100) == 100
    assert find_GCF(100, 40) == 20
    assert find_GCF(40, 100) == 20
    assert find_GCF(60, 96) == 12
