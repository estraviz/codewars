from check_password import check_password


def test_check_password():
    assert check_password("") == "not valid"
    assert check_password("password") == "not valid"
    assert check_password("P1@p") == "not valid"
    assert check_password("P1@pP1@p") == "valid"
    assert check_password("P1@pP1@pP1@pP1@pP1@pP1@p") == "not valid"
    assert check_password("Paaaaaa222!!!") == "valid"
