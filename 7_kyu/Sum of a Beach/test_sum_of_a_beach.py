from sum_of_a_beach import sum_of_a_beach


def test_sum_of_a_beach():
    assert sum_of_a_beach("SanD") == 1
    assert sum_of_a_beach("sunshine") == 1
    assert sum_of_a_beach("sunsunsunsun") == 4
    assert sum_of_a_beach("123FISH321") == 1
