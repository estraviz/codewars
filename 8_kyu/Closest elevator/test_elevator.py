from elevator import elevator


def test_sample_tests():
    assert elevator(0, 1, 0) == "left"
    assert elevator(0, 1, 1) == "right"
    assert elevator(0, 1, 2) == "right"
    assert elevator(0, 0, 0) == "right"
    assert elevator(0, 2, 1) == "right"


def test_fixed_tests():
    assert elevator(0, 0, 0) == "right"
    assert elevator(0, 0, 1) == "right"
    assert elevator(0, 0, 2) == "right"
    assert elevator(0, 1, 0) == "left"
    assert elevator(0, 1, 1) == "right"
    assert elevator(0, 1, 2) == "right"
    assert elevator(0, 2, 0) == "left"
    assert elevator(0, 2, 1) == "right"
    assert elevator(0, 2, 2) == "right"
    assert elevator(1, 0, 0) == "right"
    assert elevator(1, 0, 1) == "left"
    assert elevator(1, 0, 2) == "left"
    assert elevator(1, 1, 0) == "right"
    assert elevator(1, 1, 1) == "right"
    assert elevator(1, 1, 2) == "right"
    assert elevator(1, 2, 0) == "left"
    assert elevator(1, 2, 1) == "left"
    assert elevator(1, 2, 2) == "right"
    assert elevator(2, 0, 0) == "right"
    assert elevator(2, 0, 1) == "right"
    assert elevator(2, 0, 2) == "left"
    assert elevator(2, 1, 0) == "right"
    assert elevator(2, 1, 1) == "right"
    assert elevator(2, 1, 2) == "left"
    assert elevator(2, 2, 0) == "right"
    assert elevator(2, 2, 1) == "right"
    assert elevator(2, 2, 2) == "right"
