from duck_duck_goose import duck_duck_goose


class Player:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


def test_duck_duck_goose():
    players = [Player("a"), Player("b"), Player("c"), Player("d"), Player("c"),
               Player("e"), Player("f"), Player("g"), Player("h"), Player("z")]

    assert duck_duck_goose(players, 1) == "a"
    assert duck_duck_goose(players, 3) == "c"
    assert duck_duck_goose(players, 10) == "z"
    assert duck_duck_goose(players, 20) == "z"
    assert duck_duck_goose(players, 30) == "z"
    assert duck_duck_goose(players, 18) == "g"
    assert duck_duck_goose(players, 28) == "g"
    assert duck_duck_goose(players, 12) == "b"
    assert duck_duck_goose(players, 2) == "b"
    assert duck_duck_goose(players, 7) == "f"
