from solution import even_or_odd


def test_even_or_odd():
    assert even_or_odd("12") == "Even is greater than Odd"
    assert even_or_odd("123") == "Odd is greater than Even"
    assert even_or_odd("112") == "Even and Odd are the same"
    assert even_or_odd("1213896664") == "Even is greater than Odd"
    assert even_or_odd("12399124677") == "Odd is greater than Even"
    assert even_or_odd("7768") == "Even and Odd are the same"
    assert even_or_odd("999988888444") == "Even is greater than Odd"
    assert even_or_odd("11111111112") == "Odd is greater than Even"
    assert even_or_odd("5578843") == "Even and Odd are the same"
    assert even_or_odd("44590258866") == "Even is greater than Odd"
    assert even_or_odd("91867") == "Odd is greater than Even"
    assert even_or_odd("7247756662") == "Even and Odd are the same"
    assert even_or_odd("834") == "Even is greater than Odd"
    assert even_or_odd("964279") == "Odd is greater than Even"
    assert even_or_odd("989899686") == "Even and Odd are the same"

    s = "124326546547649683563465"
    assert even_or_odd(s) == "Even is greater than Odd"

    s = "23646531353253475361352437562453"
    assert even_or_odd(s) == "Odd is greater than Even"

    assert even_or_odd("663333") == "Even and Odd are the same"
    assert even_or_odd("87536234") == "Even is greater than Odd"
    assert even_or_odd("9998378356372") == "Odd is greater than Even"
    assert even_or_odd("88188777752") == "Even and Odd are the same"
    assert even_or_odd("46575888345254788864") == "Even is greater than Odd"
    assert even_or_odd("35345679867564") == "Odd is greater than Even"
    assert even_or_odd("3222111") == "Even and Odd are the same"
