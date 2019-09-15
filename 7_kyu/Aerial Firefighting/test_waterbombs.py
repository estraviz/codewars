from waterbombs import waterbombs

results1 = waterbombs("xxYxx", 3)
results2 = waterbombs("xxYxx", 1)
results3 = waterbombs("xxxxYxYx", 4)
results4 = waterbombs("xxxxxYxYx", 2)
results6 = waterbombs("Y", 4)
results7 = waterbombs("xx", 1)


def test_tiny_fires():
    assert results6 == 0
    assert results7 == 2


def test_medium_fires():
    assert results1 == 2
    assert results2 == 4


def test_big_fires():
    assert results3 == 3
    assert results4 == 5
