from dating_range import dating_range


def test_dating_range():
    assert dating_range(17) == "15-20"
    assert dating_range(40) == "27-66"
    assert dating_range(15) == "14-16"
    assert dating_range(35) == "24-56"
    assert dating_range(10) == "9-11"
    assert dating_range(27) == "20-40"
    assert dating_range(5) == "4-5"
