from declare_winner import declare_winner, Fighter


def test_declare_winner():
    fighter1 = Fighter("Lew", 10, 2)
    fighter2 = Fighter("Harry", 5, 4)
    first_attacker = "Lew"
    assert declare_winner(fighter1, fighter2, first_attacker) == "Lew"

    fighter1 = Fighter("Lew", 10, 2)
    fighter2 = Fighter("Harry", 5, 4)
    first_attacker = "Harry"
    assert declare_winner(fighter1, fighter2, first_attacker) == "Harry"

    fighter1 = Fighter("Harald", 20, 5)
    fighter2 = Fighter("Harry", 5, 4)
    first_attacker = "Harry"
    assert declare_winner(fighter1, fighter2, first_attacker) == "Harald"

    fighter1 = Fighter("Harald", 20, 5)
    fighter2 = Fighter("Harry", 5, 4)
    first_attacker = "Harald"
    assert declare_winner(fighter1, fighter2, first_attacker) == "Harald"

    fighter1 = Fighter("Jerry", 30, 3)
    fighter2 = Fighter("Harald", 20, 5)
    first_attacker = "Jerry"
    assert declare_winner(fighter1, fighter2, first_attacker) == "Harald"

    fighter1 = Fighter("Jerry", 30, 3)
    fighter2 = Fighter("Harald", 20, 5)
    first_attacker = "Harald"
    assert declare_winner(fighter1, fighter2, first_attacker) == "Harald"
