from nba_extrap import nba_extrap


def test_easy_breezy_tests():
    assert nba_extrap(2, 5) == 19.2
    assert nba_extrap(3, 9) == 16.0
    assert nba_extrap(16, 27) == 28.4
    assert nba_extrap(11, 19) == 27.8
    assert nba_extrap(14, 33) == 20.4
    assert nba_extrap(1, 7.5) == 6.4
    assert nba_extrap(6, 13) == 22.2


def test_notable_player_tests():
    assert nba_extrap(23.8, 34.8) == 32.8  # C.J. McCollum 1/15/17
    assert nba_extrap(29.3, 37.1) == 37.9  # Anthony Davis 1/15/17
    assert nba_extrap(20.1, 29.4) == 32.8  # Brook Lopez 1/15/17
    assert nba_extrap(19.6, 25.2) == 37.3  # Joel Embiid 1/15/17
    assert nba_extrap(25.8, 37.1) == 33.4  # LeBron James 1/15/17
    assert nba_extrap(26.3, 35.8) == 35.3  # Damian Lillard 1/15/17
    assert nba_extrap(26.0, 34.6) == 36.1  # Kevin Durant 1/15/17
    assert nba_extrap(5.6, 18.6) == 14.5   # Zaza Pachulia 1/15/17
