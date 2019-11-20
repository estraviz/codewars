from wave import wave


def test_wave():
    result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
    assert wave("hello") == result

    result = [
        "Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs",
        "codewaRs", "codewarS"
    ]
    assert wave("codewars") == result

    result = []
    assert wave("") == result

    result = [
        "Two words", "tWo words", "twO words", "two Words", "two wOrds",
        "two woRds", "two worDs", "two wordS"
    ]
    assert wave("two words") == result

    result = [" Gap ", " gAp ", " gaP "]
    assert wave(" gap ") == result

    result = ["A       b    ", "a       B    "]
    assert wave("a       b    ") == result

    result = [
        "This is a few words", "tHis is a few words", "thIs is a few words",
        "thiS is a few words", "this Is a few words", "this iS a few words",
        "this is A few words", "this is a Few words", "this is a fEw words",
        "this is a feW words", "this is a few Words", "this is a few wOrds",
        "this is a few woRds", "this is a few worDs", "this is a few wordS"
    ]
    assert wave("this is a few words") == result
