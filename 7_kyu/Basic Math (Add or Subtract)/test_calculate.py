from calculate import calculate


def test_calculate():
    assert calculate('1plus2plus3plus4') == '10'
    assert calculate('1minus2minus3minus4') == '-8'
    assert calculate('1plus2plus3minus4') == '2'
    assert calculate('1minus2plus3minus4') == '-2'
    assert calculate('1plus2minus3plus4minus5') == '-1'
