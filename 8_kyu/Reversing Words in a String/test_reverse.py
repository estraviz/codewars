from reverse import reverse


def test_reverse():
    assert reverse('I am an expert at this') == 'this at expert an am I'
    assert reverse('This is so easy') == 'easy so is This'
    assert reverse('no one cares') == 'cares one no'
