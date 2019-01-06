from pythagorean_triple import pythagorean_triple


def test_pythagorean_triple_True():
    assert pythagorean_triple([3, 4, 5]) is True
    assert pythagorean_triple([5, 12, 13]) is True
    assert pythagorean_triple([6, 8, 10]) is True
    assert pythagorean_triple([7, 24, 25]) is True
    assert pythagorean_triple([8, 15, 17]) is True
    assert pythagorean_triple([9, 12, 15]) is True
    assert pythagorean_triple([9, 40, 41]) is True
    assert pythagorean_triple([10, 24, 26]) is True
    assert pythagorean_triple([12, 16, 20]) is True
    assert pythagorean_triple([12, 16, 20]) is True
    assert pythagorean_triple([14, 48, 50]) is True
    assert pythagorean_triple([15, 20, 25]) is True
    assert pythagorean_triple([15, 36, 39]) is True
    assert pythagorean_triple([16, 30, 34]) is True
    assert pythagorean_triple([18, 24, 30]) is True
    assert pythagorean_triple([20, 21, 29]) is True
    assert pythagorean_triple([21, 28, 35]) is True
    assert pythagorean_triple([24, 32, 40]) is True
    assert pythagorean_triple([27, 36, 45]) is True
    assert pythagorean_triple([30, 40, 50]) is True


def test_pythagorean_triple_False():
    assert pythagorean_triple([70, 18, 8]) is False
    assert pythagorean_triple([50, 19, 19]) is False
    assert pythagorean_triple([44, 17, 15]) is False
    assert pythagorean_triple([33, 11, 24]) is False
    assert pythagorean_triple([69, 11, 15]) is False
    assert pythagorean_triple([77, 12, 27]) is False
    assert pythagorean_triple([35, 39, 13]) is False
    assert pythagorean_triple([90, 44, 18]) is False
    assert pythagorean_triple([31, 8, 22]) is False
    assert pythagorean_triple([22, 30, 7]) is False
    assert pythagorean_triple([94, 16, 25]) is False
    assert pythagorean_triple([84, 37, 18]) is False
    assert pythagorean_triple([84, 19, 23]) is False
    assert pythagorean_triple([9, 45, 21]) is False
    assert pythagorean_triple([61, 18, 9]) is False
    assert pythagorean_triple([93, 50, 25]) is False
    assert pythagorean_triple([10, 21, 17]) is False
    assert pythagorean_triple([65, 26, 3]) is False
    assert pythagorean_triple([39, 31, 6]) is False
