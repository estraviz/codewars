from potatoes import potatoes


def test_potatoes():
    assert potatoes(82, 127, 80) == 114
    assert potatoes(93, 129, 91) == 100
    assert potatoes(82, 134, 77) == 104
    assert potatoes(90, 194, 87) == 149
    assert potatoes(82, 173, 77) == 135
    assert potatoes(77, 227, 74) == 200
    assert potatoes(76, 64, 75) == 61
    assert potatoes(81, 120, 79) == 108
    assert potatoes(84, 65, 80) == 52
    assert potatoes(93, 69, 89) == 43
    assert potatoes(78, 121, 75) == 106
    assert potatoes(83, 185, 79) == 149
    assert potatoes(78, 57, 76) == 52
    assert potatoes(79, 132, 78) == 126
    assert potatoes(86, 195, 84) == 170
    assert potatoes(75, 96, 70) == 80
    assert potatoes(81, 150, 77) == 123
    assert potatoes(82, 57, 81) == 54
    assert potatoes(85, 58, 83) == 51
    assert potatoes(78, 173, 77) == 165
