from ship import Ship


def test_ship():
    EmptyShip = Ship(0, 0)
    assert EmptyShip.is_worth_it() is False

    Titanic = Ship(15, 10)
    assert Titanic.is_worth_it() is False

    biggerBoat = Ship(35, 20)
    assert biggerBoat.is_worth_it() is False

