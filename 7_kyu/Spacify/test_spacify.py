from spacify import spacify


def test_spacify():
    assert spacify("hello world") == "h e l l o   w o r l d"
    assert spacify("12345") == "1 2 3 4 5"
    assert spacify("") == ""
    assert spacify("a") == "a"
    assert spacify("Pippi") == "P i p p i"
