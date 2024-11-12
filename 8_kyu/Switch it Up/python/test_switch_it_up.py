from switch_it_up import switch_it_up


def test_switch_it_up():
    assert switch_it_up(0) == "Zero"
    assert switch_it_up(1) == "One"
    assert switch_it_up(2) == "Two"
    assert switch_it_up(3) == "Three"
    assert switch_it_up(4) == "Four"
    assert switch_it_up(5) == "Five"
    assert switch_it_up(6) == "Six"
    assert switch_it_up(7) == "Seven"
    assert switch_it_up(8) == "Eight"
    assert switch_it_up(9) == "Nine"
