from find_nb import find_nb


def test_there_is_m():
    assert find_nb(4183059834009) == 2022
    assert find_nb(135440716410000) == 4824
    assert find_nb(40539911473216) == 3568
    assert find_nb(26825883955641) == 3218
    assert find_nb(9541025211025) == 2485
    assert find_nb(131443152397956) == 4788
    assert find_nb(18262169777476) == 2923
    assert find_nb(11988186060816) == 2631
    assert find_nb(826691919076) == 1348
    assert find_nb(33506766981009) == 3402
    assert find_nb(56454575667876) == 3876
    assert find_nb(603544088161) == 1246
    assert find_nb(21494785321) == 541
    assert find_nb(1025292944081385001) == 45001
    assert find_nb(10252519345963644753025) == 450010


def test_there_is_not_m():
    assert find_nb(24723578342962) == -1
    assert find_nb(41364076483082) == -1
    assert find_nb(112668204662785) == -1
    assert find_nb(79172108332642) == -1
    assert find_nb(1788719004901) == -1
    assert find_nb(1801879360282) == -1
    assert find_nb(36099801072722) == -1
    assert find_nb(171814395026) == -1
    assert find_nb(637148782657) == -1
    assert find_nb(6759306226) == -1
    assert find_nb(108806345136785) == -1
    assert find_nb(14601798712901) == -1
    assert find_nb(10252519345963644753026) == -1
    assert find_nb(102525193459636447530260) == -1
    assert find_nb(4) == -1
    assert find_nb(16) == -1
