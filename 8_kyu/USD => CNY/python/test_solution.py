from solution import usdcny


def test_usdcny():
    assert usdcny(15) == "101.25 Chinese Yuan"
    assert usdcny(465) == "3138.75 Chinese Yuan"
