from seven import seven


def test_seven():
    assert seven(477557101) == (28, 7)
    assert seven(477557102) == (47, 7)
    assert seven(2340029794923400297949) == (14, 20)
    assert seven(1603) == (7, 2)
    assert seven(371) == (35, 1)
    assert seven(1369851) == (0, 5)
    assert seven(483) == (42, 1)
    assert seven(483595) == (28, 4)
    assert seven(0) == (0, 0)
    assert seven(24318976231098675 * 7) == (0, 16)
