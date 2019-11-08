from capitalize import capitalize


def test_capitalize():
    assert capitalize("abcdef") == ['AbCdEf', 'aBcDeF']
    assert capitalize("codewars") == ['CoDeWaRs', 'cOdEwArS']
    assert capitalize("abracadabra") == ['AbRaCaDaBrA', 'aBrAcAdAbRa']
    assert capitalize("codewarriors") == ['CoDeWaRrIoRs', 'cOdEwArRiOrS']

    output = ['InDeXiNgLeSsOnS', 'iNdExInGlEsSoNs']
    assert capitalize("indexinglessons") == output

    output = ['CoDiNgIsAfUnAcTiViTy', 'cOdInGiSaFuNaCtIvItY']
    assert capitalize("codingisafunactivity") == output
