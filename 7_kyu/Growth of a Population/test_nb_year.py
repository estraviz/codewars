from nb_year import nb_year


def test_nb_year():
    assert nb_year(1500, 5, 100, 5000) == 15
    assert nb_year(1500000, 2.5, 10000, 2000000) == 10
    assert nb_year(1500000, 0.25, 1000, 2000000) == 94
    assert nb_year(1500000, 0.25, -1000, 2000000) == 151
    assert nb_year(1500000, 0.25, 1, 2000000) == 116
    assert nb_year(1500000, 0.0, 10000, 2000000) == 50
