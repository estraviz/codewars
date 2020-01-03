from animals import animals


def test_valid_number_of_animals():
    assert animals(72, 200) == (44, 28)
    assert animals(116, 282) == (91, 25)
    assert animals(12, 24) == (12, 0)
    assert animals(6, 24) == (0, 6)
    assert animals(344, 872) == (252, 92)
    assert animals(158, 616) == (8, 150)


def tets_invalid_number_of_animals():
    assert animals(25, 555) == "No solutions"
    assert animals(12, 25) == "No solutions"
    assert animals(54, 956) == "No solutions"
    assert animals(5455, 54956) == "No solutions"


def test_edge_cases():
    assert animals(0, 0) == (0, 0)
    assert animals(-1, -1) == "No solutions"
    assert animals(500, 0) == "No solutions"
    assert animals(0, 500) == "No solutions"
    assert animals(-45, 5) == "No solutions"
    assert animals(5, -55) == "No solutions"
