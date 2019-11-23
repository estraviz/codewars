from zipvalidate import zipvalidate


def test_these_are_valid_post_codes():
    assert zipvalidate('198328') is True
    assert zipvalidate('310003') is True
    assert zipvalidate('424000') is True


def test_these_are_invalid_post_codes():
    assert zipvalidate('12A483') is False
    assert zipvalidate('1@63') is False
    assert zipvalidate('111') is False
    assert zipvalidate('056879') is False
    assert zipvalidate('1111111') is False
