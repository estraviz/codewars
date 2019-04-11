from count_bits import count_bits


def test_count_bits():
    assert count_bits(0) == 0
    assert count_bits(4) == 1
    assert count_bits(7) == 3
    assert count_bits(9) == 2
    assert count_bits(10) == 2
    assert count_bits(26) == 3
    assert count_bits(77231418) == 14
    assert count_bits(12525589) == 11
    assert count_bits(3811) == 8
    assert count_bits(392902058) == 17
    assert count_bits(1044) == 3
    assert count_bits(10030245) == 10
    assert count_bits(183337941) == 16
    assert count_bits(20478766) == 14
    assert count_bits(103021) == 9
    assert count_bits(287) == 6
    assert count_bits(115370965) == 15
    assert count_bits(31) == 5
    assert count_bits(417862) == 7
    assert count_bits(626031) == 12
    assert count_bits(89) == 4
    assert count_bits(674259) == 10
