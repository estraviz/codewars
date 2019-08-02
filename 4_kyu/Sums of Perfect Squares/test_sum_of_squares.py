from sum_of_squares import sum_of_squares


def test_easy_test_cases():
    assert sum_of_squares(15) == 4
    assert sum_of_squares(16) == 1
    assert sum_of_squares(17) == 2
    assert sum_of_squares(18) == 2
    assert sum_of_squares(19) == 3


def test_harder_test_cases():
    assert sum_of_squares(2017) == 2
    assert sum_of_squares(1008) == 4
    assert sum_of_squares(3456) == 3
    assert sum_of_squares(4000) == 2
    assert sum_of_squares(12321) == 1


def test_maximally_hard_test_cases():
    assert sum_of_squares(661915703) == 4
    assert sum_of_squares(999887641) == 1
    assert sum_of_squares(999950886) == 3
    assert sum_of_squares(999951173) == 2
    assert sum_of_squares(999998999) == 4
