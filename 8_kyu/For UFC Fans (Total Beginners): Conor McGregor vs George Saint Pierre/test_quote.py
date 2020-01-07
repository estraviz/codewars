from quote import quote


def test_lower_quote():
    assert quote(
        'george saint pierre') == "I am not impressed by your performance."
    assert quote(
        'conor mcgregor'
    ) == "I'd like to take this chance to apologize.. To absolutely NOBODY!"


def test_title_quote():
    assert quote(
        'George Saint Pierre') == "I am not impressed by your performance."
    assert quote(
        'Conor McGregor'
    ) == "I'd like to take this chance to apologize.. To absolutely NOBODY!"
