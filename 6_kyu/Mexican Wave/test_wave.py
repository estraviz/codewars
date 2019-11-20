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
