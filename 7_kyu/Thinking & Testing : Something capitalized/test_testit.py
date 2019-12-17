from testit import youtestit


def test_testit():
    assert youtestit("") == ""
    assert youtestit("a") == "A"
    assert youtestit("b") == "B"
    assert youtestit("a a") == "A A"
    assert youtestit("a b") == "A B"
    assert youtestit("a b c") == "A B C"
    assert youtestit("aa") == "aA"
    assert youtestit("ab ab") == "aB aB"
