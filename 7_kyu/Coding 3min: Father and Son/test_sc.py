from sc import sc


def test_sc():
    assert sc("Aab") == "Aa"
    assert sc("AabBc") == "AabB"
    assert sc("SONson") == "SONson"
    assert sc("FfAaTtHhEeRr") == "FfAaTtHhEeRr"
    assert sc("SONsonfather") == "SONson"
    assert sc("sonfather") == ""
    assert sc("DONKEYmonkey") == "ONKEYonkey"
    assert sc("monkeyDONKEY") == "onkeyONKEY"
    assert sc("BANAna") == "ANAna"
