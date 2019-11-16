from high import high


def test_high():
    assert high('man i need a taxi up to ubud') == 'taxi'
    assert high('what time are we climbing up the volcano') == 'volcano'
    assert high('take me to semynak') == 'semynak'
    assert high('massage yes massage yes massage') == 'massage'
    assert high('take two bintang and a dance please') == 'bintang'
