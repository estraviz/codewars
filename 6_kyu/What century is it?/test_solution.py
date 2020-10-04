from solution import what_century


def test_what_century():
    assert what_century("2011") == "21st"
    assert what_century("2154") == "22nd"
    assert what_century("2259") == "23rd"
    assert what_century("1234") == "13th"
    assert what_century("1023") == "11th"
    assert what_century("1999") == "20th"
    assert what_century("1124") == "12th"
    assert what_century("2000") == "20th"
