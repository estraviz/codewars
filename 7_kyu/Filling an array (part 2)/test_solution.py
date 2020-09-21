from solution import squares, num_range, rand_range, primes


def test_squares():
    assert squares(5) == [1, 4, 9, 16, 25]


def test_num_range():
    assert num_range(6, 3, 2) == [3, 5, 7, 9, 11, 13]


def test_rand_range():
    rands = rand_range(4, 5, 10)
    assert len(rands) == 4
    assert min(rands) >= 5
    assert max(rands) <= 10


def test_primes():
    assert primes(6) == [2, 3, 5, 7, 11, 13]
