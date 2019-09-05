from scoreboard import scoreboard


def test_scoreboard():
    assert scoreboard("The score is four nil") == [4, 0]
    assert scoreboard("new score: two three") == [2, 3]
    assert scoreboard("two two") == [2, 2]
    assert scoreboard("Arsenal just conceded another goal, two nil") == [2, 0]
