from double_char import double_char


def test_double_char():
    assert double_char("String") == "SSttrriinngg"
    assert double_char("Hello World") == "HHeelllloo  WWoorrlldd"
    assert double_char("1234!_ ") == "11223344!!__  "
