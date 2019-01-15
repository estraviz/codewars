from rps import rps


def test_player1_wins():
    assert rps('rock', 'scissors') == "Player 1 won!"
    assert rps('scissors', 'paper') == "Player 1 won!"
    assert rps('paper', 'rock') == "Player 1 won!"


def test_player2_wins():
    assert rps('scissors', 'rock') == "Player 2 won!"
    assert rps('paper', 'scissors') == "Player 2 won!"
    assert rps('rock', 'paper') == "Player 2 won!"


def test_draw():
    assert rps('rock', 'rock') == 'Draw!'
    assert rps('scissors', 'scissors') == 'Draw!'
    assert rps('paper', 'paper') == 'Draw!'
