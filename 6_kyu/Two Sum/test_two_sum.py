from two_sum import two_sum


def test_two_sum():
    assert sorted(two_sum([1, 2, 3], 4)) == [0, 2]
    assert sorted(two_sum([1234, 5678, 9012], 14690)) == [1, 2]
    assert sorted(two_sum([2, 2, 3], 4)) == [0, 1]
