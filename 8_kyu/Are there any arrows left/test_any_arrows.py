from any_arrows import any_arrows


def test_should_handle_empty_quiver():
    assert any_arrows([]) is False


def test_should_handle_quiver_with_undamaged_arrows():
    assert any_arrows([{'range': 5, 'damaged': False}]) is True
    assert any_arrows([{
        'range': 5,
        'damaged': False
    }, {
        'range': 15,
        'damaged': True
    }]) is True
    assert any_arrows([{
        'range': 5
    }, {
        'range': 10,
        'damaged': True
    }, {
        'damaged': True
    }]) is True


def test_should_handle_quiver_with_damaged_arrows():
    assert any_arrows([{
        'range': 10,
        'damaged': True
    }, {
        'damaged': True
    }]) is False
