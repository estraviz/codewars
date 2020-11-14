from largest_sum import largest_sum


def test_sample():
    assert largest_sum("72102450111111090") == 11
    assert largest_sum("123004560") == 15
    assert largest_sum("0") == 0
    assert largest_sum("4755843230") == 41
    assert largest_sum("3388049750") == 25
    assert largest_sum("3902864190") == 30
    assert largest_sum("4098611970") == 41
    assert largest_sum("5628206860") == 23
    assert largest_sum("5891002970") == 23
    assert largest_sum("0702175070") == 15
