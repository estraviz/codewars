from solution import get_leaderboard_honor


def test_get_leaderboard():
    A = get_leaderboard_honor()

    assert len(A) == 500
    assert A[0] > 120000
    assert A[499] > 4200
