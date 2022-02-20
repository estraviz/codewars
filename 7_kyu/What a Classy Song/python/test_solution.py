from solution import Song

mount_moose = Song('Mount Moose', 'The Snazzy Moose')


def test_for_title_and_artist():
    assert mount_moose.title == 'Mount Moose'
    assert mount_moose.artist == 'The Snazzy Moose'


def test_case_given_John_Fred_Bob_Carl_RyAn():
    assert mount_moose.how_many(['John', 'Fred', 'Bob', 'Carl', 'RyAn']) == 5


def test_case_given_JoHn_Luke_AmAndA():
    assert mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']) == 2


def test_case_given_Amanda_CalEb_CarL_Furgus():
    assert mount_moose.how_many(['Amanda', 'CalEb', 'CarL', 'Furgus']) == 2


def test_case_given_JOHN_FRED_BOB_CARL_RYAN_KATE():
    assert mount_moose.how_many(
        ['JOHN', 'FRED', 'BOB', 'CARL', 'RYAN', 'KATE']) == 1
