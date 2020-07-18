from uni_total import uni_total


def test_should_work_with_single_etters():
    assert uni_total("a") == 97
    assert uni_total("b") == 98
    assert uni_total("c") == 99


def test_no_chars_should_return_zero():
    assert uni_total("") == 0


def test_should_work_with_multiple_letters():
    assert uni_total("aaa") == 291
    assert uni_total("abc") == 294


def test_should_work_with_sentences_and_spaces():
    assert uni_total("Mary Had A Little Lamb") == 1873
    assert uni_total("Mary had a little lamb") == 2001
    assert uni_total("CodeWars rocks") == 1370
    assert uni_total("And so does Strive") == 1661
