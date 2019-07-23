from grader import grader


def test_grader():
    assert grader(1) == "A"
    assert grader(1.01) == "F"
    assert grader(0.2) == "F"
    assert grader(0.7) == "C"
    assert grader(0.8) == "B"
    assert grader(0.9) == "A"
    assert grader(0.6) == "D"
    assert grader(0.5) == "F"
    assert grader(0) == "F"
