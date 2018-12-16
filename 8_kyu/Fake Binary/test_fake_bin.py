from fake_bin import fake_bin


def test_fake_bin():
    assert fake_bin("45385593107843568") == "01011110001100111"
    assert fake_bin("509321967506747") == "101000111101101"
    assert fake_bin("366058562030849490134388085") == \
        "011011110000101010000011011"
    assert fake_bin("15889923") == "01111100"
    assert fake_bin("800857237867") == "100111001111"
