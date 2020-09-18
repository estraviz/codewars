from solution import expression_out


def test_solution():
    assert expression_out('1 + 3') == 'One Plus Three'
    assert expression_out('2 - 10') == 'Two Minus Ten'
    assert expression_out('6 ** 9') == 'Six To The Power Of Nine'
    assert expression_out('5 = 5') == 'Five Equals Five'
    assert expression_out('7 * 4') == 'Seven Times Four'
    assert expression_out('2 / 2') == 'Two Divided By Two'
    assert expression_out('8 != 5') == 'Eight Does Not Equal Five'
